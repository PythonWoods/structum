# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Utility functions for plugins."""

import inspect
from importlib.metadata import PackageNotFoundError, metadata
from pathlib import Path


def get_plugin_metadata_from_module(module_name: str) -> dict[str, str]:
    """Get plugin metadata from installed package.

    This function reads metadata from the package's pyproject.toml (via importlib.metadata).
    Plugins can use this to display their own metadata dynamically.

    Args:
        module_name: The module name (e.g., "my_plugin").

    Returns:
        Dictionary with metadata: version, author, author_email, description, license.

    Example:
        >>> # In your plugin's commands/main.py
        >>> from structum.plugins.utils import get_plugin_metadata_from_module
        >>>
        >>> @app.command("info")
        >>> def info_command() -> None:
        >>>     meta = get_plugin_metadata_from_module(__name__.split('.')[0])
        >>>     print(f"Version: {meta['version']}")
        >>>     print(f"Author: {meta['author']}")
    """
    # Try to find the distribution that contains this module
    try:
        # Common patterns for plugin package names
        potential_names = [
            f"structum-plugin-{module_name.replace('_', '-')}",
            f"structum_{module_name}",
            module_name,
        ]

        for dist_name in potential_names:
            try:
                pkg_meta = metadata(dist_name)
                return {
                    "version": pkg_meta.get("Version", "unknown"),
                    "author": pkg_meta.get("Author", "unknown"),
                    "author_email": pkg_meta.get("Author-Email", ""),
                    "description": pkg_meta.get("Summary", ""),
                    "license": pkg_meta.get("License", ""),
                }
            except PackageNotFoundError:
                continue

        # If not found, return defaults
        return {
            "version": "unknown",
            "author": "unknown",
            "author_email": "",
            "description": "",
            "license": "",
        }
    except Exception:
        return {
            "version": "unknown",
            "author": "unknown",
            "author_email": "",
            "description": "",
            "license": "",
        }


def get_current_plugin_metadata() -> dict[str, str]:
    """Get metadata for the currently executing plugin.

    Automatically detects the calling module and retrieves its metadata.
    This is the simplest function for plugins to use in their commands.

    Returns:
        Dictionary with metadata: version, author, author_email, description, license.

    Example:
        >>> # In your plugin's commands/main.py
        >>> from structum.plugins.utils import get_current_plugin_metadata
        >>>
        >>> @app.command("info")
        >>> def info_command() -> None:
        >>>     meta = get_current_plugin_metadata()
        >>>     print(f"✓ {meta['description']}")
        >>>     print(f"Version: {meta['version']}")
        >>>     print(f"Author: {meta['author']}")
    """
    # Get the calling module
    frame = inspect.currentframe()
    if frame and frame.f_back:
        caller_module = inspect.getmodule(frame.f_back)
        if caller_module and caller_module.__name__:
            # Extract root package name (e.g., "my_plugin" from "my_plugin.commands.main")
            root_module = caller_module.__name__.split(".")[0]
            return get_plugin_metadata_from_module(root_module)

    return {
        "version": "unknown",
        "author": "unknown",
        "author_email": "",
        "description": "",
        "license": "",
    }
