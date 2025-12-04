# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import hello


class SamplePlugin(PluginBase):
    """Example plugin demonstrating the plugin system."""

    name = "sample"
    version = "1.0.0"
    description = "Example plugin demonstrating the plugin system."
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(hello.app, name="sample")
