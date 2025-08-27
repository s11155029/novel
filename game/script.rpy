# game/script.rpy
# Chapter data structure
define chapter_data = {
    "ch1": {
        "title": "第一章：出征",
        "segments": [
            {
                "bg": "bg train",  # Chapter 1 background
                "who": None,
                "text": "德國，1916年春末。亞伯特·柯勒坐在蒸汽火車的木製長椅上，窗外是逐漸遠去的巴伐利亞山丘。"
            },
            {
                "bg": None,
                "who": None,
                "text": "綠意在鐵軌的顛簸中模糊成了抹茶色的霧，他的指尖緊握著軍帽，那是他昨天從徵兵辦公室領到的。"
            },
            {
                "bg": "bg office",  # Chapter 1 background
                "who": None,
                "text": "他才十七歲，實際上連這頂帽子都戴不穩。但當他在報名時昂首挺胸，說出十八歲時，那名官員連眉毛都沒抬一下。"
            },
            {
                "bg": "bg home",  # Chapter 1 background
                "who": None,
                "text": "亞伯特能跑。他能跑，能打靶，能提起家裡的麵粉袋，更重要的是，他能逃。"
            },
            {
                "bg": None,
                "who": None,
                "text": "逃離那個被沉默壓得快要崩潰的家，自從哥哥在馬恩河戰役中陣亡後，父親就像牆上褪色的軍功勳章一樣，失去了光澤。"
            },
            {
                "bg": None,
                "who": None,
                "text": "母親日日點著蠟燭祈禱，眼神裡沒有未來，只有等待。"
            },
            {
                "bg": "bg train",  # Chapter 1 background
                "who": "新兵",
                "text": "索姆河。聽說那裡，泥濘能把人吸進去，像沼澤一樣。"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特沒答話。他從背包裡抽出哥哥留下的筆記本，裡頭只有幾頁潦草的筆跡。"
            },
            {
                "bg": None,
                "who": None,
                "text": "戰場很吵，但真正的恐懼是安靜的時候。你會聽見自己的心跳，還有死人的呼吸。"
            },
            {
                "bg": "bg camp",  # Chapter 1 background
                "who": None,
                "text": "火車終於到了前線集結地。下車時，風裡混著焦油與汗水的味道。"
            },
            {
                "bg": None,
                "who": "中尉",
                "text": "所有新兵，跟我來登記！"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特走進帳篷時，腳踩在濕軟的泥地裡，發出窸窣聲，像是腐爛的蘋果被擠壓。"
            },
            {
                "bg": None,
                "who": "亞伯特",
                "text": "亞伯特·柯勒，二等兵。"
            },
            {
                "bg": None,
                "who": "軍官",
                "text": "這雙靴子還能穿。"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特想起哥哥在家中留下的最後一句話：別讓別人的腳印決定你的人生。現在，他正穿上不屬於他的靴子，走進一條不知盡頭的路。"
            },
            {
                "bg": "bg night",  # Chapter 1 background
                "who": None,
                "text": "當夜，他被分派到第72步兵團。士兵們大多不說話，只是在吃罐頭肉時偶爾咒罵天氣和指揮官。"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特躺在潮濕的鋪草上，聽著外面零星的槍聲與遠方大砲的回音。"
            },
            {
                "bg": None,
                "who": None,
                "text": "他不再是亞伯特·柯勒，學生，弟弟，村裡的郵差小幫手。他現在是士兵，是一枚將被投入火焰的彈殼。"
            },
            {
                "bg": None,
                "who": None,
                "text": "當夜幕低垂，寒鴉落在營地的旗杆上，啼聲似哭。亞伯特第一次夢見哥哥。"
            },
            {
                "bg": None,
                "who": "哥哥",
                "text": "你還想來？"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特沒有回答。"
            }
        ]
    },
    "ch2": {
        "title": "第二章：前線",
        "segments": [
            {
                "bg": "bg trench",  # Chapter 2 background
                "who": None,
                "text": "當亞伯特第一次踩進戰壕的時候，他的鞋陷進了泥水裡，像是踩進了什麼腐爛的內臟。"
            },
            {
                "bg": None,
                "who": None,
                "text": "戰壕蜿蜒如地底的蛇，每個拐角都像一張等待吞人的嘴。天空是鉛灰色的，低得像要壓碎人類的希望。"
            },
            {
                "bg": None,
                "who": None,
                "text": "索姆河戰線沒有真正的白天，也沒有乾燥的土地。每一寸泥巴都混著鮮血與汗水。"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特被編入前哨排，負責夜間巡邏與補給運送。他背著沉重的彈藥箱，跟著排長穿過連綿的壕溝。"
            },
            {
                "bg": None,
                "who": None,
                "text": "每走幾步，他就得跨過一具半埋的屍體，有的是德軍士兵，有的穿著英軍制服。"
            },
            {
                "bg": None,
                "who": "排長",
                "text": "不要看他們的臉。你越看，就越會記得他們在夢裡找你。"
            },
            {
                "bg": None,
                "who": None,
                "text": "亞伯特點了點頭，卻仍然回頭多看了一眼——那是一位少年，臉上還有稚氣。"
            },
            {
                "bg": None,
                "who": None,
                "text": "那一晚，前線傳來英軍的突襲警報。整個戰壕像被灌入熱氣，士兵奔跑、砲彈落下、指揮官吼叫。"
            },
            {
                "bg": "bg night_battle",  # Chapter 2 background
                "who": None,
                "text": "亞伯特第一次開槍是在午夜。他根本沒看清楚那個目標，只見一道黑影從對面戰壕翻過來。"
            },
            {
                "bg": None,
                "who": "士兵",
                "text": "擊中了。幹得好，新兵。"
            },
            {
                "bg": None,
                "who": None,
                "text": "但亞伯特沒有感覺。他只記得那個影子倒下的瞬間，身體像樹幹一樣僵直，然後就沉入泥巴中。"
            },
            {
                "bg": None,
                "who": None,
                "text": "他不知道那是不是一個敵人，甚至不知道那是不是人。他只知道，他殺了第一次。"
            },
            {
                "bg": None,
                "who": None,
                "text": "夜半時，砲火暫歇。亞伯特坐在戰壕一角，手裡還握著步槍，槍管熱得像火。"
            },
            {
                "bg": None,
                "who": "亞伯特",
                "text": "我今天看見一個人死了，是我讓他死的。"
            },
            {
                "bg": None,
                "who": None,
                "text": "不久後，一名軍醫拖著一具重傷士兵回來，血從擔架上滴在戰壕裡。"
            },
            {
                "bg": None,
                "who": "軍醫",
                "text": "該死的。他們也只是孩子。"
            },
            {
                "bg": None,
                "who": None,
                "text": "那天晚上，亞伯特在鋼盔裡嘔吐。他想起母親在火車站遞給他的麵包與吻。"
            },
            {
                "bg": None,
                "who": None,
                "text": "他想起哥哥說過的「戰場是男人的洗禮」。他現在知道，那不是洗禮，是葬禮。"
            }
        ]
    }
}

label start:
    scene black with fade
    "歡迎來到《出征》— 一個關於戰爭、成長與歷史的互動故事。"
    "點擊文字中標記的詞彙，可以學習英文。"
    jump ch1_start

label ch1_start:
    $ current_chapter = "ch1"
    call play_chapter("ch1")
    menu:
        "繼續閱讀第二章":
            jump ch2_start
        "重新閱讀第一章":
            jump ch1_start
        "回到主選單":
            return

label ch2_start:
    $ current_chapter = "ch2"
    call play_chapter("ch2")
    menu:
        "重新閱讀第二章":
            jump ch2_start
        "回到第一章":
            jump ch1_start
        "回到主選單":
            return

label play_chapter(ch_id):
    $ chapter = chapter_data[ch_id]
    $ renpy.dynamic("segment")
    
    scene black with fade
    "[chapter[title]]"
    
    $ segment_count = 0
    python:
        for segment in chapter["segments"]:
            segment_count += 1
            
            # Set background if specified
            if segment.get("bg"):
                renpy.scene()
                try:
                    renpy.show(segment["bg"])
                except:
                    # If background image not found, use black
                    renpy.scene()
            
            # Display text
            if segment.get("who"):
                renpy.say(segment["who"], vocab_system.process_text(segment["text"]))
            else:
                renpy.say(None, vocab_system.process_text(segment["text"]))
    
    return