# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from pathlib import Path
import pytest
from structum.plugins import skeleton

class TestSkeleton:
    """Tests for plugin skeleton generation."""

    def test_generate_plugin_skeleton(self, tmp_path):
        """Test generating a new plugin structure."""
        output = tmp_path / "plugins"
        name = "my-test-plugin"
        category = "analysis"
        
        plugin_path = skeleton.generate_plugin_skeleton(name, output, category)
        
        assert plugin_path.exists()
        assert (plugin_path / "plugin.py").exists()
        assert (plugin_path / "commands" / "main.py").exists()
        assert (plugin_path / "core" / "logic.py").exists()
        
        # Check content replacement
        content = (plugin_path / "plugin.py").read_text()
        assert 'name = "my-test-plugin"' in content
        assert 'class MyTestPluginPlugin(PluginBase):' in content # CamelCase check
        assert f'category = "{category}"' in content

    def test_generate_plugin_skeleton_default_category(self, tmp_path):
        """Test default category usage."""
        output = tmp_path / "plugins"
        name = "simple"
        
        plugin_path = skeleton.generate_plugin_skeleton(name, output)
        
        content = (plugin_path / "plugin.py").read_text()
        assert 'category = "utility"' in content
