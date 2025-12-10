# structum_clean

Official cleanup plugin for Structum.

## Description

This plugin provides cleanup utilities for the Structum framework. It recursively removes `__pycache__` directories from Python projects, helping keep your codebase clean and reducing disk usage.

## Features

- **Recursive Cleanup**: Automatically finds and removes all `__pycache__` directories
- **Virtual Environment Protection**: Optionally skip virtual environment directories
- **Verbose Output**: See exactly what's being removed in real-time
- **Safe Operations**: Handles errors gracefully and reports issues
- **Statistics**: Shows total number of removed directories

## Installation

```bash
pip install structum_clean
```

Or install as part of the full Structum bundle:

```bash
pip install structum
```

## Usage

Basic usage:

```bash
structum clean .
```

With options:

```bash
# Clean specific directory
structum clean src

# Quiet mode (no verbose output)
structum clean . --quiet

# Skip virtual environment directories
structum clean . --skip-venv

# Clean with short flags
structum clean . -q
```

## Options

- `directory`: Root directory to clean (default: current directory)
- `--verbose/-v, --quiet/-q`: Toggle verbose output (default: verbose)
- `--skip-venv`: Skip virtual environment directories (.env, venv, .venv, etc.)

## Why Clean __pycache__?

Python automatically creates `__pycache__` directories to store bytecode-compiled versions of modules. While these improve performance, they can:

- Accumulate over time and consume disk space
- Cause confusion when switching between Python versions
- Clutter version control systems if not properly ignored
- Create issues when moving projects between systems

This plugin helps maintain a clean project structure by safely removing these directories. Python will recreate them automatically when needed.

## License

Apache-2.0

## Author

PythonWoods
