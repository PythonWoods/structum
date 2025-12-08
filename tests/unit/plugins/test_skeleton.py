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

    def test_no_dev_marker_created(self, tmp_path):
        """Test that no .dev marker file is created (removed in v0.2)."""
        output = tmp_path / "plugins"
        name = "test-plugin"

        plugin_path = skeleton.generate_plugin_skeleton(name, output)

        # Verify .dev marker does NOT exist
        dev_marker = plugin_path / ".dev"
        assert not dev_marker.exists(), ".dev marker should not be created in v0.2"

    def test_external_only_generation(self, tmp_path):
        """Test that plugin generation is external-only (no built-in support)."""
        output = tmp_path / "plugins"
        name = "external-plugin"

        plugin_path = skeleton.generate_plugin_skeleton(name, output)

        # Verify it's a standard external plugin structure
        assert plugin_path.exists()
        assert (plugin_path / "plugin.py").exists()
        assert (plugin_path / "__init__.py").exists()

        # Verify no built-in specific markers or files
        assert not (plugin_path / ".builtin").exists()
        assert not (plugin_path / ".dev").exists()
