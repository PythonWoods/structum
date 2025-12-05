# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch
from typer.testing import CliRunner
from structum.cli.commands.clean import clean_command
import typer

runner = CliRunner()
app = typer.Typer()
app.command()(clean_command)

class TestCleanCommand:
    """Tests for clean CLI command."""

    @patch("structum.cli.commands.clean.clean_pycache")
    def test_clean_command_defaults(self, mock_clean, tmp_path):
        """Test clean command with defaults."""
        result = runner.invoke(app, [str(tmp_path)])
        assert result.exit_code == 0
        mock_clean.assert_called_with(tmp_path, verbose=True, skip_venv=False)

    @patch("structum.cli.commands.clean.clean_pycache")
    def test_clean_command_options(self, mock_clean, tmp_path):
        """Test clean command options."""
        result = runner.invoke(app, [str(tmp_path), "--quiet", "--skip-venv"])
        assert result.exit_code == 0
        mock_clean.assert_called_with(tmp_path, verbose=False, skip_venv=True)
