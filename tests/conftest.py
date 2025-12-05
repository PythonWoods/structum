# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

import pytest
from typing import Generator

@pytest.fixture(scope="session")
def test_session_id() -> Generator[str, None, None]:
    """Example session-scoped fixture."""
    yield "session-123"
