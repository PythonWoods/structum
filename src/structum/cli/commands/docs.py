# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Docs Commands.
"""

import typer

from structum.core.docs import deploy_docs, serve_docs

app = typer.Typer()

@app.command(name="serve")
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
        structum docs serve
        structum docs serve --dev-addr 0.0.0.0:8080
    """
    serve_docs(dev_addr=dev_addr)


@app.command(name="deploy")
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
        structum docs deploy
        structum docs deploy --message "Update docs for v1.2.0"
        structum docs deploy --force
    """
    deploy_docs(message=message, force=force)
