# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Code archiving plugin for Structum."""

from pathlib import Path

import typer
from rich.console import Console
from structum.plugins.sdk import PluginBase

from structum_archive.__about__ import __version__
from structum_archive.core import create_archive

console = Console()


def parse_list_callback(value: list[str] | None) -> list[str] | None:
    """Parse comma-separated values and flatten multiple flags.

    Supports both:
    - Multiple flags: --ext py --ext md
    - Comma-separated: --ext py,md,js
    - Mixed: --ext py,md --ext js
    """
    if not value:
        return None

    result = []
    for item in value:
        # Split by comma and strip whitespace
        parts = [part.strip() for part in item.split(",") if part.strip()]
        result.extend(parts)

    return result if result else None


class ArchivePlugin(PluginBase):
    """Official code archiving plugin for Structum."""

    name = "archive"
    version = __version__
    category = "export"
    description = "Archive source code into Markdown files"
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize the plugin."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register the archive command."""
        @app.command(name="archive", rich_help_panel=help_panel)
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
                help="Filter by file extensions (e.g., '-e py -e md' or '-e py,md,js').",
                callback=parse_list_callback
            ),
            ignore_dirs: list[str] | None = typer.Option(
                None,
                "--ignore", "-i",
                help="Directory names to exclude (e.g., '-i .git -i node_modules' or '-i .git,node_modules').",
                callback=parse_list_callback
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
                help="Verbose output."
            ),
        ) -> None:
            """Archive source code into Markdown files.

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
