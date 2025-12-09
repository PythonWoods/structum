# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from pathlib import Path
import pytest
from structum.plugins import skeleton

class TestSkeleton:
    """Tests for plugin skeleton generation."""

    def test_generate_plugin_skeleton(self, tmp_path):
        """Test generating a complete plugin package structure."""
        output = tmp_path
        name = "my-test-plugin"
        package_name = "my_test_plugin"
        category = "analysis"

        plugin_root = skeleton.generate_plugin_skeleton(name, output, category)

        # Verify package root structure (standalone project)
        assert plugin_root.exists()
        assert plugin_root == output / name
        assert (plugin_root / "pyproject.toml").exists()
        assert (plugin_root / "README.md").exists()
        assert (plugin_root / ".gitignore").exists()

        # Verify src/ layout
        src_dir = plugin_root / "src" / package_name
        assert src_dir.exists()
        assert (src_dir / "__init__.py").exists()
        assert (src_dir / "plugin.py").exists()
        assert (src_dir / "commands" / "__init__.py").exists()
        assert (src_dir / "commands" / "main.py").exists()
        assert (src_dir / "core" / "__init__.py").exists()
        assert (src_dir / "core" / "logic.py").exists()

        # Check plugin.py content
        content = (src_dir / "plugin.py").read_text()
        assert 'name = "my-test-plugin"' in content
        assert 'class MyTestPluginPlugin(PluginBase):' in content
        assert f'category = "{category}"' in content

        # Check pyproject.toml content
        pyproject_content = (plugin_root / "pyproject.toml").read_text()
        assert 'name = "structum-plugin-my-test-plugin"' in pyproject_content
        assert f'my-test-plugin = "{package_name}:MyTestPluginPlugin"' in pyproject_content
        assert 'structum>=0.2.0' in pyproject_content

        # Check README.md content
        readme_content = (plugin_root / "README.md").read_text()
        assert "My Test Plugin" in readme_content
        assert "pip install -e ." in readme_content

    def test_generate_plugin_skeleton_default_category(self, tmp_path):
        """Test default category usage."""
        output = tmp_path
        name = "simple"
        package_name = "simple"

        plugin_root = skeleton.generate_plugin_skeleton(name, output)

        src_dir = plugin_root / "src" / package_name
        content = (src_dir / "plugin.py").read_text()
        assert 'category = "utility"' in content

    def test_no_dev_marker_created(self, tmp_path):
        """Test that no .dev marker file is created (removed in v0.2)."""
        output = tmp_path
        name = "test-plugin"

        plugin_root = skeleton.generate_plugin_skeleton(name, output)

        # Verify .dev marker does NOT exist in root or src
        dev_marker_root = plugin_root / ".dev"
        dev_marker_src = plugin_root / "src" / "test_plugin" / ".dev"
        assert not dev_marker_root.exists(), ".dev marker should not be created in v0.2"
        assert not dev_marker_src.exists(), ".dev marker should not be created in v0.2"

    def test_external_only_generation(self, tmp_path):
        """Test that plugin generation is external-only (no built-in support)."""
        output = tmp_path
        name = "external-plugin"
        package_name = "external_plugin"

        plugin_root = skeleton.generate_plugin_skeleton(name, output)

        # Verify it's a standard external plugin package structure
        assert plugin_root.exists()
        assert (plugin_root / "pyproject.toml").exists()
        assert (plugin_root / "README.md").exists()

        src_dir = plugin_root / "src" / package_name
        assert (src_dir / "plugin.py").exists()
        assert (src_dir / "__init__.py").exists()

        # Verify no built-in specific markers or files
        assert not (plugin_root / ".builtin").exists()
        assert not (plugin_root / ".dev").exists()
        assert not (src_dir / ".builtin").exists()
        assert not (src_dir / ".dev").exists()
