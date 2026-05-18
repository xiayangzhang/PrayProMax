#!/usr/bin/env python3
"""PrayProMax — exhaustive multi-tradition pray flow with 3-tier caching.

For each of 291 seeded traditions:
  L1 (prayers/ RAG)   — already-contributed skeleton for this wish_type + tradition
  L2 (case_index)     — tradition's own hint for this wish_type
  L3 (web search)     — grok --search fallback; findings stage as PR candidates

Per-session work dir at .session/<slug>-<ts>/ supports resume.
Outputs to outputs/wish-<slug>-<ts>/ when complete.
Enrichments (L3 findings) stage to .session/<slug>-<ts>/enrichments/ for later PR.

Anchors never enter LLM context — only used in final local render.

Usage:
    python3 scripts/pray-all.py "<wish text>" [opts]

Opts:
    --wish-type TYPE     override auto-classify
    --anchors FILE.json
    --slug SLUG          session slug (else derived from wish)
    --parallel N         per-tradition parallelism (default 10)
    --resume SLUG        resume an existing session
    --skip-l3            don't do web search (L2-only mode, fast)
    --max N              cap to first N traditions (testing)
"""
import argparse
import asyncio
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SUB2API = ROOT / 'scripts/sub2api.py'
GROK_SCRIPT = Path.home() / '.claude/skills/grok-api/scripts/grok.py'
INDEX_PATH = ROOT / 'skills/traditions/INDEX.yaml'
TRAD_DIR = ROOT / 'skills/traditions'
OFFICIANT_DIR = ROOT / 'skills/officiants'
PRAYERS_DIR = ROOT / 'prayers'
PRAYERS_INDEX = PRAYERS_DIR / 'INDEX.json'
SESSION_DIR = ROOT / '.session'
OUTPUTS_DIR = ROOT / 'outputs'

MODEL = 'gpt-5.5'
GROK_MODEL = 'grok-4.20-fast'

WISH_TYPES = ['health', 'wealth', 'protection', 'deceased',
              'relationship', 'wisdom', 'breaking', 'event']

STATE_LOCK = asyncio.Lock()


# ───── sub2api / grok callers ────────────────────────────────

async def call_gpt(prompt, max_tokens=4096, timeout=600):
    proc = await asyncio.create_subprocess_exec(
        'python3', str(SUB2API), MODEL,
        '--max-tokens', str(max_tokens), '--timeout', str(timeout),
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate(input=prompt.encode())
    if proc.returncode != 0:
        raise RuntimeError(f'gpt rc={proc.returncode}: {err.decode()[:300]}')
    return out.decode().strip()


async def call_grok_search(query, max_tokens=2048):
    proc = await asyncio.create_subprocess_exec(
        'python3', str(GROK_SCRIPT),
        '--model', GROK_MODEL, '--search', '--max-tokens', str(max_tokens),
        query,
        stdin=asyncio.subprocess.DEVNULL,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(f'grok rc={proc.returncode}: {err.decode()[:300]}')
    return out.decode().strip()


# ───── tradition / officiant loading ─────────────────────────

def parse_md(path):
    raw = path.read_text()
    m = re.match(r'^---\n(.*?)\n---', raw, re.DOTALL)
    if not m:
        return None, raw
    return yaml.safe_load(m.group(1)), raw[m.end():]


def load_seeded_traditions():
    idx = yaml.safe_load(INDEX_PATH.read_text())
    return [t for t in idx['traditions'] if t.get('status') == 'seeded']


def load_tradition_full(entry):
    path = TRAD_DIR / entry['category'] / f'{entry["id"]}.md'
    if not path.exists():
        return None, None, None
    fm, body = parse_md(path)
    return fm, body, path.read_text()


def get_case_hints(fm, wish_type):
    """Return list of (hint, officiant) tuples matching wish_type."""
    out = []
    for c in (fm.get('case_index') or []):
        if isinstance(c, dict) and c.get('wish_type') == wish_type:
            hint = c.get('hint') or ''
            officiant = c.get('officiant') or 'none'
            if hint and hint != '无':
                out.append((hint, officiant))
    return out


def load_officiant(oid):
    candidates = list(OFFICIANT_DIR.glob(f'*/{oid}.md'))
    if not candidates:
        return None
    return parse_md(candidates[0])


# ───── L1 / L2 / L3 resolvers ────────────────────────────────

def l1_check(wish_type, tradition_id):
    """Return matching prayer entry from prayers/ RAG, or None."""
    if not PRAYERS_INDEX.exists():
        return None
    try:
        data = json.loads(PRAYERS_INDEX.read_text())
    except Exception:
        return None
    candidates = [
        e for e in data.get('entries', [])
        if e.get('wish_type') == wish_type
        and tradition_id in (e.get('traditions') or [])
    ]
    return candidates[0] if candidates else None


def l2_check(fm, wish_type):
    """Return list of (hint, officiant) matching wish_type."""
    return get_case_hints(fm, wish_type)


async def l3_search(tradition_entry, wish_text, wish_type):
    """Call grok with web search. Returns (findings_text, raw_response)."""
    query = (
        f'Find canonical mantra, prayer, or liturgical practice from the {tradition_entry["name"]} '
        f'tradition ({tradition_entry.get("name_en","")}) for this purpose: {wish_text}. '
        f'Wish type: {wish_type}. '
        f'If a fixed prayer / mantra / liturgy exists, provide: (1) name of the prayer, '
        f'(2) original-language text or precise reference, (3) source URL. '
        f'If the tradition genuinely has no fixed prayer for this purpose, say so explicitly.'
    )
    try:
        result = await call_grok_search(query)
        return result
    except Exception as e:
        return f'GROK_ERROR: {e}'


# ───── prompts ───────────────────────────────────────────────

async def classify_wish(wish_text):
    prompt = f'''Classify this prayer wish into ONE wish_type from this exact list:
{", ".join(WISH_TYPES)}

Wish: {wish_text}

Reply with ONLY the single wish_type word, nothing else.'''
    raw = await call_gpt(prompt, max_tokens=20)
    cls = raw.strip().lower().split()[0]
    if cls in WISH_TYPES:
        return cls
    for w in WISH_TYPES:
        if w in raw.lower():
            return w
    return 'event'


async def check_wish_safety(wish_text):
    """Pre-flight gate: refuse harmful wishes."""
    prompt = f'''Safety check on this prayer wish.

Wish: {wish_text}

Reply with EXACTLY one of:
- SAFE       — benign (for self / loved ones / general blessings)
- AMBIGUOUS  — could be interpreted multiple ways; draft cautiously
- HARMFUL    — explicitly wishes suffering, illness, death, financial ruin, relationship destruction, or curses against identifiable others — should be refused

One word only.'''
    raw = await call_gpt(prompt, max_tokens=10)
    tag = raw.strip().upper().split()[0] if raw.strip() else 'AMBIGUOUS'
    return tag if tag in ('SAFE', 'AMBIGUOUS', 'HARMFUL') else 'AMBIGUOUS'


async def draft_from_l2(entry, fm, full_md, wish_text, wish_type, anchor_keys):
    """Draft prayer section using tradition's existing case_index hints."""
    officiant_blocks = []
    for oid in (fm.get('required_officiants') or []):
        oc = load_officiant(oid)
        if oc and oc[0]:
            pp = oc[0].get('persona_prompt') or ''
            if pp:
                officiant_blocks.append(f'\n[OFFICIANT PERSONA: {oid}]\n{pp}\n')
    anchors_hint = ', '.join(f'{{{{anchors.{k}}}}}' for k in anchor_keys[:8])

    prompt = f'''Draft ONE prayer section in this specific tradition.

Tradition: {entry["name"]} ({entry["category"]}, id={entry["id"]})
Wish: {wish_text}
Wish type: {wish_type}

Anchors available (USE these placeholders — NEVER write real personal info):
{anchors_hint or "(none — write without personal info)"}

Tradition sub-document (follow its 结构, 通用骨架, taboos exactly):
{full_md}
{"".join(officiant_blocks)}

Output ONE markdown section:
- Start with `## {entry["name"]}` heading
- Follow with prayer body matching the tradition's 通用骨架 structure
- Use {{{{anchors.<key>}}}} for any user-specific info
- Respect taboos strictly (from `taboos` field)
- Do NOT mix deities from other traditions

## SIDE-EFFECT / MITIGATION RULES (mandatory)

- **Mitigation is mandatory when `backlash_risk: medium` or `high`**: embed the tradition's `mitigation` content (closing 回向 / 净化 / 谢神 / 护身咒 / 金刚萨埵心咒 / etc.) as the FINAL part of the prayer body. This is NOT a footnote or "usage tip" — it's part of the prayer itself.
- **No-harm clause**: do not draft prayers that wish suffering, illness, death, financial ruin, or relationship destruction to identifiable third parties. Default to "remove the obstacle / barrier" framing rather than "harm the source".
- **No-deprivation clause**: where wealth / longevity / success is requested, include an in-body line that explicitly does not seek to dispossess or shorten the lives of others (e.g. 「不夺他人福报、不损他人寿数」 or its tradition-appropriate analogue).
- **No quid-pro-quo / 交换 / 还愿 / 牲祭 clauses**: do NOT draft "if you grant X, I will offer / sacrifice / pay / vow Y" exchanges. Do NOT include payment schedules, animal sacrifice, soul-bond obligations, or "future-debt to deity" clauses. Frame as **至诚 supplication / dedication / praise / 回向** rather than barter. Even if the tradition historically used exchange ritual (e.g. 还愿戏 / 牲品供养), the drafted prayer must use the **non-transactional core form**, not the bargain form.
- **Initiation taboos**: if the tradition's case_index hint includes officiant-required practices and we're drafting a self-pray version, use the simplified / lay form noted in the officiant card's `self_substitution_notes` (if available), not the officiant's reserved liturgy.

## LANGUAGE RULES (critical)

**Prayer body MUST be in the tradition's primary_language (see frontmatter), NOT Chinese translation.**

Map by category (consult primary_languages in the sub-md frontmatter to confirm):
- 汉传佛教 / 道教 / 中国民俗 → Classical Chinese (文言)
- 藏传 → Tibetan (romanized OK) + Sanskrit dharani
- 印度 / 锡克 / 耆那 / 尼泊尔 → Sanskrit / Pali / Devanagari / Gurmukhi / Tamil (per tradition)
- 伊斯兰 (any sect) → Classical Arabic (romanized OK + Arabic script when available)
- 犹太教 → Biblical Hebrew + Aramaic
- 天主教（罗马 / Mozarabic / Ambrosian）→ Latin
- 东正教 → Koine Greek 或 Church Slavonic
- 科普特 / 埃塞俄比亚 → Coptic / Geʽez
- 神道 / 修验 / 日本佛教 → 古典日文 (祝詞 / 漢文訓読) + Sanskrit dharani when relevant
- 朝鲜 NRMs / 巫俗 → Hanmun / Korean as the tradition uses
- 东南亚佛教 → Pali (Thai/Khmer/Burmese transliteration)
- 非洲 diasporic → Yoruba / Kikongo / Kreyòl / Langaj per tradition
- 美洲原住民 → Lakota / Diné / Quechua / Kʼicheʼ / Nahuatl etc. per primary_languages
- 北亚萨满 → Mongol / Yakut / Buryat / Tuvan etc.
- 大洋洲 → Hawaiian / Māori / Samoan / Tongan etc.
- 西方仪式魔法 / Wicca / Hermeticism → Hebrew / Greek / Latin / Enochian per source
- 欧洲异教复兴 → Old Norse / Old Irish / Lithuanian / etc. per tradition
- 新思想 / Unity → English (its native idiom)

**Only Chinese (or user's language) allowed in these parts:**
- The user-aspiration paragraph that contains `{{{{anchors.*}}}}` placeholders
- Brief inline section heading

**All fixed mantras / scriptural recitations / formulaic prayers must appear in original — do NOT translate them. Romanization with original script alongside is acceptable.**

Output the section only — no preamble, no commentary, no code fences.'''
    return await call_gpt(prompt, max_tokens=4096)


async def draft_from_l3(entry, fm, full_md, wish_text, wish_type, anchor_keys, search_findings):
    """Draft prayer using L3 search findings (no existing case_index)."""
    officiant_blocks = []
    for oid in (fm.get('required_officiants') or []):
        oc = load_officiant(oid)
        if oc and oc[0]:
            pp = oc[0].get('persona_prompt') or ''
            if pp:
                officiant_blocks.append(f'\n[OFFICIANT PERSONA: {oid}]\n{pp}\n')
    anchors_hint = ', '.join(f'{{{{anchors.{k}}}}}' for k in anchor_keys[:8])

    prompt = f'''Draft ONE prayer section in this specific tradition, using newly-searched findings.

Tradition: {entry["name"]} ({entry["category"]}, id={entry["id"]})
Wish: {wish_text}
Wish type: {wish_type}

Anchors available (USE these — NEVER write real personal info):
{anchors_hint or "(none)"}

Tradition sub-document (existing seed):
{full_md}
{"".join(officiant_blocks)}

NEW SEARCH FINDINGS (just retrieved from web):
{search_findings}

Output ONE markdown section:
- Start with `## {entry["name"]}` heading
- Use the search findings to construct a prayer that this tradition would recognize
- If findings include a real mantra/prayer, embed it verbatim in **original language** (NOT Chinese translation)
- Use {{{{anchors.<key>}}}} placeholders for personal info
- Respect tradition's taboos
- Do NOT mix deities
- **Mitigation when backlash_risk medium/high**: embed tradition's `mitigation` as closing protective ritual (part of prayer body)
- **No-harm clause** + **No-deprivation clause**: wealth/longevity/success requests must include an in-body line that does not dispossess or harm others
- **No quid-pro-quo / 交换 / 还愿**: don't draft "if X then I'll Y" bargain prayers; use 至诚 supplication, not barter

## LANGUAGE RULE (critical)

Prayer body (mantras, scriptural recitations, fixed prayers) MUST be in the tradition's **original liturgical language** — never Chinese translation. Romanized OK alongside native script. Chinese only allowed for: (a) user-aspiration paragraph with `{{{{anchors.*}}}}`, (b) brief section heading.

Output the section only — no preamble, no commentary, no fences.
If findings turned out unusable / hallucinated / unverifiable, output literally:
NO_PRAYER_FOUND
on a single line.'''
    return await call_gpt(prompt, max_tokens=4096)


async def evaluate_l3_findings(tradition_name, search_findings):
    """Quick verification: did grok actually find a real practice?"""
    prompt = f'''Quick judge: did this web search find a genuine, verifiable fixed prayer / mantra / liturgical practice from {tradition_name}? Or was it vague / hallucinated / "tradition has no such practice"?

Search result:
{search_findings}

Reply with ONLY ONE of:
HAS_PRAYER   — clear evidence of a real fixed prayer/mantra with source
NO_PRAYER    — search confirmed tradition has nothing of the sort
UNCERTAIN    — too vague to tell

One word only.'''
    raw = await call_gpt(prompt, max_tokens=20)
    raw = raw.strip().upper()
    for tag in ('HAS_PRAYER', 'NO_PRAYER', 'UNCERTAIN'):
        if tag in raw:
            return tag
    return 'UNCERTAIN'


# ───── per-tradition driver ──────────────────────────────────

async def process_tradition(entry, wish_text, wish_type, anchor_keys,
                             session_dir, skip_l3=False):
    tid = entry['id']
    cat = entry['category']
    sect_dir = session_dir / 'sections' / cat
    sect_dir.mkdir(parents=True, exist_ok=True)
    sect_path = sect_dir / f'{tid}.md'
    enrich_dir = session_dir / 'enrichments'
    enrich_dir.mkdir(parents=True, exist_ok=True)

    # L1 — RAG
    l1 = l1_check(wish_type, tid)
    if l1:
        path = ROOT / l1['path']
        if path.exists():
            sect_path.write_text(path.read_text())
            return {'tid': tid, 'status': 'match', 'tier': 'L1',
                    'section_path': str(sect_path.relative_to(session_dir))}

    # Load tradition
    fm, body, full_md = load_tradition_full(entry)
    if not fm:
        return {'tid': tid, 'status': 'error', 'tier': '-',
                'reason': 'tradition file missing or unparseable'}

    # L2 — case_index
    l2 = l2_check(fm, wish_type)
    if l2:
        section = await draft_from_l2(entry, fm, full_md, wish_text, wish_type, anchor_keys)
        sect_path.write_text(section)
        return {'tid': tid, 'status': 'match', 'tier': 'L2',
                'section_path': str(sect_path.relative_to(session_dir)),
                'hint_count': len(l2)}

    # L3 — search fallback
    if skip_l3:
        return {'tid': tid, 'status': 'no-match', 'tier': '-',
                'reason': 'L2 hint=无 and --skip-l3'}

    findings = await l3_search(entry, wish_text, wish_type)
    judgment = await evaluate_l3_findings(entry['name'], findings)

    if judgment == 'NO_PRAYER':
        return {'tid': tid, 'status': 'no-match', 'tier': 'L3',
                'reason': 'search confirmed no practice',
                'search_summary': findings[:200]}

    if judgment == 'UNCERTAIN':
        return {'tid': tid, 'status': 'needs-confirmation', 'tier': 'L3',
                'reason': 'search returned ambiguous evidence',
                'search_summary': findings[:300]}

    # HAS_PRAYER: draft + stage enrichment
    section = await draft_from_l3(entry, fm, full_md, wish_text, wish_type,
                                   anchor_keys, findings)
    if section.strip() == 'NO_PRAYER_FOUND':
        return {'tid': tid, 'status': 'no-match', 'tier': 'L3',
                'reason': 'drafter rejected findings as unusable'}

    sect_path.write_text(section)
    # Stage enrichment for later PR
    enrich_path = enrich_dir / f'{tid}.md'
    enrich_path.write_text(f'''---
tradition_id: {tid}
category: {cat}
wish_type: {wish_type}
discovered_at: {time.strftime("%Y-%m-%d %H:%M:%S")}
proposed_change: add case_index entry for wish_type={wish_type}
---

## Search findings (from grok --search)

{findings}

## Proposed enrichment to {tid}.md case_index

Append to `case_index:`:
```yaml
  - wish_type: {wish_type}
    hint: <distill from search findings — see drafted section>
    officiant: <derive>
    primary_language: <derive>
```

## Drafted section (for reference)

{section}
''')

    return {'tid': tid, 'status': 'match', 'tier': 'L3',
            'section_path': str(sect_path.relative_to(session_dir)),
            'enrichment_path': str(enrich_path.relative_to(session_dir))}


# ───── session state ─────────────────────────────────────────

async def save_state(session_dir, state):
    async with STATE_LOCK:
        (session_dir / 'state.json').write_text(
            json.dumps(state, indent=2, ensure_ascii=False)
        )


def load_state(session_dir):
    p = session_dir / 'state.json'
    if p.exists():
        return json.loads(p.read_text())
    return None


# ───── output assembly ──────────────────────────────────────

def render_anchors(text, anchors):
    for k, v in (anchors or {}).items():
        text = text.replace(f'{{{{anchors.{k}}}}}', str(v))
    return text


async def synthesize_universal_closing(state, session_dir):
    """One gpt call after all sections: generate cross-tradition 总回向 covering
    no-harm clause + mitigations for any high/medium-risk traditions used.
    """
    matched = [r for r in state['results'] if r['status'] == 'match']
    high_risk_summaries = []
    idx = yaml.safe_load(INDEX_PATH.read_text())
    by_id = {t['id']: t for t in idx['traditions']}
    for r in matched:
        entry = by_id.get(r['tid'])
        if not entry:
            continue
        fm, _, _ = load_tradition_full(entry)
        if not fm:
            continue
        risk = (fm.get('backlash_risk') or '').lower()
        if risk in ('medium', 'high'):
            mit = (fm.get('mitigation') or '')[:150]
            high_risk_summaries.append(f'- {entry["name"]} ({risk}): {mit}')
    if not high_risk_summaries:
        return ''  # nothing special needed
    summaries = '\n'.join(high_risk_summaries[:30])
    prompt = f'''Generate one cross-tradition closing dedication paragraph (总回向 / universal closing) for a prayer session that drew on multiple traditions.

User wish: {state["wish"]}
wish_type: {state["wish_type"]}

Some of the traditions used had medium/high backlash_risk. Their mitigations:
{summaries}

Anchors available: {state.get("anchors_keys") or []}

Write ONE concise paragraph (8-18 sentences in Chinese, since user's wish is in Chinese) that:
- Functions as a cross-tradition closing dedication
- Synthesizes the mitigations without naming specific traditions
- Includes explicit **no-harm clause** (愿所求不损他人，不夺他人福报、寿数、姻缘、机运)
- Includes explicit **no quid-pro-quo / 无交换 / 无还愿债** clause (本次所祈非以交换为本，不立来日附条件之愿，不欠诸神债负)
- Includes initiation-respect clause (若以自代行高仪，乞各派师承宽恕)
- Uses {{{{anchors.beneficiary}}}} or {{{{anchors.name-1}}}} appropriately if listed
- Closes with a universal dedication to 法界有情

No preamble, no commentary. Just the paragraph (start with `## 总回向`).'''
    try:
        return await call_gpt(prompt, max_tokens=1500)
    except Exception as e:
        return f'## 总回向\n\n_(synthesis failed: {e})_'


def assemble_outputs(session_dir, state, anchors, universal_closing_text=''):
    slug = state['slug']
    ts = state['started_at'].replace(':', '').replace(' ', '-')
    out_dir = OUTPUTS_DIR / f'wish-{slug}-{ts}'
    out_dir.mkdir(parents=True, exist_ok=True)

    matched = [r for r in state['results'] if r['status'] == 'match']
    no_match = [r for r in state['results'] if r['status'] == 'no-match']
    needs_conf = [r for r in state['results'] if r['status'] == 'needs-confirmation']
    errored = [r for r in state['results'] if r['status'] == 'error']

    # Copy sections (and render anchors)
    (out_dir / 'sections').mkdir(parents=True, exist_ok=True)
    (out_dir / 'placeholders').mkdir(parents=True, exist_ok=True)
    rendered_blocks = []
    for r in matched:
        src = session_dir / r['section_path']
        if not src.exists():
            continue
        raw = src.read_text()
        rel = Path(r['section_path']).relative_to('sections')
        dst_render = out_dir / 'sections' / rel
        dst_place = out_dir / 'placeholders' / rel
        dst_render.parent.mkdir(parents=True, exist_ok=True)
        dst_place.parent.mkdir(parents=True, exist_ok=True)
        dst_place.write_text(raw)
        rendered = render_anchors(raw, anchors)
        dst_render.write_text(rendered)
        rendered_blocks.append(rendered)

    # RENDERED.md (mega)
    closing_block = ''
    if universal_closing_text:
        closing_block = '\n\n---\n\n' + render_anchors(universal_closing_text, anchors)
    rendered_md = (
        f'# 祈愿: {state["wish"]}\n\n'
        f'wish_type: {state["wish_type"]}\n\n'
        f'_Matched traditions: {len(matched)}_\n\n'
        + '\n\n---\n\n'.join(rendered_blocks)
        + closing_block
    )
    (out_dir / 'RENDERED.md').write_text(rendered_md)

    # INDEX.md
    tier_counts = Counter(r.get('tier') for r in matched)
    by_cat = {}
    for r in matched:
        cat = r['section_path'].split('/')[1] if '/' in r['section_path'] else '?'
        by_cat.setdefault(cat, []).append(r['tid'])

    idx = [f'# Wish session — {state["wish"]}', '']
    idx.append(f'- wish_type: `{state["wish_type"]}`')
    idx.append(f'- anchors keys (local-only): `{state.get("anchors_keys") or []}`')
    idx.append(f'- traditions evaluated: {len(state["results"])}')
    idx.append(f'- matched: **{len(matched)}** (L1={tier_counts.get("L1",0)}, L2={tier_counts.get("L2",0)}, L3={tier_counts.get("L3",0)})')
    idx.append(f'- no-match (confirmed absent): {len(no_match)}')
    idx.append(f'- needs-confirmation (L3 uncertain): {len(needs_conf)}')
    idx.append(f'- errored: {len(errored)}')
    idx.append('')
    idx.append('## Matched sections by category')
    for cat in sorted(by_cat):
        idx.append(f'\n### {cat} ({len(by_cat[cat])})')
        for tid in sorted(by_cat[cat]):
            idx.append(f'- [`{tid}`](sections/{cat}/{tid}.md)')
    (out_dir / 'INDEX.md').write_text('\n'.join(idx))

    # needs-confirmation.md
    nc_lines = ['# Needs confirmation', '',
                'Traditions where L3 search returned ambiguous evidence — review needed:', '']
    for r in needs_conf:
        nc_lines.append(f'### `{r["tid"]}`')
        nc_lines.append(f'- reason: {r.get("reason","?")}')
        nc_lines.append(f'- search summary: {r.get("search_summary","")[:500]}')
        nc_lines.append('')
    nc_lines.append('## No-match (confirmed absent)')
    nc_lines.append('')
    for r in no_match:
        nc_lines.append(f'- `{r["tid"]}` — {r.get("reason","?")}')
    if errored:
        nc_lines.append('')
        nc_lines.append('## Errored')
        for r in errored:
            nc_lines.append(f'- `{r["tid"]}` — {r.get("reason","?")}')
    (out_dir / 'needs-confirmation.md').write_text('\n'.join(nc_lines))

    # PR-CANDIDATE.md (enrichments)
    enrich_dir = session_dir / 'enrichments'
    enrichments = sorted(enrich_dir.glob('*.md'))
    pr_lines = [f'# PR Candidates — wish "{state["wish"]}"', '',
                f'{len(enrichments)} traditions had L3 search produce content '
                'worth contributing back upstream.', '',
                '## Type 1: case_index additions',
                '(append a new entry to the named tradition\'s case_index)', '']
    for ep in enrichments:
        tid = ep.stem
        pr_lines.append(f'- `{tid}` — see `.session/{session_dir.name}/enrichments/{tid}.md`')
    pr_lines.append('')
    pr_lines.append('## Type 2: new prayers/ entries')
    pr_lines.append('(stage cross-tradition skeletons to prayers/ — TODO in v2)')
    (out_dir / 'PR-CANDIDATE.md').write_text('\n'.join(pr_lines))

    return out_dir


# ───── main ──────────────────────────────────────────────────

def slugify(s):
    s = re.sub(r'[^\w\s-]', '', s.lower())
    s = re.sub(r'\s+', '-', s).strip('-')
    return s[:40]


async def run(args):
    t_start = time.time()

    # Resume vs new
    if args.resume:
        session_dir = SESSION_DIR / args.resume
        if not session_dir.exists():
            sys.exit(f'no session: {args.resume}')
        state = load_state(session_dir)
        if not state:
            sys.exit('no state.json in session dir')
        print(f'⏯  resuming {args.resume}')
        wish = state['wish']
    else:
        wish = args.wish
        ts = time.strftime('%Y%m%d-%H%M%S')
        slug = args.slug or slugify(wish[:40])
        session_dir = SESSION_DIR / f'{slug}-{ts}'
        session_dir.mkdir(parents=True, exist_ok=True)
        (session_dir / 'sections').mkdir(exist_ok=True)
        (session_dir / 'enrichments').mkdir(exist_ok=True)
        print(f'🆕 session: {session_dir.relative_to(ROOT)}')

        wish_type = args.wish_type or await classify_wish(wish)
        print(f'   wish_type: {wish_type}')

        safety = await check_wish_safety(wish)
        print(f'   safety: {safety}')
        if safety == 'HARMFUL':
            sys.exit('refused: wish is harmful (explicitly wishes harm to identifiable others). Rephrase or use --force (not implemented).')

        anchors = {}
        if args.anchors and Path(args.anchors).exists():
            anchors = json.loads(Path(args.anchors).read_text())
        anchor_keys = list(anchors.keys())
        print(f'   anchors keys: {anchor_keys}')

        state = {
            'wish': wish, 'wish_type': wish_type,
            'slug': slug,
            'started_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'anchors_keys': anchor_keys,
            'results': [],
            'done_tids': [],
        }
        await save_state(session_dir, state)

    # Load anchors at run time (kept local)
    anchors = {}
    if args.anchors and Path(args.anchors).exists():
        anchors = json.loads(Path(args.anchors).read_text())

    seeded = load_seeded_traditions()
    if args.max:
        seeded = seeded[:args.max]
    done_tids = set(state.get('done_tids') or [])
    todo = [t for t in seeded if t['id'] not in done_tids]

    print(f'   traditions to process: {len(todo)} (skipping {len(done_tids)} already done)')
    print(f'   parallel: {args.parallel}, L3: {"on" if not args.skip_l3 else "off"}')
    print()

    sem = asyncio.Semaphore(args.parallel)

    async def gated(entry):
        async with sem:
            t0 = time.time()
            try:
                r = await asyncio.wait_for(
                    process_tradition(entry, wish, state['wish_type'],
                                      state['anchors_keys'], session_dir,
                                      skip_l3=args.skip_l3),
                    timeout=900,
                )
            except asyncio.TimeoutError:
                r = {'tid': entry['id'], 'status': 'error', 'reason': 'timeout-900s'}
            except Exception as e:
                r = {'tid': entry['id'], 'status': 'error', 'reason': str(e)[:200]}
            elapsed = time.time() - t0
            r['elapsed'] = round(elapsed, 1)
            mark = {'match': '✅', 'no-match': '🚫', 'needs-confirmation': '❓', 'error': '❌'}.get(r['status'], '?')
            tier = r.get('tier', '-')
            print(f'  {mark} {r["tid"]:42} {tier:>3} {elapsed:>5.1f}s', flush=True)
            async with STATE_LOCK:
                state['results'].append(r)
                state['done_tids'].append(r['tid'])
            await save_state(session_dir, state)
            return r

    await asyncio.gather(*[gated(t) for t in todo])

    # Summary
    counts = Counter(r['status'] for r in state['results'])
    tiers = Counter(r.get('tier') for r in state['results'] if r['status'] == 'match')
    elapsed_total = time.time() - t_start

    state['finished_at'] = time.strftime('%Y-%m-%d %H:%M:%S')
    state['elapsed_seconds'] = int(elapsed_total)
    state['counts'] = dict(counts)
    state['tier_distribution'] = dict(tiers)
    await save_state(session_dir, state)

    print()
    print('=== summary ===')
    print(f'  status: {dict(counts)}')
    print(f'  tier:   {dict(tiers)}')
    print(f'  elapsed: {elapsed_total:.0f}s')

    # Synthesize universal closing (cross-tradition 总回向 + mitigations)
    print()
    print('🛡  synthesizing universal closing (side-effect mitigation)...')
    closing = await synthesize_universal_closing(state, session_dir)
    if closing:
        print(f'   closing length: {len(closing)} chars')
    else:
        print(f'   no high/medium-risk traditions used; no special closing')

    # Assemble outputs
    print('📦 assembling outputs...')
    out_dir = assemble_outputs(session_dir, state, anchors,
                                universal_closing_text=closing)
    print(f'   → {out_dir.relative_to(ROOT)}/')
    print(f'      INDEX.md / RENDERED.md / sections/ / needs-confirmation.md / PR-CANDIDATE.md')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('wish', nargs='?', help='wish text (or omit with --resume)')
    ap.add_argument('--wish-type', default=None, choices=WISH_TYPES + [None])
    ap.add_argument('--anchors', default=None)
    ap.add_argument('--slug', default=None)
    ap.add_argument('--parallel', type=int, default=10)
    ap.add_argument('--resume', default=None, help='session subdir name to resume')
    ap.add_argument('--skip-l3', action='store_true')
    ap.add_argument('--max', type=int, default=None, help='cap to first N traditions (testing)')
    args = ap.parse_args()
    if not args.wish and not args.resume:
        ap.error('provide wish text or --resume')
    asyncio.run(run(args))


if __name__ == '__main__':
    main()
