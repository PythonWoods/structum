# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Tree visualization plugin for Structum."""

from enum import Enum
from pathlib import Path

import typer
from structum.plugins.sdk import PluginBase

from structum_tree.__about__ import __version__
from structum_tree.core import print_tree


class ThemeChoice(str, Enum):
    """Valid theme choices for tree visualization."""
    NERD = "nerd"
    EMOJI = "emoji"
    ASCII = "ascii"
    NONE = "none"


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


class TreePlugin(PluginBase):
    """Official tree visualization plugin for Structum."""

    name = "tree"
    version = __version__
    category = "utility"
    description = "Visualize directory structures as trees"
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize the plugin."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register the tree command."""
        @app.command(name="tree", rich_help_panel=help_panel)
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
                help="Filter by file extensions (e.g., '-e py -e md' or '-e py,md,js').",
                callback=parse_list_callback
            ),
            ignore_dirs: list[str] | None = typer.Option(
                None,
                "--ignore", "-i",
                help="Directory names to exclude (e.g., '-i .git -i node_modules' or '-i .git,node_modules').",
                callback=parse_list_callback
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
            theme: ThemeChoice = typer.Option(
                ThemeChoice.EMOJI,
                "--theme", "-t",
                help="Icon theme to use.",
                case_sensitive=False
            ),
            show_stats: bool = typer.Option(
                False,
                "--stats", "-s",
                help="Show directory and file count statistics."
            ),
        ) -> None:
            """Visualize directory structures as trees.

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
                theme=theme.value,  # Convert Enum to string
                show_stats=show_stats
            )
