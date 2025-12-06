# SPDX-License-Identifier: Apache-2.0

"""test-greeter Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import main


class TestGreeterPlugin(PluginBase):
    """Test Greeter plugin"""

    name = "test-greeter"
    version = "0.1.0"
    category = "utility"
    description = "Test Greeter plugin"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(main.app, name="test-greeter")
