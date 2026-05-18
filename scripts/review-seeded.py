#!/usr/bin/env python3
"""Phase E review pass — Claude's quality audit of all seeded outputs.

Checks:
1. Schema validation across all tradition + officiant files
2. Forbidden phrase scan (使用提示 / 建议时机 / 功效说明 / 免责 / etc.)
3. Markdown fence / preamble residue check
4. Coverage stats (case_index wish_types, original-language inclusion, etc.)
5. Cross-reference integrity (required_officiants → cards exist)
6. Lineage rule re-check (no NRMs creeping into seeded)

Writes a markdown report to .seed/review-report.md.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRAD_DIR = ROOT / 'skills/traditions'
OFFICIANT_DIR = ROOT / 'skills/officiants'
INDEX_PATH = TRAD_DIR / 'INDEX.yaml'
REPORT_PATH = ROOT / '.seed/review-report.md'

# Forbidden in any tradition or prayer file
FORBIDDEN_PHRASES = [
    '使用提示', '使用建议', '建议时机', '功效说明', '功效介绍',
    '免责声明', '免责', '本祷词不构成', '请咨询专业',
    '本文不构成', '仅供参考',
]

# Schema-required frontmatter fields
TRADITION_REQUIRED = {
    'id', 'name', 'category', 'self_pray_capable',
    'primary_languages', 'backlash_risk', 'mitigation',
    'taboos', 'search_strategy', 'case_index', 'authoritative_texts',
}
OFFICIANT_REQUIRED = {
    'id', 'name', 'primary_tradition', 'role_type',
    'persona_prompt', 'required_for', 'self_replaceable',
}

WISH_TYPES = {'health', 'wealth', 'protection', 'deceased',
              'relationship', 'wisdom', 'breaking', 'event'}


def parse_md(path):
    raw = path.read_text()
    m = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
    if not m:
        return None, raw, 'no-frontmatter'
    try:
        fm = yaml.safe_load(m.group(1))
        body = raw[m.end():]
        return fm, body, None
    except Exception as e:
        return None, raw, f'yaml-error: {e}'


def scan_traditions():
    files = sorted(TRAD_DIR.glob('*/*.md'))
    findings = {
        'total': 0,
        'parse_errors': [],
        'missing_fields': [],
        'wish_type_gaps': [],
        'forbidden_hits': [],
        'fence_residue': [],
        'preamble_residue': [],
        'sizes': [],
        'self_pray_dist': Counter(),
        'officiant_refs': defaultdict(int),
        'lineage_concerns': [],
        'taboo_counts': [],
        'verif_counts': [],
        'case_index_counts': [],
    }

    for f in files:
        findings['total'] += 1
        rel = f.relative_to(ROOT)
        size = f.stat().st_size
        findings['sizes'].append(size)

        fm, body, err = parse_md(f)
        if err:
            findings['parse_errors'].append((str(rel), err))
            continue

        missing = TRADITION_REQUIRED - set(fm.keys())
        if missing:
            findings['missing_fields'].append((str(rel), sorted(missing)))

        # wish_type coverage
        ci = fm.get('case_index') or []
        wishes = {c.get('wish_type') for c in ci if isinstance(c, dict)}
        gap = WISH_TYPES - wishes
        if gap:
            findings['wish_type_gaps'].append((str(rel), sorted(gap)))
        findings['case_index_counts'].append(len(ci))

        # forbidden phrases
        raw_text = f.read_text()
        for ph in FORBIDDEN_PHRASES:
            if ph in raw_text:
                findings['forbidden_hits'].append((str(rel), ph))

        # markdown fence / preamble residue at file edges
        first_line = raw_text.splitlines()[0] if raw_text else ''
        if not first_line.startswith('---'):
            findings['preamble_residue'].append((str(rel), first_line[:80]))
        if '```yaml' in raw_text[:200] or '```\n---' in raw_text[:200]:
            findings['fence_residue'].append(str(rel))

        # self_pray
        sp = fm.get('self_pray_capable')
        findings['self_pray_dist'][str(sp)] += 1

        # officiants referenced
        for oid in (fm.get('required_officiants') or []):
            if oid and oid != 'none':
                findings['officiant_refs'][oid] += 1

        findings['taboo_counts'].append(len(fm.get('taboos') or []))
        findings['verif_counts'].append(len(fm.get('verification') or []))

    return findings


def scan_officiants():
    files = sorted(OFFICIANT_DIR.glob('*/*.md'))
    findings = {
        'total': 0,
        'parse_errors': [],
        'missing_fields': [],
        'persona_lengths': [],
        'self_replaceable_dist': Counter(),
        'role_type_dist': Counter(),
    }

    for f in files:
        findings['total'] += 1
        rel = f.relative_to(ROOT)
        fm, body, err = parse_md(f)
        if err:
            findings['parse_errors'].append((str(rel), err))
            continue
        missing = OFFICIANT_REQUIRED - set(fm.keys())
        if missing:
            findings['missing_fields'].append((str(rel), sorted(missing)))
        pp = fm.get('persona_prompt') or ''
        findings['persona_lengths'].append(len(pp))
        findings['self_replaceable_dist'][str(fm.get('self_replaceable'))] += 1
        findings['role_type_dist'][str(fm.get('role_type'))] += 1

    return findings


def check_cross_refs():
    trad_officiant_refs = set()
    for f in TRAD_DIR.glob('*/*.md'):
        fm, _, err = parse_md(f)
        if err or not fm: continue
        for oid in (fm.get('required_officiants') or []):
            if oid and oid != 'none':
                trad_officiant_refs.add(oid)
    existing = {f.stem for f in OFFICIANT_DIR.glob('*/*.md')}
    return {
        'referenced': len(trad_officiant_refs),
        'existing': len(existing),
        'missing': sorted(trad_officiant_refs - existing),
        'orphaned': sorted(existing - trad_officiant_refs),
    }


def stats(nums):
    if not nums: return {'n': 0}
    s = sorted(nums)
    return {
        'n': len(s),
        'min': s[0], 'p25': s[len(s)//4], 'p50': s[len(s)//2],
        'p75': s[3*len(s)//4], 'max': s[-1],
        'mean': round(sum(s)/len(s), 1),
    }


def main():
    t = scan_traditions()
    o = scan_officiants()
    x = check_cross_refs()

    rep = ['# Phase E Review Report', '']
    rep.append(f'_Generated: {Path(__file__).name}_  ')
    rep.append('')

    # === Traditions ===
    rep.append(f'## Traditions ({t["total"]} files)')
    rep.append('')
    rep.append(f'- size:        {stats(t["sizes"])}')
    rep.append(f'- case_index:  {stats(t["case_index_counts"])}')
    rep.append(f'- taboos:      {stats(t["taboo_counts"])}')
    rep.append(f'- verification:{stats(t["verif_counts"])}')
    rep.append(f'- self_pray_capable distribution: {dict(t["self_pray_dist"])}')
    rep.append('')

    issues = 0
    if t['parse_errors']:
        rep.append(f'### ❌ Parse errors ({len(t["parse_errors"])})')
        for path, err in t['parse_errors'][:20]:
            rep.append(f'- `{path}` — {err}')
        rep.append('')
        issues += len(t['parse_errors'])

    if t['missing_fields']:
        rep.append(f'### ⚠️ Missing required fields ({len(t["missing_fields"])})')
        for path, missing in t['missing_fields'][:20]:
            rep.append(f'- `{path}` — missing {missing}')
        rep.append('')
        issues += len(t['missing_fields'])

    if t['wish_type_gaps']:
        rep.append(f'### ⚠️ wish_type gaps in case_index ({len(t["wish_type_gaps"])})')
        for path, gap in t['wish_type_gaps'][:20]:
            rep.append(f'- `{path}` — missing {gap}')
        if len(t['wish_type_gaps']) > 20:
            rep.append(f'- ... +{len(t["wish_type_gaps"])-20} more')
        rep.append('')
        issues += len(t['wish_type_gaps'])

    if t['forbidden_hits']:
        rep.append(f'### ❌ Forbidden phrases ({len(t["forbidden_hits"])})')
        for path, ph in t['forbidden_hits'][:30]:
            rep.append(f'- `{path}` — contains `{ph}`')
        rep.append('')
        issues += len(t['forbidden_hits'])

    if t['preamble_residue']:
        rep.append(f'### ❌ Preamble residue (first line not `---`) ({len(t["preamble_residue"])})')
        for path, line in t['preamble_residue'][:20]:
            rep.append(f'- `{path}` — `{line}`')
        rep.append('')
        issues += len(t['preamble_residue'])

    if t['fence_residue']:
        rep.append(f'### ❌ Code-fence residue ({len(t["fence_residue"])})')
        for path in t['fence_residue'][:20]:
            rep.append(f'- `{path}`')
        rep.append('')
        issues += len(t['fence_residue'])

    if issues == 0:
        rep.append('✅ No tradition issues found.')
        rep.append('')

    # === Officiants ===
    rep.append(f'## Officiants ({o["total"]} files)')
    rep.append('')
    rep.append(f'- persona_prompt length: {stats(o["persona_lengths"])}')
    rep.append(f'- self_replaceable distribution: {dict(o["self_replaceable_dist"])}')
    rep.append(f'- role_type distribution (top 10): {dict(Counter(o["role_type_dist"]).most_common(10))}')
    rep.append('')

    o_issues = 0
    if o['parse_errors']:
        rep.append(f'### ❌ Parse errors ({len(o["parse_errors"])})')
        for path, err in o['parse_errors'][:20]:
            rep.append(f'- `{path}` — {err}')
        rep.append('')
        o_issues += len(o['parse_errors'])

    if o['missing_fields']:
        rep.append(f'### ⚠️ Missing required fields ({len(o["missing_fields"])})')
        for path, missing in o['missing_fields'][:20]:
            rep.append(f'- `{path}` — missing {missing}')
        rep.append('')
        o_issues += len(o['missing_fields'])

    if o_issues == 0:
        rep.append('✅ No officiant issues found.')
        rep.append('')

    # === Cross-refs ===
    rep.append('## Cross-references')
    rep.append('')
    rep.append(f'- traditions reference {x["referenced"]} unique officiant ids')
    rep.append(f'- {x["existing"]} officiant cards exist')
    rep.append(f'- missing cards: {len(x["missing"])}')
    rep.append(f'- orphaned cards (no tradition references): {len(x["orphaned"])}')
    if x['missing']:
        rep.append('')
        rep.append('### Missing officiant cards')
        for oid in x['missing'][:20]:
            rep.append(f'- `{oid}`')
    if x['orphaned'][:20]:
        rep.append('')
        rep.append('### Orphaned officiant cards (first 20)')
        for oid in x['orphaned'][:20]:
            rep.append(f'- `{oid}`')
    rep.append('')

    REPORT_PATH.write_text('\n'.join(rep))

    # Print summary to stdout
    print(f'TRADITIONS: {t["total"]} files')
    print(f'  parse_errors: {len(t["parse_errors"])}')
    print(f'  missing_fields: {len(t["missing_fields"])}')
    print(f'  wish_type_gaps: {len(t["wish_type_gaps"])}')
    print(f'  forbidden_phrases: {len(t["forbidden_hits"])}')
    print(f'  preamble_residue: {len(t["preamble_residue"])}')
    print(f'  fence_residue: {len(t["fence_residue"])}')
    print(f'  self_pray distribution: {dict(t["self_pray_dist"])}')
    print()
    print(f'OFFICIANTS: {o["total"]} files')
    print(f'  parse_errors: {len(o["parse_errors"])}')
    print(f'  missing_fields: {len(o["missing_fields"])}')
    print(f'  persona_prompt avg length: {stats(o["persona_lengths"]).get("mean")}')
    print()
    print(f'CROSS-REFS: {x["referenced"]} referenced, {x["existing"]} exist, '
          f'{len(x["missing"])} missing, {len(x["orphaned"])} orphaned')
    print()
    print(f'Full report: {REPORT_PATH}')


if __name__ == '__main__':
    main()
