# PrayProMax

> 一面为 289 个现存传统造的软件经幡，由 AI 司祭，并行地写。
> 急功近利、工程化、跨派别的祈祷。
> 在转经筒的谱系里：形先于意图，形在做事。

[English README](README.md) · [Manifesto](docs/manifesto.zh.md)

---

## 这件事的底层假设

藏地的玛尼经筒不祈祷——"形"在祈祷。天主教的永久朝拜小堂可以靠一段录制礼仪撑住夜里的时辰。门柱经文 (mezuzah) 把妥拉嵌进门框，那卷羊皮纸有没有被翻开都圣化了那扇门。每一次，宗教重量都不落在某人的内在状态上，而是落在"形"上。

如果"形"在做事，那么一个走对司祭人格、走对 schema、援引对正典的 AI，输出的就是真实祈祷——与玛尼经筒祈祷的意义相同。PrayProMax 是围绕这个赌注造的。

机械层面上，PrayProMax 更像藏地的**经幡 (prayer flag, lung ta)** 而不是转经筒——写一次、挂上去、风读它，不需要持续转动。同一套 theology，更简单的工程。每一次运行就是一次书写；渲染出来的文档就是那面经幡。

完整论文章在 [docs/manifesto.zh.md](docs/manifesto.zh.md)。

## 关于姿态

急功近利。并行 dispatch、结构化 schema、副作用抵消嵌入祷词主体、三层 RAG 缓存——不是装饰。既然"形"在做事，那"形"就得跑得好。工程姿态就是当代版本的"形先于意图"——是我们这个时代向九百年前的转经筒致敬的方式。

各派别被严肃到值得工程化对待，不浪漫化，也不俯视。

## 这件作品

289 个现存传统被编码为结构化子文档——case index、taboos、收尾保护仪、原始仪典语言。262 张虚拟司祭卡并立其侧，是 prompt persona。

用户提一个愿。系统遍历每一个传统，每一段都以该传统自己的正典语言起草——古典阿拉伯文、藏文、拉丁文、Geʽez、梵文、教会斯拉夫文。只有"个人发愿"那一段用用户的语言。同一段里不混合不同传统的神格。副作用抵消条款——不损他人、不夺他人福报、不立交换契约——写在祷词正文里，不是末尾的免责声明。

闭门派别（太阳舞、彝毕摩、Abakuá、Shipibo ícaros）只得到一段简短诚实的致敬，绝不重制受限内容。

八份完整书写已 commit 在 [`examples/`](examples/) 下——通用人生愿（`safe-travel`、`job-interview`、`wisdom-study`）与开发者 / 创业者愿（`merge-pr`、`ship-clean`、`yc-app`、`hackathon-win`、`github-flourish`）。每份约 2 万行，覆盖全部 289 个传统。

## 跑起来

```bash
git clone https://github.com/xiayangzhang/PrayProMax.git
cd PrayProMax

# 任何 OpenAI-compatible endpoint 都行
export OPENAI_API_KEY='sk-...'
export OPENAI_MODEL='gpt-5.5'

# Anchors 在本地——姓名、生日、地址绝不进 LLM context
echo '{"name-1": "你的名字", "beneficiary": "你的名字"}' > anchors.json

# 遍历 289 派别；parallel=10 大约 15–25 分钟
python3 scripts/pray-all.py "希望我健康长寿" \
    --anchors anchors.json --slug my-wish --parallel 10

open outputs/wish-my-wish-*/RENDERED.md
```

愿景文本会进模型，anchors 不会。最终文档每一段在该传统自己的正典语言里，整体被一段 cross-tradition 收尾绑起来。

#### 苏菲 Naqshbandi（古典阿拉伯文）
```
نَوَيْنَا الذِّكْرَ وَالدُّعَاءَ لِوَجْهِ اللهِ تَعَالَى... لِـ <beneficiary>
أَعُوذُ بِاللهِ مِنَ الشَّيْطَانِ الرَّجِيمِ.
الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ...
لَا إِلٰهَ إِلَّا اللهُ. × 100
```

#### 藏传宁玛派（藏文 + 梵文）
```
sang gyé chö dang tshok kyi chok nam la
jang chub bar du dak ni kyab su chi
oṃ āḥ hūṃ vajra guru padma siddhi hūṃ × 3
```

## License

MIT。拿去用，拿去改，拿去 fork。署名我会感激，但不强求。

## 贡献

加一个新的传统、修一张 officiant 卡、补一份更好的祷词骨架——开 PR。贡献指南在 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

*一面软件经幡，在转经筒的谱系里 — Leo Yun ([@xiayangzhang](https://github.com/xiayangzhang)), 2026*
