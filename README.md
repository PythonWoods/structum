<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2025 PythonWoods -->

# Structum

[![CI](https://github.com/pythonwoods/structum/actions/workflows/main_ci.yml/badge.svg)](https://github.com/pythonwoods/structum/actions/workflows/main_ci.yml)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/pythonwoods/structum)
[![PyPI](https://img.shields.io/pypi/v/structum.svg)](https://pypi.org/project/structum/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![REUSE status](https://api.reuse.software/badge/github.com/pythonwoods/structum)](https://api.reuse.software/info/github.com/pythonwoods/structum)

**Structum** is an enterprise-grade plugin framework for building extensible CLI applications. It provides a minimal, production-ready core with a powerful plugin system.

> **Version 2.0 Alpha** - Complete architectural redesign. See [CHANGELOG.md](CHANGELOG.md) for details.

---

## ✨ Key Features

*   **Plugin-First Architecture**: Everything is a plugin - no built-in commands beyond core utilities
*   **Entry Point Discovery**: Plugins auto-discovered via Python entry points
*   **Minimal Core**: Lightweight framework with essential infrastructure only
*   **Optional Dependencies**: Install only the plugins you need
*   **Enterprise-Grade**: Production-ready with monitoring, security, and configuration management
*   **Developer-Friendly**: Clear SDK, excellent DX, comprehensive documentation

---

## 🚀 Quick Start

### Installation

**Core Framework Only:**
```bash
pip install structum
```

**With All Official Plugins:**
```bash
pip install structum[full]
```

**Selective Installation:**
```bash
pip install structum[tree,archive]  # Just tree and archive plugins
```

### Available Official Plugins

Install `structum[full]` to get all of these:

1.  **`tree`**: Directory tree visualization
2.  **`archive`**: Export code to Markdown
3.  **`clean`**: Remove `__pycache__` directories
4.  **`docs`**: Documentation management (MkDocs integration)
5.  **`plugins`**: Plugin management utilities

### Usage Examples

#### Visualize Structure (requires `structum_tree`)
```bash
# Basic usage with stats
structum tree . --stats

# Filter by extension
structum tree . --ext py,md,json --depth 2

# Different themes
structum tree . --theme emoji  # or: nerd, ascii, none
```

#### Archive Code (requires `structum_archive`)
```bash
# Archive multiple file types
structum archive . --output code.md --ext py,js,ts

# Split archive by folder
structum archive src --split-folder --output docs/
```

#### Clean Project (requires `structum_clean`)
```bash
# Remove __pycache__ (skip virtual environments)
structum clean . --skip-venv
```

#### Manage Documentation (requires `structum_docs`)
```bash
# Serve docs locally
structum docs serve

# Deploy to GitHub Pages
structum docs deploy
```

#### Manage Plugins (requires `structum_plugins`)
```bash
# List installed plugins
structum plugins list

# Generate a new plugin
structum plugins new my-plugin --category utility

# Get plugin info
structum plugins info tree
```

> **Note**: All plugins are auto-discovered via entry points - no manual registration needed!

---

## 🎨 Themes

Structum supports different visual styles:

| Theme | Description | Best For |
| :--- | :--- | :--- |
| **Emoji** | Uses standard emojis (📂, 🐍). | Default usage, high compatibility. |
| **Nerd** | Uses Nerd Font glyphs (, ). | Power users with patched fonts. |
| **ASCII** | Uses plain text characters. | `tree.txt` files, LLM prompts, Markdown. |

---

## 📚 Documentation

Full documentation is available at:
👉 **[https://pythonwoods.github.io/structum/](https://pythonwoods.github.io/structum/)**

---

## 📜 License

Distributed under the **Apache 2.0** license. See [LICENSE](LICENSE) for details.