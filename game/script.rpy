# 遊戲腳本位於此檔案。

# 出征互動故事系統 - 基於一戰德國士兵亞伯特·柯勒的故事
# 結合歷史教育與中英詞彙學習

init python:
    # 詞彙表字典（中文→英文）
    vocabulary = {
        "蒸汽火車": "steam train",
        "長椅": "bench", 
        "軍帽": "military cap",
        "報名": "sign up",
        "麵粉": "flour",
        "指揮官": "commander",
        "郵差": "postman",
        "火焰": "flame",
        "戰場": "battlefield",
        "咀嚼": "chew",
        "安靜": "silence",
        "焦油": "tar",
        "中尉": "lieutenant",
        "泥地": "mud",
        "登記": "register",
        "鋼盔": "helmet",
        "靴子": "boot"
    }
    
    # 歷史光點資料
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

# 聲明遊戲角色
define narrator = Character(None, what_color="#ffffff")
define albert = Character("亞伯特", color="#87ceeb")

# 主要故事標籤 - 遊戲從這裡開始
label start:
    # 初始化遊戲背景
    scene bg_german_countryside with fade
    
    # 遊戲開場提示
    narrator "歡迎來到《出征》— 一個關於戰爭、成長與歷史的互動故事。"
    narrator "點擊地圖上的光點了解歷史背景，點擊文字中的詞彙學習英文。"
    
    # 顯示互動介面
    call screen story_interface

# 故事介面螢幕
screen story_interface():
    # 背景圖片區域（1916年德國鄉村/前線地圖）
    add "images/bg_warmap.jpg" xpos 0 ypos 0
    
    # 歷史光點按鈕（地圖上的戰役位置）
    imagebutton:
        xpos 180 ypos 120  # 凡爾登位置
        idle "gui/point_idle.png"
        hover "gui/point_hover.png" 
        action Show("historical_tooltip", point_id="verdun")
        
    imagebutton:
        xpos 220 ypos 80   # 日德蘭海域
        idle "gui/point_idle.png"
        hover "gui/point_hover.png"
        action Show("historical_tooltip", point_id="jutland")
        
    imagebutton:
        xpos 160 ypos 140  # 索姆河
        idle "gui/point_idle.png" 
        hover "gui/point_hover.png"
        action Show("historical_tooltip", point_id="somme")
        
    imagebutton:
        xpos 200 ypos 160  # 馬恩河
        idle "gui/point_idle.png"
        hover "gui/point_hover.png"
        action Show("historical_tooltip", point_id="marne")
    
    # 右上角導航按鈕
    hbox:
        xalign 0.95 yalign 0.05
        spacing 10
        textbutton "首頁" action Jump("main_menu") text_size 16
        textbutton "前章" action Jump("previous_chapter") text_size 16
        textbutton "下章" action Jump("next_chapter") text_size 16
    
    # 右下角故事文字區域
    frame:
        xalign 0.98 yalign 0.98
        xsize 450 ysize 350
        background "#000000cc"
        
        viewport:
            scrollbars "vertical"
            vbox:
                spacing 8
                text "德國，1916年春末。亞伯特·柯勒坐在{color=#ffcc66}{a=show_vocab:蒸汽火車}蒸汽火車{/a}{/color}的木製{color=#ffcc66}{a=show_vocab:長椅}長椅{/a}{/color}上，窗外巴伐利亞山丘正徐徐遠去。" size 16 color "#ffffff"
                
                text "鐵軌的顛簸把綠意攪成抹茶色薄霧，他緊握昨日上午在徵兵辦公室領到的灰綠色{color=#ffcc66}{a=show_vocab:軍帽}軍帽{/a}{/color}——尺寸過大，還帶霉味。" size 16 color "#ffffff"
                
                text "他只有十七歲，帽子戴得並不穩；但{color=#ffcc66}{a=show_vocab:報名}報名{/a}{/color}時，他挺胸謊報「十八歲」，那位官員連眉毛都未抬，只丟下一句：「你還能跑嗎？」" size 16 color "#ffffff"
                
                text "亞伯特能跑、能打靶，也能扛起家裡的{color=#ffcc66}{a=show_vocab:麵粉}麵粉{/a}{/color}袋。更重要的是，他想逃——逃離那個自從哥哥戰死於馬恩河後便被沉默壓得崩潰的家。" size 16 color "#ffffff"
                
                text "「索姆河。」旁邊的新兵低聲{color=#ffcc66}{a=show_vocab:咀嚼}咀嚼{/a}{/color}那陌生地名，「聽說那裡泥濘得像沼澤，可以把人整個吞掉。」" size 16 color "#ffffff"

# 歷史光點提示視窗
screen historical_tooltip(point_id):
    modal True
    
    frame:
        xalign 0.5 yalign 0.5
        padding (25, 20)
        background "#1a1a1a"
        
        vbox:
            text historical_points[point_id]["title"] size 22 bold True color "#ffcc66"
            null height 15
            text historical_points[point_id]["description"] size 16 color "#ffffff" text_align 0.0
            null height 20
            textbutton "關閉" action Hide("historical_tooltip") text_size 16

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
    narrator "返回主選單功能開發中..."
    call screen story_interface

label previous_chapter:
    narrator "前一章節功能開發中..."
    call screen story_interface
    
label next_chapter:
    narrator "下一章節功能開發中..."
    call screen story_interface

# 遊戲結束點
label ending:
    narrator "感謝體驗《出征》互動故事！"
    return