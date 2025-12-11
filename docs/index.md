# Welcome to Structum v2.0

**Structum** is an enterprise-grade plugin framework for building extensible CLI applications.

## What is Structum?

Structum v2.0 is a **minimal plugin framework** that provides infrastructure for modular, extensible command-line tools. All functionality is delivered via plugins - the core provides only the essential infrastructure.

## Key Features

- **Plugin-First Architecture**: Everything is a plugin, no built-in commands
- **Auto-Discovery**: Plugins automatically registered via Python entry points
- **Minimal Core**: Lightweight framework with essential infrastructure only
- **Optional Dependencies**: Install only the plugins you need (`structum[full]`)
- **Enterprise-Grade**: Production-ready with monitoring, security, and configuration
- **Developer-Friendly**: Clear SDK, excellent developer experience

## Quick Links

- [Getting Started](getting-started.md) - Installation and quick start
- [CLI Reference](cli/index.md) - Command documentation
- [Development Guide](development/index.md) - Contributing and plugin development
- [GitHub Repository](https://github.com/pythonwoods/structum)

## Official Plugins

Install with `pip install structum[full]`:

1. **tree** - Directory tree visualization
2. **archive** - Code archiving to Markdown
3. **clean** - Cleanup utilities (`__pycache__` removal)
4. **docs** - Documentation management (MkDocs)
5. **plugins** - Plugin management and generator

## Architecture

```
structum/               # Core framework (infrastructure only)
├── plugins/           # Plugin system (loader, registry, SDK)
├── config/            # Configuration management
├── monitoring/        # Performance metrics
└── security/          # Security validation

structum_tree/         # Official plugins
structum_archive/
structum_clean/
structum_docs/
structum_plugins/
```

See [ARCHITECTURE_V2.md](https://github.com/pythonwoods/structum/blob/develop/ARCHITECTURE_V2.md) for complete design documentation.

## Development Status

**Current**: v2.0.0-alpha.1

- ✅ Core architecture complete
- ✅ Plugin system stable
- ✅ 5 official plugins released
- ⏳ Expanding test coverage
- 🎯 Target: v2.0.0-beta.1 (Q1 2025)

---

**Get Started**: [Installation Guide →](getting-started.md)
