# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Registry for Structum."""

from dataclasses import dataclass
from enum import Enum

from rich.console import Console

from structum.plugins.sdk import CATEGORIES, PluginBase

console = Console()


class PluginType(Enum):
    """Type of plugin (official vs external)."""

    OFFICIAL = "official"  # structum_* packages (maintained by PythonWoods)
    EXTERNAL = "external"  # Third-party plugins


@dataclass
class PluginMetadata:
    """Metadata for a registered plugin."""

    plugin_class: type[PluginBase]
    plugin_type: PluginType
    module_path: str
    source: str  # Entry point name


class PluginRegistry:
    """Central registry for all plugins."""

    _plugins: dict[str, PluginMetadata] = {}
    _instances: dict[str, PluginBase] = {}

    @classmethod
    def register(cls, plugin_cls: type[PluginBase], is_official: bool = False) -> None:
        """Register a plugin class with type information.

        Args:
            plugin_cls: The plugin class to register.
            is_official: True if this is an official plugin (structum_*).

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
        plugin_type = PluginType.OFFICIAL if is_official else PluginType.EXTERNAL

        # Create metadata and register
        metadata = PluginMetadata(
            plugin_class=plugin_cls,
            plugin_type=plugin_type,
            module_path=plugin_cls.__module__,
            source=f"entrypoint:{plugin_name}",
        )

        cls._plugins[plugin_name] = metadata

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
        for name, metadata in cls._plugins.items():
            if name not in cls._instances:
                instance = metadata.plugin_class()
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
    def list_plugins_detailed(cls) -> dict[str, dict[str, str]]:
        """List all registered plugins with detailed metadata.

        Returns:
            Dictionary of plugin info including type.
        """
        return {
            name: {
                "version": metadata.plugin_class.version,
                "category": metadata.plugin_class.category,
                "description": metadata.plugin_class.description,
                "author": metadata.plugin_class.author,
                "type": metadata.plugin_type.value,
                "module": metadata.module_path,
            }
            for name, metadata in cls._plugins.items()
        }

    @classmethod
    def list_by_type(cls) -> dict[str, list[str]]:
        """List plugins grouped by type (official vs external).

        Returns:
            Dictionary mapping plugin type to list of plugin names.
        """
        result: dict[str, list[str]] = {
            PluginType.OFFICIAL.value: [],
            PluginType.EXTERNAL.value: [],
        }
        for name, metadata in cls._plugins.items():
            result[metadata.plugin_type.value].append(name)
        return result

    @classmethod
    def list_by_category(cls) -> dict[str, list[str]]:
        """List plugins grouped by category.

        Returns:
            Dictionary mapping category to list of plugin names.
        """
        result: dict[str, list[str]] = {}
        for name, metadata in cls._plugins.items():
            category = metadata.plugin_class.category
            if category not in result:
                result[category] = []
            result[category].append(name)
        return result

    @classmethod
    def clear(cls) -> None:
        """Clear registry (useful for testing)."""
        cls._plugins.clear()
        cls._instances.clear()
