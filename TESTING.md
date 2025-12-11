# Testing Guide - Structum v2.0

This document describes the testing strategy for Structum's monorepo architecture.

## Architecture

Structum v2.0 uses a **monorepo structure** with separate test suites for each package:

```
structum/                    # Core framework
├── tests/                   # Core tests
└── pyproject.toml

structum_tree/              # Tree plugin
├── tests/                  # Plugin-specific tests
└── pyproject.toml

structum_archive/           # Archive plugin
├── tests/                  # Plugin-specific tests
└── pyproject.toml

[... other plugins ...]
```

## Running Tests

### Run All Tests (Monorepo)

```bash
./scripts/run-tests.sh
```

This runs tests for:
- Core framework (structum)
- All official plugins (tree, archive, clean, docs, plugins)

### Run Tests for Specific Package

```bash
# Core framework
cd structum && pytest

# Specific plugin
cd structum_tree && pytest
```

### Run with Coverage

```bash
# Per package
cd structum && pytest --cov=structum --cov-report=term-missing

# All packages (future enhancement)
./scripts/run-tests.sh --coverage
```

## Test Organization

### Core Framework Tests

Location: `structum/tests/`

Tests for core infrastructure:
- Plugin system (loader, registry, SDK)
- CLI bootstrap
- Configuration management
- Monitoring and metrics
- Security validation

Example:
```bash
structum/tests/
├── unit/
│   ├── plugins/
│   │   ├── test_loader.py
│   │   ├── test_registry.py
│   │   └── test_sdk.py
│   ├── config/
│   │   └── test_manager.py
│   └── cli/
│       └── test_bootstrap.py
└── conftest.py
```

### Plugin Tests

Each plugin has its own test suite in its package directory.

Example for `structum_tree`:
```bash
structum_tree/tests/
├── unit/
│   ├── test_plugin.py      # Plugin class tests
│   ├── test_core.py        # Business logic tests
│   └── test_utils.py       # Utility tests
└── conftest.py
```

## Writing Tests

### Test Structure

Each package follows this pattern:

```python
# tests/unit/test_feature.py
import pytest
from your_package import feature

def test_basic_functionality():
    """Test description."""
    result = feature.do_something()
    assert result == expected
```

### Fixtures

Use `conftest.py` for shared fixtures:

```python
# tests/conftest.py
import pytest

@pytest.fixture
def sample_data():
    return {"key": "value"}
```

### Mocking

Use pytest's built-in mocking:

```python
from unittest.mock import Mock, patch

def test_with_mock():
    with patch('module.function') as mock_fn:
        mock_fn.return_value = "mocked"
        # ... test code
```

## Testing Strategy

### Unit Tests

- **Core Framework**: Test plugin system, config, CLI bootstrap
- **Plugins**: Test plugin class, business logic, integration with core

### Integration Tests

Currently minimal. Future phases will add:
- Plugin interaction tests
- End-to-end CLI tests
- Performance benchmarks

### Coverage Targets

- **Core Framework**: 85%+ coverage
- **Official Plugins**: 70%+ coverage
- **Critical paths**: 95%+ coverage

## CI/CD Integration

Tests run automatically on:
- Every push to `develop` or `main`
- Every pull request
- Before release

GitHub Actions workflow runs:
```bash
./scripts/run-tests.sh
```

## Troubleshooting

### Tests Not Found

If pytest can't find tests:

```bash
# Ensure packages are installed in editable mode
./scripts/dev-setup.sh

# Or manually
pip install -e ./structum
pip install -e ./structum_tree
# ... etc
```

### Import Errors

Make sure you're in the right directory or have installed the package:

```bash
cd structum_tree
pytest  # Runs tests in context of this package
```

### Coverage Reports

Generate HTML coverage report:

```bash
cd structum
pytest --cov=structum --cov-report=html
open htmlcov/index.html
```

## Best Practices

1. **Test in Isolation**: Each package's tests should run independently
2. **No Cross-Package Tests**: Don't test plugin A in plugin B's test suite
3. **Use Fixtures**: Share test data via conftest.py fixtures
4. **Clear Names**: Test names should describe what they test
5. **Fast Tests**: Keep unit tests fast (< 1s each)

## Future Enhancements

- [ ] Coverage reporting for entire monorepo
- [ ] Integration test suite
- [ ] Performance benchmarks
- [ ] Mutation testing
- [ ] Property-based testing (Hypothesis)

## Legacy Tests

**Note**: The `tests/` directory at the repository root contains tests from the v1.x monolithic architecture. These are **deprecated** and will be migrated or removed in future phases.

Current focus is on tests within each package's directory.
