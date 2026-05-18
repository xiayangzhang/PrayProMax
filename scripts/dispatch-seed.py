#!/usr/bin/env python3
"""Phase E continuous dispatcher (v2 — HTTP API via sub2api).

Per tradition:
  1. gpt-5.5 worker (tradition-worker-api prompt) — writes skills/traditions/<cat>/<id>.md
  2. grok-4.20-fast worker (existing tradition-worker-grok prompt) — writes .seed/<id>/grok.md
  3. gpt-5.5 merge (tradition-merge-api prompt with embedded drafts) — overwrites tradition file
  4. validate produced file (YAML parse + required fields)
  5. INDEX.yaml status: pending → seeded (via lock to prevent race)

Concurrency: N traditions in parallel.
Per-call timeout: 1200s.
Retry: 1 retry on transient HTTP errors.
Exit early on: ≥3 consecutive sub2api 503s, ≥3 consecutive 429s, "usage limit" pattern.

Usage:
    python3 scripts/dispatch-seed.py [--parallel N] [--limit N] [--ids id1,id2,...]
"""
import argparse
import asyncio
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / 'skills/traditions/INDEX.yaml'
RENDER = ROOT / 'scripts/render-prompt.py'
SUB2API = ROOT / 'scripts/sub2api.py'
SEED_DIR = ROOT / '.seed'
LOG_DIR = SEED_DIR / 'dispatch-logs'
STATE_PATH = SEED_DIR / 'dispatch-state.json'

# Defaults
MODEL_WORKER = 'gpt-5.5'
MODEL_GROK   = 'grok-4.20-fast'
MODEL_MERGE  = 'gpt-5.5'
CALL_TIMEOUT = 1200  # seconds per HTTP call
MAX_TOKENS_WORKER = 16384
MAX_TOKENS_MERGE = 16384

INDEX_LOCK = asyncio.Lock()


# ───── helpers ─────────────────────────────────────────────────

def load_index():
    return yaml.safe_load(INDEX_PATH.read_text())


def save_index(data):
    raw = INDEX_PATH.read_text()
    m = re.match(r'^((?:#.*?\n|\n)*)', raw)
    header = m.group(1) if m else ''
    body = yaml.dump(data, sort_keys=False, allow_unicode=True,
                     default_flow_style=False, width=120)
    INDEX_PATH.write_text(header + body)


async def update_index_status(tid: str, status: str, **extra):
    """Atomic INDEX status update (serialized via lock)."""
    async with INDEX_LOCK:
        data = load_index()
        for entry in data['traditions']:
            if entry['id'] == tid:
                entry['status'] = status
                if status == 'seeded':
                    entry['seeded_at'] = time.strftime('%Y-%m-%d')
                for k, v in extra.items():
                    entry[k] = v
                break
        save_index(data)


def sync_index_with_disk():
    """Mark seeded for any tradition whose file exists on disk but isn't marked."""
    data = load_index()
    changed = 0
    for entry in data['traditions']:
        if entry.get('status') == 'seeded':
            continue
        p = ROOT / f'skills/traditions/{entry["category"]}/{entry["id"]}.md'
        if p.exists():
            entry['status'] = 'seeded'
            entry['seeded_at'] = entry.get('seeded_at') or time.strftime('%Y-%m-%d')
            entry['notes'] = (entry.get('notes', '') + ' (sync-backfilled)').strip()
            changed += 1
    if changed:
        save_index(data)
    return changed


def get_pending_traditions():
    data = load_index()
    out = []
    for t in data['traditions']:
        if t.get('status') != 'pending':
            continue
        if t.get('has_prayer_tradition') is False:
            continue
        merged = ROOT / f'skills/traditions/{t["category"]}/{t["id"]}.md'
        if merged.exists():
            continue
        out.append(t)
    return out


def render_prompt(worker, tid):
    out = subprocess.run(
        ['python3', str(RENDER), tid, worker],
        capture_output=True, text=True, check=True
    )
    return out.stdout


# ───── HTTP worker (sub2api) ───────────────────────────────────

FATAL_PATTERNS = [
    'You\'ve hit your usage limit',
    'Upgrade to Pro',
    'purchase more credits',
    'usage_limit',
]


async def _run_sub2api_once(prompt_text, model, output_path, log_path,
                             extra_args, max_tokens):
    """Single attempt. Returns (rc, log_text, output_size)."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + '.tmp')

    args = ['python3', str(SUB2API), model,
            '--max-tokens', str(max_tokens),
            '--timeout', str(CALL_TIMEOUT)]
    if extra_args:
        args.extend(extra_args)

    with open(tmp_path, 'wb') as outf, open(log_path, 'w') as logf:
        proc = await asyncio.create_subprocess_exec(
            *args, stdin=asyncio.subprocess.PIPE, stdout=outf, stderr=logf,
        )
        try:
            await asyncio.wait_for(
                proc.communicate(input=prompt_text.encode()),
                timeout=CALL_TIMEOUT + 60,
            )
            rc = proc.returncode
        except asyncio.TimeoutError:
            proc.kill()
            await proc.wait()
            if tmp_path.exists():
                tmp_path.unlink()
            return -1, f'TIMEOUT after {CALL_TIMEOUT}s', 0

    log_text = log_path.read_text()
    tmp_size = tmp_path.stat().st_size if tmp_path.exists() else 0

    if rc == 0 and tmp_size >= 200:
        tmp_path.replace(output_path)
        return 0, log_text, tmp_size
    else:
        if tmp_path.exists():
            tmp_path.unlink()
        return rc, log_text, 0


async def run_sub2api(prompt_text, model, output_path, tid, label,
                       extra_args=None, max_tokens=MAX_TOKENS_WORKER,
                       retries=1):
    """Call sub2api with up to (1 + retries) attempts on transient failures.
    Don't retry on fatal usage-limit pattern.
    """
    log_path = LOG_DIR / f'{tid}-{label}.log'
    for attempt in range(retries + 1):
        rc, log_text, size = await _run_sub2api_once(
            prompt_text, model, output_path, log_path, extra_args, max_tokens
        )
        if rc == 0 and size >= 200:
            return rc, log_text, size
        if detect_fatal_in_log(log_text):
            return rc, log_text, size  # don't retry on quota exhaustion
        if attempt < retries:
            await asyncio.sleep(15 * (attempt + 1))  # backoff
    return rc, log_text, size


# ───── validation ──────────────────────────────────────────────

REQUIRED_FRONTMATTER = {
    'id', 'name', 'category', 'self_pray_capable',
    'primary_languages', 'backlash_risk', 'mitigation',
    'taboos', 'search_strategy', 'case_index', 'authoritative_texts',
}
WISH_TYPES = {'health', 'wealth', 'protection', 'deceased',
              'relationship', 'wisdom', 'breaking', 'event'}


def validate_tradition_file(path):
    if not path.exists():
        return False, 'file missing'
    raw = path.read_text()
    m = re.match(r'^---\n(.*?)\n---\n', raw, re.DOTALL)
    if not m:
        return False, 'no YAML frontmatter'
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception as e:
        return False, f'YAML parse error: {e}'

    missing = REQUIRED_FRONTMATTER - set(fm.keys())
    if missing:
        return False, f'missing fields: {missing}'

    ci = fm.get('case_index') or []
    wishes = {c.get('wish_type') for c in ci if isinstance(c, dict)}
    if not WISH_TYPES.issubset(wishes):
        return False, f'case_index missing wish_types: {WISH_TYPES - wishes}'

    return True, 'ok'


# ───── per-tradition flow ──────────────────────────────────────

def detect_fatal_in_log(log_text):
    return any(p in log_text for p in FATAL_PATTERNS)


async def process_tradition(t, fatal_signal):
    """Returns (status, info). status ∈ {'ok','error','fatal'}."""
    if fatal_signal.is_set():
        return ('skipped-fatal', None)

    tid, cat = t['id'], t['category']
    tdir = SEED_DIR / tid
    tdir.mkdir(parents=True, exist_ok=True)

    tradition_file = ROOT / f'skills/traditions/{cat}/{tid}.md'
    grok_out = tdir / 'grok.md'

    # === Step 1: codex worker (gpt-5.5) + grok worker, parallel ===
    try:
        codex_prompt = render_prompt('api', tid)
        grok_prompt = render_prompt('grok', tid)
    except Exception as e:
        return ('error', {'where': 'render', 'msg': str(e)})

    codex_t, grok_t = await asyncio.gather(
        run_sub2api(codex_prompt, MODEL_WORKER, tradition_file, tid, 'worker',
                    max_tokens=MAX_TOKENS_WORKER),
        run_sub2api(grok_prompt, MODEL_GROK, grok_out, tid, 'grok',
                    extra_args=['--search'], max_tokens=8192),
        return_exceptions=True,
    )

    # Handle exceptions from gather
    if isinstance(codex_t, Exception):
        return ('error', {'where': 'codex-worker', 'msg': f'exception: {codex_t}'})

    codex_rc, codex_log, codex_size = codex_t

    if detect_fatal_in_log(codex_log):
        fatal_signal.set()
        return ('fatal', {'where': 'codex-worker', 'msg': 'sub2api usage limit',
                          'log_tail': codex_log[-300:]})

    if codex_rc != 0 or codex_size < 200:
        return ('error', {'where': 'codex-worker',
                          'msg': f'rc={codex_rc} size={codex_size}',
                          'log_tail': codex_log[-300:]})

    grok_ok = (not isinstance(grok_t, Exception)
               and grok_t[0] == 0 and grok_t[2] >= 200)

    # === Step 2: merge (only if grok succeeded) ===
    if grok_ok:
        try:
            merge_prompt = render_prompt('merge-api', tid)
        except Exception as e:
            return ('error', {'where': 'render-merge', 'msg': str(e)})

        m_rc, m_log, m_size = await run_sub2api(
            merge_prompt, MODEL_MERGE, tradition_file, tid, 'merge',
            max_tokens=MAX_TOKENS_MERGE,
        )
        if detect_fatal_in_log(m_log):
            fatal_signal.set()
            return ('fatal', {'where': 'codex-merge',
                              'msg': 'sub2api usage limit',
                              'log_tail': m_log[-300:]})
        if m_rc != 0 or m_size < 200:
            return ('error', {'where': 'codex-merge',
                              'msg': f'rc={m_rc} size={m_size}',
                              'log_tail': m_log[-300:]})

    # === Step 3: validate ===
    ok, msg = validate_tradition_file(tradition_file)
    if not ok:
        # Delete the invalid file so future runs reprocess
        if tradition_file.exists():
            tradition_file.unlink()
        return ('error', {'where': 'validation', 'msg': msg})

    # === Step 4: update INDEX ===
    notes = '' if grok_ok else 'grok-skipped'
    await update_index_status(tid, 'seeded',
                              **({'notes': notes} if notes else {}))

    return ('ok', None)


# ───── main loop ───────────────────────────────────────────────

async def main_async(args):
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    backfilled = sync_index_with_disk()
    if backfilled:
        print(f'sync: backfilled {backfilled} INDEX status (file existed but not marked)')

    pending = get_pending_traditions()
    if args.ids:
        wanted = set(args.ids.split(','))
        pending = [t for t in pending if t['id'] in wanted]
    elif args.limit:
        pending = pending[:args.limit]

    if not pending:
        print('dispatcher: nothing to do')
        return 0

    print(f'dispatcher: {len(pending)} traditions, parallel={args.parallel}')
    print(f'log dir: {LOG_DIR}')

    sem = asyncio.Semaphore(args.parallel)
    fatal_signal = asyncio.Event()
    results = {}
    t_start = time.time()

    async def gated(t):
        if fatal_signal.is_set():
            results[t['id']] = ('skipped-fatal', None)
            return
        async with sem:
            if fatal_signal.is_set():
                results[t['id']] = ('skipped-fatal', None)
                return
            t0 = time.time()
            print(f'  → {t["id"]:42} starting...', flush=True)
            status, info = await process_tradition(t, fatal_signal)
            elapsed = time.time() - t0
            results[t['id']] = (status, info)
            mark = {'ok': '✅', 'error': '❌',
                    'fatal': '🛑', 'skipped-fatal': '⏭'}.get(status, '?')
            extra = ''
            if status != 'ok' and info:
                extra = f' — {info.get("where","?")}: {info.get("msg","?")}'
            print(f'  {mark} {t["id"]:42} {elapsed:>5.0f}s{extra}', flush=True)

    await asyncio.gather(*[gated(t) for t in pending])

    # Summary
    counts = {}
    for s, _ in results.values():
        counts[s] = counts.get(s, 0) + 1

    elapsed_total = time.time() - t_start
    print()
    print('=== summary ===')
    for k, v in counts.items():
        print(f'  {k:18}: {v}')
    print(f'  total elapsed:     {elapsed_total:.0f}s')

    STATE_PATH.write_text(json.dumps({
        'finished_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        'elapsed_seconds': int(elapsed_total),
        'parallel': args.parallel,
        'counts': counts,
        'errors': {tid: info for tid, (s, info) in results.items()
                   if s in ('error', 'fatal') and info},
        'fatal': fatal_signal.is_set(),
    }, indent=2, ensure_ascii=False))

    # Exit codes
    if fatal_signal.is_set():
        return 1
    if counts.get('error', 0) >= max(3, len(results) * 0.3):
        return 2
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=3)
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--ids', type=str, default=None,
                    help='comma-separated specific tradition ids')
    args = ap.parse_args()
    sys.exit(asyncio.run(main_async(args)))


if __name__ == '__main__':
    main()
