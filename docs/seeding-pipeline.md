# PrayProMax — Cold-Start Seeding Pipeline (how Phase A–E ran)

This is the historical record of how PrayProMax bootstrapped from a curated tradition survey
(a curated list of ~245 living mystical / religious traditions with prayer
practice) to **289 seeded traditions + 262 virtual officiant cards** in
production. A community contributor running their own slice would follow the
same pattern.

> **Community note**: the specific models below (`gpt-5.5`, `grok-4.20-fast`) were what the maintainer had access to during cold-start. Any OpenAI-compatible chat model works for the worker/merge role (set `OPENAI_MODEL`); any Grok-compatible model works for L3 search (set `XAI_MODEL`).

## Phase A — curated survey → `INDEX.yaml v0`

**Goal**: parse the source survey into a structured categorized list.

- Tool: Claude subagent
- Action: classify each survey entry into the 18-category enum, generate
  kebab-case `id`, split coordinated lists (Wicca: 4 variants → 4 entries),
  merge alias-style "X / Y" lists → 1 entry with `aliases`, preserve native
  names in `name` field
- Output: `INDEX.yaml v0` — **274 entries** (split coordinated lists
  expanded `245 → 274`)

## Phase B — 3-worker audit → `INDEX.yaml v1`

**Goal**: catch survey gaps / misclassifications / spurious entries / bad ids.

- Tool: 3 audit workers (Claude / Codex / Grok)
- Action: each independently audits survey + INDEX v0, produces YAML report
  with `missing` / `spurious` / `misclassified` / `should_merge` /
  `should_split` / `id_rename` lists
- Cross-worker aggregation: multi-worker consensus = high confidence
- Maintainer review:
  - Multi-worker consensus → apply directly
  - Single-worker findings → judgment call (~80% applied)
  - **Lineage rule applied**: 20-21c single-founder NRMs / self-help / energy
    work → skipped with `skip_reason: no-lineage`
- Output: `INDEX.yaml v1` — **345 entries** (291 pending + 56 skipped)

## Phase C — worker prompt templates

**Goal**: define what each seeding-worker produces.

- 9 prompt templates in `scripts/seed-prompts/` (worker, merge, officiant variants for legacy 3-worker community flow + Phase E 2-worker pipeline):
  - `tradition-worker-codex-solo.md` (gpt-5.5 covering synthesis +
    scholarly + officiant card generation)
  - `tradition-worker-grok.md` (contemporary lived-practice supplement)
  - `tradition-merge-2draft.md` (codex merges the 2 drafts)
  - `tradition-worker-api.md` / `tradition-merge-api.md` (Phase E
    variants using OpenAI-compatible API HTTP API instead of codex CLI)

Schema (`schemas/tradition.schema.md`) is inlined at render time so workers
have it without needing file access.

## Phase D — trial batch (3 traditions × 3 workers)

**Goal**: validate the pipeline before unleashing on 290.

- Picked 3 traditions covering self_pray / partial / officiant-required:
  - `jingtu-zong` (Pure Land — self_pray)
  - `naqshbandi` (Sufi — partial)
  - `vodou-haitian` (Vodou — officiant)
- Ran 3-worker draft + merge for each
- Validated outputs: schema pass, case_index covers 8 wish_types, original
  language preserved, no "使用提示" leakage, officiants auto-generated

## Phase E — full 291 seeding

**Goal**: seed all in-scope traditions.

- Pipeline: gpt-5.5 (OpenAI-compatible API) + grok-4.20-fast + gpt-5.5 merge, parallel=10
- Wall time: ~57 minutes for 289 traditions
- First failure mode: ChatGPT subscription rate-limited at ~4 traditions in
  → switched from codex CLI to OpenAI-compatible API HTTP (gpt-5.5 via proxy)
- Second failure mode: 18 errors (5 transient 502s, 13 YAML parse errors)
  → added retry, stricter colon-quoting rule in prompts, deleted-on-fail
  validation → all 18 recovered
- Officiant generation: separate batch via `scripts/dispatch-officiants.py`
  → 262 cards in 13 min, 0 errors
- Review pass: `scripts/review-seeded.py` →
  - 291/289 traditions: 0 parse errors, 0 missing fields, 0 wish_type gaps,
    0 forbidden phrases, 0 fence/preamble residue
  - 263/262 officiants: 0 errors after a tiny 2-card cleanup
  - cross-refs: 263 ↔ 263 perfect, 0 missing 0 orphaned

## Tools used

| Tool                      | Where             | What                                       |
| ---                       | ---               | ---                                        |
| `codex` CLI (gpt-5.5)     | Phase D trial     | initial 3-tradition draft + merge          |
| `OpenAI-compatible API` HTTP (gpt-5.5)  | Phase E main      | bulk seeding + merge                       |
| `grok` (grok-4.20-fast)   | Phase E + audit   | contemporary supplement + ref audit        |
| Claude subagent (Agent)   | Phase A, B        | parse / audit / review orchestration       |
| `scripts/render-prompt.py`| any phase         | template parameter substitution            |
| `scripts/dispatch-seed.py`| Phase E           | concurrent dispatcher with state + retry   |
| `scripts/dispatch-officiants.py` | Phase E   | officiant card batch generator             |
| `scripts/review-seeded.py`| Phase E review    | static schema + content quality scan       |

## Replicating in a community contribution context

A contributor wants to seed a **slice** (e.g., "all Korean traditions" or "fix
the 22 wealth no-match traditions"):

1. Fork repo + clone
2. Set env vars (or edit `scripts/llm-call.py` keys) with their own gpt key
3. Run `python3 scripts/dispatch-seed.py --ids korean-jogye-order,cheondogyo,...`
4. Review outputs locally
5. `git add skills/traditions/east-asian-korea/*.md skills/officiants/east-asian-korea/*.md`
6. Open PR
7. **(PLANNED CI)** Future GH Actions will run 3-reviewer + schema + lineage gates; **currently** maintainer review is manual
8. Maintainer merges or requests changes

Same scripts. BYOK (bring your own key). The community contribution dispatcher
(T6) will wrap this with friendlier UX.
