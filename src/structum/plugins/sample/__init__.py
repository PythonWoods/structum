# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Package."""

import typer

from ..sdk import PluginBase
from .commands import hello


class SamplePlugin(PluginBase):
    name = "sample"
    version = "1.0.0"
    description = "Example plugin demonstrating the plugin system."
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

def register(app: typer.Typer) -> None:
    """Registers the sample plugin commands with the main application."""
    app.add_typer(hello.app, name="sample")
