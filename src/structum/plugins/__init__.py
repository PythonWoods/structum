# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin system for Structum.

This package contains the logic for loading plugins and any built-in plugins.
"""

from .loader import load_plugins

__all__ = ["load_plugins"]
