# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Registry for Structum."""

from dataclasses import dataclass
from enum import Enum
from importlib.metadata import PackageNotFoundError, metadata

from rich.console import Console

from structum.plugins.sdk import CATEGORIES, PluginBase

console = Console()


class PluginType(Enum):
    """Type of plugin (official vs community)."""

    OFFICIAL = "official"  # structum_* packages (maintained by PythonWoods)
    COMMUNITY = "community"  # Community plugins


@dataclass
class PluginMetadata:
    """Metadata for a registered plugin."""

    plugin_class: type[PluginBase]
    plugin_type: PluginType
    module_path: str
    source: str  # Entry point name
    distribution_name: str | None = None  # PyPI package name for reading metadata


class PluginRegistry:
    """Central registry for all plugins."""

    _plugins: dict[str, PluginMetadata] = {}
    _instances: dict[str, PluginBase] = {}

    @classmethod
    def register(
        cls,
        plugin_cls: type[PluginBase],
        is_official: bool = False,
        distribution_name: str | None = None,
    ) -> None:
        """Register a plugin class with type information.

        Args:
            plugin_cls: The plugin class to register.
            is_official: True if this is an official plugin (structum_*).
            distribution_name: PyPI package name for reading metadata.

        Raises:
            TypeError: If plugin doesn't inherit from PluginBase.
            ValueError: If plugin is missing required attributes.
        """
        if not issubclass(plugin_cls, PluginBase):
            raise TypeError(f"Plugin {plugin_cls} must inherit from PluginBase")

        # Validate required attributes
        if not hasattr(plugin_cls, "name") or not isinstance(plugin_cls.name, str):
            raise ValueError(f"Plugin {plugin_cls} must have a 'name' string attribute")

        if not hasattr(plugin_cls, "version") or not isinstance(plugin_cls.version, str):
            raise ValueError(f"Plugin {plugin_cls} must have a 'version' string attribute")

        # Validate category
        category = getattr(plugin_cls, "category", "utility")
        if category not in CATEGORIES:
            raise ValueError(
                f"Plugin {plugin_cls} has invalid category '{category}'. "
                f"Valid categories: {', '.join(CATEGORIES.keys())}"
            )

        # Check for conflicts
        plugin_name = plugin_cls.name
        if plugin_name in cls._plugins:
            existing = cls._plugins[plugin_name]
            console.print(
                f"[yellow]⚠ WARNING: Plugin '{plugin_name}' already registered. "
                f"Overriding {existing.module_path} with {plugin_cls.__module__}[/yellow]"
            )

        # Determine plugin type
        plugin_type = PluginType.OFFICIAL if is_official else PluginType.COMMUNITY

        # Create metadata and register
        plugin_metadata = PluginMetadata(
            plugin_class=plugin_cls,
            plugin_type=plugin_type,
            module_path=plugin_cls.__module__,
            source=f"entrypoint:{plugin_name}",
            distribution_name=distribution_name,
        )

        cls._plugins[plugin_name] = plugin_metadata

    @classmethod
    def get(cls, name: str) -> PluginBase | None:
        """Get an instantiated plugin by name.

        Args:
            name: The name of the plugin.

        Returns:
            The plugin instance or None if not found/loaded.
        """
        return cls._instances.get(name)

    @classmethod
    def load_all(cls) -> None:
        """Instantiate and setup all registered plugins."""
        for name, plugin_meta in cls._plugins.items():
            if name not in cls._instances:
                instance = plugin_meta.plugin_class()
                instance.setup()
                cls._instances[name] = instance

    @classmethod
    def list_plugins(cls) -> list[str]:
        """List all registered plugin names.

        Returns:
            List of plugin names.
        """
        return list(cls._plugins.keys())

    @classmethod
    def get_metadata(cls, name: str) -> PluginMetadata | None:
        """Get metadata for a plugin.

        Args:
            name: The name of the plugin.

        Returns:
            Plugin metadata or None if not found.
        """
        return cls._plugins.get(name)

    @classmethod
    def get_package_metadata(cls, name: str) -> dict[str, str]:
        """Get metadata from installed package (pyproject.toml).

        Args:
            name: Plugin name.

        Returns:
            Dictionary with package metadata (version, author, description, etc.)
            Falls back to class attributes if package metadata unavailable.
        """
        plugin_metadata = cls._plugins.get(name)
        if not plugin_metadata:
            return {}

        # Try to read from installed package metadata first
        if plugin_metadata.distribution_name:
            try:
                pkg_meta = metadata(plugin_metadata.distribution_name)
                return {
                    "version": pkg_meta.get("Version", "unknown"),
                    "author": pkg_meta.get("Author", "unknown"),
                    "author_email": pkg_meta.get("Author-Email", ""),
                    "description": pkg_meta.get("Summary", ""),
                    "license": pkg_meta.get("License", ""),
                }
            except PackageNotFoundError:
                pass

        # Fallback to class attributes
        plugin_cls = plugin_metadata.plugin_class
        return {
            "version": getattr(plugin_cls, "version", "unknown"),
            "author": getattr(plugin_cls, "author", "unknown"),
            "author_email": "",
            "description": getattr(plugin_cls, "description", ""),
            "license": "",
        }

    @classmethod
    def list_plugins_detailed(cls) -> dict[str, dict[str, str]]:
        """List all registered plugins with detailed metadata.

        Returns:
            Dictionary of plugin info including type.
        """
        result = {}
        for name, plugin_metadata in cls._plugins.items():
            pkg_meta = cls.get_package_metadata(name)
            result[name] = {
                "version": pkg_meta.get("version", "unknown"),
                "category": plugin_metadata.plugin_class.category,
                "description": pkg_meta.get("description", ""),
                "author": pkg_meta.get("author", "unknown"),
                "type": plugin_metadata.plugin_type.value,
                "module": plugin_metadata.module_path,
            }
        return result

    @classmethod
    def list_by_type(cls) -> dict[str, list[str]]:
        """List plugins grouped by type (official vs community).

        Returns:
            Dictionary mapping plugin type to list of plugin names.
        """
        result: dict[str, list[str]] = {
            PluginType.OFFICIAL.value: [],
            PluginType.COMMUNITY.value: [],
        }
        for name, plugin_meta in cls._plugins.items():
            result[plugin_meta.plugin_type.value].append(name)
        return result

    @classmethod
    def list_by_category(cls) -> dict[str, list[str]]:
        """List plugins grouped by category.

        Returns:
            Dictionary mapping category to list of plugin names.
        """
        result: dict[str, list[str]] = {}
        for name, plugin_meta in cls._plugins.items():
            category = plugin_meta.plugin_class.category
            if category not in result:
                result[category] = []
            result[category].append(name)
        return result

    @classmethod
    def clear(cls) -> None:
        """Clear registry (useful for testing)."""
        cls._plugins.clear()
        cls._instances.clear()
