# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import subprocess
import sys
from unittest.mock import MagicMock, patch

import pytest
from structum.core import docs

class TestDocs:
    """Tests for documentation management."""

    @patch("subprocess.run")
    def test_serve_docs_success(self, mock_run):
        """Test serving docs successfully."""
        mock_run.return_value.returncode = 0
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost:8000")
        
        assert exc.value.code == 0
        mock_run.assert_called_once_with(
            ["mkdocs", "serve", "--dev-addr", "localhost:8000"],
            check=True
        )

    @patch("subprocess.run")
    def test_serve_docs_error(self, mock_run):
        """Test serving docs failure."""
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost:8000")
            
        assert exc.value.code == 1

    @patch("subprocess.run")
    def test_deploy_docs_success(self, mock_run):
        """Test deploying docs successfully."""
        mock_run.return_value.returncode = 0
        
        with pytest.raises(SystemExit) as exc:
            docs.deploy_docs(message="update", force=True)
            
        assert exc.value.code == 0
        mock_run.assert_called_once()
        args = mock_run.call_args[0][0]
        assert "gh-deploy" in args
        assert "--message" in args
        assert "--force" in args

    @patch("subprocess.run")
    def test_serve_docs_not_found(self, mock_run):
        """Test serve_docs when mkdocs is missing."""
        mock_run.side_effect = FileNotFoundError
        
        with pytest.raises(SystemExit) as exc:
            docs.serve_docs("localhost")
        
        assert exc.value.code == 1

    @patch("subprocess.run")
    def test_deploy_docs_not_found(self, mock_run):
        """Test deploy_docs when mkdocs is missing."""
        mock_run.side_effect = FileNotFoundError
        
        with pytest.raises(SystemExit) as exc:
            docs.deploy_docs(message=None, force=False)
            
        assert exc.value.code == 1
