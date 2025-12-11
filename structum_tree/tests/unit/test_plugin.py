# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Tests for structum_tree plugin."""

import pytest
import typer

from structum_tree.plugin import TreePlugin


class TestTreePlugin:
    """Tests for TreePlugin class."""

    def test_plugin_initialization(self):
        """Test plugin can be initialized."""
        plugin = TreePlugin()
        assert plugin is not None
        assert plugin.name == "tree"
        assert plugin.version is not None
        assert plugin.category == "utility"

    def test_plugin_setup(self):
        """Test plugin setup method."""
        plugin = TreePlugin()
        plugin.setup()
        # Setup should complete without errors
        assert True

    def test_plugin_register_commands(self):
        """Test plugin command registration."""
        plugin = TreePlugin()
        app = typer.Typer()

        plugin.register_commands(app)

        # Commands should be registered without errors
        assert True

    def test_plugin_attributes(self):
        """Test plugin has required attributes."""
        plugin = TreePlugin()
        assert hasattr(plugin, "name")
        assert hasattr(plugin, "version")
        assert hasattr(plugin, "category")
        assert hasattr(plugin, "setup")
        assert hasattr(plugin, "register_commands")
