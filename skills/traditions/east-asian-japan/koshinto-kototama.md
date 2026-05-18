---
id: koshinto-kototama
name: 古神道 / 言霊学派
name_en: Koshinto / Kototama School
category: east-asian-japan
deity_based: true

self_pray_capable: partial
required_officiants:
  - shinto-kannushi
officiant_notes: 正式な神社祭祀・慰霊祭・鎮魂祭・大祓式は神職が斎主となる。ひふみ祝詞・天津祝詞・大祓詞の私的奏上は自念可能。

authoritative_texts:
  - "『延喜式』巻八「祝詞」：大祓詞、祈年祭祝詞、月次祭祝詞"
  - "『古事記』上巻：伊邪那岐命の禊祓段"
  - "『先代旧事本紀』天神本紀・天孫本紀：天神地祇・神代系譜"
  - "『中臣祓訓解』：中臣祓・大祓詞注釈伝承"
  - "『霊界物語』出口王仁三郎：言霊・ひふみ祝詞関連説示"
  - "「ひふみ祝詞」：古神道・言霊系諸流派における奏上伝承"
primary_languages:
  - classical-japanese
  - japanese

backlash_risk: medium
mitigation: 害意・呪詛目的を撤回し、奏上を中止して祓詞または大祓詞で清め、正式祭祀が必要な場合は神職に依頼する。
taboos:
  - 呪詛・怨敵加害・他者支配を目的として言霊祝詞を用いない。
  - 穢れを軽視して、祓い・慎みを欠いたまま正式祭祀を僭称しない。
  - 神名・祝詞を戯れ、嘲弄、改竄、商業的断言のために乱用しない。
  - 異なる神格を一つの呼請段で無秩序に混合しない。
  - 慰霊・鎮魂・神葬祭を私的な断定で代行したと称しない。

search_strategy: |
  "ひふみ祝詞" OR "Hifumi Norito" full text OR practice
  Kototama sound practice Nakazono OR Koshinto modern practitioner
  言霊 古神道 自家祈祷 OR home practice
  site:k-amc.kokugakuin.ac.jp/ 神道 祝詞 大祓詞 言霊
  site:kokugakuin.ac.jp "Norito" "Oharae" "Kotodama"

case_index:
  - wish_type: health
    hint: "天津祝詞または大祓詞による祓清めの後、ひふみ祝詞を奏上する私的祈願。"
    officiant: none
    primary_language: classical-japanese
  - wish_type: wealth
    hint: "『延喜式』祈年祭祝詞の語彙に依る五穀・産業繁栄の祈願；正式な社頭祈願は神職斎行。"
    officiant: shinto-kannushi
    primary_language: classical-japanese
  - wish_type: wealth
    hint: "ひふみ祝詞を中心に、言霊の調和と豊かさへの発願として行う現代的な私的祈願。"
    officiant: none
    primary_language: japanese
  - wish_type: protection
    hint: "大祓詞・天津祝詞・祓詞を中心とする祓戸大神への祓清めの祈願。"
    officiant: none
    primary_language: classical-japanese
  - wish_type: deceased
    hint: "祖霊祭・慰霊祭・鎮魂祭の祝詞；神葬祭系統の正式祭祀は神職斎行。"
    officiant: shinto-kannushi
    primary_language: classical-japanese
  - wish_type: deceased
    hint: "ひふみ祝詞を静かに奏上し、祖霊への追慕と鎮魂を願う現代的な私的祈願。"
    officiant: none
    primary_language: japanese
  - wish_type: relationship
    hint: "産霊の神徳に基づく縁結び祈願祝詞；私的には祓詞・ひふみ祝詞を添える。"
    officiant: none
    primary_language: classical-japanese
  - wish_type: wisdom
    hint: "言霊の調えとしてひふみ祝詞を中心に奏上し、神前敬白で学業・判断の明澄を願う。"
    officiant: none
    primary_language: japanese
  - wish_type: breaking
    hint: "破壊的呪詛ではなく、大祓詞・天津祝詞による罪穢・禍事の祓いとして行う。"
    officiant: none
    primary_language: classical-japanese
  - wish_type: event
    hint: "旅行安全・試験・事業開始などの当日祈願祝詞；正式祈願祭は神職斎行。"
    officiant: none
    primary_language: classical-japanese

verification:
  - "Kokugakuin University, Encyclopedia of Shinto: Norito"
  - "Kokugakuin University, Encyclopedia of Shinto: Ōharae / Great Purification"
  - "Kokugakuin University, Encyclopedia of Shinto: Harae"
  - "Kokugakuin University, Encyclopedia of Shinto: Kotodama"
  - "『延喜式』巻八「祝詞」大祓詞・祈年祭祝詞"
  - "『古事記』上巻、伊邪那岐命禊祓段"
  - "https://d-museum.kokugakuin.ac.jp/eos/"
  - "https://sacred-texts.com/shi/kj/"
  - "https://pentacles1.com/hifuminorito/"
  - "https://kototamabooks.com/kototama-sound-practice/"
---

# 古神道 / 言霊学派

## 结构
[修祓・禊] → [敬神・敬白] → [発願] → [正行：ひふみ祝詞・天津祝詞] → [祓清め] → [納め・恐み恐みも白す]

## 通用骨架（占位符版本）
```
掛けまくも畏き祓戸大神等の大前に、{{anchors.prayer_name}}、恐み恐みも白す。

祓へ給ひ清め給へ。
守り給ひ幸へ給へ。
{{anchors.person_name}} が身魂にかかれる諸々の禍事・罪・穢れを、祓へ給ひ清め給へ。

ここに {{anchors.wish_subject}} の事につきて、{{anchors.intent}} と願ひ奉る。
曲事なく、偽りなく、言霊の幸はふ道に違ふことなく、清明正直の心をもて白す。

ひふみ　よいむなや　こともちろらね
しきる　ゆゐつわぬ　そをたはくめか
うおえ　にさりへて　のますあせゑほれけ

高天原に神留坐す
神漏岐神漏美の命以ちて
皇御祖神伊邪那岐大神
筑紫の日向の橘の小戸の阿波岐原に
禊祓ひ給ふ時に生り坐せる祓戸大神等
諸々の禍事罪穢有らむをば
祓へ給ひ清め給へと申す事を
聞こし食せと恐み恐みも白す。

祓へ給ひ清め給へ。
守り給ひ幸へ給へ。

{{anchors.person_name}} が願ひ奉る {{anchors.wish_subject}}、神ながらの道に叶ひ、言霊の幸はひによりて、清く明く直く正しく成らしめ給へ。

恐み恐みも白す。
```