# PrayProMax — Architecture

## Layered data model

```
┌─────────────────────────────────────────────────────────┐
│ skills/pray/SKILL.md      ← root orchestrator skill     │
└─────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ skills/traditions/INDEX.yaml                            │
│   ├─ 291 seeded traditions (status=seeded)              │
│   ├─ 54 skipped (no-prayer / no-lineage / split / ...)  │
│   └─ schema: schemas/tradition.schema.md                │
└─────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────────────────┐
│ skills/traditions/<category>/<id>.md                    │
│   ├─ frontmatter: 18-category enum, primary_languages,  │
│   │   case_index (8 wish_types), taboos, mitigation     │
│   │   backlash_risk, self_pray_capable, required_offic… │
│   └─ body: 结构 / 通用骨架 (anchors-placeholder template)│
└─────────────────────────────────────────────────────────┘
        │  references via required_officiants
        ▼
┌─────────────────────────────────────────────────────────┐
│ skills/officiants/<category>/<id>.md                    │
│   ├─ Virtual prompt persona — NOT real-person directory │
│   ├─ persona_prompt (injected to LLM at draft time)     │
│   ├─ self_replaceable + self_substitution_notes         │
│   └─ ritual_authority_basis, voice_attributes           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ prayers/                ← self-growing RAG cache        │
│   ├─ INDEX.json          (entries, source, traditions)  │
│   └─ <wish_type>/<id>.md (skeleton with placeholders)   │
└─────────────────────────────────────────────────────────┘
```

## 18 category enum

`east-asian-han` / `east-asian-japan` / `east-asian-korea` / `east-asian-folk` /
`southeast-asia` / `south-asia` / `tibetan-himalayan` /
`abrahamic-judaism` / `abrahamic-christianity` / `abrahamic-islam` / `abrahamic-other` /
`western-occult` / `european-pagan` /
`african-diasporic` / `americas-indigenous` / `north-asian-shamanic` / `oceanic` /
`modern-energy-newage`

## 8 wish_type enum

`health` / `wealth` / `protection` / `deceased` /
`relationship` / `wisdom` / `breaking` / `event`

Every seeded tradition's `case_index` is required to cover all 8 (hint `无` if no法门).

## 3-tier RAG cache (used in pray flow)

```
L1: prayers/ RAG
    Hit when an earlier session contributed a skeleton for the same wish_type
    + tradition combination. Zero search cost.

L2: tradition.case_index
    Per-tradition hint already seeded during Phase E. Cheap LLM call to
    draft prayer using the hint as the structural prompt.

L3: web search (grok-4.20-fast --search)
    Only when L1+L2 miss. Findings are:
      • used to draft a section for the current user
      • staged in .session/<id>/enrichments/ as PR candidates
    so a future user benefits from cache hit instead of paying search again.
```

**Key invariant**: the 3-tier hierarchy makes the system self-improving.
Search expense is paid once per gap; the result returns to the public
knowledge base via PR; future users get L1/L2 hit.

## Dispatcher pipeline (Phase E seeding)

```
INDEX.yaml (291 pending)
       │
       │   per-tradition parallel (semaphore=10):
       ▼
   gpt-5.5 (sub2api)    ← writes skills/traditions/<cat>/<id>.md
       +
   grok-4.20-fast       ← writes .seed/<id>/grok.md
       │   (with --search for contemporary supplement)
       ▼
   gpt-5.5 merge        ← overwrites skills/traditions/<cat>/<id>.md
                          (merges codex draft + grok draft)
       ▼
   validate (schema + YAML + 8 wish_types + ...)
       ▼
   INDEX status: pending → seeded   (asyncio.Lock serialized)
```

## Pray pipeline (end-user flow)

```
wish (text) + anchors (LOCAL-ONLY, key-value)
       │
       │  classify (gpt) → wish_type
       │  safety check (gpt) → SAFE / AMBIGUOUS / HARMFUL
       ▼
   for each of 291 seeded traditions (parallel=10):
       │
       ├─ L1 check (prayers/ RAG)
       ├─ L2 check (case_index has wish_type hint?)
       └─ L3 fallback (grok --search if L1+L2 miss)
       │
       ▼
   draft prayer section (per tradition)
       │  • original liturgical language only
       │  • mitigation embedded for high backlash_risk
       │  • no harm / no deprivation / no quid-pro-quo clauses
       │  • placeholders {{anchors.<key>}} (never real names)
       │
       ▼
   universal closing (synthesize cross-tradition 总回向)
       │  • includes mitigations for high-risk traditions used
       │  • includes no-harm + no-exchange clauses
       │
       ▼
   assemble outputs:
       ├─ outputs/wish-<slug>-<ts>/INDEX.md
       ├─ outputs/wish-<slug>-<ts>/RENDERED.md   (anchors filled, local)
       ├─ outputs/wish-<slug>-<ts>/placeholders/ (anchors preserved)
       ├─ outputs/wish-<slug>-<ts>/sections/<cat>/<tid>.md
       ├─ outputs/wish-<slug>-<ts>/needs-confirmation.md
       └─ outputs/wish-<slug>-<ts>/PR-CANDIDATE.md
```

## PII isolation contract

- **anchors** (any user-supplied key-value: name, dob, address, etc.) NEVER enter LLM context
- Drafts always use `{{anchors.<key>}}` placeholders
- Local-only substitution happens at final render
- `outputs/` and `.session/` are gitignored (contain rendered PII)
- `prayers/` contains only placeholder-preserved skeletons (PII-free, safe to commit)

## Side-effect mitigation (built into prayer content)

These are **part of the prayer body**, not metadata footnotes:

1. **Per-tradition mitigation** — when `backlash_risk: medium|high`, the tradition's
   `mitigation` field is embedded as closing protective ritual (回向/净化/谢神/etc.)
2. **No-harm clause** — never wish suffering to identifiable third parties
3. **No-deprivation clause** — wealth/longevity/success requests cannot dispossess others
4. **No quid-pro-quo / 无交换 / 无还愿** — no "if you grant X, I'll Y" bargains;
   never include payment schedules, sacrifice promises, soul-bond obligations
5. **Initiation taboos** — high-rite practices use self-substitution form unless
   officiant persona is explicitly invoked
6. **Cross-tradition 总回向** — synthesized closing dedication tying together all
   mitigations + no-harm + no-exchange clauses
