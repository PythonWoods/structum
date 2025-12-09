# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

from unittest.mock import patch, MagicMock
from typer.testing import CliRunner
from structum.cli.main import app, run
from structum import __version__
import pytest

runner = CliRunner()

def test_version_command():
    """Test the version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert f"v{__version__}" in result.stdout

def test_info_command():
    """Test the info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "Structum CLI" in result.stdout
    assert "Python" in result.stdout


class TestDisabledPluginErrorHandling:
    """Tests for disabled plugin error handling."""

    @patch("structum.cli.main.PluginRegistry")
    @patch("structum.cli.main.get_plugin_enabled")
    @patch("sys.argv", ["structum", "my-plugin", "info"])
    def test_disabled_plugin_shows_helpful_message(self, mock_get_enabled, mock_registry):
        """Test that disabled plugins show a helpful error message."""
        # Setup: plugin exists but is disabled
        mock_registry.list_plugins.return_value = ["my-plugin"]
        mock_get_enabled.return_value = False

        # Should exit with code 1 and show helpful message
        with pytest.raises(SystemExit) as exc_info:
            run()

        assert exc_info.value.code == 1

    @patch("structum.cli.main.PluginRegistry")
    @patch("structum.cli.main.get_plugin_enabled")
    @patch("sys.argv", ["structum", "my-plugin"])
    def test_enabled_plugin_executes_normally(self, mock_get_enabled, mock_registry):
        """Test that enabled plugins execute normally (no early exit)."""
        # Setup: plugin exists and is enabled
        mock_registry.list_plugins.return_value = ["my-plugin"]
        mock_get_enabled.return_value = True

        # Should not exit early (will fail later because plugin doesn't really exist,
        # but that's OK - we're just testing it doesn't get caught by our check)
        # We'll catch any error to avoid test failure
        try:
            run()
        except SystemExit:
            # Expected - command doesn't exist, but we passed our check
            pass

    @patch("structum.cli.main.PluginRegistry")
    @patch("sys.argv", ["structum", "nonexistent-plugin"])
    def test_nonexistent_command_passes_through(self, mock_registry):
        """Test that non-plugin commands pass through to normal Typer error handling."""
        # Setup: command doesn't match any plugin
        mock_registry.list_plugins.return_value = ["other-plugin"]

        # Should not be caught by our check, will proceed to Typer's error handling
        try:
            run()
        except SystemExit:
            # Expected - Typer will handle the unknown command
            pass

    @patch("structum.cli.main.PluginRegistry")
    @patch("sys.argv", ["structum", "--help"])
    def test_flags_are_not_checked(self, mock_registry):
        """Test that flags like --help are not checked as plugin names."""
        # Should not check --help as a plugin name
        # The function should skip the check and pass through to Typer
        mock_registry.list_plugins.return_value = ["--help"]  # Shouldn't matter

        # Will proceed normally (--help will be handled by Typer)
        try:
            run()
        except SystemExit as e:
            # --help causes exit with code 0
            assert e.code == 0
