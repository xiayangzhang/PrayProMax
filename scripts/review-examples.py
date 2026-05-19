#!/usr/bin/env python3
"""Have codex + grok review the examples/ outputs without burning Claude tokens.

For each example/<slug>/:
  - Codex compliance review (samples N sections, checks schema/language/mitigation/no-exchange compliance)
  - Grok enrichment verification (if PR-CANDIDATE exists, grok --search verifies each L3 finding's claim)

Writes:
  - examples/<slug>/REVIEW-codex.md
  - examples/<slug>/REVIEW-grok.md (only if enrichments exist)
"""
import asyncio
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LLM_CALL = ROOT / 'scripts/llm-call.py'

CODEX_MODEL = os.environ.get('OPENAI_MODEL', 'gpt-5.5')
GROK_MODEL = os.environ.get('XAI_MODEL', 'grok-4.3')

SAMPLE_PER_EXAMPLE = 12  # how many sections to send for codex compliance check
PARALLEL = 6


async def call_model(model, prompt, max_tokens=4096, search=False, timeout=600):
    args = ['python3', str(LLM_CALL), model,
            '--max-tokens', str(max_tokens), '--timeout', str(timeout)]
    if search:
        args.append('--search')
    proc = await asyncio.create_subprocess_exec(
        *args, stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate(input=prompt.encode())
    if proc.returncode != 0:
        return None, err.decode()[:500]
    return out.decode(), None


def sample_sections(example_dir):
    """Pick N sections across diverse categories from full-placeholders.md."""
    full = (example_dir / 'full-placeholders.md').read_text()
    blocks = re.split(r'\n---\n', full)
    # filter to blocks that look like ## sections
    sections = [b.strip() for b in blocks if b.lstrip().startswith('##')]
    random.seed(42)
    sample = random.sample(sections, min(SAMPLE_PER_EXAMPLE, len(sections)))
    return sample


async def codex_review_one(slug):
    example_dir = ROOT / 'examples' / slug
    sections = sample_sections(example_dir)
    sample_block = '\n\n---\n\n'.join(sections)
    index_text = (example_dir / 'INDEX.md').read_text()

    prompt = f'''You are auditing PrayProMax example output for compliance with project rules.

Example: {slug}

INDEX.md summary:
{index_text[:2000]}

Sampled prayer sections (N={SAMPLE_PER_EXAMPLE}, random subset, all with {{{{anchors.*}}}} placeholders intact, no PII):
{sample_block[:60000]}

Audit each section against these checks. Be specific: cite section name + line excerpt when flagging.

## Compliance checks

1. **Original liturgical language**: prayer body / mantras / scriptures must be in the tradition's primary_language (Sanskrit / Pali / Classical Arabic / Biblical Hebrew / Latin / Tibetan / Church Slavonic / Geʽez / Aramaic / Classical Chinese / etc.). Chinese is ONLY allowed for the personal-aspiration paragraph (with `{{{{anchors.*}}}}` placeholders). FLAG: any mantra/scripture appearing in Chinese translation where it should be original.

2. **Anchor placeholder integrity**: any user-specific info must be `{{{{anchors.<key>}}}}` form. FLAG: any real-looking personal name / dob / address.

3. **Side-effect mitigation embedded**: traditions where you'd expect medium/high backlash_risk should have closing protective ritual (回向 / 净化 / 谢神 / 护身咒) AS PART OF THE PRAYER BODY (not a footnote). FLAG: high-risk-looking sections without closing protection.

4. **No quid-pro-quo / 无交换 / 无还愿**: prayers must NOT include "if you grant X I will offer Y" bargain clauses, sacrifice schedules, payment, soul-bond promises. FLAG: any bargain/exchange wording.

5. **No-harm + No-deprivation clauses**: wealth/longevity/success requests should include in-body line that doesn't dispossess or harm others (e.g. 「不夺他人福报、不损他人寿数」 or tradition-appropriate analogue). FLAG: missing where applicable.

6. **No metadata residue**: no `<!-- source: ... -->` HTML comments, no "使用提示" / "建议时机" / "功效说明" / "免责声明" / "本祷词不构成医疗" type metadata leaks.

7. **No deity mixing in same stanza**: each section's prayer should stay within ONE tradition's pantheon. FLAG: any cross-tradition deity invocation within a single ## block.

8. **Plausibility / hallucination spot-check**: any sections that look factually wrong, with made-up mantras or non-canonical texts? Lean on your scholarly training knowledge.

## Output format

```markdown
# Codex review — {slug}

## Verdict
PASS / PASS_WITH_NOTES / FAIL — one word

## Counts
- Sections sampled: {SAMPLE_PER_EXAMPLE}
- Compliance issues found: N
- Issues by severity: critical=X / minor=Y

## Findings
For each issue:
### <severity> · <check #> · <section name>
- Line excerpt: ...
- Issue: ...
- Suggested fix: ...

## Overall assessment
1-3 paragraph qualitative summary.
```

Be terse. Skip findings where all 8 checks pass for a section.'''

    text, err = await call_model(CODEX_MODEL, prompt, max_tokens=6000)
    if err:
        text = f'# Codex review — {slug}\n\nReview call failed: {err}\n'
    (example_dir / 'REVIEW-codex.md').write_text(text)
    print(f'  ✓ codex review → examples/{slug}/REVIEW-codex.md')


async def grok_verify_enrichment(slug, enrichment_path):
    """For each enrichment file in PR-CANDIDATE, ask grok to verify with web search."""
    content = enrichment_path.read_text()
    tid_match = re.search(r'tradition_id:\s*(\S+)', content)
    wish_match = re.search(r'wish_type:\s*(\S+)', content)
    tid = tid_match.group(1) if tid_match else '?'
    wish_type = wish_match.group(1) if wish_match else '?'
    findings = content.split('## Search findings')[1].split('##')[0] if '## Search findings' in content else content[:2000]

    prompt = f'''You are independently verifying a community-PR candidate for PrayProMax.

A prior `grok --search` pass produced findings claiming this tradition has a relevant practice for the wish_type. Re-search the web and validate.

Tradition: {tid}
wish_type: {wish_type}
example slug: {slug}

Original findings to verify:
{findings[:5000]}

Your job: re-search and answer:
1. Does the cited mantra/practice ACTUALLY exist in this tradition? (search to confirm)
2. Is it canonical / widely-recognized, or fringe / synthesized / hallucinated?
3. Is the wish_type matching reasonable — does the tradition actually use this for the claimed purpose?
4. Are the cited URLs real and on-topic?

Output format:
```markdown
## verify — {tid}

verdict: CONFIRMED / PARTIAL / REJECTED
confidence: high / medium / low

evidence:
- <fresh source URL>: <what it confirms or refutes>
- <fresh source URL>: ...

assessment:
1-3 sentence summary.

upstream recommendation:
- MERGE (verdict CONFIRMED + canonical fit)
- HOLD (verdict PARTIAL, needs human review)
- REJECT (REJECTED — do not contribute)
```'''
    text, err = await call_model(GROK_MODEL, prompt, max_tokens=2000, search=True, timeout=300)
    return tid, text, err


async def grok_review_one(slug):
    example_dir = ROOT / 'examples' / slug
    enrichments_dir = example_dir / 'enrichments'
    if not enrichments_dir.exists():
        return
    enrichments = sorted(enrichments_dir.glob('*.md'))
    if not enrichments:
        return

    sem = asyncio.Semaphore(3)

    async def gated(e):
        async with sem:
            print(f'    grok verify: {e.stem}')
            return await grok_verify_enrichment(slug, e)

    results = await asyncio.gather(*[gated(e) for e in enrichments])

    out_lines = [f'# Grok enrichment verification — {slug}', '',
                 f'_Re-searched each L3 enrichment with grok with live search._', '']
    for tid, text, err in results:
        out_lines.append('---')
        out_lines.append('')
        if err:
            out_lines.append(f'## verify — {tid}\n\nERROR: {err}\n')
        else:
            out_lines.append(text)
        out_lines.append('')
    (example_dir / 'REVIEW-grok.md').write_text('\n'.join(out_lines))
    print(f'  ✓ grok review → examples/{slug}/REVIEW-grok.md ({len(enrichments)} enrichments verified)')


async def main():
    slugs = ['github-flourish', 'safe-travel', 'job-interview']
    print(f'== codex compliance reviews (parallel) ==')
    await asyncio.gather(*[codex_review_one(s) for s in slugs])
    print()
    print(f'== grok enrichment verifications ==')
    for s in slugs:
        await grok_review_one(s)
    print()
    print('done')


if __name__ == '__main__':
    asyncio.run(main())
