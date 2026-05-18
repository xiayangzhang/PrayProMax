---
id: jinja-shinto
name: 神社神道
name_en: Jinja Shinto
category: east-asian-japan
deity_based: true

self_pray_capable: partial
required_officiants:
  - jinja-kannushi
officiant_notes: 正式な神社祭祀・祈願祭・葬祭・厄除祓は神職が祝詞を奏上する。

authoritative_texts:
  - "延喜式 巻八 祝詞: 祈年祭, 月次祭, 大殿祭, 大祓"
  - "延喜式 巻九・巻十 神名帳"
  - "古事記 上巻: 伊邪那岐命の禊祓"
  - "日本書紀 巻第一 神代上: 伊弉諾尊の禊祓"
  - "神社本庁『神社祭式同行事作法』: 修祓, 祝詞奏上, 玉串拝礼"
  - "天津祝詞（Amatsu Norito）"
primary_languages:
  - classical-japanese
  - japanese

backlash_risk: medium
mitigation: 穢れ・不敬・私的改作を避け、正式祭祀や葬祭は神職に依頼し、祓と敬拝の形式に戻す。
taboos:
  - 神前での不敬語・虚偽申告・呪詛的願意を禁ずる。
  - 死穢・血穢・忌中など重い穢れを負ったまま正式祭祀に関与することを避ける。
  - 神饌・玉串・神札・神前を粗末に扱うことを禁ずる。
  - 祝詞を怨敵調伏・害意成就の文脈に改作しない。
  - 祭神名・鎮座地・願主名を乱雑に取り違えない。
  - 穢れた状態で神域に近づくことを避ける。
  - 祓・潔斎を経ずに神体へ直接触れることを避ける。
  - 血食供物を避ける。

search_strategy: |
  "norito" OR 祝詞 Jinja Shinto home practice OR self prayer
  "Hi Fu Mi norito" OR "Amatsu Norito" text
  Shinto prayer for health wealth protection modern practitioner
  site:reddit.com OR site:facebook.com Jinja Shinto norito examples

case_index:
  - wish_type: health
    hint: 祓詞（Harae-kotoba）と大祓詞（Ōharae no Kotoba）を核にした健康祈願祝詞。
    officiant: none
    primary_language: classical-japanese
  - wish_type: wealth
    hint: 延喜式祝詞「祈年祭祝詞（Toshigoi no Matsuri no Norito）」の豊穣・生業繁栄系譜に属する商売繁昌祈願祝詞。
    officiant: jinja-kannushi
    primary_language: classical-japanese
  - wish_type: wealth
    hint: 家庭・個人の簡略拝礼では、五穀豊穣・商売繁昌・稲荷信仰系の願意を通用祝詞に述べる。
    officiant: none
    primary_language: classical-japanese
  - wish_type: protection
    hint: 大祓詞（Ōharae no Kotoba）および祓詞（Harae-kotoba）を中心にした厄除・災難除の祓祈願。
    officiant: none
    primary_language: classical-japanese
  - wish_type: deceased
    hint: 神葬祭の葬場祭祝詞・遷霊祭祝詞・祖霊祭祝詞。
    officiant: jinja-kannushi
    primary_language: classical-japanese
  - wish_type: deceased
    hint: 家庭の祖霊拝礼では、慰霊・安魂・感謝を通用祝詞に述べる。
    officiant: none
    primary_language: classical-japanese
  - wish_type: relationship
    hint: 縁結び祈願祝詞（Enmusubi Kigan Norito）。
    officiant: jinja-kannushi
    primary_language: classical-japanese
  - wish_type: relationship
    hint: 家庭・個人の簡略拝礼では、良縁・家内和合の願意を通用祝詞に述べる。
    officiant: none
    primary_language: classical-japanese
  - wish_type: wisdom
    hint: 学業成就祈願祝詞（Gakugyō Jōju Kigan Norito）および天満宮系の天神祝詞。
    officiant: jinja-kannushi
    primary_language: classical-japanese
  - wish_type: wisdom
    hint: 家庭・個人の簡略拝礼では、学問・明察・判断の願意を通用祝詞に述べる。
    officiant: none
    primary_language: classical-japanese
  - wish_type: breaking
    hint: 大祓詞（Ōharae no Kotoba）と祓詞（Harae-kotoba）による罪穢・禍事の祓。
    officiant: none
    primary_language: classical-japanese
  - wish_type: event
    hint: 旅行安全祈願祝詞・交通安全祈願祝詞・地鎮祭祝詞など、事由別祈願祭祝詞。
    officiant: jinja-kannushi
    primary_language: classical-japanese
  - wish_type: event
    hint: 家庭・個人の簡略拝礼では、試験・旅行・行事安全など特定事項を通用祝詞に述べる。
    officiant: none
    primary_language: classical-japanese

verification:
  - "Engi-shiki, Book 8, Norito: Toshigoi no Matsuri, Tsukinami no Matsuri, Ōtono no Matsuri, Ōharae"
  - "Kojiki, Kamitsumaki: Izanagi no mikoto no misogi-harae"
  - "Nihon Shoki, Book 1, Age of the Gods: Izanagi no mikoto no misogi-harae"
  - "Engishiki Norito classical texts"
  - "https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9754"
  - "https://d-museum.kokugakuin.ac.jp/eos/detail/?id=9320"
  - "https://www.jinjahoncho.or.jp/"
  - "https://www.patheos.com/blogs/pagantama/2016/06/12/a-shinto-prayer-for-beginners/"
---

# 神社神道

## 结构
[修祓・祓詞] → [神前拝礼] → [称辞・祭神奉称] → [願主名奏上] → [願意奏上] → [守護・成就の奏上] → [恐み恐みも白す] → [玉串拝礼・拝礼]

## 通用骨架（占位符版本）
```
掛けまくも畏き伊邪那岐大神
筑紫の日向の橘の小戸の阿波岐原に
禊祓へ給ひし時に生り坐せる祓戸大神等
諸々の禍事罪穢有らむをば
祓へ給ひ清め給へと白す事を
聞こし食せと恐み恐みも白す

掛けまくも畏き
{{anchors.shrine_name}} に鎮まり坐す
{{anchors.kami_name}} の大前に
恐み恐みも白さく

{{anchors.petitioner_name}} は
{{anchors.address_or_affiliation}} に在りて
今日の生日の足日に
慎み敬ひ拝み奉り
御前に畏み畏みも白さく

{{anchors.wish_content}} の事を
平けく安けく聞こし食して
禍事罪穢あらむをば
祓へ給ひ清め給ひ
道の隈手に迷ふことなく
幸へ給ひ守り給ひ
夜の守り日の守りに
守り恵み給へと

恐み恐みも白す
```