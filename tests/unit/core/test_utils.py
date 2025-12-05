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
