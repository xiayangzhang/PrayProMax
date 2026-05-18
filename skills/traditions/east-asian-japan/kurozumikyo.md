---
id: kurozumikyo
name: 黒住教
name_en: Kurozumikyo
category: east-asian-japan
deity_based: true

self_pray_capable: partial
required_officiants:
  - kurozumikyo-kyoshi
officiant_notes: 日常の日拝・祓詞・御神名奉称は自念可能だが、鎮魂帰神の正式修法、神葬祭、祖霊祭、教会所での正式祈願は黒住教教師・教導職が司る。

authoritative_texts:
  - 黒住教教典「御教え」「御歌」「御文」
  - 黒住宗忠『御教語』
  - 黒住宗忠『御文』各通
  - 教祖宗忠大神の天命直授体験と御教え（日拝を中心）
  - 黒住教日拝作法・祈願作法
  - 祓詞
  - 禊祓詞
  - 大祓詞（『延喜式』巻八・祝詞）
  - 鎮魂帰神祝詞・ひふみ祝詞（鎮魂行法所用）
primary_languages:
  - japanese
  - classical-japanese

backlash_risk: medium
mitigation: 願意を正直・感謝・清明に戻し、害意・呪詛・虚偽・強制支配を除き、正式な鎮魂帰神・葬祭・祖霊祭は教師に委ねる。
taboos:
  - 天照大御神への不敬、御神前での虚偽、怨恨・呪詛・他者支配を願意に入れること。
  - 鎮魂帰神を興味本位、霊能誇示、占断商売、他者操作のために行うこと。
  - 死穢・病穢・争論・飲酒酩酊などのまま、祓いを欠いて御神前に進むこと。
  - 黒住宗忠の教えに反する暗い心・不足不平・我欲のみの祈願を正行の中心に置くこと。
  - 教師が必要な神葬祭・祖霊祭・正式祈願を、資格なく代行すること。
  - 無礼な心持ちでの日拝。
  - 太陽を直接凝視する行為。

search_strategy: |
  "黒住教 日拝 祝詞" OR "nippai Kurozumikyo" OR "禊祓詞 大祓詞 黒住教"
  "Kurozumikyo" OR 黒住教 modern practices OR nippai OR majinai OR 御陽気修行 site:kurozumikyo.com
  Kurozumikyo sun worship prayer OR norito OR self practice

case_index:
  - wish_type: health
    hint: 日拝詞・祓詞・御神名奉称「天照大御神」による身心清明の祈願；正式には鎮魂帰神祝詞を教師が修する。
    officiant: none
    primary_language: japanese
  - wish_type: wealth
    hint: 日拝詞・祈願祝詞により家業繁栄・生業成就を天照大御神へ奏上する；教会所の正式祈願は黒住教教師が司る。
    officiant: kurozumikyo-kyoshi
    primary_language: japanese
  - wish_type: wealth
    hint: 感謝と誠の心をもって日拝し、開運・生業成就を祈念する。
    officiant: none
    primary_language: classical-japanese
  - wish_type: protection
    hint: 祓詞・大祓詞・御神名奉称「天照大御神」により禍事罪穢の祓清めと守護を祈る。
    officiant: none
    primary_language: classical-japanese
  - wish_type: deceased
    hint: 神葬祭祝詞・祖霊祭祝詞による祖霊安鎮・追慕奉告は黒住教教師が司る。
    officiant: kurozumikyo-kyoshi
    primary_language: japanese
  - wish_type: deceased
    hint: 祖霊舎において禊祓詞と告辞により祖霊へ感謝と追慕を奉告する。
    officiant: none
    primary_language: classical-japanese
  - wish_type: relationship
    hint: 日拝詞・祓詞により不足不平を祓い、まことの心で和合を天照大御神へ奏上する。
    officiant: none
    primary_language: japanese
  - wish_type: wisdom
    hint: 日拝詞・御教え拝読・御神名奉称「天照大御神」により心の明朗と正直の悟りを祈る。
    officiant: none
    primary_language: japanese
  - wish_type: breaking
    hint: 大祓詞・祓詞による禍事罪穢の祓清め；呪詛返しではなく、鎮魂帰神祝詞は教師の指導下で行う。
    officiant: kurozumikyo-kyoshi
    primary_language: classical-japanese
  - wish_type: breaking
    hint: 大祓詞・禊祓詞を奏上し、障りや穢れを祓い清める。
    officiant: none
    primary_language: classical-japanese
  - wish_type: event
    hint: 祈願祝詞・日拝詞により旅行安全、試験、出産、開業などの事柄を天照大御神へ奉告する；正式祈願は教師が司る。
    officiant: kurozumikyo-kyoshi
    primary_language: japanese
  - wish_type: event
    hint: 特定事象の成就を日拝祝詞と御祈念により奉告する。
    officiant: none
    primary_language: classical-japanese

verification:
  - https://kurozumikyo.com/
  - https://munetada.jp/
  - https://en.wikipedia.org/wiki/Kurozumiky%C5%8D
  - 黒住教教典「御教え」「御歌」「御文」
  - 黒住宗忠『御教語』
  - 黒住宗忠『御文』
  - 『延喜式』巻八「六月晦大祓」
  - 祓詞「掛けまくも畏き伊邪那岐大神……」
  - 公式日拝式次第（禊祓詞 → 大祓詞 → 日拝祝詞）
---

# 黒住教

## 结构
[修祓] → [拝礼] → [天照大御神への奉称・日拝] → [鎮魂帰神・ひふみ祝詞] → [願意奏上] → [守護祈念] → [奉謝・拝礼]

## 通用骨架（占位符版本）
```
掛けまくも畏き天照大御神の大前に、恐み恐みも白さく。

{{anchors.prayer_name}}、{{anchors.birth_or_identifier}}、{{anchors.place}}に在りて、
今日の御日影を仰ぎ奉り、御陽気を戴き奉り、
まことの心をもって拝み奉る。

祓へ給ひ、清め給へ。
守り給ひ、幸へ給へ。

天照大御神。
天照大御神。
天照大御神。

ひふみよいむなやこともちろらね
しきるゆゐつわぬそをたはくめか
うおえにさりへてのますあせゑほれけ

天照大御神の御前に、恐み恐みも白さく。
{{anchors.wish_statement}}のこと、禍事罪穢あらむをば祓ひ清め給ひ、
{{anchors.person_or_group}}の心を明らけく直く正しく成さしめ給ひ、
御恵みのまにまに、{{anchors.desired_state}}へ導き給へ。

天照大御神、守り給へ幸へ給へ。
天照大御神、守り給へ幸へ給へ。
天照大御神、守り給へ幸へ給へ。

惟神霊幸倍坐世。
惟神霊幸倍坐世。
惟神霊幸倍坐世。

恐み恐みも白す。
```