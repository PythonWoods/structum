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
- **Plugin Registry**: Centralized plugin management with validation and type tracking
  - **PluginType enum** (2025-12-08): OFFICIAL vs EXTERNAL distinction
  - **PluginMetadata dataclass** (2025-12-08): Track plugin type, module path, source
  - Conflict detection with warning messages
  - `list_by_type()` method for grouping plugins
  - `list_plugins_detailed()` with full metadata including type
- **Plugin Loading** (2025-12-08): External plugins via entry points only
  - **BREAKING**: Built-in plugins no longer supported
  - **BREAKING**: Filesystem scanning removed
  - **BREAKING**: .dev marker system removed
  - Automatic official plugin detection (`structum_*` packages)
  - Entry point group: `structum.plugins`
  - Visual tags: [OFFICIAL] for structum_* packages, [EXTERNAL] for third-party
- **Plugin Template** (2025-12-06/2025-12-08): Professional skeleton for external plugins
  - Default command: `info` (displays plugin metadata)
  - `PLUGIN_INFO` constant with name, version, description, category
  - Commented examples for adding custom commands
  - Professional output formatting with plugin metadata
  - Directory output handling (auto-generates filename for directories)
- **Plugin CLI**: Full management commands
  - `structum plugins list` - List plugins with type distinction ([OFFICIAL]/[EXTERNAL])
  - **REMOVED**: `--show-dev` flag (no longer needed)
  - `structum plugins info <name>` - Show plugin details
  - `structum plugins enable/disable <name>` - Manage plugin state
  - `structum plugins new <name>` - Generate external plugin skeleton
- **Plugin Categories**: `analysis`, `export`, `formatting`, `utility`
- **Plugin Validation**: Auto-validates `name`, `version`, `category` on load
- **Configuration Persistence**: State stored in `~/.config/structum/config.json`

**Migration Note**: See `Migration_Path.md` and `Migration_Path - TODO.md` for complete refactoring details.

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

#### Plugin System Refactoring (Phase 2 - 2025-12-08)

- **Simplified Plugin Loader** (`loader.py`):
  - Removed `load_builtin_plugins()` function (~100 lines)
  - Removed `get_dev_plugins()` and `_dev_plugins` global registry
  - Removed `DevPluginInfo` TypedDict
  - Removed filesystem scanning for built-in plugins
  - Removed .dev marker tracking system
  - Reduced from 186 to 80 lines (**-57%**)
  - Added automatic official plugin detection (structum_*)
  - Added conflict warnings for duplicate plugins

- **Enhanced Plugin Registry** (`registry.py`):
  - Added `PluginType` enum (OFFICIAL, EXTERNAL)
  - Added `PluginMetadata` dataclass for type tracking
  - Updated `_plugins` dict to store metadata instead of bare classes
  - Added `is_official` parameter to `register()` method
  - Added conflict detection with console warnings
  - Added `get_metadata()` method
  - Added `list_plugins_detailed()` with type information
  - Added `list_by_type()` method
  - Updated all methods to work with metadata structure
  - Expanded from 105 to 187 lines (+78% for metadata tracking)

- **Removed Built-in Plugin Infrastructure**:
  - Deleted `src/structum/plugins/sample/` directory (6 files)
  - Removed all .dev marker references
  - Removed `--show-dev` flag from CLI
  - Removed dev mode instructions
  - Updated docstrings to reflect external-only architecture

- **Simplified Plugin Skeleton Generator** (`skeleton.py`):
  - Removed .dev marker creation logic
  - Removed `is_builtin` detection
  - Simplified to external-only plugin generation
  - Updated CLI instructions for external plugins

**Net Impact**: -138 lines (11 files changed, -305 deleted, +167 added)
**Documentation**: See `Migration_Path.md` and `Migration_Path - TODO.md`
**Commits**: `cc32d1a` (Phase 2 - Core Refactoring)

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
  - Fixed `IsADirectoryError` when `--output` points to a directory
  - Template now automatically generates `results.txt` filename when output is a directory
  - **BREAKING**: Changed default template from `run` command to `info` command only
  - New template provides metadata display command, developers implement custom commands
  - Plugin metadata (name, version, description, category) available via `PLUGIN_INFO` constant
  - Simplified core logic template with commented examples instead of placeholder implementation
  - Professional output format with plugin name, version, and structured information

---
