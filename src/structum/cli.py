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

from structum.core.archive import create_archive
from structum.core.tree import print_tree

# Initialize Typer app and Rich console
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)
console = Console()

@app.command(name="tree")
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
        theme=theme
    )


@app.command(name="archive")
def archive_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to archive.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    output: Path = typer.Option(
        "archive.md",
        "--output", "-o",
        help="Output file path (or directory if split mode is enabled)."
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g. -e py -e md)."
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude."
    ),
    split_by_folder: bool = typer.Option(
        False,
        "--split-folder",
        help="Create a separate archive for each folder."
    ),
    split_by_type: bool = typer.Option(
        False,
        "--split-type",
        help="Create a separate archive for each file extension."
    ),
    toc: bool = typer.Option(
        True,
        "--toc/--no-toc",
        help="Include a Table of Contents."
    ),
    tree: bool = typer.Option(
        True,
        "--tree/--no-tree",
        help="Include a directory tree structure."
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Enable verbose output."
    ),
) -> None:
    """
    Archives source code into Markdown files.

    \b
    Features:
    * Collects files by extension
    * Generates Table of Contents (ToC)
    * Includes ASCII directory tree
    * Supports splitting by folder or file type

    \b
    Examples:
        structum archive . --output code.md --ext py
        structum archive src --split-folder --output docs/
    """
    try:
        create_archive(
            root=directory,
            output=output,
            extensions=extensions,
            ignore_dirs=ignore_dirs,
            split_by_folder=split_by_folder,
            split_by_type=split_by_type,
            toc=toc,
            include_tree=tree,
            verbose=verbose
        )
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1) from None


if __name__ == "__main__":
    app()
