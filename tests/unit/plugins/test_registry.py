# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import PluginBase
import typer

class ValidPlugin(PluginBase):
    name = "valid-plugin"
    version = "1.0.0"
    category = "utility"
    description = "A valid plugin"
    author = "Test"
    
    def setup(self): pass
    def register_commands(self, app): pass

class InvalidPluginNoName(PluginBase):
    version = "1.0.0"
    def setup(self): pass
    def register_commands(self, app): pass

class TestPluginRegistry:
    """Tests for PluginRegistry."""

    @pytest.fixture(autouse=True)
    def clean_registry(self):
        """Clean registry before each test."""
        PluginRegistry.clear()
        yield
        PluginRegistry.clear()

    def test_register_valid_plugin(self):
        """Test registering a valid plugin."""
        PluginRegistry.register(ValidPlugin)

        # Check it's registered
        assert "valid-plugin" in PluginRegistry.list_plugins()

        # Check metadata
        metadata = PluginRegistry.get_metadata("valid-plugin")
        assert metadata is not None
        assert metadata.plugin_class == ValidPlugin

    def test_register_invalid_plugin_type(self):
        """Test registering something that isn't a PluginBase."""
        with pytest.raises(TypeError):
            PluginRegistry.register(object) # type: ignore

    def test_register_invalid_plugin_missing_attr(self):
        """Test registering plugin with missing attributes."""
        with pytest.raises(ValueError, match="must have a 'name'"):
            PluginRegistry.register(InvalidPluginNoName)

    def test_get_plugin(self):
        """Test getting plugin instance."""
        PluginRegistry.register(ValidPlugin)
        
        # Before loading, get returns None
        assert PluginRegistry.get("valid-plugin") is None
        
        # Load all
        PluginRegistry.load_all()
        
        # Now get returns instance
        instance = PluginRegistry.get("valid-plugin")
        assert instance is not None
        assert isinstance(instance, ValidPlugin)

    def test_list_by_category(self):
        """Test listing plugins by category."""
        PluginRegistry.register(ValidPlugin)

        categories = PluginRegistry.list_by_category()
        assert "utility" in categories
        assert "valid-plugin" in categories["utility"]

    def test_plugin_type_enum(self):
        """Test PluginType enum values."""
        from structum.plugins.registry import PluginType

        assert PluginType.OFFICIAL.value == "official"
        assert PluginType.COMMUNITY.value == "community"

    def test_plugin_metadata_dataclass(self):
        """Test PluginMetadata dataclass."""
        from structum.plugins.registry import PluginMetadata, PluginType

        metadata = PluginMetadata(
            plugin_class=ValidPlugin,
            plugin_type=PluginType.COMMUNITY,
            module_path="test_module",
            source="entrypoint:test",
            distribution_name="structum-plugin-test"
        )

        assert metadata.plugin_class == ValidPlugin
        assert metadata.plugin_type == PluginType.COMMUNITY
        assert metadata.module_path == "test_module"
        assert metadata.source == "entrypoint:test"
        assert metadata.distribution_name == "structum-plugin-test"

    def test_register_as_official(self):
        """Test registering plugin as official."""
        PluginRegistry.register(ValidPlugin, is_official=True)

        metadata = PluginRegistry.get_metadata("valid-plugin")
        assert metadata is not None
        assert metadata.plugin_type.value == "official"

    def test_register_as_community(self):
        """Test registering plugin as community (default)."""
        PluginRegistry.register(ValidPlugin, is_official=False)

        metadata = PluginRegistry.get_metadata("valid-plugin")
        assert metadata is not None
        assert metadata.plugin_type.value == "community"

    def test_list_by_type(self):
        """Test listing plugins by type."""
        # Create another plugin for testing
        class OfficialPlugin(PluginBase):
            name = "official-plugin"
            version = "1.0.0"
            category = "utility"
            def setup(self): pass
            def register_commands(self, app): pass

        PluginRegistry.register(ValidPlugin, is_official=False)
        PluginRegistry.register(OfficialPlugin, is_official=True)

        by_type = PluginRegistry.list_by_type()

        assert "official" in by_type
        assert "community" in by_type
        assert "official-plugin" in by_type["official"]
        assert "valid-plugin" in by_type["community"]

    def test_list_plugins_detailed(self):
        """Test listing plugins with detailed metadata."""
        PluginRegistry.register(ValidPlugin, is_official=True)

        detailed = PluginRegistry.list_plugins_detailed()

        assert "valid-plugin" in detailed
        plugin_info = detailed["valid-plugin"]
        assert plugin_info["version"] == "1.0.0"
        assert plugin_info["category"] == "utility"
        assert plugin_info["description"] == "A valid plugin"
        assert plugin_info["author"] == "Test"
        assert plugin_info["type"] == "official"
        assert "module" in plugin_info

    def test_get_metadata_nonexistent(self):
        """Test getting metadata for non-existent plugin."""
        metadata = PluginRegistry.get_metadata("nonexistent")
        assert metadata is None

    def test_conflict_detection(self):
        """Test conflict detection when registering duplicate names."""
        from unittest.mock import patch

        # Register first plugin
        PluginRegistry.register(ValidPlugin, is_official=False)

        # Try to register another with same name (should override with warning)
        class DuplicatePlugin(PluginBase):
            name = "valid-plugin"  # Same name
            version = "2.0.0"
            category = "utility"
            def setup(self): pass
            def register_commands(self, app): pass

        # Patch console to verify warning
        with patch("structum.plugins.registry.console") as mock_console:
            PluginRegistry.register(DuplicatePlugin, is_official=True)

            # Verify warning was printed
            assert mock_console.print.called
            warning_call = str(mock_console.print.call_args)
            assert "already registered" in warning_call

        # Verify the second plugin overrode the first
        metadata = PluginRegistry.get_metadata("valid-plugin")
        assert metadata is not None
        assert metadata.plugin_class == DuplicatePlugin
