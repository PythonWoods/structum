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
        console.print(f"[green]✔ Plugin package created at:[/green] {plugin_dir}")
        console.print(f"[dim]   Package name:[/dim] [cyan]structum-plugin-{name}[/cyan]")

        # Show package structure
        console.print("\n[bold]Generated files:[/bold]")
        console.print("  📄 [cyan]pyproject.toml[/cyan] - Package configuration with entry point")
        console.print("  📄 [cyan]README.md[/cyan] - Documentation template")
        console.print("  📄 [cyan].gitignore[/cyan] - Git ignore rules")
        console.print(f"  📁 [cyan]src/{name.replace('-', '_')}/[/cyan] - Plugin source code")

        # Installation instructions
        console.print("\n[bold]Next steps:[/bold]")
        console.print(f"  1. [yellow]cd {plugin_dir.name}[/yellow]")
        console.print("  2. [yellow]pip install -e .[/yellow]  [dim](install in development mode)[/dim]")
        console.print(f"  3. [yellow]structum {name} info[/yellow]  [dim](test your plugin)[/dim]")
        console.print("  4. [yellow]structum plugins list[/yellow]  [dim](verify installation)[/dim]")

        console.print("\n[dim]💡 Edit src/{}/commands/main.py to add your commands[/dim]".format(name.replace("-", "_")))
        console.print("[dim]   See README.md for detailed instructions[/dim]")
    except Exception as e:
        console.print(f"[red]✘ Error creating plugin:[/red] {e}")
