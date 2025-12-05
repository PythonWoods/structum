# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import json
from pathlib import Path
import pytest
from structum.core import config

class TestConfig:
    """Tests for configuration management."""

    @pytest.fixture(autouse=True)
    def mock_config_paths(self, tmp_path, monkeypatch):
        """Redirect config paths to a temporary directory."""
        mock_dir = tmp_path / ".config" / "structum"
        mock_file = mock_dir / "config.json"
        
        monkeypatch.setattr(config, "CONFIG_DIR", mock_dir)
        monkeypatch.setattr(config, "CONFIG_FILE", mock_file)
        
        return mock_dir, mock_file

    def test_load_config_defaults(self):
        """Test loading config when file doesn't exist."""
        data = config.load_config()
        assert data == {"plugins": {}}

    def test_save_and_load_config(self):
        """Test saving and then loading configuration."""
        test_data = {"plugins": {"test_plugin": {"enabled": True}}}
        config.save_config(test_data)
        
        loaded = config.load_config()
        assert loaded == test_data

    def test_get_plugin_enabled(self):
        """Test checking if a plugin is enabled."""
        config.set_plugin_enabled("my_plugin", True)
        assert config.get_plugin_enabled("my_plugin") is True
        
        config.set_plugin_enabled("my_plugin", False)
        assert config.get_plugin_enabled("my_plugin") is False

    def test_get_plugin_enabled_default(self):
        """Test default enabled state for unknown plugins."""
        # Current implementation defaults to True (according to code reading)
        # enabled: bool = config.get("plugins", {}).get(name, {}).get("enabled", True)
        assert config.get_plugin_enabled("unknown_plugin") is True
