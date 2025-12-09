# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Main CLI Application.
"""

import sys

import typer
from rich.console import Console

from structum.cli.commands import archive, clean, docs, plugins, tree, info
from structum.plugins import load_plugins
from structum.plugins.registry import PluginRegistry
from structum.core.config import get_plugin_enabled

# Initialize Typer app
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)

# Register commands


console = Console()

# Load plugins
load_plugins(app)

# Register commands
# Single commands use app.command()
app.command(name="tree")(tree.tree_command)
app.command(name="archive")(archive.archive_command)
app.command(name="clean")(clean.clean_command)
app.command(name="version")(info.version_command)
app.command(name="info")(info.info_command)

# Command groups use add_typer()
app.add_typer(docs.app, name="docs")  # docs serve, docs deploy
app.add_typer(plugins.app, name="plugins")  # plugins list, info, enable, disable, new

def run() -> None:
    """Run the CLI application with enhanced error handling for disabled plugins."""
    # Check if first argument corresponds to a disabled plugin
    if len(sys.argv) > 1:
        command_name = sys.argv[1]

        # Skip built-in commands and flags
        if not command_name.startswith("-"):
            # Check if this matches a registered but disabled plugin
            if command_name in PluginRegistry.list_plugins():
                if not get_plugin_enabled(command_name):
                    console.print(
                        f"[yellow]⚠ Plugin '{command_name}' is disabled.[/yellow]\n"
                        f"[dim]Enable it with:[/dim] [cyan]structum plugins enable {command_name}[/cyan]"
                    )
                    sys.exit(1)

    app()
