# Plugin Development

This guide covers everything you need to create plugins for Structum.

## Overview

Structum's plugin system allows extending functionality with custom commands and processing logic through **external plugins** installed via entry points.

### Plugin Types

All plugins are external packages, but there are two categories:

1. **Official Plugins** (`structum_*`) – Maintained by PythonWoods team, auto-detected and tagged as [OFFICIAL]
2. **External Plugins** – Third-party plugins, tagged as [EXTERNAL]

Both types work identically and use the same entry point mechanism. The only difference is the naming convention that triggers automatic official plugin detection.

## Categories

Plugins are organized into categories:

| Category | Description |
|----------|-------------|
| `analysis` | Code analysis and metrics |
| `export` | Export and format conversion |
| `formatting` | Code formatting and style |
| `utility` | Utility and helper tools (default) |

---

## Creating a Plugin

All plugins are external packages that use entry points for registration. You can create either:
- **Official plugins** (structum_*) – Maintained by PythonWoods
- **External plugins** (any name) – Third-party plugins

### Naming Conventions

**Official Plugins:**
- Package name: `structum_<name>` (e.g., `structum_latex`)
- PyPI name: `structum-<name>` (e.g., `structum-latex`)
- Auto-detected as [OFFICIAL] by the `structum_` prefix

**External Plugins:**
- Package name: Any valid Python package name
- PyPI name: Recommended `structum-plugin-<name>` (e.g., `structum-plugin-myfeature`)
- Tagged as [EXTERNAL] in plugin list

### Step 1: Generate the Plugin Package

From your preferred directory:

```bash
structum plugins new my-awesome-plugin --category export --output ~/projects/
```

This automatically creates a **complete, standalone, ready-to-install** Python package at `~/projects/my-awesome-plugin/`:

```
~/projects/my-awesome-plugin/         # ← Standalone project, like any Python package
├── pyproject.toml                    # ✅ Pre-configured with entry point
├── README.md                         # ✅ Documentation template
├── .gitignore                        # ✅ Git ignore rules
└── src/
    └── my_awesome_plugin/
        ├── __init__.py
        ├── plugin.py
        ├── commands/
        │   ├── __init__.py
        │   └── main.py
        └── core/
            ├── __init__.py
            └── logic.py
```

The generated `pyproject.toml` is **already fully configured** with:
- Package name: `structum-plugin-my-awesome-plugin`
- Entry point: `my-awesome-plugin = "my_awesome_plugin:MyAwesomePluginPlugin"`
- Dependencies: `structum>=0.2.0`, `typer>=0.12.0`, `rich>=13.0`
- Build system: `hatchling` with modern `src/` layout

> **No manual configuration needed!** The plugin is a complete Python package ready to install, develop, git commit, and publish to PyPI.

### Step 2: Install and Test Locally

```bash
cd ~/projects/my-awesome-plugin
pip install -e .

# Test your plugin
structum my-awesome-plugin info

# Verify it's loaded
structum plugins list
```

### Step 3: Implement Your Plugin

Edit the generated files to add your functionality:

1. **Add commands** in `src/my_awesome_plugin/commands/main.py`:
   ```python
   @app.command("process")
   def process_command(path: Path = typer.Argument(...)):
       """Process files."""
       from ..core.logic import process_data
       result = process_data(path)
       typer.echo(result)
   ```

2. **Add business logic** in `src/my_awesome_plugin/core/logic.py`:
   ```python
   def process_data(path: Path) -> str:
       """Your core functionality here."""
       return f"Processed: {path}"
   ```

3. **Update metadata** in `src/my_awesome_plugin/plugin.py`:
   - Change `author`, `description`, `version`

### Step 4: Publish to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

Users can then install your plugin with:

```bash
pip install structum-plugin-my-awesome-plugin
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

The generated template provides a basic `info` command that displays plugin metadata. Add your custom commands as needed:

```python
import typer

app = typer.Typer(
    help="My plugin commands.",
    no_args_is_help=True  # Show help when no subcommand is provided
)

# Plugin metadata
PLUGIN_INFO = {
    "name": "my-plugin",
    "version": "0.1.0",
    "description": "My plugin description",
    "category": "utility",
}


@app.command("info")
def info_command() -> None:
    """Display plugin information and metadata."""
    output_lines = [
        f"✓ {PLUGIN_INFO['name']} v{PLUGIN_INFO['version']}",
        f"  {PLUGIN_INFO['description']}",
        "",
        f"Category: {PLUGIN_INFO['category']}",
        "",
        "Available commands:",
        "  info     - Display this information",
        "  # TODO: Add your commands here",
    ]
    typer.echo("\n".join(output_lines))


# Add your custom commands here
# Example:
#
# @app.command("process")
# def process_command(
#     path: Path = typer.Argument(..., help="Path to process"),
#     output: Path | None = typer.Option(None, "--output", "-o"),
# ) -> None:
#     """Process files."""
#     from ..core.logic import process_data
#     result = process_data(path, plugin_info=PLUGIN_INFO)
#     typer.echo(result)
```

**Template Features:**
- ✅ `PLUGIN_INFO` constant with metadata (name, version, description, category)
- ✅ Default `info` command for displaying plugin information
- ✅ Commented examples showing how to add custom commands
- ✅ Type safety with type hints
- ✅ Professional output formatting

> **Important**: Always include `no_args_is_help=True` to maintain consistency with other Structum commands. This ensures users see helpful command lists instead of error messages when invoking your plugin without arguments.

#### `core/logic.py`

Keep business logic separate from CLI commands. The template provides commented examples:

```python
from pathlib import Path


# TODO: Implement your plugin's core business logic here
#
# Example function:
#
# def process_data(
#     path: Path,
#     plugin_info: dict[str, str] | None = None,
# ) -> dict[str, any]:
#     """Process data from the given path.
#
#     Args:
#         path: Path to process
#         plugin_info: Plugin metadata (name, version, description, category)
#
#     Returns:
#         Dictionary with processing results
#     """
#     plugin_name = plugin_info.get("name", "unknown") if plugin_info else "unknown"
#
#     # Your implementation here
#     result = {
#         "plugin": plugin_name,
#         "processed": str(path),
#         "status": "success",
#     }
#
#     return result
```

**Best Practices:**
- ✅ Implement your own functions based on plugin requirements
- ✅ Use `plugin_info` parameter to access metadata (name, version, etc.)
- ✅ Keep business logic separate from CLI command handling
- ✅ Use full type hints and comprehensive docstrings
- ✅ Return structured data (dict, dataclass) or formatted strings

**Professional Output Example:**

```python
def format_output(data: dict, plugin_info: dict) -> str:
    """Format results with plugin metadata."""
    lines = [
        f"✓ {plugin_info['name']} v{plugin_info['version']}",
        f"  {plugin_info['description']}",
        "",
        f"Status: {data['status']}",
        f"Processed: {data['processed']}",
    ]
    return "\n".join(lines)
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

## How Plugin Discovery Works

Structum uses a **single, unified discovery mechanism** via Python entry points for all plugins (both official and external).

### Plugin Loading Process

1. **Entry Point**: Plugin defined in `pyproject.toml` under `[project.entry-points."structum.plugins"]`
2. **Install**: Plugin installed via pip (`pip install structum-my-plugin`)
3. **Discovery**: Entry point system automatically loads the plugin class
4. **Type Detection**: Official plugins (`structum_*`) auto-detected and tagged as [OFFICIAL]
5. **Register**: Plugin registered in `PluginRegistry` with type metadata
6. **Conflict Check**: Warns if a plugin with the same name already exists
7. **Enable/Disable**: Respects user preferences from config file

### Official vs External Detection

```python
# In structum/plugins/loader.py
is_official = plugin_cls.__module__.startswith("structum_")

# Result:
# structum_latex → [OFFICIAL]
# my_plugin → [EXTERNAL]
```

### No Manual Registration Required

Simply:
1. Create your plugin structure
2. Add entry point in `pyproject.toml`
3. Install with `pip install -e .`
4. Plugin automatically discovered and loaded

No filesystem scanning, no .dev markers, no manual registry updates!

---

## Best Practices

1. **Naming Convention**: Use `structum_*` for official plugins, descriptive names for external
2. **Separation of Concerns**: Keep CLI code in `commands/`, logic in `core/`
3. **Type Hints**: Use type hints for all functions
4. **Entry Points**: Always define proper entry points in `pyproject.toml`
5. **Error Handling**: Use Typer's error handling and Rich for output
6. **Testing**: Write tests for your core logic
7. **Documentation**: Include docstrings and a comprehensive README
8. **Metadata**: Provide complete plugin metadata (name, version, description, author, category)
