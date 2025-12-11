# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Pytest configuration and shared fixtures for structum core tests."""

import pytest
from pathlib import Path
from typing import Generator
import tempfile
import shutil


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Return path to test data directory."""
    return Path(__file__).parent / "test_data"


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Generator[Path, None, None]:
    """Create a temporary workspace for tests."""
    workspace = tmp_path / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)
    yield workspace
    # Cleanup is automatic with tmp_path


@pytest.fixture
def sample_project(tmp_workspace: Path) -> Path:
    """Create a sample project structure for testing.

    Structure:
        project/
        ├── src/
        │   ├── __init__.py
        │   ├── main.py
        │   └── utils.py
        ├── tests/
        │   └── test_main.py
        ├── docs/
        │   └── README.md
        ├── .git/
        ├── .gitignore
        └── pyproject.toml
    """
    project = tmp_workspace / "project"
    project.mkdir()

    # Create src directory
    src = project / "src"
    src.mkdir()
    (src / "__init__.py").write_text("# Package init\n")
    (src / "main.py").write_text("def main():\n    print('Hello')\n")
    (src / "utils.py").write_text("def helper():\n    return True\n")

    # Create tests directory
    tests = project / "tests"
    tests.mkdir()
    (tests / "test_main.py").write_text("def test_example():\n    assert True\n")

    # Create docs directory
    docs = project / "docs"
    docs.mkdir()
    (docs / "README.md").write_text("# Documentation\n")

    # Create git directory (empty)
    git = project / ".git"
    git.mkdir()

    # Create config files
    (project / ".gitignore").write_text("__pycache__/\n*.pyc\n.venv/\n")
    (project / "pyproject.toml").write_text('[project]\nname = "test-project"\n')

    return project


@pytest.fixture(autouse=True)
def reset_plugin_registry():
    """Reset the plugin registry before each test."""
    from structum.plugins.registry import PluginRegistry

    # Store original state
    original_plugins = PluginRegistry._plugins.copy()
    original_instances = PluginRegistry._instances.copy()

    # Clear registry for test
    PluginRegistry.clear()

    yield

    # Restore original state
    PluginRegistry._plugins = original_plugins
    PluginRegistry._instances = original_instances
