# Modules

## Core (`src/structum/core/`)
Contains the business logic of the application. These modules are independent of the CLI interface.

*   `tree.py`: Logic for directory traversal and visualization.
*   `archive.py`: Logic for collecting files and generating markdown archives.
*   `clean.py`: Logic for cleaning artifacts.
*   `docs.py`: Logic for documentation management.
*   `config.py`: Configuration management and persistence.

## CLI (`src/structum/cli/`)
Handles the user interface using Typer.

*   `main.py`: Entry point and command registration.
*   `commands/`: Individual command definitions.

## Plugins (`src/structum/plugins/`)
Manages the plugin system.

*   `sdk.py`: Plugin SDK defining `PluginBase` class.
*   `registry.py`: Central plugin registry.
*   `loader.py`: Plugin discovery and loading.
*   `sample/`: Example plugin demonstrating the architecture.
