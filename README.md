<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- SPDX-FileCopyrightText: 2025 PythonWoods -->

# Structum

[![CI](https://github.com/pythonwoods/structum/actions/workflows/main_ci.yml/badge.svg)](https://github.com/pythonwoods/structum/actions/workflows/main_ci.yml)
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/pythonwoods/structum)
[![PyPI](https://img.shields.io/pypi/v/structum.svg)](https://pypi.org/project/structum/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![REUSE status](https://api.reuse.software/badge/github.com/pythonwoods/structum)](https://api.reuse.software/info/github.com/pythonwoods/structum)

**Structum** is an enterprise-grade CLI tool designed to visualize, document, and archive directory structures. It bridges the gap between complex file systems and human-readable documentation.

---

## ✨ Key Features

*   **Visual Tree Generation**: Create beautiful, colored directory trees directly in your terminal.
*   **Multiple Themes**: Support for **Nerd Fonts**, Emojis, and plain ASCII (perfect for Markdown/LLM contexts).
*   **Smart Filtering**: Easily exclude `.git`, `__pycache__`, or specific file extensions.
*   **Export Ready**: Generate clean output for documentation or AI context injection.
*   **Extensible Plugin System**: Auto-discovered plugins for custom commands and framework integrations.

---

## 🚀 Quick Start

### Installation

```bash
pip install structum
```

### Usage

Structum provides three main commands:

1.  **`tree`**: Visualize directory structure.
2.  **`archive`**: Export code to Markdown.
3.  **`clean`**: Remove `__pycache__` directories.

#### Visualize Structure
```bash
# Basic usage with stats
structum tree . --stats

# Filter by extension (comma-separated supported)
structum tree . --ext py,md,json --depth 2
```

#### Archive Code
```bash
# Archive multiple file types
structum archive . --output code.md --ext py,js,ts

# Split archive by folder
structum archive src --split-folder --output docs/
```

#### Clean Project
```bash
# Remove __pycache__ (use --skip-venv to exclude virtual environments)
structum clean . --skip-venv
```

#### Manage Plugins
```bash
# List installed plugins (auto-discovered)
structum plugins list

# Generate a new plugin (automatically registered)
structum plugins new my-plugin --category analysis

# Test your plugin
structum my-plugin
```

> **Note**: Built-in plugins are automatically discovered - no manual registration needed!

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