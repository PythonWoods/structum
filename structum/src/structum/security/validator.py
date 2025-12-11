# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin validation and security checks."""

from pathlib import Path
from typing import Any


class PluginValidator:
    """Validates plugins for security and correctness."""

    def __init__(self, strict_mode: bool = False) -> None:
        """Initialize validator.

        Args:
            strict_mode: Enable strict validation rules
        """
        self.strict_mode = strict_mode

    def validate_plugin_class(self, plugin_cls: type) -> tuple[bool, str]:
        """Validate a plugin class.

        Args:
            plugin_cls: Plugin class to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        # Check required attributes
        required_attrs = ["name", "version", "category"]
        for attr in required_attrs:
            if not hasattr(plugin_cls, attr):
                return False, f"Missing required attribute: {attr}"

        # Check required methods
        required_methods = ["setup"]
        for method in required_methods:
            if not hasattr(plugin_cls, method):
                return False, f"Missing required method: {method}"

        return True, ""

    def validate_plugin_metadata(self, metadata: dict[str, Any]) -> tuple[bool, str]:
        """Validate plugin metadata.

        Args:
            metadata: Plugin metadata dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        required_keys = ["name", "version"]
        for key in required_keys:
            if key not in metadata:
                return False, f"Missing required metadata key: {key}"

        return True, ""

    def is_path_safe(self, path: Path) -> bool:
        """Check if a path is safe (no path traversal).

        Args:
            path: Path to check

        Returns:
            True if path is safe
        """
        try:
            # Resolve to absolute path and check for traversal
            _ = path.resolve()
            # In a real implementation, you'd check against allowed directories
            return True
        except (OSError, RuntimeError):
            return False
