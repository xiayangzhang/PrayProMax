---
id: romuva
name: Romuva（立陶宛）
name_en: Romuva (Lithuanian)
category: european-pagan
deity_based: true

self_pray_capable: partial
required_officiants:
  - vaidila
officiant_notes: "个人可诵 daina 与家庭火/祖先祷词；婚礼、葬礼、公共 aukuras 祭火等共同体仪式通常由 vaidila/vaidilė 主持。"

authoritative_texts:
  - "Lietuvių liaudies dainynas, vestuvių dainos / kalendorinės dainos / darbo dainos / laidotuvių raudos 各卷"
  - "Lietuvių tautosakos archyvas / Lietuvių literatūros ir tautosakos institutas, dainos, sutartinės, maldelės 条目"
  - "Jonas Trinkūnas, Baltų tikėjimas: lietuvių pasaulėjauta, papročiai, apeigos, ženklai, skyriai apie ugnį, dainas, auką, protėvius"
  - "Jonas Trinkūnas, Lietuvių senosios religijos kelias, skyriai apie Romuvos apeigas ir dainas"
  - "Matthäus Prätorius, Deliciae Prussicae oder Preussische Schaubühne, sections on Žemynėle / Žemynėliauti and household offerings"
  - "Lietuvių tautosaka, t. 1–5, dainos, raudos, sakmės, maldelės"
primary_languages:
  - lithuanian

backlash_risk: medium
mitigation: "仅采用 daina、sutartinė、maldelė 与象征性供奉；不作强迫他人、诅咒、商业化冒称 vaidila 权威或破坏自然/圣火的用法。"
taboos:
  - "不得亵渎 šventa ugnis：不可向祭火投入垃圾、污物或戏谑性物品。"
  - "不得把 daina、rauda、祖先名号用于诅咒、胁迫、羞辱死者或操控他人意志。"
  - "不得在未经共同体授权时冒称 vaidila/vaidilė 主持婚礼、葬礼或公共 aukuras 仪式。"
  - "不得以伤害动物、破坏树木、水源、石丘或 alkas 圣地作为供奉。"
  - "不得把不同 dievai 的呼请混作同一段咒式；应分段、分名号、分供奉。"

search_strategy: |
  Romuva daina prayer Gabija Žemyna Žemynėle žiedkelėle
  site:romuva.lt apeigos dainos ugnis Gabija vaidila
  Lietuvių liaudies dainynas Žemyna Gabija maldelė
  Lithuanian folklore prayer Gabija ugnis Žemyna Prätorius Žemynėliauti
  Romuva funeral rauda vėlės daina vaidila
  sutartinės Lithuanian multipart songs UNESCO Romuva ritual

case_index:
  - wish_type: health
    hint: "Gabija maldelė「Šventa Gabija, būk rami」与 daina 型祷句，向家庭圣火求平安、体身 darna。"
    officiant: none
    primary_language: lithuanian
  - wish_type: wealth
    hint: "Žemyna/Žemynėlė daina-maldelė「Žemynėle žiedkelėle, žydėk rugiais, kviečiais…」用于土地、谷物、家计丰足。"
    officiant: none
    primary_language: lithuanian
  - wish_type: protection
    hint: "Perkūnas 呼请「Perkūne dievaiti」与 aukuras 火前 daina，用于雷神守护与驱散不和。"
    officiant: none
    primary_language: lithuanian
  - wish_type: deceased
    hint: "Vėlinės rauda / vėlės maldelė「Vėlelės mūsų…」；家庭追念可自诵，葬礼 rauda 与共同体送灵通常由 vaidila/vaidilė 主持。"
    officiant: vaidila
    primary_language: lithuanian
  - wish_type: relationship
    hint: "Laima daina 与 vestuvių daina；个人可向 Laima 求缘分之 darna，婚礼契约性仪式由 vaidila/vaidilė 主持。"
    officiant: vaidila
    primary_language: lithuanian
  - wish_type: wisdom
    hint: "Dievas / Saulė daina，如「Saulele motule」型呼请，用于明心、正念与秩序。"
    officiant: none
    primary_language: lithuanian
  - wish_type: breaking
    hint: "无；Romuva 规范中不以 daina 作诅咒、强制断缘或攻击性解咒。"
    officiant: none
  - wish_type: event
    hint: "Aukuras ugnies apeiga 与 proginės dainos；个人行旅/考试可用 Gabija 或 Saulė daina，公共节庆、命名、婚礼、葬礼由 vaidila/vaidilė 主持。"
    officiant: vaidila
    primary_language: lithuanian

verification:
  - "https://romuva.lt/"
  - "https://ich.unesco.org/en/RL/sutartines-lithuanian-multipart-songs-00433"
  - "https://www.vle.lt/straipsnis/romuva/"
  - "Lietuvių literatūros ir tautosakos institutas, Lietuvių tautosakos rankraštynas / Lietuvių liaudies dainynas"
  - "Jonas Trinkūnas, Baltų tikėjimas: lietuvių pasaulėjauta, papročiai, apeigos, ženklai. Vilnius: Diemedis, 2000."
  - "Matthäus Prätorius, Deliciae Prussicae oder Preussische Schaubühne, 17th c., passages on Žemynėle and Žemynėliauti."
---

# Romuva（立陶宛）

## 结构
[净火与定向] → [Gabija 圣火呼请] → [祖先 vėlės 迎请] → [按愿望选择单一 dievas/deivė 的 daina/maldelė 正行] → [供奉与陈愿] → [darna 归整] → [谢辞与送返]

## 通用骨架（占位符版本）
```
Ugnie šventa, Gabija,
būk rami, būk gera,
būk soti ant savo vietos.

Gabija, sukurta, pakurta,
neužgauk, negesk,
saugok {{anchors.home}},
saugok {{anchors.name}}.

Vėlelės mūsų,
ateikit, pasivaišinkit,
prisiminkit {{anchors.ancestor_names}},
palaiminkit {{anchors.name}}.

{{anchors.deity_section}}

Žemynėle žiedkelėle,
žydėk rugiais, kviečiais,
miežiais ir visais javais.
Priimk {{anchors.offering}},
laikyk darną {{anchors.place}}.

{{anchors.petition_lithuanian}}

Darna tegu būna širdyje,
darna tegu būna namuose,
darna tegu būna žemėje.

Ugnie šventa, Gabija,
ačiū už šviesą,
ačiū už šilumą,
lik rami, lik gera.
```