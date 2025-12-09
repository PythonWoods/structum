# Structum Core

> Enterprise-grade plugin framework for building extensible CLI applications

## Overview

**Structum Core** is a minimal, high-performance plugin framework that provides the infrastructure for building plugin-based CLI applications. It handles plugin discovery, loading, configuration, monitoring, and security.

## Features

- 🔌 **Plugin System**: Automatic discovery via entry points
- 📊 **Monitoring**: Built-in metrics and telemetry
- 🔒 **Security**: Plugin sandboxing and validation
- ⚙️ **Configuration**: Multi-environment config management
- 🏥 **Health Checks**: Plugin health monitoring
- 🚀 **Performance**: < 50ms startup time
- 📈 **Scalable**: Support for 1000+ plugins

## Installation

```bash
# Core framework only
pip install structum-core

# With monitoring features
pip install structum-core[monitoring]

# With security features
pip install structum-core[security]

# Full installation
pip install structum-core[monitoring,security]
```

## Quick Start

### Using Structum Core

```python
from structum.cli.bootstrap import create_app

# Create your CLI app
app = create_app(
    name="myapp",
    description="My Plugin-Based Application"
)

if __name__ == "__main__":
    app()
```

### Creating a Plugin

```bash
# Generate plugin skeleton
structum plugins new my-plugin --output ./plugins/

# Install in development mode
cd plugins/my-plugin
pip install -e .
```

### Plugin Structure

```python
from structum.plugins.sdk import PluginBase
import typer

class MyPlugin(PluginBase):
    name = "my-plugin"
    version = "1.0.0"
    category = "utility"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer, help_panel: str | None = None) -> None:
        """Register CLI commands."""
        # Register your commands here
        pass
```

## Architecture

Structum Core provides:

1. **Plugin Loader**: Discovers and loads plugins via entry points
2. **Plugin Registry**: Manages plugin lifecycle and metadata
3. **Configuration Manager**: Handles application and plugin configuration
4. **Monitoring System**: Tracks performance and health metrics
5. **Security Framework**: Validates and sandboxes plugins

## Core Philosophy

- **Minimal Core**: Only essential plugin infrastructure
- **Zero Business Logic**: All functionality via plugins
- **Enterprise Ready**: Production-grade features
- **Developer Friendly**: Clear APIs and excellent DX

## Documentation

Full documentation available at: [https://pythonwoods.github.io/structum/](https://pythonwoods.github.io/structum/)

## License

Apache 2.0 - See [LICENSE](LICENSE) for details.

## Part of Structum Ecosystem

- **structum-core**: Plugin framework (this package)
- **structum**: Meta-package with official plugins
- **structum_tree**: Directory tree visualization plugin
- **structum_archive**: Code archiving plugin
- **structum_clean**: Cleanup utilities plugin
- **structum_docs**: Documentation management plugin
- **structum_plugins**: Plugin management interface
