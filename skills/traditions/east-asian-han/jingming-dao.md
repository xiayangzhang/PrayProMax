---
id: jingming-dao
name: 净明道
name_en: Jingming Dao
category: east-asian-han
deity_based: true
self_pray_capable: partial
required_officiants:
  - daoist-priest
officiant_notes: 日常忏悔、诵偈、发愿可自念；正式斋醮、济度、章表、奏告等科仪须由道士主持。
authoritative_texts:
  - 《净明忠孝全书》卷一至卷六，收入《正统道藏》
  - 《太上灵宝净明洞神上品经》，收入《正统道藏》洞神部
  - 《太上灵宝净明飞仙度人经法》，净明、灵宝度亡科仪传统相关经典
  - 《许真君仙传》及《许太史真君图传》，收入《正统道藏》
  - 《许真君宝诰》，许真君信仰诵持传统
  - 《净明忏悔文》，净明派忏悔科诵传统
  - 《净明八宝偈》，净明派忠孝伦理偈颂传统
primary_languages:
  - classical-chinese
backlash_risk: medium
mitigation: 避免把净明忏悔与八宝偈用于诅咒、驱使、求邪财或替代正式斋醮；涉及亡者、章表、解厄等正式科仪时交由道士主持。
taboos:
  - 不得违背忠、孝、廉、慎、宽、裕、容、忍之净明八宝。
  - 不得以净明名义行杀害、盗取、邪淫、妄语、欺诈、诅咒、役鬼害人。
  - 不得轻慢天地、祖先、父母、师长、道经师三宝。
  - 不得把忏悔文作为推卸罪责或规避赔偿、和解、改过的手段。
  - 不得将亡者济度、章表奏告、祈禳解厄等正式科仪冒充为个人私念即可完成。
  - 不得纵忿恣欲。
  - 不得欺心昧理。
search_strategy: |
  "净明道 净明八宝偈" OR "净明忠孝全书 忏悔"
  "净明道 早晚课" OR "许真君宝诰 诵读"
  "Jingming Dao modern practice" OR "净明道 居家修行"
  site:reddit.com OR site:daoist.org "Jingming" OR "净明道"
case_index:
  - wish_type: health
    hint: 以《净明忏悔文》忏罪改过，续诵《净明八宝偈》发忠孝廉慎宽裕容忍之愿。
    officiant: none
    primary_language: classical-chinese
  - wish_type: wealth
    hint: 无
    officiant: none
  - wish_type: protection
    hint: 以《净明忏悔文》净心悔过，称念许真君圣号，续诵《净明八宝偈》守八宝戒德。
    officiant: none
    primary_language: classical-chinese
  - wish_type: deceased
    hint: 亡者荐度不以私念代替科仪；须由道士依净明、灵宝斋醮传统行济度科，并可纳入《净明忏悔文》。
    officiant: daoist-priest
    primary_language: classical-chinese
  - wish_type: relationship
    hint: 以《净明忏悔文》忏悔不孝不忠、不宽不容之过，续诵《净明八宝偈》发和合伦理愿。
    officiant: none
    primary_language: classical-chinese
  - wish_type: wisdom
    hint: 以《净明八宝偈》为主，发忠孝廉慎宽裕容忍之愿，辅以《净明忏悔文》净心。
    officiant: none
    primary_language: classical-chinese
  - wish_type: breaking
    hint: 破除罪咎、恶习、怨结可用《净明忏悔文》与《净明八宝偈》；正式解厄、禳灾、章表奏告须由道士主持。
    officiant: daoist-priest
    primary_language: classical-chinese
  - wish_type: breaking
    hint: 日常断恶习可自诵忏悔文，惩忿窒欲，依八宝自省改过；不作正式解厄、禳灾、章表奏告。
    officiant: none
    primary_language: classical-chinese
  - wish_type: event
    hint: 特定事务以《净明忏悔文》先忏悔身口意过，继诵《净明八宝偈》发正愿。
    officiant: none
    primary_language: classical-chinese
verification:
  - 《正统道藏》本《净明忠孝全书》，卷一至卷六。
  - 《正统道藏》洞神部《太上灵宝净明洞神上品经》。
  - 《太上灵宝净明飞仙度人经法》，道藏净明、灵宝度亡科仪相关资料。
  - Kristofer Schipper and Franciscus Verellen, eds., The Taoist Canon: A Historical Companion to the Daozang, entries on Jingming texts and Jingming zhongxiao corpus.
  - Fabrizio Pregadio, ed., The Encyclopedia of Taoism, Routledge, entries “Jingming dao” and “Xu Xun”.
  - https://zh.wikipedia.org/wiki/%E5%87%80%E6%98%8E%E9%81%93
  - https://en.wikipedia.org/wiki/Jingming_Dao
  - https://longhumountain.com/blogs/introduction-to-taoism-q-a/what-is-pure-brightness-daoism-净明道
---

# 净明道

## 结构
[净坛肃心] → [皈依道经师] → [礼敬太上] → [礼敬许真君] → [自陈姓名与所愿] → [净明忏悔] → [净明八宝偈] → [发愿守八宝] → [回向]

## 通用骨架（占位符版本）
```
志心皈命礼。

一心皈依无上道宝。
一心皈依无上经宝。
一心皈依无上师宝。

志心礼太上道祖。

志心礼净明祖师许真君。

弟子 {{anchors.devotee_name}}，居处 {{anchors.location}}，今为 {{anchors.wish_intent}}，稽首归命，忏悔身口意诸过，愿以忠孝为本，以净明为心。

志心忏悔。
弟子 {{anchors.devotee_name}}，自从无始以来，至于今日，身业不净，口业不净，意业不净；
或不忠不孝，或不廉不慎，或不宽不裕，或不容不忍；
或轻慢天地，或违逆父母，或欺罔师长，或损害含生；
今对道前，披露忏悔。
所作诸过，愿从今日，悉皆改悔；
所起诸恶，愿从今日，永不复作。

伏愿太上垂慈，令弟子 {{anchors.devotee_name}} 心地净明，罪咎消释，道愿坚固。

伏愿许真君鉴照，令弟子 {{anchors.devotee_name}} 心地净明，罪咎消释，道愿坚固。

净明八宝偈：
一宝忠兮二宝孝，
三宝廉兮四宝慎，
五宝宽兮六宝裕，
七宝容兮八宝忍。
忠孝廉慎，宽裕容忍；
净明心地，内外光明。

弟子 {{anchors.devotee_name}} 发愿：
愿以忠事所当事，愿以孝亲所当亲；
愿以廉绝非分，愿以慎守身心；
愿以宽待众生，愿以裕济贫乏；
愿以容化怨结，愿以忍息嗔争。
凡所祈愿 {{anchors.wish_intent}}，不违正道，不害众生，不损阴德，不背净明八宝。

愿以此忏悔诵偈功德，
上报天地祖师真君之恩，
次报父母师长之恩，
普及 {{anchors.dedication_target}}。
愿存者安宁，亡者超宁；
怨结解释，罪障消除；
弟子 {{anchors.devotee_name}} 与一切有情，
同归净明，同契真道。

志心稽首礼。
```