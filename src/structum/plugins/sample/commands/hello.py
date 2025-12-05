# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Commands."""

import typer

from ..core.greeting import get_greeting

app = typer.Typer(help="Example additional commands.")

@app.command("hello")
def hello(name: str = "dev") -> None:
    """Prints a friendly greeting."""
    message = get_greeting(name)
    typer.echo(message)
