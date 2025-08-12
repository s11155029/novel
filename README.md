# Ren'Py Interactive Vocabulary Story

## Overview
This project is a **Ren'Py 8.3.7** interactive visual novel that integrates:
1. **Historical storytelling** – A fictionalized story based on a German soldier, Albert Köhler, during WWI.
2. **Bilingual vocabulary learning** – Highlighted Chinese vocabulary in story text, with English translations shown in a tooltip on hover or click.

Codex tasks will often focus on **maintaining**, **refactoring**, or **adding features** to the vocabulary tooltip system while preserving the story and gameplay logic.

---

## Core Features
- **Vocabulary Highlighting**
  - Words from a predefined dictionary (`vocabulary`) in Chinese are automatically highlighted in gold and underlined.
  - Hovering or clicking on a highlighted word opens a tooltip showing the English translation.
  
- **Story Navigation**
  - Each chapter uses a custom screen (`story_main`) to render dialogue text with vocabulary highlighting applied.
  - Navigation buttons allow moving between chapters or returning to the main menu.

- **Tooltip System**
  - Implemented via a Ren'Py screen (`vocab_tooltip`) using `frame` and `vbox` to display:
    - Title ("詞彙解釋")
    - Highlighted word
    - English translation
    - Close button

---

## File Structure
