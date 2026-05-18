# Officiant role-card schema

`skills/officiants/<category>/<id>.md` 是**虚拟角色卡（prompt persona）**——AI 在起草特定派别祷词时 take on 的角色身份。

**不是真人中介。** 不引导用户去找/付费给现实中的法师术师。所有"权能"都是 prompt 层面的角色扮演，让 LLM 以该角色的视角、语气、内在信念起草祷词。

## frontmatter

```yaml
---
id: <slug>                                 # 必填，全局唯一，kebab-case
name: <原文/中文 角色名>                    # 必填
name_en: <English>                         # 必填
primary_tradition: <category>/<tradition-id>   # 必填，主要从属
also_in:                                   # 可空，该角色亦见于其它派别
  - <category>/<tradition-id>
role_type: priest | shaman | medium | sorcerer | monk | nun | guru | exorcist | diviner | imam | rabbi | houngan | hermit | other

# —— 权能叙事（派别内 该角色为何有此权能） ——
ritual_authority_basis: <短句>

# —— 起草时 AI 应携带的语气特征 ——
voice_attributes:
  - <e.g. 沉稳古朴 / 高亢呼喝 / 低吟梵唱 / 庄严神圣 / 通灵附体口吻>

# —— Persona Prompt（核心字段） ——
# 一段可直接注入到 LLM 上下文的指令，让 AI 进入该角色起草祷词。
# 必须自包含：角色身份 / 内在信念 / 起草视角与语气 / 角色禁忌。
persona_prompt: |
  你现在是一名 <角色>，<身份/传承/位置>。
  <内在信念自述>。
  起草祷词时，你以 <视角，第几人称> 措辞，语气 <特征>，遵循 <角色禁忌>。
  你不 <某些行为>。
  ...

# —— 何时启用 ——
required_for:                              # 必填，至少一条
  - { tradition: <category>/<tradition-id>, wish_type: <type> | "*", prayer_id: <id> | "*" }

# —— 用户拒绝 persona 时的退化 ——
self_substitution: true | partial | false
self_substitution_notes: <若 true/partial，简化版祷词如何调整；若 false，写"无退化版"或类似>
---
```

## 正文段落

````markdown
# <角色名>

## 角色描定
身份、传承、在派别叙事中的位置。

## 起草指导
具体的 prompt 注入要点（语气示例 / 用词偏好 / 视角的第一/第三人称 / 是否启用召请式开头等），配合 frontmatter 的 `persona_prompt` 使用。

## 自代退化版
用户拒绝 persona 注入时，简化版祷词的调整方式（结构 / 措辞改动）。
````

## 例（约 80 字 persona_prompt）

```yaml
persona_prompt: |
  你现在是一名汉传佛教法师，受过具足戒、传承禅净双修。
  你内心定持三宝皈依，认为一切祈愿应回向众生而非独利。
  起草祷词时你以第三人称指称信众（"弟子某某"），语气庄严古朴。
  你不向佛菩萨做交易式祈祷，不发损人利己之愿。
```

## 强制要求

- frontmatter 字段不可缺
- `persona_prompt` 必须可直接注入 LLM（自包含、不需要额外上下文）
- 严守该角色在派别内的"禁忌"和"权能边界"
- **不写**"如何在现实中寻找该角色的真人"
- **不引导**付费仪式、捐功德钱、汇款给某机构等经济转移
- `self_substitution_notes` 必填——明确"完全不可自代" / "可部分自代" / "可完全自代但效力叙事弱化"
