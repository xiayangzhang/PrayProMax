---
id: dievturiba
name: Dievturība（拉脱维亚）
name_en: Dievturība (Latvian)
category: european-pagan
deity_based: true

self_pray_capable: true
required_officiants: []
officiant_notes: "个人 dainas 诵唱、daudzinājums 与家内纪念可自念；正式社群 rite 另可由 dievturu vadonis 主持。"

authoritative_texts:
  - "Krišjānis Barons and H. Visendorfs, Latvju Dainas, thematic sections: Dievs; Laima; Māra; Saule; Veļi; Jāņi; Kāzas; Bēres"
  - "Ernests Brastiņš, Dievturu cerokslis (1932), sections: Dievs; Dievatziņa; Tikums; Daudzinājumi; Gadskārtas"
  - "Krišjānis Barons, Latvju Dainas, prayer-daina incipits including 'Dievs, dod man kalnā kāpt' and 'Dod, Dieviņi, otram dot'"
primary_languages:
  - latvian

backlash_risk: medium
mitigation: "保持 dainas 原文与单一呼请对象；避免把 Latvian 民族宗教文本改写为诅咒、商业化咒术或与无关神名混合。"
taboos:
  - "不得把 dainas 或 daudzinājums 用作伤害、强迫他人意志或诅咒的工具。"
  - "同一祷段不得混合呼请无关神祇、圣徒或外来仪式权威。"
  - "不得把现代 Dievturība 的无血祭、歌诵与德行取向改写为动物牺牲或血祭。"
  - "不得随意篡改 dainas 的核心词句来冒充传统原文。"

search_strategy: |
  site:dainuskapis.lv "Dievs, dod man kalnā kāpt"
  site:dainuskapis.lv "Dod, Dieviņi, otram dot"
  site:garamantas.lv "Latvju Dainas" "Dievs" "Laima" "Māra" "Veļi"
  "Ernests Brastiņš" "Dievturu cerokslis" "Daudzinājumi"
  "Dievturība" "dainas" "daudzinājums" "Dievs" "Laima"

case_index:
  - wish_type: health
    hint: "以 daina-prayer《Dievs, dod man kalnā kāpt》为核心，向 Dievs 陈述身体与心志的扶正。"
    officiant: none
    primary_language: latvian
  - wish_type: wealth
    hint: "以 daina-prayer《Dod, Dieviņi, otram dot》为核心，按 Dievturība 的 tikums 伦理表达正当生计与慷慨。"
    officiant: none
    primary_language: latvian
  - wish_type: protection
    hint: "以 daina-prayer《Dievs, dod man kalnā kāpt》为核心，作不混神名的 Dievs daudzinājums。"
    officiant: none
    primary_language: latvian
  - wish_type: deceased
    hint: "以 veļu piemiņa dainas《Veļu māte, saņem mani》或同类 Veļi/Bēres dainas 为核心，作亡者纪念而非召役亡灵。"
    officiant: none
    primary_language: latvian
  - wish_type: relationship
    hint: "以 wedding/household dainas 中的《Dievs, dod man otram dot》伦理句式为核心，表达和合、互惠与不强迫。"
    officiant: none
    primary_language: latvian
  - wish_type: wisdom
    hint: "以 daina-prayer《Dievs, dod man kalnā kāpt》为核心，祈求清明心志、正直判断与 tikums。"
    officiant: none
    primary_language: latvian
  - wish_type: breaking
    hint: "无攻击性解咒法；仅可用 daina-prayer《Dievs, dod man kalnā kāpt》作自我扶正与断离不义牵缠的非伤害祷词。"
    officiant: none
    primary_language: latvian
  - wish_type: event
    hint: "以 daina-prayer《Dievs, dod man kalnā kāpt》为核心，按具体事件陈述正当行程、考试、迁居或工作。"
    officiant: none
    primary_language: latvian

verification:
  - "Krišjānis Barons and H. Visendorfs, Latvju Dainas, 6 vols., Jelgava/St. Petersburg, 1894–1915."
  - "Ernests Brastiņš, Dievturu cerokslis, Rīga, 1932."
  - "https://dainuskapis.lv/"
  - "https://garamantas.lv/"
  - "https://en.wikipedia.org/wiki/Dievtur%C4%ABba"
  - "https://en.wikipedia.org/wiki/Latvju_dainas"
---

# Dievturība（拉脱维亚）

## 结构
[Daudzinājums / 称颂单一呼请对象] → [Daina 原文诵唱] → [以 tikums 伦理陈述愿望] → [再次诵唱核心 daina 句] → [Slēgums / 收束]

## 通用骨架（占位符版本）
```
Dievs, Dieviņ, labais devēj,
stāv pie {{anchors.person_name}},
stāv pie {{anchors.place_name}},
stāv pie {{anchors.wish_name}}.

Dievs, dod man kalnā kāpt,
Ne no kalna lejiņā;
Dievs, dod man otram dot,
Ne no otra mīļi lūgt.

Par {{anchors.person_name}} un {{anchors.wish_name}} es saku taisnu vārdu:
lai mana doma ir skaidra,
lai mans darbs ir godīgs,
lai mans ceļš ir taisns,
lai mana roka nedara pāri {{anchors.other_person_or_none}}.

Dod, Dieviņi, otram dot,
Ne no otra mīļi lūgt;
Otram devu, sev palika,
Savu mūžu dzīvojot.

Dievs, Dieviņ, labais devēj,
pieņem šo vārdu par {{anchors.person_name}},
pieņem šo dainu par {{anchors.wish_name}}.

Lai top.
```