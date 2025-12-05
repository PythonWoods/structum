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
