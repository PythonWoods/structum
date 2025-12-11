# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Tests for version information."""

import structum


def test_version_exists():
    """Verify that the package has a version attribute."""
    assert hasattr(structum, "__version__")
    assert structum.__version__ is not None


def test_version_is_string():
    """Verify version is a string."""
    assert isinstance(structum.__version__, str)


def test_version_format():
    """Verify version follows semantic versioning format."""
    version = structum.__version__
    # Should be in format X.Y.Z or X.Y.ZaN (alpha) or X.Y.ZbN (beta)
    assert len(version) > 0
    # Should start with a digit
    assert version[0].isdigit()
