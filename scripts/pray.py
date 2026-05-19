#!/usr/bin/env python3
"""PrayProMax pray script — execute the user-facing flow end-to-end.

For each wish:
  1. classify into one of 8 wish_types
  2. auto-pick N relevant traditions (or use --traditions)
  3. draft prayer per tradition (in parallel)
  4. merge into single prayer doc
  5. judge if generalizable → extract骨架 → write to prayers/
  6. render anchors locally → write final to outputs/

Anchors NEVER enter LLM context — only used in final local rendering.

Usage:
    python3 scripts/pray.py "<wish text>" [opts]

Opts:
    --wish-type TYPE         override auto-classification
    --traditions IDS         comma-sep tradition ids (else auto-select)
    --select N               how many to auto-select (default 3)
    --anchors FILE.json      anchor key-value file (local-only)
    --output-name SLUG       output filename slug (default derived from wish)
    --no-rag-write           skip writing to prayers/ knowledge base
"""
import argparse
import os
import asyncio
import json
import re
import subprocess
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LLM_CALL = ROOT / 'scripts/llm-call.py'
INDEX_PATH = ROOT / 'skills/traditions/INDEX.yaml'
TRAD_DIR = ROOT / 'skills/traditions'
OFFICIANT_DIR = ROOT / 'skills/officiants'
PRAYERS_DIR = ROOT / 'prayers'
PRAYERS_INDEX = PRAYERS_DIR / 'INDEX.json'
OUTPUTS_DIR = ROOT / 'outputs'

MODEL = os.environ.get('OPENAI_MODEL', 'gpt-5.5')

WISH_TYPES = ['health', 'wealth', 'protection', 'deceased',
              'relationship', 'wisdom', 'breaking', 'event']


# ───── OpenAI-compatible API wrapper ──────────────────────────────────────────

async def call_gpt(prompt, max_tokens=4096, timeout=600):
    proc = await asyncio.create_subprocess_exec(
        'python3', str(LLM_CALL), MODEL,
        '--max-tokens', str(max_tokens),
        '--timeout', str(timeout),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate(input=prompt.encode())
    if proc.returncode != 0:
        raise RuntimeError(f'OpenAI-compatible API failed rc={proc.returncode}: {err.decode()[:300]}')
    return out.decode().strip()


# ───── helpers ──────────────────────────────────────────────────

def load_index():
    return yaml.safe_load(INDEX_PATH.read_text())


def parse_md(path):
    raw = path.read_text()
    m = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
    if not m:
        return None, raw
    return yaml.safe_load(m.group(1)), raw[m.end():]


def load_tradition(tid, index):
    entry = next((t for t in index['traditions'] if t['id'] == tid), None)
    if entry is None:
        raise ValueError(f'tradition {tid!r} not found')
    path = TRAD_DIR / entry['category'] / f'{tid}.md'
    fm, body = parse_md(path)
    return entry, fm, body, path.read_text()


def load_officiant(oid, category_hint=None):
    """Find officiant card by id (search all categories)."""
    candidates = list(OFFICIANT_DIR.glob(f'*/{oid}.md'))
    if not candidates:
        return None
    return parse_md(candidates[0])


# ───── pipeline steps ──────────────────────────────────────────

async def classify_wish(wish_text):
    prompt = f'''Classify this prayer wish into ONE wish_type from this exact list:
{", ".join(WISH_TYPES)}

Wish: {wish_text}

Reply with ONLY the single wish_type word, nothing else.'''
    raw = await call_gpt(prompt, max_tokens=20)
    cls = raw.strip().lower().split()[0]
    if cls not in WISH_TYPES:
        # fallback: try to extract a known wish_type
        for w in WISH_TYPES:
            if w in raw.lower():
                return w
        return 'event'  # generic fallback
    return cls


def build_traditions_summary(index, wish_type):
    """Build a compact list of seeded traditions for auto-select.
    Filter: status=seeded, has_prayer_tradition truthy.
    """
    out = []
    for t in index['traditions']:
        if t.get('status') != 'seeded':
            continue
        if t.get('has_prayer_tradition') is False:
            continue
        # quick check: tradition has a hint for this wish_type that isn't 无
        try:
            entry, fm, _, _ = load_tradition(t['id'], index)
        except Exception:
            continue
        ci = fm.get('case_index') or []
        has_method = any(
            c.get('wish_type') == wish_type and (c.get('hint') or '') != '无'
            for c in ci if isinstance(c, dict)
        )
        if not has_method:
            continue
        out.append({
            'id': t['id'],
            'name': t['name'],
            'category': t['category'],
            'ref_note': t.get('ref_note', '')[:120],
        })
    return out


async def auto_select_traditions(wish_text, wish_type, summary, n=3):
    lines = [
        f"{t['id']} [{t['category']}] {t['name']}: {t['ref_note']}"
        for t in summary
    ]
    catalog = '\n'.join(lines)
    prompt = f'''You are PrayProMax's tradition selector. Pick {n} traditions most relevant for the user's wish.

Wish type: {wish_type}
Wish: {wish_text}

Available traditions (id [category] name: ref):
{catalog}

Pick {n} that have the best alignment with the wish + offer diverse approaches (don't pick all from same category if there are good alternatives).

Reply with ONLY {n} ids, one per line, no commentary, no numbering.'''
    raw = await call_gpt(prompt, max_tokens=200)
    valid = {t['id'] for t in summary}
    picks = [line.strip() for line in raw.split('\n') if line.strip() in valid]
    return picks[:n]


async def draft_for_tradition(wish_text, wish_type, tid, index, anchor_keys):
    """Draft a prayer section for one tradition.
    Output: {tradition_id, name, category, prayer_md, used_officiants}
    """
    entry, fm, body, full_md = load_tradition(tid, index)
    officiant_ids = fm.get('required_officiants') or []
    officiant_blocks = []
    for oid in officiant_ids:
        oc = load_officiant(oid)
        if oc:
            officiant_blocks.append(f'\n=== OFFICIANT PERSONA ({oid}) ===\n' +
                                    (oc[0].get('persona_prompt') or '') +
                                    '\n')
    officiant_text = ''.join(officiant_blocks)

    anchors_hint = ', '.join(f'{{{{anchors.{k}}}}}' for k in anchor_keys[:6])
    if not anchor_keys:
        anchors_hint = '(none provided)'

    prompt = f'''You are drafting ONE section of a multi-tradition prayer document.

Tradition: {entry["name"]} ({entry["category"]}, id={tid})
User wish_type: {wish_type}
User wish: {wish_text}

Anchor placeholders available (use these — NEVER use real personal names):
{anchors_hint}

Full tradition sub-document below — follow its 通用骨架, taboos, structure exactly. Use real mantra/经文 in original language. Use anchors.<key> placeholders for any user-specific info.

{full_md}
{officiant_text}

Output ONE markdown section starting with `## <tradition name>` heading, followed by the prayer text. The prayer must:
- Follow the tradition's 结构 and 通用骨架
- Embed actual original-language mantra/经文 inline
- Use {{{{anchors.<key>}}}} for any personal data (never real names)
- Respect taboos strictly
- If officiant persona is provided, voice it in the tradition's officiant style

No preamble, no commentary, no code fences. Just the `## ...` heading followed by the prayer body.'''
    return await call_gpt(prompt, max_tokens=4096)


async def merge_sections(wish_text, wish_type, sections, tids):
    sections_combined = '\n\n'.join(sections)
    trad_list = ', '.join(tids)
    prompt = f'''Combine these tradition-specific prayer sections into one cohesive prayer document.

Rules:
- Each tradition section stays as its own ## block. DO NOT mix deities within a section.
- Preserve all `{{{{anchors.<key>}}}}` placeholders verbatim
- Preserve all original-language mantras/scriptures verbatim
- Add a top-level frontmatter (---...---) with wish_type, traditions, generated_at
- Add a brief introductory `# 祈愿: <wish summary>` heading
- No commentary, no preamble outside the file content

Wish: {wish_text}
Traditions: {trad_list}

Sections to merge:
{sections_combined}

Output the complete merged prayer document (frontmatter + body). Raw markdown, no code fences.'''
    return await call_gpt(prompt, max_tokens=8192)


async def generalize_check(prayer_text, wish_text, wish_type):
    prompt = f'''You are deciding whether the following prayer骨架 should be saved to a reusable knowledge base.

Criteria for KEEP:
- The structure can serve future users with similar (but not identical) wishes
- Removing user-specific context still leaves a useful骨架
- Not too narrowly tied to one person's unique circumstances

Criteria for DROP:
- Highly idiosyncratic to this user's specific situation
- The wish is too unique to generalize

Original wish: {wish_text}
wish_type: {wish_type}

Prayer:
{prayer_text}

Reply with EITHER:
- "KEEP" on the first line, then on subsequent lines output the abstract skeleton (keep all {{{{anchors.*}}}} placeholders, replace specific contextual mentions with generic terms or anchors)
- OR "DROP" alone on the first line (nothing else)

Be concise. No commentary.'''
    raw = await call_gpt(prompt, max_tokens=8192)
    if raw.upper().startswith('KEEP'):
        skeleton = raw.split('\n', 1)[1] if '\n' in raw else ''
        return ('KEEP', skeleton.strip())
    else:
        return ('DROP', None)


def render_anchors(text, anchors):
    """LOCAL substitution of {{anchors.<key>}} → value."""
    for key, value in (anchors or {}).items():
        text = text.replace(f'{{{{anchors.{key}}}}}', str(value))
    return text


# ───── prayers/INDEX.json maintenance ──────────────────────────

def append_to_prayers_index(entry):
    PRAYERS_DIR.mkdir(exist_ok=True)
    if PRAYERS_INDEX.exists():
        data = json.loads(PRAYERS_INDEX.read_text())
    else:
        data = {'version': 1, 'generated_at': time.strftime('%Y-%m-%d'), 'entries': []}
    data['entries'].append(entry)
    data['generated_at'] = time.strftime('%Y-%m-%d')
    PRAYERS_INDEX.write_text(json.dumps(data, indent=2, ensure_ascii=False))


# ───── main ────────────────────────────────────────────────────

def slugify(s):
    s = re.sub(r'[^\w\s-]', '', s.lower())
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:40]


async def run(wish, args):
    t0 = time.time()
    print(f'⏱  classifying wish...', flush=True)
    wish_type = args.wish_type or await classify_wish(wish)
    print(f'   wish_type: {wish_type}')

    index = load_index()

    if args.traditions:
        tids = [t.strip() for t in args.traditions.split(',')]
    else:
        print(f'⏱  building summary...', flush=True)
        summary = build_traditions_summary(index, wish_type)
        print(f'   candidate traditions: {len(summary)}')
        print(f'⏱  auto-selecting {args.select}...', flush=True)
        tids = await auto_select_traditions(wish, wish_type, summary, n=args.select)
        print(f'   selected: {tids}')

    anchors = {}
    if args.anchors and Path(args.anchors).exists():
        anchors = json.loads(Path(args.anchors).read_text())
        print(f'   anchors keys (local-only): {list(anchors.keys())}')
    anchor_keys = list(anchors.keys())

    print(f'⏱  drafting {len(tids)} sections (parallel)...', flush=True)
    sections = await asyncio.gather(*[
        draft_for_tradition(wish, wish_type, tid, index, anchor_keys) for tid in tids
    ])
    for tid, s in zip(tids, sections):
        print(f'   ✓ {tid} ({len(s)} chars)')

    print(f'⏱  merging...', flush=True)
    merged = await merge_sections(wish, wish_type, sections, tids)

    print(f'⏱  generalization check...', flush=True)
    decision, skeleton = await generalize_check(merged, wish, wish_type)
    print(f'   decision: {decision}')

    # Write outputs
    OUTPUTS_DIR.mkdir(exist_ok=True)
    slug = args.output_name or slugify(wish[:40])
    ts = time.strftime('%Y%m%d-%H%M%S')
    out_path = OUTPUTS_DIR / f'prayer-{slug}-{ts}.md'
    rendered = render_anchors(merged, anchors)
    out_path.write_text(rendered)

    if decision == 'KEEP' and not args.no_rag_write:
        rag_dir = PRAYERS_DIR / wish_type
        rag_dir.mkdir(parents=True, exist_ok=True)
        rag_id = f'{slug}-{ts}'
        rag_path = rag_dir / f'{rag_id}.md'
        rag_path.write_text(skeleton)
        append_to_prayers_index({
            'id': rag_id,
            'path': str(rag_path.relative_to(ROOT)),
            'wish_type': wish_type,
            'sub_tags': [],
            'traditions': tids,
            'source': 'traditional-synthesized',
            'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
        })

    elapsed = time.time() - t0
    print()
    print(f'✅ done in {elapsed:.0f}s')
    print(f'   final prayer (with anchors): {out_path}')
    if decision == 'KEEP' and not args.no_rag_write:
        print(f'   skeleton added to RAG:       prayers/{wish_type}/{rag_id}.md')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('wish', help='the user wish (Chinese or English)')
    ap.add_argument('--wish-type', default=None, choices=WISH_TYPES + [None])
    ap.add_argument('--traditions', default=None, help='comma-sep tradition ids')
    ap.add_argument('--select', type=int, default=3, help='auto-select N')
    ap.add_argument('--anchors', default=None, help='anchors JSON file')
    ap.add_argument('--output-name', default=None, help='output slug')
    ap.add_argument('--no-rag-write', action='store_true')
    args = ap.parse_args()
    asyncio.run(run(args.wish, args))


if __name__ == '__main__':
    main()
