# 遊戲腳本位於此檔案。

# 出征互動故事系統 - 基於一戰德國士兵亞伯特·柯勒的故事
# 結合歷史教育與中英詞彙學習

init python:
    # 詞彙表字典（中文→英文）- 來源：chapter1 & chapter2 PDF
    vocabulary = {
        "蒸汽火車": "steam train",
        "長椅": "bench", 
        "軍帽": "military cap",
        "報名": "sign up",
        "麵粉": "flour",
        "蠟燭": "candle",
        "未來": "future",
        "戰場": "battlefield",
        "咀嚼": "chew",
        "筆跡": "handwriting",
        "安靜": "silence",
        "焦油": "tar",
        "中尉": "lieutenant",
        "泥地": "mud",
        "登記": "register",
        "鋼盔": "helmet",
        "靴子": "boot",
        "指揮官": "commander",
        "郵差": "postman",
        "火焰": "flame",
        "戰壕": "trench",
        "內臟": "guts",
        "壓碎": "crush",
        "彈藥箱": "ammunition box",
        "屍體": "dead body",
        "稚氣": "naivety",
        "子彈": "bullet",
        "突襲": "assault",
        "午夜": "midnight",
        "目標": "target",
        "敵人": "enemy",
        "步槍": "rifle",
        "軍醫": "combat medic",
        "葬禮": "funeral"
    }
    
    # 場景背景對應表
    scene_backgrounds = {
        "ch1_scene1": "ch1_train.jpg",        # TODO: 1916年德國火車車廂內景
        "ch1_scene2": "ch1_recruitment.jpg",   # TODO: 徵兵辦公室場景
        "ch1_scene3": "ch1_home_memory.jpg",   # TODO: 德國家庭回憶場景
        "ch1_scene4": "ch1_frontline_camp.jpg", # TODO: 前線軍營集結地
        "ch1_scene5": "ch1_night_camp.jpg",    # TODO: 夜晚軍營帳篷區
        "ch2_scene1": "ch2_trench_entrance.jpg", # TODO: 戰壕入口泥濘場景
        "ch2_scene2": "ch2_patrol_duty.jpg",   # TODO: 夜間巡邏戰壕通道
        "ch2_scene3": "ch2_first_kill.jpg",    # TODO: 午夜戰鬥場景
        "ch2_scene4": "ch2_medic_scene.jpg"    # TODO: 軍醫救護場景
    }

    # 歷史光點資料（保留原有功能）
    historical_points = {
        "verdun": {
            "title": "凡爾登會戰 (1916)",
            "description": "第一次世界大戰最長且傷亡慘重的戰役之一，死傷約七十萬人。德法兩軍在此進行長達10個月的血腥消耗戰。"
        },
        "jutland": {
            "title": "日德蘭海戰 (1916.5)",
            "description": "北海德英海軍主力唯一正面交鋒，雙方戰艦激烈對轟，英國海軍損失更重但保持制海權。"
        },
        "somme": {
            "title": "索姆河戰役 (1916.7-11)",
            "description": "英法為減輕凡爾登壓力而發動，亦是坦克首次上戰場。首日英軍傷亡近6萬人，成為史上最血腥一日。"
        },
        "marne": {
            "title": "馬恩河戰役",
            "description": "1914年第一次阻止德軍攻陷巴黎，戰線轉入壕溝僵局；1918年第二次為德軍最後全面進攻，最終失敗。"
        }
    }

    # 自動標記詞彙函數
    def mark_vocabulary(text):
        marked_text = text
        for chinese, english in vocabulary.items():
            if chinese in marked_text:
                marked_text = marked_text.replace(
                    chinese, 
                    "{color=#ffcc66}{a=show_vocab:" + chinese + "}" + chinese + "{/a}{/color}"
                )
        return marked_text

# 聲明遊戲角色
define narrator = Character(None, what_color="#ffffff")
define albert = Character("亞伯特", color="#87ceeb")

# 主要故事標籤 - 遊戲從這裡開始
label start:
    # 遊戲開場提示
    scene black with fade
    narrator "歡迎來到《出征》— 一個關於戰爭、成長與歷史的互動故事。"
    narrator "點擊文字中的高亮詞彙學習英文，體驗1916年一戰德國士兵的真實經歷。"
    
    # 跳轉到第一章
    jump ch1_start

# 第一章：出征
label ch1_start:
    # 場景1：火車上
    scene expression scene_backgrounds["ch1_scene1"] with fade
    # TODO: 需要 ch1_train.jpg - 1916年德國蒸汽火車車廂內景，木製長椅，窗外巴伐利亞山丘
    
    narrator "[mark_vocabulary('德國，1916年春末。亞伯特·柯勒坐在蒸汽火車的木製長椅上，窗外是逐漸遠去的巴伐利亞山丘。綠意在鐵軌的顛簸中模糊成了抹茶色的霧，他的指尖緊握著軍帽，那是他昨天從徵兵辦公室領到的，一頂過大的灰綠色制帽，還有發霉的味道。')]"
    
    # 場景2：回想報名
    scene expression scene_backgrounds["ch1_scene2"] with fade
    # TODO: 需要 ch1_recruitment.jpg - 1916年德國徵兵辦公室，官員與年輕人
    
    narrator "[mark_vocabulary('他才十七歲，實際上連這頂帽子都戴不穩。但當他在報名時昂首挺胸，說出十八歲時，那名官員連眉毛都沒抬一下，只問了一句：「你還能跑嗎？」')]"
    
    # 場景3：家庭回憶
    scene expression scene_backgrounds["ch1_scene3"] with fade  
    # TODO: 需要 ch1_home_memory.jpg - 德國家庭場景，母親點蠟燭祈禱，父親沮喪
    
    narrator "[mark_vocabulary('亞伯特能跑。他能跑，能打靶，能提起家裡的麵粉袋，更重要的是，他能逃。逃離那個被沉默壓得快要崩潰的家，自從哥哥在馬恩河戰役中陣亡後，父親就像牆上褪色的軍功勳章一樣，失去了光澤。母親日日點著蠟燭祈禱，眼神裡沒有未來，只有等待。')]"
    
    narrator "亞伯特不想等。他要去前線，去證明他不是次等的柯勒，不是那個在家裡背影永遠比哥哥小一號的弟弟。"
    
    narrator "[mark_vocabulary('「索姆河。」旁邊的新兵低聲說，像是在咀嚼一個陌生的地名，「聽說那裡，泥濘能把人吸進去，像沼澤一樣。」')]"
    
    narrator "[mark_vocabulary('亞伯特沒答話。他從背包裡抽出哥哥留下的筆記本，裡頭只有幾頁潦草的筆跡，從他嘴裡默默地唸出「戰場很吵，但真正的恐懼是安靜的時候。你會聽見自己的心跳，還有死人的呼吸。」')]"
    
    # 場景4：抵達前線
    scene expression scene_backgrounds["ch1_scene4"] with fade
    # TODO: 需要 ch1_frontline_camp.jpg - 前線軍營，帳篷，疲憊士兵，中尉點名
    
    narrator "[mark_vocabulary('火車終於到了前線集結地。下車時，風裡混著焦油與汗水的味道。一位中尉大聲點名，命令一批新兵跟著他走進帳篷登記。亞伯特走進帳篷時，腳踩在濕軟的泥地裡，發出窸窣聲，像是腐爛的蘋果被擠壓。')]"
    
    narrator "營地裡沒有想像中的激昂軍歌，也沒有榮耀的旗幟。只有一排排低矮的帳篷、一臉疲憊的老兵、還有空中盤旋不去的寒鴉，彷彿在替這片土地做記錄。"
    
    narrator "[mark_vocabulary('「亞伯特·柯勒，二等兵。」他對一名登記軍官報上名字。那人頭也不抬地寫下，然後給了他一個破舊的鋼盔和一雙沾血的靴子。')]"
    
    narrator "「這雙還能穿。」軍官說。"
    
    narrator "亞伯特想起哥哥在家中留下的最後一句話：「別讓別人的腳印決定你的人生。」現在，他正穿上不屬於他的靴子，走進一條不知盡頭的路。"
    
    # 場景5：第一夜
    scene expression scene_backgrounds["ch1_scene5"] with fade
    # TODO: 需要 ch1_night_camp.jpg - 夜晚軍營，士兵吃罐頭，亞伯特躺在草堆上
    
    narrator "[mark_vocabulary('當夜，他被分派到第72步兵團，一支剛從前線撤下補給的部隊。士兵們大多不說話，只是在吃罐頭肉時偶爾咒罵天氣和指揮官。亞伯特躺在潮濕的鋪草上，聽著外面零星的槍聲與遠方大砲的回音。')]"
    
    narrator "[mark_vocabulary('這聲音很遠，卻像是從心裡傳來。他不再是亞伯特·柯勒，學生，弟弟，村裡的郵差小幫手。他現在是士兵，是一枚將被投入火焰的彈殼，是一塊還沒被填入戰壕的泥土。')]"
    
    narrator "當夜幕低垂，寒鴉落在營地的旗杆上，啼聲似哭。亞伯特第一次夢見哥哥，夢中他穿著濕透的軍服，站在燃燒的樹林中，回頭望著亞伯特，眼神既陌生又哀傷。"
    
    albert "「你還想來？」"
    
    narrator "亞伯特沒有回答。"
    
    # 第一章結束，提供選項
    menu:
        "繼續第二章":
            jump ch2_start
        "重看第一章":
            jump ch1_start
        "返回主選單":
            jump main_menu

# 第二章：前線
label ch2_start:
    # 場景1：初入戰壕
    scene expression scene_backgrounds["ch2_scene1"] with fade
    # TODO: 需要 ch2_trench_entrance.jpg - 泥濘戰壕入口，陰暗潮濕，鉛灰天空
    
    narrator "[mark_vocabulary('當亞伯特第一次踩進戰壕的時候，他的鞋陷進了泥水裡，像是踩進了什麼腐爛的內臟。戰壕蜿蜒如地底的蛇，每個拐角都像一張等待吞人的嘴。天空是鉛灰色的，低得像要壓碎人類的希望。')]"
    
    narrator "索姆河戰線沒有真正的白天，也沒有乾燥的土地。每一寸泥巴都混著鮮血與汗水，刺鼻的氣味藏不住腐屍的真相。"
    
    # 場景2：巡邏任務
    scene expression scene_backgrounds["ch2_scene2"] with fade
    # TODO: 需要 ch2_patrol_duty.jpg - 戰壕通道，士兵巡邏，屍體遍地
    
    narrator "[mark_vocabulary('亞伯特被編入前哨排，負責夜間巡邏與補給運送。他背著沉重的彈藥箱，跟著排長穿過連綿的壕溝與交叉通道。每走幾步，他就得跨過一具半埋的屍體，有的是德軍士兵，有的穿著英軍制服，眼睛睜著，像還沒來得及入睡。')]"
    
    narrator "「不要看他們的臉。」排長低聲說，「你越看，就越會記得他們在夢裡找你。」"
    
    narrator "[mark_vocabulary('亞伯特點了點頭，卻仍然回頭多看了一眼——那是一位少年，年紀不比他大，臉上還有鬍鬚未長的稚氣。他的嘴唇微張，像是剛喊了一句「媽」就被子彈打穿了喉嚨。')]"
    
    narrator "[mark_vocabulary('那一晚，前線傳來英軍的突襲警報。整個戰壕像被灌入熱氣，士兵奔跑、砲彈落下、指揮官吼叫，聲音混成一團。他們不是在打仗，而是在暴風中求活。')]"
    
    # 場景3：第一次殺人
    scene expression scene_backgrounds["ch2_scene3"] with fade
    # TODO: 需要 ch2_first_kill.jpg - 午夜戰鬥場景，槍火閃光，士兵剪影
    
    narrator "[mark_vocabulary('亞伯特第一次開槍是在午夜。他根本沒看清楚那個目標，只見一道黑影從對面戰壕翻過來，他扣動扳機時，整隻手都在發抖。')]"
    
    narrator "「擊中了。」旁邊的士兵說，「幹得好，新兵。」"
    
    narrator "[mark_vocabulary('但亞伯特沒有感覺。他只記得那個影子倒下的瞬間，身體像樹幹一樣僵直，然後就沉入泥巴中。他不知道那是不是一個敵人，甚至不知道那是不是人。他只知道，他殺了第一次。')]"
    
    narrator "[mark_vocabulary('夜半時，砲火暫歇。亞伯特坐在戰壕一角，手裡還握著步槍，槍管熱得像火。他的胸口像塞了石塊，每一次呼吸都困難。他從口袋裡抽出筆記本，寫下第一句話：')]"
    
    albert "「我今天看見一個人死了，是我讓他死的。」"
    
    # 場景4：軍醫與現實
    scene expression scene_backgrounds["ch2_scene4"] with fade
    # TODO: 需要 ch2_medic_scene.jpg - 軍醫背著傷患，血流成河，戰壕醫療場景
    
    narrator "[mark_vocabulary('不久後，一名軍醫拖著一具重傷士兵回來，血從擔架上滴在戰壕裡，與雨水混成一道紅色小河。那人喊著什麼，說的是法語，沒有人聽得懂。')]"
    
    narrator "「該死的。」軍醫喃喃說，「他們也只是孩子。」"
    
    narrator "[mark_vocabulary('那天晚上，亞伯特在鋼盔裡嘔吐。他想起母親在火車站遞給他的麵包與吻，想起哥哥說過的「戰場是男人的洗禮」。他現在知道，那不是洗禮，是葬禮。')]"
    
    # 第二章結束
    menu:
        "重看第二章":
            jump ch2_start
        "回到第一章":
            jump ch1_start
        "結束遊戲":
            jump ending

# 詞彙解釋處理
label show_vocab(word):
    if word in vocabulary:
        $ quick_menu = False
        show screen vocab_popup(word)
        $ ui.interact()
        hide screen vocab_popup
        $ quick_menu = True
    return

# 詞彙彈出視窗
screen vocab_popup(word):
    modal True
    
    frame:
        xalign 0.5 yalign 0.5
        padding (20, 15)
        background "#2d2d2d"
        
        vbox:
            text word size 18 bold True color "#ffcc66"
            null height 8
            text vocabulary[word] size 16 color "#87ceeb" italic True
            null height 15
            textbutton "關閉" action Return() text_size 14

# 佔位標籤與結束邏輯
label main_menu:
    scene black with fade
    narrator "返回主選單功能開發中..."
    menu:
        "開始遊戲":
            jump start
        "結束":
            return

label ending:
    scene black with fade
    narrator "《出征》第一、二章體驗結束。"
    narrator "戰爭不會讓男孩成為英雄，只會讓他們成為倖存者。"
    narrator "感謝您的體驗。"
    return