# 2-draft merge — PrayProMax Phase E

You are the **merge agent** in PrayProMax's Phase E pipeline (OpenAI-compatible API).

Combine the two drafts below into a single canonical tradition sub-document.

## Tradition

- **id**: `<TRADITION_ID>`
- **name**: `<TRADITION_NAME>`
- **category**: `<TRADITION_CATEGORY>`

## Merge rules

| field | rule |
|---|---|
| base structure | codex draft is the base |
| `search_strategy` | **prefer grok** (lived queries) |
| `case_index` | union; same `(wish_type, officiant)` → prefer codex's canonical hint; grok-only modern variants → add as separate entries (officiant: none unless grok specified) |
| `authoritative_texts` | union, dedupe; prefer codex's phrasing |
| `primary_languages` | codex |
| `通用骨架` | codex |
| `taboos` | union (any worker's taboo included) |
| `mitigation` | codex |
| `verification` | union all URLs |
| `self_pray_capable` | codex |
| `required_officiants` | codex |

Default to codex on conflict. Override with grok only where grok has clear contemporary advantage (`search_strategy`, contemporary case variants).

## Hard rules

- File matches `schemas/tradition.schema.md`
- `case_index` covers all 8 wish_type (health/wealth/protection/deceased/relationship/wisdom/breaking/event)
- mantra / 经文 / 颂 保留原文
- 不写"使用提示" / "功效说明"
- 不混合 deity 同段呼请

## Output structure (CRITICAL)

Your response = the raw merged markdown file content. Required 3-part structure:

```
---
<frontmatter>
---

# <派别名>

## 结构
...

## 通用骨架
\`\`\`
...
\`\`\`
```

Exactly 2 `---` lines (opener at line 1, closer between fm and body). Body with `# 名`, `## 结构`, `## 通用骨架` headers.

### YAML EDGE CASES

If any `case_index` hint contains `:`, wrap value in `"..."`:
```yaml
- wish_type: health
 hint: "薬師如来真言: on korokoro sendari"
 officiant: shingon-ajari
```

### NEVER
- ❌ No preamble, no commentary, no code fences around the YAML/markdown
- ❌ Do NOT omit closing `---`
- ❌ Do NOT skip body sections

### ALWAYS
- ✅ First character: `-`
- ✅ Write verbatim — dispatcher saves as-is

---

=== CODEX DRAFT ===

<CODEX_DRAFT_CONTENT>

=== GROK DRAFT ===

<GROK_DRAFT_CONTENT>

---

Now respond with the merged file content (raw markdown only — no preamble, no fences).
