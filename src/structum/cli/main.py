# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Main CLI Application.
"""

import typer
from rich.console import Console

from structum.cli.commands import archive, clean, docs, tree
from structum.plugins import load_plugins

# Initialize Typer app
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)

# Register command groups/commands


console = Console()

# Load plugins
load_plugins(app)

# Register sub-apps
app.add_typer(tree.app)
app.add_typer(archive.app)
app.add_typer(clean.app)
app.add_typer(docs.app, name="docs") # docs serve, docs deploy

def run() -> None:
    app()
