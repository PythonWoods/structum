# CLI Reference

Structum v2.0 provides a powerful Command Line Interface built on the plugin architecture.

## Core Commands

Structum core provides only infrastructure commands:

- **version** - Show application version
- **info** - Show application information (version, Python, platform)

All other commands are provided by plugins.

## Official Plugin Commands

Install with `pip install structum[full]` to get all these commands:

### Tree Plugin

- [tree](commands.md#tree) - Visualize directory structures with themes

### Archive Plugin

- [archive](commands.md#archive) - Export code to Markdown

### Clean Plugin

- [clean](commands.md#clean) - Remove `__pycache__` directories

### Docs Plugin

- [docs serve](commands.md#docs) - Serve documentation locally
- [docs deploy](commands.md#docs) - Deploy to GitHub Pages

### Plugins Plugin

- [plugins list](commands.md#plugins) - List installed plugins
- [plugins info](commands.md#plugins) - Show plugin information
- [plugins enable/disable](commands.md#plugins) - Enable or disable plugins
- [plugins new](commands.md#plugins) - Generate plugin skeleton

## Plugin Discovery

All plugins are automatically discovered via Python entry points. No manual registration required!

## Command Help

Get help for any command:

```bash
# Application help
structum --help

# Command help
structum tree --help
structum archive --help

# Subcommand help
structum plugins new --help
```

## Complete Reference

See [commands.md](commands.md) for detailed documentation of all available commands.
