# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Clean Command.
"""

from pathlib import Path

import typer

from structum.core.clean import clean_pycache


def clean_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to clean.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Verbose output."
    ),
    skip_venv: bool = typer.Option(
        False,
        "--skip-venv",
        help="Skip virtual environment directories (.env, venv, etc.)."
    ),
) -> None:
    """
    Recursively removes all __pycache__ directories.

    \b
    Examples:
        structum clean .
        structum clean src --quiet
        structum clean . --skip-venv
    """
    clean_pycache(directory, verbose=verbose, skip_venv=skip_venv)
