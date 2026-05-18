# PrayProMax

**急功近利地工程化祈祷。**

把全世界宗教 / 玄学体系中的祈祷术统一编码为可调度的 skill / prompt 库。
用户给出愿望（+ 可选身份锚定），AI 遍历所有派别，从相关者中起草，合并为按规范的祈祷词 md。

## 项目定位

- **不质疑玄学本身。** 我们只是把"急功近利、有针对性、高效率的祈祷"这件早已存在的事工程化。
- **不冒犯。** 历史上每种主流传统都早已有自己的"急功近利祈祷范式"：
  - 藏传转经筒、念珠、玛尼石堆 — 重复祈祷的工程化
  - 天主教 Novena（连续 9 日祷）、玫瑰经 — 结构化批量
  - 伊斯兰 Tasbih 念珠（33×3）— 同上
  - 道教科仪、符箓 — 制式化感应
  - 犹太教 Tehillim 集体念诵 — 群体并行
  - 西方 grimoire 与 chaos magic sigil — 显式的"工程化巫术"

  PrayProMax 把这些散落的范式统一编码为可调度的 skill 库，**不评判灵不灵，只保证规范合规**。

## 当前状态 (v0.1)

- **291 个 seeded traditions** 覆盖 18 大类
- **263 个 officiant 卡**（虚拟 prompt persona，对应所有需要法师/术师/僧侣等专人主持的场景）
- **3-tier RAG 缓存**：prayers/ → tradition.case_index → grok web search fallback
- 一次 pray flow 端到端 ~14 分钟（291 派别全遍历）
- AGPL-3.0 license

## 架构

```
PrayProMax/
├── skills/
│   ├── pray/SKILL.md              # root 调度 skill（用户面）
│   ├── traditions/                # 派别子文档
│   │   ├── INDEX.yaml             # 345 条派别 + 元数据
│   │   ├── _template.md           # 子 md 模板
│   │   └── <category>/<id>.md     # 291 个 seeded
│   └── officiants/                # 虚拟 prompt persona（NOT 真人中介）
│       └── <category>/<id>.md     # 263 个 officiant 卡
├── prayers/                       # 自增长的祈祷词 RAG 知识库
│   ├── INDEX.json
│   └── <wish_type>/<id>.md        # 脱敏骨架（社区贡献回流的核心）
├── schemas/
│   ├── tradition.schema.md
│   ├── officiant.schema.md
│   └── prayer.schema.md
├── scripts/
│   ├── sub2api.py                 # OpenAI-compat caller (路由 gpt/grok key)
│   ├── render-prompt.py           # template 渲染
│   ├── dispatch-seed.py           # Phase E 派别 seeding (codex+grok 双 worker + merge)
│   ├── dispatch-officiants.py     # officiant 卡批量生成
│   ├── pray-all.py                # 用户面：全 291 遍历 + 3-tier RAG + enrichment 暂存
│   ├── review-seeded.py           # 静态 schema + 内容质量扫
│   └── seed-prompts/              # worker prompt 模板
├── docs/
│   ├── architecture.md            # 数据模型 + dispatcher + pray pipeline 全图
│   ├── feedback-loop.md           # 社区贡献循环 + PR 流 + agent review gate
│   └── seeding-pipeline.md        # Phase A–E 冷启动复盘 + 社区复制指南
└── ref.md                         # 派别清单原始资料（seed source）
```

## 用户工作流（一次 pray flow）

```
wish (text) + anchors (LOCAL-only key-value)
   │
   │  classify → wish_type ∈ {health, wealth, protection, deceased,
   │              relationship, wisdom, breaking, event}
   │  safety check → refuse if HARMFUL (wishes harm to others)
   ▼
遍历 291 派别 (parallel=10):
   ├─ L1: prayers/ RAG hit?          (0 search cost — 别人沉淀的骨架)
   ├─ L2: tradition.case_index hint? (低成本 LLM 起草)
   └─ L3: grok --search fallback     (有成本，但找到的会 stage 为 PR candidate)
   │
   ▼
draft per tradition (原文 mantra 保留 + {{anchors.*}} 占位)
   │
   ▼
synthesize universal closing (cross-tradition 总回向 + no-harm + no-exchange)
   │
   ▼
render anchors locally → outputs/wish-<slug>-<ts>/RENDERED.md
also: placeholders/ (PII-free) → 可贡献回 prayers/
also: PR-CANDIDATE.md (L3 enrichments 待社区贡献)
```

## 硬约束

- **anchors 绝不进 LLM context** — 完全本地脱敏；所有 LLM 看到的都是 `{{anchors.<key>}}` 占位符；本地渲染发生在最后
- **mantra / 经文 / 颂主体保留原文** — 梵文 / 巴利文 / 拉丁文 / 阿拉伯文 / 希伯来文 / 教会斯拉夫文 / 藏文 / Geʽez / Aramaic / ...；用户语言（中文）只用于个人发愿陈述段
- **不混合 deity 同段呼请** — 多派别并列分块 OK
- **执行每个 tradition 子 md 的 `taboos` 字段**
- **lineage 规则** — 仅收录有传承的（详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)）

### 副作用 / 代价 / 交换处理（part of prayer body，非 metadata）

- 高 `backlash_risk` 派别：自动嵌入该派别 `mitigation` 作收尾保护仪 (回向 / 净化 / 谢神 / 护身咒)
- **No-harm clause**：不为损人之愿起草
- **No-deprivation clause**：求财 / 求寿 / 求成功 → 必加"不夺他人福报、寿数、机运"句
- **No quid-pro-quo / 无交换 / 无还愿债**：不立"如蒙允 / 我必 X" 式契约；不含付费 / 牺牲 / 灵魂质押
- **Cross-tradition 总回向**：session 末尾合成统一闭式，覆盖以上各条 + 法界回向

## 怎么用

### 用 pray skill 跑一个愿

```bash
# anchors.json: {"name-1": "...", "beneficiary": "...", ...}
python3 scripts/pray-all.py "你的愿望" --anchors anchors.json --slug my-wish --parallel 10
```

输出在 `outputs/wish-<slug>-<ts>/`。带 anchors 的渲染版仅本地存在；脱敏版可贡献回 `prayers/`。

### 想贡献新派别 / 修补现有派别

详见 [`CONTRIBUTING.md`](CONTRIBUTING.md) 和 [`docs/seeding-pipeline.md`](docs/seeding-pipeline.md)。

### 想理解整套架构

- [`docs/architecture.md`](docs/architecture.md) — 数据模型 + 流水线
- [`docs/feedback-loop.md`](docs/feedback-loop.md) — 社区贡献循环 + PR review gate
- [`docs/seeding-pipeline.md`](docs/seeding-pipeline.md) — 冷启动复盘

## License

[AGPL-3.0](LICENSE) — strong copyleft. 

衍生作品（包括 SaaS 形式提供服务者）必须以 AGPL-3.0 开源全部源代码 + 衍生数据。
我们希望 PrayProMax 永远是公共的工程化祈祷库；衍生者继续公共，则不必造轮子。
