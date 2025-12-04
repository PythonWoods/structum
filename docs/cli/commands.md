# Commands

## Tree

Visualizes the directory structure of the specified path.

```bash
structum tree [OPTIONS] [DIRECTORY]
```

**Options:**
*   `--ext, -e`: Filter by file extensions.
*   `--depth, -d`: Maximum depth.
*   `--theme, -t`: Icon theme (`emoji`, `nerd`, `ascii`).

## Archive

Archives source code into Markdown files.

```bash
structum archive [OPTIONS] [DIRECTORY]
```

**Options:**
*   `--output, -o`: Output file path.
*   `--split-folder`: Create a separate archive for each folder.

## Clean

Recursively removes `__pycache__` directories.

```bash
structum clean [OPTIONS] [DIRECTORY]
```

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
