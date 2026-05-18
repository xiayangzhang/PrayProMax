---
id: kakure-kirishitan
name: 隠れキリシタン
name_en: Kakure Kirishitan / Hidden Christians
category: east-asian-japan
deity_based: true

self_pray_capable: partial
required_officiants:
  - kakure-kirishitan-chokata
  - kakure-kirishitan-mizukata
officiant_notes: 家庭内のオラショは自念可能だが、共同体年中行事・葬送・洗礼系の秘儀は帳方・水方などの世襲役が担う。

authoritative_texts:
  - "天地始之事（Tenchi Hajimari no Koto）：天地創造・デウス・サンタマリア・受難伝承諸段"
  - "生月・平戸系オラショ写本／口承：Pater Noster, Ave Maria, Credo, Gloria Patri, Salve Regina"
  - "五島・長崎系オラショ口承：デウス・サンタマリアへの祈祷、年中行事・家内祈祷の伝承"
  - "こんちりさんのりやく（Konchirisan no Riyaku）：痛悔・告白・赦しをめぐる祈祷段"
  - "ドチリナ・キリシタン（Doctrina Christam / Dochirina Kirishitan）：十字架のしるし、主の祈り、天使祝詞、使徒信経、十誡"
  - "Manuale ad Sacramenta Ecclesiae ministranda, Nagasaki Jesuit Mission, 1605：洗礼・葬送・悔悛関連式文"
primary_languages:
  - latin
  - portuguese
  - japanese

backlash_risk: high
mitigation: 秘伝性・殉教記憶・地域共同体の継承権を尊重し、外部者が共同体固有の秘儀役割を詐称しない。
taboos:
  - 共同体に伝わる御前様・納戸神・聖画・メダイ・巻物・オラショを許可なく公開または模倣しない。
  - 共同体外の者へ、秘伝とされる全文オラショや家筋固有の伝承を無断で開示しない。
  - 洗礼・葬送・年中行事で帳方・水方などの役を外部者が名乗らない。
  - オラショを呪詛・強制恋愛・敵害・利得目的の術として扱わない。
  - デウス・サンタマリア・御子・聖人への呼びかけを、同一段落で無関係な神格召喚と混交しない。
  - 踏絵・棄教強制・密告・迫害を肯定する文脈で唱えない。
  - 踏絵の記憶に関わる聖像・キリスト教象徴を侮辱的に踏む所作を再現しない。
  - 共同体ごとの口伝音形を、標準ラテン語へ一方的に訂正して真正性を否定しない。

search_strategy: |
  "Kakure Kirishitan Orasho" OR "隠れキリシタン オラショ" Ikitsuki OR Goto
  "Kakure Kirishitan" ojiiyaku OR mideshi prayer ritual
  modern Kakure Kirishitan practitioners Nagasaki OR Ikitsuki

case_index:
  - wish_type: health
    hint: "Pater Noster／Ave Maria／Gloria Patri を核に、病者名を pro {{anchors.person_name}} として挿入するオラショ"
    officiant: none
    primary_language: latin
  - wish_type: wealth
    hint: "Pater Noster の panem nostrum quotidianum 段を核に、生活保持の願意を {{anchors.petition}} として置くオラショ"
    officiant: none
    primary_language: latin
  - wish_type: wealth
    hint: "オハツホアゲなど供物・初穂に関わる共同体祈祷で、豊漁・豊作・家業維持を願う現代伝承型"
    officiant: kakure-ojiiyaku
    primary_language: japanese
  - wish_type: protection
    hint: "Credo／Ave Maria／Salve Regina を核に、デウスとサンタマリアへの保護祈願を含むオラショ"
    officiant: none
    primary_language: latin
  - wish_type: deceased
    hint: "葬送・追善系オラショ；Requiem aeternam と Pater Noster／Ave Maria を中心とする死者祈念"
    officiant: kakure-kirishitan-chokata
    primary_language: latin
  - wish_type: deceased
    hint: "葬送時に長老役が唱える死者のためのオラショ；Nunc dimittis 系変形を含む現代報告例"
    officiant: kakure-ojiiyaku
    primary_language: japanese
  - wish_type: relationship
    hint: "Konchirisan no Riyaku 系の痛悔と Pater Noster の dimitte nobis debita nostra 段を核にする和解祈祷"
    officiant: none
    primary_language: latin
  - wish_type: relationship
    hint: "家族和合・婚礼・洗礼に伴う共同体祝福のオラショを長老役が唱える現代伝承型"
    officiant: kakure-ojiiyaku
    primary_language: japanese
  - wish_type: wisdom
    hint: "Credo と Tenchi Hajimari no Koto のデウス・天地創造伝承を参照する信仰告白型オラショ"
    officiant: none
    primary_language: latin
  - wish_type: breaking
    hint: "Konchirisan no Riyaku 系の痛悔、Credo、Pater Noster の libera nos a malo 段を核にする悪からの離脱祈祷"
    officiant: none
    primary_language: latin
  - wish_type: event
    hint: "洗礼・出生・共同体行事に関わる水方系祈祷；Pater Noster／Ave Maria／洗礼式文を伴う"
    officiant: kakure-kirishitan-mizukata
    primary_language: latin
  - wish_type: event
    hint: "旅立ち・年中祭・地域儀礼の前後に、長老役がオラショを唱えて共同体と家筋を記念する現代伝承型"
    officiant: kakure-ojiiyaku
    primary_language: japanese

verification:
  - "Christal Whelan, The Beginning of Heaven and Earth: The Sacred Book of Japan’s Hidden Christians, University of Hawai‘i Press, 1996."
  - "Stephen Turnbull, The Kakure Kirishitan of Japan: A Study of Their Development, Beliefs and Rituals to the Present Day, Japan Library, 1998."
  - "C. R. Boxer, The Christian Century in Japan, 1549–1650, University of California Press, 1951."
  - "Higashibaba Ikuo, Christianity in Early Modern Japan: Kirishitan Belief and Practice, Brill, 2001."
  - "Dochirina Kirishitan, 1592/1600 editions; sections on Pater Noster, Ave Maria, Credo, Ten Commandments."
  - "Manuale ad Sacramenta Ecclesiae ministranda, Nagasaki, 1605; baptismal and funeral offices."
  - "https://www.britannica.com/topic/Kakure-Kirishitan"
  - "https://www.britishmuseum.org/blog/hidden-christians-japan"
  - "https://www.nippon.com/en/japan-topics/g00729/"
  - "https://en.wikipedia.org/wiki/Kakure_Kirishitan"
  - "https://www.nippon.com/en/japan-topics/c12905/"
  - "https://oratio.jp/"
---

# 隠れキリシタン

## 结构
[十字のしるし] → [デウスへの呼びかけ] → [主祷文 Pater Noster] → [天使祝詞 Ave Maria] → [小栄唱 Gloria Patri] → [願意挿入] → [信経 Credo または痛悔 Konchirisan] → [サンタマリアへの取次 Salve Regina] → [死者・共同体・願意の記念] → [結びの栄唱]

## 通用骨架（占位符版本）
```
In nomine Patris, et Filii, et Spiritus Sancti. Amen.

Deus, Senhor do Céu, Deus padre, Deus filho, Deus spirito santo,
por {{anchors.person_name}}, por {{anchors.household_name}}, por {{anchors.place_name}},
em {{anchors.petition}}.

Pater noster, qui es in caelis,
sanctificetur nomen tuum.
Adveniat regnum tuum.
Fiat voluntas tua, sicut in caelo et in terra.
Panem nostrum quotidianum da nobis hodie.
Et dimitte nobis debita nostra,
sicut et nos dimittimus debitoribus nostris.
Et ne nos inducas in tentationem,
sed libera nos a malo. Amen.

Ave Maria, gratia plena, Dominus tecum.
Benedicta tu in mulieribus,
et benedictus fructus ventris tui, Iesus.
Sancta Maria, Mater Dei,
ora pro nobis peccatoribus,
nunc et in hora mortis nostrae. Amen.

Gloria Patri, et Filio, et Spiritui Sancto.
Sicut erat in principio, et nunc, et semper,
et in saecula saeculorum. Amen.

Credo in Deum Patrem omnipotentem,
Creatorem caeli et terrae,
et in Iesum Christum, Filium eius unicum, Dominum nostrum,
qui conceptus est de Spiritu Sancto,
natus ex Maria Virgine,
passus sub Pontio Pilato,
crucifixus, mortuus, et sepultus,
descendit ad inferos,
tertia die resurrexit a mortuis,
ascendit ad caelos,
sedet ad dexteram Dei Patris omnipotentis,
inde venturus est iudicare vivos et mortuos.
Credo in Spiritum Sanctum,
sanctam Ecclesiam catholicam,
sanctorum communionem,
remissionem peccatorum,
carnis resurrectionem,
vitam aeternam. Amen.

Deus meus, ex toto corde paenitet me omnium meorum peccatorum,
quia peccando non solum poenas a te iuste statutas promeritus sum,
sed praesertim quia offendi te, summum bonum ac dignum qui super omnia diligaris.
Ideo firmiter propono, adiuvante gratia tua,
de cetero me non peccaturum peccandique occasiones proximas fugiturum. Amen.

Salve Regina, Mater misericordiae,
vita, dulcedo, et spes nostra, salve.
Ad te clamamus, exsules filii Evae.
Ad te suspiramus, gementes et flentes in hac lacrimarum valle.
Eia ergo, advocata nostra,
illos tuos misericordes oculos ad nos converte.
Et Iesum, benedictum fructum ventris tui,
nobis post hoc exsilium ostende.
O clemens, O pia, O dulcis Virgo Maria.

Requiem aeternam dona ei, Domine,
et lux perpetua luceat ei.
Requiescat in pace. Amen.
Pro {{anchors.deceased_name}}.

In nomine Patris, et Filii, et Spiritus Sancti. Amen.
```