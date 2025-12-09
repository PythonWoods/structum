# structum_archive

Official code archiving plugin for Structum.

## Description

This plugin archives source code into well-formatted Markdown files. It's perfect for creating documentation, sharing code snippets, or preparing code for LLM context windows.

## Features

- **File Filtering**: Filter by file extensions
- **Directory Exclusion**: Exclude specific directories
- **Table of Contents**: Automatic ToC generation
- **Directory Tree**: Include project structure visualization
- **Split Modes**: Create separate archives by folder or file type
- **Multiple Output Formats**: Single file or directory-based output

## Installation

```bash
pip install structum_archive
```

Or install as part of the full Structum bundle:

```bash
pip install structum
```

## Usage

Basic usage:

```bash
structum archive . --output code.md
```

With options:

```bash
# Archive only Python files
structum archive src --ext py --output python_code.md

# Split by folder
structum archive . --split-folder --output docs/

# Split by file type
structum archive . --split-type --output archives/

# Exclude directories and disable tree
structum archive . --ignore node_modules,.git --no-tree --output code.md

# Multiple extensions
structum archive src --ext py,md,toml --output project.md
```

## Options

- `directory`: Root directory to archive (default: current directory)
- `--output, -o`: Output file path or directory
- `--ext, -e`: Filter by file extensions
- `--ignore, -i`: Directory names to exclude
- `--split-folder`: Create separate archive for each folder
- `--split-type`: Create separate archive for each file extension
- `--toc/--no-toc`: Include Table of Contents (default: yes)
- `--tree/--no-tree`: Include directory tree (default: yes)
- `--verbose/--quiet, -v/-q`: Verbose output (default: yes)

## License

Apache-2.0

## Author

PythonWoods
