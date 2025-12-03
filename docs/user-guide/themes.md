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
    To use the `nerd` theme correctly, your terminal must be using a Nerd Font. If you see squares (□) or weird characters, you need to install and configure a font.

    ### Step 1: Install a Nerd Font
    
    We recommend **JetBrainsMono Nerd Font** or **MesloLGS NF**.

    === "Linux (Debian/Ubuntu)"
        ```bash
        # Create fonts directory
        mkdir -p ~/.local/share/fonts
        
        # Download JetBrainsMono Nerd Font
        wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/JetBrainsMono.zip
        
        # Unzip and install
        unzip JetBrainsMono.zip -d ~/.local/share/fonts
        fc-cache -fv
        ```

    === "macOS (Homebrew)"
        ```bash
        brew tap homebrew/cask-fonts
        brew install --cask font-jetbrains-mono-nerd-font
        ```

    === "Windows"
        1.  Go to [Nerd Fonts Downloads](https://www.nerdfonts.com/font-downloads).
        2.  Download **JetBrainsMono Nerd Font**.
        3.  Unzip the file.
        4.  Select all `.ttf` files, right-click, and choose **"Install"**.

    ### Step 2: Configure Your Editor/Terminal

    After installing the font, you must tell your terminal to use it.

    === "VS Code"
        1.  Open Settings (`Ctrl + ,` or `Cmd + ,`).
        2.  Search for `Terminal > Integrated: Font Family`.
        3.  Set the value to: `'JetBrainsMono Nerd Font'` (or the name of the font you installed).
        4.  Restart the terminal.

    === "Windows Terminal"
        1.  Open Settings (`Ctrl + ,`).
        2.  Select your profile (e.g., PowerShell or Ubuntu).
        3.  Go to **Appearance** > **Font face**.
        4.  Select **JetBrainsMono Nerd Font**.
        5.  Click **Save**.

    === "iTerm2 (macOS)"
        1.  Go to **Preferences** > **Profiles** > **Text**.
        2.  Check **"Use a different font for non-ASCII text"**.
        3.  Select **JetBrainsMono Nerd Font** for both font settings.

    === "GNOME Terminal (Ubuntu/Linux)"
        1.  Open GNOME Terminal.
        2.  Go to **Preferences** (or right-click and select **Preferences**).
        3.  Select your profile (usually **Unnamed** or **Default**).
        4.  Go to the **Text** tab.
        5.  Uncheck **"Use the system fixed width font"**.
        6.  Click **"Custom font"** and select **JetBrainsMono Nerd Font** (or **JetBrainsMono Nerd Font Mono**).
        7.  Close preferences. The font will apply immediately.

    === "Konsole (KDE)"
        1.  Open Konsole.
        2.  Go to **Settings** > **Edit Current Profile**.
        3.  Select the **Appearance** tab.
        4.  Click **"Select Font"**.
        5.  Choose **JetBrainsMono Nerd Font** from the list.
        6.  Click **OK** and **Apply**.

### 3. ASCII Theme
`--theme ascii`

Uses plain text characters (`|`, `-`, `+`).
*   **Pros**: 100% compatible everywhere. Perfect for copying into code blocks in Markdown files or sending to LLMs.
*   **Cons**: No colors, no icons.

### 4. None
`--theme none`

Minimalist output. Just indentation and text.