# structum_plugins

Official plugin management plugin for Structum.

## Description

This plugin provides comprehensive plugin management functionality for the Structum framework. It allows you to list, enable, disable, inspect, and create new plugins through an intuitive CLI interface.

## Features

- **Plugin Discovery**: List all installed plugins (official and community)
- **Plugin Information**: View detailed metadata about any plugin
- **Plugin Control**: Enable or disable plugins without uninstalling
- **Plugin Generation**: Create new plugin skeletons with interactive prompts
- **Rich Output**: Beautiful tables and formatted output using Rich
- **Type Classification**: Distinguish between official and community plugins

## Installation

```bash
pip install structum_plugins
```

Or install as part of the full Structum bundle:

```bash
pip install structum
```

## Usage

### List All Plugins

View all installed plugins with their status and metadata:

```bash
structum plugins list
```

Output shows:
- Plugin name
- Type (OFFICIAL or COMMUNITY)
- Category
- Version
- Status (enabled/disabled)
- Description

### Get Plugin Information

Show detailed information about a specific plugin:

```bash
structum plugins info <plugin-name>
```

Example:
```bash
structum plugins info tree
```

### Enable/Disable Plugins

Control plugin activation without uninstalling:

```bash
# Disable a plugin
structum plugins disable my-plugin

# Re-enable a plugin
structum plugins enable my-plugin
```

### Create New Plugin

Generate a complete plugin skeleton with interactive prompts:

```bash
structum plugins new my-awesome-plugin --output ~/projects/ --category utility
```

You'll be prompted for:
- Author name
- Author email
- Plugin description
- Version
- License

The command creates a complete plugin package structure:

```
my-awesome-plugin/
├── pyproject.toml          # Package configuration
├── README.md               # Documentation
├── .gitignore             # Git ignore rules
└── src/
    └── my_awesome_plugin/
        ├── __init__.py    # Package entry
        ├── plugin.py      # Plugin class
        ├── commands/      # CLI commands
        │   ├── __init__.py
        │   └── main.py
        └── core/          # Business logic
            ├── __init__.py
            └── logic.py
```

## Commands Reference

| Command | Description |
|---------|-------------|
| `plugins list` | List all installed plugins |
| `plugins info <name>` | Show detailed plugin information |
| `plugins enable <name>` | Enable a disabled plugin |
| `plugins disable <name>` | Disable a plugin |
| `plugins new <name>` | Create new plugin skeleton |

## Plugin Categories

When creating new plugins, choose from these categories:

- **analysis** - Code analysis and inspection tools
- **export** - Export and format conversion tools
- **formatting** - Code formatting and style tools
- **utility** - General utility and helper tools

## Plugin Types

Plugins are automatically classified as:

- **[OFFICIAL]** - Plugins with names starting with `structum_*` (maintained by PythonWoods)
- **[COMMUNITY]** - All other plugins (community-maintained)

## Development

This plugin integrates with:
- `structum.plugins.registry.PluginRegistry` - For plugin discovery and metadata
- `structum.plugins.skeleton` - For plugin generation
- `structum.config.manager` - For plugin enable/disable state
- `structum.plugins.sdk` - For plugin categories and base classes

## License

Apache-2.0

## Author

PythonWoods
