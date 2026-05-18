---
id: shugendo
name: 修験道（山伏）
name_en: Shugendo (Yamabushi)
category: east-asian-japan
deity_based: true
self_pray_capable: partial
required_officiants:
  - yamabushi
officiant_notes: 加持祈祷、護摩、峰中法、柴燈護摩、葬送供養などは修験の伝授と役位を持つ山伏・先達が司る。
authoritative_texts:
  - "般若波羅蜜多心経／摩訶般若波羅蜜多心経 Taishō no. 251"
  - "大楽金剛不空真実三麼耶経般若波羅蜜多理趣品／理趣経 Taishō no. 243"
  - "不動明王真言・不動明王法 真言系次第所収"
  - "光明真言／不空羂索毘盧遮那仏大灌頂光真言 Taishō no. 1002"
  - "役行者本記・神変大菩薩御宝号 南無神変大菩薩"
primary_languages:
  - japanese
  - classical-chinese
  - sanskrit
backlash_risk: medium
mitigation: 未伝授の印明・護摩・峰中法を行わず、公開経文と御宝号に限り、過失は懺悔文と回向で収める。
taboos:
  - 未伝授の秘密真言、印契、護摩次第、峰中作法を自作・公開・代行しない。
  - 山伏、先達、阿闍梨などの位階や所属を偽称しない。
  - 呪詛、報復、他者支配、強制的縁結びを目的に修験の法を用いない。
  - 入峰・行場での殺生、飲酒放逸、穢れを軽んじる行為、無断採取を避ける。
  - 本尊・諸尊・権現を同一段で混同して呼請しない。
search_strategy: |
  site:shugendo.or.jp 修験道 般若心経 不動明王 真言 神変大菩薩
  site:shugendo.or.jp 山伏 加持祈祷 護摩 先達
  SAT Taisho 251 般若心経
  SAT Taisho 243 理趣経
  光明真言 不空羂索毘盧遮那仏大灌頂光真言 Taisho 1002
case_index:
  - wish_type: health
    hint: "薬師如来真言: on korokoro sendari matōgi sowaka を念誦する公開真言系の病気平癒祈願"
    officiant: none
    primary_language: sanskrit
  - wish_type: wealth
    hint: "弁才天真言: on sorasobatei ei sowaka、または大黒天真言を用いる公開真言系の福徳祈願"
    officiant: none
    primary_language: sanskrit
  - wish_type: protection
    hint: "不動明王真言: nōmaku sanmanda bazaradan senda makaroshada sowataya untarata kanman を中心にする身護り祈願"
    officiant: yamabushi
    primary_language: sanskrit
  - wish_type: deceased
    hint: "般若心経・光明真言: on abokya beiroshanō makabodara mani handoma jinbara harabaritaya un による追善回向"
    officiant: yamabushi
    primary_language: classical-chinese
  - wish_type: relationship
    hint: "愛染明王真言: on makara gyabazoro shunikisha bazara satoba jaku un ban koku を用いる和合祈願"
    officiant: yamabushi
    primary_language: sanskrit
  - wish_type: wisdom
    hint: "般若心経: 摩訶般若波羅蜜多心経の読誦による般若・学業成就祈願"
    officiant: none
    primary_language: classical-chinese
  - wish_type: breaking
    hint: "不動明王真言: nōmaku sanmanda bazaradan senda makaroshada sowataya untarata kanman による障碍破り・断ち切りの加持"
    officiant: yamabushi
    primary_language: sanskrit
  - wish_type: event
    hint: "神変大菩薩御宝号: 南無神変大菩薩 と般若心経による入峰・行旅・試験等の発願祈願"
    officiant: none
    primary_language: japanese
verification:
  - "SAT Taishō Tripiṭaka, T0251 摩訶般若波羅蜜多心経: https://21dzk.l.u-tokyo.ac.jp/SAT2018/T0251_.08.0848c.html"
  - "SAT Taishō Tripiṭaka, T0243 大楽金剛不空真実三麼耶経般若波羅蜜多理趣品"
  - "SAT Taishō Tripiṭaka, T1002 不空羂索毘盧遮那仏大灌頂光真言"
  - "Miyake Hitoshi, Shugendō: Essays on the Structure of Japanese Folk Religion, University of Michigan Center for Japanese Studies, 2001"
  - "Gaynor Sekimori, Shugendō: The State of the Field, Monumenta Nipponica 57.2, 2002"
  - "Helen Hardacre, Religion and Society in Nineteenth-Century Japan, Princeton University Press, sections on Shugendō and mountain religion"
---

# 修験道（山伏）

## 结构
[懺悔] → [三帰依] → [発願] → [御宝号] → [般若心経] → [真言] → [祈願成就句] → [回向]

## 通用骨架
```
懺悔文
我昔所造諸悪業　皆由無始貪瞋癡　従身語意之所生　一切我今皆懺悔

三帰依
南無帰依仏　南無帰依法　南無帰依僧
南無本尊界会　南無修験道歴代祖師先徳

発願
謹み敬って、{{anchors.pray_name}}、{{anchors.pray_address}}において、{{anchors.wish_summary}}のため、清浄の心をもって発願し奉る。
願わくは、身口意の過失を懺悔し、{{anchors.target_person}}の障碍を離れ、正しき願いを成就せしめ給え。

御宝号
南無神変大菩薩
南無神変大菩薩
南無神変大菩薩

般若心経
仏説摩訶般若波羅蜜多心経
観自在菩薩　行深般若波羅蜜多時　照見五蘊皆空　度一切苦厄
舎利子　色不異空　空不異色　色即是空　空即是色　受想行識亦復如是
舎利子　是諸法空相　不生不滅　不垢不浄　不増不減
是故空中　無色　無受想行識　無眼耳鼻舌身意　無色声香味触法
無眼界　乃