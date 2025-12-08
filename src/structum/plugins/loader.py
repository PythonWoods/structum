# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin loader for Structum.

This module handles the discovery and loading of external plugins only.
Plugins are discovered via the 'structum.plugins' entry point group.
Official plugins (structum_*) are automatically detected and tagged.
"""

from importlib.metadata import entry_points

import typer
from rich.console import Console

from structum.core.config import get_plugin_enabled

from .registry import PluginRegistry

console = Console()


def load_entrypoint_plugins(app: typer.Typer) -> None:
    """Loads external plugins via entry points.

    Discovers plugins from the 'structum.plugins' entry point group.
    Automatically detects official plugins (structum_* packages) and tags them.
    Provides conflict warnings if multiple plugins have the same name.
    """
    eps = entry_points(group="structum.plugins")

    if not eps:
        return

    console.print("[bold blue]🔌 Loading plugins...[/bold blue]")

    for ep in eps:
        try:
            plugin_cls = ep.load()

            # Auto-detect official plugins by module name
            is_official = plugin_cls.__module__.startswith("structum_")

            # Check for conflicts before registration
            if plugin_cls.name in PluginRegistry.list_plugins():
                existing_plugin = PluginRegistry.get(plugin_cls.name)
                if existing_plugin:
                    console.print(
                        f"[yellow]⚠ WARNING: Plugin '{plugin_cls.name}' already registered. "
                        f"Overriding {existing_plugin.__class__.__module__} with {plugin_cls.__module__}[/yellow]"
                    )

            # Register with type information
            PluginRegistry.register(plugin_cls, is_official=is_official)

            # Display load status with tag
            tag = "[OFFICIAL]" if is_official else "[EXTERNAL]"
            console.print(f"[green]✔ Plugin loaded {tag}:[/green] {ep.name}")

        except Exception as e:
            console.print(f"[red]✘ Error loading plugin {ep.name}:[/red] {e}")

    # Initialize all loaded plugins
    PluginRegistry.load_all()

    # Register CLI commands for enabled plugins
    for name in PluginRegistry.list_plugins():
        plugin = PluginRegistry.get(name)
        if plugin and get_plugin_enabled(name):
            plugin.register_commands(app)


def load_plugins(app: typer.Typer) -> None:
    """Loads all available plugins via entry points.

    This function discovers and loads plugins from the 'structum.plugins' entry point group.
    Official plugins (structum_*) are automatically detected and tagged.
    """
    load_entrypoint_plugins(app)
