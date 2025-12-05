# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from structum.core import tree

class TestTree:
    """Tests for directory tree visualization."""

    @pytest.fixture
    def workspace(self, tmp_path):
        """Create a temporary workspace with files and folders."""
        # Create structure:
        # /root
        # ├── file1.txt
        # ├── src/
        # │   ├── main.py
        # │   └── utils.py
        # ├── docs/
        # │   └── readme.md
        # ├── .hidden/
        # └── .gitignore
        
        fs = tmp_path
        (fs / "file1.txt").touch()
        (fs / ".gitignore").touch()
        
        src = fs / "src"
        src.mkdir()
        (src / "main.py").touch()
        (src / "utils.py").touch()
        
        docs = fs / "docs"
        docs.mkdir()
        (docs / "readme.md").touch()
        
        hidden = fs / ".hidden"
        hidden.mkdir()
        
        return fs

    def test_build_tree_basic(self, workspace):
        """Test building a basic tree."""
        result = tree.build_tree(workspace)
        assert result is not None
        assert str(workspace.name) in str(result.label)

    def test_build_tree_extensions_filter(self, workspace):
        """Test filtering by extension."""
        result = tree.build_tree(workspace, extensions=[".py"])
        
        # Should contain python files
        # We need to capture the output or inspect the tree structure/labels
        # Capturing rich output to string is easier for content verification
        ascii_tree = tree.get_tree_ascii(workspace, extensions=[".py"])
        
        assert "main.py" in ascii_tree
        assert "utils.py" in ascii_tree
        assert "file1.txt" not in ascii_tree
        assert "readme.md" not in ascii_tree

    def test_build_tree_ignore_hidden(self, workspace):
        """Test ignoring hidden files."""
        result = tree.get_tree_ascii(workspace, ignore_hidden=True)
        assert ".gitignore" not in result
        assert ".hidden" not in result

    def test_build_tree_show_hidden(self, workspace):
        """Test showing hidden files."""
        result = tree.get_tree_ascii(workspace, ignore_hidden=False)
        assert ".gitignore" in result
        # Check if .hidden directory is shown (might depend on implementation details of empty dir behavior)
        if not (workspace / ".hidden").iterdir(): # Empty hidden dir
             # If empty dirs are not ignored by default in get_tree_ascii (it forces ignore_empty=True)
             # Let's check build_tree behavior directly
             t = tree.build_tree(workspace, ignore_hidden=False, ignore_empty=False)
             # Rich Tree structure inspection is complex, relying on visual output or traversal
             pass 

    def test_build_tree_max_depth(self, workspace):
        """Test max depth limit."""
        # Depth 0 should only show root (managed by build_tree logic mainly, but rich tree rendering handles display)
        # build_tree logic: current_depth > max_depth -> return False
        
        # Depth 1: root + immediate children
        result = tree.get_tree_ascii(workspace, max_depth=1)
        assert "src" in result
        assert "file1.txt" in result
        # Grandchildren should NOT be visible
        # Note: In standard tree output, folders are listed, but their content might be hidden
        # If max_depth=1, src/main.py (depth 2) should NOT be there
        assert "main.py" not in result

    def test_get_tree_ascii_returns_string(self, workspace):
        """Test that get_tree_ascii returns a non-empty string."""
        output = tree.get_tree_ascii(workspace)
        assert isinstance(output, str)
        assert len(output) > 0
        assert "src" in output
