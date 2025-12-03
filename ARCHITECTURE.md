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
│       ├── dashboard.py            # Interactive dashboard
│       ├── exporter.py             # Multi-format export
│       └── templates/              # Report templates
│           ├── corporate/
│           ├── minimal/
│           └── audit/
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
