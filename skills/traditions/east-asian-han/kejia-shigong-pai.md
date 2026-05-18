---
id: kejia-shigong-pai
name: 客家师公派
name_en: Hakka Shigong Pai
category: east-asian-han
deity_based: true

self_pray_capable: partial
required_officiants:
  - shigong
officiant_notes: 师公唱戏、请神、安龙、解煞、送亡等科仪须由传承师公主持；家内简短告祖、告神可自念。

authoritative_texts:
  - 客家师公抄本《师公唱戏神歌词》：请神、唱神、谢神、送圣诸段
  - 客家师公抄本《安龙谢土科》：启坛、请龙神、安龙、谢土段
  - 客家师公抄本《超度送亡科》：开路、引魂、过桥、送亡段
  - 客家师公抄本《解关破煞科》：请师、申牒、解结、送煞段
  - 民间师公科仪本：打斋、请神、破狱等唱本
  - 《中国戏曲志·广西卷》“师公戏”条
  - 《中国民间歌曲集成·广西卷》“师公歌”条
primary_languages:
  - hakka-chinese
  - literary-chinese

backlash_risk: medium
mitigation: 不冒充师承、不替代正式科仪；涉及亡魂、解煞、安龙、还愿时转由师公依本坛科本办理。
taboos:
  - 忌未受师承而冒称师公开坛、押煞、遣将、送亡。
  - 忌请神而不谢神、许愿而不还愿。
  - 忌在同一启请段混请无关神系或把祖先、坛神、阴魂混同称呼。
  - 忌将丧事科、喜庆科、安龙科、解煞科互相混用。
  - 忌在不明对象时妄呼亡名、妄送孤魂、妄作替身。
  - 忌以污秽、戏谑、咒骂语入神前唱词。
  - 女性经期不可近主坛。
  - 未经师公开光不得擅用神器。
  - 忌在不洁场所或凶时擅自唱神歌。

search_strategy: |
  "客家师公" OR "Hakka Shigong" OR "万丰坛" 打斋 OR 破地狱
  师公 唱戏 神歌词 OR Hakka ritual master chants
  客家 师公派 法事 科仪

case_index:
  - wish_type: health
    hint: 《请神保安唱词》：启坛净口、请本坛师公祖师与保生类神明、报名告病、唱保安词、谢神回向。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: wealth
    hint: 《招财进宝唱词》：请财神、土地、灶君，报名告愿，唱招财纳福词，申明正财与家业平安，谢神。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: protection
    hint: 《安龙谢土科》：启坛、请龙神土地、安龙脉、镇宅门、谢土回向。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: deceased
    hint: 《超度送亡科》：开路、引魂、过桥、送亡、告祖、回向亡者。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: relationship
    hint: 《和合保家唱词》：请家神祖先与和合神，报名告愿，唱和合、息争、安家词，谢神。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: wisdom
    hint: 《文昌启智唱词》：请文昌帝君、魁星，报名告学业功名，唱开聪明词，谢神。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: breaking
    hint: 《解关破煞科》：请师公祖师、申牒、解关、破煞、送煞、谢师。
    officiant: shigong
    primary_language: hakka-chinese
  - wish_type: event
    hint: 《出行过关唱词》：请路神、土地、祖先护行，报名告事，唱过关平安词，谢神。
    officiant: shigong
    primary_language: hakka-chinese

verification:
  - 《中国戏曲志·广西卷》，“师公戏”条，中国ISBN中心，1995。
  - 《中国民间歌曲集成·广西卷》，“师公歌”条，中国ISBN中心，1996。
  - 《中国民间文学集成·广东卷》有关客家师公歌、请神歌、还愿歌条目。
  - Wolfram Eberhard, The Local Cultures of South and East China, E. J. Brill, 1968, sections on Hakka ritual specialists and local cults.
  - David K. Jordan, Gods, Ghosts, and Ancestors: Folk Religion in a Taiwanese Village, University of California Press, 1972, chs. 2-5 on Han folk ritual categories comparable to southern Chinese household and specialist rites.
  - https://wanfengtan.blogspot.com/ （客家师公仪式记录）
  - 台湾及马来西亚客家打斋科仪实践。
---

# 客家师公派

## 结构
[净坛启白] → [请师请神] → [报名告愿] → [唱神正行] → [申文立愿] → [谢神送圣] → [回向]

## 通用骨架（占位符版本）
```
伏以：
香烟起处，法界通明；
宝烛光中，神灵鉴临。

弟子{{anchors.devotee_name}}，住居{{anchors.place}}，
今为{{anchors.petition_subject}}，谨具清香宝烛，虔诚启告。

一请本坛历代师公祖师。
伏愿祖师临坛，鉴纳微诚。

二请{{anchors.deity_name}}。
伏愿圣驾临坛，鉴纳微诚。

三请本境土地龙神。
伏愿土地龙神临坛，护佑本境。

四请家堂香火、历代祖先。
伏愿家堂祖先临前，照看门庭。

香花请，宝烛迎；
请神来到坛前坐，请圣来到案上停。
上坛师公开金口，下坛弟子表丹诚。
今日所告非虚语，句句分明奏上庭。

弟子{{anchors.devotee_name}}，为{{anchors.wish_statement}}，
若有惊恐不安，愿得安宁；
若有阻隔不顺，愿得开通；
若有冤结牵缠，愿得解释；
若有阴阳未妥，愿得分明。

唱曰：
一炷清香透九天，二炷宝香达神前；
三炷名香诚心献，奉请{{anchors.deity_name}}降坛筵。
神来有座，圣到有筵。

左边龙神护宅舍，右边土地保门前。

祖先堂上添香火，家内人口得安然。

今将{{anchors.petition_detail}}，一一禀明：
{{anchors.petition_detail}}

愿{{anchors.deity_name}}垂慈鉴纳。

愿本坛师公祖师扶持。

愿本境土地龙神护佑。

愿家堂祖先照看。

若愿成之日，弟子{{anchors.devotee_name}}谨依{{anchors.vow_return}}酬谢，
不敢忘恩，不敢失信。

再唱曰：
神恩浩荡如江水，圣德巍巍似岭岗；
有求须从正路求，有愿须从本心讲。
保得{{anchors.petition_subject}}清吉，
护得{{anchors.household_or_person}}平安。
凶星退位，吉曜临门；
口舌消散，灾障消沉。

谨将今日功德，回向{{anchors.dedication_target}}：
愿生者安宁，亡者超升；
愿内外和合，门户清平；
愿所求合道，所愿成真。

礼谢本坛历代师公祖师。

礼谢{{anchors.deity_name}}。

礼谢本境土地龙神。

礼谢家堂香火、历代祖先。

神归神位，圣返圣乡；
香烟送驾，宝烛照程。
来时有请，去时有送；
坛前清吉，宅内安康。

谨启。
```