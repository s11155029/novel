init python:
    import re
    
    # Vocabulary database
    vocabulary_db = {
        "蒸汽火車": {"english": "steam train", "pinyin": "zhēngqì huǒchē"},
        "長椅": {"english": "bench", "pinyin": "cháng yǐ"},
        "軍帽": {"english": "military cap", "pinyin": "jūn mào"},
        "報名": {"english": "sign up", "pinyin": "bàomíng"},
        "麵粉": {"english": "flour", "pinyin": "miànfěn"},
        "蠟燭": {"english": "candle", "pinyin": "làzhú"},
        "未來": {"english": "future", "pinyin": "wèilái"},
        "戰場": {"english": "battlefield", "pinyin": "zhànchǎng"},
        "咀嚼": {"english": "chew", "pinyin": "jǔjué"},
        "筆跡": {"english": "handwriting", "pinyin": "bǐjì"},
        "安靜": {"english": "silence", "pinyin": "ānjìng"},
        "焦油": {"english": "tar", "pinyin": "jiāoyóu"},
        "中尉": {"english": "lieutenant", "pinyin": "zhōngwèi"},
        "泥地": {"english": "mud", "pinyin": "nídì"},
        "登記": {"english": "register", "pinyin": "dēngjì"},
        "鋼盔": {"english": "helmet", "pinyin": "gāngkuī"},
        "靴子": {"english": "boot", "pinyin": "xuēzi"},
        "指揮官": {"english": "commander", "pinyin": "zhǐhuīguān"},
        "郵差": {"english": "postman", "pinyin": "yóuchāi"},
        "火焰": {"english": "flame", "pinyin": "huǒyàn"},
        "戰壕": {"english": "trench", "pinyin": "zhànháo"},
        "內臟": {"english": "guts", "pinyin": "nèizàng"},
        "壓碎": {"english": "crush", "pinyin": "yāsuì"},
        "彈藥箱": {"english": "ammunition box", "pinyin": "dànyào xiāng"},
        "屍體": {"english": "dead body", "pinyin": "shītǐ"},
        "稚氣": {"english": "naivety", "pinyin": "zhìqì"},
        "子彈": {"english": "bullet", "pinyin": "zǐdàn"},
        "突襲": {"english": "assault", "pinyin": "tūxí"},
        "午夜": {"english": "midnight", "pinyin": "wǔyè"},
        "目標": {"english": "target", "pinyin": "mùbiāo"},
        "敵人": {"english": "enemy", "pinyin": "dírén"},
        "步槍": {"english": "rifle", "pinyin": "bùqiāng"},
        "軍醫": {"english": "combat medic", "pinyin": "jūnyī"},
        "葬禮": {"english": "funeral", "pinyin": "zànglǐ"}
    }
    
    class VocabHighlight:
        def __init__(self):
            self.current_hover = None
        
        def process_text(self, text):
            """Process text and add highlighting tags for vocabulary words"""
            result = text
            for word in vocabulary_db:
                if word in result:
                    # Use a custom tag for highlighting
                    result = result.replace(word, "{vocab=" + word + "}" + word + "{/vocab}")
            return result
        
        def get_word_data(self, word):
            """Get vocabulary data for a word"""
            if word in vocabulary_db:
                data = vocabulary_db[word].copy()
                data["chinese"] = word
                return data
            return None
    
    vocab_system = VocabHighlight()
    
    def vocab_tag(tag, argument, contents):
        """Custom text tag for vocabulary highlighting"""
        return [
            (renpy.TEXT_TAG, "a=call:vocab_hover_handler," + argument),
            (renpy.TEXT_TAG, "color=#ffcc66"),
            (renpy.TEXT_TAG, "u"),
        ] + contents + [
            (renpy.TEXT_TAG, "/u"),
            (renpy.TEXT_TAG, "/color"),
            (renpy.TEXT_TAG, "/a"),
        ]
    
    config.custom_text_tags["vocab"] = vocab_tag
    
    def vocab_hover_handler(word):
        """Handle hover events for vocabulary words"""
        store.current_vocab_hover = vocab_system.get_word_data(word)
        renpy.restart_interaction()

default current_vocab_hover = None

screen story_display(text_content):
    window:
        id "story_window"
        xfill True
        yalign 1.0
        ysize gui.textbox_height
        background "#000000cc"
        
        text vocab_system.process_text(text_content):
            id "story_text"
            xpos gui.dialogue_xpos
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width
            color gui.text_color
            size gui.text_size
    
    if current_vocab_hover:
        use vocab_tooltip(current_vocab_hover)
    
    # Navigation hints
    hbox:
        xalign 0.95
        yalign 0.05
        spacing 10
        textbutton "主選單" action MainMenu() text_size 18
        textbutton "章節選擇" action ShowMenu("chapter_select") text_size 18