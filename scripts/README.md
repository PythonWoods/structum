# Development Scripts

This directory contains development and build automation scripts for the Structum monorepo.

## Quick Start (Recommended)

Use **hatch** commands from the root directory:

```bash
# Development
hatch run setup          # Setup development environment
hatch run test           # Run all tests
hatch run lint           # Run linters
hatch run format         # Format code

# Building
hatch run build          # Build all packages
hatch run clean          # Clean build artifacts

# CI workflow
hatch run ci             # Run complete CI pipeline
```

**Why hatch?** Industry-standard task runner, already used for our build system.

## Direct Script Usage

You can also run scripts directly:

## Available Scripts

### Development Setup

#### `dev-setup.sh`

One-command setup for local development environment.

```bash
./scripts/dev-setup.sh
```

**What it does:**
- Checks Python version
- Validates virtual environment
- Installs core + all plugins in editable mode
- Installs development dependencies (pytest, ruff, mypy)
- Shows next steps

**Requirements:**
- Python 3.11+
- Virtual environment (recommended)

---

### Testing

#### `run-tests.sh`

Run tests for all packages in the monorepo.

```bash
# Run all tests
./scripts/run-tests.sh

# With options
./scripts/run-tests.sh --verbose
./scripts/run-tests.sh --coverage
```

**What it does:**
- Runs pytest for each package (core + 5 plugins)
- Shows color-coded pass/fail indicators
- Displays summary with counts
- Exits with code 1 if any tests fail

**Per-package testing:**
```bash
cd structum && pytest
cd structum_tree && pytest --cov
```

---

### Building

#### `build-all.sh`

Build distribution packages for all packages.

```bash
./scripts/build-all.sh
```

**What it does:**
- Cleans old build artifacts
- Builds wheel + sdist for each package
- Uses Python build tool (PEP 517)
- Shows build summary
- Lists generated files

**Output:**
- `structum/dist/` - Core package distributions
- `structum_tree/dist/` - Tree plugin distributions
- ... etc for all packages

**Requirements:**
- `pip install build`

---

#### `clean-builds.sh`

Clean all build artifacts from monorepo.

```bash
./scripts/clean-builds.sh
```

**What it does:**
- Removes `dist/` directories
- Removes `build/` directories
- Removes `*.egg-info` directories
- Removes Python cache (`__pycache__`, `.pyc`)
- Removes pytest cache
- Removes coverage files

**When to use:**
- Before building fresh packages
- To free up disk space
- When switching branches

---

## Script Organization

Following industry standards (pytest, flask, django), all development scripts are organized in the `scripts/` directory:

```
scripts/
├── README.md           # This file
├── dev-setup.sh        # Development environment setup
├── run-tests.sh        # Monorepo test runner
├── build-all.sh        # Build all packages
└── clean-builds.sh     # Clean build artifacts
```

## Best Practices

### For Contributors

1. **Setup**: Run `./scripts/dev-setup.sh` once after cloning
2. **Testing**: Run `./scripts/run-tests.sh` before committing
3. **Building**: Run `./scripts/build-all.sh` before creating releases

### For Maintainers

1. **Clean Build**:
   ```bash
   ./scripts/clean-builds.sh
   ./scripts/build-all.sh
   ```

2. **Test Everything**:
   ```bash
   ./scripts/run-tests.sh --verbose
   ```

3. **Publish** (after building):
   ```bash
   twine upload structum/dist/*
   twine upload structum_*/dist/*
   ```

## CI/CD Integration

These scripts are designed to be used in CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Setup
  run: ./scripts/dev-setup.sh

- name: Test
  run: ./scripts/run-tests.sh

- name: Build
  run: ./scripts/build-all.sh
```

## Troubleshooting

### Permission Denied

Make scripts executable:
```bash
chmod +x scripts/*.sh
```

### Build Tool Not Found

Install build dependencies:
```bash
pip install build twine
```

### Tests Failing

Run individual package tests for details:
```bash
cd structum
pytest -v
```

## Future Enhancements

Planned scripts:
- `publish-all.sh` - Automated PyPI publishing
- `bump-version.sh` - Version bumping across packages
- `check-style.sh` - Linting and formatting check
- `generate-docs.sh` - Documentation generation

See [ARCHITECTURE_V2.md](../ARCHITECTURE_V2.md) for roadmap.
