---
name: pray
description: A software prayer flag (in the prayer-wheel tradition) — when you walk an AI through a tradition's officiant persona, schema, and canonical corpus, the form-act is what prays. Cross-tradition prayer composition over 289 living religious / mystical traditions. 触发词：祈祷/发愿/求愿/转经/念经/pray/"保佑..."/"愿..."
---

# PrayProMax — root pray skill

## Framing

This skill is the runtime side of a conceptual position: **form precedence**. The prayer wheel does not pray; the form prays. The Catholic perpetual adoration recording does not pray; the form does. An AI walking the right officiant persona + the right schema + the right canon outputs a real prayer, in the same sense the mani wheel does. Mechanically the closer analogue is the **prayer flag** — inscribed once, the wind reads it, no continuous turning. See [`docs/manifesto.md`](../../docs/manifesto.md).

This document is the operational orchestration: classify, traverse, draft, merge, render. The philosophical commitment lives in the manifesto; this file implements it.

## 输入

1. **wish**（必需）—— 自然语言愿望
2. **anchors**（可选，本地脱敏）—— 任意 key-value：

   ```yaml
   anchors:
     name-1: ...
     dob-1: ...
     name-2: ...
     relation-1-2: ...
     beneficiary: ...
     # 任意 key 都允许
   ```

3. **traditions**（可选）—— `auto` | `["dharmic/buddhism-han", ...]` | `all`

**硬约束：anchors 永远不进 LLM context。** 只在最后一步本地渲染。

## 执行步骤

### Step 0: 脱敏与分类

- anchors 暂存到 local-only memory，不进任何后续 prompt
- 对 wish 分类：
  - `wish_type` ∈ {health, wealth, protection, deceased, relationship, wisdom, breaking, event}
  - `sub_tags`：自由标签

### Step 1: 检索 `prayers/`

- 读 `prayers/INDEX.json`
- 按 wish_type + sub_tags 语义+tag 联合匹配
- 命中 confidence ≥ 0.7 → **跳 Step 4**；否则继续

### Step 2: 派别筛选 + 子文档调度

- 决定派别（默认 ai-pick 3–5 个最匹配的；user 指定 `all` 则全跑）
- 对每个 tradition 并行 spawn sub-agent：
  - 读 `skills/traditions/<category>/<id>.md`
  - 查 `case_index`：该 wish_type 是否有 hint
  - 有 → 按 hint 起草
  - 无 → 按 `search_strategy` 执行 WebSearch → 综合起草
  - **若 case 的 `officiant != none`**：读 `skills/officiants/<id>.md`，将其 `persona_prompt` 注入起草 sub-agent 的 system context（sub-agent 以该角色视角、语气起草祷词正行）。用户若拒绝 persona 注入，按 `self_substitution_notes` 退化为简化版。**注意：这是 prompt 层面的角色扮演，不是真人中介。**
- 每个 sub-agent 产出一份 draft md（占位符版本）

### Step 3: 合并 + 选择性回写知识库

- 合并 drafts → 最终 prayer.md（占位符版本）
- **评估**：本 case 或其抽象变体是否对未来用户有复用价值？
  - 能通用 → 剥离个人叙事，抽出骨架 → 写入 `prayers/<wish_type>/<auto-name>.md`，更新 `prayers/INDEX.json`
  - 不能通用（高度个性化 / 一次性） → 跳过回写
- `source` 标记：
  - 直接 hit classical 经典 → `source: classical`
  - 子 md + 搜索合成 → `source: traditional-synthesized` + `verification:` 数组
  - 社区 PR → `source: community`

### Step 4: 本地渲染 anchors

- 替换最终 md 中的 `{{anchors.<任意key>}}` 占位符
- 输出最终 md 给用户

## 输出格式

prayer.md 始终包含：

- frontmatter：`wish_type / traditions / generated_at`
- 正文：合并后的祈祷词，按派别分块（不混合 deity 同段呼请）

**不输出"使用提示" / "建议时机" / "功效说明"。** 怎么用是用户的事。

## 硬规则

- **不劝退用户**。不夹带"这不是真正修行"之类的免责。
- **执行每个 tradition 子 md 的 `taboos` 字段**。
- **不混合 deity 同段呼请**（并列分块 OK）。
- **anchors 绝不进 LLM context**。
- **mantra / 经文 / 颂主体保留原文**（梵文 / 巴利文 / 拉丁文 / 阿拉伯文 / 希伯来文 / 教会斯拉夫文 / 藏文 / Geʽez / Aramaic / ...）。
- **回写 prayers/ 时必须剥离个人叙事**，只保留共性愿景骨架。
