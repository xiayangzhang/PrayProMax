# Codex 2-draft merge — PrayProMax Phase E

You are the **codex merge agent** in PrayProMax's Phase E pipeline.

Two prior workers have produced drafts for the same tradition: **codex** (full draft, scholarly + structural, already at the canonical path) and **grok** (contemporary supplement). Your job: merge grok's contributions into codex's draft, in place.

## Tradition

- **id**: `<TRADITION_ID>`
- **name**: `<TRADITION_NAME>`
- **category**: `<TRADITION_CATEGORY>`

## Inputs

- **Codex draft**: `<CODEX_DRAFT_PATH>` (your base; you will overwrite this in place)
- **Grok draft**: `<GROK_DRAFT_PATH>` (may have leading `**` or code-fence wrap — strip before parsing)

Read both files first.

## Merge rules

| field | rule |
|---|---|
| base structure | codex draft is the base |
| `search_strategy` | **prefer grok** (lived queries) |
| `case_index` | union; for overlapping `(wish_type, officiant)` → keep codex's canonical hint; for variants only grok has → add as new entries with `officiant: none` unless grok specified otherwise |
| `authoritative_texts` | union, dedupe; prefer codex's phrasing |
| `primary_languages` | codex |
| `通用骨架` | codex |
| `taboos` | union (any worker's taboo is included) |
| `mitigation` | codex |
| `verification` | union all URLs |
| `self_pray_capable` | codex |
| `required_officiants` | codex |
| `officiant cards` | **do not touch** — codex already created them in step 1; do not modify files under `skills/officiants/` |

## Conflict resolution

When you must judge, default to codex. Override codex with grok's input only where grok has clear contemporary advantage (`search_strategy`, contemporary case variants, modern community sources).

## Hard rules

- File must match `/Volumes/leoyun/personal-projects/PrayProMax/schemas/tradition.schema.md` exactly
- `case_index` covers all 8 `wish_type` (health/wealth/protection/deceased/relationship/wisdom/breaking/event); pad with `{ hint: 无, officiant: none }` if neither worker provided
- mantra / 经文 / 颂 主体保留原文（罗马化 OK）
- 不写"使用提示" / "建议时机" / "功效说明"
- 不混合 deity 同段呼请
- file starts with `---`, no code fence inside file, no preamble outside file

## Output

Use your write/edit tool to **overwrite** `<CODEX_DRAFT_PATH>` with the merged file.

## Reporting

```
merged: <id>
  case_index entries: N (added from grok: M)
  search_strategy: from grok ✓
  verification sources: N (codex K + grok-added L)
  taboos: N (union)
  judgment calls: <0-3 brief one-liners>
```
