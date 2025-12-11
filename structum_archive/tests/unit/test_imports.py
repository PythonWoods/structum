# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Simple import tests."""

def test_import_plugin():
    """Test that plugin module can be imported."""
    plugin_name = __file__.split('/')[-4]
    __import__(plugin_name)
    assert True
