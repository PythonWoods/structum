# Structum

**Enterprise Plugin Framework - Complete Bundle**

Structum is a minimalist, enterprise-grade plugin framework for Python. This meta-package bundles all official Structum plugins, providing a complete toolkit for code analysis, documentation, and project management.

## What's Included

Installing `structum` gives you everything:

### Core Framework
- **structum-core** - Minimal plugin framework with monitoring, security, and configuration management

### Official Plugins (All Included)
- **structum_tree** - Directory tree visualization with multiple themes
- **structum_archive** - Code archiving to Markdown with syntax highlighting
- **structum_clean** - Cleanup utilities for `__pycache__` directories
- **structum_docs** - Documentation management with MkDocs integration
- **structum_plugins** - Plugin management and creation tools

## Installation

### Complete Installation (Recommended)

Get everything with a single command:

```bash
pip install structum
```

This installs the core framework plus all 5 official plugins.

### Minimal Installation

Want just the framework? Install only the core:

```bash
pip install structum-core
```

### Selective Installation

Install only what you need:

```bash
# Core + specific plugins
pip install structum-core structum_tree structum_archive

# Or mix and match
pip install structum-core structum_docs structum_plugins
```

## Quick Start

After installation, verify everything is working:

```bash
# Show all available commands
structum --help

# List installed plugins
structum plugins list

# Try some commands
structum tree . --theme emoji
structum clean .
structum plugins new my-plugin --output ~/projects/
```

## Features

### 🌳 Tree Visualization
```bash
structum tree . --theme nerd --depth 3 --ext py,md
```
- Multiple themes (emoji, nerd fonts, ASCII)
- File extension filtering
- Directory exclusion
- Depth control
- Statistics

### 📦 Code Archiving
```bash
structum archive src --output code.md --ext py
```
- Export code to Markdown with syntax highlighting
- Auto-generated Table of Contents
- Directory tree visualization
- Split by folder or file type

### 🧹 Project Cleanup
```bash
structum clean . --skip-venv
```
- Recursively remove `__pycache__` directories
- Optional virtual environment protection
- Verbose/quiet modes

### 📚 Documentation Management
```bash
structum docs serve
structum docs deploy --message "Update docs"
```
- Serve documentation locally with live reload
- Deploy to GitHub Pages
- MkDocs integration

### 🔌 Plugin Management
```bash
structum plugins list
structum plugins new my-tool --category utility
```
- List all installed plugins
- Enable/disable plugins
- Create new plugin skeletons
- Interactive plugin generation

## Architecture

Structum follows a plugin-first architecture:

```
structum-core (foundation)
    ↓
    ├─→ structum_tree
    ├─→ structum_archive (depends on tree)
    ├─→ structum_clean
    ├─→ structum_docs
    └─→ structum_plugins
```

All functionality is delivered through plugins. The core provides:
- Plugin discovery via entry points
- Plugin registry and metadata management
- Configuration management
- Monitoring and metrics
- Security validation

## Creating Plugins

Structum makes it easy to create your own plugins:

```bash
# Generate a plugin skeleton
structum plugins new awesome-tool --output ~/projects/ --category utility

# Install and test
cd ~/projects/awesome-tool
pip install -e .
structum awesome-tool --help
```

Your plugin is automatically discovered and registered!

## Requirements

- Python 3.11 or higher
- Dependencies are automatically installed

## Documentation

- **Homepage**: https://github.com/pythonwoods/structum
- **Documentation**: https://pythonwoods.github.io/structum/
- **Plugin SDK**: See individual plugin READMEs

## Version

This meta-package tracks the Structum ecosystem version. Currently: **v2.0.0-alpha.1**

All included plugins are at the same version for compatibility.

## Package Structure

This is a meta-package with minimal code. It exists to:
1. Provide a single installation entry point
2. Ensure version compatibility across all official plugins
3. Simplify dependency management

The actual functionality lives in the individual packages.

## License

Apache-2.0

## Author

PythonWoods

## Contributing

Contributions are welcome! Please see our contributing guidelines in the main repository.

## Support

- **Issues**: https://github.com/pythonwoods/structum/issues
- **Discussions**: https://github.com/pythonwoods/structum/discussions
