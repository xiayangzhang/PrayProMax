---
id: finnish-suomenusko
name: Finnish Suomenusko
name_en: Suomenusko (Finnish Native Faith)
category: european-pagan
deity_based: true

self_pray_capable: true
required_officiants: []
officiant_notes: "Loitsut, rukoukset ja runolaulun muodot ovat pääosin itse lausuttavia; yhteisöllinen laulaja tai tietäjä ei ole rakenteellisesti pakollinen."

authoritative_texts:
  - "Suomen Kansan Vanhat Runot (SKVR), loitsut: parannusloitsut, raudan sanat, tulen sanat, karjanhoitoloitsut, lemmenloitsut, matkaloitsut, kateen ja pahan silmän purkusanat"
  - "Kalevala, Runo 9: Raudan synty ja haavan parannussanat"
  - "Kalevala, Runo 17: Sanojen etsintä ja syntysanojen motiivi"
  - "Kalevala, Runo 45: Tautien lähettäminen ja parantamisen sanat"
  - "Kanteletar, III kirja: loitsurunoja ja kansanrunouden rukous- ja manausmuotoja"
primary_languages:
  - finnish
  - karelian

backlash_risk: medium
mitigation: "Keskeytä loitsu, nimeä väärinkäyttö, peru lausuttu sana, palauta väki omaan sijaansa ja päätä anteeksipyynnöllä ilman kirousta."
taboos:
  - "Loitsua ei lausuta vahingoittamistarkoituksessa eikä toisen tahdon murtamiseksi."
  - "Vainajien, hautapaikkojen ja kuolinitkujen sanoja ei käytetä pilkkaan, uhkailuun tai leikiksi."
  - "Metsän, veden, tulen, raudan ja maan väkeä ei komenneta ilman kunnioittavaa puhuttelua."
  - "Syntysanoja ei vääristellä tarkoituksella eikä loitsun vastuuta siirretä viattomalle."
  - "Suvun tai kylän salaisiksi katsottuja loitsusanoja ei esitetä ominaan."
  - "Haltijoita, jumalia ja väkiä ei sekoiteta samaan kutsujaksoon, ellei kyseinen loitsu sitä nimenomaisesti edellytä."

search_strategy: |
  SKVR loitsu "raudan sanat" "tulen sanat" "taudin synty" site:skvr.fi
  SKVR "lemmenloitsu" "karjanlaskusanat" "matkaloitsu" site:skvr.fi
  Kalevala Runo 9 Raudan synty haavan sanat Finnish text
  Kalevala Runo 45 tautien synty parannusloitsu Finnish text
  Kanteletar III kirja loitsurunoja Finnish original
  Finnish Suomenusko loitsu Ukko ylijumala rukous

case_index:
  - wish_type: health
    hint: "Parannusloitsu / Taudin synty -loitsu; SKVR:n sairauden alkuperän nimeämiseen ja palauttamiseen perustuva loitsuperinne."
    officiant: none
    primary_language: finnish
  - wish_type: wealth
    hint: "Karjan menestysloitsu / Karjanlaskusanat; talon, karjan ja elannon varjelemisen runoloitsu."
    officiant: none
    primary_language: finnish
  - wish_type: protection
    hint: "Raudan sanat ja Tulen sanat; Kalevalan Runon 9 sekä SKVR:n suojelu- ja vahingonrajausloitsujen malli."
    officiant: none
    primary_language: finnish
  - wish_type: deceased
    hint: "Kuolinitku / vainajan saattosanat; karjalais-suomalainen itkuvirsi- ja Tuonelaan saattamisen perinne."
    officiant: none
    primary_language: karelian
  - wish_type: relationship
    hint: "Lemmenloitsu; SKVR:n lemmen ja sovinnon sanoihin kuuluva runomuoto ilman tahdonpakkoa."
    officiant: none
    primary_language: finnish
  - wish_type: wisdom
    hint: "Sanojen synty / Väinämöisen sanojen etsintä; Kalevalan Runon 17 mukainen tietäjän sanan ja ymmärryksen hakemisen malli."
    officiant: none
    primary_language: finnish
  - wish_type: breaking
    hint: "Kateen sanat / Pahan silmän purkusanat; SKVR:n panennon, kateen ja väärän väen palauttamisen loitsuperinne."
    officiant: none
    primary_language: finnish
  - wish_type: event
    hint: "Matkaloitsu / Tienavaussanat; SKVR:n kulkemisen, tien ja rajanylityksen loitsumuoto."
    officiant: none
    primary_language: finnish

verification:
  - "https://skvr.fi/"
  - "https://kalevala.finlit.fi/"
  - "https://www.finlit.fi/fi/arkisto/suomen-kansan-vanhat-runot"
  - "Elias Lönnrot, Kalevala, 1849, Runot 9, 17, 45."
  - "Elias Lönnrot, Kanteletar, 1840, III kirja."
  - "Suomen Kansan Vanhat Runot, SKVR corpus, loitsut: raudan sanat, tulen sanat, parannusloitsut, lemmenloitsut, karjanhoitoloitsut, matkaloitsut."
---

# Finnish Suomenusko

## 结构
[rajaus / sanan avaaminen] → [puhujan nimeäminen] → [Ukko ylijumalan kutsu] → [väen ja synnyn nimeäminen] → [varsinainen loitsu] → [pyynnön sitominen] → [väen palautus] → [lopetussanat]

## 通用骨架（占位符版本）
```
Alku aina, alku aina,
sana synty, virsi nousi.

Minä, {{anchors.prayer_name}},
lausun sanat {{anchors.place_name}},
{{anchors.day_mark}}.

Oi Ukko, ylijumala,
taivahallinen jumala,
kuule sanat suustani,
ota virsi viereltäni.

Mieleni minun tekevi,
aivoni ajattelevi,
lähteäni laulamahan,
saa'ani sanelemahan.

Sanat suustani sulavat,
puhe'et putoelevat,
kielelleni kerkiävät,
hampahilleni hajoovat.

Synty syvä, synty vanha,
tule tietä myöten tähän,
näytä juuri, näytä alku,
näytä oikea omasi.

Ei pahaksi, ei panoksi,
ei kateeksi, ei kiroukseksi,
vaan oikeaksi avuksi
{{anchors.wish_name}} asiassa.

Oi Ukko, ylijumala,
taivahallinen jumala,
anna apu {{anchors.recipient_name}},
anna rauha {{anchors.recipient_name}},
anna suoja {{anchors.recipient_name}},
anna sana oikeahan.

Mikä on väärin lausuttu,
se takaisin peräytyköön.
Mikä on pahoin pantu,
se omaan sijaansa palatkoon.
Mikä on oikein sanottu,
se paikalleen asettukoon.

Mene väki sijallesi,
mene voima kohdallesi,
mene sana synnyllesi,
mene rauha rinnalleni.

Näin sanon, näin sidon,
sanan suuhun, työn teloille,
rauhan maahan, valon päälle,
{{anchors.recipient_name}} osaksi.
```