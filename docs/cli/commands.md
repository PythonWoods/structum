# Commands

## Tree

Visualizes the directory structure of the specified path.

```bash
structum tree [OPTIONS] [DIRECTORY]
```

**Options:**

* `--ext, -e`: Filter by file extensions (e.g., `-e py,md` or `-e py -e md`).
* `--ignore, -i`: Directory names to exclude (e.g., `-i .git,node_modules`).
* `--depth, -d`: Maximum depth.
* `--theme, -t`: Icon theme (`emoji`, `nerd`, `ascii`).
* `--stats, -s`: Show directory and file count statistics.
* `--hidden`: Show hidden files and directories.
* `--no-empty`: Hide directories that do not contain visible files.

## Archive

Archives source code into Markdown files.

```bash
structum archive [OPTIONS] [DIRECTORY]
```

**Options:**

* `--output, -o`: Output file path.
* `--ext, -e`: Filter by file extensions (e.g., `-e py,md`).
* `--ignore, -i`: Directory names to exclude.
* `--split-folder`: Create a separate archive for each folder.
* `--split-type`: Create a separate archive for each file extension.
* `--toc / --no-toc`: Include a Table of Contents (default: True).
* `--tree / --no-tree`: Include a directory tree structure (default: True).
* `--verbose, -v / --quiet, -q`: Verbose output (default: verbose).

## Clean

Recursively removes `__pycache__` directories.

```bash
structum clean [OPTIONS] [DIRECTORY]
```

**Options:**

* `--skip-venv`: Skip virtual environment directories (`.env`, `venv`, etc.).
* `--verbose, -v / --quiet, -q`: Verbose output (default: verbose).

## Docs

Manage documentation.

### Serve

```bash
structum docs serve
```

### Deploy

```bash
structum docs deploy
```

## Plugins

Manage installed plugins.

### List

List all installed plugins.

```bash
structum plugins list
```

### Info

Show detailed information about a plugin.

```bash
structum plugins info <NAME>
```

### Enable

Enable a disabled plugin.

```bash
structum plugins enable <NAME>
```

### Disable

Disable a plugin.

```bash
structum plugins disable <NAME>
```

### New

Generate a new plugin skeleton.

```bash
structum plugins new <NAME> [--output DIR] [--category CAT]
```

**Options:**

* `--output, -o`: Output directory (default: current directory).
* `--category, -c`: Plugin category (`analysis`, `export`, `formatting`, `utility`).

## Version

Show the application version.

```bash
structum version
```

## Info

Show application information (version, Python version, platform).

```bash
structum info
```
