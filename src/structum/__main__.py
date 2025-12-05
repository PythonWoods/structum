"""Entry point for Structum.

This module allows running Structum directly using:

    python -m structum

invoking the Typer application defined in :mod:`structum.cli`.
"""

from __future__ import annotations

from .cli.main import app


def main() -> None:
    """Executes the main Typer application."""
    app()


if __name__ == "__main__":
    main()
