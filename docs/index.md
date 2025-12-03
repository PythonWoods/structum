---
title: Structum
hide:
  - navigation
  - toc
---

<div class="hero-section" markdown>

<div class="hero-content">

# **Structum**

### Enterprise Code Structure & Documentation Engine

<p class="hero-description">
Il tuo strumento professionale per visualizzare, documentare e archiviare progetti.
Progettato per sviluppatori, team e AI.
</p>

<div class="hero-buttons">
[:material-rocket-launch: Quick Start](getting-started.md){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub](https://github.com/pythonwoods/structum){ .md-button }
</div>

</div>

</div>

---

<div class="features-grid" markdown>

<div class="feature-card" markdown>
### :material-file-tree: Albero del progetto

Visualizza un tree ricco e colorato con icon themes personalizzabili.
Perfetto per README e documentazione.

```bash
structum tree . --theme nerd
```
</div>

<div class="feature-card" markdown>
### :material-archive: Archivi Markdown

Crea archivi completi del codice in formato Markdown.
Ideale per debug, revisioni, refactoring e AI ingestion.

```bash
structum archive . --tree --toc
```
</div>

<div class="feature-card" markdown>
### :material-puzzle: Plugin System

Sistema di plugin estensibile per funzionalità custom.
Estendibile come un framework enterprise.

```python
# Custom plugin example
@plugin.register
def custom_format(): ...
```
</div>

<div class="feature-card" markdown>
### :material-robot: AI-Ready

Output ottimizzato per ChatGPT, Claude, Gemini, Copilot.
Format perfetti per context injection.

```bash
structum archive --ext py --split-type
```
</div>

</div>

---

## Quick Start

<div class="quick-start-grid" markdown>

<div class="qs-step" markdown>
#### 1. Installazione

```bash
pip install structum
# oppure con uv
uv pip install structum
```
</div>

<div class="qs-step" markdown>
#### 2. Tree Structure

```bash
structum tree . \
  --theme emoji \
  --depth 3
```
</div>

<div class="qs-step" markdown>
#### 3. Archive Code

```bash
structum archive . \
  --output docs/code.md \
  --ext py --ext md
```
</div>

</div>

---

## Caratteristiche Principali

<div class="key-features" markdown>

- **:material-filter:** Filtering avanzato per estensioni e directory
- **:material-palette:** Temi personalizzabili (nerd, emoji, ascii, none)
- **:material-file-multiple:** Split per folder o tipo di file
- **:material-table-of-contents:** Table of Contents automatico
- **:material-speedometer:** Performance ottimizzate per grandi codebase
- **:material-code-braces:** Syntax highlighting nei markdown generati
- **:material-git:** Integrazione Git per commit e PR
- **:material-api:** API Reference completa con mkdocstrings

</div>

---

## Use Cases

<div class="use-cases" markdown>

!!! example "Per Sviluppatori"
    Documenta rapidamente la struttura del progetto, genera README automatici,
    condividi contesto con il team.

!!! info "Per AI/LLM"
    Formatta il codice in modo ottimale per ChatGPT, Claude, Copilot.
    Massimizza la comprensione del contesto.

!!! tip "Per Code Review"
    Esporta snapshot del codice per review offline, confronti versioni,
    analisi retrospettive.

!!! success "Per Documentazione"
    Genera automaticamente overview del progetto, mantieni docs aggiornati,
    integra in CI/CD.

</div>

---

<div class="cta-section" markdown>

## Pronto a iniziare?

Installa Structum in pochi secondi e inizia a visualizzare il tuo codice.

[:material-book-open-page-variant: Leggi la Guida](getting-started.md){ .md-button .md-button--primary }
[:material-api: API Reference](api.md){ .md-button }

</div>

---

<div class="footer-info" markdown>

**Open Source** · Apache-2.0 License · Made with :material-heart: by [PythonWoods](https://github.com/pythonwoods)

[GitHub](https://github.com/pythonwoods/structum) ·
[Issues](https://github.com/pythonwoods/structum/issues) ·
[Discussions](https://github.com/pythonwoods/structum/discussions)

</div>
