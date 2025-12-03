# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""CLI entry point for Structum.

This module serves as the main entry point for the command-line interface,
providing directory tree visualization functionality directly from the terminal.
"""

import sys
from pathlib import Path

# Try to import from the installed package first.
# If it fails (dev mode without install), add the source root to sys.path.
try:
    from structum.core.tree import print_tree
except ImportError:
    # Development fallback: Allow direct execution of the file
    # Adds 'src' to sys.path so 'structum' can be imported
    sys.path.append(str(Path(__file__).resolve().parents[2]))
    from structum.core.tree import print_tree

def main() -> None:
    """Simple entry point to test the CLI functionality.
    
    Currently hardcoded for development testing. Displays the directory tree
    of the current directory with a maximum depth of 2 levels.
    """
    root = Path(".")
    
    print("--- Structum CLI (Dev Mode) ---")
    
    # Example usage
    print_tree(
        root, 
        max_depth=2, 
        theme="emoji",
        ignore_dirs=[".git", "__pycache__", "venv"]
    )

if __name__ == "__main__":
    main()