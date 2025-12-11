# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Minimal CLI bootstrap for Structum Core.

This module provides the minimal entry point for the Structum framework.
All actual functionality is provided by plugins.
"""

import time

import typer
from rich.console import Console

from structum.__about__ import __version__
from structum.monitoring.metrics import get_metrics
from structum.plugins import load_plugins

console = Console()


def create_app(
    name: str = "structum",
    description: str = "Enterprise Plugin Framework",
    version: str | None = None,
) -> typer.Typer:
    """Create a Structum CLI application.

    This function creates a minimal Typer application and loads all registered plugins.
    Plugins provide all the actual functionality.

    Args:
        name: Application name
        description: Application description
        version: Application version (defaults to core version)

    Returns:
        Configured Typer application

    Example:
        >>> app = create_app(name="myapp", description="My Plugin App")
        >>> app()
    """
    app_version = version or __version__

    app = typer.Typer(
        name=name,
        help=description,
        add_completion=False,
        no_args_is_help=True,
        rich_markup_mode="rich",
    )

    # Built-in version command
    @app.command(name="version")
    def version_command() -> None:
        """Show application version."""
        console.print(f"{name} [cyan]v{app_version}[/cyan]")
        console.print(f"[dim]Core:[/dim] structum-core v{__version__}")

    # Built-in info command
    @app.command(name="info")
    def info_command() -> None:
        """Show application information."""
        from structum.plugins.registry import PluginRegistry

        console.print(f"\n[bold cyan]{name}[/bold cyan] [dim]v{app_version}[/dim]")
        console.print(f"[dim]Built on:[/dim] structum-core v{__version__}")
        console.print(f"\n[dim]{description}[/dim]")

        # Plugin summary
        plugins = PluginRegistry.list_plugins()
        if plugins:
            console.print(f"\n[bold]Installed Plugins:[/bold] {len(plugins)}")

        # Metrics summary (if available)
        metrics = get_metrics()
        summary = metrics.get_summary()
        if summary["counters"]:
            console.print("\n[bold]Metrics:[/bold]")
            for metric_name, value in summary["counters"].items():
                console.print(f"  {metric_name}: {value}")

    # Load plugins and register their commands
    start_time = time.time()
    load_plugins(app)
    load_time = time.time() - start_time

    # Record metrics
    metrics = get_metrics()
    metrics.record_time("core.startup_time", load_time)
    metrics.increment_counter("core.startups")

    return app


def main() -> None:
    """Main entry point for structum-core CLI.

    This is the default entry point when running 'structum' command.
    It creates an application with default settings and loads all plugins.
    """
    app = create_app(
        name="structum",
        description="Enterprise Plugin Framework - Core Only",
        version=__version__,
    )
    app()


if __name__ == "__main__":
    main()
