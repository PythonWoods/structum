# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin loader for Structum.

This module handles the discovery and loading of both built-in and external plugins.
Built-in plugins are auto-discovered via filesystem scanning.
External plugins are discovered via the 'structum.plugins' entry point group.
"""

import importlib
import inspect
from importlib.metadata import entry_points
from pathlib import Path
from typing import TYPE_CHECKING

import typer
from rich.console import Console

from structum.core.config import get_plugin_enabled

from .registry import PluginRegistry
from .sdk import PluginBase

if TYPE_CHECKING:
    from typing import TypedDict

    class DevPluginInfo(TypedDict):
        """Information about a plugin in development mode."""
        name: str
        module_name: str
        path: Path
        plugin_class: type[PluginBase] | None
        error: str | None

console = Console()

# Global registry for plugins in development mode (.dev marker)
_dev_plugins: dict[str, "DevPluginInfo"] = {}


def get_dev_plugins() -> dict[str, "DevPluginInfo"]:
    """Return all plugins in development mode (.dev marker present).

    Returns:
        Dictionary mapping plugin names to their development info.
    """
    return _dev_plugins.copy()


def load_builtin_plugins(app: typer.Typer) -> None:
    """Auto-discovers and loads built-in plugins from the structum.plugins package.

    Discovery mechanism:
    - Scans all subdirectories in the plugins package
    - Looks for plugin.py files containing PluginBase subclasses
    - Checks for .dev marker file to identify development-mode plugins
    - Automatically imports and registers production plugins
    - Tracks dev-mode plugins separately (accessible via --show-dev flag)
    - Skips directories starting with underscore (_) for work-in-progress plugins
    - Consistent with external plugin loading mechanism
    """
    plugins_dir = Path(__file__).parent
    discovered_plugins = []

    # Clear dev plugins registry
    _dev_plugins.clear()

    # Scan for plugin directories
    for plugin_path in sorted(plugins_dir.iterdir()):
        # Skip non-directories and special directories
        if not plugin_path.is_dir():
            continue
        if plugin_path.name.startswith("_"):
            continue
        if plugin_path.name in ("__pycache__",):
            continue

        # Look for plugin.py file
        plugin_file = plugin_path / "plugin.py"
        if not plugin_file.exists():
            continue

        plugin_module_name = plugin_path.name

        # Check for .dev marker file (development mode)
        dev_marker = plugin_path / ".dev"
        is_dev_mode = dev_marker.exists()

        try:
            # Dynamically import the plugin module
            module = importlib.import_module(
                f".{plugin_module_name}.plugin",
                package="structum.plugins"
            )

            # Find PluginBase subclasses via introspection
            plugin_class = None
            for attr_name in dir(module):
                attr = getattr(module, attr_name)

                # Check if it's a class, subclass of PluginBase, and not PluginBase itself
                if (
                    inspect.isclass(attr)
                    and issubclass(attr, PluginBase)
                    and attr is not PluginBase
                ):
                    plugin_class = attr
                    break  # Only register the first plugin class found per module

            if plugin_class:
                if is_dev_mode:
                    # Track as development plugin (not registered)
                    _dev_plugins[plugin_class.name] = {
                        "name": plugin_class.name,
                        "module_name": plugin_module_name,
                        "path": plugin_path,
                        "plugin_class": plugin_class,
                        "error": None,
                    }
                else:
                    # Register as production plugin
                    PluginRegistry.register(plugin_class)
                    discovered_plugins.append((plugin_module_name, plugin_class.name))

        except Exception as e:
            if is_dev_mode:
                # Track failed dev plugin
                _dev_plugins[plugin_module_name] = {
                    "name": plugin_module_name,
                    "module_name": plugin_module_name,
                    "path": plugin_path,
                    "plugin_class": None,
                    "error": str(e),
                }
            else:
                console.print(
                    f"[yellow]⚠ Failed to load built-in plugin '{plugin_module_name}': {e}[/yellow]"
                )
            continue

    # Initialize all discovered plugins
    PluginRegistry.load_all()

    # Register CLI commands for enabled plugins
    for _, plugin_name in discovered_plugins:
        plugin = PluginRegistry.get(plugin_name)
        if plugin and get_plugin_enabled(plugin_name):
            plugin.register_commands(app)


def load_entrypoint_plugins(app: typer.Typer) -> None:
    """Loads external plugins via entry points.

    Looks for entry points in the 'structum.plugins' group.
    """
    eps = entry_points(group="structum.plugins")

    if not eps:
        return

    console.print("[bold blue]🔌 Loading external plugins...[/bold blue]")

    for ep in eps:
        try:
            plugin_cls = ep.load()
            PluginRegistry.register(plugin_cls)
            console.print(f"[green]✔ Plugin loaded:[/green] {ep.name}")
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
    """Loads all available plugins (built-in and external)."""
    load_builtin_plugins(app)
    load_entrypoint_plugins(app)
