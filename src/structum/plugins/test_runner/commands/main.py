# SPDX-License-Identifier: Apache-2.0

"""test-runner Plugin Commands."""

from pathlib import Path

import typer

from ..core.logic import process

app = typer.Typer(
    help="Test Runner plugin",
    no_args_is_help=True
)


@app.command("run")
def run_command(
    path: Path = typer.Argument(
        Path("."),
        help="Path to process",
        exists=True,
        resolve_path=True,
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path (optional)",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Preview changes without applying them",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    ),
) -> None:
    """Execute the plugin's main functionality.

    This is the primary command for the test-runner plugin.
    Customize this implementation to match your plugin's purpose.
    """
    result = process(
        path=path,
        output=output,
        dry_run=dry_run,
        verbose=verbose,
    )

    if verbose:
        typer.echo(f"[test-runner] Processing completed")

    typer.echo(result)
