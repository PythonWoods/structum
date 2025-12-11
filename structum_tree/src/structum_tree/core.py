# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Directory tree visualization with Rich.

This module provides functionality to build and display directory structures
as visual trees using the Rich library. It supports multiple themes, filtering
by file extension, excluding directories, and controlling the depth of traversal.

Functions:
    build_tree: Builds a Rich Tree object representing a directory structure.
    print_tree: Prints a formatted directory tree to the console.
    get_tree_ascii: Generates an ASCII string representation of a directory tree.

Example:
    >>> from structum.core.tree import print_tree
    >>> import pathlib
    >>> print_tree(pathlib.Path("./my_project"), theme="emoji", max_depth=2)
"""

import pathlib
from collections.abc import Iterable, Sequence

from rich.console import Console
from rich.text import Text
from rich.tree import Tree

from structum_tree import icons
from structum_tree.utils import normalize_extensions

console = Console()


def build_tree(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    exclude_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_files: bool = False,
    ignore_empty: bool = False,
    theme: str = "emoji",
) -> Tree | None:
    """Builds a Rich Tree object representing the directory structure.

    This is the core function that recursively traverses the specified directory
    and constructs a visual tree, applying various filtering and styling options.

    Args:
        directory: The root directory from which to build the tree.
        extensions: File extensions to include. If provided, only files with
            these extensions will be shown. Defaults to None (all files).
        exclude_dirs: Directory names to exclude from the tree. Directories
            matching these names will not be traversed or displayed.
            Defaults to None.
        max_depth: Maximum depth of the tree to display. 0 means only the root,
            1 means root and its immediate children, and so on.
            Defaults to None (no limit).
        ignore_hidden: If True, files and directories starting with '.' will be
            ignored. Defaults to True.
        ignore_files: If True, no files will be included in the tree, only
            directories. Defaults to False.
        ignore_empty: If True, empty directories (after applying all filters)
            will not be displayed. If the root directory becomes empty due to
            filters, the function returns None. Defaults to False.
        theme: The name of the theme to apply for icons and colors. Supported
            themes are 'nerd', 'emoji', 'ascii', 'none'. The 'ascii' and 'none'
            themes disable complex colors and icons. Defaults to "emoji".

    Returns:
        A Tree object representing the directory structure, or None if
        ignore_empty is True and the tree ends up being empty after applying
        all filters.

    Raises:
        NotADirectoryError: If the provided directory path does not exist or
            is not a valid directory.
    """

    # 1. Validation
    directory = directory.resolve()
    if not directory.exists() or not directory.is_dir():
        raise NotADirectoryError(f"The path '{directory}' is not a valid directory.")

    target_exts = normalize_extensions(extensions)
    excluded_dir_names = set(exclude_dirs or [])

    # 2. Theme-based Style Configuration
    # Create boolean flags to simplify logic in the loop
    is_plain_style = theme in ["ascii", "none"]

    guide_style = "white" if is_plain_style else "bright_black"

    # Setup Root
    root_icon = icons.get_icon(directory, theme)

    # If we are in plain style, no colors for the root
    if is_plain_style:
        root_label = Text(f"{root_icon} {directory.name}".strip())
    else:
        root_label = Text(f"{root_icon} {directory.name}".strip(), style="cyan")

    tree = Tree(root_label, guide_style=guide_style)

    # 3. Recursive Function
    def _populate_branch(
        current_tree: Tree, current_path: pathlib.Path, current_depth: int
    ) -> bool:
        if max_depth is not None and current_depth >= max_depth:
            return False

        try:
            items = sorted(current_path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
        except PermissionError:
            msg = "🔒 [Access Denied]"
            # Red color only if not in ascii mode
            style = "red" if not is_plain_style else ""
            current_tree.add(Text(msg, style=style))
            return True

        has_visible_content = False

        for item in items:
            if ignore_hidden and item.name.startswith("."):
                continue

            # --- DIRECTORY ---
            if item.is_dir():
                if item.name in excluded_dir_names:
                    continue

                icon = icons.get_icon(item, theme)
                label_str = f"{icon} {item.name}".strip()

                # Folder style
                style = "" if is_plain_style else "yellow"

                branch_tree = Tree(Text(label_str, style=style))

                child_has_content = _populate_branch(branch_tree, item, current_depth + 1)

                if child_has_content or (not ignore_empty):
                    current_tree.add(branch_tree)
                    has_visible_content = True

            # --- FILE ---
            elif item.is_file() and not ignore_files:
                if target_exts and item.suffix.lower() not in target_exts:
                    continue

                icon = icons.get_icon(item, theme)
                label_str = f"{icon} {item.name}".strip()

                # Color Logic (only if not in plain/ascii mode)
                style = ""
                if not is_plain_style:
                    style = "white"  # Default
                    ext = item.suffix.lower()
                    if ext == ".py":
                        style = "green"
                    elif ext == ".md":
                        style = "magenta"
                    elif ext in [".js", ".ts", ".json"]:
                        style = "cyan"
                    elif ext in [".yml", ".yaml", ".toml", ".ini"]:
                        style = "blue"
                    elif ext in [".txt", ".log", ".csv"]:
                        style = "dim white"

                current_tree.add(Text(label_str, style=style))
                has_visible_content = True

        return has_visible_content

    # 4. Start Recursion
    has_content = _populate_branch(tree, directory, 0)

    # If the root is empty (after filters) and ignore_empty is True, return None
    if ignore_empty and not has_content:
        return None

    return tree


# --- CLI Usage Wrapper (Print to screen) ---


def print_tree(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_empty: bool = False,
    theme: str = "emoji",
    show_stats: bool = False,
) -> None:
    """Prints a formatted, colored directory tree to the console.

    This function acts as a convenient wrapper around build_tree to display
    the tree directly to standard output using Rich's console rendering.

    Args:
        directory: The root directory from which to print the tree.
        extensions: File extensions to include. Defaults to None.
        ignore_dirs: Directory names to exclude. Defaults to None.
        max_depth: Maximum depth to display. Defaults to None.
        ignore_hidden: If True, hidden files and directories are ignored.
            Defaults to True.
        ignore_empty: If True, empty directories (after filtering) are not
            displayed. Defaults to False.
        theme: The theme to apply for icons and colors. Defaults to "emoji".
        show_stats: If True, displays directory and file count statistics.
            Defaults to False.
    """
    # Count directories and files if stats are requested
    dir_count = 0
    file_count = 0

    if show_stats:
        # Count items recursively
        target_exts = normalize_extensions(extensions)
        excluded_dir_names = set(ignore_dirs or [])

        def _count_items(path: pathlib.Path, depth: int) -> None:
            nonlocal dir_count, file_count

            if max_depth is not None and depth > max_depth:
                return

            try:
                items = list(path.iterdir())
            except PermissionError:
                return

            for item in items:
                if ignore_hidden and item.name.startswith("."):
                    continue

                if item.is_dir():
                    if item.name not in excluded_dir_names:
                        dir_count += 1
                        _count_items(item, depth + 1)
                elif item.is_file():
                    if not target_exts or item.suffix.lower() in target_exts:
                        file_count += 1

        _count_items(directory, 0)

    tree = build_tree(
        directory=directory,
        extensions=extensions,
        exclude_dirs=ignore_dirs,  # Note: correct parameter name mapping
        max_depth=max_depth,
        ignore_hidden=ignore_hidden,
        ignore_files=False,
        ignore_empty=ignore_empty,
        theme=theme,
    )

    if tree:
        console.print(tree)
        if show_stats:
            # Format stats like Unix tree command
            dir_word = "directory" if dir_count == 1 else "directories"
            file_word = "file" if file_count == 1 else "files"
            console.print(f"\n{dir_count} {dir_word}, {file_count} {file_word}")
    else:
        console.print("[yellow italic]No content found with current filters.[/yellow italic]")


# --- Export Wrapper (Returns string) ---


def get_tree_ascii(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_empty: bool = False,
) -> str:
    """Generates an ASCII string representation of a directory tree.

    This function is useful for exporting the tree to text files, Markdown,
    or other contexts where Rich's advanced rendering is not supported or
    desired. It forces the 'ascii' theme to ensure a plain text output.

    Args:
        directory: The root directory from which to build the tree string.
        extensions: File extensions to include. Defaults to None.
        ignore_dirs: Directory names to exclude. Defaults to None.
        max_depth: Maximum depth to display. Defaults to None.
        ignore_hidden: If True, hidden files and directories are ignored.
            Defaults to True.
        ignore_empty: If True, empty directories (after filtering) are not
            displayed. Defaults to False.

    Returns:
        A string containing the ASCII representation of the directory tree.
        Returns an empty string if no content is found after applying filters.
    """
    # Use a temporary console to capture output without spurious color codes
    temp_console = Console(no_color=True, width=1000)

    tree = build_tree(
        directory=directory,
        extensions=extensions,
        exclude_dirs=ignore_dirs,
        max_depth=max_depth,
        ignore_hidden=ignore_hidden,
        ignore_files=False,
        ignore_empty=ignore_empty,
        theme="ascii",  # <--- Force ASCII theme
    )

    if not tree:
        return ""

    with temp_console.capture() as capture:
        temp_console.print(tree)

    return capture.get()
