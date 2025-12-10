# structum_docs

Official documentation management plugin for Structum.

## Description

This plugin provides documentation management functionality for the Structum framework, built on top of MkDocs. It allows you to serve documentation locally for development and deploy it to GitHub Pages with simple commands.

## Features

- **Local Development Server**: Serve documentation locally with live reload
- **GitHub Pages Deployment**: Deploy documentation to GitHub Pages with one command
- **Custom Address Configuration**: Configure server address and port
- **Custom Deployment Messages**: Add custom commit messages when deploying
- **Force Deployment**: Force push to gh-pages branch when needed
- **Rich Console Output**: Beautiful formatted output with error messages

## Installation

```bash
pip install structum_docs
```

Or install as part of the full Structum bundle:

```bash
pip install structum
```

**Note**: This plugin requires MkDocs to be installed. Install with:

```bash
pip install mkdocs mkdocs-material
```

## Usage

### Serve Documentation Locally

Start a local development server that watches for changes and automatically rebuilds:

```bash
# Serve on default address (127.0.0.1:8000)
structum docs serve

# Serve on custom address and port
structum docs serve --dev-addr 0.0.0.0:8080

# Short flag
structum docs serve -a localhost:3000
```

The documentation will be available at the specified address. The server will automatically reload when you make changes to your documentation files.

### Deploy to GitHub Pages

Deploy your documentation to GitHub Pages:

```bash
# Deploy with default commit message
structum docs deploy

# Deploy with custom commit message
structum docs deploy --message "Update docs for v2.0.0"
structum docs deploy -m "Add new plugin documentation"

# Force push to gh-pages (use with caution)
structum docs deploy --force
```

**Requirements for deployment**:
- Git repository must be configured
- You must have write access to the repository
- The `gh-pages` branch should exist (will be created automatically on first deploy)

## Commands Reference

| Command | Description | Options |
|---------|-------------|---------|
| `docs serve` | Serve documentation locally | `--dev-addr, -a`: Server address (default: 127.0.0.1:8000) |
| `docs deploy` | Deploy to GitHub Pages | `--message, -m`: Custom commit message<br>`--force`: Force push |

## MkDocs Integration

This plugin is a wrapper around MkDocs commands, making them more accessible within the Structum ecosystem. It requires:

- **mkdocs**: Static site generator for project documentation
- **mkdocs-material** (optional but recommended): Material theme for MkDocs

Your project should have a `mkdocs.yml` configuration file at the root:

```yaml
site_name: Your Project Name
theme:
  name: material

nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - API Reference: api.md
```

And a `docs/` directory containing your Markdown documentation files.

## Error Handling

The plugin provides helpful error messages:

- **MkDocs not found**: Suggests installing mkdocs
- **Server failed to start**: Shows possible configuration issues
- **Deploy failed**: Indicates permission or git configuration problems

All errors include helpful hints on how to resolve them.

## Development

This plugin uses:
- `subprocess` module to execute mkdocs commands
- `rich` for formatted console output
- `structum-core` for plugin infrastructure

## License

Apache-2.0

## Author

PythonWoods
