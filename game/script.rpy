# 遊戲腳本位於此檔案。

# 出征互動故事系統 - 基於一戰德國士兵亞伯特·柯勒的故事
# 結合歷史教育與中英詞彙學習

# ------------- 詞彙表 -----------------
define vocabulary = {
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

# 預設全域變數
default current_display_text = ""
default current_chapter = 1

# Python 處理函數
init python:
    # 文字處理函數
    def set_story_text(text):
        global current_display_text
        current_display_text = text

    def next_chapter():
        renpy.jump("ch2_start")

    def previous_chapter():
        renpy.jump("ch1_start")
# 聲明遊戲角色
define narrator = Character(None, what_color="#ffffff")
define albert = Character("亞伯特", color="#87ceeb")

# 詞彙提示框 - 懸浮版本
screen vocab_tooltip(word):
    if word in vocabulary:
        frame:
            xalign 0.85 yalign 0.5
            padding (20, 15)
            background "#1a1a1aee"

            vbox:
                spacing 5
                text "詞彙解釋" size 14 color "#888888"
                text word size 18 color "#ffcc66" bold True
                text "▼" size 12 color "#888888"
                text vocabulary[word] size 16 color "#87ceeb"
                null height 10

# 故事顯示介面 - 修正點擊邏輯並加入懸浮功能
screen story_main():
    modal True
    use vocab_textbox(current_display_text)

    # 鍵盤行為：左鍵/空白/Enter 前進；右鍵/Esc 無動作
    key "dismiss" action Return()
    key "game_menu" action NullAction()
    # 右上角導航（維持既有行為，不改 label 名）
    hbox:
        xalign 0.95 yalign 0.05
        spacing 10
        textbutton "首頁" action MainMenu() text_size 16
        textbutton "前章" action Function(previous_chapter) text_size 16
        textbutton "下章" action Function(next_chapter) text_size 16



# 主要故事標籤 - 遊戲從這裡開始
label start:
    # 初始化遊戲背景
    scene black with fade
    
    # 遊戲開場提示
    narrator "歡迎來到《出征》— 一個關於戰爭、成長與歷史的互動故事。"
    narrator "點擊地圖上的光點了解歷史背景，點擊文字中的詞彙學習英文。"
    
    # 跳轉到第一章
    jump ch1_start

# 第一章：出征
label ch1_start:
    $ current_chapter = 1
    
    # 場景1：火車上
    scene bg room with fade
    # TODO: 請將 ch1_train.jpg 放入 images/ 資料夾，描述：1916年德國蒸汽火車車廂內景
    $ set_story_text("德國，1916年春末。亞伯特·柯勒坐在蒸汽火車的木製長椅上，窗外是逐漸遠去的巴伐利亞山丘。綠意在鐵軌的顛簸中模糊成了抹茶色的霧，他的指尖緊握著軍帽，那是他昨天從徵兵辦公室領到的，一頂過大的灰綠色制帽，還有發霉的味道。")
    call screen story_main
    
    # 場景2：回想報名  
    scene bg room with fade
    $ set_story_text("他才十七歲，實際上連這頂帽子都戴不穩。但當他在報名時昂首挺胸，說出十八歲時，那名官員連眉毛都沒抬一下，只問了一句：「你還能跑嗎？」")
    call screen story_main
    
    # 場景3：家庭回憶
    scene bg room with fade 
    $ set_story_text("亞伯特能跑。他能跑，能打靶，能提起家裡的麵粉袋，更重要的是，他能逃。逃離那個被沉默壓得快要崩潰的家，自從哥哥在馬恩河戰役中陣亡後，父親就像牆上褪色的軍功勳章一樣，失去了光澤。母親日日點著蠟燭祈禱，眼神裡沒有未來，只有等待。")
    call screen story_main
    
    # 場景3.5：亞伯特的決心
    $ set_story_text("亞伯特不想等。他要去前線，去證明他不是次等的柯勒，不是那個在家裡背影永遠比哥哥小一號的弟弟。他要成為男人，在戰場上掙來屬於自己的名字。")
    call screen story_main
    
    # 場景3.6：火車上對話
    $ set_story_text("「索姆河。」旁邊的新兵低聲說，像是在咀嚼一個陌生的地名，「聽說那裡，泥濘能把人吸進去，像沼澤一樣。」")
    call screen story_main
    
    $ set_story_text("亞伯特沒答話。他從背包裡抽出哥哥留下的筆記本，裡頭只有幾頁潦草的筆跡，從他嘴裡默默地唸出「戰場很吵，但真正的恐懼是安靜的時候。你會聽見自己的心跳，還有死人的呼吸。」")
    call screen story_main
    
    # 場景4：抵達前線
    scene bg room with fade
    $ set_story_text("火車終於到了前線集結地。下車時，風裡混著焦油與汗水的味道。一位中尉大聲點名，命令一批新兵跟著他走進帳篷登記。亞伯特走進帳篷時，腳踩在濕軟的泥地裡，發出窸窣聲，像是腐爛的蘋果被擠壓。")
    call screen story_main
    
    $ set_story_text("營地裡沒有想像中的激昂軍歌，也沒有榮耀的旗幟。只有一排排低矮的帳篷、一臉疲憊的老兵、還有空中盤旋不去的寒鴉，彷彿在替這片土地做記錄。")
    call screen story_main
    
    $ set_story_text("「亞伯特·柯勒，二等兵。」他對一名登記軍官報上名字。那人頭也不抬地寫下，然後給了他一個破舊的鋼盔和一雙沾血的靴子。「這雙還能穿。」軍官說。")
    call screen story_main
    
    $ set_story_text("亞伯特想起哥哥在家中留下的最後一句話：「別讓別人的腳印決定你的人生。」現在，他正穿上不屬於他的靴子，走進一條不知盡頭的路。")
    call screen story_main
    
    # 場景5：第一夜
    scene bg room with fade
    $ set_story_text("當夜，他被分派到第72步兵團，一支剛從前線撤下補給的部隊。士兵們大多不說話，只是在吃罐頭肉時偶爾咒罵天氣和指揮官。亞伯特躺在潮濕的鋪草上，聽著外面零星的槍聲與遠方大砲的回音。")
    call screen story_main
    
    $ set_story_text("這聲音很遠，卻像是從心裡傳來。他不再是亞伯特·柯勒，學生，弟弟，村裡的郵差小幫手。他現在是士兵，是一枚將被投入火焰的彈殼，是一塊還沒被填入戰壕的泥土。")
    call screen story_main
    
    $ set_story_text("當夜幕低垂，寒鴉落在營地的旗杆上，啼聲似哭。亞伯特第一次夢見哥哥，夢中他穿著濕透的軍服，站在燃燒的樹林中，回頭望著亞伯特，眼神既陌生又哀傷。")
    call screen story_main
    
    albert "「你還想來？」"
    narrator "亞伯特沒有回答。"
    
    # 第一章結束，提供選項
    scene black with fade
    menu:
        "繼續閱讀第二章":
            jump ch2_start
        "重新閱讀第一章":
            jump ch1_start
        "回到 Ren'Py 主選單":
            $ renpy.full_restart()

# 第二章：前線
label ch2_start:
    $ current_chapter = 2
    
    # 場景1：初入戰壕
    scene bg room with fade
    $ set_story_text("當亞伯特第一次踩進戰壕的時候，他的鞋陷進了泥水裡，像是踩進了什麼腐爛的內臟。戰壕蜿蜒如地底的蛇，每個拐角都像一張等待吞人的嘴。天空是鉛灰色的，低得像要壓碎人類的希望。")
    call screen story_main
    
    $ set_story_text("索姆河戰線沒有真正的白天，也沒有乾燥的土地。每一寸泥巴都混著鮮血與汗水，刺鼻的氣味藏不住腐屍的真相。")
    call screen story_main
    
    # 場景2：巡邏任務
    scene bg room with fade
    $ set_story_text("亞伯特被編入前哨排，負責夜間巡邏與補給運送。他背著沉重的彈藥箱，跟著排長穿過連綿的壕溝與交叉通道。每走幾步，他就得跨過一具半埋的屍體，有的是德軍士兵，有的穿著英軍制服，眼睛睜著，像還沒來得及入睡。")
    call screen story_main
    
    narrator "「不要看他們的臉。」排長低聲說，「你越看，就越會記得他們在夢裡找你。」"
    
    $ set_story_text("亞伯特點了點頭，卻仍然回頭多看了一眼——那是一位少年，年紀不比他大，臉上還有鬍鬚未長的稚氣。他的嘴唇微張，像是剛喊了一句「媽」就被子彈打穿了喉嚨。")
    call screen story_main
    
    $ set_story_text("那一晚，前線傳來英軍的突襲警報。整個戰壕像被灌入熱氣，士兵奔跑、砲彈落下、指揮官吼叫，聲音混成一團。他們不是在打仗，而是在暴風中求活。")
    call screen story_main
    
    # 場景3：第一次殺人
    scene bg room with fade
    $ set_story_text("亞伯特第一次開槍是在午夜。他根本沒看清楚那個目標，只見一道黑影從對面戰壕翻過來，他扣動扳機時，整隻手都在發抖。")
    call screen story_main
    
    narrator "「擊中了。」旁邊的士兵說，「幹得好，新兵。」"
    
    $ set_story_text("但亞伯特沒有感覺。他只記得那個影子倒下的瞬間，身體像樹幹一樣僵直，然後就沉入泥巴中。他不知道那是不是一個敵人，甚至不知道那是不是人。他只知道，他殺了第一次。")
    call screen story_main
    
    $ set_story_text("夜半時，砲火暫歇。亞伯特坐在戰壕一角，手裡還握著步槍，槍管熱得像火。他的胸口像塞了石塊，每一次呼吸都困難。他從口袋裡抽出筆記本，寫下第一句話：")
    call screen story_main
    
    albert "「我今天看見一個人死了，是我讓他死的。」"
    
    # 場景4：軍醫與現實
    scene bg room with fade
    $ set_story_text("不久後，一名軍醫拖著一具重傷士兵回來，血從擔架上滴在戰壕裡，與雨水混成一道紅色小河。那人喊著什麼，說的是法語，沒有人聽得懂。")
    call screen story_main
    
    narrator "「該死的。」軍醫喃喃說，「他們也只是孩子。」"
    
    $ set_story_text("那天晚上，亞伯特在鋼盔裡嘔吐。他想起母親在火車站遞給他的麵包與吻，想起哥哥說過的「戰場是男人的洗禮」。他現在知道，那不是洗禮，是葬禮。")
    call screen story_main
    
    # 第二章結束
    scene black with fade
    menu:
        "重新閱讀第二章":
            jump ch2_start
        "回到第一章":
            jump ch1_start
        "結束遊戲":
            jump ending

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
