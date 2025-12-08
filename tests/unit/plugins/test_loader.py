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

    @patch("structum.plugins.loader.entry_points")
    def test_official_plugin_detection(self, mock_eps):
        """Test automatic detection of official plugins (structum_*)."""
        from structum.plugins.sdk import PluginBase

        # Create mock official plugin (module starts with structum_)
        class OfficialPlugin(PluginBase):
            name = "official-plugin"
            version = "1.0.0"
            __module__ = "structum_official"
            def setup(self): pass
            def register_commands(self, app): pass

        mock_ep = MagicMock()
        mock_ep.name = "official-plugin"
        mock_ep.load.return_value = OfficialPlugin
        mock_eps.return_value = [mock_ep]

        app = typer.Typer()
        loader.load_entrypoint_plugins(app)

        # Verify plugin is registered
        assert "official-plugin" in PluginRegistry.list_plugins()

        # Verify it's marked as official
        metadata = PluginRegistry.get_metadata("official-plugin")
        assert metadata is not None
        assert metadata.plugin_type.value == "official"

    @patch("structum.plugins.loader.entry_points")
    def test_external_plugin_detection(self, mock_eps):
        """Test automatic detection of external plugins (not structum_*)."""
        from structum.plugins.sdk import PluginBase

        # Create mock external plugin
        class ExternalPlugin(PluginBase):
            name = "external-plugin"
            version = "1.0.0"
            __module__ = "my_plugin"
            def setup(self): pass
            def register_commands(self, app): pass

        mock_ep = MagicMock()
        mock_ep.name = "external-plugin"
        mock_ep.load.return_value = ExternalPlugin
        mock_eps.return_value = [mock_ep]

        app = typer.Typer()
        loader.load_entrypoint_plugins(app)

        # Verify plugin is registered
        assert "external-plugin" in PluginRegistry.list_plugins()

        # Verify it's marked as external
        metadata = PluginRegistry.get_metadata("external-plugin")
        assert metadata is not None
        assert metadata.plugin_type.value == "external"

    @patch("structum.plugins.loader.entry_points")
    @patch("structum.plugins.registry.console")
    def test_conflict_warning(self, mock_console, mock_eps):
        """Test conflict warning when duplicate plugin names are loaded."""
        from structum.plugins.sdk import PluginBase

        # Create two plugins with same name
        class Plugin1(PluginBase):
            name = "duplicate"
            version = "1.0.0"
            __module__ = "plugin1"
            def setup(self): pass
            def register_commands(self, app): pass

        class Plugin2(PluginBase):
            name = "duplicate"
            version = "2.0.0"
            __module__ = "plugin2"
            def setup(self): pass
            def register_commands(self, app): pass

        mock_ep1 = MagicMock()
        mock_ep1.name = "duplicate1"
        mock_ep1.load.return_value = Plugin1

        mock_ep2 = MagicMock()
        mock_ep2.name = "duplicate2"
        mock_ep2.load.return_value = Plugin2

        mock_eps.return_value = [mock_ep1, mock_ep2]

        app = typer.Typer()
        loader.load_entrypoint_plugins(app)

        # Verify conflict warning was printed (from registry.console)
        assert mock_console.print.called
        # Check if warning message contains "already registered"
        warning_found = False
        for call in mock_console.print.call_args_list:
            if "already registered" in str(call):
                warning_found = True
                break
        assert warning_found
