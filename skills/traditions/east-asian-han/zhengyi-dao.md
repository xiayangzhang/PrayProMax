---
id: zhengyi-dao
name: 正一道 / 天师道
name_en: Zhengyi Dao (Celestial Masters)
category: east-asian-han
deity_based: true
self_pray_capable: partial
required_officiants:
  - zhengyi-daoshi
officiant_notes: "净心、宝诰、简短祝白可自念；章奏、符箓、雷法、度亡斋醮须由受箓正一法师主持。"
authoritative_texts:
  - "《正一法文天师教戒科经》卷上、卷下，道藏洞神部戒律类"
  - "《赤松子章历》卷一至卷六，章奏文书与投章仪式"
  - "《太上三洞神咒》玉清、雷部神咒条"
  - "《道门科范大全集》斋醮章表科仪"
  - "《高上神霄玉清真王紫书大法》雷霆法文与雷部奏告"
  - "《九天应元雷声普化天尊玉枢宝经》雷声普化天尊宝诰与雷部经诰"
primary_languages:
  - classical-chinese
backlash_risk: high
mitigation: "限于净心、宝诰、祝白与回向；章奏、符箓、雷法、召将遣将、度亡科仪交由受箓正一法师。"
taboos:
  - "不得未受箓而擅称法职、妄行符箓雷法。"
  - "不得以章奏虚报姓名、生辰、事由、愿目。"
  - "不得以雷法、符命作害人、诅咒、报复之用。"
  - "不得在斋醮章奏中秽语戏慢、酒肉昏乱、轻慢三宝经箓。"
  - "不得泄露师承秘讳、内讳、符胆、诀目。"
search_strategy: |
  正一道 玉清咒 雷霆咒 章奏文
  赤松子章历 章奏 文书 正一道
  正一法文天师教戒科经 道藏
  九天应元雷声普化天尊宝诰 玉枢宝经
  道门科范大全集 章表 科仪
case_index:
  - wish_type: health
    hint: "净心神咒、玉清宝诰、章奏文: 为{{anchors.beneficiary_name}}祈安康之简祝可自念；正式祈病章奏须法师。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: wealth
    hint: "章奏文: 祈财禄、营生安稳以表章奏告，不以雷法取财。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: protection
    hint: "金光神咒、玉清宝诰、雷霆咒 / 九天应元雷声普化天尊宝诰；涉及召雷遣将须法师。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: deceased
    hint: "灵宝度亡科、救苦宝诰、章奏文: 超荐亡者须法师行科。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: relationship
    hint: "章奏文: 解冤释结、和合亲族之奏告，不作强制他人意志之法。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: wisdom
    hint: "净心神咒、玉清宝诰: 澄心明性之祝白可自念。"
    officiant: none
    primary_language: classical-chinese
  - wish_type: breaking
    hint: "雷霆咒、雷部章奏文: 破秽、解厄、断邪须受箓正一法师，不自行召雷遣将。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
  - wish_type: event
    hint: "章奏文: 行旅、考试、开工、迁居等事由以表章奏告；简短祝白可自念，正式投章须法师。"
    officiant: zhengyi-daoshi
    primary_language: classical-chinese
verification:
  - "《正一法文天师教戒科经》卷上、卷下，道藏本"
  - "《赤松子章历》卷一至卷六，道藏本"
  - "《道门科范大全集》道藏本，章表科仪门"
  - "《九天应元雷声普化天尊玉枢宝经》道藏本"
  - "Kristofer Schipper and Franciscus Verellen, eds., The Taoist Canon: A Historical Companion to the Daozang, University of Chicago Press, 2004"
---

# 正一道 / 天师道

## 结构
[净心净口] → [皈依大道] → [玉清宝诰] → [祝白 / 章奏] → [雷部宝诰或雷霆咒] → [回向] → [伏愿]

## 通用骨架
```
净心神咒：
太上台星，应变无停。驱邪缚魅，保命护身。智慧明净，心神安宁。三魂永久，魄无丧倾。急急如律令。

净口神咒：
丹朱口神，吐秽除氛。舌神正伦，通命养神。罗千齿神，却邪卫真。喉神虎贲，炁神引津。心神丹元，令我通真。思神炼液，道炁常存。急急如律令。

志心皈命礼：
太上无极大道，三十六部尊经，玄中大法师，历代祖师，正一盟威经箓法脉。

玉清宝诰：
志心皈命礼。
三界之上，梵炁弥罗。上极无上，天中之天。
郁罗萧台，玉山上京。渺渺金阙，森罗净泓。
玄元一炁，混沌之先。宝珠之中，玄之又玄。
开明三景，化生诸天。亿万天真，无鞅数众。
旋斗历箕，回度五常。巍巍大范，万道之宗。
大罗玉清，虚无自然，至真妙道，元始天尊。

章奏祝白：
伏以大道无形，生育天地；玄元一炁，陶铸阴阳。
今有{{anchors.petitioner_identity}} {{anchors.petitioner_name}}，
居住{{anchors.petitioner_location}}，
为{{anchors.wish_subject}}事，
谨以清净之心，具陈{{anchors.petition_detail}}。
伏愿玉清圣境，元始天尊，鉴此丹诚；
俾{{anchors.beneficiary_name}}身心清泰，灾障消弭，冤结解释，善愿圆成。
若有过咎，愿从忏悔；若有虚妄，愿悉改正。
臣心皈大道，愿不违科戒，不妄称法职，不假法害物。

雷部宝诰：
志心皈命礼。
九天应元府，无上玉清王。
化形而满十方，谈道而趺坐九凤。
三十六天之上，阅宝笈，考琼书。
千五百劫之先，位正真，权大化。
手举金光如意，宣说玉枢宝经。
不顺化作微尘，发号疾如风火。
以清静心而弘大愿，以智慧力而伏诸魔。
总司五雷，运心三界。群生父，万灵师。
大圣大慈，至皇至道，九天应元雷声普化天尊。

雷霆咒：
雷霆号令，速降威灵。
欻火律令，霹雳轰轰。
神雷一发，万邪灭形。
急急如九天应元雷声普化天尊律令。

回向：
愿以此清净功德，上报大道玄恩，下资{{anchors.beneficiary_name}}。
所愿{{anchors.wish_summary}}，悉归正道；所作善因，普及有情。
伏愿天尊证明，祖师护念，三界清宁，内外安和。
稽首皈依，无上大道。
```