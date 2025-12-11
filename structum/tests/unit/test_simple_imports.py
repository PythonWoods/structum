# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Simple import tests to verify package structure."""

def test_import_structum():
    """Test that structum package can be imported."""
    import structum
    assert structum is not None


def test_import_config():
    """Test importing config module."""
    from structum.config import manager
    assert manager is not None


def test_import_monitoring():
    """Test importing monitoring module."""
    from structum.monitoring import metrics
    assert metrics is not None


def test_import_security():
    """Test importing security module."""
    from structum.security import validator
    assert validator is not None


def test_import_plugins():
    """Test importing plugins module."""
    from structum.plugins import loader, registry, sdk
    assert loader is not None
    assert registry is not None
    assert sdk is not None
