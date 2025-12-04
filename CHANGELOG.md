# Changelog

All notable changes to this project will be documented in this file.

This project follows **Conventional Commits**  
and automatic release generation via **release-please**.

---

## [Unreleased]

### ✨ Features
- **Plugin System**: Full plugin architecture with SDK, registry, and CLI management
  - `structum plugins list` - List installed plugins with category and status
  - `structum plugins info <name>` - Show plugin details
  - `structum plugins enable/disable <name>` - Manage plugin state
  - `structum plugins new <name>` - Generate plugin skeleton with smart defaults
- **Plugin Categories**: Organize plugins into `analysis`, `export`, `formatting`, `utility`
- **Plugin Validation**: Automatic validation of plugin attributes on load
- **Configuration Persistence**: Plugin state stored in `~/.config/structum/config.json`

### 🐛 Bug Fixes
- …

### 🚀 Performance
- …

### 🔨 Refactoring
- Modular CLI architecture with `cli/commands/` structure
- Plugin `__init__.py` now only exports, logic moved to `plugin.py`
- Separated core business logic from CLI interface

### 🧪 Tests
- …

### 📚 Documentation
- Comprehensive plugin development guide (`docs/development/plugins.md`)
- Updated CLI commands documentation
- Context-aware help messages in `plugins new`

### 🔧 Chores
- …

---
