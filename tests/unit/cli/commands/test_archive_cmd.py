# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch
from typer.testing import CliRunner
import pytest
from structum.cli.commands.archive import archive_command
import typer

runner = CliRunner()
app = typer.Typer()
app.command()(archive_command)

class TestArchiveCommand:
    """Tests for archive CLI command wrapper."""

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_basic(self, mock_create, tmp_path):
        """Test basic invocation of archive command."""
        result = runner.invoke(app, [str(tmp_path)])
        
        assert result.exit_code == 0
        mock_create.assert_called_once()
        # Check defaults
        call_args = mock_create.call_args[1]
        assert call_args["extensions"] is None
        assert call_args["toc"] is True
        assert call_args["include_tree"] is True

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_options(self, mock_create, tmp_path):
        """Test passing options."""
        result = runner.invoke(app, [
            str(tmp_path),
            "--output", "out.md",
            "--ext", "py",
            "--ext", "md",
            "--ignore", ".git,dist",
            "--split-folder",
            "--no-toc",
            "--no-tree"
        ])
        
        assert result.exit_code == 0
        call_args = mock_create.call_args[1]
        assert call_args["output"].name == "out.md"
        assert sorted(call_args["extensions"]) == ["md", "py"]
        assert sorted(call_args["ignore_dirs"]) == [".git", "dist"]
        assert call_args["split_by_folder"] is True
        assert call_args["toc"] is False
        assert call_args["include_tree"] is False

    @patch("structum.cli.commands.archive.create_archive")
    def test_archive_command_error_handling(self, mock_create, tmp_path):
        """Test handling of ValueError from core logic."""
        mock_create.side_effect = ValueError("Test Error")
        result = runner.invoke(app, [str(tmp_path)])
        
        assert result.exit_code == 1
        assert "Error:" in result.stdout
        assert "Test Error" in result.stdout
