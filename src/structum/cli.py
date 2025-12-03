# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
CLI Entry Point.

This module defines the main command-line interface using Typer.
It acts as the bridge between the user input and the core logic.
"""

import subprocess
import sys
from pathlib import Path

import typer
from rich.console import Console

from structum.core.archive import create_archive
from structum.core.clean import clean_pycache
from structum.core.tree import print_tree
from structum.plugins import load_plugins

# Initialize Typer app and Rich console
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)
console = Console()

# Load plugins
load_plugins(app)

@app.command(name="tree")
def tree_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to analyze.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g. -e py -e md)."
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude (e.g. -i .git -i node_modules)."
    ),
    max_depth: int | None = typer.Option(
        None,
        "--depth", "-d",
        help="Maximum depth of the tree traversal."
    ),
    show_hidden: bool = typer.Option(
        False,
        "--hidden",
        help="Show hidden files and directories (starting with '.')."
    ),
    ignore_empty: bool = typer.Option(
        False,
        "--no-empty",
        help="Hide directories that do not contain visible files."
    ),
    theme: str = typer.Option(
        "emoji",
        "--theme", "-t",
        help="Icon theme to use: 'nerd', 'emoji', 'ascii', 'none'."
    ),
) -> None:
    """
    Visualizes the directory structure of the specified path.

    \b
    Examples:
        structum tree . --theme nerd
        structum tree src --depth 2 --ext py
    """

    # Note: CLI flag is --hidden (show_hidden=True),
    # but core logic expects ignore_hidden (True by default).
    # We invert the boolean here.
    ignore_hidden_logic = not show_hidden

    print_tree(
        directory=directory,
        extensions=extensions,
        ignore_dirs=ignore_dirs,
        max_depth=max_depth,
        ignore_hidden=ignore_hidden_logic,
        ignore_empty=ignore_empty,
        theme=theme
    )


@app.command(name="archive")
def archive_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to archive.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    output: Path = typer.Option(
        "archive.md",
        "--output", "-o",
        help="Output file path (or directory if split mode is enabled)."
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g. -e py -e md)."
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude."
    ),
    split_by_folder: bool = typer.Option(
        False,
        "--split-folder",
        help="Create a separate archive for each folder."
    ),
    split_by_type: bool = typer.Option(
        False,
        "--split-type",
        help="Create a separate archive for each file extension."
    ),
    toc: bool = typer.Option(
        True,
        "--toc/--no-toc",
        help="Include a Table of Contents."
    ),
    tree: bool = typer.Option(
        True,
        "--tree/--no-tree",
        help="Include a directory tree structure."
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Enable verbose output."
    ),
) -> None:
    """
    Archives source code into Markdown files.

    \b
    Features:
    * Collects files by extension
    * Generates Table of Contents (ToC)
    * Includes ASCII directory tree
    * Supports splitting by folder or file type

    \b
    Examples:
        structum archive . --output code.md --ext py
        structum archive src --split-folder --output docs/
    """
    try:
        create_archive(
            root=directory,
            output=output,
            extensions=extensions,
            ignore_dirs=ignore_dirs,
            split_by_folder=split_by_folder,
            split_by_type=split_by_type,
            toc=toc,
            include_tree=tree,
            verbose=verbose
        )
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1) from None


@app.command(name="clean")
def clean_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to clean.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Enable verbose output."
    ),
) -> None:
    """
    Recursively removes all __pycache__ directories.

    \b
    Examples:
        structum clean .
        structum clean src --quiet
    """
    clean_pycache(directory, verbose=verbose)


@app.command(name="docs-serve")
def docs_serve_command(
    dev_addr: str = typer.Option(
        "127.0.0.1:8000",
        "--dev-addr", "-a",
        help="Address and port to serve documentation on."
    ),
) -> None:
    """
    Serves the project documentation locally using MkDocs.

    \b
    This command starts a local development server that watches for changes
    and automatically rebuilds the documentation.

    \b
    Examples:
        structum docs-serve
        structum docs-serve --dev-addr 0.0.0.0:8080
    """
    try:
        console.print("[bold blue]Starting documentation server...[/bold blue]")
        result = subprocess.run(
            ["mkdocs", "serve", "--dev-addr", dev_addr],
            check=True
        )
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        console.print("[bold red]Error:[/bold red] Failed to start documentation server.")
        console.print("[dim]Make sure mkdocs and mkdocs-material are installed: pip install mkdocs mkdocs-material[/dim]")
        raise typer.Exit(code=e.returncode) from None
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        raise typer.Exit(code=1) from None


@app.command(name="docs-deploy")
def docs_deploy_command(
    message: str | None = typer.Option(
        None,
        "--message", "-m",
        help="Custom commit message for the deployment."
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force push to gh-pages branch (use with caution)."
    ),
) -> None:
    """
    Deploys the documentation to GitHub Pages.

    \b
    This command builds the documentation and pushes it to the gh-pages branch
    of your repository. Requires proper git configuration and write access.

    \b
    Examples:
        structum docs-deploy
        structum docs-deploy --message "Update docs for v1.2.0"
        structum docs-deploy --force
    """
    try:
        console.print("[bold blue]Deploying documentation to GitHub Pages...[/bold blue]")
        cmd = ["mkdocs", "gh-deploy"]

        if message:
            cmd.extend(["--message", message])

        if force:
            cmd.append("--force")

        result = subprocess.run(cmd, check=True)
        console.print("[bold green]✓[/bold green] Documentation deployed successfully!")
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        console.print("[bold red]Error:[/bold red] Failed to deploy documentation.")
        console.print("[dim]Make sure you have push access to the repository and gh-pages branch exists.[/dim]")
        raise typer.Exit(code=e.returncode) from None
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        raise typer.Exit(code=1) from None


if __name__ == "__main__":
    app()
