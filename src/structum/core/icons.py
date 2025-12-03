# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Icon management for file and directory visualization.

This module provides multiple icon themes for representing files and directories
in the structum project. Each theme offers a different visual style suitable for
various display contexts and terminal capabilities.

Available themes:
    - nerd: Uses Nerd Fonts icons (requires Nerd Fonts installation)
    - emoji: Uses Unicode emoji characters (maximum compatibility)
    - ascii: Uses simple ASCII characters (safe for text/log files)
    - none: No icons displayed

Example:
    >>> from structum.core.icons import get_icon
    >>> import pathlib
    >>> path = pathlib.Path("example.py")
    >>> icon = get_icon(path, theme_name="emoji")
    >>> print(f"{icon} {path.name}")
    🐍 example.py

Attributes:
    NERD_SET: Nerd Fonts icon theme.
    EMOJI_SET: Emoji icon theme.
    ASCII_SET: ASCII icon theme.
    NONE_SET: Empty icon theme.
    THEMES: Registry mapping theme names to IconSet instances.
"""
import pathlib
from typing import NamedTuple


class IconSet(NamedTuple):
    """Defines a set of icons for folders, default files, and mappings.

    Attributes:
        folder_open: Icon for an open folder.
        folder_closed: Icon for a closed folder.
        file_default: Default icon for files not specifically mapped.
        extensions: A dictionary mapping file extensions (e.g., ".py") to their respective icons.
        filenames: A dictionary mapping specific filenames (e.g., "dockerfile") to their respective icons.
    """
    folder_open: str
    folder_closed: str
    file_default: str
    extensions: dict[str, str]
    filenames: dict[str, str]

# --- 1. Set "NERD" (Requires Nerd Fonts) ---
NERD_SET = IconSet(
    folder_open="",
    folder_closed="",
    file_default="",
    filenames={
        "dockerfile": "", "makefile": "", "jenkinsfile": "",
        ".gitignore": "", ".env": "", "requirements.txt": "",
    },
    extensions={
        ".py": "", ".js": "", ".ts": "", ".html": "", ".css": "",
        ".json": "", ".md": "", ".txt": "", ".sql": "",
        ".zip": "", ".png": "", ".jpg": "", ".pdf": "",
    }
)

# --- 2. Set "EMOJI" (Compatible everywhere) ---
EMOJI_SET = IconSet(
    folder_open="📂",
    folder_closed="📁",
    file_default="📄",
    filenames={
        "dockerfile": "🐳", "makefile": "🛠️", ".gitignore": "🙈", ".env": "🔒",
    },
    extensions={
        ".py": "🐍", ".js": "🟨", ".ts": "🟦", ".html": "🌐", ".css": "🎨",
        ".json": "📋", ".md": "📝", ".txt": "📄", ".sql": "💾",
        ".zip": "📦", ".png": "🖼️", ".jpg": "🖼️", ".pdf": "📕",
        ".exe": "⚙️", ".sh": "🐚"
    }
)

# --- 3. Set "ASCII" (Safe for text/log files) ---
ASCII_SET = IconSet(
    folder_open="",
    folder_closed="",
    file_default="",
    filenames={},
    extensions={}
)

# --- 4. Set "NONE" (No icon) ---
NONE_SET = IconSet("", "", "", {}, {})

# Registry of available themes
THEMES = {
    "nerd": NERD_SET,
    "emoji": EMOJI_SET,
    "ascii": ASCII_SET,
    "none": NONE_SET
}

def get_icon(path: pathlib.Path, theme_name: str = "emoji") -> str:
    """Returns the appropriate icon for the given path based on the specified theme.

    The function first checks if the path is a directory. If so, it returns the
    folder icon for the chosen theme. Otherwise, it attempts to match the file's
    exact name, then its extension. If no specific match is found, it falls back
    to the theme's default file icon.

    Args:
        path: The path to the file or directory for which to get an icon.
        theme_name: The name of the icon theme to use. Available themes are
            "nerd", "emoji", "ascii", and "none". Defaults to "emoji" for
            maximum compatibility.

    Returns:
        The icon string corresponding to the path and theme. Returns an empty
        string if theme_name is "none".
    """
    theme = THEMES.get(theme_name, EMOJI_SET)

    # If the theme is 'none', return an empty string immediately
    if theme_name == "none":
        return ""

    if path.is_dir():
        return theme.folder_open

    name_lower = path.name.lower()

    # 1. Check exact filename
    if name_lower in theme.filenames:
        return theme.filenames[name_lower]

    # 2. Check extension
    return theme.extensions.get(path.suffix.lower(), theme.file_default)
