# CLI Usage

Structum is a command-line tool with three primary subcommands: `tree`, `archive`, and `clean`.

## 1. `structum tree`

Visualizes the directory structure of the specified path.

### Arguments
*   `DIRECTORY`: The root directory to analyze. Defaults to current directory (`.`).

### Options
*   `--ext, -e`: Filter by file extensions (e.g., `-e py -e md`).
*   `--ignore, -i`: Directory names to exclude (e.g., `-i .git`).
*   `--depth, -d`: Maximum depth of the tree traversal.
*   `--hidden / --no-hidden`: Show hidden files/directories. Default: `False`.
*   `--no-empty`: Hide directories that do not contain visible files.
*   `--theme, -t`: Icon theme (`emoji`, `nerd`, `ascii`, `none`). Default: `emoji`.

---

## 2. `structum archive`

Archives source code into Markdown files.

### Arguments
*   `DIRECTORY`: The root directory to archive. Defaults to current directory (`.`).

### Options
*   `--output, -o`: Output file path (or directory if split mode is enabled). Default: `archive.md`.
*   `--ext, -e`: Filter by file extensions.
*   `--ignore, -i`: Directory names to exclude.
*   `--split-folder`: Create a separate archive for each folder.
*   `--split-type`: Create a separate archive for each file extension.
*   `--toc / --no-toc`: Include a Table of Contents. Default: `True`.
*   `--tree / --no-tree`: Include a directory tree structure. Default: `True`.
*   `--verbose / --quiet`: Enable verbose output. Default: `True`.

---

## 3. `structum clean`

Recursively removes all `__pycache__` directories.

### Arguments
*   `DIRECTORY`: The root directory to clean. Defaults to current directory (`.`).

### Options
*   `--verbose / --quiet`: Enable verbose output. Default: `True`.