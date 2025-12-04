# Plugin Development

## Overview

Structum's plugin system allows extending functionality with custom commands and processing logic.

## Creating a New Plugin

Use the CLI to generate a plugin skeleton:

```bash
structum plugins new my-awesome-plugin
```

This creates:
```
my-awesome-plugin/
├── __init__.py
├── plugin.py
├── commands/
│   ├── __init__.py
│   └── main.py
└── core/
    ├── __init__.py
    └── logic.py
```

## Plugin Structure

### Required Files

#### `plugin.py`
Contains the main plugin class inheriting from `PluginBase`:

```python
from structum.plugins.sdk import PluginBase
import typer
from .commands import main

class MyPlugin(PluginBase):
    name = "my-plugin"          # Required
    version = "1.0.0"           # Required
    description = "My plugin"   # Optional
    author = "Your Name"        # Optional

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands."""
        app.add_typer(main.app, name="my-plugin")
```

#### `__init__.py`
Only exports the plugin class:

```python
from .plugin import MyPlugin
__all__ = ["MyPlugin"]
```

### Optional Structure

- `commands/`: CLI command modules
- `core/`: Business logic (separate from CLI)

## Plugin Validation

When loading, Structum validates:
- `name` attribute exists and is a string
- `version` attribute exists and is a string
- `setup()` method is implemented
- `register_commands()` method exists

## Registering External Plugins

Add to `pyproject.toml`:

```toml
[project.entry-points."structum.plugins"]
my-plugin = "my_plugin:MyPlugin"
```
