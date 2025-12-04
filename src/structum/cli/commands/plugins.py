# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Management CLI Commands."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import CATEGORIES

app = typer.Typer(help="Manage plugins.")
console = Console()


@app.command("list")
def list_plugins() -> None:
    """List all installed plugins."""
    from structum.core.config import get_plugin_enabled

    plugins = PluginRegistry.list_plugins()

    if not plugins:
        console.print("[yellow]No plugins found.[/yellow]")
        return

    table = Table(title="Installed Plugins")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Version", style="green")
    table.add_column("Status")
    table.add_column("Description")

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

    console.print(table)


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
        Path.cwd(), "--output", "-o", help="Output directory"
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

    try:
        plugin_dir = generate_plugin_skeleton(name, output, category)
        console.print(f"[green]✔ Plugin skeleton created at:[/green] {plugin_dir}")
        console.print("\n[bold]Next steps:[/bold]")
        console.print(f"  1. cd {plugin_dir}")
        console.print("  2. Implement your plugin logic")
        console.print("  3. Register with entry points or add to builtins")
    except Exception as e:
        console.print(f"[red]✘ Error creating plugin:[/red] {e}")
