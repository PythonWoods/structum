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

#### Plugin System Verification (Phase 3 - 2025-12-08)

- **CLI Commands Verification**:
  - Tested `structum plugins list` command (✓ working correctly)
  - Tested `structum plugins new` command (✓ generates external-only plugins)
  - Verified `plugins enable/disable` commands (✓ fully compatible)
  - Verified no .dev marker created in generated plugins (✓ correct)
  - Confirmed [OFFICIAL]/[EXTERNAL] tags implementation

- **Configuration System Verification**:
  - Reviewed `src/structum/core/config.py` (✓ optimal, no changes needed)
  - Verified enable/disable compatibility with new registry (✓ working)
  - Confirmed no breaking changes for existing configs (✓ backward compatible)
  - Verified all `PluginRegistry.list_plugins()` usages (✓ compatible with list[str])

- **Testing Results**:
  - All CLI commands working correctly
  - Config system fully compatible
  - Zero code changes required (Phase 2 was sufficient)
  - All acceptance criteria met

**Net Impact**: Zero code changes (excellent Phase 2 quality)
**Documentation**: Updated `Migration_Path - TODO.md`
**Commits**: `07c739d` (Phase 3 - CLI & Config Verification)

#### Documentation & Testing (Phase 4 - 2025-12-08)

- **Plugin Development Guide** (`docs/development/plugins.md`):
  - Removed "Creating a Builtin Plugin" section (lines 25-88, ~63 lines)
  - Expanded "Creating an External Plugin" section with clear workflow
  - Removed all .dev marker references
  - Added "Official vs External Plugins" explanation
  - Updated "How Plugin Discovery Works" (removed filesystem scanning)
  - Updated best practices for modern plugin development
  - Reduced from 425 to 370 lines (**-13%**)

- **Migration Guide** (`docs/MIGRATION_0.1_to_0.2.md`):
  - Created comprehensive migration documentation
  - Documented all breaking changes with severity assessment
  - Emphasized zero user impact (no external plugins exist yet)
  - Added clear migration steps for future plugin developers
  - Included FAQ section addressing common questions
  - Provided examples for official vs external plugin distinction

- **Unit Test Updates**:
  - **test_loader.py**:
    - Removed `test_load_builtin_plugins()` (built-in support removed)
    - Added `test_official_plugin_detection()` (structum_* auto-detection)
    - Added `test_external_plugin_detection()` (external plugin tagging)
    - Updated `test_conflict_warning()` (registry console patching)
  - **test_registry.py**:
    - Fixed `test_register_valid_plugin()` (list[str] compatibility)
    - Added `test_plugin_type_enum()` (PluginType.OFFICIAL/EXTERNAL)
    - Added `test_plugin_metadata_dataclass()` (metadata structure)
    - Added `test_register_as_official/external()` (type registration)
    - Added `test_list_by_type()` (plugin grouping)
    - Added `test_list_plugins_detailed()` (full metadata)
    - Added `test_get_metadata_nonexistent()` (edge case)
    - Added `test_conflict_detection()` (override warning)
  - **test_skeleton.py**:
    - Added `test_no_dev_marker_created()` (.dev removal verification)
    - Added `test_external_only_generation()` (external-only validation)
  - **test_plugins_cmd.py**:
    - Fixed `test_list_plugins()` (list_plugins_detailed API)
    - Fixed `test_enable_plugin()` (list[str] return value)

- **Migration Tracking** (`Migration_Path - TODO.md`):
  - Updated to reflect Phase 4 completion
  - Marked all tasks (4.1, 4.2, 4.3) as completed
  - Updated status to "Phase 4 COMPLETED - READY FOR RELEASE"

**Net Impact**: Documentation improvements (-55 lines in plugins.md, +262 lines migration guide) + comprehensive test coverage
**Testing Status**: All unit tests passing, full coverage for metadata system
**Commits**: Multiple Phase 4 commits (documentation, tests, fixes)

#### Version Management (2025-12-08)

- **Version Bump**: Updated from 0.0.1 to **0.2.0**
  - Reflects major refactoring with breaking changes
  - Semantic versioning: pre-1.0, breaking changes = minor bump
  - All documentation aligned with v0.2 release
  - Updated `src/structum/__about__.py`
- **Release Preparation**:
  - Merged `dev-refactoring` branch into `develop`
  - Tagged release as `v0.2.0`
  - 20 files changed: 2109 insertions(+), 459 deletions(-)

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
