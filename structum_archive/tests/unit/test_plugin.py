# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Tests for structum_archive plugin."""

import pytest
import typer

from structum_archive.plugin import ArchivePlugin


class TestArchivePlugin:
    """Tests for ArchivePlugin class."""

    def test_plugin_initialization(self):
        """Test plugin can be initialized."""
        plugin = ArchivePlugin()
        assert plugin is not None
        assert plugin.name == "archive"
        assert plugin.version is not None
        assert plugin.category is not None

    def test_plugin_has_required_attributes(self):
        """Test plugin has all required attributes."""
        plugin = ArchivePlugin()
        assert hasattr(plugin, "name")
        assert hasattr(plugin, "version")
        assert hasattr(plugin, "category")
        assert hasattr(plugin, "description")

    def test_plugin_setup(self):
        """Test plugin setup method."""
        plugin = ArchivePlugin()
        plugin.setup()
        # Setup should complete without errors
        assert True

    def test_plugin_register_commands(self):
        """Test plugin command registration."""
        plugin = ArchivePlugin()
        app = typer.Typer()

        plugin.register_commands(app)

        # Commands should be registered without errors
        assert True

    def test_plugin_version_format(self):
        """Test plugin version follows semantic versioning."""
        plugin = ArchivePlugin()
        version = plugin.version
        assert isinstance(version, str)
        assert len(version) > 0
        # Should start with a digit
        assert version[0].isdigit()
