# Tradition sub-document schema

每个 `skills/traditions/<category>/<id>.md` 必须严格符合本 schema。

## frontmatter (YAML)

```yaml
---
id: <slug>                         # 必填，全局唯一，kebab-case
name: <中文/原文 派别名>            # 必填
name_en: <English name>            # 必填
category: <分类>                   # 必填，见下方枚举
deity_based: true | false          # 必填

# —— officiant / 主持角色 ——
self_pray_capable: true | false | partial   # 必填。partial = 部分祷词可自念，部分必须法师
required_officiants:                         # self_pray_capable != true 时必填；
  - <officiant-id>                          # 引用 skills/officiants/<category>/<id>.md 的 id
officiant_notes: <短句>                     # 可选，对 officiant 必要性的补充

# —— 文本依据 ——
authoritative_texts:               # 必填，可空数组
  - <经典名 + 章节/出处>
primary_languages:                 # 必填，按祷词主体使用的语言
  - <e.g. sanskrit, pali, classical-arabic, biblical-hebrew, latin, geez, aramaic, church-slavonic, tibetan, ...>

# —— 安全与规范 ——
backlash_risk: low | medium | high # 必填
mitigation: <短句>                  # 必填
taboos:                            # 必填，可空数组
  - <禁忌 1>

# —— 调度信息 ——
search_strategy: |                  # 必填，给后续 agent 使用的实测有效查询
  <查询模板 1>
  <查询模板 2>

case_index:                        # 必填。按 wish_type 罗列；同 wish_type 可多 entry（按 officiant 区分）
  - wish_type: health
    hint: <祷法描述>
    officiant: none | <officiant-id>
    primary_language: <e.g. sanskrit>      # 可选，该 case 主体语言（若与 tradition 默认不同）
  - wish_type: wealth
    hint: ...
    officiant: ...
  - wish_type: protection
    ...
  - wish_type: deceased
    ...
  - wish_type: relationship
    ...
  - wish_type: wisdom
    ...
  - wish_type: breaking            # 破除 / 解咒 / 切断
    ...
  - wish_type: event               # 特定事件 / 考试 / 行旅
    ...

verification:                      # 可选，引用来源 URL / 经文位置
  - <URL or citation>
---
```

## category 枚举

- `east-asian-han` — 道教 / 汉传佛教 / 中国民俗
- `east-asian-japan` — 神道 / 日本佛教各派 / 新兴
- `east-asian-korea` — 巫俗 / 天道教 / etc.
- `east-asian-folk` — 中国少数民族 / 跨境民俗
- `southeast-asia` — 东南亚体系
- `south-asia` — 印度教各派 / 锡克 / 耆那 / 尼泊尔 / 斯里兰卡
- `tibetan-himalayan` — 藏传佛教各派 / 苯教 / 不丹
- `abrahamic-judaism` — 犹太教各支
- `abrahamic-christianity` — 基督教各支
- `abrahamic-islam` — 伊斯兰各支
- `abrahamic-other` — 巴哈伊 / 曼达 / 雅兹迪 / 拉斯塔法里 / etc.
- `western-occult` — 仪式魔法 / 神秘学 / 西方现代魔法
- `european-pagan` — 欧洲本土异教复兴
- `african-diasporic` — 非洲及其离散裔
- `americas-indigenous` — 美洲原住民及其衍生
- `north-asian-shamanic` — 北亚 / 中亚 / 西伯利亚萨满
- `oceanic` — 大洋洲
- `modern-energy-newage` — 灵气 / Theta / Pranic / 新时代仪式

## wish_type 枚举（八类）

`health / wealth / protection / deceased / relationship / wisdom / breaking / event`

某派别对某 wish_type 无对应法门则填 `hint: 无, officiant: none`。

## 正文段落

文件正文必须包含以下两个段落，顺序固定：

````markdown
# <派别名>

## 结构
祷词的组成顺序，如：[皈依] → [发愿] → [正行] → [回向]

## 通用骨架（占位符版本）
```
<完整祷词骨架，用户特定信息用 {{anchors.<任意key>}} 占位>
<经文/咒语主体必须使用原文（罗马化或原始文字皆可，但保持音准）>
```
````

## 强制要求

- frontmatter 字段不可缺
- 通用骨架中**所有用户特定信息**用 `{{anchors.<key>}}` 占位
- 经文 / 咒语 / 颂的主体**必须使用原文**，不要翻译（罗马化或原始文字皆可）
- 不要写"使用提示"、"建议时机"、"功效说明"——只描述祷词本身及其内部规范
- `officiant: none` 必须显式写出（不允许省略）以确认"该 case 用户可自念"
- 若引用 `<officiant-id>` 但 `skills/officiants/` 下还没有对应文件，worker 必须同时产出该角色卡
