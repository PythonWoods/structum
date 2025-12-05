# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Tree Command.
"""

from pathlib import Path

import typer

from structum.core.tree import print_tree


def tree_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to analyze.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g. -e py -e md)."
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude (e.g. -i .git -i node_modules)."
    ),
    max_depth: int | None = typer.Option(
        None,
        "--depth", "-d",
        help="Maximum depth of the tree traversal."
    ),
    show_hidden: bool = typer.Option(
        False,
        "--hidden",
        help="Show hidden files and directories (starting with '.')."
    ),
    ignore_empty: bool = typer.Option(
        False,
        "--no-empty",
        help="Hide directories that do not contain visible files."
    ),
    theme: str = typer.Option(
        "emoji",
        "--theme", "-t",
        help="Icon theme to use: 'nerd', 'emoji', 'ascii', 'none'."
    ),
    show_stats: bool = typer.Option(
        False,
        "--stats", "-s",
        help="Show directory and file count statistics."
    ),
) -> None:
    """
    Visualizes the directory structure of the specified path.

    \b
    Examples:
        structum tree . --theme nerd
        structum tree src --depth 2 --ext py
    """

    # Note: CLI flag is --hidden (show_hidden=True),
    # but core logic expects ignore_hidden (True by default).
    # We invert the boolean here.
    ignore_hidden_logic = not show_hidden

    print_tree(
        directory=directory,
        extensions=extensions,
        ignore_dirs=ignore_dirs,
        max_depth=max_depth,
        ignore_hidden=ignore_hidden_logic,
        ignore_empty=ignore_empty,
        theme=theme,
        show_stats=show_stats
    )
