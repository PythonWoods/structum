# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Core logic for tree generation and visualization.

This package contains the essential business logic for traversing directories,
handling icons, and rendering output in various formats (Rich/ASCII).

Modules:
    tree: Directory tree building and rendering functionality.
    icons: Icon management for different themes and file types.

Functions:
    build_tree: Build a Rich Tree object from a directory structure.
    get_tree_ascii: Generate an ASCII string representation of a tree.
    print_tree: Display a directory tree in the console.
"""

from .tree import build_tree, get_tree_ascii, print_tree

__all__ = ["build_tree", "get_tree_ascii", "print_tree"]
