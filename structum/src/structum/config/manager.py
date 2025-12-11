# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Configuration Manager for Structum."""

import json
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".config" / "structum"
CONFIG_FILE = CONFIG_DIR / "config.json"


def _ensure_config_dir() -> None:
    """Ensure the configuration directory exists."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> dict[str, Any]:
    """Load configuration from file.

    Returns:
        Configuration dictionary.
    """
    _ensure_config_dir()
    if CONFIG_FILE.exists():
        data: dict[str, Any] = json.loads(CONFIG_FILE.read_text())
        return data
    return {"plugins": {}}


def save_config(config: dict[str, Any]) -> None:
    """Save configuration to file.

    Args:
        config: Configuration dictionary to save.
    """
    _ensure_config_dir()
    CONFIG_FILE.write_text(json.dumps(config, indent=2))


def get_plugin_enabled(name: str) -> bool:
    """Check if a plugin is enabled.

    Args:
        name: Plugin name.

    Returns:
        True if enabled, False otherwise.
    """
    config = load_config()
    enabled: bool = config.get("plugins", {}).get(name, {}).get("enabled", True)
    return enabled


def set_plugin_enabled(name: str, enabled: bool) -> None:
    """Set plugin enabled state.

    Args:
        name: Plugin name.
        enabled: Whether the plugin should be enabled.
    """
    config = load_config()
    if "plugins" not in config:
        config["plugins"] = {}
    if name not in config["plugins"]:
        config["plugins"][name] = {}
    config["plugins"][name]["enabled"] = enabled
    save_config(config)
