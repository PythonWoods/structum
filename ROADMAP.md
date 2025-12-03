# Structum Roadmap - Documentation Engine

> **Vision:** Trasformare Structum nel leading Documentation Engine per sviluppatori, team enterprise e AI/LLM workflows.

---

## Executive Summary

Structum evolverà da un tool di visualizzazione del codice a una **piattaforma completa di documentazione**, con capacità di:

- **AI-ready output** ottimizzato per ChatGPT, Claude, Gemini
- **Pipeline automation** per CI/CD enterprise
- **Report generation** professionale (PDF, Dashboard)
- **Plugin ecosystem** estensibile per framework popolari
- **Git integration** per documentazione evolutiva

---

## Target Audience

1. **Developers individuali** - Quick documentation, AI assistant integration
2. **Team aziendali** - Code review, onboarding, audit compliance
3. **AI/LLM users** - Context injection, RAG workflows
4. **Enterprise** - Compliance, security audit, documentation standards

---

## Strategic Phases

### 🚀 Phase 1: AI-Ready Output (PRIORITY 1)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Differenziatore chiave nel mercato

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

```python
class SmartChunker:
    """Intelligent code chunking for LLM consumption."""

    def chunk_by_tokens(self, max_tokens: int) -> list[Chunk]
    def chunk_by_module(self) -> list[Chunk]
    def chunk_by_dependencies(self) -> list[Chunk]
    def prioritize_chunks(self, strategy: str) -> list[Chunk]
```

**Strategies:**
- Token-based (rispetta limits GPT-4, Claude, etc.)
- Module-based (mantiene coesione logica)
- Dependency-based (include imports necessari)
- Semantic-based (raggruppa funzionalità correlate)

##### 1.3 Format Adapters
**File:** `src/structum/core/ai/formatters.py`

```python
class OpenAIFormatter:
    """Optimized for GPT-3.5/GPT-4/GPT-4o"""
    token_limit = 128000  # GPT-4 Turbo
    format_style = "conversational"

class ClaudeFormatter:
    """Optimized for Claude 3 Opus/Sonnet"""
    token_limit = 200000  # Claude 3 Opus
    format_style = "structured"

class GeminiFormatter:
    """Optimized for Gemini Pro/Ultra"""
    token_limit = 1000000  # Gemini 1.5 Pro
    format_style = "comprehensive"
```

##### 1.4 RAG Integration
**File:** `src/structum/core/ai/rag.py`

- Vector embeddings ready
- Chunk metadata per retrieval
- Semantic search preparation
- Context window optimization

**Example output:**
```json
{
  "chunk_id": "uuid",
  "file_path": "src/core/archive.py",
  "content": "...",
  "metadata": {
    "dependencies": ["pathlib", "rich"],
    "purpose": "Archive generation",
    "complexity": "medium",
    "lines": "1-150",
    "git_blame": {
      "last_author": "PythonWoods",
      "last_modified": "2025-12-03"
    }
  },
  "embedding_ready": true
}
```

#### Success Metrics
- ✅ Output < token limits per ogni formato
- ✅ Context retention > 95%
- ✅ 3+ format adapters implementati
- ✅ Documentazione completa per AI workflows

---

### 📚 Phase 2: Documentation Pipeline (PRIORITY 2)
**Timeline:** 3-4 settimane
**Impact:** HIGH - Enterprise adoption driver

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

```python
class GitIntegration:
    """Git-aware documentation generation."""

    def get_file_blame(self, file_path: Path) -> dict
    def get_changelog(self, since: str) -> list[Change]
    def get_diff_summary(self, from_ref: str, to_ref: str) -> DiffSummary
    def get_commit_history(self, file_path: Path) -> list[Commit]
```

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

#### Success Metrics
- ✅ Auto-update < 5 secondi
- ✅ Git integration completa
- ✅ CI/CD templates per GitHub/GitLab
- ✅ Versioning system funzionante

---

### 🔌 Phase 3: Plugin Ecosystem (PRIORITY 3)
**Timeline:** 4-6 settimane
**Impact:** MEDIUM-HIGH - Estensibilità e adoption

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
```bash
structum plugins add fastapi-autodoc
structum archive . --use-plugin=fastapi
```

Features:
- Auto-detect routes
- Extract endpoint metadata
- Generate OpenAPI supplement
- Document dependencies

**Typer/Click Plugin**
```bash
structum plugins add typer-autodoc
structum archive . --use-plugin=typer
```

Features:
- CLI command documentation
- Argument/option extraction
- Help text generation
- Command tree visualization

**Pydantic Plugin**
```bash
structum plugins add pydantic-schema
structum archive . --use-plugin=pydantic
```

Features:
- Schema extraction
- Validation rules documentation
- Field descriptions
- JSON Schema export

**SQLAlchemy Plugin**
```bash
structum plugins add sqlalchemy-er
structum archive . --use-plugin=sqlalchemy
```

Features:
- Model relationship mapping
- ER diagram generation
- Migration history
- Schema visualization

##### 3.3 Plugin Development Kit
**File:** `src/structum/plugins/sdk.py`

```python
from structum.plugins import PluginBase

class MyCustomPlugin(PluginBase):
    name = "my-plugin"
    version = "1.0.0"

    def process_file(self, file_path: Path) -> ProcessedFile:
        """Process single file."""
        pass

    def generate_output(self, data: dict) -> str:
        """Generate plugin-specific output."""
        pass
```

**Documentation:**
- Plugin development guide
- API reference
- Example plugins
- Testing framework

##### 3.4 Plugin Registry
- Central plugin repository
- Version management
- Security scanning
- Community ratings

#### Success Metrics
- ✅ 4+ official plugins rilasciati
- ✅ Plugin SDK completo
- ✅ Community plugin support
- ✅ Plugin documentation

---

### 📊 Phase 4: Report Generation (PRIORITY 3)
**Timeline:** 3-4 settimane
**Impact:** MEDIUM - Visual appeal e enterprise adoption

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

##### 4.2 Interactive Dashboard
```bash
structum report dashboard --interactive --output=./dashboard/
structum report dashboard --serve --port=8080
```

**Features:**
- File explorer interattivo
- Code statistics charts
- Dependency graphs
- Timeline evolution
- Search functionality

**Tech Stack:**
- Static HTML/CSS/JS
- Chart.js per grafici
- D3.js per visualizzazioni
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

##### 4.4 Export Formats
- **PDF** - Audit, compliance, presentation
- **HTML** - Interactive, dashboard
- **JSON** - API, integration
- **XML** - Enterprise systems
- **Markdown** - Documentation
- **DOCX** - Word documents

#### Success Metrics
- ✅ PDF generation funzionante
- ✅ Dashboard interattiva
- ✅ 3+ themes disponibili
- ✅ Multiple export formats

---

### 🏗️ Phase 5: CI/CD Integration (PRIORITY 2)
**Timeline:** 2-3 settimane
**Impact:** HIGH - Enterprise adoption

#### Obiettivi
- GitHub Actions templates
- GitLab CI templates
- Jenkins integration
- Pre-commit hooks

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
│   └── reports/            # NEW - Phase 4
│       ├── __init__.py
│       ├── pdf.py          # PDF generation
│       ├── dashboard.py    # Interactive dashboard
│       └── templates/      # Report templates
│           ├── corporate/
│           ├── minimal/
│           └── audit/
├── integrations/           # NEW - Phase 2
│   ├── __init__.py
│   ├── git.py              # Git integration
│   └── frameworks/         # NEW - Phase 3
│       ├── __init__.py
│       ├── fastapi.py      # FastAPI plugin
│       ├── typer_cli.py    # Typer/Click plugin
│       ├── pydantic.py     # Pydantic plugin
│       └── sqlalchemy.py   # SQLAlchemy plugin
├── plugins/                # Existing - Enhanced in Phase 3
│   ├── __init__.py
│   ├── loader.py
│   ├── sdk.py              # NEW - Plugin development kit
│   └── registry.py         # NEW - Plugin registry
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

# Phase 3 - Plugins
structum plugins list
structum plugins add fastapi-autodoc
structum plugins config

# Phase 4 - Reports
structum report full --pdf
structum report dashboard --interactive

# Phase 5 - CI/CD
structum hooks install
structum ci-template generate --platform=github
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

### Optional Dependencies
```toml
[project.optional-dependencies]
ai = ["tiktoken", "anthropic", "openai"]
pipeline = ["watchdog", "GitPython"]
reports = ["weasyprint", "jinja2", "markdown2"]
plugins = ["pluggy", "importlib-metadata"]
full = ["structum[ai,pipeline,reports,plugins]"]
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

**Total:** ~880 hours (22 settimane full-time o 6 mesi part-time)

### Team Composition (Ideale)
- 1 Senior Python Developer (core development)
- 1 DevOps Engineer (CI/CD, automation)
- 1 Technical Writer (documentation)
- 1 Designer (UI/UX per dashboard)
- Community contributors (plugin ecosystem)

---

## Next Actions

### Immediate (Week 1)
1. ✅ Create ROADMAP.md (questo documento)
2. ⬜ Create ARCHITECTURE.md (dettaglio tecnico)
3. ⬜ Setup project structure per Phase 1
4. ⬜ Create GitHub project board con milestones
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

**Legend:** ✅ Full support | ⚠️ Partial | 🔄 In progress | ❌ Not supported

### References
- [OpenAI Token limits](https://platform.openai.com/docs/models)
- [Claude context windows](https://docs.anthropic.com/claude/docs)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Plugin architecture patterns](https://pluggy.readthedocs.io/)

---

**Document Version:** 1.0
**Last Updated:** 2025-12-03
**Maintained by:** PythonWoods Team
**Status:** 🟢 Active Development
