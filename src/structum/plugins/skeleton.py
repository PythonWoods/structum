# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin skeleton generator."""

from pathlib import Path

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
    version = "0.1.0"
    category = "{category}"
    description = "{description}"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(main.app, name="{name}")
'''

COMMANDS_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands Package."""
'''

COMMANDS_MAIN_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands."""

import typer

app = typer.Typer(
    help="{description}",
    no_args_is_help=True
)

# Plugin metadata
PLUGIN_INFO = {{
    "name": "{name}",
    "version": "0.1.0",
    "description": "{description}",
    "category": "{category}",
}}


@app.command("info")
def info_command() -> None:
    """Display plugin information and metadata."""
    output_lines = [
        f"✓ {{PLUGIN_INFO['name']}} v{{PLUGIN_INFO['version']}}",
        f"  {{PLUGIN_INFO['description']}}",
        "",
        f"Category: {{PLUGIN_INFO['category']}}",
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
    name: str, output_dir: Path, category: str = "utility"
) -> Path:
    """Generate a plugin skeleton.

    Args:
        name: Plugin name (kebab-case).
        output_dir: Directory to create plugin in.
        category: Plugin category (analysis, export, formatting, utility).

    Returns:
        Path to created plugin directory.
    """
    # Convert name to class name
    class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"
    description = f"{name.replace('-', ' ').title()} plugin"

    # Create directories
    plugin_dir = output_dir / name.replace("-", "_")
    commands_dir = plugin_dir / "commands"
    core_dir = plugin_dir / "core"

    plugin_dir.mkdir(parents=True, exist_ok=True)
    commands_dir.mkdir(exist_ok=True)
    core_dir.mkdir(exist_ok=True)

    context = {
        "name": name,
        "class_name": class_name,
        "description": description,
        "category": category,
    }

    # Write files
    (plugin_dir / "__init__.py").write_text(PLUGIN_INIT_TEMPLATE.format(**context))
    (plugin_dir / "plugin.py").write_text(PLUGIN_CLASS_TEMPLATE.format(**context))
    (commands_dir / "__init__.py").write_text(COMMANDS_INIT_TEMPLATE.format(**context))
    (commands_dir / "main.py").write_text(COMMANDS_MAIN_TEMPLATE.format(**context))
    (core_dir / "__init__.py").write_text(CORE_INIT_TEMPLATE.format(**context))
    (core_dir / "logic.py").write_text(CORE_LOGIC_TEMPLATE.format(**context))

    # Create .dev marker for built-in plugins (development mode by default)
    # Check if we're in the structum project (creating a built-in plugin)
    is_builtin = "structum" in str(output_dir) and "plugins" in str(output_dir)
    if is_builtin:
        dev_marker = plugin_dir / ".dev"
        dev_marker.write_text(
            "# This file marks the plugin as being in development mode.\n"
            "# The plugin will not be registered until this file is removed.\n"
            "# Remove this file when the plugin is ready for production use.\n"
        )

    return plugin_dir
