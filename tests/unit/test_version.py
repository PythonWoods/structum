# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import structum

def test_version():
    """Verify that the package has a version attribute."""
    assert structum.__version__ is not None
    assert isinstance(structum.__version__, str)
