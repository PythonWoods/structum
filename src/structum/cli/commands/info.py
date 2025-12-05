# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""
Info and Version Commands.
"""

import platform
import sys
from rich.console import Console
from structum import __version__

console = Console()

def version_command() -> None:
    """Show the application version."""
    console.print(f"Structum CLI v{__version__}")

def info_command() -> None:
    """Show application information."""
    console.print(f"[bold]Structum CLI[/bold] v{__version__}")
    console.print(f"Python {sys.version.split()[0]}")
    console.print(f"Platform: {platform.system()} {platform.release()}")
