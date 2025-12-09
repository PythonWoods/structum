# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin skeleton generator."""

from pathlib import Path

PYPROJECT_TEMPLATE = '''[project]
name = "{pypi_name}"
version = "{version}"
description = "{description}"
requires-python = ">=3.11"
authors = [
    {{name = "{author_name}", email = "{author_email}"}},
]
readme = "README.md"
license = {{text = "{license}"}}
keywords = ["structum", "plugin", "{name}"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "structum>=0.2.0",
    "typer>=0.12.0",
    "rich>=13.0",
]

[project.entry-points."structum.plugins"]
{name} = "{package_name}:{class_name}"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/{package_name}"]
'''

README_TEMPLATE = '''# {title}

{description}

## Development Setup

This plugin is currently in development. To install it locally:

```bash
cd {name}
pip install -e .
```

The `-e` flag installs in "editable" mode, so changes to the code take effect immediately.

## Usage

After installation, the plugin will be automatically available in Structum:

```bash
# List all plugins (verify installation)
structum plugins list

# Show plugin info
structum {name} info

# TODO: Add your custom commands here
# structum {name} <your-command>
```

## Development

### Project Structure

```
{name}/
├── pyproject.toml          # Package configuration
├── README.md               # This file
├── .gitignore             # Git ignore rules
└── src/
    └── {package_name}/
        ├── __init__.py    # Package entry point
        ├── plugin.py      # Plugin class definition
        ├── commands/      # CLI commands
        │   ├── __init__.py
        │   └── main.py    # Main command implementation
        └── core/          # Business logic
            ├── __init__.py
            └── logic.py   # Core functionality
```

### Adding Commands

Edit `src/{package_name}/commands/main.py` to add new commands:

```python
@app.command("mycommand")
def my_command(path: Path = typer.Argument(...)):
    """My custom command."""
    from ..core.logic import process_something
    result = process_something(path)
    typer.echo(result)
```

### Testing Locally

```bash
# Install in editable mode
pip install -e .

# Test your plugin
structum {name} info
structum plugins list
```

## Publishing to PyPI

Once your plugin is ready, you can publish it to PyPI:

```bash
pip install build twine
python -m build
twine upload dist/*
```

Users will then be able to install it with:

```bash
pip install {pypi_name}
```

## License

{license}

## Author

{author_name} <{author_email}>
'''

GITIGNORE_TEMPLATE = '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS
.DS_Store
Thumbs.db
'''

PLUGIN_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Package."""

from .plugin import {class_name}

__all__ = ["{class_name}"]
'''

PLUGIN_CLASS_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import main


class {class_name}(PluginBase):
    """{description}"""

    name = "{name}"
    version = "{version}"
    category = "{category}"
    description = "{description}"
    author = "{author_name}"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(main.app, name="{name}", rich_help_panel=help_panel)
'''

COMMANDS_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands Package."""
'''

COMMANDS_MAIN_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands."""

import typer

# Configuration for command behavior
# no_args_is_help=True: Show help when plugin is called without arguments
# no_args_is_help=False: Allow plugin to run without arguments (useful for default actions)
app = typer.Typer(
    help="{description}",
    no_args_is_help=True  # Set to False if your plugin has a default action
)


@app.command("info")
def info_command() -> None:
    """Display plugin information and metadata."""
    from structum.plugins.utils import get_current_plugin_metadata

    # Read metadata from pyproject.toml (via importlib.metadata)
    meta = get_current_plugin_metadata()

    output_lines = [
        f"✓ {{meta['description']}}",
        "",
        f"Version: {{meta['version']}}",
        f"Author: {{meta['author']}}",
        f"License: {{meta['license']}}",
        "",
        "Available commands:",
        "  info     - Display this information",
        "  # TODO: Add your commands here",
    ]
    typer.echo("\\n".join(output_lines))


# TODO: Implement your plugin commands here
# Example:
#
# @app.command("process")
# def process_command(
#     path: Path = typer.Argument(..., help="Path to process"),
#     output: Path | None = typer.Option(None, "--output", "-o"),
# ) -> None:
#     \"\"\"Process files.\"\"\"
#     from ..core.logic import process
#     result = process(path, output, plugin_info=PLUGIN_INFO)
#     typer.echo(result)
'''

CORE_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Package."""
'''

CORE_LOGIC_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Logic."""

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
#     result = {{
#         "plugin": plugin_name,
#         "processed": str(path),
#         "status": "success",
#     }}
#
#     return result
'''


def generate_plugin_skeleton(
    name: str,
    output_dir: Path,
    category: str = "utility",
    author_name: str = "Your Name",
    author_email: str = "your.email@example.com",
    description: str | None = None,
    version: str = "0.1.0",
    license_type: str = "Apache-2.0",
) -> Path:
    """Generate a complete plugin package skeleton with src/ layout.

    Args:
        name: Plugin name (kebab-case, e.g., 'my-plugin').
        output_dir: Directory to create plugin package in.
        category: Plugin category (analysis, export, formatting, utility).
        author_name: Author's name.
        author_email: Author's email address.
        description: Plugin description (auto-generated if not provided).
        version: Initial version (default: 0.1.0).
        license_type: License type (default: Apache-2.0).

    Returns:
        Path to created plugin root directory.
    """
    # Convert names
    package_name = name.replace("-", "_")
    class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"
    title = name.replace("-", " ").title()
    if description is None:
        description = f"{title} plugin for Structum"
    pypi_name = f"structum-plugin-{name}"

    # Create standalone plugin project directory
    plugin_root = output_dir / name
    src_dir = plugin_root / "src"
    plugin_dir = src_dir / package_name
    commands_dir = plugin_dir / "commands"
    core_dir = plugin_dir / "core"

    # Create all directories
    plugin_root.mkdir(parents=True, exist_ok=True)
    src_dir.mkdir(exist_ok=True)
    plugin_dir.mkdir(exist_ok=True)
    commands_dir.mkdir(exist_ok=True)
    core_dir.mkdir(exist_ok=True)

    context = {
        "name": name,
        "package_name": package_name,
        "class_name": class_name,
        "title": title,
        "description": description,
        "category": category,
        "pypi_name": pypi_name,
        "author_name": author_name,
        "author_email": author_email,
        "version": version,
        "license": license_type,
    }

    # Write package configuration files
    (plugin_root / "pyproject.toml").write_text(PYPROJECT_TEMPLATE.format(**context))
    (plugin_root / "README.md").write_text(README_TEMPLATE.format(**context))
    (plugin_root / ".gitignore").write_text(GITIGNORE_TEMPLATE)

    # Write Python package files
    (plugin_dir / "__init__.py").write_text(PLUGIN_INIT_TEMPLATE.format(**context))
    (plugin_dir / "plugin.py").write_text(PLUGIN_CLASS_TEMPLATE.format(**context))
    (commands_dir / "__init__.py").write_text(COMMANDS_INIT_TEMPLATE.format(**context))
    (commands_dir / "main.py").write_text(COMMANDS_MAIN_TEMPLATE.format(**context))
    (core_dir / "__init__.py").write_text(CORE_INIT_TEMPLATE.format(**context))
    (core_dir / "logic.py").write_text(CORE_LOGIC_TEMPLATE.format(**context))

    return plugin_root
