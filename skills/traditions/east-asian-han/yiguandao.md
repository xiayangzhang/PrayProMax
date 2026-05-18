---
id: yiguandao
name: 一貫道
name_en: Yiguandao
category: east-asian-han
deity_based: true
self_pray_capable: partial
required_officiants:
  - yiguandao-dianchuanshi
officiant_notes: 求道、點玄關、傳三寶、超拔拔薦等須由點傳師或壇務授權人員主持；日常獻香叩首、誦念愿文可由已入道者自念。
authoritative_texts:
  - 暫定佛規：求道禮、請壇禮、獻供禮、叩首禮、辦道規程
  - 一貫道禮本：獻香叩首、早晚獻香、愿文、回向文
  - 彌勒救苦真經：全經
  - 皇母訓子十誡：十誡訓文
  - 一貫道疑問解答：求道、三寶、佛規禮節相關條目
  - 師尊師母慈訓及仙佛寶訓
  - 經典綜合：四書、五經、佛經、道藏選用
primary_languages:
  - classical-chinese
  - mandarin-chinese
backlash_risk: high
mitigation: 三寶與五字真言屬入道後內傳內容，非入道者不得冒稱已受傳；公開文本應限於壇前禮文、愿文、經文名目與非祕密稱誦，涉及求道、點傳、超拔須交由點傳師處理。
taboos:
  - 未經求道不得冒稱受明師一指或自行點玄關。
  - 三寶不得向未入道者戲言、妄傳、公開演示或作表演化使用。
  - 壇前禮節忌嬉笑、褻慢、酒肉穢氣、衣冠不整與不依佛規叩拜。
  - 不得以祈禱名義求害人、詛咒、賭博、欺詐或違背愿文之事。
  - 不得將仙佛聖號、五字真言或求道儀節與外道咒術、商業招財術混雜。
  - 超拔拔薦、求道、開壇等不得由未授權者私辦。
  - 不得洩漏三寶。
  - 忌虛心假意，求道後違背所立愿心。
  - 壇前供品忌用非素食供品。
search_strategy: |
  "一貫道 佛堂 參駕 獻香 禮節" OR "一貫道 恭迎佛駕"
  "Yiguandao three treasures" OR "一貫道 三寶 五字真言" (post-initiation contexts)
  "一貫道 早午晚獻香" OR "Yiguandao prayer hall ritual" Taiwan
  site:facebook.com OR site:pixnet.net 一貫道 禱告 OR 默念 OR 守玄
case_index:
  - wish_type: health
    hint: 以一貫道禮本「獻香叩首禮」起首，誦「彌勒救苦真經」或壇前愿文，已入道者可於默禱中持「五字真言」。
    officiant: none
    primary_language: classical-chinese
  - wish_type: wealth
    hint: 無專門求財法；可用一貫道禮本「獻香叩首禮」與愿文，祈願正業、清口、立德，不作偏財咒。
    officiant: none
    primary_language: classical-chinese
  - wish_type: protection
    hint: 已入道者依三寶中「五字真言」默持，並配合一貫道禮本「獻香叩首禮」；未入道者不作三寶持誦。
    officiant: none
    primary_language: classical-chinese
  - wish_type: deceased
    hint: 以一貫道「超拔拔薦禮」或壇辦拔薦功德為主，須由點傳師或授權壇務依佛規辦理。
    officiant: yiguandao-dianchuanshi
    primary_language: classical-chinese
  - wish_type: relationship
    hint: 無專門和合法；可用一貫道禮本「獻香叩首禮」與懺悔愿文，祈求化冤解結、各守倫常。
    officiant: none
    primary_language: classical-chinese
  - wish_type: wisdom
    hint: 以一貫道禮本「獻香叩首禮」起首，誦「彌勒救苦真經」或「皇母訓子十誡」相關訓文，祈求明理修辦。
    officiant: none
    primary_language: classical-chinese
  - wish_type: breaking
    hint: 無專門解咒破法；以一貫道禮本「獻香叩首禮」、懺悔愿文及已入道者默持「五字真言」作正念歸依，不作攻擊性破法。
    officiant: none
    primary_language: classical-chinese
  - wish_type: event
    hint: 以一貫道禮本「獻香叩首禮」與壇前愿文為主，事件名稱置於祈愿句；已入道者可於默禱中持「五字真言」。
    officiant: none
    primary_language: classical-chinese
verification:
  - Jordan, David K. and Daniel L. Overmyer. The Flying Phoenix: Aspects of Chinese Sectarianism in Taiwan. Princeton University Press, 1986, chapters on Yiguan Dao initiation and altar practice.
  - Lu, Yunfeng. The Transformation of Yiguan Dao in Taiwan: Adapting to a Changing Religious Economy. Lexington Books, 2008, chapters 2-4.
  - Clart, Philip. “The Phoenix and the Mother: The Interaction of Spirit Writing Cults and Popular Sects in Taiwan.” Journal of Chinese Religions 25, 1997.
  - Billioud, Sébastien. “The Sage and the People: The Confucian Revival in China.” Oxford University Press, 2015, sections on Yiguandao.
  - https://wrldrels.org/2016/10/08/yiguandao/
  - https://en.wikipedia.org/wiki/Yiguandao
---

# 一貫道

## 结构
[整肅壇前] → [獻香叩首] → [請壇稱聖號] → [表明弟子與愿心] → [正行：愿文／經文／五字真言] → [具體祈愿] → [懺悔守愿] → [回向] → [叩首禮成]

## 通用骨架（占位符版本）
```
明明上帝
無量清虛
至尊至聖
三界十方萬靈真宰

弟子 {{anchors.devotee_name}}，叩首稟告。
弟子願守佛規禮節，願改過遷善，願行功立德，願不忘根本。

南無彌勒祖師。

弟子為 {{anchors.wish_subject}}，因 {{anchors.wish_cause}}，今在壇前虔誠叩求。
願 {{anchors.wish_subject}} 業障消除，冤欠和解，身心安定，道心堅固，所行合乎天理良心。

彌勒救苦真經。
佛說彌勒救苦真經。
彌勒下世不非輕，領寶齊魯靈山地。
拈花印證考三乘，落在中原三星地。
大證四川王桃心，天真收圓掛聖號。
等待時至點神兵，雲雷震開戊己土。
天下神鬼不安寧，親在仁天中華母。
九蓮聖教歸上乘，天花老母垂玉線。
收圓顯化在古東，南北兩極連宗緒。
混元古冊在中央，老母降下通天竅。
無影山前對合同，嬰兒要想歸家去。
持念當來彌勒經，用心持念佛來救。
朵朵金蓮去超生，認識西來白陽子。
鄉兒點鐵化成金，每日志心常持念。
三災八難不來侵，要想成佛勤禮拜。
常持聰明智慧心，休聽邪人胡說話。
牢拴意馬念無生，老母降下真天咒。
用心持念有神通，滿天星斗都下世。
五方列仙下天宮，各方城隍來對號。
報事靈童察得清，三官大帝慈悲註。
赦罪天曹救眾生，救苦天尊來救世。
親點文部揭諦神，八大金剛來護法。
四位菩薩救眾生，緊領三十六員將。
五百靈官緊隨跟，扶助彌勒成大道。
保佑鄉兒得安寧，北方真武為將帥。
青臉紅髮顯神通，扯起皂旗遮日月。
頭頂森羅七寶星，威鎮北方為帥首。
肅清諸惡掛甲兵，搭救原人鄉兒女。
火光落地化為塵，四海龍王來助道。
各駕祥雲去騰空，十方天兵護佛駕。
保佑彌勒去成功，紅陽了道歸家去。
轉到三陽彌勒尊，無皇敕令寄下生。
收伏南閻歸正宗，來往造下真言咒。
傳下當來大藏經，嬰兒姹女常持念。
邪神不敢來近身，持念一遍神通大。
持念兩遍得超生，持念三遍神鬼怕。
魍魎邪魔化為塵，修持劫內尋路徑。
念起真言歸佛令，南無天元太保阿彌陀佛。

五字真言：
無太佛彌勒

弟子 {{anchors.devotee_name}} 懺悔往昔身口意過，願以今日所修所誦，回向 {{anchors.dedication_target}}。
願 {{anchors.dedication_target}} 離苦得安，冤親平等，各得其所。
願弟子守愿了愿，行道不退。

叩首。
叩首。
叩首。
```