# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Plugin SDK for Structum."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import typer


@dataclass
class PluginConfig:
    """Configuration for a plugin."""

    enabled: bool = True
    options: dict[str, Any] = field(default_factory=dict)


# Available plugin categories
CATEGORIES = {
    "analysis": "Code analysis and metrics",
    "export": "Export and format conversion",
    "formatting": "Code formatting and style",
    "utility": "Utility and helper tools",
}


class PluginBase(ABC):
    """Base class for all Structum plugins."""

    name: str
    version: str
    category: str = "utility"  # Default category
    description: str = ""
    author: str = ""

    def __init__(self, config: PluginConfig | None = None) -> None:
        """Initialize the plugin."""
        self.config = config or PluginConfig()

    @abstractmethod
    def setup(self) -> None:
        """Initialize plugin resources."""
        pass

    def process_file(self, file_path: Path) -> dict[str, Any] | None:
        """Process a single file and return metadata.

        Args:
            file_path: Path to the file to process.

        Returns:
            Dictionary containing extracted metadata or None if file is ignored.
        """
        return None

    def generate_output(self, data: dict[str, Any]) -> str | None:
        """Generate plugin-specific output.

        Args:
            data: Metadata extracted from files.

        Returns:
            String content to append to documentation or None.
        """
        return None

    def register_commands(self, app: "typer.Typer") -> None:  # noqa: B027
        """Register CLI commands for this plugin. Override in subclass."""

    def teardown(self) -> None:  # noqa: B027
        """Cleanup resources. Override in subclass if needed."""
