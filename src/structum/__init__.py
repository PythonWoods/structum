# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Structum - Visualization and management of directory trees.

This package provides tools for visualizing and managing directory structures
with support for multiple themes, filtering, and export formats.

Main Functions:
    print_tree: Display a directory tree in the console.
    get_tree_ascii: Generate an ASCII string representation of a directory tree.
    build_tree: Build a Rich Tree object representing a directory structure.

Example:
    >>> from structum import print_tree
    >>> from pathlib import Path
    >>> print_tree(Path("./my_project"), theme="emoji", max_depth=2)
"""

from .__about__ import __version__
from .core.tree import build_tree, get_tree_ascii, print_tree

__all__ = ["__version__", "print_tree", "get_tree_ascii", "build_tree"]