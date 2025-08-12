# game/ui_vocab.rpy
# 將一句文字拆成「一般片段」與「詞彙片段」，詞彙片段以 textbutton 呈現，hover/點擊顯示 tooltip。
# 不依賴 config.hyperlink_focus/leave，穩定支援 Ren'Py 8.x。

init python:
    # 取得詞彙鍵值，若尚未定義 vocabulary 也不會炸
    try:
        _VOCAB_KEYS = list(vocabulary.keys())
        # 長詞優先，避免「戰壕」被「戰」先吃掉
        _VOCAB_KEYS.sort(key=len, reverse=True)
    except Exception:
        _VOCAB_KEYS = []

    def _split_line_by_vocab(line):
        """
        將單行字串拆成 segments：
        segment = {"text": <文字>, "is_vocab": True/False}
        用最左優先、同起點取最長詞的策略，避免重疊與亂序。
        """
        if not line:
            return [{"text": "", "is_vocab": False}]

        segments = []
        i = 0
        n = len(line)

        while i < n:
            earliest_pos = None
            chosen_word = None

            # 找從 i 起最早出現的詞，若有多個同位置，取最長
            for w in _VOCAB_KEYS:
                pos = line.find(w, i)
                if pos == -1:
                    continue
                if (earliest_pos is None) or (pos < earliest_pos) or (pos == earliest_pos and len(w) > len(chosen_word or "")):
                    earliest_pos = pos
                    chosen_word = w

            if earliest_pos is None:
                # 後面都是一般文字
                segments.append({"text": line[i:], "is_vocab": False})
                break

            # 先加一般文字
            if earliest_pos > i:
                segments.append({"text": line[i:earliest_pos], "is_vocab": False})

            # 再加詞彙片段
            segments.append({"text": chosen_word, "is_vocab": True})
            i = earliest_pos + len(chosen_word)

        return segments

screen vocab_textbox(display_text):
    # 文字框：1000x220、黑底 80% 透明、字 22px（按需求）
    frame:
        xalign 0.5 yalign 0.85
        xsize 1000 ysize 220
        background "#000000cc"
        padding (40, 25)

        vbox:
            spacing 6
            for _line in (display_text or "").split("\n"):
                $ _segments = _split_line_by_vocab(_line)
                hbox:
                    spacing 0
                    for seg in _segments:
                        if seg["is_vocab"]:
                            textbutton seg["text"]:
                                action NullAction()
                                background None
                                padding (0, 0)
                                # 金色 + 滑過變白
                                text_color "#ffcc66"
                                text_hover_color "#ffffff"
                                text_size 22
                                # 懸浮顯示詞彙 tooltip；移開就關閉
                                hovered Show("vocab_tooltip", word=seg["text"])
                                unhovered Hide("vocab_tooltip")
                        else:
                            text seg["text"] size 22 color "#ffffff"
