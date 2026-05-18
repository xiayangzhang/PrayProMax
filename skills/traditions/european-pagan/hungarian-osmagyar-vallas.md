---
id: hungarian-osmagyar-vallas
name: 匈牙利 Ősmagyar Vallás
name_en: Ősmagyar Vallás (Hungarian Native Faith)
category: european-pagan
deity_based: true

self_pray_capable: true
required_officiants: []
officiant_notes: 现代 Ősmagyar Vallás 多数祝词、祖先祷与家庭祈愿可自念；táltos 或 közösségi szertartás 角色并非所有祷词的必需条件。

authoritative_texts:
  - Anonymus, Gesta Hungarorum, cap. 5–6, 13, 16; blood-oath and early Magyar sacral kingship motifs
  - Képes Krónika / Chronicon Pictum, chs. on Hunor-Magor, Álmos, Árpád, and the Turul lineage tradition
  - Constantine VII Porphyrogenitus, De Administrando Imperio, ch. 38–40, on the Turks/Hungarians and early Magyar polity
  - Ibn Rusta / Gardīzī notices on the Magyars, in Gyula Kristó ed., A honfoglalás korának írott forrásai
  - Ipolyi Arnold, Magyar mythologia, sections on Isten, Boldogasszony, táltos, fire, water, tree, and ancestor motifs
  - Diószegi Vilmos, A pogány magyarok hitvilága, chapters on táltos tradition, world tree, soul concepts, and shamanic survivals
  - Erdélyi János, Magyar közmondások könyve, entries preserving Hungarian blessing formulae such as “Adjon Isten…” and “Áldjon meg az Isten…”
primary_languages:
  - hungarian
  - old-hungarian

backlash_risk: medium
mitigation: Kerülni kell a hamis történeti bizonyosság állítását, a más népek vagy vallások gyalázását, az ártó átkot, valamint a táltos cím jogosulatlan felvételét.
taboos:
  - Ártó, kényszerítő vagy bosszúálló átokmondás nem része a közösségi áldásrendnek.
  - Hamis eskü, esküszegés és a vérszerződés-motívum profán utánzása tilalmazott.
  - Az ősök, sírok, tűz, víz, kenyér és otthon küszöbének gyalázása tilos.
  - Táltosnak, regösnek vagy szertartásvezetőnek mondani magát beavatás, közösségi elismerés vagy hagyományos felhatalmazás nélkül kerülendő.
  - Nem szabad idegen hagyományok szent neveit Ősmagyar imába keverni úgy, mintha azok magyar ősvallási szövegtestek lennének.

search_strategy: |
  "Ősmagyar Vallás" áldás "Áldjon meg az Isten"
  "magyar ősvallás" táltos ima áldás
  "Adjon Isten" magyar népi áldás
  "Magyarok Istene" áldás ima
  "Gesta Hungarorum" vérszerződés Álmos Turul
  "Ipolyi Arnold Magyar mythologia" Isten Boldogasszony táltos
  "Diószegi Vilmos A pogány magyarok hitvilága" táltos világfa
  "Erdélyi János Magyar közmondások könyve" "Adjon Isten"

case_index:
  - wish_type: health
    hint: “Egészség-áldás / Áldjon meg az Isten” magyar áldásmondás beteg vagy gyógyulást kérő személy nevével
    officiant: none
    primary_language: hungarian
  - wish_type: wealth
    hint: “Bőség-áldás / Adjon Isten” magyar népi bőség- és házáldás-formula
    officiant: none
    primary_language: hungarian
  - wish_type: protection
    hint: “Ősök oltalma / Áldjon meg az Isten” védelemkérő ősi áldás Istenhez és az ősök emlékezetéhez
    officiant: none
    primary_language: hungarian
  - wish_type: deceased
    hint: “Ősök útja / Nyugodjék békében” magyar halotti emlékező ima ősi keretben
    officiant: none
    primary_language: hungarian
  - wish_type: relationship
    hint: “Békesség-áldás / Adjon Isten békességet” magyar békéltető és családi áldásmondás
    officiant: none
    primary_language: hungarian
  - wish_type: wisdom
    hint: “Táltos-bölcsesség kérése / Világfa-áldás” bölcsességkérő magyar invokáció Istenhez és az ősök rendjéhez
    officiant: none
    primary_language: hungarian
  - wish_type: breaking
    hint: “Rontás elvitele / Rossz szó visszavétele” ártás nélküli magyar eloldó formula
    officiant: none
    primary_language: hungarian
  - wish_type: event
    hint: “Út- és eseményáldás / Adjon Isten jó utat” magyar eseményre vagy útra mondott áldás
    officiant: none
    primary_language: hungarian

verification:
  - Anonymus, Gesta Hungarorum, cap. 5–6, 13, 16; ed. and trans. in Central European University Press, The Deeds of the Hungarians
  - Képes Krónika / Chronicon Pictum, medieval Hungarian chronicle tradition on Hunor-Magor, Álmos, Árpád and sacral origins
  - Constantine Porphyrogenitus, De Administrando Imperio, ch. 38–40
  - Gyula Kristó, ed., A honfoglalás korának írott forrásai, Szeged, 1995
  - Ipolyi Arnold, Magyar mythologia, Pest, 1854
  - Diószegi Vilmos, A pogány magyarok hitvilága, Budapest, 1967
  - Erdélyi János, Magyar közmondások könyve, Pest, 1851
  - https://mek.oszk.hu/
  - https://www.dmgh.de/
---

# 匈牙利 Ősmagyar Vallás

## 结构
[megszólítás / 呼名] → [ősök emlékezete / 忆祖] → [áldáskérés / 正行祝愿] → [eloldás vagy békítés / 破除或和解] → [hálaadás / 致谢] → [áldás lezárása / 祝词封闭]

## 通用骨架（占位符版本）
```
Istenem, Magyarok Istene,
hallgasd meg {{anchors.prayer_name}} szavát.

Őseim, apáim és anyáim,
kik előttem jártatok,
álljatok mögöttem tiszta emlékezettel,
ne ártással, ne haraggal,
hanem áldással.

Áldjon meg az Isten,
őrizzen meg az Isten,
fordítsa jóra {{anchors.wish_matter}} dolgát.

Adjon Isten egészséget {{anchors.health_target}} testének,
békességet {{anchors.health_target}} lelkének,
erőt a szívbe,
világosságot az elmébe.

Adjon Isten kenyeret a háznak,
bőséget a munkának,
tiszta szerencsét {{anchors.wealth_matter}} útján.

Isten oltalma legyen {{anchors.protection_target}} felett,
ősök emlékezete legyen {{anchors.protection_target}} mögött,
rossz szó, rossz szem, rossz szándék
ne találjon rajta fogást.

{{anchors.deceased_name}} lelke nyugodjék békében.
Ősei fogadják,
útja legyen világos,
emléke legyen áldott.

Adjon Isten békességet {{anchors.relationship_names}} között.
A harag halkuljon,
a szó tisztuljon,
a szív igaz útra térjen.

Adjon Isten bölcsességet {{anchors.wisdom_target}} elméjébe,
jó mértéket a szóba,
erős tartást a cselekedetbe,
tiszta látást a döntésbe.

Ami ártó szó,
ami rossz kötés,
ami nem igaz rend szerint tapad {{anchors.breaking_target}} köré,
az oldódjék el,
menjen vissza a semmibe,
ne bántson senkit,
ne térjen ártással.

Adjon Isten jó utat {{anchors.event_name}} dolgában.
Legyen előtte nyitott kapu,
mögötte békesség,
mellette jó társ,
felette tiszta ég.

Nem kérek ártást,
nem mondok hamis esküt,
nem gyalázom az ősöket,
nem töröm meg a kenyeret haraggal,
nem szennyezem a tüzet rossz szóval.

Áldás legyen {{anchors.prayer_name}} házán,
áldás legyen {{anchors.prayer_name}} útján,
áldás legyen azon, ami igaz és tiszta.

Úgy legyen.
Áldás, békesség.
```