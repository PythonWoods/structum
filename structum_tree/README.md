# structum_tree

Official tree visualization plugin for Structum.

## Description

This plugin provides directory tree visualization functionality for the Structum framework. It displays directory structures in a beautiful, formatted tree view with support for multiple themes, filtering, and customization options.

## Features

- **Multiple Themes**: Choose from emoji, nerd fonts, ASCII, or no icons
- **Filtering**: Filter by file extensions
- **Exclusion**: Exclude specific directories
- **Depth Control**: Limit tree depth for large directories
- **Statistics**: Show file and directory counts
- **Hidden Files**: Optionally show/hide hidden files
- **Empty Directories**: Optionally hide empty directories

## Installation

```bash
pip install structum_tree
```

Or install as part of the full Structum bundle:

```bash
pip install structum
```

## Usage

Basic usage:

```bash
structum tree .
```

With options:

```bash
# Show tree with nerd font icons
structum tree . --theme nerd

# Filter Python files only, max depth 2
structum tree src --ext py --depth 2

# Show statistics
structum tree . --stats

# Ignore node_modules and .git
structum tree . --ignore node_modules,.git

# Show hidden files
structum tree . --hidden
```

## Options

- `directory`: Root directory to visualize (default: current directory)
- `--ext, -e`: Filter by file extensions
- `--ignore, -i`: Directory names to exclude
- `--depth, -d`: Maximum depth of tree traversal
- `--hidden`: Show hidden files and directories
- `--no-empty`: Hide empty directories
- `--theme, -t`: Icon theme (nerd, emoji, ascii, none)
- `--stats, -s`: Show directory and file count statistics

## License

Apache-2.0

## Author

PythonWoods
