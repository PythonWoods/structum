# Getting Started with Structum

Welcome to Structum v2.0 - an enterprise-grade plugin framework for building extensible CLI applications.

## Installation

### Core Framework Only

Install just the core framework (no commands, only infrastructure):

```bash
pip install structum
```

### With All Official Plugins (Recommended)

Install core + all official plugins:

```bash
pip install structum[full]
```

This includes:

- **tree**: Directory tree visualization
- **archive**: Code archiving to Markdown
- **clean**: Cleanup utilities (`__pycache__` removal)
- **docs**: Documentation management (MkDocs integration)
- **plugins**: Plugin management tools

### Selective Installation

Install only the plugins you need:

```bash
# Core + tree + archive plugins
pip install structum[tree,archive]

# Core + docs plugin only
pip install structum[docs]
```

## Quick Start

### Visualize Directory Structure

```bash
# Basic tree with emoji theme
structum tree .

# Show statistics
structum tree . --stats

# Filter by extension
structum tree . --ext py,md --depth 3

# ASCII theme (for copying to documentation)
structum tree . --theme ascii
```

### Archive Code to Markdown

```bash
# Archive Python files
structum archive . --output code.md --ext py

# Archive with directory tree included
structum archive . --output archive.md --ext py,md --tree

# Split by folder
structum archive src --split-folder --output docs/
```

### Clean Project

```bash
# Remove all __pycache__ directories
structum clean .

# Skip virtual environments
structum clean . --skip-venv
```

### Manage Documentation

```bash
# Serve docs locally (requires MkDocs)
structum docs serve

# Deploy to GitHub Pages
structum docs deploy
```

### Manage Plugins

```bash
# List installed plugins
structum plugins list

# Get plugin information
structum plugins info tree

# Generate new plugin skeleton
structum plugins new my-tool --category utility --output ~/projects/

# Enable/disable plugins
structum plugins disable my-tool
structum plugins enable my-tool
```

## Plugin Architecture

Structum v2.0 uses a **plugin-first architecture**:

- **Core framework** provides only infrastructure (plugin system, config, monitoring, security)
- **All functionality** is delivered via plugins
- **Plugins auto-discovered** via Python entry points
- **No manual registration** needed

### Creating Your First Plugin

Use the built-in generator:

```bash
structum plugins new my-awesome-tool --category utility
cd my-awesome-tool
pip install -e .
```

Your plugin is automatically discovered and available:

```bash
structum my-awesome-tool --help
```

See [Plugin Development Guide](development/plugins.md) for details.

## Available Themes

Structum tree visualization supports multiple themes:

| Theme    | Description                      | Use Case                    |
|----------|----------------------------------|-----------------------------|
| **emoji** | Standard emojis (📂, 🐍)        | Terminal output (default)   |
| **nerd**  | Nerd Font glyphs (, )         | Power users                 |
| **ascii** | Plain text characters            | Documentation, LLM prompts  |

## Configuration

Structum stores configuration in `~/.config/structum/config.json`:

```json
{
  "plugins": {
    "my-plugin": {
      "enabled": true
    }
  }
}
```

## Next Steps

- [CLI Reference](cli/commands.md) - Complete command documentation
- [Plugin Development](development/plugins.md) - Create your own plugins
- [Architecture V2.0](architecture/v2.md) - Understand the v2.0 design
- [Architecture V3 Vision](architecture/v3/) - Future architectural vision
- [Contributing](../CONTRIBUTING.md) - Contribute to Structum

## Need Help?

- **Documentation**: Full guide at [pythonwoods.github.io/structum](https://pythonwoods.github.io/structum/)
- **Issues**: Report bugs at [GitHub Issues](https://github.com/pythonwoods/structum/issues)
- **Discussions**: Ask questions in [GitHub Discussions](https://github.com/pythonwoods/structum/discussions)
