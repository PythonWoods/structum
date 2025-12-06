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
- `commands/main.py` – CLI commands (default: `run` command)
- `core/logic.py` – Business logic

**Development Mode (.dev marker):**

New plugins are created in development mode with a `.dev` marker file. This means:
- ✅ Plugin exists and can be inspected
- ❌ Plugin is NOT registered (invisible in normal plugin list)
- 🔍 Visible with `structum plugins list --show-dev`

### Step 3: Test Your Plugin

**While in development mode:**

```bash
# View your dev-mode plugin
structum plugins list --show-dev

# The plugin will show with [DEV MODE] status
```

**When ready for production:**

```bash
# Remove the .dev marker
rm src/structum/plugins/my_plugin/.dev

# Verify it's now registered
structum plugins list

# Test your plugin
structum my-plugin run
```

> **Note**: The `.dev` marker prevents accidental use of incomplete plugins. Remove it only when your plugin is production-ready.

### Step 4: Submit a Pull Request

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

Define your CLI commands using the enterprise-grade `run` template:

```python
from pathlib import Path

import typer

from ..core.logic import process

app = typer.Typer(
    help="My plugin commands.",
    no_args_is_help=True  # Show help when no subcommand is provided
)


@app.command("run")
def run_command(
    path: Path = typer.Argument(
        Path("."),
        help="Path to process",
        exists=True,
        resolve_path=True,
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path (optional)",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Preview changes without applying them",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    ),
) -> None:
    """Execute the plugin's main functionality."""
    result = process(
        path=path,
        output=output,
        dry_run=dry_run,
        verbose=verbose,
    )

    if verbose:
        typer.echo(f"[my-plugin] Processing completed")

    typer.echo(result)
```

**Template Features:**
- ✅ `Path` arguments with validation
- ✅ Enterprise options: `--output`, `--dry-run`, `--verbose`
- ✅ Type safety with type hints
- ✅ Clear separation: CLI → core logic
- ✅ Professional parameter names

> **Important**: Always include `no_args_is_help=True` to maintain consistency with other Structum commands. This ensures users see helpful command lists instead of error messages when invoking your plugin without arguments.

#### `core/logic.py`

Keep business logic separate from CLI with the enterprise template:

```python
from pathlib import Path


def process(
    path: Path,
    output: Path | None = None,
    dry_run: bool = False,
    verbose: bool = False,
) -> str:
    """Process the given path and return results.

    Args:
        path: Path to process
        output: Optional output file path
        dry_run: If True, preview changes without applying
        verbose: Enable verbose logging

    Returns:
        Result message
    """
    if dry_run:
        return f"[DRY RUN] Would process: {path}"

    if verbose:
        print(f"Processing {path}...")

    # TODO: Add your implementation here
    result = f"Processed {path} successfully"

    if output:
        output.write_text(result)
        return f"Results written to {output}"

    return result
```

**Template includes:**
- ✅ Full type hints
- ✅ Comprehensive docstring
- ✅ Dry-run support
- ✅ Verbose logging
- ✅ Optional file output
- ✅ TODO markers for implementation

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

Structum uses different discovery mechanisms for built-in and external plugins to provide a consistent developer experience.

### Built-in Plugin Discovery

Built-in plugins are **automatically discovered** via filesystem scanning:

1. **Scan**: The loader scans `src/structum/plugins/` for directories
2. **Filter**: Skips directories starting with `_` (e.g., `_wip_plugin`) and special folders
3. **Import**: Dynamically imports modules with a `plugin.py` file
4. **Check**: Looks for `.dev` marker file
5. **Introspect**: Uses reflection to find `PluginBase` subclasses
6. **Register**: Automatically registers production plugins (without `.dev` marker)
7. **Track**: Stores dev-mode plugins separately for `--show-dev` inspection

**No manual registration required!** Simply create your plugin structure and it's immediately available.

**Development Mode Options:**

| Method | Use Case | Visibility |
|--------|----------|------------|
| `.dev` marker | **Recommended** - Work in progress | Hidden by default, `--show-dev` to view |
| `_` prefix | Quick temporary disable | Completely invisible (not even discovered) |

**Workflow comparison:**
```bash
# .dev marker (Recommended)
structum plugins new my-plugin  # Auto-creates .dev
structum plugins list --show-dev  # Visible in dev mode
rm .dev  # Promote to production

# _ prefix (Old method)
mv my_plugin _my_plugin  # Disable
mv _my_plugin my_plugin  # Enable
```

### External Plugin Discovery

External plugins are discovered via **entry points** (standard Python packaging):

1. **Entry Point**: Defined in `pyproject.toml` under `[project.entry-points."structum.plugins"]`
2. **Install**: Plugin is installed via pip (`pip install structum-my-plugin`)
3. **Discovery**: Entry point system loads the plugin class
4. **Register**: Automatically registered like built-in plugins

Both mechanisms ensure **zero configuration** for plugin developers.

---

## Best Practices

1. **Separation of Concerns**: Keep CLI code in `commands/`, logic in `core/`
2. **Type Hints**: Use type hints for all functions
3. **Error Handling**: Use Typer's error handling and Rich for output
4. **Testing**: Write tests for your core logic
5. **Documentation**: Include docstrings and a README
6. **Auto-discovery Friendly**: Follow the standard plugin structure for automatic registration
