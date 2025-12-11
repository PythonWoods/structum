# Contributing to Structum

Thank you for your interest in contributing to Structum! We welcome contributions from the community to help make this project better.

## 🏗️ V2.0 Monorepo Architecture

Structum v2.0 uses a **monorepo structure** with a minimal core and plugin-based architecture:

```
structum/                    # Core framework package
structum_tree/              # Tree visualization plugin
structum_archive/           # Code archiving plugin
structum_clean/             # Cleanup utilities plugin
structum_docs/              # Documentation management plugin
structum_plugins/           # Plugin management plugin
```

All packages are **independent** but developed together during alpha/beta phase.

---

## 🚀 Development Setup

### Quick Start (Recommended)

```bash
# Clone repository
git clone https://github.com/pythonwoods/structum.git
cd structum

# One-command setup (installs all packages + dev tools)
hatch run setup
```

### Manual Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Run development setup script
./scripts/dev-setup.sh
```

This installs:
- Core framework (`structum`) in editable mode
- All official plugins in editable mode
- Development tools (pytest, ruff, mypy, hatch)

---

## 🧪 Running Tests

```bash
# Run all tests (recommended)
hatch run test

# Run tests with coverage
hatch run test --coverage

# Run tests for specific package
cd structum && pytest
cd structum_tree && pytest
```

See [TESTING.md](TESTING.md) for comprehensive testing guide.

---

## 🔍 Code Quality

### Linting & Formatting

```bash
# Check code style
hatch run lint

# Auto-format code
hatch run format

# Run all checks
hatch run check
```

### Type Checking

We use **MyPy in strict mode**:

```bash
mypy structum/src structum_*/src
```

### Pre-commit Hooks

Install pre-commit hooks for automatic checks:

```bash
pre-commit install
```

All code must pass:
- ✅ Ruff linting (PEP 8 compliance)
- ✅ Ruff formatting
- ✅ MyPy type checking (strict)
- ✅ REUSE license compliance

---

## 📦 Project Structure

### Core Framework (`structum/`)

```
structum/
├── src/structum/
│   ├── cli/bootstrap.py     # Minimal CLI entry point
│   ├── plugins/             # Plugin system (loader, registry, SDK)
│   ├── config/              # Configuration management
│   ├── monitoring/          # Performance metrics
│   └── security/            # Security validation
├── tests/                   # Core tests
└── pyproject.toml
```

### Plugin Packages (`structum_*/`)

```
structum_tree/               # Example plugin
├── src/structum_tree/
│   ├── plugin.py           # Plugin class (PluginBase)
│   ├── core.py             # Business logic
│   └── __init__.py
├── tests/                  # Plugin tests
└── pyproject.toml
```

---

## 🔌 Contributing to Core

### Modifying Core Framework

Core framework provides **only infrastructure**, no commands:

- **Plugin System**: `structum/src/structum/plugins/`
- **Configuration**: `structum/src/structum/config/`
- **Monitoring**: `structum/src/structum/monitoring/`
- **Security**: `structum/src/structum/security/`

**Example: Adding a new core feature**

```bash
# 1. Add implementation
cd structum/src/structum/monitoring/
# Edit metrics.py

# 2. Add tests
cd ../../tests/unit/
# Create test_monitoring.py

# 3. Run tests
cd ../..
pytest
```

---

## 🎨 Creating a Plugin

### Method 1: Using Plugin Generator (Recommended)

```bash
structum plugins new my-awesome-tool --category utility --output ~/projects/
```

This creates a complete plugin structure with:
- Entry point configuration
- Plugin class skeleton
- README and documentation
- pyproject.toml with dependencies

### Method 2: Manual Plugin Creation

1. **Create package directory**:
   ```bash
   mkdir -p structum_mytool/src/structum_mytool
   ```

2. **Create plugin class** (`plugin.py`):
   ```python
   from structum.plugins.sdk import PluginBase
   import typer

   class MyToolPlugin(PluginBase):
       name = "mytool"
       version = "0.1.0"
       category = "utility"
       description = "My awesome tool"

       def setup(self) -> None:
           """Initialize plugin."""
           pass

       def register_commands(self, app: typer.Typer) -> None:
           """Register CLI commands."""
           @app.command(name="mytool")
           def mytool_cmd(path: str = typer.Argument(...)):
               """Run my tool."""
               print(f"Processing {path}")
   ```

3. **Create `pyproject.toml`**:
   ```toml
   [project]
   name = "structum-mytool"
   version = "0.1.0"
   dependencies = ["structum>=2.0.0a1"]

   [project.entry-points."structum.plugins"]
   mytool = "structum_mytool.plugin:MyToolPlugin"
   ```

4. **Install in editable mode**:
   ```bash
   pip install -e ./structum_mytool
   ```

5. **Test it**:
   ```bash
   structum mytool /path/to/something
   ```

### Plugin Categories

- `analysis` – Code analysis and metrics
- `export` – Export and format conversion
- `formatting` – Code formatting and style
- `utility` – Utility and helper tools

---

## 📝 Documentation

### Serving Docs Locally

```bash
structum docs serve
```

Or directly with MkDocs:

```bash
mkdocs serve
```

### Building Docs

```bash
mkdocs build
```

### Documentation Structure

```
docs/
├── index.md                # Main documentation page
├── getting-started.md      # Quick start guide
├── architecture/           # Architecture documentation
├── cli/                    # CLI reference
├── development/            # Development guides
└── reference/              # API reference
```

---

## 🔄 Git Workflow

### Branching Strategy

- `main` – Stable releases only
- `develop` – Active development (default branch)
- Feature branches: `feature/my-feature`
- Bug fixes: `fix/issue-123`

### Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(tree): add depth limit option
fix(archive): handle empty directories
docs: update plugin development guide
test: add tests for config manager
ci: update GitHub Actions workflow
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

### Pull Requests

1. **Fork** the repository
2. **Create branch** from `develop`
3. **Make changes** with clear commits
4. **Add tests** for new features
5. **Run checks**: `hatch run ci`
6. **Submit PR** to `develop` branch

**PR Template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Other (please describe)

## Testing
- [ ] Tests added/updated
- [ ] All tests passing
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
```

---

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Structum version**: `structum --version`
2. **Python version**: `python --version`
3. **OS**: Linux/macOS/Windows + version
4. **Steps to reproduce**
5. **Expected vs actual behavior**
6. **Error messages** (full traceback)

---

## 💡 Need Help?

- **Documentation**: <https://pythonwoods.github.io/structum/>
- **CLAUDE.md**: Development guide for contributors
- **ARCHITECTURE_V2.md**: Complete v2.0 architecture design
- **TESTING.md**: Testing strategy and conventions

---

## 📄 License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

All source files must include SPDX headers:

```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods
```

---

**Thank you for contributing to Structum! 🎉**
