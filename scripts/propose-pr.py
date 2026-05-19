#!/usr/bin/env python3
"""propose-pr.py — turn .session/*/enrichments/ into PR-ready proposals.

Closes the PrayProMax feedback loop. When a user runs `pray-all.py` and L3
search produces a new candidate enrichment for some tradition, that finding
should benefit future users — not just sit in `.session/`. This script:

1. Scans all `.session/*/enrichments/*.md` for L3 discoveries
2. Cross-references prior `examples/*/REVIEW-grok.md` verdicts:
   - REJECTED  → SKIP (community already verified unsuitable; don't pollute upstream)
   - PARTIAL   → HOLD (needs human review before PR)
   - CONFIRMED → PROPOSE (ready to PR)
   - no review → PROPOSE (no prior assessment; flag low-confidence)
3. Writes per-enrichment PR proposal to `PR-READY/<session>_<tradition>.md`
4. Writes summary index to `PR-READY/INDEX.md`

This avoids the bad pattern of every contributor's L3 false positive becoming
an upstream PR. Instead, the community's prior grok reviews act as a filter.

Usage:
    python3 scripts/propose-pr.py [--apply]

Without --apply: writes proposals only. With --apply: currently a placeholder — prints the would-be branch name
but does not yet create branches. Future versions will apply the proposed
diff to a feature branch ready for `gh pr create`.
"""
import argparse
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SESSION_DIR = ROOT / '.session'
EXAMPLES_DIR = ROOT / 'examples'
PR_READY_DIR = ROOT / 'PR-READY'
INDEX_PATH = ROOT / 'skills/traditions/INDEX.yaml'


def load_index():
    return yaml.safe_load(INDEX_PATH.read_text())


def tradition_path(tradition_id):
    idx = load_index()
    entry = next((t for t in idx['traditions'] if t['id'] == tradition_id), None)
    if not entry:
        return None
    return ROOT / f'skills/traditions/{entry["category"]}/{tradition_id}.md'


def parse_enrichment(enrichment_path):
    raw = enrichment_path.read_text()
    m = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
    if not m:
        return None
    fm = yaml.safe_load(m.group(1))
    body = raw[m.end():]
    return {
        'tradition_id': fm.get('tradition_id'),
        'category': fm.get('category'),
        'wish_type': fm.get('wish_type'),
        'discovered_at': fm.get('discovered_at'),
        'body': body,
        'source_session': enrichment_path.parent.parent.name,
    }


def find_grok_verdict(tradition_id):
    """Look across all examples/*/REVIEW-grok.md for prior verdicts on this tid.

    Two formats supported:
    1. Explicit "verify — <tid>" header followed by "verdict:"
    2. Block-order match against sorted(enrichments/*.md) when no header
    """
    for review_path in EXAMPLES_DIR.glob('*/REVIEW-grok.md'):
        text = review_path.read_text()
        # Format 1: explicit header
        for sep in ('—', '-'):
            pattern = rf'verify\s*{sep}\s*{re.escape(tradition_id)}.*?verdict:\s*\*?\*?(\w+)'
            m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if m:
                return m.group(1).upper(), review_path
        # Format 2: block-order match
        example_dir = review_path.parent
        enrich_dir = example_dir / 'enrichments'
        if not enrich_dir.exists():
            continue
        sorted_tids = sorted(f.stem for f in enrich_dir.glob('*.md'))
        if tradition_id not in sorted_tids:
            continue
        position = sorted_tids.index(tradition_id)
        blocks = re.split(r'\n---\n', text)
        # blocks[0] is the file header; enrichment blocks start at index 1
        if position + 1 < len(blocks):
            block = blocks[position + 1]
            m = re.search(r'verdict:\s*\*?\*?(\w+)', block, re.IGNORECASE)
            if m:
                return m.group(1).upper(), review_path
    return None, None


def assess(enrichment):
    tid = enrichment['tradition_id']
    verdict, review_path = find_grok_verdict(tid)
    if verdict == 'REJECTED':
        return 'SKIP', f'prior grok REJECTED in {review_path.relative_to(ROOT)}', verdict
    if verdict == 'PARTIAL':
        return 'HOLD', f'prior grok PARTIAL in {review_path.relative_to(ROOT)}; manual review needed', verdict
    if verdict == 'CONFIRMED':
        return 'PROPOSE', f'prior grok CONFIRMED in {review_path.relative_to(ROOT)}', verdict
    return 'PROPOSE_UNVERIFIED', 'no prior grok review — propose but flag low-confidence', None


def write_pr_proposal(enrichment, decision, reason, verdict):
    tid = enrichment['tradition_id']
    sess = enrichment['source_session']
    PR_READY_DIR.mkdir(exist_ok=True)
    out = PR_READY_DIR / f'{sess}_{tid}.md'

    trad_path = tradition_path(tid)
    trad_rel = (trad_path.relative_to(ROOT) if trad_path else f'(tradition `{tid}` not in INDEX)')

    pr_md = [
        f'# PR proposal: enrich `{tid}` (wish_type `{enrichment["wish_type"]}`)',
        '',
        f'**Decision**: `{decision}` — {reason}',
        '',
        f'| field | value |',
        f'|---|---|',
        f'| tradition_id | `{tid}` |',
        f'| wish_type | `{enrichment["wish_type"]}` |',
        f'| source session | `.session/{sess}/enrichments/{tid}.md` |',
        f'| discovered_at | {enrichment["discovered_at"]} |',
        f'| prior grok verdict | `{verdict or "—"}` |',
        f'| target file | `{trad_rel}` |',
        '',
        '## Recommended action',
        '',
    ]
    if decision == 'SKIP':
        pr_md += [
            '🛑 **Do not PR.** A prior community grok review verified this',
            'enrichment is not a canonical fit for the named tradition.',
            'Opening a PR would pollute the upstream knowledge base with',
            'AI-search-derived content that has already been refuted.',
        ]
    elif decision == 'HOLD':
        pr_md += [
            '⚠️ **Manual review required.** Prior grok review returned PARTIAL —',
            'tradition exists for the cited practice but wish-type fit is unclear.',
            'A maintainer should evaluate before opening a PR.',
        ]
    elif decision == 'PROPOSE':
        pr_md += [
            '✅ **Open PR.** Prior community grok review confirmed canonical fit.',
            'Append the following to the `case_index:` block of the target file:',
            '',
            '```yaml',
            f'  - wish_type: {enrichment["wish_type"]}',
            f'    hint: <distill from search findings — see body>',
            f'    officiant: <derive from search findings>',
            f'    primary_language: <derive>',
            '```',
            '',
            'Also append URLs from search findings to the `verification:` array.',
        ]
    else:  # PROPOSE_UNVERIFIED
        pr_md += [
            '🟡 **Propose with low-confidence flag.** No prior community review',
            'has assessed this tradition for the wish-type. Maintainer or 3-agent',
            'CI review should verify before merge. Append to `case_index:` of the',
            'target file:',
            '',
            '```yaml',
            f'  - wish_type: {enrichment["wish_type"]}',
            f'    hint: <distill from search findings — see body>',
            f'    officiant: <derive from search findings>',
            f'    primary_language: <derive>',
            '```',
        ]
    pr_md += [
        '',
        '## Original L3 enrichment (verbatim from session)',
        '',
        enrichment['body'].strip(),
        '',
    ]
    out.write_text('\n'.join(pr_md))
    return out


def maybe_apply(decision, enrichment):
    """If --apply: create a feature branch with the proposed change.
    Currently a placeholder — generates the branch name only.
    Real implementation would parse the proposed yaml fragment from the
    enrichment, append to the target case_index in-place, commit, and
    print the `gh pr create` command for the user.
    """
    if decision not in ('PROPOSE', 'PROPOSE_UNVERIFIED'):
        return
    tid = enrichment['tradition_id']
    short_ts = time.strftime('%Y%m%d')
    branch = f'contrib/enrich-{tid}-{short_ts}'
    print(f'    --apply: would create branch `{branch}` (not implemented yet)')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true',
                    help='also create feature branches (placeholder)')
    args = ap.parse_args()

    enrichments = list(SESSION_DIR.glob('*/enrichments/*.md'))
    print(f'scanning .session/: {len(enrichments)} enrichment file(s)')

    if not enrichments:
        print('no enrichments — nothing to propose')
        return

    PR_READY_DIR.mkdir(exist_ok=True)
    counts = defaultdict(int)
    written = []
    for ep in sorted(enrichments):
        e = parse_enrichment(ep)
        if not e:
            print(f'  skip (unparseable): {ep}')
            continue
        decision, reason, verdict = assess(e)
        counts[decision] += 1
        out = write_pr_proposal(e, decision, reason, verdict)
        written.append((decision, e['tradition_id'], out, reason))
        mark = {'SKIP': '🛑', 'HOLD': '⚠️ ', 'PROPOSE': '✅',
                'PROPOSE_UNVERIFIED': '🟡'}.get(decision, '?')
        print(f'  {mark} [{decision:18}] {e["tradition_id"]:32} — {reason}')
        if args.apply:
            maybe_apply(decision, e)

    # INDEX
    idx = ['# PR-READY proposals', '',
           f'_Generated by `scripts/propose-pr.py` at {time.strftime("%Y-%m-%d %H:%M:%S")}._', '',
           '## Summary', '']
    for d in ('PROPOSE', 'PROPOSE_UNVERIFIED', 'HOLD', 'SKIP'):
        n = counts.get(d, 0)
        if n:
            idx.append(f'- `{d}`: {n}')
    idx += ['', '## Per-enrichment proposals', '',
            '| decision | tradition | proposal | reason |',
            '|---|---|---|---|']
    for d, tid, p, reason in written:
        idx.append(f'| `{d}` | `{tid}` | [{p.name}]({p.name}) | {reason} |')
    (PR_READY_DIR / 'INDEX.md').write_text('\n'.join(idx))

    print(f'\n→ {len(written)} proposals written to {PR_READY_DIR.relative_to(ROOT)}/')
    print(f'  summary: {PR_READY_DIR.relative_to(ROOT)}/INDEX.md')


if __name__ == '__main__':
    main()
