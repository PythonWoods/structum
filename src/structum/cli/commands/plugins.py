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
def list_plugins() -> None:
    """List all installed plugins (official and external)."""
    from structum.core.config import get_plugin_enabled

    plugins = PluginRegistry.list_plugins_detailed()

    if not plugins:
        console.print("[yellow]No plugins found.[/yellow]")
        console.print("\n[dim]Install plugins with:[/dim] [cyan]pip install structum-<plugin-name>[/cyan]")
        return

    table = Table(title="Installed Plugins")
    table.add_column("Name", style="cyan")
    table.add_column("Type", style="magenta")
    table.add_column("Category", style="yellow")
    table.add_column("Version", style="green")
    table.add_column("Status")
    table.add_column("Description")

    # Add all plugins with type information
    for name, info in plugins.items():
        enabled = get_plugin_enabled(name)
        status = "[green]enabled[/green]" if enabled else "[red]disabled[/red]"

        # Format type with visual tag
        plugin_type = info["type"]
        type_display = (
            "[bold green][OFFICIAL][/bold green]"
            if plugin_type == "official"
            else "[blue][EXTERNAL][/blue]"
        )

        table.add_row(
            name,
            type_display,
            info["category"],
            info["version"],
            status,
            info["description"],
        )

    console.print(table)

    # Show legend
    console.print("\n[dim]Legend:[/dim]")
    console.print("  [bold green][OFFICIAL][/bold green] - Official plugins maintained by PythonWoods (structum_*)")
    console.print("  [blue][EXTERNAL][/blue] - Third-party plugins")


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
    if output is None:
        output = Path.cwd()

    try:
        plugin_dir = generate_plugin_skeleton(name, output, category)
        console.print(f"[green]✔ Plugin skeleton created at:[/green] {plugin_dir}")

        # Generate proper class name (same logic as skeleton.py)
        class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"

        # External plugin instructions
        console.print("\n[bold]Next steps (external plugin):[/bold]")
        console.print("  1. Create package structure with [cyan]pyproject.toml[/cyan]")
        console.print("  2. Add entry point:")
        console.print('     [yellow][project.entry-points."structum.plugins"][/yellow]')
        console.print(f'     [yellow]{name} = "{name.replace("-", "_")}:{class_name}"[/yellow]')
        console.print("  3. Install with [cyan]pip install -e .[/cyan]")
        console.print("  4. Test your plugin with [cyan]structum {name} info[/cyan]")
        console.print("\n[dim]See docs/development/plugins.md for details.[/dim]")
    except Exception as e:
        console.print(f"[red]✘ Error creating plugin:[/red] {e}")
