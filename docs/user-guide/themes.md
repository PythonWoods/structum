# Themes and Icons

Structum offers a flexible theming system to adapt the output to your terminal capabilities and use case.

## Available Themes

You can select a theme using the `--theme` (or `-t`) option.

### 1. Emoji Theme (Default)
`--theme emoji`

Uses standard Unicode emojis.
*   **Pros**: Works in almost all modern terminals and web browsers. No special setup required.
*   **Cons**: Icons are generic (e.g., generic file icon vs specific language icon).

### 2. Nerd Theme (Professional)
`--theme nerd`

Uses specific glyphs from the **Nerd Fonts** project.
*   **Pros**: Highly detailed icons for specific file types (Python, Docker, Rust, React, etc.). Looks very professional.
*   **Cons**: **Requires a patched font.**

!!! warning "Requirement: Nerd Fonts"
    To use the `nerd` theme correctly, your terminal must be using a Nerd Font. If you see squares (□) or weird characters, you need to install a font.

    1.  Go to [Nerd Fonts Downloads](https://www.nerdfonts.com/font-downloads).
    2.  Download a font like **JetBrainsMono Nerd Font** or **MesloLGS NF**.
    3.  Install the font on your OS.
    4.  Configure your terminal (VS Code, iTerm, Windows Terminal) to use that font.

### 3. ASCII Theme
`--theme ascii`

Uses plain text characters (`|`, `-`, `+`).
*   **Pros**: 100% compatible everywhere. Perfect for copying into code blocks in Markdown files or sending to LLMs.
*   **Cons**: No colors, no icons.

### 4. None
`--theme none`

Minimalist output. Just indentation and text.