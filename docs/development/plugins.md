# Plugin Development

This guide covers everything you need to create plugins for Structum, whether you're contributing to the core project or building standalone plugins.

## Overview

Structum's plugin system allows extending functionality with custom commands and processing logic. There are two ways to create plugins:

1. **Builtin Plugins** – For contributors to the Structum project
2. **External Plugins** – Standalone packages published to PyPI

## Categories

Plugins are organized into categories:

| Category | Description |
|----------|-------------|
| `analysis` | Code analysis and metrics |
| `export` | Export and format conversion |
| `formatting` | Code formatting and style |
| `utility` | Utility and helper tools (default) |

---

## Creating a Builtin Plugin (Contributors)

If you're contributing to the Structum project and want to add a new plugin:

### Step 1: Generate the Skeleton

From the **root of the structum repository**:

```bash
structum plugins new my-plugin --category analysis
```

This automatically creates the plugin in `src/structum/plugins/my_plugin/`.

### Step 2: Implement Your Plugin

Edit the generated files:

- `plugin.py` – Main plugin class
- `commands/main.py` – CLI commands
- `core/logic.py` – Business logic

### Step 3: Register the Plugin

Edit `src/structum/plugins/loader.py`:

```python
def load_builtin_plugins(app: typer.Typer) -> None:
    """Loads built-in plugins."""
    from . import sample, my_plugin  # Add your import

    # Register plugin classes
    PluginRegistry.register(sample.SamplePlugin)
    PluginRegistry.register(my_plugin.MyPlugin)  # Add this

    # Initialize plugins
    PluginRegistry.load_all()

    # Register CLI commands for enabled plugins
    for name in ["sample", "my_plugin"]:  # Add your plugin name
        plugin = PluginRegistry.get(name)
        if plugin and get_plugin_enabled(name):
            plugin.register_commands(app)
```

### Step 4: Test Your Plugin

```bash
# Verify it appears in the list
structum plugins list

# Enable it if disabled
structum plugins enable my-plugin

# Run your command
structum my-plugin <your-command>
```

### Step 5: Submit a Pull Request

Commit your changes and open a PR to the `develop` branch.

---

## Creating an External Plugin (Standalone Package)

If you want to create a plugin that can be published to PyPI:

### Step 1: Generate the Skeleton

From your preferred directory:

```bash
structum plugins new my-awesome-plugin --category export --output ~/projects/
```

This creates `~/projects/my_awesome_plugin/`.

### Step 2: Create Package Structure

Add these files to make it a proper Python package:

```
my_awesome_plugin/
├── pyproject.toml      # NEW
├── README.md           # NEW
├── src/
│   └── my_awesome_plugin/
│       ├── __init__.py
│       ├── plugin.py
│       ├── commands/
│       │   ├── __init__.py
│       │   └── main.py
│       └── core/
│           ├── __init__.py
│           └── logic.py
```

### Step 3: Configure `pyproject.toml`

```toml
[project]
name = "structum-my-awesome-plugin"
version = "0.1.0"
description = "My awesome Structum plugin"
requires-python = ">=3.11"
dependencies = [
    "structum>=0.1.0",
    "typer>=0.9.0",
]

[project.entry-points."structum.plugins"]
my-awesome-plugin = "my_awesome_plugin:MyAwesomePluginPlugin"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

> **Important**: The entry point format is:
> ```
> plugin-name = "package_name:PluginClassName"
> ```

### Step 4: Install Locally for Testing

```bash
cd ~/projects/my_awesome_plugin
pip install -e .

# Verify it's loaded
structum plugins list
```

### Step 5: Publish to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

Users can then install your plugin with:

```bash
pip install structum-my-awesome-plugin
```

---

## Plugin Structure Reference

### Required Files

#### `plugin.py`

```python
import typer
from structum.plugins.sdk import PluginBase
from .commands import main


class MyPlugin(PluginBase):
    """My plugin description."""

    # Required attributes
    name = "my-plugin"
    version = "1.0.0"
    category = "utility"  # analysis, export, formatting, utility

    # Optional attributes
    description = "What this plugin does"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources (called once on load)."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands."""
        app.add_typer(main.app, name="my-plugin")
```

#### `__init__.py`

Keep this clean – only export the plugin class:

```python
from .plugin import MyPlugin

__all__ = ["MyPlugin"]
```

#### `commands/main.py`

Define your CLI commands:

```python
import typer

app = typer.Typer(help="My plugin commands.")


@app.command("run")
def run_command(
    path: str = typer.Argument(".", help="Path to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Run the main plugin action."""
    from ..core.logic import process

    result = process(path, verbose)
    typer.echo(result)
```

#### `core/logic.py`

Keep business logic separate from CLI:

```python
def process(path: str, verbose: bool) -> str:
    """Core processing logic."""
    # Your implementation here
    return f"Processed {path}"
```

---

## Plugin Validation

When a plugin is loaded, Structum validates:

| Attribute | Requirement |
|-----------|-------------|
| `name` | Must be a non-empty string |
| `version` | Must be a non-empty string |
| `category` | Must be one of: `analysis`, `export`, `formatting`, `utility` |
| `setup()` | Must be implemented |

Invalid plugins are rejected with a descriptive error message.

---

## Plugin Configuration

Plugins can be enabled/disabled via CLI:

```bash
structum plugins disable my-plugin  # Disable
structum plugins enable my-plugin   # Enable
structum plugins list               # Check status
```

Configuration is stored in `~/.config/structum/config.json`.

---

## Best Practices

1. **Separation of Concerns**: Keep CLI code in `commands/`, logic in `core/`
2. **Type Hints**: Use type hints for all functions
3. **Error Handling**: Use Typer's error handling and Rich for output
4. **Testing**: Write tests for your core logic
5. **Documentation**: Include docstrings and a README
