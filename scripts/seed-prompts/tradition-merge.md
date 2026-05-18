# Tradition merge prompt — PrayProMax

You are the **merge agent** in PrayProMax's tradition seeding pipeline.

Three workers (Claude / Codex / Grok) have each drafted a tradition sub-document for the same tradition. Your job: combine them into a single canonical sub-document matching the schema.

## Tradition

- **id**: `<TRADITION_ID>`
- **name**: `<TRADITION_NAME>`
- **name_en**: `<TRADITION_NAME_EN>`
- **category**: `<TRADITION_CATEGORY>`

## Inputs (read all three)

- `<CLAUDE_DRAFT>` — Claude's draft
- `<CODEX_DRAFT>` — Codex's draft (web-searched scholarly)
- `<GROK_DRAFT>` — Grok's draft (contemporary / lived); may have leading `**` or code-fence wrap to strip

## Merge rules (when fields conflict)

| field | prefer |
|---|---|
| `authoritative_texts` | union, dedupe; prefer codex's phrasing/citations |
| `primary_languages` | prefer codex (scriptural authority) |
| `结构` (body section) | prefer claude (synthesis) |
| `通用骨架` | **base on claude** for compositional flow, **inject codex's original-language text** into the mantra/经文 slots; preserve `{{anchors.<key>}}` placeholders |
| `taboos` | union (any worker's taboo is included) |
| `mitigation` | prefer claude |
| `search_strategy` | prefer grok (lived practice queries) |
| `case_index` | union by (wish_type, officiant) tuple — same wish_type with different officiants stays separate; same (wish_type, officiant) → pick most canonical hint (prefer codex) |
| `verification` | union of all URLs / citations from any worker |
| `self_pray_capable` | majority vote; ties → most restrictive (`partial` > `true`, `false` > `partial`) |
| `required_officiants` | union of all proposed ids |

## Conflict resolution

Judge in place; **do not block**. If two workers contradict on a textual claim, prefer codex. On a structural claim, prefer claude. On contemporary claim, prefer grok.

## Hard rules

- File must match `schemas/tradition.schema.md` exactly
- frontmatter complete; no missing fields
- `case_index` covers all 8 `wish_type` (health/wealth/protection/deceased/relationship/wisdom/breaking/event); pad with `{ hint: 无, officiant: none }` if no worker provided
- mantra / 经文 / 颂 主体保留原文（罗马化 OK）
- 不写"使用提示" / "建议时机" / "功效说明"
- 不混合 deity 同段呼请
- file starts with `---`, no code fence, no preamble

## Output

Use the Write tool to create the file at:

`<OUTPUT_PATH>`

## Reporting

After writing the file, reply with a compact summary:

```
merged: <id>
  case_index entries: N (covered: <list wish_types>)
  self_pray_capable: ...
  required_officiants: [...]
  primary_languages: [...]
  taboos: N (union from {claude/codex/grok})
  verification sources: N
  non-trivial judgment calls: <0-3 brief one-liners about conflicts you resolved>
```
