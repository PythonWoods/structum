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
        info = PluginRegistry.list_plugins()["valid-plugin"]
        assert info["version"] == "1.0.0"

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
