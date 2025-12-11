# Development Conventions

This document outlines the coding standards and conventions used in Structum v2.0.

## Code Style

We use **Ruff** for both linting and formatting:

```bash
# Check code style
ruff check structum/src structum_*/src

# Auto-format code
ruff format structum/src structum_*/src
```

### Style Rules

- **Line Length**: 100 characters maximum
- **Quotes**: Double quotes for strings
- **Imports**: Automatically sorted by Ruff (isort compatible)
- **Indentation**: 4 spaces (no tabs)
- **Trailing Commas**: Required in multi-line structures

### Ruff Configuration

See `pyproject.toml` (root) for Ruff settings:

```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B"]
ignore = ["E501", "B008"]
```

## Type Hinting

We use **MyPy in strict mode**. All code must be fully typed:

```bash
mypy structum/src structum_*/src
```

### Type Hint Requirements

- **All function signatures** must have type hints for parameters and return values
- Use **Python 3.11+ union syntax**: `str | None` instead of `Optional[str]`
- Use **built-in generics**: `dict[str, Any]` instead of `Dict[str, Any]`
- Avoid `Any` when possible - use specific types

### Example

```python
from pathlib import Path

def process_file(path: Path, max_size: int | None = None) -> dict[str, str]:
    """Process a file and return metadata.

    Args:
        path: Path to file to process
        max_size: Optional maximum size in bytes

    Returns:
        Dictionary with file metadata
    """
    return {"name": path.name, "size": str(path.stat().st_size)}
```

## Docstrings

We follow the **Google docstring style**. Every public module, class, and function must have a docstring.

### Module Docstrings

```python
"""Module for handling directory tree visualization.

This module provides functionality to build and render directory trees
with multiple theme support.
"""
```

### Function Docstrings

```python
def build_tree(
    directory: Path,
    max_depth: int | None = None,
    extensions: list[str] | None = None,
) -> Tree:
    """Build a directory tree structure.

    Args:
        directory: Root directory to scan
        max_depth: Maximum recursion depth (None = unlimited)
        extensions: List of file extensions to include (e.g., [".py", ".md"])

    Returns:
        Rich Tree object representing the directory structure

    Raises:
        FileNotFoundError: If directory does not exist
        PermissionError: If directory is not accessible
    """
```

## File Headers

All source files must include SPDX license headers:

```python
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods
```

## Import Order

Ruff automatically organizes imports in this order:

1. Future imports
2. Standard library
3. Third-party packages
4. First-party (structum packages)
5. Local imports (relative)

## Naming Conventions

- **Packages**: `lowercase` or `lowercase_with_underscores`
- **Modules**: `lowercase_with_underscores.py`
- **Classes**: `PascalCase`
- **Functions/Methods**: `snake_case`
- **Constants**: `UPPER_CASE_WITH_UNDERSCORES`
- **Private**: prefix with single underscore `_private`

## Testing Conventions

- Test files: `test_*.py` or `*_test.py`
- Test functions: `test_descriptive_name()`
- Test classes: `TestFeatureName`
- Fixtures: descriptive names like `tmp_workspace`, `sample_files`

See [testing.md](testing.md) and [TESTING.md](../../TESTING.md) for complete testing guidelines.

## Commit Messages

We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `ci`: CI/CD changes
- `chore`: Maintenance tasks

**Examples:**

```
feat(tree): add depth limit option
fix(archive): handle empty directories correctly
docs: update plugin development guide
test(config): add tests for config manager
```

## Pre-commit Hooks

Install pre-commit hooks to automatically enforce standards:

```bash
pre-commit install
```

This runs on every commit:

- Ruff linting and formatting
- MyPy type checking
- REUSE license compliance
- Markdown linting
- YAML/TOML validation

## Editor Configuration

### VS Code

Recommended settings (`.vscode/settings.json`):

```json
{
  "python.linting.enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "none",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

### PyCharm

- Enable MyPy plugin
- Set Ruff as external tool for formatting
- Configure code style: 100 character line length

## Performance

- Avoid unnecessary computations in hot paths
- Use generators for large datasets
- Profile before optimizing (don't guess)
- Document performance-critical sections

## Security

- Never commit secrets or API keys
- Validate all user inputs
- Use Path objects (not strings) for file operations
- Follow principle of least privilege

---

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for complete contribution guidelines.
