# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Cleanup utilities for Structum.

This module provides functionality to recursively remove ``__pycache__`` directories
from a project. It is used by the clean command.
"""

import os
import shutil
from pathlib import Path

from rich.console import Console

console = Console()

# Common virtual environment directory names
VENV_DIRS = {'.env', 'env', 'venv', '.venv', 'virtualenv'}


def clean_pycache(root: Path, verbose: bool = True, skip_venv: bool = False) -> int:
    """Recursively removes all ``__pycache__`` directories under the specified root.

    Args:
        root: The root directory to start the recursive search.
        verbose: If ``True``, prints each removed directory to the console.
        skip_venv: If ``True``, skips common virtual environment directories.

    Returns:
        The number of ``__pycache__`` directories successfully removed.

    Note:
        By default, this function cleans __pycache__ in all directories including
        virtual environments. Python will recreate them automatically when needed.
        Use skip_venv=True to exclude virtual environments if desired.
    """
    root = root.resolve()
    removed = 0
    skipped_venvs = set()

    for dirpath, dirnames, _ in os.walk(root):
        current_dir = Path(dirpath)

        # Skip virtual environment directories if requested
        if skip_venv:
            for dirname in list(dirnames):
                if dirname in VENV_DIRS:
                    skipped_venvs.add(current_dir / dirname)
                    dirnames.remove(dirname)  # Don't walk into venv

        # Remove __pycache__ directories
        for dirname in list(dirnames):
            if dirname == "__pycache__":
                target = current_dir / dirname
                try:
                    shutil.rmtree(target)
                    removed += 1
                    if verbose:
                        console.print(f"🗑️  Removed: [dim]{target}[/dim]")
                except Exception as exc:
                    console.print(f"[bold red]⚠️  Error removing {target}:[/bold red] {exc}")

                # Prevent walking into the directory we just removed
                dirnames.remove(dirname)

    if verbose:
        if skipped_venvs:
            console.print(f"[dim]ℹ️  Skipped {len(skipped_venvs)} virtual environment(s)[/dim]")
        console.print(f"✅ Total __pycache__ directories removed: [bold green]{removed}[/bold green]")

    return removed
