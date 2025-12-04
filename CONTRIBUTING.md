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

Refer to `src/structum/plugins/sample/` for a reference implementation.
Plugins should follow the `commands`/`core` structure.

## Documentation

Documentation is built with MkDocs.
```bash
structum docs serve
```
