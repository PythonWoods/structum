# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin system for Structum.

This package contains the logic for loading external plugins via entry points.
Official plugins (structum_*) and third-party plugins are loaded dynamically.
"""

from .loader import load_plugins
from .registry import PluginRegistry, PluginType, PluginMetadata

__all__ = ["load_plugins", "PluginRegistry", "PluginType", "PluginMetadata"]
