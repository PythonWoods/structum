# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Cleanup plugin for Structum."""

from pathlib import Path

import typer
from structum.plugins.sdk import PluginBase

from structum_clean.__about__ import __version__
from structum_clean.core import clean_pycache


class CleanPlugin(PluginBase):
    """Official cleanup plugin for Structum."""

    name = "clean"
    version = __version__
    category = "utility"
    description = "Remove __pycache__ directories recursively"
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize the plugin."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register the clean command."""

        @app.command(name="clean", rich_help_panel=help_panel)
        def clean_command(
            directory: Path = typer.Argument(
                ".",
                help="The root directory to clean.",
                exists=True,
                file_okay=False,
                dir_okay=True,
                resolve_path=True,
            ),
            verbose: bool = typer.Option(
                True, "--verbose/--quiet", "-v/-q", help="Verbose output."
            ),
            skip_venv: bool = typer.Option(
                False,
                "--skip-venv",
                help="Skip virtual environment directories (.env, venv, etc.).",
            ),
        ) -> None:
            """Recursively removes all __pycache__ directories.

            \b
            Examples:
                structum clean .
                structum clean src --quiet
                structum clean . --skip-venv
            """
            clean_pycache(directory, verbose=verbose, skip_venv=skip_venv)
