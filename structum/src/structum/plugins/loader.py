# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin loader for Structum.

This module handles the discovery and loading of plugins.
All plugins are external packages discovered via the 'structum.plugins' entry point group.
Official plugins (structum_*) are automatically detected and tagged as [OFFICIAL].
Community plugins are tagged as [COMMUNITY].
"""

from importlib.metadata import entry_points

import typer
from rich.console import Console

from structum.config.manager import get_plugin_enabled

from .registry import PluginRegistry

console = Console()


def _register_disabled_plugin_command(
    app: typer.Typer, plugin_name: str, help_panel: str | None = None
) -> None:
    """Register a placeholder command for a disabled plugin.

    This shows a helpful message when users try to use a disabled plugin,
    instead of the generic "No such command" error.

    Args:
        app: The Typer application to register the command with.
        plugin_name: The name of the disabled plugin.
        help_panel: Optional help panel name for grouping in --help output.
    """

    def disabled_command_callback(ctx: typer.Context) -> None:
        """Show helpful message for disabled plugin."""
        console.print(
            f"[yellow]⚠ Plugin '{plugin_name}' is disabled.[/yellow]\n"
            f"[dim]Enable it with:[/dim] [cyan]structum plugins enable {plugin_name}[/cyan]"
        )
        raise typer.Exit(1)

    # Create a Typer app for the disabled plugin with no_args_is_help=False
    # This ensures the callback is invoked even when no subcommand is provided
    disabled_app = typer.Typer(
        name=plugin_name,
        help=f"Plugin '{plugin_name}' (currently disabled)",
        callback=disabled_command_callback,
        no_args_is_help=False,  # Call callback even without args
        invoke_without_command=True,  # Invoke callback without subcommand
        rich_help_panel=help_panel,
    )

    # Register it with the main app
    app.add_typer(disabled_app, name=plugin_name, rich_help_panel=help_panel)


def load_entrypoint_plugins(app: typer.Typer) -> None:
    """Loads plugins via entry points.

    Discovers plugins from the 'structum.plugins' entry point group.
    Automatically detects official plugins (structum_* packages) and tags them.
    Community plugins are tagged as [COMMUNITY].
    Provides conflict warnings if multiple plugins have the same name.
    """
    from structum.plugins.sdk import CATEGORIES

    eps = entry_points(group="structum.plugins")

    if not eps:
        return

    console.print("\n[bold blue]🔌 Loading Plugins[/bold blue]")

    loaded_count = 0
    failed_count = 0

    for ep in eps:
        try:
            plugin_cls = ep.load()

            # Auto-detect official plugins by module name
            is_official = plugin_cls.__module__.startswith("structum_")

            # Get distribution name for metadata reading
            distribution_name = ep.dist.name if ep.dist else None

            # Check for conflicts before registration
            if plugin_cls.name in PluginRegistry.list_plugins():
                existing_plugin = PluginRegistry.get(plugin_cls.name)
                if existing_plugin:
                    console.print(
                        f"[yellow]⚠  {plugin_cls.name}: Overriding existing registration[/yellow]"
                    )

            # Register with type information and distribution name
            PluginRegistry.register(
                plugin_cls, is_official=is_official, distribution_name=distribution_name
            )

            # Get plugin metadata for rich display
            pkg_meta = PluginRegistry.get_package_metadata(plugin_cls.name)
            plugin_metadata = PluginRegistry.get_metadata(plugin_cls.name)

            # Display load status with rich info
            tag = (
                "[bold green][OFFICIAL][/bold green]" if is_official else "[blue][COMMUNITY][/blue]"
            )
            category_name = CATEGORIES.get(plugin_cls.category, plugin_cls.category)

            console.print(
                f"[green]✔[/green] {tag} [cyan]{plugin_cls.name}[/cyan] "
                f"[dim]v{pkg_meta.get('version', 'unknown')}[/dim] "
                f"[dim]({category_name})[/dim]"
            )
            if pkg_meta.get("description"):
                console.print(f"  [dim]{pkg_meta['description']}[/dim]")

            loaded_count += 1

        except Exception as e:
            console.print(f"[red]✘ {ep.name}: {str(e)}[/red]")
            failed_count += 1

    # Summary
    if loaded_count > 0:
        console.print(f"\n[green]Loaded {loaded_count} plugin(s)[/green]", end="")
        if failed_count > 0:
            console.print(f" [red]({failed_count} failed)[/red]")
        else:
            console.print()

    # Initialize all loaded plugins
    PluginRegistry.load_all()

    # Register CLI commands for ALL plugins (enabled and disabled)
    # Plugins are organized by category in the help output
    for name in PluginRegistry.list_plugins():
        plugin = PluginRegistry.get(name)
        plugin_metadata = PluginRegistry.get_metadata(name)
        if plugin and plugin_metadata:
            # Determine help panel based on category
            category = plugin_metadata.plugin_class.category
            category_label = CATEGORIES.get(category, category).title()
            help_panel = f"Plugins: {category_label}"

            if get_plugin_enabled(name):
                # Enabled: register plugin's actual commands with category panel
                plugin.register_commands(app, help_panel=help_panel)
            else:
                # Disabled: register placeholder with helpful message
                _register_disabled_plugin_command(app, name, help_panel=help_panel)


def load_plugins(app: typer.Typer) -> None:
    """Loads all available plugins via entry points.

    This function discovers and loads plugins from the 'structum.plugins' entry point group.
    Official plugins (structum_*) are automatically detected and tagged.
    """
    load_entrypoint_plugins(app)
