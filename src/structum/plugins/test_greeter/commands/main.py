# SPDX-License-Identifier: Apache-2.0

"""test-greeter Plugin Commands."""

import typer

app = typer.Typer(
    help="Test Greeter plugin",
    no_args_is_help=True
)


@app.command("hello")
def hello(name: str = "world") -> None:
    """Say hello."""
    typer.echo(f"Hello, {name}!")
