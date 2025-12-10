# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin management plugin for Structum."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table
from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import CATEGORIES, PluginBase
from structum.plugins.skeleton import generate_plugin_skeleton

from structum_plugins.__about__ import __version__

console = Console()


class PluginsPlugin(PluginBase):
    """Official plugin management plugin for Structum."""

    name = "plugins"
    version = __version__
    category = "utility"
    description = "Manage Structum plugins"
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize the plugin."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register the plugins command group."""
        plugins_app = typer.Typer(
            help="Manage plugins.",
            no_args_is_help=True,
            rich_help_panel=help_panel
        )

        @plugins_app.command("list")
        def list_plugins() -> None:
            """List all installed plugins (official and community)."""
            from structum.config.manager import get_plugin_enabled

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
                    else "[blue][COMMUNITY][/blue]"
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
            console.print("  [blue][COMMUNITY][/blue] - Community plugins")

        @plugins_app.command("info")
        def plugin_info(name: str) -> None:
            """Show detailed information about a plugin."""
            plugin = PluginRegistry.get(name)

            if not plugin:
                console.print(f"[red]Plugin '{name}' not found.[/red]")
                return

            # Get metadata from package (pyproject.toml)
            pkg_meta = PluginRegistry.get_package_metadata(name)
            plugin_metadata = PluginRegistry.get_metadata(name)

            console.print(f"[bold cyan]Plugin:[/bold cyan] {plugin.name}")
            console.print(f"[bold yellow]Category:[/bold yellow] {plugin.category}")
            console.print(f"[bold green]Version:[/bold green] {pkg_meta.get('version', 'unknown')}")
            console.print(f"[bold]Author:[/bold] {pkg_meta.get('author', 'unknown')}")
            if pkg_meta.get('author_email'):
                console.print(f"[bold]Email:[/bold] {pkg_meta['author_email']}")
            console.print(f"[bold]Description:[/bold] {pkg_meta.get('description', '')}")
            if pkg_meta.get('license'):
                console.print(f"[bold]License:[/bold] {pkg_meta['license']}")

            # Show type and module info
            if plugin_metadata:
                plugin_type = "[bold green][OFFICIAL][/bold green]" if plugin_metadata.plugin_type.value == "official" else "[blue][COMMUNITY][/blue]"
                console.print(f"[bold]Type:[/bold] {plugin_type}")
                console.print(f"[bold]Module:[/bold] {plugin_metadata.module_path}")
                if plugin_metadata.distribution_name:
                    console.print(f"[bold]Package:[/bold] {plugin_metadata.distribution_name}")

        @plugins_app.command("enable")
        def enable_plugin(name: str) -> None:
            """Enable a plugin."""
            from structum.config.manager import set_plugin_enabled

            plugins = PluginRegistry.list_plugins()
            if name not in plugins:
                console.print(f"[red]Plugin '{name}' not found.[/red]")
                return

            set_plugin_enabled(name, True)
            console.print(f"[green]✔ Plugin '{name}' enabled.[/green]")

        @plugins_app.command("disable")
        def disable_plugin(name: str) -> None:
            """Disable a plugin."""
            from structum.config.manager import set_plugin_enabled

            plugins = PluginRegistry.list_plugins()
            if name not in plugins:
                console.print(f"[red]Plugin '{name}' not found.[/red]")
                return

            set_plugin_enabled(name, False)
            console.print(f"[yellow]⚠ Plugin '{name}' disabled.[/yellow]")

        @plugins_app.command("new")
        def new_plugin(
            name: str = typer.Argument(..., help="Plugin name (kebab-case, e.g. my-plugin)"),
            output: Path = typer.Option(
                ..., "--output", "-o", help="Output directory where the plugin will be created"
            ),
            category: str = typer.Option(
                "utility",
                "--category",
                "-c",
                help=f"Plugin category ({', '.join(CATEGORIES.keys())})",
            ),
        ) -> None:
            """Generate a new plugin skeleton with interactive prompts."""
            if category not in CATEGORIES:
                console.print(
                    f"[red]Invalid category '{category}'. "
                    f"Valid: {', '.join(CATEGORIES.keys())}[/red]"
                )
                return

            # Interactive prompts (like npm init)
            console.print(f"\n[bold cyan]Creating plugin: {name}[/bold cyan]")
            console.print("[dim]Press Enter to use default values shown in brackets.[/dim]\n")

            try:
                # Collect metadata interactively
                author_name = typer.prompt("Author name", default="Your Name")
                author_email = typer.prompt("Author email", default="your.email@example.com")

                default_description = f"{name.replace('-', ' ').title()} plugin for Structum"
                description = typer.prompt("Description", default=default_description)

                version = typer.prompt("Version", default="0.1.0")
                license_type = typer.prompt("License", default="Apache-2.0")

                # Generate plugin with collected metadata
                plugin_dir = generate_plugin_skeleton(
                    name=name,
                    output_dir=output,
                    category=category,
                    author_name=author_name,
                    author_email=author_email,
                    description=description,
                    version=version,
                    license_type=license_type,
                )

                console.print(f"\n[green]✔ Plugin package created at:[/green] {plugin_dir}")
                console.print(f"[dim]   Package name:[/dim] [cyan]structum-plugin-{name}[/cyan]")
                console.print(f"[dim]   Author:[/dim] [cyan]{author_name} <{author_email}>[/cyan]")

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

        app.add_typer(plugins_app, name="plugins")
