---
id: ontakekyo
name: 御岳教
name_en: Ontakekyo
category: east-asian-japan
deity_based: true

self_pray_capable: partial
required_officiants:
  - ontakekyo-kyoshi
officiant_notes: 家庭での祓詞・拝詞・六根清浄唱和は自念可；鎮魂帰神・正式祭式・祖霊祭は御岳教教師または教会所の祭員が中心となる。

authoritative_texts:
  - 御岳教『御岳教教典』祭祀・祝詞・祓詞所収
  - 御岳教『御岳教規』祭祀・教師・教会所関係条項
  - 御嶽教祝詞集（三要祝詞：開闢祝詞、陽之祝詞、不動祝詞等）
  - 『神道大系 教派神道』御岳教関係資料
  - 神道祭式一般「祓詞」：掛けまくも畏き伊邪那岐大神
  - 神道鎮魂行法「神語」：幸魂奇魂守給幸給
primary_languages:
  - japanese
  - classical-japanese

backlash_risk: medium
mitigation: 不浄・怨念・私的呪詛を混ぜた場合は祓詞で清め、願意を鎮魂・祈願・報謝の範囲に戻し、正式祭式は御岳教教師に委ねる。
taboos:
  - 御嶽大神・神前・霊山を軽んじる言辞を入れない。
  - 私怨による呪詛・害意・他者支配を願意にしない。
  - 鎮魂帰神を娯楽・占い遊び・無資格の霊媒行為として扱わない。
  - 喪・血・病穢などの穢れを自覚したまま正式神事を強行しない。
  - 教師でない者が御岳教の正式祭主・取次者を僭称しない。
  - 山中での不浄行為を避ける。
  - 無許可の山頂立入をせず、安全と神域尊重を守る。

search_strategy: |
  "御嶽教" OR Ontakekyo 祈祷 OR 祝詞 OR 鎮魂
  "六根清浄" 御嶽山 登拝 OR 祈祷
  御嶽教 教会 OR 本宮 ご祈祷 現代
  site:ontakekyo.or.jp 祈祷

case_index:
  - wish_type: health
    hint: 祓詞・御嶽大神拝詞・鎮魂帰神祝詞による身体平癒祈願
    officiant: ontakekyo-kyoshi
    primary_language: classical-japanese
  - wish_type: health
    hint: 御嶽大神に無病息災・病難平癒を祈る日常祈願
    officiant: none
    primary_language: japanese
  - wish_type: wealth
    hint: 御嶽大神拝詞・家業繁栄祈願祝詞
    officiant: ontakekyo-kyoshi
    primary_language: classical-japanese
  - wish_type: wealth
    hint: 子孫繁栄・福徳授与を祈る陽之祝詞系の現代祈願
    officiant: none
    primary_language: japanese
  - wish_type: protection
    hint: 祓詞・六根清浄唱和・御嶽大神守護祈願
    officiant: none
    primary_language: japanese
  - wish_type: protection
    hint: 厄除け・災難除去・山行安全祈願
    officiant: none
    primary_language: japanese
  - wish_type: deceased
    hint: 祖霊拝詞・慰霊祭祝詞
    officiant: ontakekyo-kyoshi
    primary_language: classical-japanese
  - wish_type: deceased
    hint: 鎮魂帰神・霊魂御嶽山帰依の祈り
    officiant: none
    primary_language: japanese
  - wish_type: relationship
    hint: 祓詞・御嶽大神拝詞による和合祈願
    officiant: none
    primary_language: classical-japanese
  - wish_type: relationship
    hint: 縁結び・家族和合祈願
    officiant: none
    primary_language: japanese
  - wish_type: wisdom
    hint: 鎮魂帰神祝詞・神語「幸魂奇魂守給幸給」による心魂鎮定祈願
    officiant: ontakekyo-kyoshi
    primary_language: classical-japanese
  - wish_type: wisdom
    hint: 少彦名命の智恵・才能授与を祈る現代祈願
    officiant: none
    primary_language: japanese
  - wish_type: breaking
    hint: 祓詞・六根清浄唱和による穢れ祓い・悪縁断ち祈願
    officiant: ontakekyo-kyoshi
    primary_language: classical-japanese
  - wish_type: breaking
    hint: 禁厭・穢れ祓い・不動祝詞による解呪祈願
    officiant: none
    primary_language: japanese
  - wish_type: event
    hint: 御嶽大神拝詞・道中安全／試験成就／事始め祈願祝詞
    officiant: none
    primary_language: classical-japanese
  - wish_type: event
    hint: 登山・試験・旅行安全、祭事奉仕の現代祈願
    officiant: none
    primary_language: japanese

verification:
  - 御岳教公式サイト「御岳教」教団概要・祭神・教会所情報
  - 『神道大系 教派神道』神道大系編纂会、御岳教関係資料
  - 村上重良『近代民衆宗教史の研究』教派神道・御嶽信仰関連章
  - 井上順孝ほか編『新宗教教団・人物事典』御岳教項
  - 『神道事典』弘文堂、御嶽信仰・御岳教・鎮魂帰神項
  - https://www.ontakekyo.or.jp/
  - https://ja.wikipedia.org/wiki/御嶽教
---

# 御岳教

## 结构
[修祓] → [御嶽大神への敬神] → [発願] → [六根清浄] → [鎮魂帰神] → [祈願奏上] → [祖霊・諸霊への回向] → [報謝]

## 通用骨架（占位符版本）
```
掛けまくも畏き伊邪那岐大神
筑紫の日向の橘の小戸の阿波岐原に
禊祓へ給ひし時に生り坐せる祓戸大神等
諸々の禍事罪穢有らむをば
祓へ給ひ清め給へと白す

恐み恐みも白さく。
御嶽大神の大前に、{{anchors.prayer_name}}、身を慎み心を鎮めて、今日の生日の足日に、{{anchors.place}}より拝み奉る。

懺悔懺悔　六根清浄
懺悔懺悔　六根清浄
懺悔懺悔　六根清浄

御嶽大神、荒魂は荒び給はず、和魂は和み給ひ、幸魂奇魂は守り給ひ幸へ給へ。
幸魂　奇魂　守給　幸給
幸魂　奇魂　守給　幸給
幸魂　奇魂　守給　幸給

鎮魂帰神祝詞。
高天原に神留り坐す御嶽大神の御稜威を仰ぎ奉り、{{anchors.prayer_name}}が魂を鎮め、心を正し、身に纏へる諸々の禍事罪穢を祓ひ清め、神ながらの道に帰らしめ給へと、恐み恐みも白す。

御嶽大神の広き厚き御恵みに依りて、
{{anchors.wish_detail}}
この願ひを聞こし食して、過ちあらしめず、禍事あらしめず、道を開かしめ、心身を安らけく平らけく守り給ひ幸へ給へ。

{{anchors.deceased_name}}の御霊に向けて白す。
遠つ御祖、家の御祖、縁ある御霊等、安らけく鎮まり坐して、御嶽大神の御光のもとに清く明らけくあらしめ給へ。

祓へ給ひ清め給へ。
守り給ひ幸へ給へ。
恐み恐みも白す。
```