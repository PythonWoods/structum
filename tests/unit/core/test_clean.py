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
