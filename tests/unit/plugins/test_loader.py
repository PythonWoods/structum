# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import MagicMock, patch
import pytest
import typer
from structum.plugins import loader
from structum.plugins.registry import PluginRegistry

class TestLoader:
    """Tests for plugin loading."""

    @pytest.fixture(autouse=True)
    def clean_registry(self):
        PluginRegistry.clear()
        yield
        PluginRegistry.clear()

    def test_load_builtin_plugins(self):
        """Test loading built-in plugins."""
        app = typer.Typer()
        
        # We assume 'sample' is the builtin plugin
        # We need to mock get_plugin_enabled if we check command registration
        # But load_builtin_plugins registers and loads it
        
        loader.load_builtin_plugins(app)
        
        assert "sample" in PluginRegistry.list_plugins()
        # Check if loaded
        assert PluginRegistry.get("sample") is not None

    @patch("structum.plugins.loader.entry_points")
    def test_load_entrypoint_plugins_none(self, mock_eps):
        """Test loading when no entry points exist."""
        mock_eps.return_value = []
        app = typer.Typer()
        
        loader.load_entrypoint_plugins(app)
        
        # Should be empty (assuming no builtins loaded)
        assert len(PluginRegistry.list_plugins()) == 0

    @patch("structum.plugins.loader.entry_points")
    def test_load_entrypoint_plugins_valid(self, mock_eps):
        """Test loading valid entry point plugin."""
        # Mock entry point
        mock_ep = MagicMock()
        mock_ep.name = "external-plugin"
        # Create a dummy plugin class
        from structum.plugins.sdk import PluginBase
        class ExternalPlugin(PluginBase):
            name = "external-plugin"
            version = "0.0.1"
            def setup(self): pass
            def register_commands(self, app): pass
            
        mock_ep.load.return_value = ExternalPlugin
        mock_eps.return_value = [mock_ep]
        
        app = typer.Typer()
        loader.load_entrypoint_plugins(app)
        
        assert "external-plugin" in PluginRegistry.list_plugins()
        assert PluginRegistry.get("external-plugin") is not None
