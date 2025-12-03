# Plugin System

Structum features a robust plugin system that allows extending its functionality. Plugins can add new commands or modify existing behavior.

## Built-in Plugins

Structum comes with some built-in plugins. For example, the `sample` plugin demonstrates how to add commands.

```bash
structum sample hello
# Output: 👋 Hello, dev! This command was loaded as a plugin.
```

## Creating External Plugins

You can create your own plugins and distribute them as Python packages. Structum uses the standard Python entry point mechanism to discover plugins.

### 1. Create a Plugin Module

Create a Python module (e.g., `my_plugin.py`) with a `register` function that accepts the Typer `app` instance.

```python
import typer

def register(app: typer.Typer):
    plugin_app = typer.Typer(help="My custom commands.")
    app.add_typer(plugin_app, name="custom")

    @plugin_app.command("greet")
    def greet(name: str):
        print(f"Hello from custom plugin, {name}!")
```

### 2. Configure Entry Points

In your plugin's `pyproject.toml`, define an entry point under the `structum.plugins` group.

```toml
[project]
name = "structum-extra-tools"
dependencies = ["structum"]

[project.entry-points."structum.plugins"]
extra_tools = "my_plugin:register"
```

### 3. Install and Run

Install your plugin package in the same environment as Structum.

```bash
pip install .
```

Structum will automatically discover and load your plugin.

```bash
structum custom greet World
# Output: Hello from custom plugin, World!
```

## How it Works

The plugin loader performs the following steps:

1.  **Built-in Plugins**: Loads internal plugins from `structum.plugins`.
2.  **External Plugins**: Scans for entry points in the `structum.plugins` group.
    ```python
    eps = entry_points(group="structum.plugins")
    ```
3.  **Registration**: For each discovered plugin, it loads the entry point and executes the registered function, passing the main `app` instance.
    ```python
    plugin = ep.load()
    plugin(app)
    ```
