#!/usr/bin/env python3
"""Officiant card batch dispatcher — scans seeded tradition files for
required_officiants, generates missing officiant cards OpenAI-compatible API.

Usage:
    python3 scripts/dispatch-officiants.py [--parallel N] [--limit N] [--ids id1,id2,...]
"""
import argparse
import os
import asyncio
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LLM_CALL = ROOT / 'scripts/llm-call.py'
OFFICIANT_PROMPT = ROOT / 'scripts/seed-prompts/officiant-worker-api.md'
OFFICIANT_SCHEMA = ROOT / 'schemas/officiant.schema.md'
INDEX_PATH = ROOT / 'skills/traditions/INDEX.yaml'
SEED_DIR = ROOT / '.seed'
LOG_DIR = SEED_DIR / 'officiant-logs'
STATE_PATH = SEED_DIR / 'officiant-dispatch-state.json'

MODEL = os.environ.get('OPENAI_MODEL', 'gpt-5.5')
MAX_TOKENS = 8192
CALL_TIMEOUT = 600


# ───── scanning ───────────────────────────────────────────────

def scan_required_officiants():
    """Returns dict: officiant_id -> list of (tradition_id, category, name)."""
    needed = defaultdict(list)
    for f in (ROOT / 'skills/traditions').glob('*/*.md'):
        if f.name.startswith('_'):
            continue
        try:
            raw = f.read_text()
            m = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
            if not m:
                continue
            fm = yaml.safe_load(m.group(1))
        except Exception:
            continue
        ofs = fm.get('required_officiants') or []
        for oid in ofs:
            if oid and oid != 'none':
                needed[oid].append((
                    fm.get('id'), fm.get('category'), fm.get('name')
                ))
    return needed


def existing_officiant_ids():
    return {f.stem for f in (ROOT / 'skills/officiants').glob('*/*.md')}


# ───── prompt rendering ───────────────────────────────────────

def render_prompt(officiant_id, traditions_using):
    """Build officiant generation prompt.
    traditions_using: list of (tid, category, name) — first is primary.
    """
    primary_tid, primary_cat, primary_name = traditions_using[0]
    others = traditions_using[1:]
    others_str = ', '.join(f'{t[0]}' for t in others) if others else 'none'

    template = OFFICIANT_PROMPT.read_text()
    schema = OFFICIANT_SCHEMA.read_text()

    out = template
    subs = {
        '<OFFICIANT_ID>': officiant_id,
        '<PRIMARY_TRADITION_ID>': primary_tid,
        '<PRIMARY_TRADITION_NAME>': primary_name,
        '<PRIMARY_TRADITION_CATEGORY>': primary_cat,
        '<OTHER_TRADITIONS>': others_str,
        '<SCHEMA>': schema,
    }
    for k, v in subs.items():
        out = out.replace(k, v)
    return out


def output_path_for(officiant_id, category):
    return ROOT / f'skills/officiants/{category}/{officiant_id}.md'


# ───── HTTP worker ────────────────────────────────────────────

FATAL_PATTERNS = [
    "You've hit your usage limit",
    'Upgrade to Pro',
    'purchase more credits',
    'usage_limit',
]


def detect_fatal(log):
    return any(p in log for p in FATAL_PATTERNS)


async def _run_once(prompt_text, output_path, log_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = output_path.with_suffix(output_path.suffix + '.tmp')

    args = ['python3', str(LLM_CALL), MODEL,
            '--max-tokens', str(MAX_TOKENS),
            '--timeout', str(CALL_TIMEOUT)]

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
            return -1, 'TIMEOUT', 0

    log_text = log_path.read_text()
    size = tmp_path.stat().st_size if tmp_path.exists() else 0

    if rc == 0 and size >= 200:
        tmp_path.replace(output_path)
        return 0, log_text, size
    else:
        if tmp_path.exists():
            tmp_path.unlink()
        return rc, log_text, 0


async def generate_card(officiant_id, traditions_using, fatal_signal):
    if fatal_signal.is_set():
        return ('skipped-fatal', None)

    category = traditions_using[0][1]  # use primary tradition's category
    out_path = output_path_for(officiant_id, category)
    log_path = LOG_DIR / f'{officiant_id}.log'

    if out_path.exists():
        return ('skipped-exists', None)

    prompt = render_prompt(officiant_id, traditions_using)

    # 1 retry on transient
    for attempt in range(2):
        rc, log, size = await _run_once(prompt, out_path, log_path)
        if rc == 0 and size >= 200:
            break
        if detect_fatal(log):
            fatal_signal.set()
            return ('fatal', {'log_tail': log[-300:]})
        if attempt == 0:
            await asyncio.sleep(15)

    if rc != 0 or size < 200:
        return ('error', {'msg': f'rc={rc} size={size}', 'log_tail': log[-300:]})

    # Validate
    try:
        raw = out_path.read_text()
        m = re.match(r'^---\n(.*?)\n---\n', raw, re.DOTALL)
        if not m:
            out_path.unlink()
            return ('error', {'msg': 'no frontmatter'})
        fm = yaml.safe_load(m.group(1))
        required = {'id', 'name', 'primary_tradition', 'role_type',
                    'persona_prompt', 'required_for', 'self_replaceable'}
        missing = required - set(fm.keys() if fm else [])
        if missing:
            out_path.unlink()
            return ('error', {'msg': f'missing fields: {missing}'})
    except Exception as e:
        if out_path.exists():
            out_path.unlink()
        return ('error', {'msg': f'validation: {e}'})

    return ('ok', None)


# ───── main loop ──────────────────────────────────────────────

async def main_async(args):
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    needed = scan_required_officiants()
    existing = existing_officiant_ids()
    missing = {oid: trads for oid, trads in needed.items()
               if oid not in existing}

    if args.ids:
        wanted = set(args.ids.split(','))
        missing = {k: v for k, v in missing.items() if k in wanted}
    elif args.limit:
        sorted_keys = sorted(missing.keys(), key=lambda k: -len(missing[k]))
        missing = {k: missing[k] for k in sorted_keys[:args.limit]}

    if not missing:
        print('officiant dispatcher: nothing to do (all referenced officiants exist)')
        return 0

    print(f'officiant dispatcher: {len(missing)} cards to generate, parallel={args.parallel}')
    print(f'log dir: {LOG_DIR}')

    sem = asyncio.Semaphore(args.parallel)
    fatal_signal = asyncio.Event()
    results = {}
    t_start = time.time()

    async def gated(oid, trads):
        if fatal_signal.is_set():
            results[oid] = ('skipped-fatal', None)
            return
        async with sem:
            if fatal_signal.is_set():
                results[oid] = ('skipped-fatal', None)
                return
            t0 = time.time()
            print(f'  → {oid:42} starting (refs by {len(trads)})...', flush=True)
            status, info = await generate_card(oid, trads, fatal_signal)
            elapsed = time.time() - t0
            results[oid] = (status, info)
            mark = {'ok': '✅', 'error': '❌', 'fatal': '🛑',
                    'skipped-fatal': '⏭', 'skipped-exists': '·'}.get(status, '?')
            extra = f' — {info.get("msg","?")}' if info else ''
            print(f'  {mark} {oid:42} {elapsed:>5.0f}s{extra}', flush=True)

    await asyncio.gather(*[gated(oid, trads) for oid, trads in missing.items()])

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
        'errors': {oid: info for oid, (s, info) in results.items()
                   if s in ('error', 'fatal') and info},
        'fatal': fatal_signal.is_set(),
    }, indent=2, ensure_ascii=False))

    if fatal_signal.is_set():
        return 1
    if counts.get('error', 0) >= max(3, len(results) * 0.3):
        return 2
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parallel', type=int, default=10)
    ap.add_argument('--limit', type=int, default=None)
    ap.add_argument('--ids', type=str, default=None)
    args = ap.parse_args()
    sys.exit(asyncio.run(main_async(args)))


if __name__ == '__main__':
    main()
