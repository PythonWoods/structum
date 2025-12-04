# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Package."""

import typer

from .commands import hello


def register(app: typer.Typer) -> None:
    """Registers the sample plugin commands with the main application."""
    app.add_typer(hello.app, name="sample")
