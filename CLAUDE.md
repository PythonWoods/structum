# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ IMPORTANT: V2.0 REFACTORING IN PROGRESS

**Current Status**: 🔄 **Major architectural refactoring to v2.0 - Enterprise Plugin Framework**

Structum is being transformed from a monolithic CLI tool into a **minimal enterprise-grade plugin framework**. All current functionality will be extracted into separate plugins.

**Key Architecture Document**: Read `ARCHITECTURE_V2.md` for complete design details.

### Refactoring Status Dashboard

#### Phase 1: Core Preparation ✅ COMPLETED
- ✅ Created `structum` core package (v2.0.0-alpha.1)
- ✅ Extracted plugin system to core
- ✅ Created minimal CLI bootstrap (`structum.cli.bootstrap`)
- ✅ Added monitoring infrastructure (`structum.monitoring.metrics`)
- ✅ Added security framework (`structum.security.validator`)
- ✅ Tested core package independently

#### Phase 2: Plugin Extraction ✅ COMPLETED (5/5 completed)

- ✅ **structum_tree** (v2.0.0-alpha.1) - Tree visualization plugin
- ✅ **structum_archive** (v2.0.0-alpha.1) - Code archiving plugin
- ✅ **structum_clean** (v2.0.0-alpha.1) - Cleanup utilities plugin
- ✅ **structum_docs** (v2.0.0-alpha.1) - Documentation management plugin
- ✅ **structum_plugins** (v2.0.0-alpha.1) - Plugin management plugin

#### Phase 3: Meta-Package ✅ COMPLETED

- ✅ Created `structum` meta-package (v2.0.0-alpha.1)
- ✅ Bundled all official plugins as dependencies
- ⏳ Update CI/CD pipelines (deferred to Phase 5)

#### Phase 3.5: Naming Refactor ✅ COMPLETED

- ✅ Renamed `structum-core/` → `structum/`
- ✅ Updated package name: `structum-core` → `structum`
- ✅ Added optional dependencies (`[full]`, `[tree]`, etc.)
- ✅ Deleted meta-package (replaced with extras)
- ✅ Updated all 5 plugin dependencies
- ✅ Tested new installation patterns

**Result**: Clear, intuitive naming that follows industry standards (pytest, flask, django)

#### Phase 3.6: Development Tooling ✅ COMPLETED

- ✅ Created `dev-setup.sh` for automated development environment setup
- ✅ Virtual environment detection and validation
- ✅ One-command installation of core + all plugins + dev tools
- ✅ Helpful next-steps instructions for developers

**Result**: Streamlined onboarding for new contributors

#### Phase 3.7: Test Configuration ✅ COMPLETED

- ✅ Created `run-tests.sh` monorepo test runner
- ✅ Color-coded test output with summary
- ✅ Created `TESTING.md` comprehensive testing guide
- ✅ Defined testing strategy: package-specific test suites
- ✅ Set coverage targets (core: 85%+, plugins: 70%+)

**Result**: Clear testing strategy and tooling for monorepo

#### Phase 3.8: Build and Development Scripts ✅ COMPLETED

- ✅ Organized scripts into `scripts/` directory
- ✅ Created build automation (`build-all.sh`, `clean-builds.sh`)
- ✅ Implemented hatch task runner (industry-standard)
- ✅ Created `scripts/README.md` comprehensive documentation
- ✅ Created root `pyproject.toml` with hatch scripts
- ✅ Updated `TESTING.md` script references

**Result**: Professional development workflow with industry-standard tooling (hatch, not Make/tox/just)

#### Phase 3.9: CI/CD Configuration ✅ COMPLETED

- ✅ Created modular GitHub Actions workflows (tests, lint, build, publish)
- ✅ Multi-version Python testing (3.11, 3.12, 3.13)
- ✅ Pre-commit hooks configuration (.pre-commit-config.yaml)
- ✅ Release-please automation for changelog and releases
- ✅ PyPI trusted publishing setup (no API tokens needed)
- ✅ Removed obsolete main_ci.yml workflow

**Result**: Complete CI/CD pipeline with automated testing, releases, and PyPI publishing

#### Phase 4: Enterprise Features ⏳ PENDING
- ⏳ Health checks
- ⏳ Advanced monitoring
- ⏳ Hot reload support

### How to Continue Refactoring

#### Quick Start (Resume Work)
```bash
# 1. Navigate to project
cd ~/develop/structum

# 2. Check current branch
git status  # Should show: "On branch develop"

# 3. View current structure
ls -la
# You should see:
#   - structum/             (Core package - Phase 1 complete)
#   - structum_tree/        (Plugin 1 complete)
#   - structum_archive/     (Plugin 2 complete)
#   - structum_clean/       (Plugin 3 complete)
#   - structum_docs/        (Plugin 4 complete)
#   - structum_plugins/     (Plugin 5 complete)
#   - scripts/              (Development scripts - Phase 3.8)
#   - .github/workflows/    (CI/CD - Phase 3.9)
#   - src/                  (Legacy v1.x monolith - deprecated)

# 4. Test current state
structum --help
# Should show:
#   - [OFFICIAL] tree
#   - [OFFICIAL] archive
#   - [COMMUNITY] demo, demo2
```

#### Next Steps: Begin Phase 4 - Enterprise Features

**Phase 3.9 is now COMPLETE!** CI/CD pipeline fully configured.

**Current State:**

- ✅ Clean, intuitive naming (`structum` for core)
- ✅ Optional dependencies pattern (`[full]`, `[tree]`, etc.)
- ✅ All 5 plugins working with new structure
- ✅ Industry-standard architecture (matches pytest, flask)
- ✅ Professional development scripts in `scripts/` directory
- ✅ Hatch task runner for all workflows (setup, test, build, lint, ci)
- ✅ Complete CI/CD pipeline with GitHub Actions
- ✅ Pre-commit hooks for code quality
- ✅ Automated releases with release-please
- ✅ PyPI trusted publishing configured

**Next Phase**: Implement enterprise features (Phase 4)

**Enterprise Features to Implement:**

1. **Health Checks**
   - Plugin health monitoring
   - System resource checks
   - Dependency validation

2. **Advanced Monitoring**
   - Performance metrics collection
   - Telemetry integration
   - Structured logging enhancements

3. **Hot Reload Support**
   - Dynamic plugin reload
   - Configuration hot-reload
   - Development mode improvements

**Installation Patterns (Current):**

```bash
# Local development - using hatch (RECOMMENDED)
hatch run setup                    # Automated setup (all packages + dev tools)

# Local development - manual installation
pip install -e ./structum          # Core only
pip install -e ./structum[full]    # Core + all plugins as optional dependencies

# Individual plugins (if needed)
pip install -e ./structum_tree
pip install -e ./structum_archive
# ... etc

# When published to PyPI (future):
pip install structum               # Core framework only
pip install structum[full]         # Core + all official plugins
pip install structum[tree,docs]    # Core + selective plugins
```

#### Package Structure Reference

**Current Monorepo Layout**:

```
structum/                       # ✅ Monorepo root
├── structum/                   # ✅ Core package (Phase 1)
│   ├── src/structum/
│   │   ├── cli/bootstrap.py    # Minimal CLI entry point
│   │   ├── plugins/            # Plugin system (loader, registry, SDK)
│   │   ├── config/             # Configuration management
│   │   ├── monitoring/         # Performance metrics
│   │   └── security/           # Security validation
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── structum_tree/              # ✅ Plugin 1 complete
│   ├── src/structum_tree/
│   │   ├── plugin.py           # TreePlugin class
│   │   ├── core.py             # tree visualization logic
│   │   ├── icons.py            # icon themes
│   │   └── utils.py            # helper functions
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── structum_archive/           # ✅ Plugin 2 complete
│   ├── src/structum_archive/
│   │   ├── plugin.py           # ArchivePlugin class
│   │   └── core.py             # archiving logic
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── structum_clean/             # ✅ Plugin 3 complete
│   ├── src/structum_clean/
│   │   ├── plugin.py           # CleanPlugin class
│   │   └── core.py             # cleanup logic
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── structum_plugins/           # ✅ Plugin 4 complete
│   ├── src/structum_plugins/
│   │   └── plugin.py           # PluginsPlugin class
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── structum_docs/              # ✅ Plugin 5 complete
│   ├── src/structum_docs/
│   │   ├── plugin.py           # DocsPlugin class
│   │   └── core.py             # docs management logic
│   └── pyproject.toml          # v2.0.0-alpha.1
│
├── scripts/                    # ✅ Development scripts (Phase 3.8)
│   ├── README.md               # Script documentation
│   ├── dev-setup.sh            # Environment setup
│   ├── run-tests.sh            # Test runner
│   ├── build-all.sh            # Build all packages
│   └── clean-builds.sh         # Clean artifacts
│
├── .github/workflows/          # ✅ CI/CD (Phase 3.9)
│   ├── tests.yml               # Multi-version testing
│   ├── lint.yml                # Code quality checks
│   ├── build.yml               # Package building
│   ├── publish.yml             # PyPI publishing
│   └── release-please.yml      # Release automation
│
├── pyproject.toml              # Monorepo task automation (hatch)
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── ARCHITECTURE_V2.md          # Complete v2.0 architecture design
├── TESTING.md                  # Testing guide
├── CHANGELOG.md                # Version history
├── CLAUDE.md                   # This file (dev guide)
└── src/                        # ⚠️ Legacy v1.x monolith (deprecated)
```

### Created Packages Summary

#### 1. structum (v2.0.0-alpha.1)

**Purpose**: Minimal enterprise-grade plugin framework (core package)
**Location**: `structum/`
**Entry Point**: `structum = "structum.cli.bootstrap:main"`
**Dependencies**: `typer>=0.12`, `rich>=13.0`, `pydantic>=2.0`, `pydantic-settings>=2.0`

**Key Components**:
- `structum.cli.bootstrap.create_app()` - Creates CLI app with plugin loading
- `structum.plugins.loader` - Plugin discovery via entry points
- `structum.plugins.registry` - Plugin registry with metadata
- `structum.plugins.sdk.PluginBase` - Base class for all plugins
- `structum.config.manager` - Configuration management
- `structum.monitoring.metrics` - Performance metrics collection
- `structum.security.validator` - Plugin validation

**Built-in Commands**:
- `structum version` - Show version
- `structum info` - Show app info and metrics

---

#### 2. structum_tree (v2.0.0-alpha.1)
**Purpose**: Directory tree visualization plugin
**Location**: `structum_tree/`
**Entry Point**: `tree = "structum_tree.plugin:TreePlugin"`
**Dependencies**: `structum>=2.0.0a1`, `rich>=13.0`

**Features**:
- Multiple themes: emoji, nerd, ascii, none
- File extension filtering (`--ext py,md`)
- Directory exclusion (`--ignore .git,node_modules`)
- Depth control (`--depth 3`)
- Statistics (`--stats`)
- Hidden files support (`--hidden`)

**Usage**:
```bash
structum tree . --theme emoji --depth 2 --ext py
```

---

#### 3. structum_archive (v2.0.0-alpha.1)
**Purpose**: Code archiving to Markdown plugin
**Location**: `structum_archive/`
**Entry Point**: `archive = "structum_archive.plugin:ArchivePlugin"`
**Dependencies**: `structum>=2.0.0a1`, `structum_tree>=2.0.0a1`, `rich>=13.0`

**Features**:
- Archive code to Markdown with syntax highlighting
- Auto-generated Table of Contents
- Includes directory tree visualization
- Split by folder (`--split-folder`)
- Split by file type (`--split-type`)
- File extension filtering

**Usage**:
```bash
structum archive src --ext py,md --output code.md
structum archive . --split-folder --output docs/
```

**Note**: Depends on `structum_tree` for tree visualization functionality (reuses `get_tree_ascii()` and utilities).

---

#### 4. structum_clean (v2.0.0-alpha.1)

**Purpose**: Cleanup utilities plugin
**Location**: `structum_clean/`
**Entry Point**: `clean = "structum_clean.plugin:CleanPlugin"`
**Dependencies**: `structum>=2.0.0a1`, `rich>=13.0`

**Features**:

- Recursively removes `__pycache__` directories
- Optional virtual environment protection (--skip-venv)
- Verbose/quiet output modes
- Rich-formatted console output
- Error handling and statistics

**Usage**:

```bash
structum clean .
structum clean src --quiet
structum clean . --skip-venv
```

---

#### 5. structum_plugins (v2.0.0-alpha.1)

**Purpose**: Plugin management plugin
**Location**: `structum_plugins/`
**Entry Point**: `plugins = "structum_plugins.plugin:PluginsPlugin"`
**Dependencies**: `structum>=2.0.0a1`, `rich>=13.0`

**Features**:

- List all installed plugins with metadata
- Show detailed plugin information
- Enable/disable plugins without uninstalling
- Generate new plugin skeletons with interactive prompts
- Distinguish between official and community plugins

**Usage**:

```bash
structum plugins list
structum plugins info tree
structum plugins enable my-plugin
structum plugins disable my-plugin
structum plugins new awesome-tool --output ~/projects/ --category utility
```

---

#### 6. structum_docs (v2.0.0-alpha.1)

**Purpose**: Documentation management plugin
**Location**: `structum_docs/`
**Entry Point**: `docs = "structum_docs.plugin:DocsPlugin"`
**Dependencies**: `structum>=2.0.0a1`, `rich>=13.0`

**Features**:

- Serve documentation locally with live reload
- Deploy documentation to GitHub Pages
- Custom server address and port configuration
- Custom deployment commit messages
- Force deployment option
- Integrates with MkDocs

**Usage**:

```bash
structum docs serve
structum docs serve --dev-addr 0.0.0.0:8080
structum docs deploy
structum docs deploy --message "Update docs for v2.0.0"
structum docs deploy --force
```

**Note**: Requires MkDocs to be installed (`pip install mkdocs mkdocs-material`).

---

### Optional Dependencies Pattern

**Phase 3.5 Update**: The meta-package approach was replaced with Python's optional dependencies (extras) pattern.

**Installation Options:**

```bash
# Core framework only
pip install structum

# All official plugins (recommended for most users)
pip install structum[full]

# Selective plugins
pip install structum[tree]           # Core + tree plugin
pip install structum[tree,docs]      # Core + tree + docs plugins

# All available extras:
# - [full]     → All official plugins
# - [tree]     → Tree visualization
# - [archive]  → Code archiving
# - [clean]    → Cleanup utilities
# - [docs]     → Documentation management
# - [plugins]  → Plugin management
```

**Benefits of Optional Dependencies:**

- ✅ Industry standard (pytest, flask, django use this pattern)
- ✅ Cleaner than separate meta-package
- ✅ Single package to maintain
- ✅ Flexible installation options
- ✅ Better dependency resolution

---

### Plugin Dependency Graph

```
structum (core framework)
    ↓
    ├─→ structum_tree (no plugin dependencies)
    │       ↓
    │       └─→ structum_archive (depends on structum_tree for tree rendering)
    │
    ├─→ structum_clean (no plugin dependencies)
    ├─→ structum_docs (no plugin dependencies)
    └─→ structum_plugins (no plugin dependencies)
```

**Note**: All plugins depend on `structum>=2.0.0a1`. Only `structum_archive` has an additional plugin dependency (`structum_tree`) for shared tree rendering functionality.

---

## Project Overview

**Structum v2.0** is a minimal enterprise-grade plugin framework (similar to pytest, flask).

**Current Architecture:**

- ✅ **Core Package** (`structum`): Provides only plugin infrastructure
- ✅ **Official Plugins**: All functionality delivered via plugins (tree, archive, clean, docs, plugins)
- ✅ **Plugin Discovery**: Entry point-based auto-discovery
- ✅ **Optional Dependencies**: Install core alone or with plugins via `[full]`/`[tree]`/etc extras

**Core Technologies:**

- Python 3.11+ with strict type checking (MyPy)
- Typer (CLI framework) + Rich (terminal output)
- Entry point-based plugin system
- Hatchling for builds
- Hatch for task automation
- GitHub Actions for CI/CD

## Development Commands

### Quick Start (Recommended - Using Hatch)

```bash
# One-command setup (creates venv, installs core + all plugins + dev tools)
hatch run setup

# Run all tests
hatch run test

# Build all packages
hatch run build

# Lint and format code
hatch run lint
hatch run format

# Complete CI workflow (clean, test, lint, build)
hatch run ci
```

### Manual Setup (Alternative)

```bash
# Create virtual environment and install
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Run setup script
./scripts/dev-setup.sh
```

### Testing

```bash
# Run all tests (recommended - using hatch)
hatch run test

# Run tests with verbose output
hatch run test-verbose

# Manual testing (alternative)
./scripts/run-tests.sh

# Run specific package tests
cd structum && pytest

# Run specific test file
pytest tests/unit/core/test_tree.py

# Run specific test function
pytest tests/unit/core/test_tree.py::test_function_name

# Run tests with verbose output
pytest -v

# Run tests without coverage report
pytest --no-cov
```

### Code Quality
```bash
# Lint and format with Ruff
ruff check src/structum
ruff format src/structum

# Type checking with MyPy (strict mode)
mypy src/structum

# Run all quality checks
ruff check src/structum && ruff format src/structum && mypy src/structum
```

### Documentation
```bash
# Serve docs locally (uses structum's own docs command)
structum docs serve

# Build docs
mkdocs build

# Deploy docs
structum docs deploy
```

### Running the CLI
```bash
# Run structum commands during development
python -m structum tree .
python -m structum archive . --output code.md
python -m structum plugins list
```

## Architecture

### High-Level Structure

```
src/structum/
├── cli/              # CLI layer (Typer commands)
│   ├── main.py       # App entry point, command registration
│   └── commands/     # Individual command implementations
├── core/             # Business logic (tree, archive, clean)
├── plugins/          # Plugin system (loader, registry, SDK)
└── utils/            # Shared utilities
```

### Key Architectural Principles

1. **Separation of Concerns**: CLI commands in `cli/commands/` delegate to business logic in `core/`
2. **Plugin-First**: All plugins are external packages discovered via entry points (`structum.plugins` group)
3. **Type Safety**: Full type hints with strict mypy checking
4. **Entry Point Registration**: Plugins register via `pyproject.toml` entry points, no manual registration needed

### Plugin Architecture

**All plugins are external packages** - there are no "built-in" plugins in the source tree. The plugin system works via Python entry points:

1. **Plugin Discovery**: Uses `importlib.metadata.entry_points(group="structum.plugins")`
2. **Plugin Types**:
   - Official plugins: Package name starts with `structum_*` → auto-tagged as `[OFFICIAL]`
   - Community plugins: Any other name → tagged as `[COMMUNITY]`
3. **Plugin Lifecycle**:
   - Discovered via entry points
   - Registered in `PluginRegistry` with distribution name
   - Metadata read from package's `pyproject.toml` (via `importlib.metadata`)
   - Validated (name, version, category)
   - CLI commands registered or placeholder added (if disabled)

**Creating a plugin (interactive):**
```bash
# Generate standalone plugin package with interactive prompts
structum plugins new my-plugin --output ~/projects/ --category utility
# You'll be prompted for: author name, email, description, version, license

# Install locally
cd ~/projects/my-plugin
pip install -e .

# Plugin is auto-discovered on next structum invocation
```

**Plugin Categories**: `analysis`, `export`, `formatting`, `utility`

**Enable/Disable plugins** (without uninstalling):
```bash
structum plugins disable my-plugin  # Keeps installed but inactive
structum plugins enable my-plugin
```

**Plugin Metadata**: Metadata (version, author, description, etc.) is read from the installed package's `pyproject.toml` via `importlib.metadata`, not from hardcoded class attributes. This ensures single source of truth.

### CLI Command Registration

Commands are registered in `src/structum/cli/main.py`:
- Single commands: `app.command(name="tree")(tree.tree_command)`
- Command groups: `app.add_typer(docs.app, name="docs")`
- Plugins: Auto-registered via `load_plugins(app)` which calls `plugin.register_commands(app)`

### Data Flow Pattern

For CLI commands:
1. User invokes command (e.g., `structum tree .`)
2. Typer routes to command function in `cli/commands/`
3. Command function parses args, validates input
4. Delegates to business logic in `core/` (e.g., `core.tree.generate_tree()`)
5. Business logic returns structured data
6. Command function formats output with Rich and displays to user

## Testing Strategy

Test structure follows the source layout:
```
tests/
├── unit/
│   ├── cli/commands/     # CLI command tests
│   ├── core/             # Business logic tests
│   └── plugins/          # Plugin system tests
└── conftest.py           # Shared fixtures
```

**Coverage targets:**
- Overall: 85%+
- Core modules: 90%+
- Plugins: 70%+

**Run a single test:**
```bash
pytest tests/unit/core/test_tree.py::test_generate_tree_basic
```

## Code Conventions

### File Headers
All source files include SPDX headers:
```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods
```

### Imports
Ruff enforces import order (isort):
1. Future imports
2. Standard library
3. Third-party packages
4. First-party (structum)
5. Local imports

### Type Hints
Strict typing is enforced:
- Use type hints for all function signatures
- Use `| None` instead of `Optional[...]` (Python 3.11+ union syntax)
- Use `dict[str, Any]` instead of `Dict[str, Any]`
- MyPy runs in strict mode

### Error Handling
- Use Typer's `typer.Exit()` for CLI errors
- Use Rich console for formatted error messages
- Provide actionable error messages to users

## Plugin Development Notes

When developing plugins:
1. **Always use entry points** - defined in `pyproject.toml` under `[project.entry-points."structum.plugins"]`
2. **Plugin class must inherit from `PluginBase`** (from `structum.plugins.sdk`)
3. **Required attributes**: `name`, `version`, `category`
4. **Required method**: `setup()` (initialization)
5. **Optional methods**: `register_commands()`, `process_file()`, `generate_output()`, `teardown()`
6. **Use `typer.Typer(no_args_is_help=True)`** for plugin command groups
7. **Metadata from pyproject.toml**: Use `get_current_plugin_metadata()` to read your plugin's metadata dynamically

**Official plugin naming**: `structum_<name>` (e.g., `structum_latex`)
**Community plugin naming**: Recommend `structum-plugin-<name>` on PyPI

**Reading plugin metadata in commands:**
```python
from structum.plugins.utils import get_current_plugin_metadata

@app.command("info")
def info_command() -> None:
    meta = get_current_plugin_metadata()  # Reads from pyproject.toml
    print(f"Version: {meta['version']}")
    print(f"Author: {meta['author']}")
```

## Common Patterns

### Adding a new core command
1. Implement business logic in `src/structum/core/new_feature.py`
2. Create CLI interface in `src/structum/cli/commands/new_feature.py`
3. Register in `src/structum/cli/main.py`
4. Add tests in `tests/unit/core/test_new_feature.py` and `tests/unit/cli/commands/test_new_feature_cmd.py`

### Working with config
```python
from structum.core.config import get_plugin_enabled, set_plugin_enabled

enabled = get_plugin_enabled("my-plugin")  # Returns bool
set_plugin_enabled("my-plugin", False)     # Disable plugin
```

Config is stored in `~/.config/structum/config.json`.

## Critical Files Reference

**Architecture & Design:**

- **[ARCHITECTURE_V2.md](ARCHITECTURE_V2.md)**: Complete v2.0 architecture documentation with all design decisions
- **[TESTING.md](TESTING.md)**: Comprehensive testing guide and strategy
- **[CHANGELOG.md](CHANGELOG.md)**: Version history and release notes

**Core Package Files:**

- `structum/src/structum/cli/bootstrap.py` - Minimal CLI entry point
- `structum/src/structum/plugins/loader.py` - Plugin discovery and loading
- `structum/src/structum/plugins/registry.py` - Plugin registry management
- `structum/src/structum/plugins/sdk.py` - Plugin SDK base classes

**Development Tools:**

- `scripts/dev-setup.sh` - Automated development environment setup
- `scripts/run-tests.sh` - Monorepo test runner
- `scripts/build-all.sh` - Build all packages
- `pyproject.toml` (root) - Hatch task automation configuration

**CI/CD:**

- `.github/workflows/tests.yml` - Multi-version testing
- `.github/workflows/lint.yml` - Code quality checks
- `.github/workflows/build.yml` - Package building
- `.github/workflows/publish.yml` - PyPI publishing
- `.pre-commit-config.yaml` - Pre-commit hooks

### Refactoring Progress Checklist

Track the v2.0 refactoring progress:

**Phase 1: Core Preparation** ✅ COMPLETED

- [x] Create `structum/` core package structure
- [x] Move plugin system to core
- [x] Add monitoring infrastructure
- [x] Add security framework
- [x] Create bootstrap CLI

**Phase 2: Plugin Extraction** ✅ COMPLETED (5/5)

- [x] Extract tree → `structum_tree`
- [x] Extract archive → `structum_archive`
- [x] Extract clean → `structum_clean`
- [x] Extract docs → `structum_docs`
- [x] Extract plugins → `structum_plugins`

**Phase 3: Distribution & Tooling** ✅ COMPLETED

- [x] Phase 3.0: Meta-package (later replaced by extras)
- [x] Phase 3.5: Naming refactor (`structum-core` → `structum`)
- [x] Phase 3.6: Development tooling (`scripts/dev-setup.sh`)
- [x] Phase 3.7: Test configuration (`scripts/run-tests.sh`, `TESTING.md`)
- [x] Phase 3.8: Build scripts (`scripts/build-all.sh`, hatch tasks)
- [x] Phase 3.9: CI/CD configuration (GitHub Actions, pre-commit)

**Phase 4: Enterprise Features** ⏳ IN PROGRESS

- [ ] Health checks (plugin health monitoring)
- [ ] Advanced monitoring (metrics, telemetry)
- [ ] Security enhancements (sandboxing)
- [ ] Hot reload support (dynamic plugin reload)
- [ ] Multi-environment configuration

**Phase 5: Documentation & Release** ⏳ PENDING

- [ ] Update all documentation for v2.0
- [ ] Create migration guide (v1.x → v2.0)
- [ ] Clean up obsolete files (`src/structum/` monolith)
- [ ] Prepare PyPI packages for publishing
- [ ] Release v2.0.0-beta.1
- [ ] Release v2.0.0 (stable)

---

## Important Notes

- **V2.0 Architecture**: Minimal plugin framework - see [ARCHITECTURE_V2.md](ARCHITECTURE_V2.md) for complete design
- **No built-in commands**: All functionality delivered via plugins (tree, archive, clean, docs, plugins)
- **Plugin auto-discovery**: Plugins registered via entry points, auto-discovered on load
- **Disabled plugins**: Show helpful error messages instead of "No such command"
- **Plugin conflicts**: Detected and warnings shown during load
- **Plugin metadata**: Read from `pyproject.toml` via `importlib.metadata` (single source of truth)
- **Interactive plugin creation**: `structum plugins new` prompts for all metadata interactively
- **Plugin types**: `[OFFICIAL]` for `structum_*` packages, `[COMMUNITY]` for all others
- **Version location**: Each package has `__about__.py` (e.g., `structum/src/structum/__about__.py`)
- **Branch strategy**: Develop on `develop`, merge to `main` for releases
- **Task automation**: Use `hatch run <task>` for all development workflows (not Make/tox/just)
- **CI/CD**: GitHub Actions with modular workflows (tests, lint, build, publish, release-please)
