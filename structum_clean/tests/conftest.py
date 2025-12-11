# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Pytest configuration for structum_clean tests."""

import pytest
from pathlib import Path


@pytest.fixture
def tmp_workspace(tmp_path: Path):
    """Create a temporary workspace."""
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    return workspace


@pytest.fixture
def sample_files(tmp_workspace: Path):
    """Create sample files for testing."""
    (tmp_workspace / "file1.txt").write_text("Content 1")
    (tmp_workspace / "file2.py").write_text("# Python code")
    
    subdir = tmp_workspace / "subdir"
    subdir.mkdir()
    (subdir / "file3.md").write_text("# Markdown")
    
    return tmp_workspace
