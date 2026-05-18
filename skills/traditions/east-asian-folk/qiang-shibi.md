---
id: qiang-shibi
name: 羌族释比
name_en: Qiang Shibi
category: east-asian-folk
deity_based: true
self_pray_capable: partial
required_officiants:
  - shibi
officiant_notes: 释比唱经、祭山、送魂、驱邪、还愿等完整仪式须由受传承的释比主持；一般家庭性告祝可自述。
authoritative_texts:
  - "《羌族释比经典·刷勒日》：羌族释比唱经整理本，刷勒日唱段"
  - "《羌族释比经典》：请神、祭山、祓禳、送魂、还愿诸经段"
  - "《中国少数民族古籍总目提要·羌族卷》：释比经典、《刷勒日》条"
  - "《羌族释比文化研究》：释比经文、释比法器、祭祀程序相关章节"
  - "《刷勒日》（Shualeri，释比图经/唱经）相关文献"
primary_languages:
  - qiang
  - chinese
backlash_risk: medium
mitigation: 不代替释比擅行送魂、驱邪、祭山、血祭、还愿等法事；仅保留告祝骨架时应省去秘密经段与法器动作。
taboos:
  - 未受释比师承者不得冒称释比，不得擅唱秘传经段或执法器行完整法事。
  - 丧葬送魂经段不得与婚庆、添丁、还愿等喜庆经段混用。
  - 祭山、还愿、请神、送魂等仪式中忌污言、争斗、戏谑、亵渎白石、羊皮鼓、法杖、神案。
  - 供献、牺牲、洁净、送神等次第不得倒置；已请之神灵祖灵不得不送。
  - 对病灾、亡灵、寨神、山神之名不得任意改写或虚构，以免错请、错送。
  - 不得亵渎白石或山神。
  - 未经传承不得擅自完整表演释比戏剧。
  - 仪式中不得混用不洁之物。
search_strategy: |
  "羌族释比" OR "Qiang Shibi" 刷勒日 OR Shualeri 唱经
  羌族 释比 祭山 OR 驱邪 OR 婚丧仪式
  Qiang shaman rituals modern practice site:edu OR site:cn
  释比 端公 羌族 自念 OR lay
case_index:
  - wish_type: health
    hint: "《刷勒日》病灾祓禳唱段；以释比请神、述病名、祛秽、安魂为正行。"
    officiant: shibi
    primary_language: qiang
  - wish_type: wealth
    hint: "《刷勒日》还愿与家宅兴旺唱段；以告白家门、牲礼愿文、谢神送神为核心。"
    officiant: shibi
    primary_language: qiang
  - wish_type: protection
    hint: "《刷勒日》祭山、护寨、镇宅唱段；以白石、寨神、山神告祝及祓禳为核心。"
    officiant: shibi
    primary_language: qiang
  - wish_type: deceased
    hint: "《刷勒日》丧葬送魂唱段；由释比为亡者开路、指路、送魂，不可自作完整法事。"
    officiant: shibi
    primary_language: qiang
  - wish_type: relationship
    hint: "《刷勒日》婚礼祝颂、家门和合唱段；以祖先告祝、两家名号、祝颂为核心。"
    officiant: shibi
    primary_language: qiang
  - wish_type: wisdom
    hint: "《刷勒日》请师祖与释比传承告祝唱段；以敬师、明心、守规为核心。"
    officiant: shibi
    primary_language: qiang
  - wish_type: breaking
    hint: "《刷勒日》驱邪、解秽、断灾唱段；须释比辨名、祓禳、送离，不可自行代替。"
    officiant: shibi
    primary_language: qiang
  - wish_type: event
    hint: "《刷勒日》出行、建房、迁居、节庆告祝唱段；按事件名告白、请护、谢送。"
    officiant: shibi
    primary_language: qiang
verification:
  - "UNESCO Intangible Cultural Heritage: Qiang New Year festival, https://ich.unesco.org/en/USL/qiang-new-year-festival-00330"
  - "Qiang folk religion, https://en.wikipedia.org/wiki/Qiang_folk_religion"
  - "《羌族释比经典·刷勒日》，羌族口传释比经文整理本"
  - "《刷勒日》释比图经相关文献"
  - "《中国少数民族古籍总目提要·羌族卷》，释比经典、《刷勒日》相关条目"
  - "《羌族释比文化研究》，释比经文与仪式程序章节"
---

# 羌族释比

## 结构
[洁净与陈设白石、神案、法器] → [请释比师祖] → [请天神、寨神或相应神灵] → [告白事由与愿名] → [《刷勒日》唱经正行] → [祓禳、安魂、送魂、祝颂或还愿] → [谢神] → [送神] → [收愿回告祖先]

## 通用骨架（占位符版本）
```
今日在{{anchors.place}}，为{{anchors.petitioner_name}}、{{anchors.household_name}}，告白{{anchors.wish_type}}之事：
{{anchors.petitioner_name}}心中所愿为{{anchors.wish_content}}，
所涉之人名为{{anchors.target_name}}，
所涉之时为{{anchors.event_time}}，
所涉之地为{{anchors.event_place}}。

【请师祖】
Aba Shibi, a-yo, a-yo.
Shibi bba, Shibi ma, a-yo.
Śua-le-ri, Śua-le-ri.

【请天神】
Aba Mubi-ta, a-yo.
Mubi-ta, a-yo, a-yo.
Śua-le-ri, Śua-le-ri.

【请本寨神灵】
{{anchors.local_spirit_name}}, a-yo.
{{anchors.local_spirit_name}}, a-yo.
Śua-le-ri, Śua-le-ri.

【告愿】
{{anchors.petitioner_name}} mi, {{anchors.household_name}} mi,
{{anchors.wish_content}} mi,
a-yo, a-yo.
Śua-le-ri, Śua-le-ri.

【正行唱经】
Śua-le-ri, Śua-le-ri.
Aba Shibi a-yo.
Śua-le-ri, Śua-le-ri.
Mubi-ta a-yo.
Śua-le-ri, Śua-le-ri.
{{anchors.wish_content}} a-yo.
Śua-le-ri, Śua-le-ri.

【若为病灾祓禳】
{{anchors.illness_name}} mi,
{{anchors.patient_name}} mi,
Śua-le-ri, Śua-le-ri.
a-yo, a-yo.

【若为亡者送魂】
{{anchors.deceased_name}} mi,
{{anchors.deceased_lineage}} mi,
Śua-le-ri, Śua-le-ri.
a-yo, a-yo.

【若为还愿祝颂】
{{anchors.vow_name}} mi,
{{anchors.offering_name}} mi,
Śua-le-ri, Śua-le-ri.
a-yo, a-yo.

【谢送师祖】
Aba Shibi, a-yo.
Śua-le-ri, Śua-le-ri.

【谢送天神】
Mubi-ta, a-yo.
Śua-le-ri, Śua-le-ri.

【谢送本寨神灵】
{{anchors.local_spirit_name}}, a-yo.
Śua-le-ri, Śua-le-ri.

愿已告，名已明，事已陈。
为{{anchors.petitioner_name}}、{{anchors.household_name}}收此愿文。
Śua-le-ri, Śua-le-ri.
a-yo, a-yo.
```