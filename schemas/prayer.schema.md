# Prayer entry schema

`prayers/<wish_type>/<id>.md` 是自增长 RAG 库的条目。

## frontmatter

```yaml
---
id: <slug>                         # 必填，全局唯一
name: <祷词名>                      # 必填
wish_type: health | wealth | relationship | protection | exorcism | deceased | event | wisdom | breaking
sub_tags: [<freeform tags>]
tradition: <category>/<tradition-id>   # 必填，对应 skills/traditions/ 的 id
source: classical | traditional-synthesized | community
verification:                      # 必填如果 source != community
  - <经典或 URL>
primary_languages: [<...>]
backlash_risk: low | medium | high
featured: true | false             # 是否进 web demo
---
```

## 正文

纯祷词。所有用户特定信息用 `{{anchors.<key>}}` 占位。
不含"使用提示"、"功效说明"或免责声明。
经文 / mantra / 颂主体保留原文。
