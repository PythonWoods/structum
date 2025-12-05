# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Documentation Management Logic.

This module contains the business logic for serving and deploying documentation.
"""

import subprocess
import sys

from rich.console import Console

console = Console()

def serve_docs(dev_addr: str) -> None:
    """
    Serves the project documentation locally using MkDocs.

    Args:
        dev_addr: Address and port to serve documentation on.
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
        sys.exit(e.returncode)
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        sys.exit(1)

def deploy_docs(message: str | None, force: bool) -> None:
    """
    Deploys the documentation to GitHub Pages.

    Args:
        message: Custom commit message for the deployment.
        force: Force push to gh-pages branch.
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
        sys.exit(e.returncode)
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        sys.exit(1)
