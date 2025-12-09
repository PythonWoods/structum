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

### Phase 2: Plugin Separation 🔄 IN PROGRESS (2/5 completed)
1. ✅ Extract tree → structum_tree (v2.0.0-alpha.1)
2. ✅ Extract archive → structum_archive (v2.0.0-alpha.1)
3. ⬜ Extract clean → structum_clean
4. ⬜ Extract docs → structum_docs
5. ⬜ Extract plugins management → structum_plugins

### Phase 3: Meta-Package
1. ⬜ Create structum meta-package
2. ⬜ Setup monorepo or multi-repo structure
3. ⬜ Update CI/CD pipelines
4. ⬜ Coordinate versioning strategy

### Phase 4: Enterprise Features
1. ⬜ Implement health checks
2. ⬜ Add performance monitoring
3. ⬜ Add security features
4. ⬜ Add hot reload support
5. ⬜ Add multi-environment support

### Phase 5: Documentation & Release
1. ⬜ Update all documentation
2. ⬜ Create migration guide
3. ⬜ Update CLAUDE.md
4. ⬜ Release v2.0.0

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
