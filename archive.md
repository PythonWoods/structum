# Code Archive for `structum`

_Generated on 2025-12-05T12:08:41_

## Project Structure

```text
structum
├── docs
│   ├── architecture
│   │   ├── design-principles.md
│   │   ├── index.md
│   │   └── modules.md
│   ├── cli
│   │   ├── commands.md
│   │   └── index.md
│   ├── development
│   │   ├── conventions.md
│   │   ├── index.md
│   │   ├── plugins.md
│   │   ├── roadmap.md
│   │   └── testing.md
│   ├── overrides
│   │   └── main.html
│   ├── reference
│   │   ├── api.md
│   │   └── index.md
│   ├── stylesheets
│   │   └── extra.css
│   ├── getting-started.md
│   └── index.md
├── LICENSES
│   └── Apache-2.0.txt
├── src
│   └── structum
│       ├── cli
│       │   ├── commands
│       │   │   ├── __init__.py
│       │   │   ├── archive.py
│       │   │   ├── clean.py
│       │   │   ├── docs.py
│       │   │   ├── info.py
│       │   │   ├── plugins.py
│       │   │   └── tree.py
│       │   ├── __init__.py
│       │   └── main.py
│       ├── core
│       │   ├── __init__.py
│       │   ├── archive.py
│       │   ├── clean.py
│       │   ├── config.py
│       │   ├── docs.py
│       │   ├── icons.py
│       │   ├── tree.py
│       │   └── utils.py
│       ├── plugins
│       │   ├── sample
│       │   │   ├── commands
│       │   │   │   ├── __init__.py
│       │   │   │   └── hello.py
│       │   │   ├── core
│       │   │   │   ├── __init__.py
│       │   │   │   └── greeting.py
│       │   │   ├── __init__.py
│       │   │   └── plugin.py
│       │   ├── __init__.py
│       │   ├── loader.py
│       │   ├── registry.py
│       │   ├── sdk.py
│       │   └── skeleton.py
│       ├── __about__.py
│       ├── __init__.py
│       └── __main__.py
├── temp
│   └── BUGS.md
├── tests
│   ├── unit
│   │   ├── cli
│   │   │   ├── commands
│   │   │   │   ├── test_archive_cmd.py
│   │   │   │   ├── test_clean_cmd.py
│   │   │   │   └── test_plugins_cmd.py
│   │   │   └── test_main.py
│   │   ├── core
│   │   │   ├── test_archive.py
│   │   │   ├── test_clean.py
│   │   │   ├── test_config.py
│   │   │   ├── test_docs.py
│   │   │   ├── test_tree.py
│   │   │   └── test_utils.py
│   │   ├── plugins
│   │   │   ├── test_loader.py
│   │   │   ├── test_registry.py
│   │   │   └── test_skeleton.py
│   │   ├── conftest.py
│   │   └── test_version.py
│   └── conftest.py
├── ARCHITECTURE.md
├── archive.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── mkdocs.yml
├── pyproject.toml
├── README.md
└── ROADMAP.md

```

## Table of Contents

- [ARCHITECTURE.md](#ARCHITECTURE-md)
- [.coverage](#-coverage)
- [LICENSE](#LICENSE)
- [pyproject.toml](#pyproject-toml)
- [README.md](#README-md)
- [mkdocs.yml](#mkdocs-yml)
- [CHANGELOG.md](#CHANGELOG-md)
- [.gitignore](#-gitignore)
- [CONTRIBUTING.md](#CONTRIBUTING-md)
- [ROADMAP.md](#ROADMAP-md)
- [temp/BUGS.md](#temp-BUGS-md)
- [docs/getting-started.md](#docs-getting-started-md)
- [docs/index.md](#docs-index-md)
- [docs/overrides/main.html](#docs-overrides-main-html)
- [docs/stylesheets/extra.css](#docs-stylesheets-extra-css)
- [docs/cli/commands.md](#docs-cli-commands-md)
- [docs/cli/index.md](#docs-cli-index-md)
- [docs/reference/api.md](#docs-reference-api-md)
- [docs/reference/index.md](#docs-reference-index-md)
- [docs/development/conventions.md](#docs-development-conventions-md)
- [docs/development/roadmap.md](#docs-development-roadmap-md)
- [docs/development/index.md](#docs-development-index-md)
- [docs/development/testing.md](#docs-development-testing-md)
- [docs/development/plugins.md](#docs-development-plugins-md)
- [docs/architecture/modules.md](#docs-architecture-modules-md)
- [docs/architecture/index.md](#docs-architecture-index-md)
- [docs/architecture/design-principles.md](#docs-architecture-design-principles-md)
- [tests/conftest.py](#tests-conftest-py)
- [tests/unit/test_version.py](#tests-unit-test_version-py)
- [tests/unit/conftest.py](#tests-unit-conftest-py)
- [tests/unit/plugins/test_skeleton.py](#tests-unit-plugins-test_skeleton-py)
- [tests/unit/plugins/test_loader.py](#tests-unit-plugins-test_loader-py)
- [tests/unit/plugins/test_registry.py](#tests-unit-plugins-test_registry-py)
- [tests/unit/cli/test_main.py](#tests-unit-cli-test_main-py)
- [tests/unit/cli/commands/test_clean_cmd.py](#tests-unit-cli-commands-test_clean_cmd-py)
- [tests/unit/cli/commands/test_plugins_cmd.py](#tests-unit-cli-commands-test_plugins_cmd-py)
- [tests/unit/cli/commands/test_archive_cmd.py](#tests-unit-cli-commands-test_archive_cmd-py)
- [tests/unit/core/test_tree.py](#tests-unit-core-test_tree-py)
- [tests/unit/core/test_archive.py](#tests-unit-core-test_archive-py)
- [tests/unit/core/test_config.py](#tests-unit-core-test_config-py)
- [tests/unit/core/test_clean.py](#tests-unit-core-test_clean-py)
- [tests/unit/core/test_utils.py](#tests-unit-core-test_utils-py)
- [tests/unit/core/test_docs.py](#tests-unit-core-test_docs-py)
- [LICENSES/Apache-2.0.txt](#LICENSES-Apache-2-0-txt)
- [.reuse/dep5](#-reuse-dep5)
- [.github/dependabot.yml](#-github-dependabot-yml)
- [.github/labeler.yml](#-github-labeler-yml)
- [.github/workflows/main_ci.yml](#-github-workflows-main_ci-yml)
- [src/structum/__main__.py](#src-structum-__main__-py)
- [src/structum/__about__.py](#src-structum-__about__-py)
- [src/structum/__init__.py](#src-structum-__init__-py)
- [src/structum/plugins/registry.py](#src-structum-plugins-registry-py)
- [src/structum/plugins/skeleton.py](#src-structum-plugins-skeleton-py)
- [src/structum/plugins/loader.py](#src-structum-plugins-loader-py)
- [src/structum/plugins/__init__.py](#src-structum-plugins-__init__-py)
- [src/structum/plugins/sdk.py](#src-structum-plugins-sdk-py)
- [src/structum/plugins/sample/plugin.py](#src-structum-plugins-sample-plugin-py)
- [src/structum/plugins/sample/__init__.py](#src-structum-plugins-sample-__init__-py)
- [src/structum/plugins/sample/commands/__init__.py](#src-structum-plugins-sample-commands-__init__-py)
- [src/structum/plugins/sample/commands/hello.py](#src-structum-plugins-sample-commands-hello-py)
- [src/structum/plugins/sample/core/greeting.py](#src-structum-plugins-sample-core-greeting-py)
- [src/structum/plugins/sample/core/__init__.py](#src-structum-plugins-sample-core-__init__-py)
- [src/structum/cli/main.py](#src-structum-cli-main-py)
- [src/structum/cli/__init__.py](#src-structum-cli-__init__-py)
- [src/structum/cli/commands/archive.py](#src-structum-cli-commands-archive-py)
- [src/structum/cli/commands/info.py](#src-structum-cli-commands-info-py)
- [src/structum/cli/commands/plugins.py](#src-structum-cli-commands-plugins-py)
- [src/structum/cli/commands/tree.py](#src-structum-cli-commands-tree-py)
- [src/structum/cli/commands/docs.py](#src-structum-cli-commands-docs-py)
- [src/structum/cli/commands/clean.py](#src-structum-cli-commands-clean-py)
- [src/structum/cli/commands/__init__.py](#src-structum-cli-commands-__init__-py)
- [src/structum/core/utils.py](#src-structum-core-utils-py)
- [src/structum/core/archive.py](#src-structum-core-archive-py)
- [src/structum/core/tree.py](#src-structum-core-tree-py)
- [src/structum/core/icons.py](#src-structum-core-icons-py)
- [src/structum/core/docs.py](#src-structum-core-docs-py)
- [src/structum/core/clean.py](#src-structum-core-clean-py)
- [src/structum/core/__init__.py](#src-structum-core-__init__-py)
- [src/structum/core/config.py](#src-structum-core-config-py)

---

## `ARCHITECTURE.md` {#ARCHITECTURE-md}

```md
# Structum - Technical Architecture

> **Last Updated:** 2025-12-03
> **Status:** 🔵 In Development
> **Version:** 2.0 Architecture

---

## Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Module Design](#module-design)
4. [Data Flow](#data-flow)
5. [Plugin Architecture](#plugin-architecture)
6. [AI Integration](#ai-integration)
7. [Performance Considerations](#performance-considerations)
8. [Security](#security)
9. [Testing Strategy](#testing-strategy)
10. [Deployment](#deployment)

---

## Overview

Structum è progettato come un **modular documentation engine** con architettura a plugin, ottimizzato per:

- **Scalabilità:** Gestione di codebase da 10 a 100,000+ files
- **Estensibilità:** Plugin system per framework e custom logic
- **Performance:** Processing parallelo, caching, incremental builds
- **AI-Ready:** Output ottimizzato per LLM con token management

### Core Principles

1. **Separation of Concerns** - Ogni modulo ha responsabilità chiare
2. **Plugin-First Architecture** - Extensibility by design
3. **Performance by Default** - Lazy loading, caching, parallelization
4. **Type Safety** - Full type hints (Python 3.11+)
5. **Testability** - 85%+ code coverage target

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLI Layer                             │
│                     (Typer + Rich)                           │
└──────────────────┬──────────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                    Core Engine                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Tree    │  │ Archive  │  │   AI     │  │ Pipeline │   │
│  │ Module   │  │  Module  │  │  Module  │  │  Module  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────┬──────────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                  Plugin System                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ FastAPI  │  │  Pydantic│  │   Typer  │  │SQLAlchemy│   │
│  │  Plugin  │  │  Plugin  │  │  Plugin  │  │  Plugin  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────┬──────────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                  Integrations                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   Git    │  │  GitHub  │  │  GitLab  │  │  Docker  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└──────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

#### 1. CLI Layer
- **Purpose:** User interaction, command parsing, output formatting
- **Components:** Typer commands, Rich console output
- **Dependencies:** typer, rich, click

#### 2. Core Engine
- **Purpose:** Business logic, data processing, orchestration
- **Components:** Tree, Archive, AI, Pipeline modules
- **Dependencies:** pathlib, typing, dataclasses

#### 3. Plugin System
- **Purpose:** Extensibility, framework integrations
- **Components:** Plugin loader, registry, SDK
- **Dependencies:** pluggy, importlib-metadata

#### 4. Integrations
- **Purpose:** External system connectivity
- **Components:** Git, GitHub Actions, GitLab CI, Docker
- **Dependencies:** GitPython, requests, PyYAML

---

## Module Design

### Core Modules Structure

```
src/structum/
├── __init__.py
├── __about__.py
├── cli.py                          # CLI entry point
├── core/
│   ├── __init__.py
│   ├── tree.py                     # Tree visualization
│   ├── archive.py                  # Code archiving
│   ├── clean.py                    # Cleanup utilities
│   ├── config.py                   # Configuration management
│   ├── ai/                         # AI Module (Phase 1)
│   │   ├── __init__.py
│   │   ├── chunker.py              # Smart chunking engine
│   │   ├── formatters.py           # LLM format adapters
│   │   ├── optimizer.py            # Token optimization
│   │   ├── metadata.py             # Metadata extraction
│   │   └── rag.py                  # RAG integration
│   ├── pipeline/                   # Pipeline Module (Phase 2)
│   │   ├── __init__.py
│   │   ├── compiler.py             # Documentation compiler
│   │   ├── watcher.py              # File system watcher
│   │   ├── versioning.py           # Version management
│   │   └── incremental.py          # Incremental builds
│   └── reports/                    # Reports Module (Phase 4)
│       ├── __init__.py
│       ├── pdf.py                  # PDF generation
│       ├── latex.py                # LaTeX export
│       ├── dashboard.py            # Interactive dashboard
│       ├── exporter.py             # Multi-format export
│       └── templates/              # Report templates
│           ├── corporate/
│           ├── minimal/
│           ├── audit/
│           └── latex/              # LaTeX templates
│               ├── academic/       # IEEE, ACM styles
│               ├── thesis/         # University thesis
│               ├── book/           # Technical book
│               └── report/         # Technical report
├── integrations/                   # Integrations (Phase 2)
│   ├── __init__.py
│   ├── git.py                      # Git integration
│   ├── github.py                   # GitHub Actions
│   ├── gitlab.py                   # GitLab CI
│   └── frameworks/                 # Framework plugins (Phase 3)
│       ├── __init__.py
│       ├── fastapi.py              # FastAPI integration
│       ├── typer_cli.py            # Typer/Click integration
│       ├── pydantic.py             # Pydantic integration
│       └── sqlalchemy.py           # SQLAlchemy integration
├── plugins/                        # Plugin System
│   ├── __init__.py
│   ├── loader.py                   # Plugin loader
│   ├── registry.py                 # Plugin registry
│   ├── sdk.py                      # Plugin SDK
│   └── sample_plugin.py            # Example plugin
└── utils/                          # Utilities
    ├── __init__.py
    ├── fs.py                       # Filesystem utilities
    ├── text.py                     # Text processing
    └── cache.py                    # Caching system
```

---

## Data Flow

### 1. Tree Visualization Flow

```
User Command
    │
    ▼
┌─────────────────┐
│  CLI Parser     │
│  (cli.py)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tree Module    │
│  (tree.py)      │
└────────┬────────┘
         │
         ├──► Filesystem Walker
         │      │
         │      ▼
         │   Filter Files
         │      │
         │      ▼
         │   Build Tree
         │      │
         │      ▼
         └──► Rich Renderer
                │
                ▼
          Console Output
```

### 2. Archive Generation Flow

```
User Command
    │
    ▼
┌─────────────────┐
│  CLI Parser     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Archive Module  │
└────────┬────────┘
         │
         ├──► Collect Files
         │      │
         │      ▼
         │   Filter & Sort
         │      │
         │      ▼
         │   Load Plugins
         │      │
         │      ▼
         │   Process Each File
         │      │
         │      ├──► Tree Generation
         │      ├──► TOC Generation
         │      └──► Code Formatting
         │            │
         │            ▼
         └──► Write Output
                │
                ▼
          Markdown File(s)
```

### 3. AI Bundle Flow (Phase 1)

```
User Command
    │
    ▼
┌─────────────────┐
│  CLI Parser     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Module      │
└────────┬────────┘
         │
         ├──► Load Files
         │      │
         │      ▼
         │   Extract Metadata
         │      │
         │      ▼
         │   Smart Chunker
         │      │
         │      ├──► Calculate Tokens
         │      ├──► Prioritize Content
         │      └──► Split by Strategy
         │            │
         │            ▼
         │   Format Adapter
         │      │
         │      ├──► OpenAI Formatter
         │      ├──► Claude Formatter
         │      └──► Gemini Formatter
         │            │
         │            ▼
         └──► Export Bundle
                │
                ▼
          AI-Ready Output
```

---

## Plugin Architecture

### Plugin System Design

```python
# Plugin Interface (sdk.py)
from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path

class PluginBase(ABC):
    """Base class for all Structum plugins."""

    name: str
    version: str
    description: str
    author: str

    @abstractmethod
    def setup(self, config: dict[str, Any]) -> None:
        """Initialize plugin with configuration."""
        pass

    @abstractmethod
    def process_file(self, file_path: Path) -> dict[str, Any]:
        """Process a single file and return metadata."""
        pass

    @abstractmethod
    def generate_output(self, data: dict[str, Any]) -> str:
        """Generate plugin-specific output."""
        pass

    def teardown(self) -> None:
        """Cleanup resources."""
        pass
```

### Plugin Lifecycle

```
┌─────────────────┐
│  Discovery      │  Plugin discovery via entry points
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Registration   │  Register in plugin registry
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Validation     │  Check compatibility, dependencies
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Setup          │  Initialize with config
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Execution      │  Process files, generate output
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Teardown       │  Cleanup resources
└─────────────────┘
```

### Plugin Registry

```python
# registry.py
from typing import Type
from structum.plugins.sdk import PluginBase

class PluginRegistry:
    """Central registry for all plugins."""

    _plugins: dict[str, Type[PluginBase]] = {}

    @classmethod
    def register(cls, plugin: Type[PluginBase]) -> None:
        """Register a plugin."""
        cls._plugins[plugin.name] = plugin

    @classmethod
    def get(cls, name: str) -> Type[PluginBase] | None:
        """Get plugin by name."""
        return cls._plugins.get(name)

    @classmethod
    def list_all(cls) -> list[str]:
        """List all registered plugins."""
        return list(cls._plugins.keys())
```

### Example Plugin

```python
# frameworks/fastapi.py
from structum.plugins.sdk import PluginBase
from pathlib import Path
import ast

class FastAPIPlugin(PluginBase):
    """FastAPI endpoint documentation plugin."""

    name = "fastapi-autodoc"
    version = "1.0.0"
    description = "Auto-document FastAPI routes and endpoints"
    author = "PythonWoods"

    def setup(self, config: dict) -> None:
        self.include_internal = config.get("include_internal", False)

    def process_file(self, file_path: Path) -> dict:
        """Extract FastAPI route information."""
        with open(file_path) as f:
            tree = ast.parse(f.read())

        routes = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if self._is_route_decorator(decorator):
                        routes.append({
                            "name": node.name,
                            "method": self._get_http_method(decorator),
                            "path": self._get_route_path(decorator),
                            "docstring": ast.get_docstring(node)
                        })

        return {"routes": routes}

    def generate_output(self, data: dict) -> str:
        """Generate FastAPI documentation."""
        output = ["## FastAPI Endpoints\n"]
        for route in data["routes"]:
            output.append(f"### {route['method']} {route['path']}")
            output.append(f"**Function:** `{route['name']}`")
            if route["docstring"]:
                output.append(f"\n{route['docstring']}\n")
        return "\n".join(output)
```

---

## AI Integration

### Smart Chunking Strategy

```python
# ai/chunker.py
from dataclasses import dataclass
from enum import Enum

class ChunkStrategy(Enum):
    TOKEN_BASED = "token"
    MODULE_BASED = "module"
    DEPENDENCY_BASED = "dependency"
    SEMANTIC_BASED = "semantic"

@dataclass
class Chunk:
    """Represents a code chunk for AI consumption."""
    id: str
    content: str
    tokens: int
    metadata: dict
    priority: int  # 1-10, higher = more important

class SmartChunker:
    """Intelligent code chunking for LLM consumption."""

    def __init__(self, strategy: ChunkStrategy, max_tokens: int):
        self.strategy = strategy
        self.max_tokens = max_tokens

    def chunk(self, files: list[Path]) -> list[Chunk]:
        """Split files into optimal chunks."""
        if self.strategy == ChunkStrategy.TOKEN_BASED:
            return self._chunk_by_tokens(files)
        elif self.strategy == ChunkStrategy.MODULE_BASED:
            return self._chunk_by_module(files)
        # ... other strategies

    def _chunk_by_tokens(self, files: list[Path]) -> list[Chunk]:
        """Chunk based on token limits."""
        chunks = []
        current_chunk = []
        current_tokens = 0

        for file_path in files:
            content = file_path.read_text()
            tokens = self._count_tokens(content)

            if current_tokens + tokens > self.max_tokens:
                # Save current chunk
                chunks.append(self._create_chunk(current_chunk))
                current_chunk = [file_path]
                current_tokens = tokens
            else:
                current_chunk.append(file_path)
                current_tokens += tokens

        if current_chunk:
            chunks.append(self._create_chunk(current_chunk))

        return chunks
```

### Format Adapters

```python
# ai/formatters.py
from abc import ABC, abstractmethod

class Formatter(ABC):
    """Base class for LLM format adapters."""

    token_limit: int
    format_style: str

    @abstractmethod
    def format_chunk(self, chunk: Chunk) -> str:
        """Format chunk for specific LLM."""
        pass

class OpenAIFormatter(Formatter):
    """Optimized for GPT-3.5/GPT-4."""

    token_limit = 128000  # GPT-4 Turbo
    format_style = "conversational"

    def format_chunk(self, chunk: Chunk) -> str:
        """Format for OpenAI models."""
        return f"""
# File: {chunk.metadata['file_path']}

## Purpose
{chunk.metadata.get('purpose', 'Not specified')}

## Dependencies
{', '.join(chunk.metadata.get('dependencies', []))}

## Code
```python
{chunk.content}
```

## Context
- Lines: {chunk.metadata['line_range']}
- Complexity: {chunk.metadata['complexity']}
- Last Modified: {chunk.metadata['git_info']['last_modified']}
"""

class ClaudeFormatter(Formatter):
    """Optimized for Claude 3."""

    token_limit = 200000  # Claude 3 Opus
    format_style = "structured"

    def format_chunk(self, chunk: Chunk) -> str:
        """Format for Claude models."""
        return f"""
<file path="{chunk.metadata['file_path']}">
  <metadata>
    <purpose>{chunk.metadata.get('purpose', 'Not specified')}</purpose>
    <dependencies>{', '.join(chunk.metadata.get('dependencies', []))}</dependencies>
    <complexity>{chunk.metadata['complexity']}</complexity>
  </metadata>
  <content>
{chunk.content}
  </content>
</file>
"""
```

---

## Performance Considerations

### Optimization Strategies

#### 1. Lazy Loading
```python
class LazyFileLoader:
    """Load files only when needed."""

    def __init__(self, file_paths: list[Path]):
        self._paths = file_paths
        self._cache: dict[Path, str] = {}

    def get(self, path: Path) -> str:
        if path not in self._cache:
            self._cache[path] = path.read_text()
        return self._cache[path]
```

#### 2. Parallel Processing
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class ParallelProcessor:
    """Process files in parallel."""

    def process_files(
        self,
        files: list[Path],
        processor: Callable,
        max_workers: int = 4
    ) -> list[Any]:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            return list(executor.map(processor, files))
```

#### 3. Caching System
```python
# utils/cache.py
import hashlib
import pickle
from pathlib import Path

class CacheManager:
    """File-based caching system."""

    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(exist_ok=True)

    def get(self, key: str) -> Any | None:
        cache_file = self._get_cache_file(key)
        if cache_file.exists():
            return pickle.loads(cache_file.read_bytes())
        return None

    def set(self, key: str, value: Any) -> None:
        cache_file = self._get_cache_file(key)
        cache_file.write_bytes(pickle.dumps(value))

    def _get_cache_file(self, key: str) -> Path:
        hash_key = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{hash_key}.cache"
```

### Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Files/second (tree) | 1000+ | 800 |
| Files/second (archive) | 500+ | 300 |
| Memory usage (1K files) | < 100MB | 150MB |
| Startup time | < 500ms | 300ms |
| Plugin load time | < 100ms | 50ms |

---

## Security

### Security Considerations

#### 1. Plugin Sandboxing
```python
# plugins/sandbox.py
import subprocess
import sys

class PluginSandbox:
    """Execute plugins in isolated environment."""

    def run_plugin(
        self,
        plugin_path: Path,
        timeout: int = 30
    ) -> dict:
        """Run plugin with resource limits."""
        result = subprocess.run(
            [sys.executable, str(plugin_path)],
            timeout=timeout,
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
```

#### 2. Input Validation
- Path traversal prevention
- File size limits
- Extension whitelist
- Content sanitization

#### 3. Secrets Detection
```python
# utils/secrets.py
import re

SECRET_PATTERNS = [
    r'api[_-]?key["\s:=]+["\']?([a-zA-Z0-9_-]+)',
    r'password["\s:=]+["\']?([a-zA-Z0-9_!@#$%^&*()-=+]+)',
    r'token["\s:=]+["\']?([a-zA-Z0-9_-]+)',
]

def detect_secrets(content: str) -> list[dict]:
    """Detect potential secrets in content."""
    secrets = []
    for pattern in SECRET_PATTERNS:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            secrets.append({
                "type": match.group(0).split("=")[0].strip(),
                "line": content[:match.start()].count("\n") + 1
            })
    return secrets
```

---

## Testing Strategy

### Test Pyramid

```
     ┌─────────────┐
     │   E2E Tests │  (5%)
     └─────────────┘
    ┌───────────────┐
    │Integration Tests│  (15%)
    └───────────────┘
   ┌─────────────────┐
   │   Unit Tests    │  (80%)
   └─────────────────┘
```

### Test Structure

```
tests/
├── unit/                   # Unit tests (80%)
│   ├── test_tree.py
│   ├── test_archive.py
│   ├── test_ai/
│   │   ├── test_chunker.py
│   │   └── test_formatters.py
│   └── test_plugins/
├── integration/            # Integration tests (15%)
│   ├── test_cli.py
│   ├── test_pipeline.py
│   └── test_git_integration.py
├── e2e/                    # End-to-end tests (5%)
│   ├── test_full_workflow.py
│   └── test_ci_cd.py
└── fixtures/               # Test data
    ├── sample_project/
    └── expected_outputs/
```

### Coverage Target

- **Overall:** 85%+
- **Core modules:** 90%+
- **Plugins:** 70%+
- **Integrations:** 80%+

---

## Deployment

### Distribution Strategy

#### 1. PyPI Package
```bash
# Build
python -m build

# Upload
twine upload dist/*
```

#### 2. Docker Image
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["structum"]
```

#### 3. GitHub Action
```yaml
# action.yml
name: 'Structum Documentation'
description: 'Generate documentation with Structum'
inputs:
  quality:
    description: 'Documentation quality level'
    default: 'standard'
runs:
  using: 'docker'
  image: 'docker://pythonwoods/structum:latest'
```

### Release Process

1. **Version bump** (semantic versioning)
2. **Update CHANGELOG.md**
3. **Run full test suite**
4. **Build packages**
5. **Upload to PyPI**
6. **Create GitHub release**
7. **Build and push Docker image**
8. **Update documentation**

---

## Configuration Management

### Configuration File

```yaml
# .structum.yml
version: "2.0"

# General settings
project_name: "My Project"
output_dir: "./docs/generated"

# Tree settings
tree:
  theme: "nerd"
  max_depth: 5
  show_hidden: false
  ignore_dirs:
    - ".git"
    - "node_modules"
    - "__pycache__"

# Archive settings
archive:
  toc: true
  tree: true
  extensions:
    - ".py"
    - ".md"
  split_by_type: false

# AI settings
ai:
  default_format: "openai"
  max_tokens: 8000
  chunking_strategy: "token"
  include_metadata: true

# Plugin settings
plugins:
  enabled:
    - "fastapi-autodoc"
    - "pydantic-schema"
  disabled:
    - "sample-plugin"

# Pipeline settings
pipeline:
  watch: true
  auto_rebuild: true
  incremental: true
  git_integration: true

# Report settings
reports:
  default_theme: "corporate"
  include_statistics: true
  pdf_quality: "high"
```

---

## Future Considerations

### Planned Enhancements

1. **GraphQL Support** - Query-based documentation access
2. **WebAssembly** - Browser-based processing
3. **Machine Learning** - Intelligent categorization
4. **Real-time Collaboration** - Multi-user editing
5. **Cloud Integration** - AWS/GCP/Azure deployment

### Scalability Roadmap

- **1K files:** Current architecture ✅
- **10K files:** Parallel processing, caching
- **100K files:** Distributed processing, database indexing
- **1M files:** Microservices architecture, streaming

---

**Document Version:** 1.0
**Maintained by:** PythonWoods Team
**Review Date:** 2025-03-01

```

## `.coverage` {#-coverage}

```text
SQLite format 3   @     	   
                                                            	 .zq
V � ^
O-�
&�m	��a	c�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         �Q�}tabletracertracer
CREATE TABLE tracer (
    -- A row per file indicating the tracer used for that file.
    file_id integer primary key,
    tracer text,
    foreign key (file_id) references file (id)
)�
�etablearcarcCREATE TABLE arc (
    -- If recording branches, a row per context per from/to line transition executed.
    file_id integer,            -- foreign key to `file`.
    context_id integer,         -- foreign key to `context`.
    fromno integer,             -- line number jumped from.
    tono integer,               -- line number jumped to.
    foreign key (file_id) references file (id),
    foreign key (context_id) references context (id),
    unique (file_id, context_id, fromno, tono)
)%9 indexsqlite_autoindex_arc_1arc��qtableline_bitsline_bits	CREATE TABLE line_bits (
    -- If recording lines, a row per context per file executed.
    -- All of the line numbers for that file/context are in one numbits.
    file_id integer,            -- foreign key to `file`.
    context_id integer,         -- foreign key to `context`.
    numbits blob,               -- see the numbits functions in coverage.numbits
    foreign key (file_id) references file (id),
    foreign key (context_id) references context (id),
    unique (file_id, context_id)
)1	E indexsqlite_autoindex_line_bits_1line_bits
��	tablecontextcontextCREATE TABLE context (
    -- A row per context measured.
    id integer primary key,
    context text,
    unique (context)
)-A indexsqlite_autoindex_context_1context��qtablefilefileCREATE TABLE file (
    -- A row per file measured.
    id integer primary key,
    path text,
    unique (path)
)'; indexsqlite_autoindex_file_1file�[�tablemetametaCREATE TABLE meta (
    -- Key-value pairs, to record metadata about the data
    key text,
    value text,
    unique (key)
    -- Possible keys:
    --  'has_arcs' boolean      -- Is this data recording branches?
    --  'sys_argv' text         -- The coverage command line that recorded the data.
    --  'version' text          -- The version of coverage.py that made the file.
    --  'when' text             -- Datetime when the file was created.
)'; indexsqlite_autoindex_meta_1meta       �++�utablecoverage_schemacoverage_schemaCREATE TABLE coverage_schema (
    -- One row, to record the version of the schema in this db.
    version integer
)
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    has_arcs0version7.12.0
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            has_arcs
	version
   , �}8��\
�
�
L
	�{1��Y
�
�
A	�	�	]	�`�m,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ? �/home/pythinwoods/develop/structum/src/structum/__main__.pyG �/home/pythinwoods/develop/structum/src/structum/plugins/skeleton.pyS �+/home/pythinwoods/develop/structum/src/structum/plugins/sample/core/greeting.pyS �+/home/pythinwoods/develop/structum/src/structum/plugins/sample/core/__init__.pyT �-/home/pythinwoods/develop/structum/src/structum/plugins/sample/commands/hello.pyW �3/home/pythinwoods/develop/structum/src/structum/plugins/sample/commands/__init__.pyL �/home/pythinwoods/develop/structum/src/structum/plugins/sample/plugin.pyN �!/home/pythinwoods/develop/structum/src/structum/plugins/sample/__init__.pyH �/home/pythinwoods/develop/structum/src/structum/cli/commands/info.pyH �/home/pythinwoods/develop/structum/src/structum/cli/commands/tree.pyB �	/home/pythinwoods/develop/structum/src/structum/plugins/sdk.pyG �/home/pythinwoods/develop/structum/src/structum/plugins/registry.pyB �	/home/pythinwoods/develop/structum/src/structum/core/config.pyE �/home/pythinwoods/develop/structum/src/structum/plugins/loader.pyG �/home/pythinwoods/develop/structum/src/structum/plugins/__init__.pyK �/home/pythinwoods/develop/structum/src/structum/cli/commands/plugins.py@ �/home/pythinwoods/develop/structum/src/structum/core/docs.pyH �/home/pythinwoods/develop/structum/src/structum/cli/commands/docs.pyI
 �/home/pythinwoods/develop/structum/src/structum/cli/commands/clean.pyA �/home/pythinwoods/develop/structum/src/structum/core/clean.pyA �/home/pythinwoods/develop/structum/src/structum/core/utils.pyA
 �/home/pythinwoods/develop/structum/src/structum/core/icons.py@	 �/home/pythinwoods/develop/structum/src/structum/core/tree.pyC �/home/pythinwoods/develop/structum/src/structum/core/archive.pyD �
/home/pythinwoods/develop/structum/src/structum/core/__init__.pyK �/home/pythinwoods/develop/structum/src/structum/cli/commands/archive.pyL �/home/pythinwoods/develop/structum/src/structum/cli/commands/__init__.py? �/home/pythinwoods/develop/structum/src/structum/cli/main.pyC �/home/pythinwoods/develop/structum/src/structum/cli/__init__.py@ �/home/pythinwoods/develop/structum/src/structum/__about__.py? �/home/pythinwoods/develop/structum/src/structum/__init__.py
   - ~�-9�]|2	��	��
��
��
M
�
Z
�	^�a�	
Bn                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       @�/home/pythinwoods/develop/structum/src/structum/__main__.pyH�/home/pythinwoods/develop/structum/src/structum/plugins/skeleton.pyT�+/home/pythinwoods/develop/structum/src/structum/plugins/sample/core/greeting.pyT�+/home/pythinwoods/develop/structum/src/structum/plugins/sample/core/__init__.pyU�-/home/pythinwoods/develop/structum/src/structum/plugins/sample/commands/hello.pyX�3/home/pythinwoods/develop/structum/src/structum/plugins/sample/commands/__init__.pyM�/home/pythinwoods/develop/structum/src/structum/plugins/sample/plugin.pyO�!/home/pythinwoods/develop/structum/src/structum/plugins/sample/__init__.pyI�/home/pythinwoods/develop/structum/src/structum/cli/commands/info.pyI�/home/pythinwoods/develop/structum/src/structum/cli/commands/tree.pyC�	/home/pythinwoods/develop/structum/src/structum/plugins/sdk.pyH�/home/pythinwoods/develop/structum/src/structum/plugins/registry.pyC�	/home/pythinwoods/develop/structum/src/structum/core/config.pyF�/home/pythinwoods/develop/structum/src/structum/plugins/loader.pyH�/home/pythinwoods/develop/structum/src/structum/plugins/__init__.pyL�/home/pythinwoods/develop/structum/src/structum/cli/commands/plugins.pyA�/home/pythinwoods/develop/structum/src/structum/core/docs.pyI�/home/pythinwoods/develop/structum/src/structum/cli/commands/docs.pyJ�/home/pythinwoods/develop/structum/src/structum/cli/commands/clean.py
B�/home/pythinwoods/develop/structum/src/structum/core/clean.pyB�/home/pythinwoods/develop/structum/src/structum/core/utils.pyB�/home/pythinwoods/develop/structum/src/structum/core/icons.py
A�/home/pythinwoods/develop/structum/src/structum/core/tree.py	D�/home/pythinwoods/develop/structum/src/structum/core/archive.pyE�
/home/pythinwoods/develop/structum/src/structum/core/__init__.pyL�/home/pythinwoods/develop/structum/src/structum/cli/commands/archive.pyM�/home/pythinwoods/develop/structum/src/structum/cli/commands/__init__.py@�/home/pythinwoods/develop/structum/src/structum/cli/main.pyD�/home/pythinwoods/develop/structum/src/structum/cli/__init__.pyA�/home/pythinwoods/develop/structum/src/structum/__about__.py?�	/home/pythinwoods/develop/structum/src/structum/__init__.py
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
   � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
	
   ! ���������wj`6%�����~umd\TI8!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             	,P  @ �  s��	 Ћ�j  			Pe_	P		P5		P	(�l�Š�7�e�	�JINh}��	
	  @  �_.	^	 �s�    p�d�ޮsS���ڒ�� �����?w�  ��,	0
  �������#�  �%	���=	�M	>�8�=	 \I ���
(
	R�Z> ���� �>@o�ڧ������� `�m	 �	��
	$+? ���{�}/		2P�Y��?Y�Yc�𧻓�S �	��	�/ ��	
��	*�l˿�}�� ��					
   0 ����������}�����vo�h7��a>ZSLE0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            															
				
			
					
							
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
```

## `LICENSE` {#LICENSE}

```text

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## `pyproject.toml` {#pyproject-toml}

```toml
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

[build-system]
requires = ["hatchling>=1.25"]
build-backend = "hatchling.build"

[project]
name = "structum"
dynamic = ["version"]
description = "Enterprise Code Structure & Documentation Engine."
readme = "README.md"
license = { text = "Apache-2.0" }
authors = [{ name = "PythonWoods", email = "info@pythonwoods.com" }]
requires-python = ">=3.11"
keywords = [
  "cli",
  "tree",
  "structure",
  "documentation",
  "markdown",
  "visualization",
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "License :: OSI Approved :: Apache Software License",
  "Operating System :: OS Independent",
  "Topic :: Software Development :: Documentation",
  "Topic :: Utilities",
]

dependencies = ["typer>=0.12", "rich>=13.0"]

[project.scripts]
structum = "structum.cli:app"

[project.entry-points."structum.plugins"]
# Future plugins will be registered here
# example = "structum.plugins.example:register"

[tool.hatch.build.targets.wheel]
packages = ["src/structum"]

#[tool.hatch.build]
# sources = ["src"]

[tool.hatch.version]
path = "src/structum/__about__.py"

[tool.hatch.build.targets.sdist]
include = ["src/**", "README.md", "LICENSE"]

# -----------------------------------------
# Dev Environments
# -----------------------------------------

[project.optional-dependencies]
dev = [
  "pytest>=8",
  "pytest-cov>=4",
  "mypy>=1.11",
  "ruff>=0.5",
  "types-setuptools",
]
docs = ["mkdocs>=1.5", "mkdocs-material>=9.5", "mkdocstrings[python]>=0.24"]

# -----------------------------------------
# Ruff configuration
# -----------------------------------------
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B"]
ignore = ["E501", "B008"]

[tool.ruff.lint.isort]
known-first-party = ["structum"]
section-order = [
  "future",
  "standard-library",
  "third-party",
  "first-party",
  "local-folder",
]

# -----------------------------------------
# mypy configuration
# -----------------------------------------
[tool.mypy]
python_version = "3.11"
strict = true
ignore_missing_imports = true
check_untyped_defs = true

# -----------------------------------------
# pytest
# -----------------------------------------
[tool.pytest.ini_options]
minversion = "8.0"
python_files = "test_*.py"
testpaths = ["tests"]
addopts = "--cov=structum --cov-report=term-missing"

```

## `README.md` {#README-md}

```md
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
# List installed plugins
structum plugins list

# Generate a new plugin
structum plugins new my-plugin --category analysis
```

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
```

## `mkdocs.yml` {#mkdocs-yml}

```yml
site_name: Structum
site_description: Enterprise Code Structure & Documentation Engine
site_url: https://pythonwoods.github.io/structum/
repo_url: https://github.com/pythonwoods/structum
repo_name: pythonwoods/structum

# Copyright
copyright: Copyright &copy; 2025 PythonWoods

# Theme Configuration
theme:
  name: material
  custom_dir: docs/overrides
  language: it
  logo: assets/logo.svg
  favicon: assets/favicon.png

  # Color Palette
  palette:
    # Light Mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: teal
      accent: purple
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode

    # Dark Mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: lime
      toggle:
        icon: material/weather-night
        name: Switch to light mode

  # Theme Features
  features:
    - navigation.instant        # Instant loading
    - navigation.instant.progress  # Progress indicator
    - navigation.tracking       # URL updates with scroll
    - navigation.tabs           # Top-level navigation tabs
    - navigation.tabs.sticky    # Sticky navigation tabs
    - navigation.sections       # Section index pages
    - navigation.expand         # Expand all sections by default
    - navigation.path           # Breadcrumbs
    - navigation.top            # Back to top button
    - navigation.footer         # Footer navigation
    - toc.follow                # TOC follows scroll
    - toc.integrate             # TOC integrated in nav
    - search.suggest            # Search suggestions
    - search.highlight          # Highlight search terms
    - search.share              # Share search results
    - content.code.copy         # Copy code button
    - content.code.annotate     # Code annotations
    - content.tooltips          # Improved tooltips
    - content.tabs.link         # Link content tabs

  # Icon Configuration
  icon:
    repo: fontawesome/brands/github
    logo: material/code-braces
    admonition:
      note: octicons/tag-16
      abstract: octicons/checklist-16
      info: octicons/info-16
      tip: octicons/light-bulb-16
      success: octicons/check-16
      question: octicons/question-16
      warning: octicons/alert-16
      failure: octicons/x-circle-16
      danger: octicons/zap-16
      bug: octicons/bug-16
      example: octicons/beaker-16
      quote: octicons/quote-16

# Custom CSS and JavaScript
extra_css:
  - stylesheets/extra.css

extra_javascript:
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

# Extra Configuration
extra:
  version: "1.0.0"
  generator: false  # Hide "Made with Material for MkDocs"

  # Social Links
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/pythonwoods/structum
      name: Structum on GitHub
    - icon: fontawesome/brands/python
      link: https://pypi.org/project/structum/
      name: Structum on PyPI
    - icon: fontawesome/solid/paper-plane
      link: mailto:info@pythonwoods.com
      name: Contact Us

  # Analytics (optional - uncomment and configure)
  # analytics:
  #   provider: google
  #   property: G-XXXXXXXXXX

# Plugins
plugins:
  - search:
      lang: it
      separator: '[\s\-,:!=\[\]()"/]+|(?!\b)(?=[A-Z][a-z])|\.(?!\d)|&[lg]t;'

  - mkdocstrings:
      handlers:
        python:
          paths: [src]
          options:
            docstring_style: google
            show_root_heading: true
            show_root_full_path: false
            show_source: true
            show_bases: true
            show_submodules: true
            members_order: source
            heading_level: 2
            show_signature_annotations: true
            separate_signature: true
            line_length: 80

  # Optional: git-revision-date-localized for last update dates
  # - git-revision-date-localized:
  #     enable_creation_date: true
  #     type: timeago

# Markdown Extensions
markdown_extensions:
  # Python Markdown
  - abbr                        # Abbreviations
  - admonition                  # Admonitions (notes, warnings, etc.)
  - attr_list                   # Add HTML attributes to elements
  - def_list                    # Definition lists
  - footnotes                   # Footnotes
  - md_in_html                  # Markdown in HTML
  - meta                        # Meta-data
  - tables                      # Tables
  - toc:
      permalink: true
      permalink_title: Anchor link to this section
      toc_depth: 3

  # PyMdown Extensions
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret               # Superscript and insert
  - pymdownx.mark                # Highlighting
  - pymdownx.tilde               # Subscript and delete
  - pymdownx.critic              # Critic markup
  - pymdownx.details             # Collapsible admonitions
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
      auto_title: true
  - pymdownx.inlinehilite       # Inline code highlighting
  - pymdownx.keys                # Keyboard keys
  - pymdownx.magiclink:          # Auto-link URLs
      normalize_issue_symbols: true
      repo_url_shorthand: true
      user: pythonwoods
      repo: structum
  - pymdownx.smartsymbols        # Smart symbols
  - pymdownx.snippets            # Include external files
  - pymdownx.superfences:        # Code blocks with syntax highlighting
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:             # Content tabs
      alternate_style: true
      combine_header_slug: true
  - pymdownx.tasklist:           # Task lists
      custom_checkbox: true
      clickable_checkbox: false

# Navigation Structure
nav:
  - Home: index.md
  - Getting Started: getting-started.md
  - CLI Reference:
      - Overview: cli/index.md
      - Commands: cli/commands.md
  - Architecture:
      - Overview: architecture/index.md
      - Modules: architecture/modules.md
      - Design Principles: architecture/design-principles.md
  - Development:
      - Overview: development/index.md
      - Conventions: development/conventions.md
      - Plugins: development/plugins.md
      - Testing: development/testing.md
      - Roadmap: development/roadmap.md
  - Reference:
      - Overview: reference/index.md
      - API: reference/api.md

# Validation and Strict Mode
validation:
  nav:
    omitted_files: warn
    not_found: warn
    absolute_links: warn
  links:
    not_found: warn
    absolute_links: warn
    unrecognized_links: warn

# Watch additional files for changes during development
watch:
  - src/structum
  - docs/overrides
  - docs/stylesheets

```

## `CHANGELOG.md` {#CHANGELOG-md}

```md
# Changelog

All notable changes to this project will be documented in this file.

This project follows **Conventional Commits**  
and automatic release generation via **release-please**.

---

## [Unreleased]

### ✨ Features

#### Core Commands
- **Code Archiving** (`structum archive`): Export source code to Markdown files
  - Single file or split by folder output
  - Filter by file extension
- **Clean Command** (`structum clean`): Remove `__pycache__` directories recursively
- **Entry Point**: Run via `python -m structum`

#### Plugin System
- **Plugin SDK**: `PluginBase` abstract class for standardized plugin development
- **Plugin Registry**: Centralized plugin management with validation
- **Plugin CLI**: Full management commands
  - `structum plugins list` - List plugins with category/status
  - `structum plugins info <name>` - Show plugin details
  - `structum plugins enable/disable <name>` - Manage plugin state
  - `structum plugins new <name>` - Generate skeleton with smart defaults
- **Plugin Categories**: `analysis`, `export`, `formatting`, `utility`
- **Plugin Validation**: Auto-validates `name`, `version`, `category` on load
- **Configuration Persistence**: State stored in `~/.config/structum/config.json`

#### Documentation
- **MkDocs Integration**: Professional documentation site with Material theme
- **Docs Commands**: `structum docs serve` and `structum docs deploy`

#### Planned (Phase 4)
- **LaTeX Export**: Academic document generation (IEEE, ACM styles)

### 🔨 Refactoring
- Modular CLI architecture (`cli/commands/` structure)
- Separated core business logic from CLI interface
- Plugin `__init__.py` now only exports, logic in `plugin.py`
- Modern type hints (Python 3.11+ PEP 585/604)
- Migrated CLI from Click to Typer

### 📚 Documentation
- Comprehensive technical architecture (`ARCHITECTURE.md`)
- Development roadmap (`ROADMAP.md`)
- Plugin development guide (`docs/development/plugins.md`)
- CLI commands reference (`docs/cli/commands.md`)
- Context-aware help messages in `plugins new`

### 🔧 Chores
- Dynamic versioning with hatchling
- Dependabot configuration for pip and GitHub Actions
- REUSE/SPDX compliance

---

```

## `.gitignore` {#-gitignore}

```text
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

# ─────────────────────────────────────────────
#  Python Core & Bytecode
# ─────────────────────────────────────────────
__pycache__/
*.py[cod]
*$py.class

# ─────────────────────────────────────────────
#  Virtual Environments
# ─────────────────────────────────────────────
.venv/
venv/
env/
.env/
ENV/
env.bak/
venv.bak/

# ─────────────────────────────────────────────
#  Distribution & Packaging
# ─────────────────────────────────────────────
build/
dist/
*.egg-info/
*.egg
.eggs/
pip-wheel-metadata/
MANIFEST

# ─────────────────────────────────────────────
#  Dependency Managers & Tooling (Hatch, uv, Poetry)
# ─────────────────────────────────────────────
.hatch/
.uv/
.uv_cache/
.python_modules/
poetry.lock
# Nota: poetry.lock va committato per le app, ma a volte escluso per le lib.
# Se usi uv/hatch, poetry.lock non serve.

# ─────────────────────────────────────────────
#  Testing & Coverage
# ─────────────────────────────────────────────
.tox/
.nox/
.pytest_cache/
.coverage
.coverage.*
coverage.xml
nosetests.xml
htmlcov/
report.xml
*.cover
*.py,cover
.hypothesis/

# ─────────────────────────────────────────────
#  Static Analysis & Linters (MyPy, Ruff, Pyright)
# ─────────────────────────────────────────────
.mypy_cache/
.ruff_cache/
.pytype/
.pyright/
.dmypy.json
dmypy.json

# ─────────────────────────────────────────────
#  Documentation (MkDocs, Sphinx)
# ─────────────────────────────────────────────
site/
docs/_build/
docs/site/

# ─────────────────────────────────────────────
#  IDE & Editors
# ─────────────────────────────────────────────
# VS Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
*.code-workspace

# JetBrains / IntelliJ
.idea/
*.iml
out/

# Sublime Text
*.sublime-workspace
*.sublime-project

# ─────────────────────────────────────────────
#  OS & Filesystem
# ─────────────────────────────────────────────
.DS_Store
.DS_Store?
._*
.Trashes
ehthumbs.db
Thumbs.db

# ─────────────────────────────────────────────
#  Logs & Databases
# ─────────────────────────────────────────────
*.log
logs/
*.sqlite
*.db

# ─────────────────────────────────────────────
#  Jupyter Notebooks
# ─────────────────────────────────────────────
.ipynb_checkpoints/
profile_default/
ipython_config.py

# ─────────────────────────────────────────────
#  Temporary & Caches
# ─────────────────────────────────────────────
tmp/
temp/
.cache/
.reuse/cache/
```

## `CONTRIBUTING.md` {#CONTRIBUTING-md}

```md
# Contributing to Structum

Thank you for your interest in contributing to Structum! We welcome contributions from the community to help make this project better.

## Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/pythonwoods/structum.git
    cd structum
    ```

2.  **Set up the environment**:
    We recommend using a virtual environment.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    pip install -e ".[dev,docs]"
    ```

## Project Structure

The project follows a modular architecture:

*   `src/structum/cli/`: CLI interface and commands.
    *   `commands/`: Individual command modules (e.g., `tree.py`, `archive.py`).
    *   `main.py`: Main Typer application entry point.
*   `src/structum/core/`: Business logic (e.g., `tree.py`, `archive.py`).
*   `src/structum/plugins/`: Plugin system and built-in plugins.

## Code Quality Standards

We enforce high code quality standards using the following tools:

*   **Ruff**: For linting and formatting.
    ```bash
    ruff check src/structum
    ruff format src/structum
    ```
*   **MyPy**: For static type checking (strict mode).
    ```bash
    mypy src/structum
    ```

Please ensure all checks pass before submitting a Pull Request.

## Adding a New Command

1.  **Core Logic**: Implement the business logic in `src/structum/core/`.
2.  **CLI Interface**: Create a new module in `src/structum/cli/commands/`.
3.  **Registration**: Register the command in `src/structum/cli/main.py`.

## Adding a Plugin

### Quick Start

Generate a plugin skeleton from the project root:

```bash
structum plugins new my-plugin --category utility
```

This creates `src/structum/plugins/my_plugin/` with the complete structure.

### Register Your Plugin

Edit `src/structum/plugins/loader.py`:

```python
from . import sample, my_plugin  # Add your import

PluginRegistry.register(my_plugin.MyPlugin)  # Add registration
```

### Plugin Categories

Choose the appropriate category for your plugin:
- `analysis` – Code analysis and metrics
- `export` – Export and format conversion
- `formatting` – Code formatting and style
- `utility` – Utility and helper tools

### Full Documentation

See `docs/development/plugins.md` for:
- Complete plugin structure reference
- External plugin development (for PyPI)
- Best practices and examples

## Documentation

Documentation is built with MkDocs.
```bash
structum docs serve
```

```

## `ROADMAP.md` {#ROADMAP-md}

```md
# Structum Roadmap - Documentation Engine

> **Vision:** Trasformare Structum nel leading Documentation Engine per sviluppatori, team enterprise e AI/LLM workflows.
> **Version:** 2.0 (Updated 2025-12-04)

---

## Executive Summary

Structum evolverà da un tool di visualizzazione del codice a una **piattaforma completa di documentazione**, con capacità di:

- **AI-ready output** ottimizzato per ChatGPT, Claude, Gemini
- **Multi-language support** (Python, JavaScript, TypeScript, Go, Rust, Java)
- **Pipeline automation** per CI/CD enterprise
- **Report generation** professionale (PDF, Dashboard, LaTeX)
- **Plugin ecosystem** estensibile per framework popolari
- **Git integration** per documentazione evolutiva
- **Collaboration features** per team distributed
- **Quality assurance** per documentation excellence

---

## Target Audience

1. **Developers individuali** - Quick documentation, AI assistant integration
2. **Team aziendali** - Code review, onboarding, audit compliance, collaboration
3. **AI/LLM users** - Context injection, RAG workflows, semantic search
4. **Enterprise** - Compliance, security audit, documentation standards, multi-language support
5. **Academic** - Research documentation, thesis, technical papers
6. **Open Source** - Community documentation, contributor onboarding

---

## Strategic Phases

### 🚀 Phase 1: AI-Ready Output (PRIORITY 1)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Differenziatore chiave nel mercato
**Status:** 📋 Planned

#### Obiettivi
- Output ottimizzato per LLM (token limits, chunking intelligente)
- Format-specific adapters (OpenAI, Claude, Gemini, DeepSeek)
- RAG-ready structured output
- Metadata injection per context enhancement

#### Deliverables

##### 1.1 AI Bundle Command
```bash
structum ai-bundle --format=openai --max-tokens=8000
structum ai-bundle --format=claude --split-by-module
structum ai-bundle --format=gemini --context=refactoring
structum ai-bundle --format=generic --output=./ai-context/
```

**Features:**
- Chunking intelligente (rispetta token limits)
- Prioritizzazione file (core > tests > docs)
- Metadata injection (dependencies, purpose, git info)
- Format-specific optimization
- Multiple output formats (Markdown, JSON, XML)

##### 1.2 Chunking Engine
**File:** `src/structum/core/ai/chunker.py`

**Strategies:**
- Token-based (rispetta limits GPT-4, Claude, etc.)
- Module-based (mantiene coesione logica)
- Dependency-based (include imports necessari)
- Semantic-based (raggruppa funzionalità correlate)

##### 1.3 Format Adapters
**File:** `src/structum/core/ai/formatters.py`

- OpenAI Formatter (GPT-4 Turbo, 128K tokens)
- Claude Formatter (Claude 3 Opus, 200K tokens)
- Gemini Formatter (Gemini 1.5 Pro, 1M tokens)
- DeepSeek Formatter

##### 1.4 RAG Integration
**File:** `src/structum/core/ai/rag.py`

- Vector embeddings ready
- Chunk metadata per retrieval
- Semantic search preparation
- Context window optimization

#### Success Metrics
- ✅ Output < token limits per ogni formato
- ✅ Context retention > 95%
- ✅ 3+ format adapters implementati
- ✅ Documentazione completa per AI workflows

---

### 📚 Phase 2: Documentation Pipeline (PRIORITY 2)
**Timeline:** 3-4 settimane
**Impact:** HIGH - Enterprise adoption driver
**Status:** 📋 Planned

#### Obiettivi
- Automazione completa documentazione
- Git integration (blame, changelog, diff)
- Auto-update su commit
- Versioning e snapshot

#### Deliverables

##### 2.1 Documentation Compiler
```bash
structum docs compile --quality=enterprise
structum docs compile --format=mkdocs --output=./docs/generated/
structum docs compile --incremental  # Solo file modificati
```

**Features:**
- Auto-detection progetto (Python, JS, Go, Rust)
- Template-based generation
- Multi-format output (Markdown, HTML, PDF)
- Incremental builds (solo delta)

##### 2.2 Git Integration
**File:** `src/structum/integrations/git.py`

**Features:**
- Blame → documentation attribution
- Changelog automation
- Diff visualization
- Commit history per file
- Evolution tracking

##### 2.3 Auto-Update Pipeline
```bash
structum docs watch --auto-rebuild
structum docs watch --git-hook  # Installa git hook
```

**Features:**
- File watcher con debouncing
- Git hooks (pre-commit, post-commit)
- CI/CD integration
- Webhook support

##### 2.4 Versioning System
**File:** `src/structum/core/pipeline/versioning.py`

- Snapshot management
- Version comparison
- Rollback support
- Archive old versions

##### 2.5 Change Detection & Diff Visualization ⭐ NEW
```bash
structum diff v1.0.0..HEAD --output=changes.md
structum changelog auto-generate --conventional-commits
structum diff visualize --interactive --output=diff.html
```

**Features:**
- Visual diff per codice
- API breaking changes detection
- Deprecation warnings
- Migration guides auto-generation
- Semantic versioning suggestions
- Release notes automation

#### Success Metrics
- ✅ Auto-update < 5 secondi
- ✅ Git integration completa
- ✅ CI/CD templates per GitHub/GitLab
- ✅ Versioning system funzionante
- ✅ Automated diff detection

---

### 🔌 Phase 3: Plugin Ecosystem (PRIORITY 3)
**Timeline:** 4-6 settimane
**Impact:** MEDIUM-HIGH - Estensibilità e adoption
**Status:** 🔄 In Progress (SDK exists)

#### Obiettivi
- Plugin system robusto
- Framework integrations (FastAPI, Pydantic, SQLAlchemy, Typer)
- Community plugins support
- Plugin marketplace concept

#### Deliverables

##### 3.1 Enhanced Plugin System
```bash
structum plugins list
structum plugins search fastapi
structum plugins add fastapi-autodoc
structum plugins remove django-mapper
structum plugins update --all
```

**Features:**
- Plugin discovery
- Dependency management
- Version compatibility
- Enable/disable plugins
- Plugin configuration

##### 3.2 Framework Plugins

**FastAPI Plugin**
- Auto-detect routes
- Extract endpoint metadata
- Generate OpenAPI supplement
- Document dependencies

**Typer/Click Plugin**
- CLI command documentation
- Argument/option extraction
- Help text generation
- Command tree visualization

**Pydantic Plugin**
- Schema extraction
- Validation rules documentation
- Field descriptions
- JSON Schema export

**SQLAlchemy Plugin**
- Model relationship mapping
- ER diagram generation
- Migration history
- Schema visualization

##### 3.3 Plugin Marketplace & Templates ⭐ NEW
```bash
structum templates list --category=fintech
structum templates install corporate-standard
structum templates publish my-template --public
```

**Features:**
- Template marketplace (como npm)
- Industry-specific templates (fintech, healthcare, etc)
- Company branding templates
- Community ratings & reviews
- Security scanning
- Version management

##### 3.4 Plugin Development Kit
**File:** `src/structum/plugins/sdk.py`

**Documentation:**
- Plugin development guide
- API reference
- Example plugins
- Testing framework

#### Success Metrics
- ✅ 4+ official plugins rilasciati
- ✅ Plugin SDK completo
- ✅ Community plugin support
- ✅ Plugin documentation
- ✅ Plugin marketplace operational

---

### 📊 Phase 4: Report Generation (PRIORITY 3)
**Timeline:** 3-4 settimane
**Impact:** MEDIUM - Visual appeal e enterprise adoption
**Status:** 📋 Planned

#### Obiettivi
- PDF export professionale
- Dashboard interattive
- Custom themes e branding
- Multiple output formats

#### Deliverables

##### 4.1 PDF Report Generator
```bash
structum report full --pdf --theme=corporate --output=report.pdf
structum report summary --pdf --theme=minimal
structum report audit --pdf --compliance=iso27001
```

**Features:**
- Corporate themes (branding)
- Tree visualization
- Code statistics
- Git history
- Compliance sections
- Custom logo/footer

**Tech Stack:**
- WeasyPrint o ReportLab
- Jinja2 templates
- CSS styling
- SVG tree rendering

##### 4.2 Interactive Dashboard (Static HTML)
```bash
structum report dashboard --interactive --output=./dashboard/
structum report dashboard --serve --port=8080
```

**Features:**
- File explorer interattivo
- Code statistics charts
- Dependency graphs
- Timeline evolution
- Search functionality (client-side con Lunr.js)

**Tech Stack:**
- Static HTML/CSS/vanilla JS (NO React/Vue framework overhead)
- Chart.js per grafici
- D3.js per visualizzazioni
- Lunr.js per ricerca client-side
- Responsive design

##### 4.3 Custom Templates
```bash
structum report template list
structum report template create my-template
structum report full --template=my-template
```

**Features:**
- Template engine (Jinja2)
- Custom sections
- Conditional rendering
- Variable injection
- Partial includes

##### 4.4 LaTeX Export
```bash
structum report latex --output=documentation.tex
structum report latex --template=academic --with-toc
structum report latex --compile-pdf  # Auto-compile to PDF
```

**Features:**
- Professional LaTeX document generation
- Academic paper templates (IEEE, ACM, Springer)
- Thesis/dissertation templates
- Technical book format
- Code listings with syntax highlighting (listings/minted)
- Mathematical notation support
- Bibliography integration (BibTeX)
- Cross-referencing (labels, refs)
- Table of contents, list of figures
- Overleaf-compatible output
- Auto-compile to PDF (requires pdflatex/xelatex)

**Templates Included:**
- `academic` - IEEE/ACM style
- `thesis` - University thesis format
- `book` - Technical book layout
- `report` - Formal technical report
- `minimal` - Basic LaTeX article

##### 4.5 Multi-Format Export
- **PDF** - Audit, compliance, presentation
- **HTML** - Interactive, dashboard
- **LaTeX** - Academic papers, theses, technical books
- **JSON** - API, integration
- **XML** - Enterprise systems
- **Markdown** - Documentation
- **DOCX** - Word documents

#### Success Metrics
- ✅ PDF generation funzionante
- ✅ Dashboard interattiva
- ✅ 3+ themes disponibili
- ✅ Multiple export formats
- ✅ LaTeX templates operational

---

### 🏗️ Phase 5: CI/CD Integration (PRIORITY 2)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Enterprise adoption
**Status:** 📋 Planned

#### Obiettivi
- GitHub Actions templates
- GitLab CI templates
- Jenkins integration
- Pre-commit hooks
- Docker containerization

#### Deliverables

##### 5.1 GitHub Actions Workflow
```yaml
# .github/workflows/docs.yml
name: Documentation Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pythonwoods/structum-action@v1
        with:
          quality: enterprise
          format: mkdocs
          ai-bundle: true
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
```

##### 5.2 GitLab CI Template
```yaml
# .gitlab-ci.yml
include:
  - remote: 'https://raw.githubusercontent.com/pythonwoods/structum/main/ci/gitlab-ci.yml'

structum:docs:
  extends: .structum-base
  variables:
    QUALITY: enterprise
    FORMAT: mkdocs
```

##### 5.3 Pre-commit Hooks
```bash
structum hooks install
structum hooks config --auto-update
```

**Hooks:**
- `pre-commit` - Validate structure
- `post-commit` - Update docs
- `pre-push` - Generate report

##### 5.4 CI/CD Examples Repository
```
examples/ci-cd/
├── github-actions/
│   ├── basic.yml
│   ├── enterprise.yml
│   └── multi-format.yml
├── gitlab-ci/
│   ├── basic.yml
│   └── enterprise.yml
├── jenkins/
│   └── Jenkinsfile
└── docker/
    └── Dockerfile.docs
```

#### Success Metrics
- ✅ GitHub Action pubblicata
- ✅ GitLab CI template
- ✅ Examples completi
- ✅ Documentation per CI/CD
- ✅ Docker image pubblicata

---

### 🐳 Phase 5.5: Docker & Static Dashboard ⚡ QUICK WIN
**Timeline:** 1-2 settimane
**Impact:** HIGH - Zero-dependency deployment, enterprise ready
**Status:** 📋 Planned
**Priority:** IMMEDIATE (Quick Win)

#### Obiettivi
- Docker containerization completa
- Static dashboard HTML prototipo
- Zero dependency hell
- One-command deployment

#### Deliverables

##### 5.5.1 Docker Container
```dockerfile
# Dockerfile multi-stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -e .[full]

FROM python:3.11-slim
COPY --from=builder /app /app
WORKDIR /app
ENTRYPOINT ["structum"]
CMD ["--help"]
```

**Features:**
- Multi-stage build (size optimization)
- Alpine variant per lightweight deployments
- Docker Compose per development
- GitHub Container Registry
- Docker Hub publishing
- Healthcheck support

**Usage:**
```bash
docker run pythonwoods/structum:latest tree /project
docker-compose up docs-server
```

##### 5.5.2 Docker Compose Stack
```yaml
# docker-compose.yml
version: '3.8'
services:
  structum:
    image: pythonwoods/structum:latest
    volumes:
      - ./project:/workspace
    command: archive /workspace --output=/workspace/docs

  dashboard:
    image: pythonwoods/structum:latest
    command: serve-dashboard --port=8080
    ports:
      - "8080:8080"
    volumes:
      - ./dashboard:/dashboard
```

##### 5.5.3 Static Dashboard HTML
```bash
structum dashboard generate --output=./dashboard/
structum dashboard serve --port=8080 --watch
```

**Tech Stack:**
- Pure HTML5/CSS3
- Vanilla JavaScript (ES6+)
- Chart.js for metrics
- Lunr.js for search
- Zero build step
- Zero npm dependencies

**Dashboard Features:**
- File tree explorer
- Code statistics
- Search functionality
- Responsive design
- Dark/Light theme
- Offline-capable

#### Success Metrics
- ✅ Docker image < 200MB
- ✅ Build time < 2 minuti
- ✅ Dashboard loads < 1 secondo
- ✅ Works offline
- ✅ Published to Docker Hub

---

### 🌐 Phase 6: Multi-Language & IDE Integration (PRIORITY 1)
**Timeline:** 3-4 mesi
**Impact:** VERY HIGH - 10x market expansion
**Status:** 📋 Planned

#### Obiettivi
- Support multi-language codebases
- IDE extensions per developer experience
- Framework detection automatica
- Cross-language documentation

#### Deliverables

##### 6.1 Multi-Language Support
```bash
structum tree . --lang javascript
structum archive . --lang typescript --output ts-docs/
structum archive . --lang go,rust --multi-lang
structum archive . --auto-detect  # Smart language detection
```

**Linguaggi Supportati:**

1. **JavaScript/TypeScript** (Phase 6.1)
   - Node.js, React, Vue, Angular
   - JSDoc/TSDoc parsing
   - Package.json analysis
   - npm/yarn dependency mapping

2. **Go** (Phase 6.2)
   - Module structure
   - Godoc comments
   - go.mod dependency analysis
   - Interface documentation

3. **Rust** (Phase 6.3)
   - Cargo.toml analysis
   - Rustdoc comments
   - Trait documentation
   - Macro expansion

4. **Java/Kotlin** (Phase 6.4)
   - Maven/Gradle projects
   - JavaDoc/KDoc
   - Spring Framework detection
   - Annotation processing

5. **C#/.NET** (Phase 6.5)
   - .csproj analysis
   - XML documentation
   - NuGet dependencies
   - .NET Core/Framework detection

6. **PHP** (Phase 6.6)
   - Composer projects
   - PHPDoc
   - Laravel/Symfony detection
   - Namespace analysis

**Tech Stack:**
- Tree-sitter per multi-language parsing
- Language-specific AST analyzers
- Universal documentation format
- Cross-language reference linking

##### 6.2 IDE Extensions

**VS Code Extension** (`structum-vscode`)
```bash
# Features:
- Tree preview in sidebar
- Documentation hover tooltips
- Generate docs on save
- Plugin marketplace integration
- Live preview
- Keyboard shortcuts (Ctrl+Shift+D)
```

**JetBrains Plugin** (IntelliJ, PyCharm, WebStorm, GoLand, Rider)
```bash
# Features:
- Tool window integration
- Context menu actions
- Run configurations
- Code insights
- Refactoring integration
```

**Vim/Neovim Plugin** (`structum.nvim`)
```lua
-- :Structum tree
-- :Structum archive
-- :Structum ai-bundle
```

**Emacs Package** (`structum-mode`)
```elisp
;; M-x structum-tree
;; M-x structum-archive
```

##### 6.3 Framework Detection
```bash
structum detect  # Auto-detect all frameworks
```

**Detected Frameworks:**
- Python: Django, Flask, FastAPI, Pydantic
- JavaScript: React, Vue, Angular, Express, Next.js
- Go: Gin, Echo, Fiber
- Rust: Actix, Rocket, Axum
- Java: Spring Boot, Micronaut, Quarkus

#### Success Metrics
- ✅ 6+ languages supported
- ✅ 4+ IDE extensions pubblicati
- ✅ Framework detection > 90% accuracy
- ✅ Cross-language reference linking
- ✅ 10x market size increase

---

### 🎯 Phase 7: Quality Assurance & Testing (PRIORITY 2)
**Timeline:** 2-3 mesi
**Impact:** HIGH - Enterprise documentation quality
**Status:** 📋 Planned

#### Obiettivi
- Documentation quality metrics
- Automated testing for docs
- Linting e validation
- Code metrics integration

#### Deliverables

##### 7.1 Documentation Quality Assurance
```bash
structum lint docs/ --check-completeness --check-style
structum quality-report --output quality.html
structum validate --standard=enterprise
```

**Quality Metrics:**
- **Completeness Score**: % moduli documentati
- **Readability Score**: Flesch-Kincaid, Gunning Fog
- **Link Validation**: Broken links, missing references
- **Code Examples**: Syntax check, runnable
- **Consistency Check**: Naming conventions, formatting
- **Terminology Validation**: Glossario aziendale
- **Accessibility Check**: WCAG compliance per HTML output

**Output Dashboard:**
```
Documentation Quality Report
────────────────────────────────────
✅ Coverage:        87% (target: 90%)
⚠️  Readability:    Grade 10 (target: 8)
❌ Broken Links:    12 found
✅ Code Examples:   100% valid
⚠️  Terminology:    5 inconsistencies
Overall Score:      78/100 (Good)
```

##### 7.2 Documentation-as-Code Testing
```bash
structum test docs/ --extract-examples
structum test docs/ --validate-links --check-syntax
structum test docs/ --ci-mode  # Exit code per CI/CD
```

**Features:**
- Code block extraction
- Auto-execution degli esempi
- Snapshot testing
- Link validation (HTTP 200 check)
- Image validation
- Version compatibility testing

##### 7.3 Code Metrics & Technical Debt
```bash
structum metrics analyze --output=metrics.json
structum debt-tracker init --threshold=high
structum complexity-report --format=html
```

**Metrics Tracked:**
- Cyclomatic Complexity
- Code Churn (file change frequency)
- Test Coverage integration
- Technical Debt Score (SQALE)
- Security Vulnerabilities (Bandit, Safety)
- Performance Hotspots
- Maintainability Index

**Output:**
```
Code Health Dashboard
─────────────────────────────────
High Complexity:       23 functions
Technical Debt:        47 hours estimated
Security Issues:       3 medium, 1 low
Test Coverage:         73%
Hotspot Files:         5 identified
Action Required:       12 refactorings
```

##### 7.4 Accessibility (a11y) Support
```bash
structum a11y check --standard=wcag2.1-aa
structum a11y fix --auto
```

**Features:**
- Screen reader optimization
- Keyboard navigation
- Alt text generation per immagini
- Color contrast validation
- ARIA labels automation
- Multi-language support (i18n)

#### Success Metrics
- ✅ Quality score > 85/100
- ✅ Zero broken links in docs
- ✅ 100% runnable code examples
- ✅ WCAG AA compliance
- ✅ Automated testing in CI/CD

---

### 👥 Phase 8: Collaboration & Enterprise (PRIORITY 2)
**Timeline:** 3-4 mesi
**Impact:** HIGH - Team productivity, enterprise sales
**Status:** 📋 Planned

#### Obiettivi
- Real-time collaboration features
- Cloud integrations
- Compliance & audit reports
- Team workflow automation

#### Deliverables

##### 8.1 Cloud Integrations
```bash
structum export confluence --space=DOCS --page=root
structum export notion --database=docs-db
structum export sharepoint --site=company-docs
structum sync google-drive --folder=Documentation
```

**Integrations:**
- **Confluence** - Auto-sync documentation
- **Notion** - Database exports
- **SharePoint** - Enterprise document management
- **Google Drive/Workspace** - Team sharing
- **Slack/Teams** - Notification webhooks

##### 8.2 Compliance & Audit Reports
```bash
structum audit compliance --standard=iso27001
structum audit compliance --standard=soc2
structum audit compliance --standard=hipaa
structum audit report --format=pdf --output=audit.pdf
```

**Standards Supported:**
- **ISO 27001** - Information security
- **SOC 2** - Service organization controls
- **HIPAA** - Healthcare data protection
- **GDPR** - Data privacy
- **PCI DSS** - Payment card industry

**Report Sections:**
- Code inventory
- Access control documentation
- Change management logs
- Security vulnerability tracking
- Compliance gap analysis

##### 8.3 Team Collaboration Features
```bash
structum team init --workspace=myteam
structum team invite user@company.com --role=editor
structum team review create --pr=123
structum team analytics --period=monthly
```

**Features:**
- Workspace management
- Role-based access control (RBAC)
- Documentation review workflow
- Comment threads on docs
- Change approval process
- Team activity dashboard

##### 8.4 Documentation Analytics
```bash
structum analytics report --period=monthly
structum analytics export --format=json
```

**Metrics Tracked:**
- Documentation coverage trends
- Update frequency
- Most/least documented modules
- Stale documentation detection
- Contributor statistics
- Quality score evolution

#### Success Metrics
- ✅ 3+ cloud integrations
- ✅ 5+ compliance standards supported
- ✅ Team collaboration features
- ✅ Analytics dashboard
- ✅ 10+ enterprise customers

---

### 🤖 Phase 9: AI-Powered Intelligence (PRIORITY 3)
**Timeline:** 4-5 mesi
**Impact:** MEDIUM - Future-proofing, innovation
**Status:** 📋 Planned

#### Obiettivi
- Semantic search e knowledge graph
- AI-powered documentation suggestions
- Auto-improvement system
- Multi-language translation (i18n)

#### Deliverables

##### 9.1 Semantic Search & Knowledge Graph
```bash
structum search semantic "authentication flow"
structum search similar --file=auth.py
structum graph knowledge --output=graph.json
structum graph visualize --interactive
```

**Features:**
- Vector-based semantic search
- Code similarity detection
- Knowledge graph construction
- Relationship mapping (imports, inheritance, calls)
- Interactive graph visualization (D3.js)
- Context-aware search results

**Tech Stack:**
- Sentence transformers for embeddings
- ChromaDB/FAISS for vector storage
- NetworkX for graph analysis
- D3.js for visualization

##### 9.2 AI-Powered Suggestions
```bash
structum ai suggest-docs --file=utils.py
structum ai auto-docstring --experimental
structum ai improve-quality --target-score=90
```

**Features:**
- Missing documentation detection
- Auto-generated docstrings (GPT-4)
- Documentation quality improvement suggestions
- Consistency recommendations
- Best practice hints

##### 9.3 Auto-Improvement System
```bash
structum ai learn --from-feedback
structum ai optimize --based-on=usage-patterns
```

**Features:**
- Learning from user edits
- Template optimization
- Format preference learning
- Continuous improvement loop

##### 9.4 Multi-Language Translation (i18n)
```bash
structum translate docs/ --to=es,fr,de,ja
structum translate auto-detect --sync
```

**Features:**
- AI translation (GPT-4, DeepL)
- Multi-language documentation sync
- Glossary consistency
- Cultural adaptation
- 20+ languages supported

##### 9.5 Voice-to-Documentation (Experimental)
```bash
structum voice record --output=docs/module.md
structum voice transcribe audio.mp3 --enhance
```

**Features:**
- Voice recording for documentation
- Speech-to-text with code understanding
- Meeting transcription → docs
- Whiteboard OCR → technical docs

#### Success Metrics
- ✅ Semantic search accuracy > 85%
- ✅ AI suggestions acceptance rate > 60%
- ✅ 20+ languages supported
- ✅ Knowledge graph visualization
- ✅ Voice input functional (experimental)

---

### 🚀 Phase 10: Ecosystem Expansion (PRIORITY LOW)
**Timeline:** Ongoing
**Impact:** MEDIUM - Long-term growth
**Status:** 📋 Planned

#### Obiettivi
- Performance profiling integration
- API contract testing
- Documentation gamification
- Additional tool integrations

#### Deliverables

##### 10.1 Performance Profiling Integration
```bash
structum profile integrate --tool=pyinstrument
structum profile report --output=performance.html
```

**Features:**
- Integration with profilers (cProfile, py-spy, pyinstrument)
- Performance hotspot documentation
- Optimization suggestions
- Benchmark tracking

##### 10.2 API Contract Testing
```bash
structum api-contracts extract --from=openapi.yaml
structum api-contracts test --against=implementation
structum api-contracts diff v1.0..v2.0
```

**Features:**
- OpenAPI/Swagger integration
- Contract vs. implementation validation
- Breaking change detection
- API versioning documentation

##### 10.3 Documentation Gamification
```bash
structum gamify init --team=engineering
structum gamify leaderboard
structum gamify badges award --user=john --badge=docs-master
```

**Features:**
- Points for documentation contributions
- Badges and achievements
- Team leaderboards
- Streak tracking
- Challenges and quests

##### 10.4 Additional Integrations

**Obsidian Plugin**
- Vault integration
- Bidirectional linking
- Graph view sync

**Raycast Extension**
- Quick docs generation
- Search integration
- Command palette

**Alfred Workflow**
- macOS productivity
- Quick search
- Clipboard integration

##### 10.5 Distribution Channels
```bash
# Package managers
brew install structum           # Homebrew (macOS/Linux)
choco install structum          # Chocolatey (Windows)
snap install structum           # Snap (Linux)
winget install pythonwoods.structum  # Windows Package Manager
```

#### Success Metrics
- ✅ 5+ additional integrations
- ✅ Gamification adoption > 30%
- ✅ 4+ package managers
- ✅ Performance profiling functional

---

## Technical Architecture

### Core Modules

```
structum/
├── core/
│   ├── archive.py          # Existing
│   ├── tree.py             # Existing
│   ├── clean.py            # Existing
│   ├── ai/                 # NEW - Phase 1
│   │   ├── __init__.py
│   │   ├── chunker.py      # Smart chunking engine
│   │   ├── formatters.py   # LLM format adapters
│   │   ├── optimizer.py    # Token optimization
│   │   └── rag.py          # RAG integration
│   ├── pipeline/           # NEW - Phase 2
│   │   ├── __init__.py
│   │   ├── compiler.py     # Documentation compiler
│   │   ├── watcher.py      # File watcher
│   │   └── versioning.py   # Version management
│   ├── reports/            # NEW - Phase 4
│   │   ├── __init__.py
│   │   ├── pdf.py          # PDF generation
│   │   ├── dashboard.py    # Interactive dashboard
│   │   └── templates/      # Report templates
│   │       ├── corporate/
│   │       ├── minimal/
│   │       └── audit/
│   ├── quality/            # NEW - Phase 7
│   │   ├── __init__.py
│   │   ├── metrics.py      # Quality metrics
│   │   ├── linter.py       # Documentation linting
│   │   └── validator.py    # Link & syntax validation
│   └── intelligence/       # NEW - Phase 9
│       ├── __init__.py
│       ├── search.py       # Semantic search
│       ├── suggestions.py  # AI suggestions
│       └── knowledge_graph.py
├── integrations/           # NEW - Phase 2, 8
│   ├── __init__.py
│   ├── git.py              # Git integration
│   ├── cloud/              # Cloud integrations
│   │   ├── confluence.py
│   │   ├── notion.py
│   │   └── sharepoint.py
│   └── frameworks/         # Framework plugins
│       ├── __init__.py
│       ├── fastapi.py
│       ├── typer_cli.py
│       ├── pydantic.py
│       └── sqlalchemy.py
├── languages/              # NEW - Phase 6
│   ├── __init__.py
│   ├── javascript.py
│   ├── typescript.py
│   ├── go.py
│   ├── rust.py
│   ├── java.py
│   └── csharp.py
├── plugins/                # Existing - Enhanced in Phase 3
│   ├── __init__.py
│   ├── loader.py
│   ├── sdk.py              # Plugin development kit
│   └── registry.py         # Plugin registry
└── cli.py                  # Enhanced with new commands
```

### CLI Commands Evolution

```bash
# Existing
structum tree
structum archive
structum clean
structum docs-serve
structum docs-deploy

# Phase 1 - AI
structum ai-bundle --format=openai
structum ai-optimize --for=claude

# Phase 2 - Pipeline
structum docs compile --quality=enterprise
structum docs watch --auto-rebuild
structum git-integration enable
structum diff v1.0.0..HEAD
structum changelog auto-generate

# Phase 3 - Plugins
structum plugins list
structum plugins add fastapi-autodoc
structum plugins config
structum templates install corporate-standard

# Phase 4 - Reports
structum report full --pdf
structum report dashboard --interactive
structum report latex --template=academic

# Phase 5 - CI/CD
structum hooks install
structum ci-template generate --platform=github

# Phase 5.5 - Docker & Dashboard
structum dashboard generate
structum dashboard serve --port=8080

# Phase 6 - Multi-Language
structum tree . --lang javascript
structum archive . --auto-detect

# Phase 7 - Quality
structum lint docs/
structum quality-report
structum test docs/ --extract-examples
structum metrics analyze

# Phase 8 - Collaboration
structum export confluence
structum audit compliance --standard=iso27001
structum team init

# Phase 9 - AI Intelligence
structum search semantic "authentication"
structum ai suggest-docs
structum translate docs/ --to=es,fr
```

---

## Dependencies & Tech Stack

### Core Dependencies
- **Existing:** typer, rich, pathlib
- **Phase 1:** tiktoken (token counting), anthropic-sdk, openai
- **Phase 2:** watchdog (file watching), GitPython
- **Phase 3:** importlib-metadata, pluggy
- **Phase 4:** WeasyPrint/ReportLab, Jinja2, markdown2
- **Phase 5:** PyYAML, docker-py
- **Phase 6:** tree-sitter, language parsers
- **Phase 7:** pylint, flake8, bandit, radon
- **Phase 9:** sentence-transformers, chromadb, networkx

### Optional Dependencies
```toml
[project.optional-dependencies]
ai = ["tiktoken", "anthropic", "openai", "sentence-transformers"]
pipeline = ["watchdog", "GitPython"]
reports = ["weasyprint", "jinja2", "markdown2", "python-docx"]
plugins = ["pluggy", "importlib-metadata"]
languages = ["tree-sitter", "tree-sitter-javascript", "tree-sitter-python"]
quality = ["pylint", "flake8", "bandit", "radon"]
intelligence = ["chromadb", "faiss-cpu", "networkx"]
full = ["structum[ai,pipeline,reports,plugins,languages,quality,intelligence]"]
```

---

## Success Metrics

### Adoption Metrics
- **Downloads/month:** 10K+ (6 mesi)
- **GitHub stars:** 1K+ (12 mesi)
- **Contributors:** 20+ (12 mesi)
- **Enterprise users:** 50+ (12 mesi)

### Technical Metrics
- **Test coverage:** > 85%
- **Performance:** < 5s per 1000 files
- **Documentation:** 100% API documented
- **Plugin ecosystem:** 10+ plugins (12 mesi)

### Business Metrics
- **Community engagement:** 100+ GitHub discussions
- **Blog posts/tutorials:** 20+ articles
- **Conference talks:** 3+ presentations
- **Case studies:** 5+ enterprise adopters

---

## Risk Management

### Technical Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Token limit complessità | HIGH | Multiple format adapters, fallback strategies |
| Performance con large codebase | MEDIUM | Incremental processing, caching, parallel processing |
| Plugin security | HIGH | Sandbox execution, security audit, whitelist |
| Git integration edge cases | MEDIUM | Extensive testing, fallback to basic mode |
| Multi-language parsing complexity | HIGH | Tree-sitter abstraction, language-specific fallbacks |

### Business Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Low adoption | HIGH | Strong marketing, documentation, examples |
| Competition | MEDIUM | Focus su AI integration (differenziatore) |
| Maintenance burden | MEDIUM | Strong test suite, community contribution |
| Feature creep | LOW | Clear roadmap, prioritization |

---

## Go-to-Market Strategy

### Phase 1: Developer Community (Months 1-3)
- Open source release (Apache 2.0)
- Hacker News, Reddit launch
- Dev.to, Medium articles
- Twitter/X presence
- Discord community

### Phase 2: Enterprise Outreach (Months 4-6)
- Case studies
- White papers
- Conference presentations
- LinkedIn content
- Enterprise features

### Phase 3: Ecosystem Growth (Months 7-12)
- Plugin marketplace
- Partner integrations
- Training/certification
- Consulting services
- Pro/Enterprise tier (optional)

---

## Budget & Resources

### Development Time Estimate
- **Phase 1:** 160 hours (4 settimane full-time)
- **Phase 2:** 200 hours (5 settimane full-time)
- **Phase 3:** 240 hours (6 settimane full-time)
- **Phase 4:** 160 hours (4 settimane full-time)
- **Phase 5:** 120 hours (3 settimane full-time)
- **Phase 5.5:** 80 hours (2 settimane full-time) **QUICK WIN**
- **Phase 6:** 480 hours (12 settimane full-time)
- **Phase 7:** 320 hours (8 settimane full-time)
- **Phase 8:** 400 hours (10 settimane full-time)
- **Phase 9:** 480 hours (12 settimane full-time)
- **Phase 10:** Ongoing

**Total (Phases 1-9):** ~2640 hours (66 settimane full-time o 18 mesi part-time)

### Team Composition (Ideale)
- 1 Senior Python Developer (core development)
- 1 DevOps Engineer (CI/CD, automation)
- 1 Frontend Developer (dashboard, IDE extensions)
- 1 Technical Writer (documentation)
- 1 Designer (UI/UX per dashboard)
- Community contributors (plugin ecosystem)

---

## Next Actions

### Immediate (Week 1)
1. ✅ Create ROADMAP.md (questo documento)
2. ✅ Create GitHub milestones and issues
3. ⬜ Setup project structure per Phase 1
4. ⬜ Create ARCHITECTURE.md (dettaglio tecnico)
5. ⬜ Write technical specification per AI Bundle

### Short-term (Weeks 2-4)
1. ⬜ Implement SmartChunker prototype
2. ⬜ Create OpenAI formatter
3. ⬜ Build ai-bundle command
4. ⬜ Write comprehensive tests
5. ⬜ Document AI workflows

### Mid-term (Months 2-3)
1. ⬜ Complete Phase 1
2. ⬜ Start Phase 2 (pipeline)
3. ⬜ Community engagement
4. ⬜ First blog post/tutorial
5. ⬜ Alpha release

---

## Appendix

### Competitive Analysis

| Feature | Structum | Tree | Sphinx | MkDocs |
|---------|----------|------|--------|--------|
| Code visualization | ✅ Rich | ⚠️ Basic | ❌ | ❌ |
| AI-ready output | ✅ Optimized | ❌ | ❌ | ❌ |
| Plugin system | ✅ | ❌ | ✅ | ✅ |
| Git integration | 🔄 Planned | ❌ | ❌ | ⚠️ Partial |
| Report generation | 🔄 Planned | ❌ | ✅ | ✅ |
| CI/CD templates | 🔄 Planned | ❌ | ⚠️ Partial | ✅ |
| Framework plugins | 🔄 Planned | ❌ | ✅ | ⚠️ Limited |
| Multi-language | 🔄 Planned | ❌ | ⚠️ Limited | ⚠️ Limited |
| Quality metrics | 🔄 Planned | ❌ | ❌ | ❌ |
| Collaboration | 🔄 Planned | ❌ | ❌ | ❌ |

**Legend:** ✅ Full support | ⚠️ Partial | 🔄 In progress | ❌ Not supported

### References
- [OpenAI Token limits](https://platform.openai.com/docs/models)
- [Claude context windows](https://docs.anthropic.com/claude/docs)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Plugin architecture patterns](https://pluggy.readthedocs.io/)
- [Tree-sitter documentation](https://tree-sitter.github.io/)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-04
**Maintained by:** PythonWoods Team
**Status:** 🟢 Active Development

```

## `temp/BUGS.md` {#temp-BUGS-md}

```md
## Il comando archive senza argomenti non legge alcun file

```bash
structum archive -o ~/draft 
📂 Project Root: /home/pythinwoods/develop/structum
📄 Files found: 0
```

## Il comando archive genera un errore non gestito quando --output è una directory ma split mode non è abilittato

```
(.env) ➜  structum git:(develop) ✗ structum archive -e py -o ~/draft
📂 Project Root: /home/pythinwoods/develop/structum
📄 Files found: 47
✍️  Writing archive: /home/pythinwoods/draft
```

## Il flag --tree genera sempre l'albero delle directory completo, e non filtrato secondo i parametri impostati con --ext

```

## `docs/getting-started.md` {#docs-getting-started-md}

```md
# Getting Started

## Installation

Install Structum using pip:

```bash
pip install structum
```

## Basic Usage

### Visualize Directory Tree

```bash
structum tree .
```

### Archive Code

```bash
structum archive . --output code_context.md
```

### Clean Artifacts

```bash
structum clean .
```

## Next Steps

Explore the [CLI Reference](cli/index.md) for detailed command usage.
```

## `docs/index.md` {#docs-index-md}

```md
# Welcome to Structum

Structum is an Enterprise Code Structure & Documentation Engine designed to help you visualize, manage, and document your codebase effectively.

## Key Features

*   **Tree Visualization**: Visualize directory structures with rich icons and themes.
*   **Code Archiving**: Archive source code into Markdown files for LLM context or documentation.
*   **Maintenance**: Clean up `__pycache__` and other artifacts.
*   **Documentation**: Built-in tools to serve and deploy MkDocs documentation.
*   **Extensible**: Plugin system to add custom commands.

## Quick Links

*   [Getting Started](getting-started.md)
*   [CLI Reference](cli/index.md)
*   [Architecture](architecture/index.md)
*   [Development Guide](development/index.md)

```

## `docs/overrides/main.html` {#docs-overrides-main-html}

```html
{% extends "base.html" %}

<!-- Custom announcement banner -->
{% block announce %}
<div class="md-banner">
  <div class="md-banner-content">
    <span class="md-banner-icon">⭐</span>
    <span class="md-banner-text">
      Versione {{ config.extra.version | default("1.0.0") }} —
      <a href="https://github.com/pythonwoods/structum/releases" class="md-banner-link">
        Nuova release disponibile!
      </a>
    </span>
  </div>
</div>
{% endblock %}

<!-- Custom hero section for homepage -->
{% block hero %}
  {{ super() }}
{% endblock %}

<!-- Enhanced footer with additional links and branding -->
{% block footer %}
<footer class="md-footer">
  <!-- Standard footer navigation -->
  {% if page.previous_page or page.next_page %}
  <nav class="md-footer__inner md-grid" aria-label="Footer">
    {% if page.previous_page %}
    <a href="{{ page.previous_page.url | url }}" class="md-footer__link md-footer__link--prev" aria-label="Previous: {{ page.previous_page.title }}">
      <div class="md-footer__button md-icon">
        {% include ".icons/material/arrow-left.svg" %}
      </div>
      <div class="md-footer__title">
        <span class="md-footer__direction">Previous</span>
        <div class="md-ellipsis">{{ page.previous_page.title }}</div>
      </div>
    </a>
    {% endif %}
    {% if page.next_page %}
    <a href="{{ page.next_page.url | url }}" class="md-footer__link md-footer__link--next" aria-label="Next: {{ page.next_page.title }}">
      <div class="md-footer__title">
        <span class="md-footer__direction">Next</span>
        <div class="md-ellipsis">{{ page.next_page.title }}</div>
      </div>
      <div class="md-footer__button md-icon">
        {% include ".icons/material/arrow-right.svg" %}
      </div>
    </a>
    {% endif %}
  </nav>
  {% endif %}

  <!-- Custom footer metadata -->
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">

      <!-- Custom footer content -->
      <div class="md-footer-custom">
        <div class="md-footer-custom-content">
          <div class="md-footer-custom-section">
            <h4>Structum</h4>
            <p>Enterprise Code Structure & Documentation Engine</p>
            <p class="md-footer-license">
              Licensed under <a href="https://github.com/pythonwoods/structum/blob/main/LICENSE">Apache-2.0</a>
            </p>
          </div>

          <div class="md-footer-custom-section">
            <h4>Links</h4>
            <ul class="md-footer-links">
              <li><a href="https://github.com/pythonwoods/structum">GitHub Repository</a></li>
              <li><a href="https://github.com/pythonwoods/structum/issues">Report Issues</a></li>
              <li><a href="https://github.com/pythonwoods/structum/discussions">Discussions</a></li>
              <li><a href="{{ config.site_url }}">Documentation</a></li>
            </ul>
          </div>

          <div class="md-footer-custom-section">
            <h4>Resources</h4>
            <ul class="md-footer-links">
              <li><a href="{{ config.site_url }}getting-started/">Getting Started</a></li>
              <li><a href="{{ config.site_url }}user-guide/cli/">CLI Reference</a></li>
              <li><a href="{{ config.site_url }}api/">API Documentation</a></li>
              <li><a href="https://pypi.org/project/structum/">PyPI Package</a></li>
            </ul>
          </div>
        </div>

        <!-- Copyright and credits -->
        <div class="md-footer-copyright">
          <div class="md-footer-copyright-content">
            <p>
              © 2025 <a href="https://github.com/pythonwoods">PythonWoods</a>
              · Built with <a href="https://www.mkdocs.org/">MkDocs</a>
              and <a href="https://squidfunk.github.io/mkdocs-material/">Material for MkDocs</a>
            </p>
          </div>
        </div>
      </div>

      <!-- Social links (optional) -->
      {% include "partials/social.html" %}
    </div>
  </div>
</footer>
{% endblock %}

<!-- Additional custom blocks for future extensions -->
{% block styles %}
  {{ super() }}
  <!-- Custom styles are loaded via extra_css in mkdocs.yml -->
{% endblock %}

{% block scripts %}
  {{ super() }}
  <!-- Add custom JavaScript if needed -->
  <script>
    // Custom analytics or interactions can go here
    document.addEventListener('DOMContentLoaded', function() {
      // Example: Track custom events
      console.log('Structum documentation loaded');
    });
  </script>
{% endblock %}

```

## `docs/stylesheets/extra.css` {#docs-stylesheets-extra-css}

```css
/* ========================================
   Structum Custom Styles
   ======================================== */

/* CSS Variables for theming */
:root {
  --structum-primary: #009688;
  --structum-primary-dark: #00796b;
  --structum-accent: #ab47bc;
  --structum-gradient-start: #009688;
  --structum-gradient-end: #00bcd4;
  --structum-shadow: rgba(0, 0, 0, 0.1);
  --structum-shadow-hover: rgba(0, 0, 0, 0.2);
  --structum-border-radius: 12px;
}

[data-md-color-scheme="slate"] {
  --structum-primary: #26a69a;
  --structum-primary-dark: #00897b;
  --structum-accent: #ce93d8;
  --structum-gradient-start: #26a69a;
  --structum-gradient-end: #4dd0e1;
  --structum-shadow: rgba(0, 0, 0, 0.3);
  --structum-shadow-hover: rgba(0, 0, 0, 0.5);
}

/* ========================================
   Announcement Banner
   ======================================== */

.md-banner {
  background: linear-gradient(90deg, var(--structum-gradient-start), var(--structum-gradient-end));
  padding: 12px 16px;
  color: white;
  text-align: center;
  font-weight: 600;
  box-shadow: 0 2px 8px var(--structum-shadow);
}

.md-banner-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.md-banner-icon {
  font-size: 1.2em;
  animation: pulse 2s infinite;
}

.md-banner-link {
  color: white !important;
  text-decoration: underline;
  font-weight: 700;
}

.md-banner-link:hover {
  opacity: 0.9;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

/* ========================================
   Hero Section
   ======================================== */

.hero-section {
  text-align: center;
  padding: 60px 20px 40px;
  background: linear-gradient(135deg,
    var(--structum-gradient-start) 0%,
    var(--structum-gradient-end) 100%
  );
  color: white;
  border-radius: var(--structum-border-radius);
  margin-bottom: 40px;
  box-shadow: 0 8px 32px var(--structum-shadow);
}

.hero-content h1 {
  font-size: 3.5em;
  font-weight: 800;
  margin-bottom: 0.3em;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.hero-content h3 {
  font-size: 1.5em;
  font-weight: 400;
  opacity: 0.95;
  margin-bottom: 1em;
}

.hero-description {
  font-size: 1.15em;
  max-width: 700px;
  margin: 0 auto 2em;
  opacity: 0.9;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.hero-buttons .md-button {
  font-size: 1.1em;
  padding: 12px 32px;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.hero-buttons .md-button--primary {
  background-color: white !important;
  color: var(--structum-primary) !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.hero-buttons .md-button--primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 24px rgba(0, 0, 0, 0.25);
}

.hero-buttons .md-button:not(.md-button--primary) {
  background-color: rgba(255, 255, 255, 0.2) !important;
  color: white !important;
  border: 2px solid white;
}

.hero-buttons .md-button:not(.md-button--primary):hover {
  background-color: rgba(255, 255, 255, 0.3) !important;
  transform: translateY(-2px);
}

/* ========================================
   Feature Cards Grid
   ======================================== */

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
  margin: 40px 0;
}

.feature-card {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: var(--structum-border-radius);
  padding: 28px;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px var(--structum-shadow);
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px var(--structum-shadow-hover);
  border-color: var(--structum-primary);
}

.feature-card h3 {
  color: var(--structum-primary);
  margin-top: 0;
  font-size: 1.3em;
  font-weight: 700;
}

.feature-card code {
  font-size: 0.9em;
}

.feature-card pre {
  margin-top: 16px;
  border-radius: 8px;
}

/* ========================================
   Quick Start Grid
   ======================================== */

.quick-start-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
  margin: 32px 0;
}

.qs-step {
  background: var(--md-code-bg-color);
  border-left: 4px solid var(--structum-primary);
  border-radius: 8px;
  padding: 24px;
  transition: all 0.3s ease;
}

.qs-step:hover {
  border-left-width: 6px;
  transform: translateX(4px);
  box-shadow: 0 4px 16px var(--structum-shadow);
}

.qs-step h4 {
  color: var(--structum-primary);
  margin-top: 0;
  font-weight: 700;
}

.qs-step pre {
  margin-top: 12px;
  border-radius: 6px;
}

/* ========================================
   Key Features List
   ======================================== */

.key-features {
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: var(--structum-border-radius);
  padding: 32px;
  margin: 32px 0;
  box-shadow: 0 2px 8px var(--structum-shadow);
}

.key-features ul {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 16px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.key-features li {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.05em;
}

.key-features li strong {
  color: var(--structum-primary);
}

/* ========================================
   Use Cases Section
   ======================================== */

.use-cases {
  margin: 32px 0;
}

.use-cases .admonition {
  border-radius: var(--structum-border-radius);
  box-shadow: 0 2px 8px var(--structum-shadow);
  transition: all 0.3s ease;
}

.use-cases .admonition:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px var(--structum-shadow-hover);
}

/* ========================================
   CTA Section
   ======================================== */

.cta-section {
  text-align: center;
  padding: 48px 24px;
  background: linear-gradient(135deg,
    rgba(var(--structum-primary), 0.1) 0%,
    rgba(var(--structum-accent), 0.1) 100%
  );
  border-radius: var(--structum-border-radius);
  margin: 40px 0;
  box-shadow: 0 4px 16px var(--structum-shadow);
}

.cta-section h2 {
  color: var(--structum-primary);
  font-size: 2.2em;
  margin-bottom: 0.5em;
}

.cta-section .md-button {
  margin: 8px;
  font-size: 1.1em;
  padding: 12px 32px;
  border-radius: 8px;
}

/* ========================================
   Footer Custom Styles
   ======================================== */

.md-footer-custom {
  padding: 40px 0 20px;
  background: var(--md-footer-bg-color);
}

.md-footer-custom-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 32px;
  margin-bottom: 32px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
  padding: 0 24px;
}

.md-footer-custom-section h4 {
  color: var(--structum-primary);
  font-size: 1.1em;
  font-weight: 700;
  margin-bottom: 12px;
}

.md-footer-custom-section p {
  opacity: 0.8;
  font-size: 0.95em;
  margin: 8px 0;
}

.md-footer-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.md-footer-links li {
  margin: 8px 0;
}

.md-footer-links a {
  color: var(--md-footer-fg-color);
  text-decoration: none;
  opacity: 0.8;
  transition: all 0.2s ease;
}

.md-footer-links a:hover {
  opacity: 1;
  color: var(--structum-primary);
  text-decoration: underline;
}

.md-footer-license {
  font-size: 0.9em;
  opacity: 0.7;
  margin-top: 12px;
}

.md-footer-copyright {
  text-align: center;
  padding: 20px 0;
  border-top: 1px solid var(--md-default-fg-color--lightest);
  opacity: 0.7;
  font-size: 0.9em;
}

.md-footer-copyright-content p {
  margin: 0;
}

.md-footer-copyright a {
  color: inherit;
  text-decoration: none;
}

.md-footer-copyright a:hover {
  color: var(--structum-primary);
  text-decoration: underline;
}

/* ========================================
   Footer Info (on landing page)
   ======================================== */

.footer-info {
  text-align: center;
  padding: 32px 16px;
  opacity: 0.8;
  font-size: 0.95em;
}

.footer-info a {
  margin: 0 12px;
  color: var(--md-default-fg-color);
  text-decoration: none;
  transition: color 0.2s ease;
}

.footer-info a:hover {
  color: var(--structum-primary);
  text-decoration: underline;
}

/* ========================================
   Enhanced Header
   ======================================== */

.md-header {
  box-shadow: 0 2px 16px var(--structum-shadow);
  backdrop-filter: blur(8px);
}

/* ========================================
   Responsive Design
   ======================================== */

@media (max-width: 768px) {
  .hero-content h1 {
    font-size: 2.5em;
  }

  .hero-content h3 {
    font-size: 1.2em;
  }

  .hero-description {
    font-size: 1em;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .quick-start-grid {
    grid-template-columns: 1fr;
  }

  .key-features ul {
    grid-template-columns: 1fr;
  }

  .md-footer-custom-content {
    grid-template-columns: 1fr;
  }
}

/* ========================================
   Code Blocks Enhancement
   ======================================== */

.highlight pre {
  border-radius: 8px;
  box-shadow: 0 2px 8px var(--structum-shadow);
}

/* ========================================
   Admonitions Enhancement
   ======================================== */

.admonition {
  border-radius: var(--structum-border-radius);
  box-shadow: 0 2px 4px var(--structum-shadow);
}

/* ========================================
   Navigation Enhancement
   ======================================== */

.md-nav__link--active {
  color: var(--structum-primary) !important;
  font-weight: 600;
}

.md-nav__link:hover {
  color: var(--structum-primary);
}

/* ========================================
   Tables Enhancement
   ======================================== */

table {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px var(--structum-shadow);
}

/* ========================================
   Utility Classes
   ======================================== */

.text-center {
  text-align: center;
}

.mt-4 {
  margin-top: 2rem;
}

.mb-4 {
  margin-bottom: 2rem;
}

```

## `docs/cli/commands.md` {#docs-cli-commands-md}

```md
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

```

## `docs/cli/index.md` {#docs-cli-index-md}

```md
# CLI Reference

Structum provides a powerful Command Line Interface (CLI) to interact with its features.

## Commands

*   [Tree](commands.md#tree): Visualize directory structures.
*   [Archive](commands.md#archive): Archive source code.
*   [Clean](commands.md#clean): Clean up artifacts.
*   [Docs](commands.md#docs): Manage documentation.
*   [Plugins](commands.md#plugins): Manage plugins.

```

## `docs/reference/api.md` {#docs-reference-api-md}

```md
# API Reference

::: structum.core.tree
    handler: python
    options:
      members:
        - build_tree
        - print_tree
        - get_tree_ascii

::: structum.core.archive
    handler: python
    options:
      members:
        - create_archive

::: structum.core.clean
    handler: python
    options:
      members:
        - clean_pycache

```

## `docs/reference/index.md` {#docs-reference-index-md}

```md
# Reference

Technical reference documentation.

## Sections

*   [API Reference](api.md): Python API documentation.

```

## `docs/development/conventions.md` {#docs-development-conventions-md}

```md
# Conventions

## Code Style

We use `ruff` for linting and formatting.

*   **Line Length**: 100 characters.
*   **Quotes**: Double quotes.
*   **Imports**: Sorted automatically.

## Type Hinting

We use `mypy` in strict mode. All functions must have type hints for arguments and return values.

## Docstrings

We follow the Google docstring style. Every public module, class, and function must have a docstring.

```

## `docs/development/roadmap.md` {#docs-development-roadmap-md}

```md
# Structum Roadmap - Documentation Engine

> **Vision:** Trasformare Structum nel leading Documentation Engine per sviluppatori, team enterprise e AI/LLM workflows.
> **Version:** 2.0 (Updated 2025-12-04)

---

## Executive Summary

Structum evolverà da un tool di visualizzazione del codice a una **piattaforma completa di documentazione**, con capacità di:

- **AI-ready output** ottimizzato per ChatGPT, Claude, Gemini
- **Multi-language support** (Python, JavaScript, TypeScript, Go, Rust, Java)
- **Pipeline automation** per CI/CD enterprise
- **Report generation** professionale (PDF, Dashboard, LaTeX)
- **Plugin ecosystem** estensibile per framework popolari
- **Git integration** per documentazione evolutiva
- **Collaboration features** per team distributed
- **Quality assurance** per documentation excellence

---

## Target Audience

1. **Developers individuali** - Quick documentation, AI assistant integration
2. **Team aziendali** - Code review, onboarding, audit compliance, collaboration
3. **AI/LLM users** - Context injection, RAG workflows, semantic search
4. **Enterprise** - Compliance, security audit, documentation standards, multi-language support
5. **Academic** - Research documentation, thesis, technical papers
6. **Open Source** - Community documentation, contributor onboarding

---

## Strategic Phases

### 🚀 Phase 1: AI-Ready Output (PRIORITY 1)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Differenziatore chiave nel mercato
**Status:** 📋 Planned

#### Obiettivi
- Output ottimizzato per LLM (token limits, chunking intelligente)
- Format-specific adapters (OpenAI, Claude, Gemini, DeepSeek)
- RAG-ready structured output
- Metadata injection per context enhancement

#### Deliverables

##### 1.1 AI Bundle Command
```bash
structum ai-bundle --format=openai --max-tokens=8000
structum ai-bundle --format=claude --split-by-module
structum ai-bundle --format=gemini --context=refactoring
structum ai-bundle --format=generic --output=./ai-context/
```

**Features:**
- Chunking intelligente (rispetta token limits)
- Prioritizzazione file (core > tests > docs)
- Metadata injection (dependencies, purpose, git info)
- Format-specific optimization
- Multiple output formats (Markdown, JSON, XML)

##### 1.2 Chunking Engine
**File:** `src/structum/core/ai/chunker.py`

**Strategies:**
- Token-based (rispetta limits GPT-4, Claude, etc.)
- Module-based (mantiene coesione logica)
- Dependency-based (include imports necessari)
- Semantic-based (raggruppa funzionalità correlate)

##### 1.3 Format Adapters
**File:** `src/structum/core/ai/formatters.py`

- OpenAI Formatter (GPT-4 Turbo, 128K tokens)
- Claude Formatter (Claude 3 Opus, 200K tokens)
- Gemini Formatter (Gemini 1.5 Pro, 1M tokens)
- DeepSeek Formatter

##### 1.4 RAG Integration
**File:** `src/structum/core/ai/rag.py`

- Vector embeddings ready
- Chunk metadata per retrieval
- Semantic search preparation
- Context window optimization

#### Success Metrics
- ✅ Output < token limits per ogni formato
- ✅ Context retention > 95%
- ✅ 3+ format adapters implementati
- ✅ Documentazione completa per AI workflows

---

### 📚 Phase 2: Documentation Pipeline (PRIORITY 2)
**Timeline:** 3-4 settimane
**Impact:** HIGH - Enterprise adoption driver
**Status:** 📋 Planned

#### Obiettivi
- Automazione completa documentazione
- Git integration (blame, changelog, diff)
- Auto-update su commit
- Versioning e snapshot

#### Deliverables

##### 2.1 Documentation Compiler
```bash
structum docs compile --quality=enterprise
structum docs compile --format=mkdocs --output=./docs/generated/
structum docs compile --incremental  # Solo file modificati
```

**Features:**
- Auto-detection progetto (Python, JS, Go, Rust)
- Template-based generation
- Multi-format output (Markdown, HTML, PDF)
- Incremental builds (solo delta)

##### 2.2 Git Integration
**File:** `src/structum/integrations/git.py`

**Features:**
- Blame → documentation attribution
- Changelog automation
- Diff visualization
- Commit history per file
- Evolution tracking

##### 2.3 Auto-Update Pipeline
```bash
structum docs watch --auto-rebuild
structum docs watch --git-hook  # Installa git hook
```

**Features:**
- File watcher con debouncing
- Git hooks (pre-commit, post-commit)
- CI/CD integration
- Webhook support

##### 2.4 Versioning System
**File:** `src/structum/core/pipeline/versioning.py`

- Snapshot management
- Version comparison
- Rollback support
- Archive old versions

##### 2.5 Change Detection & Diff Visualization ⭐ NEW
```bash
structum diff v1.0.0..HEAD --output=changes.md
structum changelog auto-generate --conventional-commits
structum diff visualize --interactive --output=diff.html
```

**Features:**
- Visual diff per codice
- API breaking changes detection
- Deprecation warnings
- Migration guides auto-generation
- Semantic versioning suggestions
- Release notes automation

#### Success Metrics
- ✅ Auto-update < 5 secondi
- ✅ Git integration completa
- ✅ CI/CD templates per GitHub/GitLab
- ✅ Versioning system funzionante
- ✅ Automated diff detection

---

### 🔌 Phase 3: Plugin Ecosystem (PRIORITY 3)
**Timeline:** 4-6 settimane
**Impact:** MEDIUM-HIGH - Estensibilità e adoption
**Status:** 🔄 In Progress (SDK exists)

#### Obiettivi
- Plugin system robusto
- Framework integrations (FastAPI, Pydantic, SQLAlchemy, Typer)
- Community plugins support
- Plugin marketplace concept

#### Deliverables

##### 3.1 Enhanced Plugin System
```bash
structum plugins list
structum plugins search fastapi
structum plugins add fastapi-autodoc
structum plugins remove django-mapper
structum plugins update --all
```

**Features:**
- Plugin discovery
- Dependency management
- Version compatibility
- Enable/disable plugins
- Plugin configuration

##### 3.2 Framework Plugins

**FastAPI Plugin**
- Auto-detect routes
- Extract endpoint metadata
- Generate OpenAPI supplement
- Document dependencies

**Typer/Click Plugin**
- CLI command documentation
- Argument/option extraction
- Help text generation
- Command tree visualization

**Pydantic Plugin**
- Schema extraction
- Validation rules documentation
- Field descriptions
- JSON Schema export

**SQLAlchemy Plugin**
- Model relationship mapping
- ER diagram generation
- Migration history
- Schema visualization

##### 3.3 Plugin Marketplace & Templates ⭐ NEW
```bash
structum templates list --category=fintech
structum templates install corporate-standard
structum templates publish my-template --public
```

**Features:**
- Template marketplace (como npm)
- Industry-specific templates (fintech, healthcare, etc)
- Company branding templates
- Community ratings & reviews
- Security scanning
- Version management

##### 3.4 Plugin Development Kit
**File:** `src/structum/plugins/sdk.py`

**Documentation:**
- Plugin development guide
- API reference
- Example plugins
- Testing framework

#### Success Metrics
- ✅ 4+ official plugins rilasciati
- ✅ Plugin SDK completo
- ✅ Community plugin support
- ✅ Plugin documentation
- ✅ Plugin marketplace operational

---

### 📊 Phase 4: Report Generation (PRIORITY 3)
**Timeline:** 3-4 settimane
**Impact:** MEDIUM - Visual appeal e enterprise adoption
**Status:** 📋 Planned

#### Obiettivi
- PDF export professionale
- Dashboard interattive
- Custom themes e branding
- Multiple output formats

#### Deliverables

##### 4.1 PDF Report Generator
```bash
structum report full --pdf --theme=corporate --output=report.pdf
structum report summary --pdf --theme=minimal
structum report audit --pdf --compliance=iso27001
```

**Features:**
- Corporate themes (branding)
- Tree visualization
- Code statistics
- Git history
- Compliance sections
- Custom logo/footer

**Tech Stack:**
- WeasyPrint o ReportLab
- Jinja2 templates
- CSS styling
- SVG tree rendering

##### 4.2 Interactive Dashboard (Static HTML)
```bash
structum report dashboard --interactive --output=./dashboard/
structum report dashboard --serve --port=8080
```

**Features:**
- File explorer interattivo
- Code statistics charts
- Dependency graphs
- Timeline evolution
- Search functionality (client-side con Lunr.js)

**Tech Stack:**
- Static HTML/CSS/vanilla JS (NO React/Vue framework overhead)
- Chart.js per grafici
- D3.js per visualizzazioni
- Lunr.js per ricerca client-side
- Responsive design

##### 4.3 Custom Templates
```bash
structum report template list
structum report template create my-template
structum report full --template=my-template
```

**Features:**
- Template engine (Jinja2)
- Custom sections
- Conditional rendering
- Variable injection
- Partial includes

##### 4.4 LaTeX Export
```bash
structum report latex --output=documentation.tex
structum report latex --template=academic --with-toc
structum report latex --compile-pdf  # Auto-compile to PDF
```

**Features:**
- Professional LaTeX document generation
- Academic paper templates (IEEE, ACM, Springer)
- Thesis/dissertation templates
- Technical book format
- Code listings with syntax highlighting (listings/minted)
- Mathematical notation support
- Bibliography integration (BibTeX)
- Cross-referencing (labels, refs)
- Table of contents, list of figures
- Overleaf-compatible output
- Auto-compile to PDF (requires pdflatex/xelatex)

**Templates Included:**
- `academic` - IEEE/ACM style
- `thesis` - University thesis format
- `book` - Technical book layout
- `report` - Formal technical report
- `minimal` - Basic LaTeX article

##### 4.5 Multi-Format Export
- **PDF** - Audit, compliance, presentation
- **HTML** - Interactive, dashboard
- **LaTeX** - Academic papers, theses, technical books
- **JSON** - API, integration
- **XML** - Enterprise systems
- **Markdown** - Documentation
- **DOCX** - Word documents

#### Success Metrics
- ✅ PDF generation funzionante
- ✅ Dashboard interattiva
- ✅ 3+ themes disponibili
- ✅ Multiple export formats
- ✅ LaTeX templates operational

---

### 🏗️ Phase 5: CI/CD Integration (PRIORITY 2)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Enterprise adoption
**Status:** 📋 Planned

#### Obiettivi
- GitHub Actions templates
- GitLab CI templates
- Jenkins integration
- Pre-commit hooks
- Docker containerization

#### Deliverables

##### 5.1 GitHub Actions Workflow
```yaml
# .github/workflows/docs.yml
name: Documentation Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  generate-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pythonwoods/structum-action@v1
        with:
          quality: enterprise
          format: mkdocs
          ai-bundle: true
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
```

##### 5.2 GitLab CI Template
```yaml
# .gitlab-ci.yml
include:
  - remote: 'https://raw.githubusercontent.com/pythonwoods/structum/main/ci/gitlab-ci.yml'

structum:docs:
  extends: .structum-base
  variables:
    QUALITY: enterprise
    FORMAT: mkdocs
```

##### 5.3 Pre-commit Hooks
```bash
structum hooks install
structum hooks config --auto-update
```

**Hooks:**
- `pre-commit` - Validate structure
- `post-commit` - Update docs
- `pre-push` - Generate report

##### 5.4 CI/CD Examples Repository
```
examples/ci-cd/
├── github-actions/
│   ├── basic.yml
│   ├── enterprise.yml
│   └── multi-format.yml
├── gitlab-ci/
│   ├── basic.yml
│   └── enterprise.yml
├── jenkins/
│   └── Jenkinsfile
└── docker/
    └── Dockerfile.docs
```

#### Success Metrics
- ✅ GitHub Action pubblicata
- ✅ GitLab CI template
- ✅ Examples completi
- ✅ Documentation per CI/CD
- ✅ Docker image pubblicata

---

### 🐳 Phase 5.5: Docker & Static Dashboard ⚡ QUICK WIN
**Timeline:** 1-2 settimane
**Impact:** HIGH - Zero-dependency deployment, enterprise ready
**Status:** 📋 Planned
**Priority:** IMMEDIATE (Quick Win)

#### Obiettivi
- Docker containerization completa
- Static dashboard HTML prototipo
- Zero dependency hell
- One-command deployment

#### Deliverables

##### 5.5.1 Docker Container
```dockerfile
# Dockerfile multi-stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -e .[full]

FROM python:3.11-slim
COPY --from=builder /app /app
WORKDIR /app
ENTRYPOINT ["structum"]
CMD ["--help"]
```

**Features:**
- Multi-stage build (size optimization)
- Alpine variant per lightweight deployments
- Docker Compose per development
- GitHub Container Registry
- Docker Hub publishing
- Healthcheck support

**Usage:**
```bash
docker run pythonwoods/structum:latest tree /project
docker-compose up docs-server
```

##### 5.5.2 Docker Compose Stack
```yaml
# docker-compose.yml
version: '3.8'
services:
  structum:
    image: pythonwoods/structum:latest
    volumes:
      - ./project:/workspace
    command: archive /workspace --output=/workspace/docs

  dashboard:
    image: pythonwoods/structum:latest
    command: serve-dashboard --port=8080
    ports:
      - "8080:8080"
    volumes:
      - ./dashboard:/dashboard
```

##### 5.5.3 Static Dashboard HTML
```bash
structum dashboard generate --output=./dashboard/
structum dashboard serve --port=8080 --watch
```

**Tech Stack:**
- Pure HTML5/CSS3
- Vanilla JavaScript (ES6+)
- Chart.js for metrics
- Lunr.js for search
- Zero build step
- Zero npm dependencies

**Dashboard Features:**
- File tree explorer
- Code statistics
- Search functionality
- Responsive design
- Dark/Light theme
- Offline-capable

#### Success Metrics
- ✅ Docker image < 200MB
- ✅ Build time < 2 minuti
- ✅ Dashboard loads < 1 secondo
- ✅ Works offline
- ✅ Published to Docker Hub

---

### 🌐 Phase 6: Multi-Language & IDE Integration (PRIORITY 1)
**Timeline:** 3-4 mesi
**Impact:** VERY HIGH - 10x market expansion
**Status:** 📋 Planned

#### Obiettivi
- Support multi-language codebases
- IDE extensions per developer experience
- Framework detection automatica
- Cross-language documentation

#### Deliverables

##### 6.1 Multi-Language Support
```bash
structum tree . --lang javascript
structum archive . --lang typescript --output ts-docs/
structum archive . --lang go,rust --multi-lang
structum archive . --auto-detect  # Smart language detection
```

**Linguaggi Supportati:**

1. **JavaScript/TypeScript** (Phase 6.1)
   - Node.js, React, Vue, Angular
   - JSDoc/TSDoc parsing
   - Package.json analysis
   - npm/yarn dependency mapping

2. **Go** (Phase 6.2)
   - Module structure
   - Godoc comments
   - go.mod dependency analysis
   - Interface documentation

3. **Rust** (Phase 6.3)
   - Cargo.toml analysis
   - Rustdoc comments
   - Trait documentation
   - Macro expansion

4. **Java/Kotlin** (Phase 6.4)
   - Maven/Gradle projects
   - JavaDoc/KDoc
   - Spring Framework detection
   - Annotation processing

5. **C#/.NET** (Phase 6.5)
   - .csproj analysis
   - XML documentation
   - NuGet dependencies
   - .NET Core/Framework detection

6. **PHP** (Phase 6.6)
   - Composer projects
   - PHPDoc
   - Laravel/Symfony detection
   - Namespace analysis

**Tech Stack:**
- Tree-sitter per multi-language parsing
- Language-specific AST analyzers
- Universal documentation format
- Cross-language reference linking

##### 6.2 IDE Extensions

**VS Code Extension** (`structum-vscode`)
```bash
# Features:
- Tree preview in sidebar
- Documentation hover tooltips
- Generate docs on save
- Plugin marketplace integration
- Live preview
- Keyboard shortcuts (Ctrl+Shift+D)
```

**JetBrains Plugin** (IntelliJ, PyCharm, WebStorm, GoLand, Rider)
```bash
# Features:
- Tool window integration
- Context menu actions
- Run configurations
- Code insights
- Refactoring integration
```

**Vim/Neovim Plugin** (`structum.nvim`)
```lua
-- :Structum tree
-- :Structum archive
-- :Structum ai-bundle
```

**Emacs Package** (`structum-mode`)
```elisp
;; M-x structum-tree
;; M-x structum-archive
```

##### 6.3 Framework Detection
```bash
structum detect  # Auto-detect all frameworks
```

**Detected Frameworks:**
- Python: Django, Flask, FastAPI, Pydantic
- JavaScript: React, Vue, Angular, Express, Next.js
- Go: Gin, Echo, Fiber
- Rust: Actix, Rocket, Axum
- Java: Spring Boot, Micronaut, Quarkus

#### Success Metrics
- ✅ 6+ languages supported
- ✅ 4+ IDE extensions pubblicati
- ✅ Framework detection > 90% accuracy
- ✅ Cross-language reference linking
- ✅ 10x market size increase

---

### 🎯 Phase 7: Quality Assurance & Testing (PRIORITY 2)
**Timeline:** 2-3 mesi
**Impact:** HIGH - Enterprise documentation quality
**Status:** 📋 Planned

#### Obiettivi
- Documentation quality metrics
- Automated testing for docs
- Linting e validation
- Code metrics integration

#### Deliverables

##### 7.1 Documentation Quality Assurance
```bash
structum lint docs/ --check-completeness --check-style
structum quality-report --output quality.html
structum validate --standard=enterprise
```

**Quality Metrics:**
- **Completeness Score**: % moduli documentati
- **Readability Score**: Flesch-Kincaid, Gunning Fog
- **Link Validation**: Broken links, missing references
- **Code Examples**: Syntax check, runnable
- **Consistency Check**: Naming conventions, formatting
- **Terminology Validation**: Glossario aziendale
- **Accessibility Check**: WCAG compliance per HTML output

**Output Dashboard:**
```
Documentation Quality Report
────────────────────────────────────
✅ Coverage:        87% (target: 90%)
⚠️  Readability:    Grade 10 (target: 8)
❌ Broken Links:    12 found
✅ Code Examples:   100% valid
⚠️  Terminology:    5 inconsistencies
Overall Score:      78/100 (Good)
```

##### 7.2 Documentation-as-Code Testing
```bash
structum test docs/ --extract-examples
structum test docs/ --validate-links --check-syntax
structum test docs/ --ci-mode  # Exit code per CI/CD
```

**Features:**
- Code block extraction
- Auto-execution degli esempi
- Snapshot testing
- Link validation (HTTP 200 check)
- Image validation
- Version compatibility testing

##### 7.3 Code Metrics & Technical Debt
```bash
structum metrics analyze --output=metrics.json
structum debt-tracker init --threshold=high
structum complexity-report --format=html
```

**Metrics Tracked:**
- Cyclomatic Complexity
- Code Churn (file change frequency)
- Test Coverage integration
- Technical Debt Score (SQALE)
- Security Vulnerabilities (Bandit, Safety)
- Performance Hotspots
- Maintainability Index

**Output:**
```
Code Health Dashboard
─────────────────────────────────
High Complexity:       23 functions
Technical Debt:        47 hours estimated
Security Issues:       3 medium, 1 low
Test Coverage:         73%
Hotspot Files:         5 identified
Action Required:       12 refactorings
```

##### 7.4 Accessibility (a11y) Support
```bash
structum a11y check --standard=wcag2.1-aa
structum a11y fix --auto
```

**Features:**
- Screen reader optimization
- Keyboard navigation
- Alt text generation per immagini
- Color contrast validation
- ARIA labels automation
- Multi-language support (i18n)

#### Success Metrics
- ✅ Quality score > 85/100
- ✅ Zero broken links in docs
- ✅ 100% runnable code examples
- ✅ WCAG AA compliance
- ✅ Automated testing in CI/CD

---

### 👥 Phase 8: Collaboration & Enterprise (PRIORITY 2)
**Timeline:** 3-4 mesi
**Impact:** HIGH - Team productivity, enterprise sales
**Status:** 📋 Planned

#### Obiettivi
- Real-time collaboration features
- Cloud integrations
- Compliance & audit reports
- Team workflow automation

#### Deliverables

##### 8.1 Collaboration Hub
```bash
structum collab start --session=planning
structum collab invite user@company.com
structum collab comments --list
```

**Features:**
- Inline comments on docs
- Suggestion mode (like Google Docs)
- Real-time editing (WebSockets)
- Approval workflows
- Team roles & permissions

##### 8.2 Enterprise Cloud Integration
```bash
structum cloud sync --provider=aws-s3
structum cloud backup --provider=gcp-storage
structum cloud audit-logs --export
```

**Integrations:**
- AWS S3 / CloudFront
- Google Cloud Storage
- Azure Blob Storage
- SharePoint / OneDrive
- Confluence / Jira
- Slack / Microsoft Teams notifications

##### 8.3 Compliance & Audit
```bash
structum audit generate --standard=gdpr
structum audit generate --standard=soc2
structum audit generate --standard=hipaa
```

**Features:**
- GDPR compliance report
- SOC2 documentation trail
- HIPAA compliance check
- Access logs
- Change history audit

#### Success Metrics
- ✅ Real-time collaboration functional
- ✅ 3+ cloud providers supported
- ✅ Compliance reports generated
- ✅ Enterprise security standards met

---

### 🧠 Phase 9: AI-Powered Intelligence (PRIORITY 1)
**Timeline:** 4-6 mesi
**Impact:** VERY HIGH - Future proofing
**Status:** 📋 Planned

#### Obiettivi
- Semantic search (RAG)
- Auto-documentation generation
- Code explanation
- Refactoring suggestions

#### Deliverables

##### 9.1 Semantic Search Engine
```bash
structum search "how to authenticate user" --semantic
structum search "database connection logic" --context=legacy
```

**Features:**
- Vector database integration (ChromaDB, Pinecone)
- Embeddings generation (OpenAI, HuggingFace)
- Natural language queries
- Context-aware results

##### 9.2 Auto-Doc Generator
```bash
structum autodoc generate src/auth.py --level=detailed
structum autodoc update --all --ai-model=gpt-4
```

**Features:**
- Docstring generation
- README generation
- Architecture diagram generation
- API reference automation

##### 9.3 Code Assistant
```bash
structum explain src/complex_algo.py
structum suggest-refactor src/legacy_module.py
structum generate-tests src/utils.py
```

**Features:**
- Code explanation
- Refactoring proposals
- Unit test generation
- Bug detection

#### Success Metrics
- ✅ Semantic search < 200ms
- ✅ Auto-doc accuracy > 90%
- ✅ Code assistant helpfulness rating > 4.5/5

---

### 🌍 Phase 10: Ecosystem Expansion (Long Term)
**Timeline:** 6-12 mesi
**Impact:** HIGH - Platform dominance
**Status:** 📋 Planned

#### Obiettivi
- Mobile app
- Desktop app (Electron/Tauri)
- Web platform (SaaS)
- Community events

#### Deliverables

##### 10.1 Desktop Application
- Cross-platform (Windows, macOS, Linux)
- Visual editor
- Drag & drop interface
- Offline mode

##### 10.2 Web Platform (SaaS)
- Hosted documentation
- Team management
- Analytics dashboard
- Custom domains

##### 10.3 Mobile App
- Documentation viewer
- Quick reference
- Notifications
- Offline access

#### Success Metrics
- ✅ Desktop app launched
- ✅ SaaS platform beta
- ✅ Mobile app MVP

```

## `docs/development/index.md` {#docs-development-index-md}

```md
# Development

Guide for contributors and developers.

## Sections

*   [Conventions](conventions.md): Coding style and standards.
*   [Plugin Development](plugins.md): Creating custom plugins.
*   [Testing](testing.md): How to run and write tests.
*   [Roadmap](roadmap.md): Future plans.

```

## `docs/development/testing.md` {#docs-development-testing-md}

```md
# Testing

## Running Tests

We use `pytest` for testing.

```bash
pytest
```

## Writing Tests

*   **Unit Tests**: Place in `tests/`.
*   **CLI Tests**: Use `typer.testing.CliRunner`.

Example:
```python
from typer.testing import CliRunner
from structum.cli.main import app

runner = CliRunner()

def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
```

```

## `docs/development/plugins.md` {#docs-development-plugins-md}

```md
# Plugin Development

This guide covers everything you need to create plugins for Structum, whether you're contributing to the core project or building standalone plugins.

## Overview

Structum's plugin system allows extending functionality with custom commands and processing logic. There are two ways to create plugins:

1. **Builtin Plugins** – For contributors to the Structum project
2. **External Plugins** – Standalone packages published to PyPI

## Categories

Plugins are organized into categories:

| Category | Description |
|----------|-------------|
| `analysis` | Code analysis and metrics |
| `export` | Export and format conversion |
| `formatting` | Code formatting and style |
| `utility` | Utility and helper tools (default) |

---

## Creating a Builtin Plugin (Contributors)

If you're contributing to the Structum project and want to add a new plugin:

### Step 1: Generate the Skeleton

From the **root of the structum repository**:

```bash
structum plugins new my-plugin --category analysis
```

This automatically creates the plugin in `src/structum/plugins/my_plugin/`.

### Step 2: Implement Your Plugin

Edit the generated files:

- `plugin.py` – Main plugin class
- `commands/main.py` – CLI commands
- `core/logic.py` – Business logic

### Step 3: Register the Plugin

Edit `src/structum/plugins/loader.py`:

```python
def load_builtin_plugins(app: typer.Typer) -> None:
    """Loads built-in plugins."""
    from . import sample, my_plugin  # Add your import

    # Register plugin classes
    PluginRegistry.register(sample.SamplePlugin)
    PluginRegistry.register(my_plugin.MyPlugin)  # Add this

    # Initialize plugins
    PluginRegistry.load_all()

    # Register CLI commands for enabled plugins
    for name in ["sample", "my_plugin"]:  # Add your plugin name
        plugin = PluginRegistry.get(name)
        if plugin and get_plugin_enabled(name):
            plugin.register_commands(app)
```

### Step 4: Test Your Plugin

```bash
# Verify it appears in the list
structum plugins list

# Enable it if disabled
structum plugins enable my-plugin

# Run your command
structum my-plugin <your-command>
```

### Step 5: Submit a Pull Request

Commit your changes and open a PR to the `develop` branch.

---

## Creating an External Plugin (Standalone Package)

If you want to create a plugin that can be published to PyPI:

### Step 1: Generate the Skeleton

From your preferred directory:

```bash
structum plugins new my-awesome-plugin --category export --output ~/projects/
```

This creates `~/projects/my_awesome_plugin/`.

### Step 2: Create Package Structure

Add these files to make it a proper Python package:

```
my_awesome_plugin/
├── pyproject.toml      # NEW
├── README.md           # NEW
├── src/
│   └── my_awesome_plugin/
│       ├── __init__.py
│       ├── plugin.py
│       ├── commands/
│       │   ├── __init__.py
│       │   └── main.py
│       └── core/
│           ├── __init__.py
│           └── logic.py
```

### Step 3: Configure `pyproject.toml`

```toml
[project]
name = "structum-my-awesome-plugin"
version = "0.1.0"
description = "My awesome Structum plugin"
requires-python = ">=3.11"
dependencies = [
    "structum>=0.1.0",
    "typer>=0.9.0",
]

[project.entry-points."structum.plugins"]
my-awesome-plugin = "my_awesome_plugin:MyAwesomePluginPlugin"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

> **Important**: The entry point format is:
> ```
> plugin-name = "package_name:PluginClassName"
> ```

### Step 4: Install Locally for Testing

```bash
cd ~/projects/my_awesome_plugin
pip install -e .

# Verify it's loaded
structum plugins list
```

### Step 5: Publish to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

Users can then install your plugin with:

```bash
pip install structum-my-awesome-plugin
```

---

## Plugin Structure Reference

### Required Files

#### `plugin.py`

```python
import typer
from structum.plugins.sdk import PluginBase
from .commands import main


class MyPlugin(PluginBase):
    """My plugin description."""

    # Required attributes
    name = "my-plugin"
    version = "1.0.0"
    category = "utility"  # analysis, export, formatting, utility

    # Optional attributes
    description = "What this plugin does"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources (called once on load)."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands."""
        app.add_typer(main.app, name="my-plugin")
```

#### `__init__.py`

Keep this clean – only export the plugin class:

```python
from .plugin import MyPlugin

__all__ = ["MyPlugin"]
```

#### `commands/main.py`

Define your CLI commands:

```python
import typer

app = typer.Typer(help="My plugin commands.")


@app.command("run")
def run_command(
    path: str = typer.Argument(".", help="Path to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Run the main plugin action."""
    from ..core.logic import process

    result = process(path, verbose)
    typer.echo(result)
```

#### `core/logic.py`

Keep business logic separate from CLI:

```python
def process(path: str, verbose: bool) -> str:
    """Core processing logic."""
    # Your implementation here
    return f"Processed {path}"
```

---

## Plugin Validation

When a plugin is loaded, Structum validates:

| Attribute | Requirement |
|-----------|-------------|
| `name` | Must be a non-empty string |
| `version` | Must be a non-empty string |
| `category` | Must be one of: `analysis`, `export`, `formatting`, `utility` |
| `setup()` | Must be implemented |

Invalid plugins are rejected with a descriptive error message.

---

## Plugin Configuration

Plugins can be enabled/disabled via CLI:

```bash
structum plugins disable my-plugin  # Disable
structum plugins enable my-plugin   # Enable
structum plugins list               # Check status
```

Configuration is stored in `~/.config/structum/config.json`.

---

## Best Practices

1. **Separation of Concerns**: Keep CLI code in `commands/`, logic in `core/`
2. **Type Hints**: Use type hints for all functions
3. **Error Handling**: Use Typer's error handling and Rich for output
4. **Testing**: Write tests for your core logic
5. **Documentation**: Include docstrings and a README

```

## `docs/architecture/modules.md` {#docs-architecture-modules-md}

```md
# Modules

## Core (`src/structum/core/`)
Contains the business logic of the application. These modules are independent of the CLI interface.

*   `tree.py`: Logic for directory traversal and visualization.
*   `archive.py`: Logic for collecting files and generating markdown archives.
*   `clean.py`: Logic for cleaning artifacts.
*   `docs.py`: Logic for documentation management.
*   `config.py`: Configuration management and persistence.

## CLI (`src/structum/cli/`)
Handles the user interface using Typer.

*   `main.py`: Entry point and command registration.
*   `commands/`: Individual command definitions.

## Plugins (`src/structum/plugins/`)
Manages the plugin system.

*   `sdk.py`: Plugin SDK defining `PluginBase` class.
*   `registry.py`: Central plugin registry.
*   `loader.py`: Plugin discovery and loading.
*   `sample/`: Example plugin demonstrating the architecture.

```

## `docs/architecture/index.md` {#docs-architecture-index-md}

```md
# Architecture

Structum follows a modular architecture designed for maintainability and extensibility.

## Sections

*   [Modules](modules.md): Overview of the core modules.
*   [Design Principles](design-principles.md): Key principles guiding the development.

```

## `docs/architecture/design-principles.md` {#docs-architecture-design-principles-md}

```md
# Design Principles

## Separation of Concerns
We strictly separate business logic (Core) from interface logic (CLI). This ensures that the core functionality can be reused in other contexts (e.g., scripts, other tools) without dependencies on the CLI framework.

## Modularity
Each feature is encapsulated in its own module. This applies to both the Core and CLI layers.

## Extensibility
The plugin system allows adding new commands without modifying the core codebase.

```

## `tests/conftest.py` {#tests-conftest-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from typing import Generator

@pytest.fixture(scope="session")
def test_session_id() -> Generator[str, None, None]:
    """Example session-scoped fixture."""
    yield "session-123"

```

## `tests/unit/test_version.py` {#tests-unit-test_version-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import structum

def test_version():
    """Verify that the package has a version attribute."""
    assert structum.__version__ is not None
    assert isinstance(structum.__version__, str)

```

## `tests/unit/conftest.py` {#tests-unit-conftest-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest

@pytest.fixture
def mock_fs():
    """Placeholder for a mock filesystem fixture (e.g. pyfakefs)."""
    return "mock_fs_placeholder"

```

## `tests/unit/plugins/test_skeleton.py` {#tests-unit-plugins-test_skeleton-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from pathlib import Path
import pytest
from structum.plugins import skeleton

class TestSkeleton:
    """Tests for plugin skeleton generation."""

    def test_generate_plugin_skeleton(self, tmp_path):
        """Test generating a new plugin structure."""
        output = tmp_path / "plugins"
        name = "my-test-plugin"
        category = "analysis"
        
        plugin_path = skeleton.generate_plugin_skeleton(name, output, category)
        
        assert plugin_path.exists()
        assert (plugin_path / "plugin.py").exists()
        assert (plugin_path / "commands" / "main.py").exists()
        assert (plugin_path / "core" / "logic.py").exists()
        
        # Check content replacement
        content = (plugin_path / "plugin.py").read_text()
        assert 'name = "my-test-plugin"' in content
        assert 'class MyTestPluginPlugin(PluginBase):' in content # CamelCase check
        assert f'category = "{category}"' in content

    def test_generate_plugin_skeleton_default_category(self, tmp_path):
        """Test default category usage."""
        output = tmp_path / "plugins"
        name = "simple"
        
        plugin_path = skeleton.generate_plugin_skeleton(name, output)
        
        content = (plugin_path / "plugin.py").read_text()
        assert 'category = "utility"' in content

```

## `tests/unit/plugins/test_loader.py` {#tests-unit-plugins-test_loader-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import MagicMock, patch
import pytest
import typer
from structum.plugins import loader
from structum.plugins.registry import PluginRegistry

class TestLoader:
    """Tests for plugin loading."""

    @pytest.fixture(autouse=True)
    def clean_registry(self):
        PluginRegistry.clear()
        yield
        PluginRegistry.clear()

    def test_load_builtin_plugins(self):
        """Test loading built-in plugins."""
        app = typer.Typer()
        
        # We assume 'sample' is the builtin plugin
        # We need to mock get_plugin_enabled if we check command registration
        # But load_builtin_plugins registers and loads it
        
        loader.load_builtin_plugins(app)
        
        assert "sample" in PluginRegistry.list_plugins()
        # Check if loaded
        assert PluginRegistry.get("sample") is not None

    @patch("structum.plugins.loader.entry_points")
    def test_load_entrypoint_plugins_none(self, mock_eps):
        """Test loading when no entry points exist."""
        mock_eps.return_value = []
        app = typer.Typer()
        
        loader.load_entrypoint_plugins(app)
        
        # Should be empty (assuming no builtins loaded)
        assert len(PluginRegistry.list_plugins()) == 0

    @patch("structum.plugins.loader.entry_points")
    def test_load_entrypoint_plugins_valid(self, mock_eps):
        """Test loading valid entry point plugin."""
        # Mock entry point
        mock_ep = MagicMock()
        mock_ep.name = "external-plugin"
        # Create a dummy plugin class
        from structum.plugins.sdk import PluginBase
        class ExternalPlugin(PluginBase):
            name = "external-plugin"
            version = "0.0.1"
            def setup(self): pass
            def register_commands(self, app): pass
            
        mock_ep.load.return_value = ExternalPlugin
        mock_eps.return_value = [mock_ep]
        
        app = typer.Typer()
        loader.load_entrypoint_plugins(app)
        
        assert "external-plugin" in PluginRegistry.list_plugins()
        assert PluginRegistry.get("external-plugin") is not None

```

## `tests/unit/plugins/test_registry.py` {#tests-unit-plugins-test_registry-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import PluginBase
import typer

class ValidPlugin(PluginBase):
    name = "valid-plugin"
    version = "1.0.0"
    category = "utility"
    description = "A valid plugin"
    author = "Test"
    
    def setup(self): pass
    def register_commands(self, app): pass

class InvalidPluginNoName(PluginBase):
    version = "1.0.0"
    def setup(self): pass
    def register_commands(self, app): pass

class TestPluginRegistry:
    """Tests for PluginRegistry."""

    @pytest.fixture(autouse=True)
    def clean_registry(self):
        """Clean registry before each test."""
        PluginRegistry.clear()
        yield
        PluginRegistry.clear()

    def test_register_valid_plugin(self):
        """Test registering a valid plugin."""
        PluginRegistry.register(ValidPlugin)
        
        # Check it's registered
        assert "valid-plugin" in PluginRegistry.list_plugins()
        info = PluginRegistry.list_plugins()["valid-plugin"]
        assert info["version"] == "1.0.0"

    def test_register_invalid_plugin_type(self):
        """Test registering something that isn't a PluginBase."""
        with pytest.raises(TypeError):
            PluginRegistry.register(object) # type: ignore

    def test_register_invalid_plugin_missing_attr(self):
        """Test registering plugin with missing attributes."""
        with pytest.raises(ValueError, match="must have a 'name'"):
            PluginRegistry.register(InvalidPluginNoName)

    def test_get_plugin(self):
        """Test getting plugin instance."""
        PluginRegistry.register(ValidPlugin)
        
        # Before loading, get returns None
        assert PluginRegistry.get("valid-plugin") is None
        
        # Load all
        PluginRegistry.load_all()
        
        # Now get returns instance
        instance = PluginRegistry.get("valid-plugin")
        assert instance is not None
        assert isinstance(instance, ValidPlugin)

    def test_list_by_category(self):
        """Test listing plugins by category."""
        PluginRegistry.register(ValidPlugin)
        
        categories = PluginRegistry.list_by_category()
        assert "utility" in categories
        assert "valid-plugin" in categories["utility"]

```

## `tests/unit/cli/test_main.py` {#tests-unit-cli-test_main-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from typer.testing import CliRunner
from structum.cli.main import app
from structum import __version__

runner = CliRunner()

def test_version_command():
    """Test the version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert f"v{__version__}" in result.stdout

def test_info_command():
    """Test the info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "Structum CLI" in result.stdout
    assert "Python" in result.stdout

```

## `tests/unit/cli/commands/test_clean_cmd.py` {#tests-unit-cli-commands-test_clean_cmd-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch
from typer.testing import CliRunner
from structum.cli.commands.clean import clean_command
import typer

runner = CliRunner()
app = typer.Typer()
app.command()(clean_command)

class TestCleanCommand:
    """Tests for clean CLI command."""

    @patch("structum.cli.commands.clean.clean_pycache")
    def test_clean_command_defaults(self, mock_clean, tmp_path):
        """Test clean command with defaults."""
        result = runner.invoke(app, [str(tmp_path)])
        assert result.exit_code == 0
        mock_clean.assert_called_with(tmp_path, verbose=True, skip_venv=False)

    @patch("structum.cli.commands.clean.clean_pycache")
    def test_clean_command_options(self, mock_clean, tmp_path):
        """Test clean command options."""
        result = runner.invoke(app, [str(tmp_path), "--quiet", "--skip-venv"])
        assert result.exit_code == 0
        mock_clean.assert_called_with(tmp_path, verbose=False, skip_venv=True)

```

## `tests/unit/cli/commands/test_plugins_cmd.py` {#tests-unit-cli-commands-test_plugins_cmd-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch, MagicMock
from typer.testing import CliRunner
import pytest
from structum.cli.commands.plugins import app
from structum.plugins.sdk import PluginBase

runner = CliRunner()

class TestPluginsCommand:
    """Tests for plugins CLI commands."""

    @patch("structum.cli.commands.plugins.PluginRegistry")
    @patch("structum.core.config.get_plugin_enabled")
    def test_list_plugins(self, mock_enabled, mock_registry):
        """Test listing plugins."""
        mock_registry.list_plugins.return_value = {
            "test-plugin": {
                "version": "1.0",
                "category": "utility",
                "description": "Test",
                "author": "Me"
            }
        }
        mock_enabled.return_value = True
        
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0
        assert "test-plugin" in result.stdout
        assert "enabled" in result.stdout

    @patch("structum.cli.commands.plugins.PluginRegistry")
    def test_info_plugin(self, mock_registry):
        """Test getting plugin info."""
        mock_plugin = MagicMock()
        mock_plugin.name = "test-plugin"
        mock_plugin.description = "My Desc"
        mock_plugin.category = "utility"
        mock_plugin.version = "1.0"
        mock_plugin.author = "Me"
        mock_registry.get.return_value = mock_plugin
        
        result = runner.invoke(app, ["info", "test-plugin"])
        assert result.exit_code == 0
        assert "My Desc" in result.stdout

    @patch("structum.cli.commands.plugins.PluginRegistry")
    @patch("structum.core.config.set_plugin_enabled")
    def test_enable_plugin(self, mock_set, mock_registry):
        """Test enabling a plugin."""
        mock_registry.list_plugins.return_value = {"test-plugin": {}}
        
        result = runner.invoke(app, ["enable", "test-plugin"])
        assert result.exit_code == 0
        
        # Note: Depending on where set_plugin_enabled is patched (source vs destination)
        # Plugins CLI imports it locally: from structum.core.config import set_plugin_enabled
        # So we patch source: structum.core.config.set_plugin_enabled
        mock_set.assert_called_with("test-plugin", True)
        assert "enabled" in result.stdout

    def test_new_plugin_generator(self, tmp_path):
        """Test generating a new plugin."""
        # Patch the source since it is imported inside the function
        with patch("structum.plugins.skeleton.generate_plugin_skeleton") as mock_gen:
            mock_gen.return_value = tmp_path / "my-plugin"
            
            # Simulate "outside" structum project by creating a bare temp dir
            with runner.isolated_filesystem(temp_dir=tmp_path):
                result = runner.invoke(app, ["new", "my-plugin"])
                
                assert result.exit_code == 0
                mock_gen.assert_called_once()
                assert mock_gen.call_args[0][0] == "my-plugin"
                assert "Plugin skeleton created" in result.stdout

    def test_new_plugin_invalid_category(self):
        """Test invalid category."""
        result = runner.invoke(app, ["new", "my-plugin", "--category", "invalid"])
        assert result.exit_code == 0 # Typer defaults to 0 but prints error if not Exception
        assert "Invalid category" in result.stdout

```

## `tests/unit/cli/commands/test_archive_cmd.py` {#tests-unit-cli-commands-test_archive_cmd-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch
from typer.testing import CliRunner
import pytest
from structum.cli.commands.archive import archive_command
import typer

runner = CliRunner()
app = typer.Typer()
app.command()(archive_command)

class TestArchiveCommand:
    """Tests for archive CLI command wrapper."""

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_basic(self, mock_create, tmp_path):
        """Test basic invocation of archive command."""
        result = runner.invoke(app, [str(tmp_path)])
        
        assert result.exit_code == 0
        mock_create.assert_called_once()
        # Check defaults
        call_args = mock_create.call_args[1]
        assert call_args["extensions"] is None
        assert call_args["toc"] is True
        assert call_args["include_tree"] is True

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_options(self, mock_create, tmp_path):
        """Test passing options."""
        result = runner.invoke(app, [
            str(tmp_path),
            "--output", "out.md",
            "--ext", "py",
            "--ext", "md",
            "--ignore", ".git,dist",
            "--split-folder",
            "--no-toc",
            "--no-tree"
        ])
        
        assert result.exit_code == 0
        call_args = mock_create.call_args[1]
        assert call_args["output"].name == "out.md"
        assert sorted(call_args["extensions"]) == ["md", "py"]
        assert sorted(call_args["ignore_dirs"]) == [".git", "dist"]
        assert call_args["split_by_folder"] is True
        assert call_args["toc"] is False
        assert call_args["include_tree"] is False

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_error_handling(self, mock_create, tmp_path):
        """Test handling of ValueError from core logic."""
        mock_create.side_effect = ValueError("Test Error")
        result = runner.invoke(app, [str(tmp_path)])
        
        assert result.exit_code == 1
        assert "Error:" in result.stdout
        assert "Test Error" in result.stdout

```

## `tests/unit/core/test_tree.py` {#tests-unit-core-test_tree-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from unittest.mock import patch
from structum.core import tree

class TestTree:
    """Tests for directory tree visualization."""

    @pytest.fixture
    def workspace(self, tmp_path):
        """Create a temporary workspace with files and folders."""
        # Create structure:
        # /root
        # ├── file1.txt
        # ├── src/
        # │   ├── main.py
        # │   └── utils.py
        # ├── docs/
        # │   └── readme.md
        # ├── .hidden/
        # └── .gitignore
        
        fs = tmp_path
        (fs / "file1.txt").touch()
        (fs / ".gitignore").touch()
        
        src = fs / "src"
        src.mkdir()
        (src / "main.py").touch()
        (src / "utils.py").touch()
        
        docs = fs / "docs"
        docs.mkdir()
        (docs / "readme.md").touch()
        
        hidden = fs / ".hidden"
        hidden.mkdir()
        
        return fs

    def test_build_tree_basic(self, workspace):
        """Test building a basic tree."""
        result = tree.build_tree(workspace)
        assert result is not None
        assert str(workspace.name) in str(result.label)

    def test_build_tree_extensions_filter(self, workspace):
        """Test filtering by extension."""
        result = tree.build_tree(workspace, extensions=[".py"])
        
        # Should contain python files
        # We need to capture the output or inspect the tree structure/labels
        # Capturing rich output to string is easier for content verification
        ascii_tree = tree.get_tree_ascii(workspace, extensions=[".py"])
        
        assert "main.py" in ascii_tree
        assert "utils.py" in ascii_tree
        assert "file1.txt" not in ascii_tree
        assert "readme.md" not in ascii_tree

    def test_build_tree_ignore_hidden(self, workspace):
        """Test ignoring hidden files."""
        result = tree.get_tree_ascii(workspace, ignore_hidden=True)
        assert ".gitignore" not in result
        assert ".hidden" not in result

    def test_build_tree_show_hidden(self, workspace):
        """Test showing hidden files."""
        result = tree.get_tree_ascii(workspace, ignore_hidden=False)
        assert ".gitignore" in result
        # Check if .hidden directory is shown (might depend on implementation details of empty dir behavior)
        if not (workspace / ".hidden").iterdir(): # Empty hidden dir
             # If empty dirs are not ignored by default in get_tree_ascii (it forces ignore_empty=True)
             # Let's check build_tree behavior directly
             t = tree.build_tree(workspace, ignore_hidden=False, ignore_empty=False)
             # Rich Tree structure inspection is complex, relying on visual output or traversal
             pass 

    def test_build_tree_max_depth(self, workspace):
        """Test max depth limit."""
        # Depth 0 should only show root (managed by build_tree logic mainly, but rich tree rendering handles display)
        # build_tree logic: current_depth > max_depth -> return False
        
        # Depth 1: root + immediate children
        result = tree.get_tree_ascii(workspace, max_depth=1)
        assert "src" in result
        assert "file1.txt" in result
        # Grandchildren should NOT be visible
        # Note: In standard tree output, folders are listed, but their content might be hidden
        # If max_depth=1, src/main.py (depth 2) should NOT be there
        assert "main.py" not in result

    def test_get_tree_ascii_returns_string(self, workspace):
        """Test that get_tree_ascii returns a non-empty string."""
        output = tree.get_tree_ascii(workspace)
        assert isinstance(output, str)
        assert len(output) > 0

    @patch("structum.core.tree.console.print")
    def test_print_tree_stats(self, mock_print, workspace):
        """Test print_tree with stats enabled."""
        tree.print_tree(workspace, show_stats=True)
        # Check that stats are printed
        # The stats line is likely the LAST print call
        found_stats = False
        for call in mock_print.call_args_list:
            if not call.args:
                continue
            arg = str(call.args[0])
            # "3 directories, 4 files" pattern
            if "directory" in arg or "directories" in arg:
                if "file" in arg or "files" in arg:
                    found_stats = True
        assert found_stats

    def test_build_tree_invalid_dir(self, tmp_path):
        """Test build_tree with invalid directory."""
        with pytest.raises(NotADirectoryError):
            tree.build_tree(tmp_path / "nonexistent")
            
    def test_build_tree_permission_error(self, workspace):
        """Test handling of PermissionError."""
        # Using mock to simulate permission error on iterdir
        with patch("pathlib.Path.iterdir", side_effect=PermissionError):
             # Recursion starts at root. If root fails, what happens?
             # build_tree resolves directory. But _populate_branch calls iterdir.
             # If root fails iterdir:
             result = tree.build_tree(workspace)
             # The error is caught and added to tree as "[Access Denied]"
             assert result is not None
             # Check if text contains access denied
             # Rich Tree structure complex to inspect string content directly without rendering
             # But we can verify it ran without raising exception

```

## `tests/unit/core/test_archive.py` {#tests-unit-core-test_archive-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from structum.core import archive

class TestArchive:
    """Tests for code archiving functionality."""

    @pytest.fixture
    def workspace(self, tmp_path):
        """Create a sample workspace."""
        fs = tmp_path / "project"
        fs.mkdir()
        
        (fs / "main.py").write_text("print('hello')")
        (fs / "readme.md").write_text("# Readme")
        
        src = fs / "src"
        src.mkdir()
        (src / "utils.py").write_text("def util(): pass")
        
        ignored = fs / ".git"
        ignored.mkdir()
        (ignored / "config").write_text("config")

        (fs / "READ.txt").write_text("read me")
        
        my_ignored = fs / "ignored"
        my_ignored.mkdir()
        (my_ignored / "ignored.py").write_text("pass")

        return fs

    def test_gather_files_basic(self, workspace):
        """Test gathering files with explicit extensions."""
        # Note: gather_files requires explicit extensions currently
        files = archive.gather_files(workspace, extensions=[".py", ".md", ".txt"])
        
        rel_paths = {str(r) for r, a in files}
        assert "main.py" in rel_paths
        assert "readme.md" in rel_paths
        assert "src/utils.py" in rel_paths
        assert ".git/config" not in rel_paths # Default ignore

    def test_gather_files_extension_filter(self, workspace):
        """Test gathering files with specific extension filter."""
        files = archive.gather_files(workspace, extensions=[".py"])
        
        rel_paths = {str(r) for r, a in files}
        assert "main.py" in rel_paths
        assert "src/utils.py" in rel_paths
        assert "readme.md" not in rel_paths

    @patch("structum.core.archive.get_tree_ascii")
    def test_create_archive_single(self, mock_tree, workspace, tmp_path):
        """Test creating a single archive file."""
        mock_tree.return_value = "TREE"
        output = tmp_path / "archive.md"
        
        archive.create_archive(
            root=workspace,
            output=output,
            extensions=[".py", ".md"],
            verbose=False
        )
        
        assert output.exists()
        content = output.read_text()
        assert "Code Archive" in content
        assert "## `main.py`" in content
        assert "## `src/utils.py`" in content
        assert "TREE" in content # Tree included by default

    def test_gather_files_default_all(self, workspace):
        """Test gathering all files when extensions is None."""
        files = archive.gather_files(workspace, extensions=None)
        # Should find src/main.py, READ.txt, ignored/ignored.py (if not ignored)
        # Default ignores: .git, etc.
        # "ignored" dir is not in default ignore list unless we put it there
        
        # We expect: src/main.py, READ.txt, ignored/ignored.py
        # But wait, gather_files uses IGNORE_DIRS_DEFAULT if ignore_dirs is None.
        
        found = {str(f[0]) for f in files}
        assert "main.py" in found
        assert "src/utils.py" in found
        assert "READ.txt" in found
        # ignored.py is in 'ignored' folder. Is 'ignored' in defaults? No.
        assert "ignored/ignored.py" in found
        assert ".git/config" not in found # Default ignore

    def test_create_archive_tree_filtering(self, workspace, tmp_path):
        """Test that tree output respects filters."""
        output = tmp_path / "archive.md"
        # We ignore "ignored" directory explicitly
        archive.create_archive(
            workspace, 
            output, 
            extensions=None, 
            ignore_dirs=["ignored"],
            include_tree=True
        )
        
        content = output.read_text(encoding="utf-8")
        # Tree should NOT contain "ignored" folder
        assert "ignored" not in content
        # But should contain src
        assert "src" in content

    def test_create_archive_output_is_dir(self, workspace, tmp_path):
        """Test robust handling when output is an existing directory."""
        out_dir = tmp_path / "out_dir"
        out_dir.mkdir()
        
        # Call with output=out_dir (directory) and single mode
        archive.create_archive(workspace, out_dir, extensions=[".py"])
        
        expected_file = out_dir / "archive.md"
        assert expected_file.exists()

    def test_create_archive_split_by_folder(self, workspace, tmp_path):
        """Test splitting archive by folder."""
        output_dir = tmp_path / "output"
        
        archive.create_archive(
            root=workspace,
            output=output_dir,
            extensions=[".py", ".md"],
            split_by_folder=True,
            verbose=False
        )
        
        # Should have root.md (for top level) and src.md
        assert (output_dir / "root.md").exists()
        assert (output_dir / "src.md").exists()
        
        root_content = (output_dir / "root.md").read_text()
        assert "main.py" in root_content
        assert "readme.md" in root_content
        
        src_content = (output_dir / "src.md").read_text()
        assert "src/utils.py" in src_content

    def test_create_archive_split_by_type(self, workspace, tmp_path):
        """Test splitting archive by file extension."""
        output_dir = tmp_path / "output_type"
        
        archive.create_archive(
            root=workspace,
            output=output_dir,
            extensions=[".py", ".md"],
            split_by_type=True,
            verbose=False
        )
        
        assert (output_dir / "py.md").exists()
        assert (output_dir / "md.md").exists()
        
        py_content = (output_dir / "py.md").read_text()
        assert "## `main.py`" in py_content
        assert "## `src/utils.py`" in py_content
        assert "## `readme.md`" not in py_content # Content block should not exist

    def test_create_archive_conflict_error(self, workspace, tmp_path):
        """Test error when both split options are used."""
        with pytest.raises(ValueError, match="Cannot use both"):
            archive.create_archive(
                root=workspace,
                output=tmp_path,
                extensions=None,
                split_by_folder=True,
                split_by_type=True
            )

```

## `tests/unit/core/test_config.py` {#tests-unit-core-test_config-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import json
from pathlib import Path
import pytest
from structum.core import config

class TestConfig:
    """Tests for configuration management."""

    @pytest.fixture(autouse=True)
    def mock_config_paths(self, tmp_path, monkeypatch):
        """Redirect config paths to a temporary directory."""
        mock_dir = tmp_path / ".config" / "structum"
        mock_file = mock_dir / "config.json"
        
        monkeypatch.setattr(config, "CONFIG_DIR", mock_dir)
        monkeypatch.setattr(config, "CONFIG_FILE", mock_file)
        
        return mock_dir, mock_file

    def test_load_config_defaults(self):
        """Test loading config when file doesn't exist."""
        data = config.load_config()
        assert data == {"plugins": {}}

    def test_save_and_load_config(self):
        """Test saving and then loading configuration."""
        test_data = {"plugins": {"test_plugin": {"enabled": True}}}
        config.save_config(test_data)
        
        loaded = config.load_config()
        assert loaded == test_data

    def test_get_plugin_enabled(self):
        """Test checking if a plugin is enabled."""
        config.set_plugin_enabled("my_plugin", True)
        assert config.get_plugin_enabled("my_plugin") is True
        
        config.set_plugin_enabled("my_plugin", False)
        assert config.get_plugin_enabled("my_plugin") is False

    def test_get_plugin_enabled_default(self):
        """Test default enabled state for unknown plugins."""
        # Current implementation defaults to True (according to code reading)
        # enabled: bool = config.get("plugins", {}).get(name, {}).get("enabled", True)
        assert config.get_plugin_enabled("unknown_plugin") is True

```

## `tests/unit/core/test_clean.py` {#tests-unit-core-test_clean-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from pathlib import Path
from structum.core.clean import clean_pycache

class TestClean:
    """Tests for clean utilities."""

    def test_clean_pycache_basic(self, tmp_path):
        """Test basic removal of __pycache__ directories."""
        # Setup
        d1 = tmp_path / "d1"
        d1.mkdir()
        
        pyc1 = d1 / "__pycache__"
        pyc1.mkdir()
        (pyc1 / "foo.pyc").touch()
        
        src = tmp_path / "src"
        src.mkdir()
        pyc2 = src / "__pycache__"
        pyc2.mkdir()
        
        # Run
        removed = clean_pycache(tmp_path, verbose=False)
        
        assert removed == 2
        assert not pyc1.exists()
        assert not pyc2.exists()
        assert d1.exists()
        assert src.exists()

    def test_clean_pycache_skip_venv(self, tmp_path):
        """Test skipping virtual environments."""
        venv = tmp_path / ".inv" # Not a standard name
        venv.mkdir()
        (venv / "__pycache__").mkdir()
        
        standard_venv = tmp_path / ".venv"
        standard_venv.mkdir()
        (standard_venv / "__pycache__").mkdir()
        
        # Run with skip_venv=True
        removed = clean_pycache(tmp_path, verbose=False, skip_venv=True)
        
        # .inv is NOT skipped (unless configured elsewhere, but cleaner uses hardcoded set)
        # .venv SHOULD be skipped
        
        # Wait, VENV_DIRS in clean.py default set
        # VENV_DIRS = {'.env', 'env', 'venv', '.venv', 'virtualenv'}
        
        # .inv is NOT in default list, so it should be cleaned
        # .venv IS in list, so it should be skipped
        
        assert not (venv / "__pycache__").exists()
        assert (standard_venv / "__pycache__").exists()

```

## `tests/unit/core/test_utils.py` {#tests-unit-core-test_utils-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from structum.core.utils import normalize_extensions, IGNORE_DIRS_DEFAULT

class TestUtils:
    """Tests for core utility functions."""

    @pytest.mark.parametrize(
        "input_exts,expected",
        [
            (["py", ".txt", "MD"], {".py", ".txt", ".md"}),
            ([""], set()),
            (["  "], set()),
            (None, set()),
            ([], set()),
            ([".py", "py"], {".py"}),  # Deduplication
        ],
    )
    def test_normalize_extensions(self, input_exts, expected):
        """Verify extension normalization logic."""
        assert normalize_extensions(input_exts) == expected

    def test_ignore_dirs_default(self):
        """Verify default ignore directories contain common patterns."""
        assert ".git" in IGNORE_DIRS_DEFAULT
        assert "__pycache__" in IGNORE_DIRS_DEFAULT
        assert "node_modules" in IGNORE_DIRS_DEFAULT

```

## `tests/unit/core/test_docs.py` {#tests-unit-core-test_docs-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import subprocess
import sys
from unittest.mock import MagicMock, patch

import pytest
from structum.core import docs

class TestDocs:
    """Tests for documentation management."""

    @patch("subprocess.run")
    def test_serve_docs_success(self, mock_run):
        """Test serving docs successfully."""
        mock_run.return_value.returncode = 0
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost:8000")
        
        assert exc.value.code == 0
        mock_run.assert_called_once_with(
            ["mkdocs", "serve", "--dev-addr", "localhost:8000"],
            check=True
        )

    @patch("subprocess.run")
    def test_serve_docs_error(self, mock_run):
        """Test serving docs failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost:8000")
            
        assert exc.value.code == 1

    @patch("subprocess.run")
    def test_deploy_docs_success(self, mock_run):
        """Test deploying docs successfully."""
        mock_run.return_value.returncode = 0
        
        with pytest.raises(SystemExit) as exc:
            docs.deploy_docs(message="update", force=True)
            
        assert exc.value.code == 0
        mock_run.assert_called_once()
        args = mock_run.call_args[0][0]
        assert "gh-deploy" in args
        assert "--message" in args
        assert "--force" in args

    @patch("subprocess.run")
    def test_serve_docs_not_found(self, mock_run):
        """Test serve_docs when mkdocs is missing."""
        mock_run.side_effect = FileNotFoundError
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost")
        
        assert exc.value.code == 1

    @patch("subprocess.run")
    def test_deploy_docs_not_found(self, mock_run):
        """Test deploy_docs when mkdocs is missing."""
        mock_run.side_effect = FileNotFoundError
        
        with pytest.raises(SystemExit) as exc:
            docs.deploy_docs(message=None, force=False)
            
        assert exc.value.code == 1

```

## `LICENSES/Apache-2.0.txt` {#LICENSES-Apache-2-0-txt}

```txt

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## `.reuse/dep5` {#-reuse-dep5}

```text
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: Structum
Upstream-Contact: PythonWoods <pythonwoods@example.com>
Source: https://github.com/PythonWoods/structum

Files: LICENSES/Apache-2.0.txt
Copyright: 2004 The Apache Software Foundation
License: Apache-2.0

```

## `.github/dependabot.yml` {#-github-dependabot-yml}

```yml
# SPDX-License-Identifier: Apache-2.0

version: 2

updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
      day: "monday"
      time: "03:00"
      timezone: "Europe/Rome"
    open-pull-requests-limit: 10
    labels: ["dependencies"]
    commit-message:
      prefix: "chore(deps)"
      include: "scope"
    versioning-strategy: "increase-if-necessary"

    groups:
      cli-tools:
        patterns:
          - "typer*"
          - "rich*"
      dev-tools:
        dependency-type: "development"
        patterns:
          - "ruff*"
          - "black*"
          - "mypy*"
      testing:
        dependency-type: "development"
        patterns:
          - "pytest*"
          - "httpx*"

  - package-ecosystem: github-actions
    directory: "/"
    schedule:
      interval: "monthly"
      time: "03:00"
      day: "sunday"
    labels: ["ci", "github-actions"]

```

## `.github/labeler.yml` {#-github-labeler-yml}

```yml
# SPDX-License-Identifier: Apache-2.0

# Documentazione
documentation:
  - "*.md"
  - "docs/**"
  - "LICENSE"

# CI/CD e Workflow GitHub
ci:
  - ".github/**"

# Dipendenze e Configurazione Progetto
dependencies:
  - "pyproject.toml"
  - "poetry.lock"
  - "requirements.txt"
  - "setup.py"

# Test
tests:
  - "tests/**"
  - "**/conftest.py"

# Codice Sorgente (Core)
core:
  - "src/structum/core/**"
  - "src/structum/__init__.py"

# Codice Sorgente (CLI)
cli:
  - "src/structum/cli.py"
  - "src/structum/main.py" # Legacy fallback

# Codice Sorgente (Plugins)
plugins:
  - "src/structum/plugins/**"

# Configurazione Generica
config:
  - "**/*.yml"
  - "**/*.yaml"
  - ".gitignore"
  - ".editorconfig"
```

## `.github/workflows/main_ci.yml` {#-github-workflows-main_ci-yml}

```yml
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.12"

    - name: Install build backend
      run: pip install hatchling

    - name: Build
      run: python -m hatchling build

```

## `src/structum/__main__.py` {#src-structum-__main__-py}

```py
"""Entry point for Structum.

This module allows running Structum directly using:

    python -m structum

invoking the Typer application defined in :mod:`structum.cli`.
"""

from __future__ import annotations

from .cli.main import app


def main() -> None:
    """Executes the main Typer application."""
    app()


if __name__ == "__main__":
    main()

```

## `src/structum/__about__.py` {#src-structum-__about__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

__version__ = "0.0.1"

```

## `src/structum/__init__.py` {#src-structum-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Structum - Visualization and management of directory trees.

This package provides tools for visualizing and managing directory structures
with support for multiple themes, filtering, and export formats.
"""

from .__about__ import __version__

__all__ = ["__version__"]

```

## `src/structum/plugins/registry.py` {#src-structum-plugins-registry-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Registry for Structum."""


from structum.plugins.sdk import CATEGORIES, PluginBase


class PluginRegistry:
    """Central registry for all plugins."""

    _plugins: dict[str, type[PluginBase]] = {}
    _instances: dict[str, PluginBase] = {}

    @classmethod
    def register(cls, plugin_cls: type[PluginBase]) -> None:
        """Register a plugin class.

        Args:
            plugin_cls: The plugin class to register.

        Raises:
            TypeError: If plugin doesn't inherit from PluginBase.
            ValueError: If plugin is missing required attributes.
        """
        if not issubclass(plugin_cls, PluginBase):
            raise TypeError(f"Plugin {plugin_cls} must inherit from PluginBase")

        # Validate required attributes
        if not hasattr(plugin_cls, "name") or not isinstance(plugin_cls.name, str):
            raise ValueError(f"Plugin {plugin_cls} must have a 'name' string attribute")

        if not hasattr(plugin_cls, "version") or not isinstance(plugin_cls.version, str):
            raise ValueError(f"Plugin {plugin_cls} must have a 'version' string attribute")

        # Validate category
        category = getattr(plugin_cls, "category", "utility")
        if category not in CATEGORIES:
            raise ValueError(
                f"Plugin {plugin_cls} has invalid category '{category}'. "
                f"Valid categories: {', '.join(CATEGORIES.keys())}"
            )

        cls._plugins[plugin_cls.name] = plugin_cls

    @classmethod
    def get(cls, name: str) -> PluginBase | None:
        """Get an instantiated plugin by name.

        Args:
            name: The name of the plugin.

        Returns:
            The plugin instance or None if not found/loaded.
        """
        return cls._instances.get(name)

    @classmethod
    def load_all(cls) -> None:
        """Instantiate and setup all registered plugins."""
        for name, plugin_cls in cls._plugins.items():
            if name not in cls._instances:
                instance = plugin_cls()
                instance.setup()
                cls._instances[name] = instance

    @classmethod
    def list_plugins(cls) -> dict[str, dict[str, str]]:
        """List all registered plugins with metadata.

        Returns:
            Dictionary of plugin info.
        """
        return {
            name: {
                "version": plugin.version,
                "category": plugin.category,
                "description": plugin.description,
                "author": plugin.author,
            }
            for name, plugin in cls._plugins.items()
        }

    @classmethod
    def list_by_category(cls) -> dict[str, list[str]]:
        """List plugins grouped by category.

        Returns:
            Dictionary mapping category to list of plugin names.
        """
        result: dict[str, list[str]] = {}
        for name, plugin in cls._plugins.items():
            category = plugin.category
            if category not in result:
                result[category] = []
            result[category].append(name)
        return result

    @classmethod
    def clear(cls) -> None:
        """Clear registry (useful for testing)."""
        cls._plugins.clear()
        cls._instances.clear()

```

## `src/structum/plugins/skeleton.py` {#src-structum-plugins-skeleton-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin skeleton generator."""

from pathlib import Path

PLUGIN_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Package."""

from .plugin import {class_name}

__all__ = ["{class_name}"]
'''

PLUGIN_CLASS_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import main


class {class_name}(PluginBase):
    """{description}"""

    name = "{name}"
    version = "0.1.0"
    category = "{category}"
    description = "{description}"
    author = "Your Name"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(main.app, name="{name}")
'''

COMMANDS_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands Package."""
'''

COMMANDS_MAIN_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Commands."""

import typer

app = typer.Typer(help="{description}")


@app.command("hello")
def hello(name: str = "world") -> None:
    """Say hello."""
    typer.echo(f"Hello, {{name}}!")
'''

CORE_INIT_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Package."""
'''

CORE_LOGIC_TEMPLATE = '''# SPDX-License-Identifier: Apache-2.0

"""{name} Plugin Core Logic."""


def example_function() -> str:
    """Example function."""
    return "Hello from {name} plugin!"
'''


def generate_plugin_skeleton(
    name: str, output_dir: Path, category: str = "utility"
) -> Path:
    """Generate a plugin skeleton.

    Args:
        name: Plugin name (kebab-case).
        output_dir: Directory to create plugin in.
        category: Plugin category (analysis, export, formatting, utility).

    Returns:
        Path to created plugin directory.
    """
    # Convert name to class name
    class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"
    description = f"{name.replace('-', ' ').title()} plugin"

    # Create directories
    plugin_dir = output_dir / name.replace("-", "_")
    commands_dir = plugin_dir / "commands"
    core_dir = plugin_dir / "core"

    plugin_dir.mkdir(parents=True, exist_ok=True)
    commands_dir.mkdir(exist_ok=True)
    core_dir.mkdir(exist_ok=True)

    context = {
        "name": name,
        "class_name": class_name,
        "description": description,
        "category": category,
    }

    # Write files
    (plugin_dir / "__init__.py").write_text(PLUGIN_INIT_TEMPLATE.format(**context))
    (plugin_dir / "plugin.py").write_text(PLUGIN_CLASS_TEMPLATE.format(**context))
    (commands_dir / "__init__.py").write_text(COMMANDS_INIT_TEMPLATE.format(**context))
    (commands_dir / "main.py").write_text(COMMANDS_MAIN_TEMPLATE.format(**context))
    (core_dir / "__init__.py").write_text(CORE_INIT_TEMPLATE.format(**context))
    (core_dir / "logic.py").write_text(CORE_LOGIC_TEMPLATE.format(**context))

    return plugin_dir

```

## `src/structum/plugins/loader.py` {#src-structum-plugins-loader-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin loader for Structum.

This module handles the discovery and loading of both built-in and external plugins.
External plugins are discovered via the 'structum.plugins' entry point group.
"""

from importlib.metadata import entry_points

import typer
from rich.console import Console

from structum.core.config import get_plugin_enabled

from .registry import PluginRegistry

console = Console()


def load_builtin_plugins(app: typer.Typer) -> None:
    """Loads built-in plugins contained in the structum.plugins package."""
    from . import sample

    # Register the plugin class
    PluginRegistry.register(sample.SamplePlugin)

    # Initialize plugins
    PluginRegistry.load_all()

    # Register CLI commands only if plugin is enabled
    plugin = PluginRegistry.get("sample")
    if plugin and get_plugin_enabled("sample"):
        plugin.register_commands(app)


def load_entrypoint_plugins(app: typer.Typer) -> None:
    """Loads external plugins via entry points.

    Looks for entry points in the 'structum.plugins' group.
    """
    eps = entry_points(group="structum.plugins")

    if not eps:
        return

    console.print("[bold blue]🔌 Loading external plugins...[/bold blue]")

    for ep in eps:
        try:
            plugin_cls = ep.load()
            PluginRegistry.register(plugin_cls)
            console.print(f"[green]✔ Plugin loaded:[/green] {ep.name}")
        except Exception as e:
            console.print(f"[red]✘ Error loading plugin {ep.name}:[/red] {e}")

    # Initialize all loaded plugins
    PluginRegistry.load_all()

    # Register CLI commands for enabled plugins
    for name in PluginRegistry.list_plugins():
        plugin = PluginRegistry.get(name)
        if plugin and get_plugin_enabled(name):
            plugin.register_commands(app)


def load_plugins(app: typer.Typer) -> None:
    """Loads all available plugins (built-in and external)."""
    load_builtin_plugins(app)
    load_entrypoint_plugins(app)

```

## `src/structum/plugins/__init__.py` {#src-structum-plugins-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin system for Structum.

This package contains the logic for loading plugins and any built-in plugins.
"""

from .loader import load_plugins

__all__ = ["load_plugins"]

```

## `src/structum/plugins/sdk.py` {#src-structum-plugins-sdk-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin SDK for Structum."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import typer


@dataclass
class PluginConfig:
    """Configuration for a plugin."""

    enabled: bool = True
    options: dict[str, Any] = field(default_factory=dict)


# Available plugin categories
CATEGORIES = {
    "analysis": "Code analysis and metrics",
    "export": "Export and format conversion",
    "formatting": "Code formatting and style",
    "utility": "Utility and helper tools",
}


class PluginBase(ABC):
    """Base class for all Structum plugins."""

    name: str
    version: str
    category: str = "utility"  # Default category
    description: str = ""
    author: str = ""

    def __init__(self, config: PluginConfig | None = None) -> None:
        """Initialize the plugin."""
        self.config = config or PluginConfig()

    @abstractmethod
    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def process_file(self, file_path: Path) -> dict[str, Any] | None:
        """Process a single file and return metadata.

        Args:
            file_path: Path to the file to process.

        Returns:
            Dictionary containing extracted metadata or None if file is ignored.
        """
        return None

    def generate_output(self, data: dict[str, Any]) -> str | None:
        """Generate plugin-specific output.

        Args:
            data: Metadata extracted from files.

        Returns:
            String content to append to documentation or None.
        """
        return None

    def register_commands(self, app: "typer.Typer") -> None:  # noqa: B027
        """Register CLI commands for this plugin. Override in subclass."""

    def teardown(self) -> None:  # noqa: B027
        """Cleanup resources. Override in subclass if needed."""

```

## `src/structum/plugins/sample/plugin.py` {#src-structum-plugins-sample-plugin-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Definition."""

import typer

from structum.plugins.sdk import PluginBase

from .commands import hello


class SamplePlugin(PluginBase):
    """Example plugin demonstrating the plugin system."""

    name = "sample"
    version = "1.0.0"
    category = "utility"
    description = "Example plugin demonstrating the plugin system."
    author = "PythonWoods"

    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def register_commands(self, app: typer.Typer) -> None:
        """Register CLI commands for this plugin."""
        app.add_typer(hello.app, name="sample")

```

## `src/structum/plugins/sample/__init__.py` {#src-structum-plugins-sample-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Package."""

from .plugin import SamplePlugin

__all__ = ["SamplePlugin"]

```

## `src/structum/plugins/sample/commands/__init__.py` {#src-structum-plugins-sample-commands-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Commands Package."""

```

## `src/structum/plugins/sample/commands/hello.py` {#src-structum-plugins-sample-commands-hello-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Commands."""

import typer

from ..core.greeting import get_greeting

app = typer.Typer(help="Example additional commands.")

@app.command("hello")
def hello(name: str = "dev") -> None:
    """Prints a friendly greeting."""
    message = get_greeting(name)
    typer.echo(message)

```

## `src/structum/plugins/sample/core/greeting.py` {#src-structum-plugins-sample-core-greeting-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Core Logic."""

def get_greeting(name: str) -> str:
    """Generates a friendly greeting message."""
    return f"👋 Hello, {name}! This command was loaded as a plugin."

```

## `src/structum/plugins/sample/core/__init__.py` {#src-structum-plugins-sample-core-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Sample Plugin Core Package."""

```

## `src/structum/cli/main.py` {#src-structum-cli-main-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Main CLI Application.
"""

import typer
from rich.console import Console

from structum.cli.commands import archive, clean, docs, plugins, tree, info
from structum.plugins import load_plugins

# Initialize Typer app
app = typer.Typer(
    name="structum",
    help="Enterprise Code Structure & Documentation Engine.",
    add_completion=False,
    no_args_is_help=True
)

# Register commands


console = Console()

# Load plugins
load_plugins(app)

# Register commands
# Single commands use app.command()
app.command(name="tree")(tree.tree_command)
app.command(name="archive")(archive.archive_command)
app.command(name="clean")(clean.clean_command)
app.command(name="version")(info.version_command)
app.command(name="info")(info.info_command)

# Command groups use add_typer()
app.add_typer(docs.app, name="docs")  # docs serve, docs deploy
app.add_typer(plugins.app, name="plugins")  # plugins list, info, enable, disable, new

def run() -> None:
    app()

```

## `src/structum/cli/__init__.py` {#src-structum-cli-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
CLI Package.
"""

from .main import app

__all__ = ["app"]

```

## `src/structum/cli/commands/archive.py` {#src-structum-cli-commands-archive-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Archive Command.
"""

from pathlib import Path

import typer
from rich.console import Console

from structum.core.archive import create_archive

console = Console()


def parse_list_callback(value: list[str] | None) -> list[str] | None:
    """Parse comma-separated values and flatten multiple flags.
    
    Supports both:
    - Multiple flags: --ext py --ext md
    - Comma-separated: --ext py,md,js
    - Mixed: --ext py,md --ext js
    """
    if not value:
        return None
    
    result = []
    for item in value:
        # Split by comma and strip whitespace
        parts = [part.strip() for part in item.split(",") if part.strip()]
        result.extend(parts)
    
    return result if result else None


def archive_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to archive.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    output: Path = typer.Option(
        "archive.md",
        "--output", "-o",
        help="Output file path (or directory if split mode is enabled)."
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g., '-e py -e md' or '-e py,md,js').",
        callback=parse_list_callback
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude (e.g., '-i .git -i node_modules' or '-i .git,node_modules').",
        callback=parse_list_callback
    ),
    split_by_folder: bool = typer.Option(
        False,
        "--split-folder",
        help="Create a separate archive for each folder."
    ),
    split_by_type: bool = typer.Option(
        False,
        "--split-type",
        help="Create a separate archive for each file extension."
    ),
    toc: bool = typer.Option(
        True,
        "--toc/--no-toc",
        help="Include a Table of Contents."
    ),
    tree: bool = typer.Option(
        True,
        "--tree/--no-tree",
        help="Include a directory tree structure."
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Verbose output."
    ),
) -> None:
    """
    Archives source code into Markdown files.

    \b
    Features:
    * Collects files by extension
    * Generates Table of Contents (ToC)
    * Includes ASCII directory tree
    * Supports splitting by folder or file type

    \b
    Examples:
        structum archive . --output code.md --ext py
        structum archive src --split-folder --output docs/
    """
    try:
        create_archive(
            root=directory,
            output=output,
            extensions=extensions,
            ignore_dirs=ignore_dirs,
            split_by_folder=split_by_folder,
            split_by_type=split_by_type,
            toc=toc,
            include_tree=tree,
            verbose=verbose
        )
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1) from None

```

## `src/structum/cli/commands/info.py` {#src-structum-cli-commands-info-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Info and Version Commands.
"""

import platform
import sys
from rich.console import Console
from structum import __version__

console = Console()

def version_command() -> None:
    """Show the application version."""
    console.print(f"Structum CLI v{__version__}")

def info_command() -> None:
    """Show application information."""
    console.print(f"[bold]Structum CLI[/bold] v{__version__}")
    console.print(f"Python {sys.version.split()[0]}")
    console.print(f"Platform: {platform.system()} {platform.release()}")

```

## `src/structum/cli/commands/plugins.py` {#src-structum-cli-commands-plugins-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin Management CLI Commands."""

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from structum.plugins.registry import PluginRegistry
from structum.plugins.sdk import CATEGORIES

app = typer.Typer(help="Manage plugins.")
console = Console()


@app.command("list")
def list_plugins() -> None:
    """List all installed plugins."""
    from structum.core.config import get_plugin_enabled

    plugins = PluginRegistry.list_plugins()

    if not plugins:
        console.print("[yellow]No plugins found.[/yellow]")
        return

    table = Table(title="Installed Plugins")
    table.add_column("Name", style="cyan")
    table.add_column("Category", style="yellow")
    table.add_column("Version", style="green")
    table.add_column("Status")
    table.add_column("Description")

    for name, info in plugins.items():
        enabled = get_plugin_enabled(name)
        status = "[green]enabled[/green]" if enabled else "[red]disabled[/red]"
        table.add_row(
            name,
            info["category"],
            info["version"],
            status,
            info["description"],
        )

    console.print(table)


@app.command("info")
def plugin_info(name: str) -> None:
    """Show detailed information about a plugin."""
    plugin = PluginRegistry.get(name)

    if not plugin:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    console.print(f"[bold cyan]Plugin:[/bold cyan] {plugin.name}")
    console.print(f"[bold yellow]Category:[/bold yellow] {plugin.category}")
    console.print(f"[bold green]Version:[/bold green] {plugin.version}")
    console.print(f"[bold]Author:[/bold] {plugin.author}")
    console.print(f"[bold]Description:[/bold] {plugin.description}")


@app.command("enable")
def enable_plugin(name: str) -> None:
    """Enable a plugin."""
    from structum.core.config import set_plugin_enabled

    plugins = PluginRegistry.list_plugins()
    if name not in plugins:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    set_plugin_enabled(name, True)
    console.print(f"[green]✔ Plugin '{name}' enabled.[/green]")


@app.command("disable")
def disable_plugin(name: str) -> None:
    """Disable a plugin."""
    from structum.core.config import set_plugin_enabled

    plugins = PluginRegistry.list_plugins()
    if name not in plugins:
        console.print(f"[red]Plugin '{name}' not found.[/red]")
        return

    set_plugin_enabled(name, False)
    console.print(f"[yellow]⚠ Plugin '{name}' disabled.[/yellow]")


@app.command("new")
def new_plugin(
    name: str = typer.Argument(..., help="Plugin name (kebab-case, e.g. my-plugin)"),
    output: Path = typer.Option(
        None, "--output", "-o", help="Output directory (default: auto-detect)"
    ),
    category: str = typer.Option(
        "utility",
        "--category",
        "-c",
        help=f"Plugin category ({', '.join(CATEGORIES.keys())})",
    ),
) -> None:
    """Generate a new plugin skeleton."""
    from structum.plugins.skeleton import generate_plugin_skeleton

    if category not in CATEGORIES:
        console.print(
            f"[red]Invalid category '{category}'. "
            f"Valid: {', '.join(CATEGORIES.keys())}[/red]"
        )
        return

    # Smart default: detect if we're in structum project
    is_structum_project = (Path.cwd() / "src" / "structum" / "plugins").exists()

    if output is None:
        if is_structum_project:
            output = Path.cwd() / "src" / "structum" / "plugins"
        else:
            output = Path.cwd()

    try:
        plugin_dir = generate_plugin_skeleton(name, output, category)
        console.print(f"[green]✔ Plugin skeleton created at:[/green] {plugin_dir}")
        
        # Generate proper class name (same logic as skeleton.py)
        class_name = "".join(word.capitalize() for word in name.split("-")) + "Plugin"

        if is_structum_project and output == Path.cwd() / "src" / "structum" / "plugins":
            # Builtin plugin instructions
            console.print("\n[bold]Next steps (builtin plugin):[/bold]")
            console.print(f"  1. Implement your plugin in [cyan]{plugin_dir}[/cyan]")
            console.print("  2. Edit [cyan]src/structum/plugins/loader.py[/cyan]:")
            console.print(f"     - Add [yellow]from . import {name.replace('-', '_')}[/yellow]")
            console.print(f"     - Register [yellow]{name.replace('-', '_')}.{class_name}[/yellow]")
            console.print("  3. Run [cyan]structum plugins list[/cyan] to verify")
            console.print("\n[dim]See docs/development/plugins.md for details.[/dim]")
        else:
            # External plugin instructions
            console.print("\n[bold]Next steps (external plugin):[/bold]")
            console.print("  1. Create package structure with [cyan]pyproject.toml[/cyan]")
            console.print("  2. Add entry point:")
            console.print('     [yellow][project.entry-points."structum.plugins"][/yellow]')
            console.print(f'     [yellow]{name} = "{name.replace("-", "_")}:{class_name}"[/yellow]')
            console.print("  3. Install with [cyan]pip install -e .[/cyan]")
            console.print("\n[dim]See docs/development/plugins.md for details.[/dim]")
    except Exception as e:
        console.print(f"[red]✘ Error creating plugin:[/red] {e}")

```

## `src/structum/cli/commands/tree.py` {#src-structum-cli-commands-tree-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Tree Command.
"""

from enum import Enum
from pathlib import Path

import typer

from structum.core.tree import print_tree


class ThemeChoice(str, Enum):
    """Valid theme choices for tree visualization."""
    NERD = "nerd"
    EMOJI = "emoji"
    ASCII = "ascii"
    NONE = "none"


def parse_list_callback(value: list[str] | None) -> list[str] | None:
    """Parse comma-separated values and flatten multiple flags.
    
    Supports both:
    - Multiple flags: --ext py --ext md
    - Comma-separated: --ext py,md,js
    - Mixed: --ext py,md --ext js
    """
    if not value:
        return None
    
    result = []
    for item in value:
        # Split by comma and strip whitespace
        parts = [part.strip() for part in item.split(",") if part.strip()]
        result.extend(parts)
    
    return result if result else None




def tree_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to analyze.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    extensions: list[str] | None = typer.Option(
        None,
        "--ext", "-e",
        help="Filter by file extensions (e.g., '-e py -e md' or '-e py,md,js').",
        callback=parse_list_callback
    ),
    ignore_dirs: list[str] | None = typer.Option(
        None,
        "--ignore", "-i",
        help="Directory names to exclude (e.g., '-i .git -i node_modules' or '-i .git,node_modules').",
        callback=parse_list_callback
    ),
    max_depth: int | None = typer.Option(
        None,
        "--depth", "-d",
        help="Maximum depth of the tree traversal."
    ),
    show_hidden: bool = typer.Option(
        False,
        "--hidden",
        help="Show hidden files and directories (starting with '.')."
    ),
    ignore_empty: bool = typer.Option(
        False,
        "--no-empty",
        help="Hide directories that do not contain visible files."
    ),
    theme: ThemeChoice = typer.Option(
        ThemeChoice.EMOJI,
        "--theme", "-t",
        help="Icon theme to use.",
        case_sensitive=False
    ),
    show_stats: bool = typer.Option(
        False,
        "--stats", "-s",
        help="Show directory and file count statistics."
    ),
) -> None:
    """
    Visualizes the directory structure of the specified path.

    \b
    Examples:
        structum tree . --theme nerd
        structum tree src --depth 2 --ext py
    """

    # Note: CLI flag is --hidden (show_hidden=True),
    # but core logic expects ignore_hidden (True by default).
    # We invert the boolean here.
    ignore_hidden_logic = not show_hidden

    print_tree(
        directory=directory,
        extensions=extensions,
        ignore_dirs=ignore_dirs,
        max_depth=max_depth,
        ignore_hidden=ignore_hidden_logic,
        ignore_empty=ignore_empty,
        theme=theme.value,  # Convert Enum to string
        show_stats=show_stats
    )

```

## `src/structum/cli/commands/docs.py` {#src-structum-cli-commands-docs-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Docs Commands.
"""

import typer

from structum.core.docs import deploy_docs, serve_docs

app = typer.Typer()

@app.command(name="serve")
def docs_serve_command(
    dev_addr: str = typer.Option(
        "127.0.0.1:8000",
        "--dev-addr", "-a",
        help="Address and port to serve documentation on."
    ),
) -> None:
    """
    Serves the project documentation locally using MkDocs.

    \b
    This command starts a local development server that watches for changes
    and automatically rebuilds the documentation.

    \b
    Examples:
        structum docs serve
        structum docs serve --dev-addr 0.0.0.0:8080
    """
    serve_docs(dev_addr=dev_addr)


@app.command(name="deploy")
def docs_deploy_command(
    message: str | None = typer.Option(
        None,
        "--message", "-m",
        help="Custom commit message for the deployment."
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force push to gh-pages branch (use with caution)."
    ),
) -> None:
    """
    Deploys the documentation to GitHub Pages.

    \b
    This command builds the documentation and pushes it to the gh-pages branch
    of your repository. Requires proper git configuration and write access.

    \b
    Examples:
        structum docs deploy
        structum docs deploy --message "Update docs for v1.2.0"
        structum docs deploy --force
    """
    deploy_docs(message=message, force=force)

```

## `src/structum/cli/commands/clean.py` {#src-structum-cli-commands-clean-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Clean Command.
"""

from pathlib import Path

import typer

from structum.core.clean import clean_pycache


def clean_command(
    directory: Path = typer.Argument(
        ".",
        help="The root directory to clean.",
        exists=True,
        file_okay=False,
        dir_okay=True,
        resolve_path=True
    ),
    verbose: bool = typer.Option(
        True,
        "--verbose/--quiet", "-v/-q",
        help="Verbose output."
    ),
    skip_venv: bool = typer.Option(
        False,
        "--skip-venv",
        help="Skip virtual environment directories (.env, venv, etc.)."
    ),
) -> None:
    """
    Recursively removes all __pycache__ directories.

    \b
    Examples:
        structum clean .
        structum clean src --quiet
        structum clean . --skip-venv
    """
    clean_pycache(directory, verbose=verbose, skip_venv=skip_venv)

```

## `src/structum/cli/commands/__init__.py` {#src-structum-cli-commands-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
CLI Commands Package.
"""

```

## `src/structum/core/utils.py` {#src-structum-core-utils-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Core utility functions for structum.

This module provides common utility functions used across the structum package,
including file extension normalization and other shared helpers.

Functions:
    normalize_extensions: Normalizes file extensions into standardized ".ext" format.

Example:
    >>> from structum.core.utils import normalize_extensions
    >>> normalize_extensions(["py", ".txt", "MD"])
    {'.py', '.txt', '.md'}
"""
from collections.abc import Iterable

# Default directories to ignore during traversal
IGNORE_DIRS_DEFAULT: set[str] = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".vscode",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
    "__pycache__",
}


def normalize_extensions(extensions: Iterable[str] | None) -> set[str]:
    """Normalizes file extensions into standardized ".ext" format.

    Args:
        extensions: An iterable of strings representing file extensions
            (e.g., "py", ".txt", "md"). Can be None or empty.

    Returns:
        A set of normalized extensions where each extension starts with a dot
        (e.g., {".py", ".txt"}). Returns an empty set if the input is None
        or empty.

    Example:
        >>> normalize_extensions(["py", ".txt", "MD"])
        {'.py', '.txt', '.md'}
        >>> normalize_extensions(None)
        set()
        >>> normalize_extensions([])
        set()
    """
    if not extensions:
        return set()

    normalized: set[str] = set()
    for ext in extensions:
        clean_ext = ext.strip().lower()
        if not clean_ext:
            continue
        if not clean_ext.startswith("."):
            clean_ext = f".{clean_ext}"
        normalized.add(clean_ext)

    return normalized

```

## `src/structum/core/archive.py` {#src-structum-core-archive-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Code archiving functionality.

This module provides tools to traverse a codebase, collect source files based on
extensions, and generate Markdown archives. It supports features like Table of
Contents (ToC) generation and ASCII tree visualization.
"""

import os
from collections import defaultdict
from collections.abc import Sequence
from datetime import datetime
from pathlib import Path

from rich.console import Console

from structum.core.tree import get_tree_ascii
from structum.core.utils import IGNORE_DIRS_DEFAULT, normalize_extensions

console = Console()


def gather_files(
    root: Path,
    extensions: Sequence[str] | None,
    ignore_dirs: Sequence[str] | None = None,
) -> list[tuple[Path, Path]]:
    """Collects all files matching the requested extensions.

    Recursively traverses the ``root`` directory, excluding directories specified
    in ``ignore_dirs`` (or defaults), and includes only files matching the
    provided extensions.

    Args:
        root: The root directory of the project.
        extensions: A sequence of file extensions to include (e.g., [".py", ".md"]).
            If None, ALL files (except ignored ones) will be collected.
        ignore_dirs: A sequence of directory names to exclude. If None, uses
            ``IGNORE_DIRS_DEFAULT``.

    Returns:
        A list of tuples ``(relative_path, absolute_path)`` for each collected file.
    """
    root = root.resolve()
    normalized_exts = normalize_extensions(extensions)

    ignored = set(ignore_dirs) if ignore_dirs else IGNORE_DIRS_DEFAULT
    collected: list[tuple[Path, Path]] = []

    for dirpath, dirnames, filenames in os.walk(root):
        # Filter directories in-place to prevent traversal
        dirnames[:] = [d for d in dirnames if d not in ignored]
        current_dir = Path(dirpath)

        for filename in filenames:
            # If extensions is None or empty (after normalization checks), include all.
            # But normalize_extensions returns empty set for None.
            # We need to distinguish between "User provided explicit empty list" vs "User provided None"
            # However, normalize_extensions(None) -> set(). normalize_extensions([]) -> set().
            # So checking normalized_exts is not enough if we want default behaviors.
            # But wait, logic: if NO extensions specified, we usually want ALL files?
            # Or should we require at least one extension?
            # The bug report says "structum archive -o ~/draft" finds 0 files.
            # This implies default behavior should be "all files".
            
            should_include = False
            if not normalized_exts:
                 should_include = True
            elif any(filename.endswith(ext) for ext in normalized_exts):
                 should_include = True
            
            if should_include:
                full_path = current_dir / filename
                rel_path = full_path.relative_to(root)
                collected.append((rel_path, full_path))

    return collected


def write_markdown(
    path: Path,
    files: Sequence[tuple[Path, Path]],
    root: Path,
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Writes a Markdown archive containing the collected source files.

    Args:
        path: The path to the output Markdown file.
        files: A sequence of tuples ``(relative_path, absolute_path)``.
        root: The root directory of the project (used for relative paths).
        toc: If True, includes a Table of Contents.
        include_tree: If True, includes an ASCII directory tree.
        verbose: If True, prints status messages to the console.
        extensions: Extensions to filter the tree view.
        ignore_dirs: Directories to ignore in the tree view.
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    if verbose:
        console.print(f"✍️  Writing archive: [bold cyan]{path}[/bold cyan]")

    with path.open("w", encoding="utf-8") as md:
        md.write(f"# Code Archive for `{root.name}`\n\n")
        md.write(f"_Generated on {datetime.now().isoformat(timespec='seconds')}_\n\n")

        if include_tree:
            if verbose:
                console.print("   ➕ Including directory tree")
            md.write("## Project Structure\n\n")
            md.write("```text\n")
            # PASSING FILTERS TO TREE GENERATION
            # Use defaults if ignore_dirs is None, but get_tree_ascii handles None by default?
            # Actually get_tree_ascii treats ignore_dirs=None as "no specific ignores"? 
            # No, let's look at get_tree_ascii docstring in tree.py (it doesn't default to common ignores there).
            # But build_tree logic: excluded_dir_names = set(exclude_dirs or [])
            # So if we pass None, it filters nothing.
            # We want to match gather_files logic: ignore_dirs OR defaults.
            
            final_ignore_dirs = ignore_dirs if ignore_dirs is not None else IGNORE_DIRS_DEFAULT
            
            tree_str = get_tree_ascii(
                root, 
                extensions=extensions, 
                ignore_dirs=final_ignore_dirs
            )
            md.write(tree_str)
            md.write("\n```\n\n")

        if toc:
            if verbose:
                console.print("   ➕ Including Table of Contents")
            md.write("## Table of Contents\n\n")
            for rel_path, _ in files:
                anchor = str(rel_path).replace("/", "-").replace(".", "-")
                md.write(f"- [{rel_path}](#{anchor})\n")
            md.write("\n---\n\n")

        for rel_path, full_path in files:
            # Simple heuristic for code block language
            ext = full_path.suffix.replace(".", "") or "text"
            anchor = str(rel_path).replace("/", "-").replace(".", "-")

            md.write(f"## `{rel_path}` {{#{anchor}}}\n\n")
            md.write(f"```{ext}\n")
            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
                md.write(content)
            except Exception as exc:
                md.write(f"# ERROR reading file: {exc}")
            md.write("\n```\n\n")

    if verbose:
        console.print(f"✅ Archive created: [green]{path}[/green]")


def _create_archives_per_folder(
    root: Path,
    output_dir: Path,
    files: Sequence[tuple[Path, Path]],
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Generates a Markdown file for each directory containing collected files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: defaultdict[Path, list[tuple[Path, Path]]] = defaultdict(list)

    for rel_path, full_path in files:
        grouped[rel_path.parent].append((rel_path, full_path))

    for folder, group_files in grouped.items():
        # Map '.' folder to 'root.md', others to 'path/to/dir.md'
        relative_dir = folder if folder != Path(".") else Path("root")
        out_path = output_dir / relative_dir.with_suffix(".md")
        write_markdown(out_path, group_files, root, toc, include_tree, verbose, extensions, ignore_dirs)


def _create_archives_per_type(
    root: Path,
    output_dir: Path,
    files: Sequence[tuple[Path, Path]],
    toc: bool,
    include_tree: bool,
    verbose: bool,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Sequence[str] | None = None,
) -> None:
    """Generates a Markdown file for each file extension."""
    output_dir.mkdir(parents=True, exist_ok=True)
    grouped: defaultdict[str, list[tuple[Path, Path]]] = defaultdict(list)

    for rel_path, full_path in files:
        ext = full_path.suffix.replace(".", "") or "noext"
        grouped[ext].append((rel_path, full_path))

    for ext, group_files in grouped.items():
        out_path = output_dir / f"{ext}.md"
        write_markdown(out_path, group_files, root, toc, include_tree, verbose, extensions, ignore_dirs)


def create_archive(
    root: Path,
    output: Path,
    extensions: Sequence[str] | None,
    ignore_dirs: Sequence[str] | None = None,
    split_by_folder: bool = False,
    split_by_type: bool = False,
    toc: bool = True,
    include_tree: bool = True,
    verbose: bool = True,
) -> None:
    """Main entry point to create code archives.

    Args:
        root: Root directory of the project.
        output: Output file path (single mode) or directory path (split mode).
        extensions: List of file extensions to include.
        ignore_dirs: List of directory names to exclude.
        split_by_folder: If True, creates one archive per folder.
        split_by_type: If True, creates one archive per file extension.
        toc: If True, includes Table of Contents.
        include_tree: If True, includes directory tree.
        verbose: If True, enables verbose output.

    Raises:
        ValueError: If both split_by_folder and split_by_type are True.
    """
    if split_by_folder and split_by_type:
        raise ValueError("Cannot use both split_by_folder and split_by_type.")

    root = root.resolve()
    output = output.resolve()

    # FIX: Handle directory output for single file mode
    if output.is_dir() and not (split_by_folder or split_by_type):
        if verbose:
            console.print(f"[yellow]Address output '{output}' is a directory. Defaulting to '{output / 'archive.md'}'[/yellow]")
        output = output / "archive.md"

    files = gather_files(root, extensions, ignore_dirs)

    if verbose:
        console.print(f"📂 Project Root: [bold]{root}[/bold]")
        console.print(f"📄 Files found: [bold]{len(files)}[/bold]")

    if not files:
        if verbose:
            console.print("[yellow]No files found matching the criteria.[/yellow]")
        return

    if split_by_folder:
        if verbose:
            console.print("📁 Mode: Split by folder")
        _create_archives_per_folder(root, output, files, toc, include_tree, verbose, extensions, ignore_dirs)
        return

    if split_by_type:
        if verbose:
            console.print("📚 Mode: Split by extension")
        _create_archives_per_type(root, output, files, toc, include_tree, verbose, extensions, ignore_dirs)
        return

    # Single archive mode
    write_markdown(output, files, root, toc, include_tree, verbose, extensions, ignore_dirs)

```

## `src/structum/core/tree.py` {#src-structum-core-tree-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Directory tree visualization with Rich.

This module provides functionality to build and display directory structures
as visual trees using the Rich library. It supports multiple themes, filtering
by file extension, excluding directories, and controlling the depth of traversal.

Functions:
    build_tree: Builds a Rich Tree object representing a directory structure.
    print_tree: Prints a formatted directory tree to the console.
    get_tree_ascii: Generates an ASCII string representation of a directory tree.

Example:
    >>> from structum.core.tree import print_tree
    >>> import pathlib
    >>> print_tree(pathlib.Path("./my_project"), theme="emoji", max_depth=2)
"""
import pathlib
from collections.abc import Iterable, Sequence

from rich.console import Console
from rich.text import Text
from rich.tree import Tree

# Robust import handling (as both module and script)
try:
    from . import icons
    from .utils import normalize_extensions
except ImportError:
    import icons  # type: ignore[no-redef]
    from utils import normalize_extensions  # type: ignore[no-redef]

console = Console()

def build_tree(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    exclude_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_files: bool = False,
    ignore_empty: bool = False,
    theme: str = "emoji",
) -> Tree | None:
    """Builds a Rich Tree object representing the directory structure.

    This is the core function that recursively traverses the specified directory
    and constructs a visual tree, applying various filtering and styling options.

    Args:
        directory: The root directory from which to build the tree.
        extensions: File extensions to include. If provided, only files with
            these extensions will be shown. Defaults to None (all files).
        exclude_dirs: Directory names to exclude from the tree. Directories
            matching these names will not be traversed or displayed.
            Defaults to None.
        max_depth: Maximum depth of the tree to display. 0 means only the root,
            1 means root and its immediate children, and so on.
            Defaults to None (no limit).
        ignore_hidden: If True, files and directories starting with '.' will be
            ignored. Defaults to True.
        ignore_files: If True, no files will be included in the tree, only
            directories. Defaults to False.
        ignore_empty: If True, empty directories (after applying all filters)
            will not be displayed. If the root directory becomes empty due to
            filters, the function returns None. Defaults to False.
        theme: The name of the theme to apply for icons and colors. Supported
            themes are 'nerd', 'emoji', 'ascii', 'none'. The 'ascii' and 'none'
            themes disable complex colors and icons. Defaults to "emoji".

    Returns:
        A Tree object representing the directory structure, or None if
        ignore_empty is True and the tree ends up being empty after applying
        all filters.

    Raises:
        NotADirectoryError: If the provided directory path does not exist or
            is not a valid directory.
    """

    # 1. Validation
    directory = directory.resolve()
    if not directory.exists() or not directory.is_dir():
        raise NotADirectoryError(f"The path '{directory}' is not a valid directory.")

    target_exts = normalize_extensions(extensions)
    excluded_dir_names = set(exclude_dirs or [])

    # 2. Theme-based Style Configuration
    # Create boolean flags to simplify logic in the loop
    is_plain_style = theme in ["ascii", "none"]

    guide_style = "white" if is_plain_style else "bright_black"

    # Setup Root
    root_icon = icons.get_icon(directory, theme)

    # If we are in plain style, no colors for the root
    if is_plain_style:
        root_label = Text(f"{root_icon} {directory.name}".strip())
    else:
        root_label = Text(f"{root_icon} {directory.name}".strip(), style="cyan")

    tree = Tree(root_label, guide_style=guide_style)

    # 3. Recursive Function
    def _populate_branch(current_tree: Tree, current_path: pathlib.Path, current_depth: int) -> bool:
        if max_depth is not None and current_depth >= max_depth:
            return False

        try:
            items = sorted(
                current_path.iterdir(),
                key=lambda p: (not p.is_dir(), p.name.lower())
            )
        except PermissionError:
            msg = "🔒 [Access Denied]"
            # Red color only if not in ascii mode
            style = "red" if not is_plain_style else ""
            current_tree.add(Text(msg, style=style))
            return True

        has_visible_content = False

        for item in items:
            if ignore_hidden and item.name.startswith("."):
                continue

            # --- DIRECTORY ---
            if item.is_dir():
                if item.name in excluded_dir_names:
                    continue

                icon = icons.get_icon(item, theme)
                label_str = f"{icon} {item.name}".strip()

                # Folder style
                style = "" if is_plain_style else "yellow"

                branch_tree = Tree(Text(label_str, style=style))

                child_has_content = _populate_branch(branch_tree, item, current_depth + 1)

                if child_has_content or (not ignore_empty):
                    current_tree.add(branch_tree)
                    has_visible_content = True

            # --- FILE ---
            elif item.is_file() and not ignore_files:
                if target_exts and item.suffix.lower() not in target_exts:
                    continue

                icon = icons.get_icon(item, theme)
                label_str = f"{icon} {item.name}".strip()

                # Color Logic (only if not in plain/ascii mode)
                style = ""
                if not is_plain_style:
                    style = "white"  # Default
                    ext = item.suffix.lower()
                    if ext == ".py":
                        style = "green"
                    elif ext == ".md":
                        style = "magenta"
                    elif ext in [".js", ".ts", ".json"]:
                        style = "cyan"
                    elif ext in [".yml", ".yaml", ".toml", ".ini"]:
                        style = "blue"
                    elif ext in [".txt", ".log", ".csv"]:
                        style = "dim white"

                current_tree.add(Text(label_str, style=style))
                has_visible_content = True

        return has_visible_content

    # 4. Start Recursion
    has_content = _populate_branch(tree, directory, 0)

    # If the root is empty (after filters) and ignore_empty is True, return None
    if ignore_empty and not has_content:
        return None

    return tree


# --- CLI Usage Wrapper (Print to screen) ---

def print_tree(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_empty: bool = False,
    theme: str = "emoji",
    show_stats: bool = False
) -> None:
    """Prints a formatted, colored directory tree to the console.

    This function acts as a convenient wrapper around build_tree to display
    the tree directly to standard output using Rich's console rendering.

    Args:
        directory: The root directory from which to print the tree.
        extensions: File extensions to include. Defaults to None.
        ignore_dirs: Directory names to exclude. Defaults to None.
        max_depth: Maximum depth to display. Defaults to None.
        ignore_hidden: If True, hidden files and directories are ignored.
            Defaults to True.
        ignore_empty: If True, empty directories (after filtering) are not
            displayed. Defaults to False.
        theme: The theme to apply for icons and colors. Defaults to "emoji".
        show_stats: If True, displays directory and file count statistics.
            Defaults to False.
    """
    # Count directories and files if stats are requested
    dir_count = 0
    file_count = 0
    
    if show_stats:
        # Count items recursively
        target_exts = normalize_extensions(extensions)
        excluded_dir_names = set(ignore_dirs or [])
        
        def _count_items(path: pathlib.Path, depth: int) -> None:
            nonlocal dir_count, file_count
            
            if max_depth is not None and depth > max_depth:
                return
            
            try:
                items = list(path.iterdir())
            except PermissionError:
                return
            
            for item in items:
                if ignore_hidden and item.name.startswith("."):
                    continue
                
                if item.is_dir():
                    if item.name not in excluded_dir_names:
                        dir_count += 1
                        _count_items(item, depth + 1)
                elif item.is_file():
                    if not target_exts or item.suffix.lower() in target_exts:
                        file_count += 1
        
        _count_items(directory, 0)
    
    tree = build_tree(
        directory=directory,
        extensions=extensions,
        exclude_dirs=ignore_dirs, # Note: correct parameter name mapping
        max_depth=max_depth,
        ignore_hidden=ignore_hidden,
        ignore_files=False,
        ignore_empty=ignore_empty,
        theme=theme
    )

    if tree:
        console.print(tree)
        if show_stats:
            # Format stats like Unix tree command
            dir_word = "directory" if dir_count == 1 else "directories"
            file_word = "file" if file_count == 1 else "files"
            console.print(f"\n{dir_count} {dir_word}, {file_count} {file_word}")
    else:
        console.print("[yellow italic]No content found with current filters.[/yellow italic]")


# --- Export Wrapper (Returns string) ---

def get_tree_ascii(
    directory: pathlib.Path,
    extensions: Sequence[str] | None = None,
    ignore_dirs: Iterable[str] | None = None,
    max_depth: int | None = None,
    ignore_hidden: bool = True,
    ignore_empty: bool = False,
) -> str:
    """Generates an ASCII string representation of a directory tree.

    This function is useful for exporting the tree to text files, Markdown,
    or other contexts where Rich's advanced rendering is not supported or
    desired. It forces the 'ascii' theme to ensure a plain text output.

    Args:
        directory: The root directory from which to build the tree string.
        extensions: File extensions to include. Defaults to None.
        ignore_dirs: Directory names to exclude. Defaults to None.
        max_depth: Maximum depth to display. Defaults to None.
        ignore_hidden: If True, hidden files and directories are ignored.
            Defaults to True.
        ignore_empty: If True, empty directories (after filtering) are not
            displayed. Defaults to False.

    Returns:
        A string containing the ASCII representation of the directory tree.
        Returns an empty string if no content is found after applying filters.
    """
    # Use a temporary console to capture output without spurious color codes
    temp_console = Console(no_color=True, width=1000)

    tree = build_tree(
        directory=directory,
        extensions=extensions,
        exclude_dirs=ignore_dirs,
        max_depth=max_depth,
        ignore_hidden=ignore_hidden,
        ignore_files=False,
        ignore_empty=ignore_empty,
        theme="ascii"      # <--- Force ASCII theme
    )

    if not tree:
        return ""

    with temp_console.capture() as capture:
        temp_console.print(tree)

    return capture.get()

```

## `src/structum/core/icons.py` {#src-structum-core-icons-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Icon management for file and directory visualization.

This module provides multiple icon themes for representing files and directories
in the structum project. Each theme offers a different visual style suitable for
various display contexts and terminal capabilities.

Available themes:
    - nerd: Uses Nerd Fonts icons (requires Nerd Fonts installation)
    - emoji: Uses Unicode emoji characters (maximum compatibility)
    - ascii: Uses simple ASCII characters (safe for text/log files)
    - none: No icons displayed

Example:
    >>> from structum.core.icons import get_icon
    >>> import pathlib
    >>> path = pathlib.Path("example.py")
    >>> icon = get_icon(path, theme_name="emoji")
    >>> print(f"{icon} {path.name}")
    🐍 example.py

Attributes:
    NERD_SET: Nerd Fonts icon theme.
    EMOJI_SET: Emoji icon theme.
    ASCII_SET: ASCII icon theme.
    NONE_SET: Empty icon theme.
    THEMES: Registry mapping theme names to IconSet instances.
"""
import pathlib
from typing import NamedTuple


class IconSet(NamedTuple):
    """Defines a set of icons for folders, default files, and mappings.

    Attributes:
        folder_open: Icon for an open folder.
        folder_closed: Icon for a closed folder.
        file_default: Default icon for files not specifically mapped.
        extensions: A dictionary mapping file extensions (e.g., ".py") to their respective icons.
        filenames: A dictionary mapping specific filenames (e.g., "dockerfile") to their respective icons.
    """
    folder_open: str
    folder_closed: str
    file_default: str
    extensions: dict[str, str]
    filenames: dict[str, str]

# --- 1. Set "NERD" (Requires Nerd Fonts) ---
NERD_SET = IconSet(
    folder_open="",
    folder_closed="",
    file_default="",
    filenames={
        "dockerfile": "", "makefile": "", "jenkinsfile": "",
        ".gitignore": "", ".env": "", "requirements.txt": "",
    },
    extensions={
        ".py": "", ".js": "", ".ts": "", ".html": "", ".css": "",
        ".json": "", ".md": "", ".txt": "", ".sql": "",
        ".zip": "", ".png": "", ".jpg": "", ".pdf": "",
    }
)

# --- 2. Set "EMOJI" (Compatible everywhere) ---
EMOJI_SET = IconSet(
    folder_open="📂",
    folder_closed="📁",
    file_default="📄",
    filenames={
        "dockerfile": "🐳", "makefile": "🛠️", ".gitignore": "🙈", ".env": "🔒",
    },
    extensions={
        ".py": "🐍", ".js": "🟨", ".ts": "🟦", ".html": "🌐", ".css": "🎨",
        ".json": "📋", ".md": "📝", ".txt": "📄", ".sql": "💾",
        ".zip": "📦", ".png": "🖼️", ".jpg": "🖼️", ".pdf": "📕",
        ".exe": "⚙️", ".sh": "🐚"
    }
)

# --- 3. Set "ASCII" (Safe for text/log files) ---
ASCII_SET = IconSet(
    folder_open="",
    folder_closed="",
    file_default="",
    filenames={},
    extensions={}
)

# --- 4. Set "NONE" (No icon) ---
NONE_SET = IconSet("", "", "", {}, {})

# Registry of available themes
THEMES = {
    "nerd": NERD_SET,
    "emoji": EMOJI_SET,
    "ascii": ASCII_SET,
    "none": NONE_SET
}

def get_icon(path: pathlib.Path, theme_name: str = "emoji") -> str:
    """Returns the appropriate icon for the given path based on the specified theme.

    The function first checks if the path is a directory. If so, it returns the
    folder icon for the chosen theme. Otherwise, it attempts to match the file's
    exact name, then its extension. If no specific match is found, it falls back
    to the theme's default file icon.

    Args:
        path: The path to the file or directory for which to get an icon.
        theme_name: The name of the icon theme to use. Available themes are
            "nerd", "emoji", "ascii", and "none". Defaults to "emoji" for
            maximum compatibility.

    Returns:
        The icon string corresponding to the path and theme. Returns an empty
        string if theme_name is "none".
    """
    theme = THEMES.get(theme_name, EMOJI_SET)

    # If the theme is 'none', return an empty string immediately
    if theme_name == "none":
        return ""

    if path.is_dir():
        return theme.folder_open

    name_lower = path.name.lower()

    # 1. Check exact filename
    if name_lower in theme.filenames:
        return theme.filenames[name_lower]

    # 2. Check extension
    return theme.extensions.get(path.suffix.lower(), theme.file_default)

```

## `src/structum/core/docs.py` {#src-structum-core-docs-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Documentation Management Logic.

This module contains the business logic for serving and deploying documentation.
"""

import subprocess
import sys

from rich.console import Console

console = Console()

def serve_docs(dev_addr: str) -> None:
    """
    Serves the project documentation locally using MkDocs.

    Args:
        dev_addr: Address and port to serve documentation on.
    """
    try:
        console.print("[bold blue]Starting documentation server...[/bold blue]")
        result = subprocess.run(
            ["mkdocs", "serve", "--dev-addr", dev_addr],
            check=True
        )
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        console.print("[bold red]Error:[/bold red] Failed to start documentation server.")
        console.print("[dim]Make sure mkdocs and mkdocs-material are installed: pip install mkdocs mkdocs-material[/dim]")
        sys.exit(e.returncode)
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        sys.exit(1)

def deploy_docs(message: str | None, force: bool) -> None:
    """
    Deploys the documentation to GitHub Pages.

    Args:
        message: Custom commit message for the deployment.
        force: Force push to gh-pages branch.
    """
    try:
        console.print("[bold blue]Deploying documentation to GitHub Pages...[/bold blue]")
        cmd = ["mkdocs", "gh-deploy"]

        if message:
            cmd.extend(["--message", message])

        if force:
            cmd.append("--force")

        result = subprocess.run(cmd, check=True)
        console.print("[bold green]✓[/bold green] Documentation deployed successfully!")
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        console.print("[bold red]Error:[/bold red] Failed to deploy documentation.")
        console.print("[dim]Make sure you have push access to the repository and gh-pages branch exists.[/dim]")
        sys.exit(e.returncode)
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] mkdocs command not found.")
        console.print("[dim]Install mkdocs: pip install 'structum[docs]'[/dim]")
        sys.exit(1)

```

## `src/structum/core/clean.py` {#src-structum-core-clean-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Cleanup utilities for Structum.

This module provides functionality to recursively remove ``__pycache__`` directories
from a project. It is used by the CLI ``clean`` command.
"""

import os
import shutil
from pathlib import Path

from rich.console import Console

console = Console()

# Common virtual environment directory names
VENV_DIRS = {'.env', 'env', 'venv', '.venv', 'virtualenv'}


def clean_pycache(root: Path, verbose: bool = True, skip_venv: bool = False) -> int:
    """Recursively removes all ``__pycache__`` directories under the specified root.

    Args:
        root: The root directory to start the recursive search.
        verbose: If ``True``, prints each removed directory to the console.
        skip_venv: If ``True``, skips common virtual environment directories.

    Returns:
        The number of ``__pycache__`` directories successfully removed.
        
    Note:
        By default, this function cleans __pycache__ in all directories including
        virtual environments. Python will recreate them automatically when needed.
        Use skip_venv=True to exclude virtual environments if desired.
    """
    root = root.resolve()
    removed = 0
    skipped_venvs = set()

    for dirpath, dirnames, _ in os.walk(root):
        current_dir = Path(dirpath)
        
        # Skip virtual environment directories if requested
        if skip_venv:
            for dirname in list(dirnames):
                if dirname in VENV_DIRS:
                    skipped_venvs.add(current_dir / dirname)
                    dirnames.remove(dirname)  # Don't walk into venv
        
        # Remove __pycache__ directories
        for dirname in list(dirnames):
            if dirname == "__pycache__":
                target = current_dir / dirname
                try:
                    shutil.rmtree(target)
                    removed += 1
                    if verbose:
                        console.print(f"🗑️  Removed: [dim]{target}[/dim]")
                except Exception as exc:
                    console.print(f"[bold red]⚠️  Error removing {target}:[/bold red] {exc}")

                # Prevent walking into the directory we just removed
                dirnames.remove(dirname)

    if verbose:
        if skipped_venvs:
            console.print(f"[dim]ℹ️  Skipped {len(skipped_venvs)} virtual environment(s)[/dim]")
        console.print(f"✅ Total __pycache__ directories removed: [bold green]{removed}[/bold green]")

    return removed

```

## `src/structum/core/__init__.py` {#src-structum-core-__init__-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Core logic for tree generation and visualization.

This package contains the essential business logic for traversing directories,
handling icons, and rendering output in various formats (Rich/ASCII).

Modules:
    tree: Directory tree building and rendering functionality.
    icons: Icon management for different themes and file types.

Functions:
    build_tree: Build a Rich Tree object from a directory structure.
    get_tree_ascii: Generate an ASCII string representation of a tree.
    print_tree: Display a directory tree in the console.
"""

from .archive import create_archive
from .clean import clean_pycache
from .tree import build_tree, get_tree_ascii, print_tree

__all__ = ["build_tree", "get_tree_ascii", "print_tree", "create_archive", "clean_pycache"]

```

## `src/structum/core/config.py` {#src-structum-core-config-py}

```py
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Configuration Manager for Structum."""

import json
from pathlib import Path
from typing import Any

CONFIG_DIR = Path.home() / ".config" / "structum"
CONFIG_FILE = CONFIG_DIR / "config.json"


def _ensure_config_dir() -> None:
    """Ensure the configuration directory exists."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> dict[str, Any]:
    """Load configuration from file.

    Returns:
        Configuration dictionary.
    """
    _ensure_config_dir()
    if CONFIG_FILE.exists():
        data: dict[str, Any] = json.loads(CONFIG_FILE.read_text())
        return data
    return {"plugins": {}}


def save_config(config: dict[str, Any]) -> None:
    """Save configuration to file.

    Args:
        config: Configuration dictionary to save.
    """
    _ensure_config_dir()
    CONFIG_FILE.write_text(json.dumps(config, indent=2))


def get_plugin_enabled(name: str) -> bool:
    """Check if a plugin is enabled.

    Args:
        name: Plugin name.

    Returns:
        True if enabled, False otherwise.
    """
    config = load_config()
    enabled: bool = config.get("plugins", {}).get(name, {}).get("enabled", True)
    return enabled


def set_plugin_enabled(name: str, enabled: bool) -> None:
    """Set plugin enabled state.

    Args:
        name: Plugin name.
        enabled: Whether the plugin should be enabled.
    """
    config = load_config()
    if "plugins" not in config:
        config["plugins"] = {}
    if name not in config["plugins"]:
        config["plugins"][name] = {}
    config["plugins"][name]["enabled"] = enabled
    save_config(config)

```

