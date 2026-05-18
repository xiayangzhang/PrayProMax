---
id: tenrikyo
name: 天理教
name_en: Tenrikyo
category: east-asian-japan
deity_based: true
self_pray_capable: partial
required_officiants:
  - tenrikyo-yoboku
  - tenrikyo-church-minister
officiant_notes: "日常拝礼与「みかぐらうた」唱和可自念；「おさづけ」取次、教会祭儀、葬儀・霊祭等须由受资格者或教会主持。"
authoritative_texts:
  - "『みかぐらうた』第一節「よろづよ八首」及び十二下り"
  - "『おふでさき』第一号—第十七号"
  - "『おさしづ』明治二十年正月四日以降諸指図"
  - "『天理教教典』第三章「元の理」、第六章「てびき」、第七章「かしもの・かりもの」"
primary_languages:
  - japanese
  - classical-japanese
backlash_risk: medium
mitigation: "以親神への御礼・たすけ一条に限定し、利益交換・呪詛・無資格の「おさづけ」模倣を避け、教会祭儀は教会長または所定役割に委ねる。"
taboos:
  - "「おさづけ」は授与を受けたようぼく以外が取次を称して行わない。"
  - "かぐらづとめはぢばで行われる本来的祭儀であり、私的に面・所作を模倣して神事化しない。"
  - "祈願を呪詛、怨敵調伏、強制的な縁切り・支配に用いない。"
  - "病気・災難を金銭取引の治療保証として扱わない。"
  - "八つのほこり（をしい・ほしい・にくい・かわい・うらみ・はらだち・よく・こうまん）を正当化する願意にしない。"
  - "自己中心的・不合理な願意を祈願の中心にしない。"
  - "不浄・不平不満・感謝を欠く心のまま祭儀や唱和を行わない。"
search_strategy: |
  "Tenrikyo Otsutome" OR "Mikagura-uta" prayer text
  Tenrikyo Sazuke administration
  Tenrikyo morning evening service home practice
  site:tenrikyo.or.jp OR site:tenrikyoamericacanada.org prayers
  Tenrikyo memorial service ancestors
case_index:
  - wish_type: health
    hint: "「おさづけの理」取次、ならびに『みかぐらうた』冒頭句「あしきをはらうて たすけたまへ 天理王命」による病身平癒・心のほこり払いの祈り。"
    officiant: tenrikyo-yoboku
    primary_language: japanese
  - wish_type: health
    hint: "日常拝礼・朝夕のおつとめとして、『みかぐらうた』冒頭句「あしきをはらうて たすけたまへ 天理王命」を唱和し、身上の悪しき払いと御守護を願う祈り。"
    officiant: none
    primary_language: japanese
  - wish_type: wealth
    hint: "特定の金運呪法は立てず、『みかぐらうた』十二下り・「ひのきしん」精神に即した、かしもの・かりものへの御礼と陽気ぐらしへの願い。"
    officiant: none
    primary_language: japanese
  - wish_type: protection
    hint: "『みかぐらうた』冒頭句「あしきをはらうて たすけたまへ 天理王命」を中心とする、身上・事情の悪しき払いと親神への守護願い。"
    officiant: none
    primary_language: japanese
  - wish_type: deceased
    hint: "天理教葬儀・霊祭における親神天理王命への祭詞、故人の御霊を親神の守護に委ねる祈り。"
    officiant: tenrikyo-church-minister
    primary_language: japanese
  - wish_type: deceased
    hint: "家庭での拝礼として、先人・祖霊への感謝を述べ、故人の御霊を親神天理王命の御守護に委ねる祈り。"
    officiant: none
    primary_language: japanese
  - wish_type: relationship
    hint: "『おふでさき』「世界一れつみな兄弟」および『みかぐらうた』に即し、夫婦・親子・周囲との心のほこりを払う和合祈願。"
    officiant: none
    primary_language: japanese
  - wish_type: wisdom
    hint: "『おふでさき』拝読と親神天理王命への心定めの祈り；悟り・判断を私利ではなく「たすけ一条」に向ける。"
    officiant: none
    primary_language: japanese
  - wish_type: breaking
    hint: "呪詛解除ではなく、『みかぐらうた』冒頭句「あしきをはらうて たすけたまへ 天理王命」による悪しき心遣い・因縁的事情の払い。"
    officiant: none
    primary_language: japanese
  - wish_type: event
    hint: "教会祭儀または日常拝礼で『みかぐらうた』冒頭句と御礼を奏し、受験・旅・出産・移転等を親神の守護に委ねる祈り。"
    officiant: none
    primary_language: japanese
verification:
  - "Tenrikyo Church Headquarters, 『みかぐらうた』／The Songs for the Service."
  - "Tenrikyo Church Headquarters, 『おふでさき』／The Tip of the Writing Brush, Parts I–XVII."
  - "Tenrikyo Church Headquarters, 『おさしづ』／The Divine Directions."
  - "Tenrikyo Church Headquarters, 『天理教教典』, chapters on 元の理, かしもの・かりもの, てびき."
  - "https://www.tenrikyo.or.jp/"
  - "https://www.tenrikyo.or.jp/en/"
  - "https://en.wikipedia.org/wiki/Service_(Tenrikyo)"
  - "https://tenrikyoamericacanada.org/mikagura-uta-the-songs-of-the-service"
---

# 天理教

## 结构
[拝礼・親神名奉称] → [御礼] → [願意の表明] → [正行：「みかぐらうた」冒頭句・必要に応じて『おふでさき』拝読] → [心定め] → [御礼・結び]

## 通用骨架（占位符版本）
```
親神天理王命様

本日、{{anchors.place}}にて、{{anchors.prayer_name}}、つつしみて拝礼いたします。

親神天理王命様、
この身はかしもの・かりものにて、
今日までの御守護をありがたく存じます。

{{anchors.person_name}}の{{anchors.wish_matter}}につき、
心のほこりを払い、たすけ一条の心に立ち返り、
親神様の御守護を仰ぎ奉ります。

あしきをはらうて　たすけたまへ
天理王命

あしきをはらうて　たすけたまへ
天理王命

あしきをはらうて　たすけたまへ
天理王命

ちよとはなし　かみのいふこときいてくれ
あしきのことはいはんでな

このよふを　はじめたかみのことならば
せかい一れつ　みなわがこなり

{{anchors.person_name}}、{{anchors.relationship_or_context}}において、
{{anchors.vow_or_resolution}}の心を定め、
をしい・ほしい・にくい・かわい・うらみ・はらだち・よく・こうまんのほこりを慎み、
陽気ぐらしへ向かう心をもって歩みます。

親神天理王命様、
本日の祈りを御前に納め奉ります。

あしきをはらうて　たすけたまへ
天理王命
```