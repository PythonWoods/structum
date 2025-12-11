# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Pytest configuration for structum_tree tests."""

import pytest
from pathlib import Path


@pytest.fixture
def sample_directory(tmp_path: Path) -> Path:
    """Create a sample directory structure for testing.

    Structure:
        sample/
        ├── file1.py
        ├── file2.txt
        ├── folder1/
        │   ├── file3.py
        │   └── file4.md
        └── folder2/
            └── file5.txt
    """
    sample = tmp_path / "sample"
    sample.mkdir()

    # Create files
    (sample / "file1.py").write_text("# Python file\n")
    (sample / "file2.txt").write_text("Text file\n")

    # Create folder1 with files
    folder1 = sample / "folder1"
    folder1.mkdir()
    (folder1 / "file3.py").write_text("# Another Python file\n")
    (folder1 / "file4.md").write_text("# Markdown\n")

    # Create folder2 with file
    folder2 = sample / "folder2"
    folder2.mkdir()
    (folder2 / "file5.txt").write_text("More text\n")

    return sample
