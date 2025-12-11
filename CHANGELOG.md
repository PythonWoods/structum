# Changelog

All notable changes to this project will be documented in this file.

This project follows **Conventional Commits**  
and automatic release generation via **release-please**.

---

## [Unreleased]

## [2.0.0-alpha.1] - 2025-12-11

### 🎉 Major Release - Enterprise Plugin Framework

Complete architectural redesign transforming Structum into an enterprise-grade plugin framework.

### ✨ Features

#### Phase 3.9: CI/CD Configuration (2025-12-11)

- **GitHub Actions Workflows**: Modular CI/CD with tests, lint, build, publish, release-please
- **Multi-Version Testing**: Python 3.11, 3.12, 3.13 support
- **Pre-commit Hooks**: Ruff, MyPy, REUSE, markdown linting, file checks
- **Release Automation**: release-please for automated changelog and releases
- **PyPI Publishing**: Trusted publishing (no API tokens needed)
- **Local CI Parity**: `hatch run test/lint/build` matches GitHub Actions exactly

#### Phase 3.8: Build and Development Scripts (2025-12-11)

- **Script Organization**: Moved all development scripts to `scripts/` directory
- **Build Automation**: Added `scripts/build-all.sh` and `scripts/clean-builds.sh`
- **Hatch Task Runner**: Industry-standard task automation via root `pyproject.toml`
- **Script Documentation**: Complete `scripts/README.md` guide
- **Task Commands**: `hatch run setup/test/build/lint/format/ci`
- **Updated References**: Updated `TESTING.md` with new script paths

#### Phase 3.7: Test Configuration (2025-12-11)

- **Monorepo Test Runner**: Added `run-tests.sh` to run all package tests
- **Color-Coded Output**: Pass/fail indicators with summary report
- **Testing Documentation**: Complete `TESTING.md` guide for contributors
- **Coverage Targets**: Core 85%+, plugins 70%+
- **Package-Specific Tests**: Independent test suites per package

#### Phase 3.6: Development Tooling (2025-12-11)

- **Development Setup Script**: Added `dev-setup.sh` for one-command environment setup
- **Virtual Environment Detection**: Warns if not in venv
- **Automated Installation**: Installs core + all plugins + dev dependencies in editable mode
- **Developer Instructions**: Clear next steps after setup

#### Phase 3.5: Naming Refactor (2025-12-11)

- **Package Rename**: `structum-core` → `structum` for clarity and industry standards
- **Optional Dependencies**: Added `[full]`, `[tree]`, `[archive]`, `[clean]`, `[docs]`, `[plugins]` extras
- **Meta-Package Elimination**: Replaced with cleaner optional dependencies pattern
- **Installation Patterns**:
  - `pip install structum` - Core framework only
  - `pip install structum[full]` - All official plugins
  - `pip install structum[tree,docs]` - Selective plugins

#### Phase 3: Meta-Package (2025-12-11)

- **Meta-Package**: Created bundle package with all official plugins
- **Synchronized Versioning**: All packages at v2.0.0-alpha.1

#### Phase 2: Plugin Extraction (2025-12-10)

- **structum_tree** (v2.0.0-alpha.1): Extracted tree visualization as standalone plugin
- **structum_archive** (v2.0.0-alpha.1): Extracted code archiving as standalone plugin
- **structum_clean** (v2.0.0-alpha.1): Extracted cleanup utilities as standalone plugin
- **structum_docs** (v2.0.0-alpha.1): Extracted documentation management as standalone plugin
- **structum_plugins** (v2.0.0-alpha.1): Extracted plugin management as standalone plugin

#### Phase 1: Core Preparation (2025-12-10)

- **Minimal Core**: Enterprise-grade plugin framework with minimal dependencies
- **Plugin System**: Entry point-based discovery, lazy loading, conflict detection
- **Monitoring**: Performance metrics collection infrastructure
- **Security**: Plugin validation and security framework
- **Configuration**: Centralized config management with validation

### 🔄 Changed

- **BREAKING**: Monolithic architecture → Plugin-based architecture
- **BREAKING**: Package name: `structum` now refers to core framework (was meta-package)
- **BREAKING**: All commands are now plugins (no built-in commands except `version` and `info`)
- **Plugin Dependencies**: All plugins now depend on `structum>=2.0.0a1` (was `structum-core`)

### 🗑️ Removed

- **Meta-Package**: `structum-meta` eliminated in favor of optional dependencies
- **Built-in Commands**: All functionality moved to plugins
- **Old Documentation**: ARCHITECTURE.md, ROADMAP.md, Migration_Path.md (replaced by ARCHITECTURE_V2.md)

### 📚 Documentation

- **ARCHITECTURE_V2.md**: Complete v2.0 architecture documentation
- **CLAUDE.md**: Updated with Phase 3.5 completion status
- **Architectural Decisions**: Documented all key decisions and rationale

---

## [0.2.0] - 2024-12-05

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
  - **Enhanced Error Handling** (2025-12-09): Helpful messages when attempting to use disabled plugins
    - Disabled plugins now show: "Plugin 'X' is disabled. Enable it with: structum plugins enable X"
    - Clear distinction between "not installed" vs "disabled" error messages
    - Enterprise-grade UX: self-service guidance for users
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

#### Plugin Skeleton Generator Enhancement (2025-12-09)

- **Complete Package Generation** (`skeleton.py`):
  - Now generates **ready-to-install** Python package (no manual setup needed)
  - Added `pyproject.toml` template with pre-configured entry point
  - Added `README.md` template with installation and usage instructions
  - Added `.gitignore` template with Python best practices
  - Implemented modern `src/` layout for package structure
  - **Standalone projects**: Each plugin is a complete Python package (no container directory)
  - Package naming: `structum-plugin-<name>` (PyPI-ready)

- **Generated Structure** (standalone Python project):
  ```
  output_dir/my-plugin/              # ← Standalone project, no container folder
  ├── pyproject.toml                 # Entry point, dependencies, build config
  ├── README.md                      # Documentation template
  ├── .gitignore                     # Git ignore rules
  └── src/
      └── my_plugin/
          ├── __init__.py
          ├── plugin.py
          ├── commands/
          │   ├── __init__.py
          │   └── main.py
          └── core/
              ├── __init__.py
              └── logic.py
  ```

- **Clear Pipeline**:
  - `cd ~/projects/ && structum plugins new my-plugin`
  - `cd my-plugin && pip install -e .`
  - `git init && git add . && git commit -m "Initial commit"`
  - `python -m build && twine upload dist/*`
  - Each plugin is a **complete, standalone Python package**

- **Improved CLI Output** (`plugins.py`):
  - Enhanced success message with generated files list
  - Clear step-by-step installation instructions
  - Package name display for PyPI publishing
  - Helpful tips for development workflow

- **Updated Documentation** (`docs/development/plugins.md`):
  - Simplified workflow (4 steps instead of 5)
  - Removed manual `pyproject.toml` configuration step
  - Added clear examples for implementing custom commands
  - Updated installation instructions for new structure

- **Test Coverage** (`test_skeleton.py`):
  - Updated all tests for new `src/` layout
  - Added verification for `pyproject.toml`, `README.md`, `.gitignore`
  - Added validation for entry point configuration
  - All tests passing with 100% coverage for skeleton.py

**Developer Experience**:
- **Before**: Generate skeleton → manually create pyproject.toml → manually configure entry point → install
- **After**: `structum plugins new my-plugin` → `cd my-plugin && pip install -e .` → done! ✨
- **Workflow**: Identical to any standard Python project (git, PyPI, etc.)
- **Philosophy**: Each plugin is a **standalone Python package**, not a sub-component

**Net Impact**: +220 lines in skeleton.py (templates), significantly improved DX
**Commits**: TBD (Plugin Skeleton Enhancement)

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
