# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Core utility functions for structum.

This module provides common utility functions used across the structum package,
including file extension normalization and other shared helpers.

Functions:
    normalize_extensions: Normalizes file extensions into standardized ".ext" format.

Example:
    >>> from structum.core.utils import normalize_extensions
    >>> normalize_extensions(["py", ".txt", "MD"])
    {'.py', '.txt', '.md'}
"""
from collections.abc import Iterable


def normalize_extensions(extensions: Iterable[str] | None) -> set[str]:
    """Normalizes file extensions into standardized ".ext" format.

    Args:
        extensions: An iterable of strings representing file extensions
            (e.g., "py", ".txt", "md"). Can be None or empty.

    Returns:
        A set of normalized extensions where each extension starts with a dot
        (e.g., {".py", ".txt"}). Returns an empty set if the input is None
        or empty.

    Example:
        >>> normalize_extensions(["py", ".txt", "MD"])
        {'.py', '.txt', '.md'}
        >>> normalize_extensions(None)
        set()
        >>> normalize_extensions([])
        set()
    """
    if not extensions:
        return set()

    normalized: set[str] = set()
    for ext in extensions:
        clean_ext = ext.strip().lower()
        if not clean_ext:
            continue
        if not clean_ext.startswith("."):
            clean_ext = f".{clean_ext}"
        normalized.add(clean_ext)

    return normalized
