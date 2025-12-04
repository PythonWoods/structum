# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Registry for Structum."""


from structum.plugins.sdk import PluginBase


class PluginRegistry:
    """Central registry for all plugins."""

    _plugins: dict[str, type[PluginBase]] = {}
    _instances: dict[str, PluginBase] = {}

    @classmethod
    def register(cls, plugin_cls: type[PluginBase]) -> None:
        """Register a plugin class.

        Args:
            plugin_cls: The plugin class to register.

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

        cls._plugins[plugin_cls.name] = plugin_cls

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
        for name, plugin_cls in cls._plugins.items():
            if name not in cls._instances:
                instance = plugin_cls()
                instance.setup()
                cls._instances[name] = instance

    @classmethod
    def list_plugins(cls) -> dict[str, dict[str, str]]:
        """List all registered plugins with metadata.

        Returns:
            Dictionary of plugin info.
        """
        return {
            name: {
                "version": plugin.version,
                "description": plugin.description,
                "author": plugin.author,
            }
            for name, plugin in cls._plugins.items()
        }

    @classmethod
    def clear(cls) -> None:
        """Clear registry (useful for testing)."""
        cls._plugins.clear()
        cls._instances.clear()
