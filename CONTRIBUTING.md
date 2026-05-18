# Contributing to PrayProMax

> 冷启动阶段，规则会随仓库一起成熟。

## 可以贡献什么

1. **新派别子文档** — `skills/traditions/<category>/<id>.md`
   - 必须符合 [`schemas/tradition.schema.md`](schemas/tradition.schema.md)
   - 在 `skills/traditions/INDEX.yaml` 同步登记

2. **新虚拟角色卡** — `skills/officiants/<category>/<id>.md`
   - 必须符合 [`schemas/officiant.schema.md`](schemas/officiant.schema.md)
   - 是 prompt persona，**不是真人中介**

3. **已验证祈祷词条目** — `prayers/<wish_type>/<id>.md`
   - 必须符合 [`schemas/prayer.schema.md`](schemas/prayer.schema.md)
   - `source: classical` 必须附经典出处；`source: traditional-synthesized` 必须附 `verification` URLs

4. **跑社区 seeding 脚本** — `scripts/community-seed.*`（待发布）
   - 用你自己的 LLM 凭证认领若干派别 slice，跑完 PR 子 md 回来

## 硬规则

- mantra / 经文 / 颂 主体使用原文（梵文 / 拉丁 / 阿拉伯 / etc.），**不翻译**
- 不在 prayer 条目里写"使用提示" / "功效说明" / "免责声明"
- 不混合 deity 同段呼请（多派别并列分块 OK）
- PII 占位符 `{{anchors.<key>}}` 必须保留，不要硬编码姓名

## 收录原则：有传承

只收录**有传承**的祈祷体系。"传承"指至少满足以下之一：

- 有早于 1800 年的经典文本 / 仪轨文献依据
- 有跨代师徒 / 教派 / 法脉传承链
- 是上述传统的明确分支或复兴（复兴本身可晚近，但原传统古老）

剔除：

- 单一创始人 + 无前接传承 的 20–21 世纪新兴宗教 / 灵性运动 / 能量疗法 / manifestation / dynamic-meditation 系统
- 例：Falun Gong (1992) / Reiki Usui (1922) / Brahma Kumaris (1936) / Self-Realization Fellowship (1920) / Ananda Marga (1955) / ThetaHealing (1995) / Pranic Healing (1987) / EFT (1990s) / Subud (1924) / 圆佛教 (1916) / 甑山道·大巡真理会 (19c末)

边界判断（保留）：

- 19 世纪已成型且持续跨代传承的体系：摩门教 (1830) / 耶和华见证人 (1870s) / 基督教科学派 (1879) / 巴哈伊 (1844) / 天道教 (1860)
- 古传统的现代分支：日莲系新兴宗教（创价学会 / 立正佼成会）保留，因脱胎 13c 日莲

被剔除的条目仍保留在 `INDEX.yaml` 中，但 `status: skipped` + `skip_reason: no-lineage`，以保持清单透明。

## 不接受什么

- 任何"显灵率" / "灵不灵" 的论断
- 任何贬低、嘲讽或攻击某一派别的内容
- 与 schema 不符的子文档
- 引导付费仪式 / 经济转移 / 还愿契约 / 灵魂质押 的内容
- 损人之愿、夺人福报 / 寿数 / 机运的祈祷词

## 提交 PR 即同意

提交 PR 即视为同意按 [AGPL-3.0](LICENSE) 许可贡献。本仓库及其衍生物永远 AGPL-3.0。
不接受 CLA。社区拥有所有 PR 内容；维护者无权 relicense 至更宽松条款。
