# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Configuration management for Structum Core."""

from structum.config.manager import (
    get_plugin_enabled,
    load_config,
    save_config,
    set_plugin_enabled,
)

__all__ = [
    "load_config",
    "save_config",
    "get_plugin_enabled",
    "set_plugin_enabled",
]
