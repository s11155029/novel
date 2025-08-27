# game/screens.rpy
screen say(who, what):
    style_prefix "say"
    
    window:
        id "window"
        
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        
        text what id "what"
    
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing
        
        if main_menu:
            textbutton _("開始遊戲") action Start()
            textbutton _("章節選擇") action ShowMenu("chapter_select")
        else:
            textbutton _("歷史") action ShowMenu("history")
            textbutton _("儲存") action ShowMenu("save")
        
        textbutton _("讀取") action ShowMenu("load")
        textbutton _("設定") action ShowMenu("preferences")
        
        if not main_menu:
            textbutton _("返回標題") action MainMenu()
        
        textbutton _("關於") action ShowMenu("about")
        
        if renpy.variant("pc"):
            textbutton _("離開") action Quit(confirm=not main_menu)

screen main_menu():
    tag menu
    add gui.main_menu_background
    
    frame:
        style "main_menu_frame"
    
    use navigation
    
    if gui.show_name:
        vbox:
            style "main_menu_vbox"
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"

screen chapter_select():
    tag menu
    add gui.game_menu_background
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 50)
        
        vbox:
            spacing 30
            xalign 0.5
            
            text "章節選擇" size 40 xalign 0.5
            
            null height 20
            
            textbutton "第一章：出征" action [Hide("chapter_select"), Jump("ch1_start")]
            textbutton "第二章：前線" action [Hide("chapter_select"), Jump("ch2_start")]
            
            null height 40
            
            textbutton "返回主選單" action Return()

screen vocab_tooltip(word_data):
    if word_data:
        frame:
            style "vocab_tooltip_frame"
            at_list [vocab_tooltip_appear]
            xpos renpy.get_mouse_pos()[0] + 20
            ypos renpy.get_mouse_pos()[1] - 50
            
            vbox:
                spacing 8
                text word_data["chinese"] style "vocab_chinese"
                text "▼" size 12 color "#888888" xalign 0.5
                text word_data["english"] style "vocab_english"

transform vocab_tooltip_appear:
    alpha 0.0
    linear 0.2 alpha 1.0

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_title:
    size gui.title_text_size

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")