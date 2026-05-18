#!/usr/bin/env python3
"""Render a tradition-seeding worker prompt for given tradition id + worker name.

Usage:
    python3 scripts/render-prompt.py <tradition_id> <worker:claude|codex|grok>

Output: rendered prompt to stdout (or to --out path).
"""
import sys
import argparse
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def render(tradition_id: str, worker: str) -> str:
    index = yaml.safe_load((ROOT / 'skills/traditions/INDEX.yaml').read_text())
    tradition = next((t for t in index['traditions'] if t['id'] == tradition_id), None)
    if tradition is None:
        sys.exit(f'tradition {tradition_id!r} not found in INDEX.yaml')

    # Try several naming patterns
    candidates = [
        ROOT / f'scripts/seed-prompts/tradition-worker-{worker}.md',
        ROOT / f'scripts/seed-prompts/tradition-{worker}.md',
    ]
    template_path = next((p for p in candidates if p.exists()), None)
    if template_path is None:
        sys.exit(f'no prompt template for worker {worker!r} (tried {candidates})')

    cat = tradition['category']
    tid = tradition['id']
    template = template_path.read_text()
    schema = (ROOT / 'schemas/tradition.schema.md').read_text()

    # Default output path depends on worker
    if worker in ('claude', 'codex', 'grok'):
        # legacy / community 3-worker: write to .seed/<id>/<worker>.md
        out_path = ROOT / f'.seed/{tid}/{worker}.md'
    elif worker in ('codex-solo', 'merge-2draft', 'merge'):
        # Phase E: write directly to canonical tradition file
        out_path = ROOT / f'skills/traditions/{cat}/{tid}.md'
    else:
        out_path = ROOT / f'.seed/{tid}/{worker}.md'

    # Embedded draft contents (for API merge prompt, since model can't read files)
    codex_draft_path = ROOT / f'skills/traditions/{cat}/{tid}.md'
    grok_draft_path = ROOT / f'.seed/{tid}/grok.md'
    codex_content = codex_draft_path.read_text() if codex_draft_path.exists() else ''
    grok_content = grok_draft_path.read_text() if grok_draft_path.exists() else ''

    subs = {
        '<TRADITION_ID>': tid,
        '<TRADITION_NAME>': tradition.get('name', ''),
        '<TRADITION_NAME_EN>': tradition.get('name_en', ''),
        '<TRADITION_CATEGORY>': cat,
        '<REF_NOTE>': tradition.get('ref_note', ''),
        '<OUTPUT_PATH>': str(out_path),
        '<CODEX_DRAFT_PATH>': str(codex_draft_path),
        '<GROK_DRAFT_PATH>': str(grok_draft_path),
        '<CODEX_DRAFT_CONTENT>': codex_content,
        '<GROK_DRAFT_CONTENT>': grok_content,
        '<CLAUDE_DRAFT>': str(ROOT / f'.seed/{tid}/claude.md'),
        '<CODEX_DRAFT>': str(ROOT / f'.seed/{tid}/codex.md'),
        '<GROK_DRAFT>': str(ROOT / f'.seed/{tid}/grok.md'),
        '<SCHEMA>': schema,
    }
    out = template
    for k, v in subs.items():
        out = out.replace(k, v)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('tradition_id')
    ap.add_argument('worker', choices=['claude', 'codex', 'grok', 'codex-solo', 'merge-2draft', 'merge', 'api', 'merge-api'])
    ap.add_argument('--out', type=Path, help='write to file instead of stdout')
    args = ap.parse_args()

    out = render(args.tradition_id, args.worker)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(out)
    else:
        sys.stdout.write(out)


if __name__ == '__main__':
    main()
