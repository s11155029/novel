# game/gui.rpy
init offset = -2

init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

# Colors
define gui.accent_color = '#87ceeb'
define gui.idle_color = '#888888'
define gui.idle_small_color = '#606060'
define gui.hover_color = '#ffffff'
define gui.selected_color = '#87ceeb'
define gui.insensitive_color = '#7070707f'
define gui.muted_color = '#666666'
define gui.hover_muted_color = '#999999'
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#404040'

# Fonts and sizes
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"
define gui.text_size = 28
define gui.name_text_size = 32
define gui.interface_text_size = 24
define gui.label_text_size = 28
define gui.notify_text_size = 20
define gui.title_text_size = 50

# Backgrounds
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

# Dialogue
define gui.textbox_height = 240
define gui.textbox_yalign = 1.0
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 50
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

# Highlight word style
style vocab_highlight:
    color "#ffcc66"
    hover_background "#333333aa"
    hover_color "#ffffff"
    underline True

style vocab_tooltip_frame:
    background "#1a1a1aee"
    padding (20, 15)
    xmaximum 400

style vocab_tooltip_text:
    size 18
    color "#ffffff"

style vocab_chinese:
    size 20
    color "#ffcc66"
    bold True

style vocab_english:
    size 18
    color "#87ceeb"
