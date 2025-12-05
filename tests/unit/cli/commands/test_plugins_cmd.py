# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch, MagicMock
from typer.testing import CliRunner
import pytest
from structum.cli.commands.plugins import app
from structum.plugins.sdk import PluginBase

runner = CliRunner()

class TestPluginsCommand:
    """Tests for plugins CLI commands."""

    @patch("structum.cli.commands.plugins.PluginRegistry")
    @patch("structum.core.config.get_plugin_enabled")
    def test_list_plugins(self, mock_enabled, mock_registry):
        """Test listing plugins."""
        mock_registry.list_plugins.return_value = {
            "test-plugin": {
                "version": "1.0",
                "category": "utility",
                "description": "Test",
                "author": "Me"
            }
        }
        mock_enabled.return_value = True
        
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "test-plugin" in result.stdout
        assert "enabled" in result.stdout

    @patch("structum.cli.commands.plugins.PluginRegistry")
    def test_info_plugin(self, mock_registry):
        """Test getting plugin info."""
        mock_plugin = MagicMock()
        mock_plugin.name = "test-plugin"
        mock_plugin.description = "My Desc"
        mock_plugin.category = "utility"
        mock_plugin.version = "1.0"
        mock_plugin.author = "Me"
        mock_registry.get.return_value = mock_plugin
        
        result = runner.invoke(app, ["info", "test-plugin"])
        assert result.exit_code == 0
        assert "My Desc" in result.stdout

    @patch("structum.cli.commands.plugins.PluginRegistry")
    @patch("structum.core.config.set_plugin_enabled")
    def test_enable_plugin(self, mock_set, mock_registry):
        """Test enabling a plugin."""
        mock_registry.list_plugins.return_value = {"test-plugin": {}}
        
        result = runner.invoke(app, ["enable", "test-plugin"])
        assert result.exit_code == 0
        
        # Note: Depending on where set_plugin_enabled is patched (source vs destination)
        # Plugins CLI imports it locally: from structum.core.config import set_plugin_enabled
        # So we patch source: structum.core.config.set_plugin_enabled
        mock_set.assert_called_with("test-plugin", True)
        assert "enabled" in result.stdout

    def test_new_plugin_generator(self, tmp_path):
        """Test generating a new plugin."""
        # Patch the source since it is imported inside the function
        with patch("structum.plugins.skeleton.generate_plugin_skeleton") as mock_gen:
            mock_gen.return_value = tmp_path / "my-plugin"
            
            # Simulate "outside" structum project by creating a bare temp dir
            with runner.isolated_filesystem(temp_dir=tmp_path):
                result = runner.invoke(app, ["new", "my-plugin"])
                
                assert result.exit_code == 0
                mock_gen.assert_called_once()
                assert mock_gen.call_args[0][0] == "my-plugin"
                assert "Plugin skeleton created" in result.stdout

    def test_new_plugin_invalid_category(self):
        """Test invalid category."""
        result = runner.invoke(app, ["new", "my-plugin", "--category", "invalid"])
        assert result.exit_code == 0 # Typer defaults to 0 but prints error if not Exception
        assert "Invalid category" in result.stdout
