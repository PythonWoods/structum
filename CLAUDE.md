# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## ⚠️ IMPORTANT: V2.0 REFACTORING IN PROGRESS

**Current Status**: 🔄 **Major architectural refactoring to v2.0 - Enterprise Plugin Framework**

Structum is being transformed from a monolithic CLI tool into a **minimal enterprise-grade plugin framework**. All current functionality will be extracted into separate plugins.

**Key Architecture Document**: Read `ARCHITECTURE_V2.md` for complete design details.

### Refactoring Status Dashboard

#### Phase 1: Core Preparation ✅ COMPLETED
- ✅ Created `structum-core` package (v2.0.0-alpha.1)
- ✅ Extracted plugin system to core
- ✅ Created minimal CLI bootstrap (`structum.cli.bootstrap`)
- ✅ Added monitoring infrastructure (`structum.monitoring.metrics`)
- ✅ Added security framework (`structum.security.validator`)
- ✅ Tested core package independently

#### Phase 2: Plugin Extraction 🔄 IN PROGRESS (2/5 completed)
- ✅ **structum_tree** (v2.0.0-alpha.1) - Tree visualization plugin
- ✅ **structum_archive** (v2.0.0-alpha.1) - Code archiving plugin
- ⏳ **structum_clean** - Cleanup utilities (pending)
- ⏳ **structum_docs** - Documentation management (pending)
- ⏳ **structum_plugins** - Plugin management (pending)

#### Phase 3: Meta-Package ⏳ PENDING
- ⏳ Create `structum` meta-package
- ⏳ Bundle all official plugins
- ⏳ Update CI/CD pipelines

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
#   - structum-core/        (Phase 1 complete)
#   - structum_tree/        (Plugin 1 complete)
#   - structum_archive/     (Plugin 2 complete)
#   - src/                  (Original monolith - being phased out)

# 4. Test current state
structum --help
# Should show:
#   - [OFFICIAL] tree
#   - [OFFICIAL] archive
#   - [COMMUNITY] demo, demo2
```

#### Next Steps: Complete Phase 2

**Remaining Plugins to Extract** (in this order):
1. `structum_clean` - Extract from `src/structum/cli/commands/clean.py` and `src/structum/core/clean.py`
2. `structum_docs` - Extract from `src/structum/cli/commands/docs.py` and `src/structum/core/docs.py`
3. `structum_plugins` - Extract from `src/structum/cli/commands/plugins.py` and `src/structum/plugins/skeleton.py`

**Pattern to Follow** (same as tree and archive):
```bash
# For each plugin (example: clean):
mkdir -p structum_clean/src/structum_clean
cd structum_clean

# Create pyproject.toml with:
# - name: structum_clean
# - version: dynamic from __about__.py
# - dependencies: structum-core>=2.0.0a1 (+ others as needed)
# - entry-points: clean = "structum_clean.plugin:CleanPlugin"

# Create plugin files:
# - src/structum_clean/__about__.py      (version info)
# - src/structum_clean/__init__.py       (exports)
# - src/structum_clean/plugin.py         (PluginBase subclass)
# - src/structum_clean/core.py           (business logic)
# - README.md                            (plugin documentation)

# Install and test:
pip install -e .
structum --help  # Should show [OFFICIAL] clean
structum clean --help
```

#### Package Structure Reference

**Current Monorepo Layout**:
```
structum/
├── structum-core/              # ✅ Phase 1 complete
│   ├── src/structum/
│   │   ├── cli/bootstrap.py    # Minimal entry point
│   │   ├── plugins/            # Plugin system
│   │   ├── config/             # Config management
│   │   ├── monitoring/         # Metrics
│   │   └── security/           # Validation
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
├── src/structum/               # ⚠️ Legacy monolith (being replaced)
│   ├── cli/commands/           # Extract from here
│   │   ├── clean.py           # → structum_clean
│   │   ├── docs.py            # → structum_docs
│   │   └── plugins.py         # → structum_plugins
│   └── core/
│       ├── clean.py           # → structum_clean/core.py
│       └── docs.py            # → structum_docs/core.py
│
├── ARCHITECTURE_V2.md          # Complete architecture design
└── CLAUDE.md                   # This file
```

### Created Packages Summary

#### 1. structum-core (v2.0.0-alpha.1)
**Purpose**: Minimal enterprise-grade plugin framework
**Location**: `structum-core/`
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
**Dependencies**: `structum-core>=2.0.0a1`, `rich>=13.0`

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
**Dependencies**: `structum-core>=2.0.0a1`, `structum_tree>=2.0.0a1`, `rich>=13.0`

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

### Plugin Dependency Graph

```
structum-core (foundation)
    ↓
    ├─→ structum_tree (no plugin dependencies)
    │       ↓
    │       └─→ structum_archive (depends on tree)
    │
    ├─→ structum_clean (pending)
    ├─→ structum_docs (pending)
    └─→ structum_plugins (pending)
```

---

## Project Overview (Current State - Will Change)

**Current**: Structum is a CLI tool with plugin support
**Future (v2.0)**: Structum will be a minimal plugin framework (like pytest)

**Core Technologies:**
- Python 3.11+ with strict type checking
- Typer (CLI framework) + Rich (terminal output)
- Entry point-based plugin system
- Hatchling for builds

**V2.0 Vision**: Core package (`structum-core`) provides only plugin infrastructure. All commands (tree, archive, clean, docs) become official plugins.

## Development Commands

### Setup
```bash
# Create virtual environment and install
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev,docs]"
```

### Testing
```bash
# Run all tests with coverage
pytest

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

## V2.0 Refactoring Guide

### Current Architecture (v1.x - Being Replaced)

```
src/structum/
├── cli/              # CLI commands (will be extracted)
│   ├── main.py       # Entry point
│   └── commands/     # tree, archive, clean, docs, plugins
├── core/             # Business logic (will be extracted)
├── plugins/          # Plugin system (will stay, enhanced)
└── utils/            # Utilities (will be reorganized)
```

### Target Architecture (v2.0)

```
structum-core/                    # Minimal core (new package)
├── src/structum/
│   ├── cli/
│   │   └── bootstrap.py          # Minimal entry point
│   ├── plugins/                  # Enhanced plugin system
│   │   ├── loader.py
│   │   ├── registry.py
│   │   ├── sdk.py
│   │   ├── utils.py
│   │   └── health.py             # NEW: Health checks
│   ├── config/                   # NEW: Config management
│   ├── monitoring/               # NEW: Metrics & telemetry
│   └── security/                 # NEW: Sandboxing & validation

structum_tree/                    # Official plugin
structum_archive/                 # Official plugin
structum_clean/                   # Official plugin
structum_docs/                    # Official plugin
structum_plugins/                 # Official plugin

structum/                         # Meta-package (bundles all)
```

### Refactoring Steps (In Order)

**Phase 1: Core Preparation**
1. Create `structum-core/` directory structure
2. Move plugin system to core
3. Add monitoring infrastructure
4. Add security framework
5. Create minimal bootstrap CLI

**Phase 2: Plugin Extraction**
1. Extract `tree` command → `structum_tree/`
2. Extract `archive` command → `structum_archive/`
3. Extract `clean` command → `structum_clean/`
4. Extract `docs` command → `structum_docs/`
5. Extract `plugins` commands → `structum_plugins/`

**Phase 3: Meta-Package**
1. Create `structum/` meta-package
2. Add all official plugins as dependencies
3. Update CI/CD for monorepo

**Phase 4: Enterprise Features**
1. Implement health checks
2. Add performance monitoring
3. Add security features (sandboxing)
4. Add hot reload
5. Add multi-environment config

**Phase 5: Testing & Release**
1. Comprehensive testing
2. Update all documentation
3. Migration guide for v1 users
4. Release v2.0.0

### Key Decisions Made

1. **Repository Structure**: Monorepo (easier coordination)
2. **Backward Compatibility**: Clean break for v2.0 (no v1 compat layer)
3. **Plugin Types**: `[OFFICIAL]` (structum_*) and `[COMMUNITY]` (all others)
4. **Installation**: `pip install structum` bundles all official plugins
5. **Core Package**: `pip install structum-core` for framework only

### Commands for Refactoring

```bash
# Check refactoring status
git status
git branch  # Should be on 'develop'

# Review architecture
cat ARCHITECTURE_V2.md

# Start Phase 1: Create core structure
mkdir -p structum-core/src/structum/{cli,plugins,config,monitoring,security}

# Extract tree plugin (example)
mkdir -p structum_tree/src/structum_tree/{commands,core}
# Copy relevant code from src/structum/core/tree.py
# Copy relevant code from src/structum/cli/commands/tree.py

# Test during development
pip install -e .
python -m structum --help
```

### Critical Files to Know

- **`ARCHITECTURE_V2.md`**: Complete v2.0 design document
- **`ARCHITECTURE.md`**: Old v1.x architecture (will be deprecated)
- **`src/structum/plugins/loader.py`**: Plugin loading logic
- **`src/structum/plugins/registry.py`**: Plugin registry
- **`src/structum/plugins/sdk.py`**: Plugin SDK base classes
- **`src/structum/cli/main.py`**: Current CLI entry (will be replaced)

### Testing Strategy During Refactoring

1. Keep v1.x working during transition
2. Test each extracted plugin independently
3. Integration tests for plugin interactions
4. Performance benchmarks (startup time, memory)
5. Security tests for sandboxing

### Migration Checklist

Use this to track progress:

- [ ] Phase 1: Core Preparation
  - [ ] Create directory structure
  - [ ] Move plugin system
  - [ ] Add monitoring infrastructure
  - [ ] Add security framework
  - [ ] Create bootstrap CLI
- [ ] Phase 2: Plugin Extraction
  - [ ] Extract tree → structum_tree
  - [ ] Extract archive → structum_archive
  - [ ] Extract clean → structum_clean
  - [ ] Extract docs → structum_docs
  - [ ] Extract plugins → structum_plugins
- [ ] Phase 3: Meta-Package
  - [ ] Create structum meta-package
  - [ ] Configure dependencies
  - [ ] Update CI/CD
- [ ] Phase 4: Enterprise Features
  - [ ] Health checks
  - [ ] Monitoring
  - [ ] Security
  - [ ] Hot reload
  - [ ] Multi-environment
- [ ] Phase 5: Release
  - [ ] Update docs
  - [ ] Migration guide
  - [ ] Release v2.0.0

---

## Important Notes

- **V2.0 IN PROGRESS**: Architecture is changing, see `ARCHITECTURE_V2.md`
- **No built-in plugins in v2.0** - everything becomes a plugin
- **Plugin commands auto-registered** during `load_plugins()` call
- **Disabled plugins show helpful error messages** instead of "No such command"
- **Plugin conflicts are detected** and warnings shown during load
- **Plugin metadata read from pyproject.toml** - single source of truth via `importlib.metadata`
- **Interactive plugin creation** - `structum plugins new` prompts for author, email, description, etc.
- **Plugin types**: `[OFFICIAL]` for `structum_*` packages, `[COMMUNITY]` for all others
- **Version is in `src/structum/__about__.py`** (managed by hatchling)
- **Branch strategy**: Develop on `develop`, merge to `main` for releases
