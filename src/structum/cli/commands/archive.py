# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Archive Command.
"""

from pathlib import Path

import typer
from rich.console import Console

from structum.core.archive import create_archive

app = typer.Typer()
console = Console()

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
