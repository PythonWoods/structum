# SPDX-License-Identifier: Apache-2.0

"""test-runner Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import main


class TestRunnerPlugin(PluginBase):
    """Test Runner plugin"""

    name = "test-runner"
    version = "0.1.0"
    category = "utility"
    description = "Test Runner plugin"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(main.app, name="test-runner")
