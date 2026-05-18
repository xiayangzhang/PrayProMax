---
id: heathenry-asatru
name: Heathenry / Ásatrú
name_en: Heathenry / Ásatrú
category: european-pagan
deity_based: true

self_pray_capable: partial
required_officiants:
  - gothi-gydja
officiant_notes: 私人 galdr、祈愿与献辞可自念；公共 blót、sumbel、誓言见证、祖先追思通常由 goði/gyðja 或同等主持者维持 frith 与礼序。

authoritative_texts:
  - "Poetic Edda: Sigrdrífumál 3-4, 6-14; Hávamál 76-77, 138-145; Völuspá 1-66"
  - "Prose Edda: Gylfaginning 20, 24, 35; Skáldskaparmál, Prologue and deity kennings"
  - "Heimskringla: Hákonar saga góða 14-18, especially ch. 17 on blót and full"
  - "Landnámabók: accounts of hof, blót, oaths, land-taking rites"
  - "Kormáks saga ch. 22; Eyrbyggja saga ch. 4 and ch. 10, ritual and oath references"
primary_languages:
  - old-norse
  - modern-icelandic
  - english

backlash_risk: medium
mitigation: 保持单一对象、清楚愿文、避免誓言滥用与 níð/cursing；若涉及公共 blót、亡者追思或 oath，则交由 goði/gyðja 见证并维护 frith。
taboos:
  - 不作虚假誓言、轻率誓言或违誓；oath 属强约束言语行为。
  - 不以 níð、诅咒、coercive seiðr 或羞辱性言辞伤害无辜者、破坏 frith。
  - 不把互相冲突的神祇诉求混在同一段直接呼请中；同段只向一个明确对象发愿。
  - 不以祖先、landvættir 或神名为工具化命令；献辞须以尊敬、互惠、记忆与 frith 为界。
  - 公共 blót、sumbel 与 memorial rite 不应绕过共同体主持、誓言见证与礼序。

search_strategy: |
  "Sigrdrífumál 3 4 Heill dagr Heilir æsir læknishendr Old Norse"
  "Hákonar saga góða chapter 17 blót full Njörðr Freyr árs ok friðar"
  "Hávamál 76 77 Deyr fé deyja frændr Old Norse"
  "Hávamál 138 141 runes Old Norse Odin"
  "Sigrdrífumál bjargrúnar brimrúnar limrúnar málrúnar"
  "Heathen blót sumbel goði gyðja frith oath modern Ásatrú"

case_index:
  - wish_type: health
    hint: "Sigrdrífumál læknishendr / bjargrúnar：以「Heilir æsir, heilar ásynjur… ok læknishendr」为核心的健康 galdr。"
    officiant: none
    primary_language: old-norse
  - wish_type: wealth
    hint: "Hákonar saga góða blót formula：以 Njǫrðr/Freyr 的「til árs ok friðar」为 canonical 名称的丰年与富足 blót。"
    officiant: gothi-gydja
    primary_language: old-norse
  - wish_type: protection
    hint: "Sigrdrífumál sigrúnar / Heill dagr：以「Heill dagr, heilir dags synir… gefið sitjendum sigr」为核心的守护 galdr。"
    officiant: none
    primary_language: old-norse
  - wish_type: deceased
    hint: "Minni / erfi with Hávamál 76-77：以「Deyr fé, deyja frændr… orðstírr deyr aldregi」为核心的亡者追忆。"
    officiant: gothi-gydja
    primary_language: old-norse
  - wish_type: relationship
    hint: "Hávamál vinátta stanzas 41-44：以 friendship-gifting 与 frith-restoration 为核心的关系祈愿；非强制爱情咒。"
    officiant: none
    primary_language: old-norse
  - wish_type: wisdom
    hint: "Hávamál rúnatal 138-141 / Sigrdrífumál mál ok manvit：以 Óðinn、rúnar、mál ok manvit 为核心的智慧祈愿。"
    officiant: none
    primary_language: old-norse
  - wish_type: breaking
    hint: "Sigrdrífumál limrúnar / málrúnar：用于切断恶意言辞、解开纷争与恢复 lawful frith；不作 níð 或伤害性诅咒。"
    officiant: none
    primary_language: old-norse
  - wish_type: event
    hint: "Sigrdrífumál brimrúnar / Heill dagr：用于行旅、海行、考试或特定事件的 sigr 与 safe passage galdr。"
    officiant: none
    primary_language: old-norse

verification:
  - "Poetic Edda, Sigrdrífumál 3-4, 6-14; Hávamál 76-77, 138-145"
  - "Heimskringla, Hákonar saga góða 17: ritual full to Óðinn, Njörðr and Freyr, 'til árs ok friðar'"
  - "Prose Edda, Gylfaginning 20, 24, 35"
  - "https://heimskringla.no/wiki/H%C3%A1vam%C3%A1l"
  - "https://heimskringla.no/wiki/Sigrdr%C3%ADfum%C3%A1l"
  - "https://heimskringla.no/wiki/H%C3%A1konar_saga_g%C3%B3%C3%B0a"
  - "https://www.sacred-texts.com/neu/poe/"
  - "https://www.sacred-texts.com/neu/pre/"
---

# Heathenry / Ásatrú

## 结构
[开场安定 frith] → [称名与单一对象呼请] → [献辞/记忆 blót 或 galdr] → [正行：原文颂段、rúnar 或愿文] → [誓言边界与互惠] → [完成语与 frith 收束]

## 通用骨架（占位符版本）
```
Friðr sé hér.
Helga ek þenna stað til fríðar ok sannra orða.

Ek kalla á {{anchors.deity_name_or_wight}},
{{anchors.deity_heiti_old_norse}},
heyr orð mín.

Heill dagr, heilir dags synir,
heil nótt ok nipt!
Óreiðum augum lítið okkr þinig,
ok gefið sitjendum sigr.

Heilir æsir, heilar ásynjur,
heil sjá in fjölnýta fold!
Mál ok manvit gefið okkr mærum tveim
ok læknishendr, meðan lifum.

Ek ber fram {{anchors.offering_name}}.
Ek nefni {{anchors.beneficiary_name}}.
Ek bið um {{anchors.wish_statement}}.
Lát {{anchors.beneficiary_name}} standa í frith,
með heilum hug, heilum orðum, heilum verkum.

Ef þetta er til heilsu:
Bjargrúnar skaltu kunna,
ef þú bjarga vilt
ok leysa kind frá konum.

Ef þetta er til verndar eða sigurs:
Sigrúnar skaltu kunna,
ef þú vilt sigr hafa,
ok rísta á hjalti hjörs.

Ef þetta er til ferðar eða atburðar:
Brimrúnar skaltu kunna,
ef þú vilt borgit hafa
á sundi seglmörum.

Ef þetta er til mála, dóms eða lausnar:
Málrúnar skaltu kunna,
ef þú vilt at manngi þér
heiptum gjaldi harm.

Ef þetta er til visku:
Veit ek, at ek hekk
vindga meiði á
nætr allar níu,
geiri undaðr
ok gefinn Óðni,
sjálfr sjálfum mér.

Ek fimbulljóð níu
nam af inum frægja syni
Bölþorns, Bestlu föður,
ok ek drykk of gat
ins dýra mjaðar,
ausinn Óðreri.

Þá nam ek frævask
ok fróðr vera
ok vaxa ok vel hafask;
orð mér af orði
orðs leitaði,
verk mér af verki
verks leitaði.

Ef þetta er fyrir látinn/látna:
Deyr fé,
deyja frændr,
deyr sjálfr it sama;
ek veit einn,
at aldrei deyr:
dómr um dauðan hvern.

Deyr fé,
deyja frændr,
deyr sjálfr it sama;
en orðstírr
deyr aldregi,
hveim er sér góðan getr.

Ek geri eigi níð.
Ek bind eigi vilja annars.
Ek sver eigi ósannan eið.
Orð mín standi innan frithar.

{{anchors.deity_name_or_wight}}, tak við {{anchors.offering_name}}.
Gef {{anchors.beneficiary_name}} {{anchors.wish_statement}} ef það er rétt, heilt ok innan frithar.

Svá sé.
Friðr með oss.
```