# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
CLI Entry Point.

This module defines the main command-line interface using Typer.
It acts as the bridge between the user input and the core logic.
"""

from pathlib import Path

import typer
from rich.console import Console

from structum.core.tree import print_tree

# Initialize Typer app and Rich console
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)
console = Console()

@app.command()
def main(
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
) -> None:
    """
    Visualizes the directory structure of the specified path.
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
        theme=theme
    )

if __name__ == "__main__":
    app()
