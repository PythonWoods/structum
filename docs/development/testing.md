# Testing Guide

Comprehensive testing guide for Structum v2.0 monorepo.

## Architecture

Structum v2.0 uses a **monorepo structure** with separate test suites for each package:

```
structum/tests/              # Core framework tests
structum_tree/tests/         # Tree plugin tests
structum_archive/tests/      # Archive plugin tests
structum_clean/tests/        # Clean plugin tests
structum_docs/tests/          # Docs plugin tests
structum_plugins/tests/      # Plugins plugin tests
```

Each package has its own independent test suite.

## Running Tests

### Run All Tests (Recommended)

```bash
# Using hatch (recommended)
hatch run test

# Or directly
./scripts/run-tests.sh
```

This runs tests for all 6 packages (core + 5 plugins).

### Run Tests for Specific Package

```bash
# Core framework
cd structum && pytest

# Specific plugin
cd structum_tree && pytest

# With coverage
cd structum && pytest --cov=structum --cov-report=term
```

### Run Specific Test File

```bash
pytest structum/tests/unit/test_version.py
```

### Run Specific Test Function

```bash
pytest structum/tests/unit/test_version.py::test_version_exists
```

### Run with Verbose Output

```bash
pytest -v
pytest -vv  # Extra verbose
```

## Test Structure

### Directory Layout

```
package/
├── src/package_name/       # Source code
│   ├── plugin.py
│   └── core.py
└── tests/                  # Test suite
    ├── conftest.py         # Shared fixtures
    ├── unit/               # Unit tests
    │   ├── test_plugin.py
    │   └── test_core.py
    └── integration/        # Integration tests (optional)
```

### Test Organization

- **Unit tests**: Test individual functions/classes in isolation
- **Integration tests**: Test interaction between components
- **CLI tests**: Test command-line interface using `typer.testing.CliRunner`

## Writing Tests

### Basic Test Example

```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Tests for version information."""

import structum


def test_version_exists():
    """Verify that the package has a version attribute."""
    assert hasattr(structum, "__version__")
    assert structum.__version__ is not None


def test_version_is_string():
    """Verify version is a string."""
    assert isinstance(structum.__version__, str)
```

### Using Fixtures

```python
import pytest
from pathlib import Path


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Path:
    """Create a temporary workspace."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    return workspace


@pytest.fixture
def sample_files(tmp_workspace: Path) -> Path:
    """Create sample files for testing."""
    (tmp_workspace / "file1.txt").write_text("Content 1")
    (tmp_workspace / "file2.py").write_text("# Python code")

    subdir = tmp_workspace / "subdir"
    subdir.mkdir()
    (subdir / "file3.md").write_text("# Markdown")

    return tmp_workspace


def test_with_fixtures(sample_files: Path):
    """Test using fixtures."""
    assert (sample_files / "file1.txt").exists()
    assert (sample_files / "subdir").is_dir()
```

### Testing CLI Commands

```python
from typer.testing import CliRunner
import typer

runner = CliRunner()


def test_tree_command():
    """Test tree command execution."""
    from structum.cli.bootstrap import create_app

    app = create_app()
    result = runner.invoke(app, ["tree", "--help"])

    assert result.exit_code == 0
    assert "tree" in result.output.lower()
```

### Testing with Mocks

```python
from unittest.mock import patch, MagicMock


@patch("structum.plugins.loader.entry_points")
def test_plugin_loading(mock_eps):
    """Test plugin loading with mocked entry points."""
    mock_ep = MagicMock()
    mock_ep.name = "test-plugin"
    mock_eps.return_value = [mock_ep]

    # Test plugin loading logic
    # ...
```

## Coverage

### Coverage Targets

- **Core framework** (`structum`): **85%+**
- **Plugins**: **70%+**
- **Overall**: **80%+**

### Current Status (2025-12-11)

- ✅ structum core: **49%** coverage (target: 85%+)
- ✅ All plugins: Basic coverage established
- ✅ 35 tests passing, 0 failures

### Generate Coverage Report

```bash
# HTML report
pytest --cov=structum --cov-report=html
open htmlcov/index.html

# Terminal report
pytest --cov=structum --cov-report=term

# Missing lines report
pytest --cov=structum --cov-report=term-missing
```

## Testing Conventions

### Test File Naming

- Unit tests: `test_*.py` (e.g., `test_plugin.py`)
- Integration tests: `test_*_integration.py`
- Fixtures: `conftest.py`

### Test Function Naming

Use descriptive names that explain what is being tested:

```python
def test_build_tree_basic()  # Good
def test_tree()              # Bad - not descriptive

def test_plugin_initialization()           # Good
def test_archive_handles_empty_directory() # Good
```

### Test Class Organization

```python
class TestTreePlugin:
    """Tests for TreePlugin class."""

    def test_initialization(self):
        """Test plugin can be initialized."""
        pass

    def test_setup(self):
        """Test plugin setup method."""
        pass


class TestTreeCore:
    """Tests for tree generation core functions."""

    def test_build_tree_basic(self):
        """Test building a basic tree."""
        pass
```

### Assertions

Be explicit and test one thing per test:

```python
# Good - clear what is being tested
def test_version_format():
    version = structum.__version__
    assert isinstance(version, str)
    assert len(version) > 0
    assert version[0].isdigit()


# Bad - too generic
def test_version():
    assert structum.__version__
```

## Fixtures

### Shared Fixtures (conftest.py)

```python
# structum/tests/conftest.py

import pytest
from pathlib import Path


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Path:
    """Create a temporary workspace."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    return workspace


@pytest.fixture(autouse=True)
def reset_plugin_registry():
    """Reset plugin registry before each test."""
    from structum.plugins.registry import PluginRegistry

    original_plugins = PluginRegistry._plugins.copy()
    original_instances = PluginRegistry._instances.copy()

    PluginRegistry.clear()
    yield

    PluginRegistry._plugins = original_plugins
    PluginRegistry._instances = original_instances
```

## Continuous Integration

Tests run automatically on:

- **Push to `main` or `develop`** branches
- **Pull requests**
- **Manual workflow dispatch**

See `.github/workflows/tests.yml` for CI configuration.

### CI Test Matrix

Tests run on:

- Python 3.11, 3.12, 3.13
- Ubuntu Latest
- Multiple test scenarios

## Debugging Tests

### Run with Debug Output

```bash
pytest -vv -s
```

### Run Specific Test with Debugging

```bash
pytest -vv -s structum/tests/unit/test_version.py::test_version_format
```

### Use pdb for Interactive Debugging

```python
def test_something():
    result = some_function()
    import pdb; pdb.set_trace()  # Breakpoint
    assert result == expected
```

## Best Practices

### 1. Test Independence

Each test should be independent and not rely on other tests:

```python
# Good - each test is self-contained
def test_feature_a():
    setup_a()
    assert feature_a() == expected_a

def test_feature_b():
    setup_b()
    assert feature_b() == expected_b


# Bad - test_b depends on test_a
def test_a():
    global state
    state = setup()

def test_b():
    assert state.something()  # Depends on test_a
```

### 2. Use Fixtures for Setup

Use fixtures instead of setup methods:

```python
# Good - using fixtures
@pytest.fixture
def configured_plugin():
    plugin = MyPlugin()
    plugin.setup()
    return plugin

def test_plugin(configured_plugin):
    assert configured_plugin.ready


# Bad - manual setup in each test
def test_plugin():
    plugin = MyPlugin()
    plugin.setup()
    assert plugin.ready
```

### 3. Test Edge Cases

Test not just the happy path, but also edge cases:

```python
def test_build_tree_basic(sample_directory):
    """Test building a basic tree."""
    tree = build_tree(sample_directory)
    assert tree is not None


def test_build_tree_nonexistent_directory():
    """Test handling of nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        build_tree(Path("/nonexistent"))


def test_build_tree_empty_directory(tmp_workspace):
    """Test handling of empty directory."""
    tree = build_tree(tmp_workspace)
    assert tree is not None
```

### 4. Keep Tests Fast

- Use mocks for slow operations (network, disk I/O)
- Avoid unnecessary sleeps
- Use temporary directories that pytest cleans up automatically

### 5. Meaningful Test Names

Test names should describe the scenario:

```python
# Good names
def test_tree_with_depth_limit_excludes_deep_files()
def test_archive_includes_directory_tree_when_requested()
def test_plugin_disabled_by_config_shows_placeholder_command()

# Bad names
def test_tree()
def test_archive()
def test_plugin()
```

## Troubleshooting

### Import Errors

If you get import errors, ensure packages are installed in editable mode:

```bash
pip install -e ./structum -e ./structum_tree -e ./structum_archive \
    -e ./structum_clean -e ./structum_docs -e ./structum_plugins
```

### Test Discovery Issues

Pytest discovers tests in files matching `test_*.py` or `*_test.py`. Ensure:

- Test files are named correctly
- Test functions start with `test_`
- Test files are in directories with `__init__.py` (if needed)

### Fixture Not Found

If a fixture is not found:

- Check it's defined in `conftest.py` in the same directory or parent
- Verify the fixture name matches exactly
- Ensure `conftest.py` is valid Python

## Additional Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest fixtures guide](https://docs.pytest.org/en/stable/fixture.html)
- [Typer testing guide](https://typer.tiangolo.com/tutorial/testing/)
- [CONTRIBUTING.md](../../CONTRIBUTING.md) - Contribution guidelines
- [conventions.md](conventions.md) - Coding conventions

---

**Questions?** See [CONTRIBUTING.md](../../CONTRIBUTING.md) or open a discussion on GitHub.
