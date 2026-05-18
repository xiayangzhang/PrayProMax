---
id: famadihana
name: 马达加斯加 Famadihana
name_en: Madagascar Famadihana
category: african-diasporic
deity_based: false

self_pray_capable: partial
required_officiants:
  - malagasy-family-elder
  - mpikabary
officiant_notes: Famadihana 属家族祖先仪礼，核心 kabary、开墓、裹骨、祝福与回葬通常由家族长者及熟悉礼辞者主持；个人可诵简短追念语，但不能单独替代家族仪程。

authoritative_texts:
  - "Maurice Bloch, Placing the Dead: Tombs, Ancestral Villages, and Kinship Organization in Madagascar, chapters 2-5"
  - "Maurice Bloch, From Blessing to Violence: History and Ideology in the Circumcision Ritual of the Merina of Madagascar, sections on tsodrano and ancestral blessing"
  - "Robert Hertz, A Contribution to the Study of the Collective Representation of Death, sections on secondary burial"
  - "Richard Huntington and Peter Metcalf, Celebrations of Death: The Anthropology of Mortuary Ritual, chapter on Madagascar and secondary burial"
  - "Conrad P. Kottak, The Past in the Present: History, Ecology, and Cultural Variation in Highland Madagascar, sections on Merina and Betsileo tombs and ancestors"
primary_languages:
  - malagasy

backlash_risk: high
mitigation: 严格标注为马达加斯加家族祖先礼的文本骨架；不得模拟开墓、翻骨、替他族祖先发令或商业化表演；涉及遗骨、墓地、家族名号须由合法亲属与当地礼俗权威处理。
taboos:
  - 不得在无家族授权、无亲属同意或违法情况下开墓、移动遗骨、触碰 lambamena 或宣称代替本家祖先发言。
  - 不得把 razana 当作可任意驱使的灵体；礼辞应以尊称、告知、请福与回向为主。
  - 不得在 kabary 中公开侮辱死者、争吵、诅咒亲属或把家族纷争置于祖先名义之下。
  - 不得混同非本地神祇、咒术命令或外来驱灵词与 Famadihana 的祖先告祭同段呼请。
  - 不得省略对在场长辈、祖坟、家系与亡者姓名的确认而直接进行“翻骨”宣称。
  - 不得将遗骨、裹尸布、墓土、墓石作为个人灵物私自占有、买卖或带离家族语境。

search_strategy: |
  "Famadihana kabary razana tsodrano Malagasy prayer"
  "famadihana turning of the bones lambamena razana Merina Betsileo"
  "Maurice Bloch Placing the Dead Famadihana ancestral blessing"
  "Madagascar secondary burial famadihana family elder mpikabary"
  "tsodrano razana Malagasy ancestral blessing"

case_index:
  - wish_type: health
    hint: "Tsodrano avy amin'ny Razana：以 kabary famadihana 的告祖与请福格式，为 {{anchors.person_name}} 求 fahasalamana；不替代开墓仪程。"
    officiant: malagasy-family-elder
    primary_language: malagasy
  - wish_type: wealth
    hint: "Tsodrano avy amin'ny Razana：在家族祖先祝福语中祈请 fitahiana、hasina 与 fanambinana ho an'ny ankohonana。"
    officiant: malagasy-family-elder
    primary_language: malagasy
  - wish_type: protection
    hint: "Kabary amin'ny Razana：向 razana 报告家族名号与处境，请 arovana ny taranaka, ny trano, ny tany。"
    officiant: mpikabary
    primary_language: malagasy
  - wish_type: deceased
    hint: "Kabary famadihana sy famonosana lambamena：告知 razana、称名亡者、请其安归祖坟并与祖先同受尊敬。"
    officiant: mpikabary
    primary_language: malagasy
  - wish_type: relationship
    hint: "Tsodrano ho an'ny fihavanana：以祖先见证的 kabary 请求 fihavanana、fifamelana 与 firaisan-kina。"
    officiant: malagasy-family-elder
    primary_language: malagasy
  - wish_type: wisdom
    hint: "Tsodrano avy amin'ny Razana：请 razana hanome saina mazava, fahendrena, teny marina。"
    officiant: malagasy-family-elder
    primary_language: malagasy
  - wish_type: breaking
    hint: "无"
    officiant: none
  - wish_type: event
    hint: "Kabary fangataham-pitahiana：在家族事件前向 razana 报告 {{anchors.event_name}} 并请 fitahiana sy lalana mahitsy。"
    officiant: malagasy-family-elder
    primary_language: malagasy

verification:
  - "Maurice Bloch, Placing the Dead: Tombs, Ancestral Villages, and Kinship Organization in Madagascar. London: Seminar Press, 1971."
  - "Maurice Bloch, From Blessing to Violence: History and Ideology in the Circumcision Ritual of the Merina of Madagascar. Cambridge University Press, 1986."
  - "Robert Hertz, A Contribution to the Study of the Collective Representation of Death, in Death and the Right Hand, trans. Rodney and Claudia Needham. Free Press, 1960."
  - "Richard Huntington and Peter Metcalf, Celebrations of Death: The Anthropology of Mortuary Ritual. Cambridge University Press, 1979."
  - "Conrad P. Kottak, The Past in the Present: History, Ecology, and Cultural Variation in Highland Madagascar. University of Michigan Press, 1980."
  - "https://www.britannica.com/topic/famadihana"
---

# 马达加斯加 Famadihana

## 结构
[称呼祖先与祖坟] → [报明家族与来意] → [称名亡者与亲属] → [kabary 告祖] → [请求 tsodrano] → [家族和合誓言] → [安归祖坟与回向]

## 通用骨架（占位符版本）
```
Ry Razana malala,
Ry Razambenay ao {{anchors.tomb_place}},
ry razan'ny {{anchors.family_lineage}},
henoy izahay taranakareo.

Izahay {{anchors.family_representatives}},
avy amin'ny ankohonana {{anchors.family_name}},
mijoro eto amim-panajana,
mitondra teny sy fo madio,
tsy hanadino anareo,
tsy hanary ny lova,
tsy hanapaka ny fihavanana.

Ry {{anchors.deceased_name}},
zanaka sy havanay,
anarana tsy very,
ra tsy ritra,
taranaka tsy tapaka,
miverena amim-boninahitra amin'ny razana,
mipetraha am-piadanana ao amin'ny tranon-drazana.

Ry Razana,
izao no teninay:
mangataka tsodrano izahay,
mangataka fitahiana,
mangataka hasina,
mangataka fiadanana.

Arovy {{anchors.protected_persons}},
arovy ny trano {{anchors.household_name}},
arovy ny tany {{anchors.land_name}},
arovy ny ankizy sy ny antitra,
arovy ny velona sy ny fahatsiarovana ny maty.

Omeo fahasalamana {{anchors.health_person}},
omeo saina mazava {{anchors.wisdom_person}},
omeo fihavanana {{anchors.relationship_persons}},
omeo fanambinana ny asa sy ny fivelomana {{anchors.wealth_household}},
omeo lalana mahitsy amin'ny {{anchors.event_name}}.

Aoka tsy hisy teny ratsy eto,
aoka tsy hisy fifandirana eto,
aoka tsy hisy fanadinoana eto.
Ny razana hajaina,
ny velona hifankatia,
ny taranaka hitohy.

Ry Razana,
raiso ny fanajanay,
raiso ny fahatsiarovanay,
raiso ny lambanay sy ny teninay,
ary omeo tsodrano izahay.

Tsodrano, tsodrano, tsodrano:
Ho lava andro,
ho salama,
ho miray hina,
ho tsara lalana,
ho voatahy ny taranaka.

Misaotra, ry Razana.
Mitoera am-piadanana.
Izahay kosa hitahiry ny anarana,
hitahiry ny fihavanana,
hitahiry ny fomban-drazana.
Amin'ny fanajana sy ny fihavanana.
```