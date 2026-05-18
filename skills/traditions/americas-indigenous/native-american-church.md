---
id: native-american-church
name: 美洲原住民教会（NAC）
name_en: Native American Church (NAC)
category: americas-indigenous
deity_based: true

self_pray_capable: partial
required_officiants:
  - nac-roadman
  - nac-fireman
  - nac-drummer
officiant_notes: 正式 peyote meeting / fireplace prayer service 由获本教会与家族授权的 Roadman 主持，并由 fireman、drummer 等礼仪角色维持火、鼓、歌与会场秩序；个人可作非圣礼性祈祷，但不可自称主持正式仪式。

authoritative_texts:
  - "Native American Church of North America, Code of Ethics, arts. I–IV"
  - "American Indian Religious Freedom Act Amendments of 1994, 42 U.S.C. § 1996a(b)(1)–(5)"
  - "Omer C. Stewart, Peyote Religion: A History, chs. 6–8"
  - "James S. Slotkin, The Peyote Religion, chs. 5–7"
  - "Weston La Barre, The Peyote Cult, chs. 2–4"
primary_languages:
  - english
  - navajo
  - comanche
  - kiowa
  - lakota
  - various-indigenous-languages
  - vocables

backlash_risk: high
mitigation: 仅保留公开、泛化的祷词骨架；不伪造部族授权、不复制家族专属 peyote song、不指示取得或使用受管制圣物；涉及正式会仪时必须交由 NAC 授权 Roadman 与本地会众处理。
taboos:
  - 未经 NAC 章节、家族或 Roadman 授权，不得主持、出售、录制、公开传播或改编 peyote meeting 与专属 peyote songs。
  - 不得将 peyote 作为娱乐性、商业性、猎奇性或脱离教会纪律的物质使用。
  - 不得在同一祷词段落混杂非 NAC 神灵体系、现代显化术、诅咒术或外来神秘学召请。
  - 不得冒称具体部族、火路、家族传承或 Roadman 资格。
  - 不得把病痛、创伤、丧事或家庭纠纷当作绕过会众授权与法律限制的理由。
  - 不得公开索要或泄露本教会、家族、会场中被视为保留或闭合的歌、火路细节、器物排列和个人忏悔内容。

search_strategy: |
  "Native American Church Code of Ethics peyote Roadman"
  "42 USC 1996a American Indian Religious Freedom Act peyote Native American Church"
  "Omer C. Stewart Peyote Religion ceremony roadman songs"
  "James Slotkin The Peyote Religion peyote songs ceremony"
  "Native American Church fireplace roadman drummer fireman cedar man water woman"

case_index:
  - wish_type: health
    hint: "Healing meeting / doctoring prayer；Roadman 以 Creator / Great Spirit / Jesus 方向的祈祷、cedar、water、drum 与授权 peyote song 为病者 {{anchors.person_name}} 祈求身心恢复"
    officiant: nac-roadman
    primary_language: english
  - wish_type: wealth
    hint: 无
    officiant: none
  - wish_type: protection
    hint: "Protection prayer；Roadman 以 Creator / Great Spirit 方向的祈祷与授权 peyote song 为 {{anchors.person_name}}、家庭与行路求护持"
    officiant: nac-roadman
    primary_language: english
  - wish_type: deceased
    hint: "Funeral / memorial peyote meeting；Roadman 在会众与家属面前为 {{anchors.deceased_name}}、遗族与道路安宁祈祷"
    officiant: nac-roadman
    primary_language: english
  - wish_type: relationship
    hint: "Family reconciliation prayer；Roadman 以会众见证、忏悔、宽恕祈祷与授权 peyote song 为 {{anchors.person_name}} 与 {{anchors.other_person_name}} 求和解"
    officiant: nac-roadman
    primary_language: english
  - wish_type: wisdom
    hint: "Guidance prayer；Roadman 以 Creator / Great Spirit 方向的祈祷、聆听、歌与夜间会仪次第为 {{anchors.person_name}} 求清明道路"
    officiant: nac-roadman
    primary_language: english
  - wish_type: breaking
    hint: 无
    officiant: none
  - wish_type: event
    hint: "Special meeting prayer；Roadman 为 {{anchors.event_name}}、{{anchors.person_name}} 与相关家人祈求道路平安、心意端正与会众支持"
    officiant: nac-roadman
    primary_language: english

verification:
  - "42 U.S.C. § 1996a, Traditional Indian religious use of peyote: https://www.law.cornell.edu/uscode/text/42/1996a"
  - "American Indian Religious Freedom Act Amendments of 1994, Pub. L. 103-344, 108 Stat. 3125"
  - "Omer C. Stewart, Peyote Religion: A History, University of Oklahoma Press, 1987, chs. 6–8"
  - "James S. Slotkin, The Peyote Religion: A Study in Indian-White Relations, Free Press, 1956, chs. 5–7"
  - "Weston La Barre, The Peyote Cult, 5th ed., University of Oklahoma Press, 1989, chs. 2–4"
---

# 美洲原住民教会（NAC）

## 结构
[开场称名与净心] → [说明祈祷对象与会众见证] → [向 Creator / Great Spirit / Father God 呼告] → [为当事人与家族陈明祈愿] → [公开经文或公共赞歌段落] → [授权 peyote song 段落] → [忏悔、宽恕与端正道路] → [为会众、祖先与后代作总祷] → [感谢与 Amen]

## 通用骨架（占位符版本）
```
Creator, Great Spirit, Father God,
we come before You with humble hearts.

We place before You {{anchors.person_name}},
the family of {{anchors.family_name}},
and the matter called {{anchors.prayer_intention}}.

Our Father, which art in heaven,
Hallowed be thy Name.
Thy Kingdom come.
Thy will be done in earth,
As it is in heaven.
Give us this day our daily bread.
And forgive us our trespasses,
As we forgive them that trespass against us.
And lead us not into temptation;
But deliver us from evil.
For thine is the kingdom,
The power, and the glory,
For ever and ever.
Amen.

Creator, Great Spirit,
look upon {{anchors.person_name}}.
Straighten the road before {{anchors.person_name}}.
Put good mind, clean heart, and strong breath
in {{anchors.person_name}} and in the people gathered for {{anchors.prayer_intention}}.

Amazing grace! how sweet the sound,
That saved a wretch like me!
I once was lost, but now am found;
Was blind, but now I see.

He-ne-ne-yo-wa,
He-ne-ne-yo-wa,
He-ne-ne-yo-wa,
He-ne-ne-yo-wa.

Creator, Great Spirit,
if there is hurt, let truth stand.
If there is fear, let courage stand.
If there is anger, let forgiveness stand.
If there is sickness, let help and mercy stand.
If there is grief, let the family of {{anchors.family_name}} stand together.

We remember the old people,
the ones who prayed before us,
the ones who carried the road,
the ones who kept the fire,
the songs, the water, the cedar, and the drum
in a good way.

Bless {{anchors.person_name}}.
Bless {{anchors.family_name}}.
Bless the children, the elders, the relatives,
and all who are named in {{anchors.prayer_intention}}.

Creator, Great Spirit,
thank You for hearing this prayer.
Thank You for life.
Thank You for this road.

Amen.
```