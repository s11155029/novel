# game/ui_vocab.rpy
# Splits text into normal and vocabulary segments, displaying vocab segments as textbuttons.
# Hover or click shows tooltip. Works with Ren'Py 8.3.x without hyperlink config.

init python:
    try:
        _VOCAB_KEYS = list(vocabulary.keys())
        _VOCAB_KEYS.sort(key=len, reverse=True)  # Longer words first
    except Exception:
        _VOCAB_KEYS = []

    def _split_line_by_vocab(line):
        if not line:
            return [{"text": "", "is_vocab": False}]
        segments = []
        i = 0
        n = len(line)
        while i < n:
            earliest_pos = None
            chosen_word = None
            for w in _VOCAB_KEYS:
                pos = line.find(w, i)
                if pos == -1:
                    continue
                if (earliest_pos is None) or (pos < earliest_pos) or (pos == earliest_pos and len(w) > len(chosen_word or "")):
                    earliest_pos = pos
                    chosen_word = w
            if earliest_pos is None:
                segments.append({"text": line[i:], "is_vocab": False})
                break
            if earliest_pos > i:
                segments.append({"text": line[i:earliest_pos], "is_vocab": False})
            segments.append({"text": chosen_word, "is_vocab": True})
            i = earliest_pos + len(chosen_word)
        return segments

screen vocab_textbox(display_text):
    default tt = Tooltip(None)

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
                                action tt.Action(seg["text"])
                                background None
                                padding (0, 0)
                                text_color "#ffcc66"
                                text_hover_color "#ffffff"
                                text_size 22
                                hovered tt.Action(seg["text"])
                                unhovered tt.Action(None)
                        else:
                            text seg["text"] size 22 color "#ffffff"

    if tt.value:
        use vocab_tooltip(tt.value)
