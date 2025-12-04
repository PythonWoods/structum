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

app = typer.Typer(help="{description}")


@app.command("hello")
def hello(name: str = "world") -> None:
    """Say hello."""
    typer.echo(f"Hello, {{name}}!")
'''

CORE_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Package."""
'''

CORE_LOGIC_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Logic."""


def example_function() -> str:
    """Example function."""
    return "Hello from {name} plugin!"
'''


def generate_plugin_skeleton(name: str, output_dir: Path) -> Path:
    """Generate a plugin skeleton.

    Args:
        name: Plugin name (kebab-case).
        output_dir: Directory to create plugin in.

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
    }

    # Write files
    (plugin_dir / "__init__.py").write_text(PLUGIN_INIT_TEMPLATE.format(**context))
    (plugin_dir / "plugin.py").write_text(PLUGIN_CLASS_TEMPLATE.format(**context))
    (commands_dir / "__init__.py").write_text(COMMANDS_INIT_TEMPLATE.format(**context))
    (commands_dir / "main.py").write_text(COMMANDS_MAIN_TEMPLATE.format(**context))
    (core_dir / "__init__.py").write_text(CORE_INIT_TEMPLATE.format(**context))
    (core_dir / "logic.py").write_text(CORE_LOGIC_TEMPLATE.format(**context))

    return plugin_dir
