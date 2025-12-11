# Structum v2.0 - Enterprise Plugin Framework Architecture

> **Vision**: Transform Structum into an enterprise-grade, highly scalable plugin framework that serves as the foundation for future plugin-based solutions.

## Executive Summary

Structum v2.0 is a complete architectural redesign that transforms the project from a monolithic CLI tool into a **minimalist plugin framework**. All functionality is delivered through plugins, creating a clean separation of concerns and maximum flexibility.

---

## Core Principles

1. **Plugin-First Everything**: Core only provides plugin infrastructure
2. **Zero Built-in Commands**: All commands are plugins (including `plugins` management itself)
3. **Enterprise-Grade**: Production-ready with monitoring, health checks, security
4. **Highly Scalable**: Support for hundreds of plugins without performance degradation
5. **Developer-Friendly**: Clear SDK, excellent DX, comprehensive documentation

---

## Architecture Overview

### Package Structure

```
structum-ecosystem/
├── structum-core/              # Minimal framework (plugin system only)
│   └── src/structum/
│       ├── __init__.py
│       ├── __about__.py
│       ├── cli/
│       │   └── bootstrap.py    # Minimal CLI entry point
│       ├── plugins/
│       │   ├── loader.py       # Plugin discovery & loading
│       │   ├── registry.py     # Plugin registry
│       │   ├── sdk.py          # Plugin SDK
│       │   ├── utils.py        # Plugin utilities
│       │   └── health.py       # Plugin health checks
│       ├── config/
│       │   ├── manager.py      # Configuration management
│       │   └── schema.py       # Config schema validation
│       ├── monitoring/
│       │   ├── metrics.py      # Performance metrics
│       │   ├── telemetry.py    # Telemetry collection
│       │   └── logging.py      # Structured logging
│       └── security/
│           ├── sandbox.py      # Plugin sandboxing
│           └── validator.py    # Security validation
│
├── structum_tree/              # Official plugin: tree command
├── structum_archive/           # Official plugin: archive command
├── structum_clean/             # Official plugin: clean command
├── structum_docs/              # Official plugin: docs command
├── structum_plugins/           # Official plugin: plugin management
│
└── structum/                   # Meta-package (bundles all official plugins)
    └── pyproject.toml          # Dependencies: structum-core + all official plugins
```

---

## Core Package: structum-core

### Minimal Scope

**What's IN the core:**
- Plugin system (loader, registry, SDK)
- CLI bootstrap (minimal entry point)
- Configuration management
- Monitoring & telemetry infrastructure
- Security & sandboxing
- Health checks
- Logging infrastructure

**What's NOT in the core:**
- No business logic commands
- No domain-specific functionality
- No heavy dependencies (beyond typer, rich, pydantic)

### Core Features

#### 1. Plugin System
```python
# Advanced plugin loader with:
- Entry point discovery
- Dependency resolution
- Version conflict detection
- Hot reload support
- Lazy loading
- Plugin isolation
```

#### 2. Plugin Registry
```python
# Enterprise registry features:
- Plugin metadata caching
- Fast lookup (O(1))
- Category indexing
- Dependency graph
- Health status tracking
- Performance metrics per plugin
```

#### 3. Configuration Management
```python
# Multi-environment support:
- YAML/JSON/TOML support
- Environment variable override
- Secret management integration
- Config validation (Pydantic)
- Hot reload on config change
```

#### 4. Monitoring & Telemetry
```python
# Production-ready monitoring:
- Plugin load times
- Command execution metrics
- Error rate tracking
- Memory usage per plugin
- OpenTelemetry integration
- Prometheus metrics export
```

#### 5. Security
```python
# Enterprise security:
- Plugin signature verification
- Sandboxed execution
- Resource limits (CPU, memory)
- Permission system
- Audit logging
```

---

## Official Plugins

### 1. structum_tree ✅ IMPLEMENTED
- **Version**: v2.0.0-alpha.1
- **Category**: Utility
- **Description**: Directory structure visualization with multiple themes
- **Dependencies**: `structum-core>=2.0.0a1`, `rich>=13.0`
- **Entry Point**: `tree = "structum_tree.plugin:TreePlugin"`
- **Status**: Installed and tested

### 2. structum_archive ✅ IMPLEMENTED
- **Version**: v2.0.0-alpha.1
- **Category**: Export
- **Description**: Code archiving to Markdown with ToC and tree
- **Dependencies**: `structum-core>=2.0.0a1`, `structum_tree>=2.0.0a1`, `rich>=13.0`
- **Entry Point**: `archive = "structum_archive.plugin:ArchivePlugin"`
- **Status**: Installed and tested

### 3. structum_clean
- **Category**: Utility
- **Description**: Cleanup utilities
- **Dependencies**: None
- **Size**: ~15KB

### 4. structum_docs
- **Category**: Documentation
- **Description**: Documentation management
- **Dependencies**: mkdocs
- **Size**: ~20KB

### 5. structum_plugins
- **Category**: Core
- **Description**: Plugin management interface
- **Dependencies**: structum-core
- **Size**: ~25KB
- **Commands**: list, info, enable, disable, new, search, update

---

## Installation Strategies

### Strategy 1: Full Installation (Current Users)
```bash
pip install structum
# Installs: structum-core + all official plugins
```

### Strategy 2: Core Only (Framework Users)
```bash
pip install structum-core
# Minimal installation, add plugins as needed
```

### Strategy 3: Selective Installation
```bash
pip install structum-core structum_tree structum_archive
# Only install what you need
```

### Strategy 4: Development
```bash
pip install structum-core[dev]
# Core + development tools
```

---

## Enterprise Features

### 1. Health Checks
```python
# Plugin health monitoring
structum health check --all
structum health check --plugin tree

# Output:
✓ structum-core: OK (v2.0.0)
✓ structum_tree: OK (v1.0.0)
✗ structum_archive: DEGRADED (slow response)
✓ structum_plugins: OK (v1.0.0)
```

### 2. Performance Monitoring
```python
# Built-in performance tracking
structum monitor --plugin tree
structum metrics export --format prometheus

# Metrics tracked:
- Plugin load time
- Command execution time
- Memory usage
- Error rates
- Cache hit rates
```

### 3. Plugin Dependencies
```python
# Declare plugin dependencies in pyproject.toml
[project.entry-points."structum.plugins"]
my-plugin = "my_plugin:MyPlugin"

[tool.structum.plugin]
requires-plugins = ["structum_tree>=1.0.0"]
conflicts-with = ["old-tree-plugin"]
```

### 4. Security Features
```python
# Plugin verification
structum security verify --plugin tree
structum security audit --all

# Sandboxing
structum config set security.sandbox_mode strict
```

### 5. Hot Reload
```python
# Development mode with hot reload
structum --watch
# Automatically reloads plugins on code change
```

### 6. Multi-Environment Support
```python
# Environment-specific configs
structum --env production tree .
structum --env development tree .

# Config hierarchy:
# 1. ~/.config/structum/config.yaml (global)
# 2. ./.structum.yaml (project)
# 3. Environment variables
# 4. CLI arguments
```

---

## Migration Path (v1 → v2)

### Phase 1: Core Extraction ✅ COMPLETED
1. ✅ Move plugin system to core
2. ✅ Create minimal CLI bootstrap
3. ✅ Extract configuration management
4. ✅ Add monitoring infrastructure
5. ✅ Add security framework

### Phase 2: Plugin Separation ✅ COMPLETED
1. ✅ Extract tree → structum_tree (v2.0.0-alpha.1)
2. ✅ Extract archive → structum_archive (v2.0.0-alpha.1)
3. ✅ Extract clean → structum_clean (v2.0.0-alpha.1)
4. ✅ Extract docs → structum_docs (v2.0.0-alpha.1)
5. ✅ Extract plugins management → structum_plugins (v2.0.0-alpha.1)

### Phase 3: Meta-Package ✅ COMPLETED
1. ✅ Created structum meta-package (v2.0.0-alpha.1)
2. ✅ Setup monorepo structure (for alpha/beta development)
3. ⬜ Update CI/CD pipelines (deferred to Phase 5)
4. ✅ Coordinated versioning strategy (synchronized for v2.0.0a1)

**Note**: Phase 3 implementation revealed naming issues. See Phase 3.5 for refactoring plan.

### Phase 3.5: Naming Refactor ✅ COMPLETED

**Problem Identified**: `pip install structum-core` was confusing and didn't follow industry standards. The core framework should be named `structum`, not `structum-core`.

**Refactoring Completed**:

1. ✅ **Analysis Complete** - Documented naming issues
2. ✅ **Renamed structum-core → structum**
   - Directory: `structum-core/` → `structum/`
   - Package name: `structum-core` → `structum`
   - Now matches pytest, flask, django pattern
3. ✅ **Added Optional Dependencies to Core**
   ```toml
   [project.optional-dependencies]
   tree = ["structum_tree>=2.0.0a1"]
   archive = ["structum_archive>=2.0.0a1"]
   clean = ["structum_clean>=2.0.0a1"]
   docs = ["structum_docs>=2.0.0a1"]
   plugins = ["structum_plugins>=2.0.0a1"]
   full = [
       "structum_tree>=2.0.0a1",
       "structum_archive>=2.0.0a1",
       "structum_clean>=2.0.0a1",
       "structum_docs>=2.0.0a1",
       "structum_plugins>=2.0.0a1",
   ]
   ```
4. ✅ **Eliminated Meta-Package**
   - Deleted `structum-meta/` directory
   - Replaced with `pip install structum[full]` pattern
5. ✅ **Updated All Plugin Dependencies**
   - Updated all 5 plugin pyproject.toml files
   - Changed: `structum-core>=2.0.0a1` → `structum>=2.0.0a1`
6. ✅ **Tested New Installation Patterns**
   - `pip install structum` - core only ✅
   - All 5 plugins load correctly ✅
   - Clean, professional user experience ✅

**Results Achieved**:
- ✅ Clear, intuitive naming
- ✅ Follows industry best practices
- ✅ Better user experience
- ✅ Simpler maintenance
- ✅ All tests passing

### Phase 3.6: Development Tooling ✅ COMPLETED

**Objective**: Improve developer experience with setup automation and tooling.

**Work Completed**:

1. ✅ **Development Setup Script** (`dev-setup.sh`)
   - Automated installation of all packages in editable mode
   - Virtual environment detection
   - Python version check
   - Installs core + all plugins + dev dependencies
   - Clear instructions for next steps

**Usage**:
```bash
./dev-setup.sh
```

**Benefits**:
- ✅ One-command setup for new contributors
- ✅ Ensures consistent development environment
- ✅ Reduces onboarding friction

### Phase 3.7: Test Configuration ✅ COMPLETED

**Objective**: Establish testing strategy for monorepo architecture.

**Work Completed**:

1. ✅ **Monorepo Test Runner** (`run-tests.sh`)
   - Runs tests for all packages in monorepo
   - Color-coded output (pass/fail indicators)
   - Summary report with pass/fail counts
   - Support for verbose and coverage options

2. ✅ **Testing Documentation** (`TESTING.md`)
   - Complete testing guide for contributors
   - Package-specific test organization
   - Coverage targets (core: 85%+, plugins: 70%+)
   - Best practices and troubleshooting
   - Future enhancement roadmap

**Testing Strategy**:
- Each package has its own `tests/` directory
- Independent test suites (no cross-package tests)
- Monorepo script runs all packages sequentially
- Legacy v1.x tests marked as deprecated

**Usage**:
```bash
# Run all tests
./run-tests.sh

# Run specific package
cd structum && pytest
cd structum_tree && pytest
```

**Benefits**:
- ✅ Clear testing strategy for monorepo
- ✅ Easy to run all tests or package-specific tests
- ✅ Documented coverage targets and best practices
- ✅ Foundation for CI/CD integration

### Phase 3.8: Build and Development Scripts ✅ COMPLETED

**Goal**: Organize development scripts into proper directory structure, add build automation, and implement industry-standard task runner.

**Changes**:

1. ✅ Created `scripts/` directory for all development scripts
2. ✅ Moved existing scripts to organized location
3. ✅ Added build automation tools
4. ✅ Created root `pyproject.toml` with hatch task runner
5. ✅ Updated all documentation references

**Script Organization**:
```bash
scripts/
├── README.md              # Comprehensive script documentation
├── dev-setup.sh          # Development environment setup
├── run-tests.sh          # Monorepo test runner
├── build-all.sh          # Build all packages
└── clean-builds.sh       # Clean build artifacts
```

**Hatch Task Runner** (industry-standard, used by pytest, black, pip):
```bash
# Development
hatch run setup              # Run dev-setup.sh

# Testing
hatch run test               # Run all tests
hatch run test-verbose       # Run tests with verbose output

# Building
hatch run build              # Build all packages
hatch run clean              # Clean build artifacts

# Linting & Formatting
hatch run lint               # Run ruff + mypy
hatch run format             # Format code with ruff

# Combined CI workflow
hatch run ci                 # clean + test + lint + build
```

**Why Hatch (not tox or just)**:

- ✅ Already using hatchling as build backend
- ✅ Industry standard (pytest, black, pip use it)
- ✅ Python-native, no external dependencies
- ✅ PEP 621 compliant
- ✅ Combines task running + building + publishing

**Files Created**:

- `scripts/README.md`: Complete documentation for all scripts
- `scripts/build-all.sh`: Builds all packages using `python -m build` (PEP 517)
- `scripts/clean-builds.sh`: Cleans dist/, build/, .egg-info across all packages
- `pyproject.toml` (root): Hatch scripts configuration for monorepo tasks

**Files Updated**:

- `TESTING.md`: Updated script paths (`./run-tests.sh` → `./scripts/run-tests.sh`)

**Benefits**:

- ✅ Industry-standard directory structure (follows pytest, flask, django)
- ✅ Professional task automation without Makefile
- ✅ Clear documentation for all development workflows
- ✅ Easy CI/CD integration via hatch commands
- ✅ Consistent with existing build tools (hatchling)

### Phase 3.9: CI/CD Configuration ✅ COMPLETED

**Goal**: Configure GitHub Actions workflows, pre-commit hooks, and release automation for monorepo v2.0.

**Changes**:

1. ✅ Replaced monolithic CI with modular workflows
2. ✅ Created pre-commit hooks configuration
3. ✅ Set up release-please automation
4. ✅ Configured PyPI trusted publishing

**GitHub Actions Workflows**:

- `tests.yml` - Run all package tests on Python 3.11, 3.12, 3.13
- `lint.yml` - Ruff linting and formatting checks
- `build.yml` - Build all packages and upload artifacts
- `publish.yml` - Publish to PyPI (triggered on release)
- `release-please.yml` - Automated release PR generation

**Pre-commit Hooks** (`.pre-commit-config.yaml`):

- Ruff (linter + formatter)
- MyPy (type checking)
- REUSE compliance (SPDX headers)
- Markdown linting
- General file checks (EOF, trailing whitespace, YAML, TOML)

**CI/CD Integration**:

```bash
# Local development matches CI exactly
hatch run test      # Same as tests.yml
hatch run lint      # Same as lint.yml
hatch run build     # Same as build.yml
hatch run ci        # Run complete CI workflow locally
```

**Release Automation**:

1. Merge to `main` → release-please creates PR with changelog
2. Merge release PR → GitHub Release created
3. Release created → publish.yml uploads to PyPI (trusted publishing)

**Files Created**:

- `.github/workflows/tests.yml` - Multi-version Python testing
- `.github/workflows/lint.yml` - Code quality checks
- `.github/workflows/build.yml` - Package building
- `.github/workflows/publish.yml` - PyPI publishing
- `.github/workflows/release-please.yml` - Release automation
- `.pre-commit-config.yaml` - Pre-commit hooks

**Files Removed**:

- `.github/workflows/main_ci.yml` - Replaced by modular workflows

**Benefits**:

- ✅ Modular CI workflows (easier to debug, faster feedback)
- ✅ Multi-version Python testing (3.11, 3.12, 3.13)
- ✅ Pre-commit hooks enforce quality before commit
- ✅ Automated releases with conventional commits
- ✅ PyPI trusted publishing (no API tokens needed)
- ✅ Local CI commands match GitHub Actions exactly

### Phase 4: Enterprise Features
1. ⬜ Implement health checks
2. ⬜ Add performance monitoring
3. ⬜ Add security features
4. ⬜ Add hot reload support
5. ⬜ Add multi-environment support

### Phase 5: Testing, Documentation & Release ⏳ IN PROGRESS

1. ✅ Create test infrastructure for all packages (Phase 5.1 - completed 2025-12-11)
2. ⬜ Expand test coverage to meet targets (Phase 5.2)
3. ⬜ Update all documentation (Phase 5.3)
4. ⬜ Create migration guide (Phase 5.4)
5. ⬜ Release v2.0.0-beta.1 (Phase 5.5)
6. ⬜ Release v2.0.0 stable (Phase 5.6)

---

## Architectural Decisions & Rationale

### Decision 1: Monorepo vs Multi-Repo (Phase 3)

**Decision**: Use monorepo for alpha/beta, transition to multi-repo for stable release.

**Rationale**:
- **Monorepo benefits during development**: Easier coordination, atomic commits across packages, simpler testing
- **Multi-repo for production**: Industry standard (pytest, flask), independent versioning, cleaner releases
- **Transition plan**: Keep monorepo until v2.0.0 stable, then split to individual repos

**Implementation**: Current monorepo structure with separate package directories.

### Decision 2: Versioning Strategy (Phase 3)

**Decision**: Synchronized versioning for v2.0.0 alpha/beta, independent versioning post-stable.

**Rationale**:
- **Alpha/Beta**: All packages at `2.0.0a1` simplifies testing and communication
- **Post-Stable**: Independent versioning allows plugin updates without core changes
- **Compatibility**: Use version constraints (e.g., `structum>=2.0.0,<3.0.0`)

**Example**:
```toml
# During alpha/beta (current)
structum==2.0.0a1
structum_tree==2.0.0a1

# Post-stable (future)
structum==2.1.0
structum_tree==2.3.5  # Can evolve independently
```

### Decision 3: Naming Convention (Phase 3.5)

**Decision**: Rename `structum-core` → `structum`, eliminate meta-package, use optional dependencies.

**Rationale**:
- **User confusion**: `pip install structum-core` doesn't communicate "this is the main package"
- **Industry standard**: pytest, flask, django all use the framework name for the core
- **Better UX**: `pip install structum` for core, `pip install structum[full]` for everything
- **Simpler maintenance**: One less package to manage

**Migration**: Planned for Phase 3.5.

### Decision 4: Meta-Package Pattern (Phase 3)

**Decision**: Initially created meta-package, will replace with optional dependencies.

**Rationale**:
- **Initial approach**: Separate meta-package bundles all plugins
- **Problem discovered**: Confusing naming, extra package to maintain
- **Better solution**: Optional dependencies in core (`[full]`, `[plugins]`, etc.)
- **Lesson learned**: Test naming patterns before committing to architecture

**Status**: Meta-package created in Phase 3, will be eliminated in Phase 3.5.

### Decision 5: Plugin Naming Convention

**Decision**: Use `structum_*` naming for official plugins (underscore, not dash).

**Rationale**:
- **PyPI convention**: Dashes on PyPI (`structum-tree`), underscores in Python imports (`structum_tree`)
- **Official marker**: Plugins starting with `structum_` are automatically tagged as `[OFFICIAL]`
- **Community plugins**: Use any name (e.g., `structum-plugin-latex`, `my-custom-plugin`)

**Implementation**: Entry point detection checks package name prefix.

### Decision 6: Dependency Management

**Decision**: Plugins depend on core only, not on each other (except documented cases).

**Rationale**:
- **Loose coupling**: Plugins should be independent
- **Exception**: `structum_archive` depends on `structum_tree` for reusable tree rendering
- **Documentation**: Dependencies must be clearly documented in README

**Example**:
```toml
# Most plugins
dependencies = ["structum>=2.0.0a1"]

# Exception: archive needs tree utilities
dependencies = ["structum>=2.0.0a1", "structum_tree>=2.0.0a1"]
```

---

## Benefits

### For Users
- **Flexibility**: Install only what you need
- **Performance**: Minimal overhead, lazy loading
- **Reliability**: Production-grade monitoring
- **Security**: Enterprise-level security features

### For Plugin Developers
- **Clean SDK**: Clear contracts, excellent DX
- **Rich Ecosystem**: Build on solid foundation
- **No Vendor Lock-in**: Plugins are independent
- **Great Tools**: Plugin generator, testing utilities

### For Enterprise
- **Scalability**: Hundreds of plugins without issues
- **Monitoring**: Full observability
- **Security**: Audit trail, sandboxing, verification
- **Support**: Long-term stability guarantees

---

## Technical Specifications

### Performance Targets

| Metric | Target | Rationale |
|--------|--------|-----------|
| Core startup time | < 50ms | Fast CLI experience |
| Plugin discovery | < 100ms | Even with 100+ plugins |
| Plugin load time | < 50ms per plugin | Lazy loading |
| Memory overhead | < 10MB | Core only |
| Plugin isolation overhead | < 5ms | Acceptable latency |

### Scalability Targets

| Scenario | Target | Strategy |
|----------|--------|----------|
| Number of plugins | 1000+ | Lazy loading, indexing |
| Plugin size | Up to 100MB | Streaming, lazy import |
| Concurrent commands | 100+ | Process isolation |
| Config file size | Up to 10MB | Lazy parsing, caching |

### Compatibility

- Python: 3.11+
- OS: Linux, macOS, Windows
- Architecture: x86_64, ARM64
- Dependencies: Minimal (typer, rich, pydantic)

---

## Open Questions

1. **Repository Structure**: Monorepo vs multi-repo?
   - Monorepo: Easier coordination, shared CI/CD
   - Multi-repo: Independent releases, cleaner separation

2. **Versioning Strategy**: How to version core vs plugins?
   - Semantic versioning for all
   - Core defines compatibility contract

3. **Plugin Marketplace**: Build a plugin discovery service?
   - Like VSCode marketplace
   - Community contributions

4. **Backward Compatibility**: Support v1 plugins in v2?
   - Add compatibility layer?
   - Clean break for v2?

---

## Next Steps

1. [ ] Review and approve architecture
2. [ ] Choose repository structure
3. [ ] Start Phase 1: Core extraction
4. [ ] Set up development workflow
5. [ ] Begin plugin separation

---

**Document Version**: 1.1
**Last Updated**: 2025-12-09
**Status**: 🟢 IN PROGRESS - Phase 1 Complete, Phase 2 In Progress (2/5)
