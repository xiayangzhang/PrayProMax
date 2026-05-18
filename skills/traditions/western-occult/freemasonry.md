---
id: freemasonry
name: 共济会
name_en: Freemasonry
category: western-occult
deity_based: true
self_pray_capable: partial
required_officiants:
  - masonic-worshipful-master
  - masonic-chaplain
officiant_notes: 私人祈祷可自念；会所开闭会、入会誓约、晋级、葬礼等正式仪文须由合法会所及其 Worshipful Master、Chaplain 或相应职员主持。
authoritative_texts:
  - "James Anderson, The Constitutions of the Free-Masons (1723), Charges I: Concerning God and Religion; VI: Of Behaviour"
  - "Duncan's Masonic Ritual and Monitor (1866), Opening and Closing Prayers; Entered Apprentice Degree; Fellow Craft Degree; Master Mason Degree; Masonic Funeral Service"
  - "Emulation Ritual, First Degree Opening and Closing; Installation and Lodge Prayers, as used in English Craft Masonry"
  - "Holy Bible, King James Version: Psalm 133; Ecclesiastes 12:1-7; Amos 7:7-8; 1 Kings 6-7"
  - "Ahiman Rezon / Book of Constitutions traditions, Charges and Prayers used in Craft lodges"
  - "Lodge Opening/Closing Prayers in various Grand Lodge Monitors"
  - "Entered Apprentice, Fellow Craft, and Master Mason Obligations as referenced in public monitor traditions"
primary_languages:
  - english
  - biblical-hebrew
backlash_risk: medium
mitigation: 仅采用公开祷文、圣经段落与非秘密称谓；不得仿造入会誓词、秘密字、握手、暗号或宣称取得会籍、等级、会所授权。
taboos:
  - 不得泄露或伪造共济会秘密字、暗号、握手、入会誓词及等级工作细节。
  - 不得向非会员公开会内秘密、识别方式或义务细节。
  - 不得在会所内争论宗教教义或政党政治。
  - 不得以无神论或否认至高存在者的立场参加正规共济会祈祷与仪式。
  - 不得以共济会名义谋取私利、欺诈、胁迫或作非法目的。
  - 不得将私人祈祷冒充为合法会所开闭会、入会、晋级或葬礼仪文。
search_strategy: |
  "Freemasonry lodge opening closing prayer" OR "Great Architect of the Universe prayer"
  "Masonic degree obligations" OR "Entered Apprentice oath text"
  Freemasonry modern practices OR contemporary rituals site:reddit.com/r/freemasonry
  "co-masonry" OR "women's freemasonry" prayers
  "Masonic Funeral Service" "Duncan" "So mote it be"
  "Anderson Constitutions 1723" "Concerning God and Religion"
case_index:
  - wish_type: health
    hint: "Masonic Opening Prayer / General Petition to the Great Architect of the Universe for aid, harmony, and moral strength"
    officiant: none
    primary_language: english
  - wish_type: wealth
    hint: 无
    officiant: none
  - wish_type: protection
    hint: "Masonic Opening Prayer invoking the Great Architect of the Universe for order, peace, and safe conduct"
    officiant: none
    primary_language: english
  - wish_type: deceased
    hint: "Masonic Funeral Service prayer: Almighty Father, into Thy hands we commend the soul of our departed brother"
    officiant: masonic-chaplain
    primary_language: english
  - wish_type: relationship
    hint: "Psalm 133 / Entered Apprentice fraternal harmony text: Behold, how good and how pleasant it is for brethren to dwell together in unity"
    officiant: none
    primary_language: biblical-hebrew
  - wish_type: wisdom
    hint: "Masonic Opening Prayer to the Great Architect of the Universe for Wisdom, Strength, and Beauty in moral work"
    officiant: none
    primary_language: english
  - wish_type: breaking
    hint: 无
    officiant: none
  - wish_type: event
    hint: "Lodge Opening / Closing Prayer formula: Great Architect of the Universe, direct us in all our doings"
    officiant: masonic-worshipful-master
    primary_language: english
  - wish_type: event
    hint: "Contemporary co-masonry or women's Freemasonry public opening/closing prayer variants addressed to the Great Architect of the Universe"
    officiant: none
    primary_language: english
verification:
  - "James Anderson, The Constitutions of the Free-Masons, London, 1723, Charges I and VI."
  - "Malcolm C. Duncan, Duncan's Masonic Ritual and Monitor, New York, 1866, sections: Opening Prayer; Closing Prayer; Funeral Service."
  - "https://www.sacred-texts.com/mas/dun/index.htm"
  - "https://sacred-texts.com/mas/gar/gar11.htm"
  - "United Grand Lodge of England, Freemasonry and Religion: https://www.ugle.org.uk/about-us/freemasonry-and-religion"
  - "Holy Bible, King James Version, Psalm 133; Ecclesiastes 12:1-7; Amos 7:7-8."
---

# 共济会

## 结构
[承认至高存在者 / Great Architect of the Universe] → [合法与谦卑的陈述] → [求智慧、力量、和谐与正直] → [兄弟合一经文] → [为特定对象或事件陈述] → [保守秘密与合乎道德的自我约束] → [共济会式结语]

## 通用骨架（占位符版本）
```
Most holy and glorious Lord God,
the Great Architect of the Universe,
the Giver of all good gifts and graces:

Thou hast promised that where two or three are gathered together in Thy Name,
Thou wilt be in the midst of them and bless them.

In Thy Name, and in reverence before Thy presence,
I place this petition concerning {{anchors.subject}}
and the matter of {{anchors.intent}}.

Grant that every thought, word, and act
may be ordered by Wisdom,
supported by Strength,
and adorned with Beauty.

הִנֵּה מַה־טּוֹב וּמַה־נָּעִים
שֶׁבֶת אַחִים גַּם־יָחַד׃

Let Brotherly Love, Relief, and Truth
govern my heart toward {{anchors.person_or_brethren}}.
Let no anger, vanity, unlawful gain, false witness,
or betrayal of trust enter this work.

If this prayer concerns the departed,
receive with mercy {{anchors.deceased_name}},
and keep the living in sobriety, remembrance, and peace.

If this prayer concerns a journey, undertaking, meeting, labor, or event,
direct the work of {{anchors.event_name}}
so that it may proceed in order, concord, and uprightness.

Keep me faithful to every lawful obligation,
silent where silence is due,
truthful where speech is required,
and charitable toward all mankind.

May the Supreme Grand Master
preside over this intention,
until all work is closed in peace.

So mote it be.
```