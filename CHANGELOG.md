# Changelog

All notable changes to this project will be documented in this file.

This project follows **Conventional Commits**  
and automatic release generation via **release-please**.

---

## [Unreleased]

### ✨ Features

#### Core Commands

- **Code Archiving** (`structum archive`): Export source code to Markdown files
  - Single file or split by folder output
  - Filter by file extension
- **Clean Command** (`structum clean`): Remove `__pycache__` directories recursively
- **Entry Point**: Run via `python -m structum`

#### Plugin System

- **Plugin SDK**: `PluginBase` abstract class for standardized plugin development
- **Plugin Registry**: Centralized plugin management with validation
- **Plugin Auto-Discovery**: Built-in plugins automatically discovered via filesystem scanning
  - Uses introspection to find `PluginBase` subclasses
  - Consistent with external plugin entry point mechanism
  - Zero-configuration plugin registration
  - Support for disabling plugins with underscore prefix (`_plugin_name`)
- **Development Mode (.dev marker)** (2025-12-06): Hybrid system for work-in-progress plugins
  - New plugins auto-created with `.dev` marker file
  - Dev-mode plugins NOT registered (invisible by default)
  - Visible with `structum plugins list --show-dev` flag
  - Remove `.dev` file to promote plugin to production
  - Better developer workflow with clear visibility and control
- **Enterprise Plugin Template** (2025-12-06): Professional skeleton for new plugins
  - Command: `run` (replaces "hello world" example)
  - Arguments: Path with validation and resolution
  - Options: `--output`, `--dry-run`, `--verbose`
  - Full type hints with `Path`, `Optional`
  - Comprehensive docstrings with Args/Returns
  - TODO markers for clear implementation guidance
  - Separation of concerns: CLI in `commands/`, logic in `core/`
- **Plugin CLI**: Full management commands
  - `structum plugins list` - List plugins with category/status
  - `structum plugins list --show-dev` - Include dev-mode plugins
  - `structum plugins info <name>` - Show plugin details
  - `structum plugins enable/disable <name>` - Manage plugin state
  - `structum plugins new <name>` - Generate skeleton (creates in dev mode)
- **Plugin Categories**: `analysis`, `export`, `formatting`, `utility`
- **Plugin Validation**: Auto-validates `name`, `version`, `category` on load
- **Configuration Persistence**: State stored in `~/.config/structum/config.json`

#### Documentation

- **MkDocs Integration**: Professional documentation site with Material theme
- **Docs Commands**: `structum docs serve` and `structum docs deploy`

#### Planned (Phase 4)

- **LaTeX Export**: Academic document generation (IEEE, ACM styles)

### 🔨 Refactoring

- Modular CLI architecture (`cli/commands/` structure)
- Separated core business logic from CLI interface
- Plugin `__init__.py` now only exports, logic in `plugin.py`
- Modern type hints (Python 3.11+ PEP 585/604)
- Migrated CLI from Click to Typer

### 📚 Documentation

- Comprehensive technical architecture (`ARCHITECTURE.md`)
- Development roadmap (`ROADMAP.md`)
- Plugin development guide (`docs/development/plugins.md`)
- CLI commands reference (`docs/cli/commands.md`)
- Context-aware help messages in `plugins new`

### 🔧 Chores

- Dynamic versioning with hatchling
- Dependabot configuration for pip and GitHub Actions
- REUSE/SPDX compliance

### 🐛 Fixes

- **Archive Command**:
  - `structum archive` now correctly includes all files if no `--ext` is provided (previously found 0 files).
  - Fixed crash when `--output` is an existing directory in single-file mode (defaults to `archive.md`).
  - Directory tree in archive now respects `--ignore` and `--ext` filters.

- **CLI Help Behavior** (2025-12-06):
  - Fixed inconsistent help behavior for command groups (`docs`, `plugins`, `sample`)
  - Running `structum docs` or `structum plugins` without subcommand now shows help instead of "Missing command." error
  - Added `no_args_is_help=True` to all command groups for consistent UX
  - Updated plugin skeleton template to include this fix automatically

- **Plugin Template** (2025-12-06):
  - Fixed `IsADirectoryError` when `--output` points to a directory in enterprise template
  - Template now automatically generates `results.txt` filename when output is a directory
  - Maintains backward compatibility with file paths

---
