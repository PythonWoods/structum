# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample plugin for Structum.

This module demonstrates how to create a built-in plugin for Structum.
It registers a 'sample' command group with a 'hello' command.
"""

import typer


def register(app: typer.Typer) -> None:
    """Registers the sample plugin commands with the main application."""
    plugin_app = typer.Typer(help="Example additional commands.")
    app.add_typer(plugin_app, name="sample")

    @plugin_app.command("hello")
    def hello(name: str = "dev") -> None:
        """Prints a friendly greeting."""
        typer.echo(f"👋 Hello, {name}! This command was loaded as a plugin.")
