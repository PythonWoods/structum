# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin loader for Structum.

This module handles the discovery and loading of both built-in and external plugins.
External plugins are discovered via the 'structum.plugins' entry point group.
"""

from importlib.metadata import entry_points

import typer
from rich.console import Console

console = Console()


def load_builtin_plugins(app: typer.Typer) -> None:
    """Loads built-in plugins contained in the structum.plugins package."""
    from . import sample_plugin

    sample_plugin.register(app)


def load_entrypoint_plugins(app: typer.Typer) -> None:
    """Loads external plugins via entry points.

    Looks for entry points in the 'structum.plugins' group.
    """
    # Note: We only print if we actually find plugins to avoid noise,
    # or we could use a verbose flag if passed down (but loader runs early).
    # For now, we'll keep it quiet unless errors occur or plugins are found.

    eps = entry_points(group="structum.plugins")

    if not eps:
        return

    console.print("[bold blue]🔌 Loading external plugins...[/bold blue]")

    for ep in eps:
        try:
            plugin = ep.load()
            plugin(app)
            console.print(f"[green]✔ Plugin loaded:[/green] {ep.name}")
        except Exception as e:
            console.print(f"[red]✘ Error loading plugin {ep.name}:[/red] {e}")


def load_plugins(app: typer.Typer) -> None:
    """Loads all available plugins (built-in and external)."""
    load_builtin_plugins(app)
    load_entrypoint_plugins(app)
