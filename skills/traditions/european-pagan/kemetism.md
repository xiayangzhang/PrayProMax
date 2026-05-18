---
id: kemetism
name: Kemetism
name_en: Kemetism
category: european-pagan
deity_based: true
self_pray_capable: partial
required_officiants:
  - kemetic-lector-priest
officiant_notes: "日常赞颂、供献、护佑可自念；涉及开口仪式、亡者名号安置、正式葬仪文本时需诵经祭司或同等主持者。"
authoritative_texts:
  - "Book of the Dead, Spell 15: Hymns to Ra at sunrise and sunset"
  - "Book of the Dead, Spell 30B: Chapter for not letting the heart oppose the deceased"
  - "Book of the Dead, Spell 125: Declaration of Innocence / Negative Confession before the Forty-Two Assessors"
  - "Book of the Dead, Spell 151: Protective formulae for the mummy and burial chamber"
  - "Book of the Dead, Spell 110: Field of Reeds"
  - "Pyramid Texts, Utterance 214: royal solar ascent and identification formulae"
  - "Pyramid Texts, Utterance 600: offering formula and invocation to the gods"
  - "Coffin Texts, Spell 335: becoming a spirit among the akhu"
  - "Offering formula ḥtp-dỉ-nsw in Middle Egyptian funerary stelae"
  - "Metternich Stela: Horus-on-the-crocodiles healing and protection texts"
primary_languages:
  - middle-egyptian-transliteration
  - egyptian
backlash_risk: medium
mitigation: "限于供献、赞颂、正名、护佑与亡者安置；避免以古埃及亡灵文本作威胁、诅咒或商业化戏仿。"
taboos:
  - "不得以祷词助长 isfet：虚假、破坏秩序、蓄意伤害、亵渎神名或亡者名。"
  - "不得偷取、污染、戏弄或虚称献给 nṯrw 与 akhu 的供品。"
  - "不得把 Book of the Dead、Pyramid Texts 等亡灵章句改作诅咒他人的文本。"
  - "不得在同一呼请段落混合多位神明而造成神名、职能与神像的混淆。"
  - "不得伪称自己具备古代祭司职分来主持开口仪式或正式亡者仪轨。"
search_strategy: |
  "Book of the Dead Spell 15 Hymn to Ra transliteration"
  "Book of the Dead Spell 30B heart scarab transliteration ib=i"
  "Book of the Dead Spell 125 Negative Confession transliteration"
  "Pyramid Texts Utterance 600 offering formula htp di nsw"
  "ancient Egyptian offering formula htp di nsw transliteration"
  "Metternich Stela Horus crocodiles healing spell translation transliteration"
  "Coffin Texts Spell 335 becoming akh transliteration"
case_index:
  - wish_type: health
    hint: "Metternich Stela 的 Horus-on-the-crocodiles healing charm，并以 ḥtp-dỉ-nsw 供献式向单一医治性 nṯr 或 nṯrt 正名祈请。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: wealth
    hint: "ḥtp-dỉ-nsw offering formula；以 prt-ḫrw 供献清单祈求 t, ḥnqt, kꜣw, ꜣpdw 等正当供养与家宅丰足。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: protection
    hint: "Book of the Dead Spell 151 protective formulae，并配合 Spell 30B 心章中 m ḏd r=ỉ m mꜣꜥty 的自护句。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: deceased
    hint: "Book of the Dead Spell 15、Spell 110、Spell 125 与 ḥtp-dỉ-nsw n kꜣ n 亡者名；正式葬仪或开口仪式须由 lector-priest 主持。"
    officiant: kemetic-lector-priest
    primary_language: middle-egyptian-transliteration
  - wish_type: relationship
    hint: "Book of the Dead Spell 125 Declaration of Innocence 中不欺、不夺、不扰乱 mꜣꜥt 的誓言结构；配合 Hathor 赞颂式单独呼请。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: wisdom
    hint: "Book of the Dead Spell 125 的 mꜣꜥt 宣告与 Thoth/Djehuty 书写、衡量、正言赞颂式；同段只呼请 Djehuty。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: breaking
    hint: "以 Spell 125 Negative Confession 断绝 isfet、虚言与污染；不使用 execration texts 伤害他人。"
    officiant: none
    primary_language: middle-egyptian-transliteration
  - wish_type: event
    hint: "Book of the Dead Spell 15 Hymn to Ra at sunrise 作为启程、考试、审判、旅途前的正名赞颂；以单一太阳神呼请。"
    officiant: none
    primary_language: middle-egyptian-transliteration
verification:
  - "E. A. Wallis Budge, The Book of the Dead: The Papyrus of Ani, chs. 15, 30B, 110, 125, 151."
  - "R. O. Faulkner, The Ancient Egyptian Book of the Dead, spells 15, 30B, 110, 125, 151."
  - "Raymond O. Faulkner, The Ancient Egyptian Pyramid Texts, Utterances 214 and 600."
  - "James P. Allen, The Ancient Egyptian Pyramid Texts, Writings from the Ancient World, Utterances 214 and 600."
  - "Adriaan de Buck, The Egyptian Coffin Texts, Spell 335."
  - "https://sacred-texts.com/egy/ebod/"
  - "https://sacred-texts.com/egy/pyt/"
  - "https://www.ucl.ac.uk/museums-static/digitalegypt/religion/offering.html"
  - "Metternich Stela, Metropolitan Museum of Art, accession 50.85; Horus-on-the-crocodiles healing texts."
---

# Kemetism

## 结构
[净名与正心] → [单一神名呼请] → [供献式] → [正行章句] → [mꜣꜥt 宣告] → [愿望安置] → [回向给 nṯrw 与 akhu]

## 通用骨架（占位符版本）
```
ỉw=ỉ r ḏd mdw m mꜣꜥt.
rn=ỉ {{anchors.supplicant_ritual_name}}.
ỉb=ỉ wꜥb, r=ỉ mꜣꜥ, ḏrt=ỉ wꜥbt.
n ỉnk ỉr ỉsft.
n ỉnk ḥḏ ḥtpw nṯrw.
n ỉnk šd mꜣꜥt.

dwꜣ {{anchors.netjer_egyptian_name}}.
dwꜣ {{anchors.netjer_egyptian_name}} m wbn=f m ꜣḫt.
ỉꜣw n=k, {{anchors.netjer_egyptian_name}}, nb {{anchors.netjer_domain}}.
di=k mꜣꜥt r st=s, di=k ḥtp r ỉb {{anchors.supplicant_ritual_name}}.

ḥtp dỉ nsw {{anchors.netjer_egyptian_name}} nb {{anchors.netjer_place}}.
dỉ=f prt-ḫrw:
t ḥnqt, kꜣw ꜣpdw, šs mnḫt,
snṯr mrḥt, ḫt nb(t) nfr(t) wꜥb(t),
n kꜣ n {{anchors.supplicant_ritual_name}}.

ỉb=ỉ n mwt=ỉ,
ỉb=ỉ n ḫprw=ỉ,
m ḏd r=ỉ m mꜣꜥty,
m ỉr ḫft r=ỉ m-bꜣḥ nṯr ꜥꜣ.
ỉb=ỉ n mwt=ỉ,
m ḫsf r=ỉ m ḏꜣḏꜣt.

n ỉnk ỉr ỉsft.
n ỉnk ḏd grg.
n ỉnk ỉṯỉ ḫt n nṯr.
n ỉnk ỉṯỉ ḫt n ꜣḫ.
n ỉnk ḥtm rn.
n ỉnk sḫm r ḏrt ḫft mꜣꜥt.

{{anchors.petition_statement}}

di=k {{anchors.request_in_maat}} n {{anchors.supplicant_ritual_name}}.
di=k wꜣḏ ỉb, snb ẖt, ḥtp pr, mꜣꜥ ḫrw.
di=k wḏꜣ, snb, ꜥnḫ m mꜣꜥt.

n kꜣ n {{anchors.deceased_ritual_name}}:
ḥtp dỉ nsw Wsir nb Ḏdw, nṯr ꜥꜣ nb ꜣbḏw,
dỉ=f prt-ḫrw t ḥnqt kꜣw ꜣpdw,
šs mnḫt snṯr mrḥt,
ḫt nb(t) nfr(t) wꜥb(t)
n kꜣ n {{anchors.deceased_ritual_name}},
mꜣꜥ ḫrw.

dwꜣ {{anchors.netjer_egyptian_name}}.
mꜣꜥt rꜥ nb.
ḥtp n nṯrw, ḥtp n ꜣḫw,
ḥtp n {{anchors.supplicant_ritual_name}},
mꜣꜥ ḫrw.
```