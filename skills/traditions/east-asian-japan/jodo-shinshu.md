---
id: jodo-shinshu
name: 浄土真宗
name_en: Jodo Shinshu
category: east-asian-japan
deity_based: false
self_pray_capable: true
required_officiants: []
officiant_notes: 在家可称念念佛、读诵正信偈与御文章；葬儀・法要可由僧侶主持，但并非日常称名的必要条件。
authoritative_texts:
  - "『佛説無量寿経』本願成就文・第十八願"
  - "『佛説観無量寿経』下品下生・称名念佛段"
  - "『佛説阿弥陀経』執持名号段"
  - "親鸞『顕浄土真実教行証文類』行巻・信巻"
  - "親鸞『正信念佛偈』"
  - "親鸞『浄土和讃』『高僧和讃』『正像末和讃』"
  - "蓮如『御文章』"
  - "蓮如『御文章』五帖目第十六通「白骨」"
primary_languages:
  - japanese
  - classical-chinese
backlash_risk: medium
mitigation: 避免把念佛当作治病、求财、驱邪或操控结果的咒术；保持为聞信・報恩・称名・読誦的净土真宗语境。
taboos:
  - 不将「南無阿弥陀仏」作为交换式祈愿、灵验咒、治病咒、招财咒或驱邪咒使用。
  - 不以自力修行、杂行杂修、占卜、吉凶日、物忌、祓除等替代或混同他力信心与念佛。
  - 不在同一祷词段落中混合向诸神、诸佛、灵体作功利性呼请。
  - 不以回向自我功德的方式声称能控制亡者去处；净土真宗语境中以阿弥陀如来本愿为依归。
  - 不把御文章、正信偈、和讃改写成诅咒、断缘、报复或压制他人意志的文本。
search_strategy: |
  "Jodo Shinshu" OR "Shin Buddhism" nembutsu daily practice OR funeral OR memorial
  Jodo Shinshu Hongwanji OR BCA service structure gassho oshoko
  "Namu Amida Butsu" shinjin gratitude lived experience site:reddit.com OR site:buddhistchurchesofamerica.org
  site:hongwanji.or.jp 浄土真宗 南無阿弥陀仏 正信偈 御文章 白骨章
  site:bdkamerica.org Three Pure Land Sutras Larger Sutra eighteenth vow nembutsu
  site:shinranworks.com Shoshinge Namu Amida Butsu Kyogyoshinsho
  浄土真宗 聖典 正信念仏偈 御文章 五帖目 第十六通 白骨
case_index:
  - wish_type: health
    hint: "無治病専用法門；可作報恩称名として「念佛（南無阿弥陀仏）」および「正信念佛偈」を称読する。"
    officiant: none
    primary_language: japanese
  - wish_type: wealth
    hint: "無"
    officiant: none
  - wish_type: protection
    hint: "無護摩・祓除型法門；可作帰依・報恩として「念佛（南無阿弥陀仏）」および「正信念佛偈」を称読する。"
    officiant: none
    primary_language: japanese
  - wish_type: deceased
    hint: "「念佛（南無阿弥陀仏）」「正信念佛偈」「御文章・白骨章」を、亡者追善の呪術ではなく仏恩報謝・聞法の文脈で読誦する。"
    officiant: none
    primary_language: japanese
  - wish_type: relationship
    hint: "無縁結び・復縁専用法門；可作聞信・報恩として「念佛（南無阿弥陀仏）」および「御文章」を読誦する。"
    officiant: none
    primary_language: japanese
  - wish_type: wisdom
    hint: "聞法・信心の文脈で「正信念佛偈」および「念佛（南無阿弥陀仏）」を称読する。"
    officiant: none
    primary_language: japanese
  - wish_type: breaking
    hint: "無"
    officiant: none
  - wish_type: event
    hint: "無成就祈願専用法門；節目の表白として「念佛（南無阿弥陀仏）」「正信念佛偈」「御文章」を読誦する。"
    officiant: none
    primary_language: japanese
verification:
  - "『佛説無量寿経』第十八願：「設我得佛、十方衆生、至心信楽、欲生我国、乃至十念……」"
  - "『佛説阿弥陀経』執持名号段：「聞説阿弥陀佛、執持名号……」"
  - "親鸞『正信念佛偈』冒頭：「帰命無量寿如来　南無不可思議光」"
  - "蓮如『御文章』五帖目第十六通「白骨」"
  - "https://www.bdkamerica.org/product/the-three-pure-land-sutras/"
  - "https://shinranworks.com/"
  - "https://www.hongwanji.or.jp/"
  - "https://en.wikipedia.org/wiki/J%C5%8Ddo_Shinsh%C5%AB"
  - "https://www.buddhistchurchesofamerica.org/"
---

# 浄土真宗

## 结构
[帰敬・称名] → [表白] → [正行：念佛] → [讃偈：正信念佛偈] → [御文章読誦] → [回向]

## 通用骨架（占位符版本）
```
南無阿弥陀仏
南無阿弥陀仏
南無阿弥陀仏

ただ今、{{anchors.context}}にあたり、{{anchors.person_name}}、{{anchors.family_or_group}}とともに、阿弥陀如来の本願を仰ぎ、親鸞聖人のみ教えに依り、称名念佛し、聖教を読誦する。

南無阿弥陀仏
南無阿弥陀仏
南無阿弥陀仏

帰命無量寿如来
南無不可思議光
法蔵菩薩因位時
在世自在王仏所
覩見諸仏浄土因
国土人天之善悪
建立無上殊勝願
超発希有大弘誓

南無阿弥陀仏
南無阿弥陀仏
南無阿弥陀仏

それ、人間の浮生なる相をつらつら観ずるに、おほよそはかなきものはこの世の始中終、まぼろしのごとくなる一期なり。
されば朝には紅顔ありて夕には白骨となれる身なり。
すでに無常の風きたりぬれば、すなはちふたつのまなこたちまちに閉ぢ、ひとつの息ながく絶えぬれば、紅顔むなしく変じて桃李のよそほひを失ひぬるときは、六親眷属あつまりて歎き悲しめども、さらにその甲斐あるべからず。

南無阿弥陀仏
南無阿弥陀仏
南無阿弥陀仏

願以此功徳
平等施一切
同発菩提心
往生安楽国

南無阿弥陀仏
南無阿弥陀仏
南無阿弥陀仏
```