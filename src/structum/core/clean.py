# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Cleanup utilities for Structum.

This module provides functionality to recursively remove ``__pycache__`` directories
from a project. It is used by the CLI ``clean`` command.
"""

import os
import shutil
from pathlib import Path

from rich.console import Console

console = Console()


def clean_pycache(root: Path, verbose: bool = True) -> int:
    """Recursively removes all ``__pycache__`` directories under the specified root.

    Args:
        root: The root directory to start the recursive search.
        verbose: If ``True``, prints each removed directory to the console.

    Returns:
        The number of ``__pycache__`` directories successfully removed.
    """
    root = root.resolve()
    removed = 0

    for dirpath, dirnames, _ in os.walk(root):
        current_dir = Path(dirpath)
        # Iterate over a copy of dirnames to modify it safely
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
        console.print(f"✅ Total __pycache__ directories removed: [bold green]{removed}[/bold green]")

    return removed
