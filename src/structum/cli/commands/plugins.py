# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Management CLI Commands."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import CATEGORIES

app = typer.Typer(
    help="Manage plugins.",
    no_args_is_help=True
)
console = Console()


@app.command("list")
def list_plugins(
    show_dev: bool = typer.Option(
        False,
        "--show-dev",
        help="Show plugins in development mode (.dev marker)",
    ),
) -> None:
    """List all installed plugins."""
    from structum.core.config import get_plugin_enabled
    from structum.plugins.loader import get_dev_plugins

    plugins = PluginRegistry.list_plugins()
    dev_plugins = get_dev_plugins() if show_dev else {}

    if not plugins and not dev_plugins:
        console.print("[yellow]No plugins found.[/yellow]")
        return

    title = "Installed Plugins" + (" (including dev mode)" if show_dev else "")
    table = Table(title=title)
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Version", style="green")
    table.add_column("Status")
    table.add_column("Description")

    # Add production plugins
    for name, info in plugins.items():
        enabled = get_plugin_enabled(name)
        status = "[green]enabled[/green]" if enabled else "[red]disabled[/red]"
        table.add_row(
            name,
            info["category"],
            info["version"],
            status,
            info["description"],
        )

    # Add dev mode plugins if requested
    if show_dev:
        for name, info in dev_plugins.items():
            plugin_class = info.get("plugin_class")
            if plugin_class:
                table.add_row(
                    f"{name}*",
                    getattr(plugin_class, "category", "unknown"),
                    getattr(plugin_class, "version", "0.1.0"),
                    "[dim yellow][DEV MODE][/dim yellow]",
                    getattr(plugin_class, "description", "Development plugin"),
                )
            else:
                # Plugin with errors
                table.add_row(
                    f"{name}*",
                    "unknown",
                    "unknown",
                    "[red][ERROR][/red]",
                    f"Failed to load: {info.get('error', 'Unknown error')}",
                )

    console.print(table)

    if show_dev and dev_plugins:
        console.print(
            "\n[dim]* Plugins in development mode (.dev marker present)[/dim]"
        )


@app.command("info")
def plugin_info(name: str) -> None:
    """Show detailed information about a plugin."""
    plugin = PluginRegistry.get(name)

    if not plugin:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    console.print(f"[bold cyan]Plugin:[/bold cyan] {plugin.name}")
    console.print(f"[bold yellow]Category:[/bold yellow] {plugin.category}")
    console.print(f"[bold green]Version:[/bold green] {plugin.version}")
    console.print(f"[bold]Author:[/bold] {plugin.author}")
    console.print(f"[bold]Description:[/bold] {plugin.description}")


@app.command("enable")
def enable_plugin(name: str) -> None:
    """Enable a plugin."""
    from structum.core.config import set_plugin_enabled

    plugins = PluginRegistry.list_plugins()
    if name not in plugins:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    set_plugin_enabled(name, True)
    console.print(f"[green]✔ Plugin '{name}' enabled.[/green]")


@app.command("disable")
def disable_plugin(name: str) -> None:
    """Disable a plugin."""
    from structum.core.config import set_plugin_enabled

    plugins = PluginRegistry.list_plugins()
    if name not in plugins:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    set_plugin_enabled(name, False)
    console.print(f"[yellow]⚠ Plugin '{name}' disabled.[/yellow]")


@app.command("new")
def new_plugin(
    name: str = typer.Argument(..., help="Plugin name (kebab-case, e.g. my-plugin)"),
    output: Path = typer.Option(
        None, "--output", "-o", help="Output directory (default: auto-detect)"
    ),
    category: str = typer.Option(
        "utility",
        "--category",
        "-c",
        help=f"Plugin category ({', '.join(CATEGORIES.keys())})",
    ),
) -> None:
    """Generate a new plugin skeleton."""
    from structum.plugins.skeleton import generate_plugin_skeleton

    if category not in CATEGORIES:
        console.print(
            f"[red]Invalid category '{category}'. "
            f"Valid: {', '.join(CATEGORIES.keys())}[/red]"
        )
        return

    # Smart default: detect if we're in structum project
    is_structum_project = (Path.cwd() / "src" / "structum" / "plugins").exists()

    if output is None:
        if is_structum_project:
            output = Path.cwd() / "src" / "structum" / "plugins"
        else:
            output = Path.cwd()

    try:
        plugin_dir = generate_plugin_skeleton(name, output, category)
        console.print(f"[green]✔ Plugin skeleton created at:[/green] {plugin_dir}")
        
        # Generate proper class name (same logic as skeleton.py)
        class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"

        if is_structum_project and output == Path.cwd() / "src" / "structum" / "plugins":
            # Builtin plugin instructions
            console.print("\n[bold]Next steps (builtin plugin):[/bold]")
            console.print(f"  1. Implement your plugin logic in [cyan]{plugin_dir}[/cyan]")
            console.print(f"  2. View dev plugin with [cyan]structum plugins list --show-dev[/cyan]")
            console.print(f"  3. When ready, remove dev marker: [cyan]rm {plugin_dir}/.dev[/cyan]")
            console.print(f"  4. Test your plugin with [cyan]structum {name} run[/cyan]")
            console.print("\n[dim yellow]ℹ Plugin created in development mode (.dev marker present)[/dim yellow]")
            console.print("[dim]The plugin will not be registered until .dev file is removed.[/dim]")
            console.print("[dim]See docs/development/plugins.md for details.[/dim]")
        else:
            # External plugin instructions
            console.print("\n[bold]Next steps (external plugin):[/bold]")
            console.print("  1. Create package structure with [cyan]pyproject.toml[/cyan]")
            console.print("  2. Add entry point:")
            console.print('     [yellow][project.entry-points."structum.plugins"][/yellow]')
            console.print(f'     [yellow]{name} = "{name.replace("-", "_")}:{class_name}"[/yellow]')
            console.print("  3. Install with [cyan]pip install -e .[/cyan]")
            console.print("\n[dim]See docs/development/plugins.md for details.[/dim]")
    except Exception as e:
        console.print(f"[red]✘ Error creating plugin:[/red] {e}")
