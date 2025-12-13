# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Health check system for Structum framework and plugins."""

import importlib.metadata
import platform
import sys
import time
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()


class HealthStatus(str, Enum):
    """Health status levels."""

    OK = "ok"
    WARNING = "warning"
    DEGRADED = "degraded"
    ERROR = "error"


@dataclass
class HealthCheck:
    """Result of a health check."""

    component: str
    status: HealthStatus
    message: str
    details: dict[str, str] | None = None
    duration_ms: float | None = None


class HealthChecker:
    """System and plugin health checker."""

    def check_system(self) -> list[HealthCheck]:
        """Check system health (Python version, dependencies, etc.)."""
        checks: list[HealthCheck] = []

        # Python version check
        python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        required_version = (3, 11)

        if sys.version_info[:2] >= required_version:
            checks.append(
                HealthCheck(
                    component="Python",
                    status=HealthStatus.OK,
                    message=f"Version {python_version}",
                    details={"required": f">= {required_version[0]}.{required_version[1]}"},
                )
            )
        else:
            checks.append(
                HealthCheck(
                    component="Python",
                    status=HealthStatus.ERROR,
                    message=f"Version {python_version} too old",
                    details={"required": f">= {required_version[0]}.{required_version[1]}"},
                )
            )

        # Platform check
        checks.append(
            HealthCheck(
                component="Platform",
                status=HealthStatus.OK,
                message=f"{platform.system()} {platform.release()}",
                details={"architecture": platform.machine()},
            )
        )

        # Core framework check
        try:
            core_version = importlib.metadata.version("structum")
            checks.append(
                HealthCheck(
                    component="Structum Core",
                    status=HealthStatus.OK,
                    message=f"v{core_version}",
                )
            )
        except Exception as e:
            checks.append(
                HealthCheck(
                    component="Structum Core",
                    status=HealthStatus.ERROR,
                    message=f"Failed to get version: {e}",
                )
            )

        # Config directory check
        config_dir = Path.home() / ".config" / "structum"
        if config_dir.exists():
            config_file = config_dir / "config.json"
            checks.append(
                HealthCheck(
                    component="Configuration",
                    status=HealthStatus.OK,
                    message=f"Found at {config_dir}",
                    details={"config_file": str(config_file)},
                )
            )
        else:
            checks.append(
                HealthCheck(
                    component="Configuration",
                    status=HealthStatus.WARNING,
                    message="No config directory found (will be created on first use)",
                )
            )

        return checks

    def check_plugin(self, plugin_name: str) -> HealthCheck:
        """Check health of a specific plugin by entry point name or package name."""
        # First, try to find the entry point and extract package name
        try:
            entry_points = importlib.metadata.entry_points(group="structum.plugins")
            for ep in entry_points:
                if ep.name == plugin_name:
                    # Extract package name from module path
                    module_parts = ep.value.split(":")
                    if module_parts:
                        package_name = module_parts[0].split(".")[0]
                        return self._check_plugin_package(plugin_name, package_name)

            # If not found by entry point, try as package name directly
            return self._check_plugin_package(plugin_name, plugin_name)

        except Exception as e:
            return HealthCheck(
                component=plugin_name,
                status=HealthStatus.ERROR,
                message="Failed to check plugin health",
                details={"error": str(e)},
            )

    def check_all_plugins(self) -> list[HealthCheck]:
        """Check health of all installed plugins."""
        checks: list[HealthCheck] = []

        try:
            entry_points = importlib.metadata.entry_points(group="structum.plugins")

            # Create mapping of plugin names to package names
            plugin_packages: dict[str, str] = {}
            for ep in entry_points:
                # Extract package name from module path
                # e.g., "structum_tree.plugin" -> "structum_tree"
                module_parts = ep.value.split(":")
                if module_parts:
                    package_name = module_parts[0].split(".")[0]
                    plugin_packages[ep.name] = package_name

            for plugin_name in sorted(plugin_packages.keys()):
                package_name = plugin_packages[plugin_name]
                check = self._check_plugin_package(plugin_name, package_name)
                checks.append(check)

        except Exception as e:
            checks.append(
                HealthCheck(
                    component="Plugin Discovery",
                    status=HealthStatus.ERROR,
                    message=f"Failed to discover plugins: {e}",
                )
            )

        return checks

    def _check_plugin_package(self, plugin_name: str, package_name: str) -> HealthCheck:
        """Check health of a plugin using its package name."""
        start_time = time.time()

        try:
            # Try to get plugin metadata using package name
            metadata = importlib.metadata.metadata(package_name)
            version = metadata.get("Version", "unknown")

            # Try to load the plugin
            try:
                entry_points = importlib.metadata.entry_points(group="structum.plugins")
                plugin_entry = None
                for ep in entry_points:
                    if ep.name == plugin_name:
                        plugin_entry = ep
                        break

                if plugin_entry:
                    # Try to load the plugin class
                    plugin_class = plugin_entry.load()

                    duration = (time.time() - start_time) * 1000

                    return HealthCheck(
                        component=plugin_name,
                        status=HealthStatus.OK,
                        message=f"v{version}",
                        details={"load_time": f"{duration:.2f}ms", "package": package_name},
                        duration_ms=duration,
                    )
                else:
                    return HealthCheck(
                        component=plugin_name,
                        status=HealthStatus.WARNING,
                        message=f"v{version} (not registered)",
                        details={"reason": "No entry point found", "package": package_name},
                    )

            except Exception as e:
                return HealthCheck(
                    component=plugin_name,
                    status=HealthStatus.DEGRADED,
                    message=f"v{version} (import failed)",
                    details={"error": str(e), "package": package_name},
                )

        except Exception as e:
            return HealthCheck(
                component=plugin_name,
                status=HealthStatus.ERROR,
                message="Not installed or corrupted",
                details={"error": str(e), "package": package_name},
            )

    def print_health_report(
        self, system_checks: list[HealthCheck], plugin_checks: list[HealthCheck]
    ) -> None:
        """Print a formatted health report."""
        console.print("\n[bold]🏥 Structum Health Check[/bold]\n")

        # System checks table
        console.print("[bold]System Health:[/bold]")
        system_table = Table(show_header=True, header_style="bold cyan")
        system_table.add_column("Component", style="dim")
        system_table.add_column("Status", justify="center")
        system_table.add_column("Details")

        for check in system_checks:
            status_icon = self._get_status_icon(check.status)
            status_text = f"{status_icon} {check.status.value.upper()}"

            details_text = check.message
            if check.details:
                details_parts = [f"{k}: {v}" for k, v in check.details.items()]
                details_text += f" ({', '.join(details_parts)})"

            system_table.add_row(check.component, status_text, details_text)

        console.print(system_table)
        console.print()

        # Plugin checks table
        if plugin_checks:
            console.print("[bold]Plugin Health:[/bold]")
            plugin_table = Table(show_header=True, header_style="bold cyan")
            plugin_table.add_column("Plugin", style="dim")
            plugin_table.add_column("Status", justify="center")
            plugin_table.add_column("Details")

            for check in plugin_checks:
                status_icon = self._get_status_icon(check.status)
                status_text = f"{status_icon} {check.status.value.upper()}"

                details_text = check.message
                if check.details:
                    details_parts = [f"{k}: {v}" for k, v in check.details.items()]
                    details_text += f" ({', '.join(details_parts)})"

                plugin_table.add_row(check.component, status_text, details_text)

            console.print(plugin_table)
            console.print()

        # Summary
        total_checks = len(system_checks) + len(plugin_checks)
        ok_count = sum(
            1 for c in system_checks + plugin_checks if c.status == HealthStatus.OK
        )
        warning_count = sum(
            1 for c in system_checks + plugin_checks if c.status == HealthStatus.WARNING
        )
        degraded_count = sum(
            1 for c in system_checks + plugin_checks if c.status == HealthStatus.DEGRADED
        )
        error_count = sum(
            1 for c in system_checks + plugin_checks if c.status == HealthStatus.ERROR
        )

        console.print("[bold]Summary:[/bold]")
        console.print(f"  Total checks: {total_checks}")
        console.print(f"  ✓ OK: {ok_count}")
        if warning_count > 0:
            console.print(f"  ⚠ Warning: {warning_count}")
        if degraded_count > 0:
            console.print(f"  ⚠ Degraded: {degraded_count}")
        if error_count > 0:
            console.print(f"  ✗ Error: {error_count}")
        console.print()

    def _get_status_icon(self, status: HealthStatus) -> str:
        """Get icon for health status."""
        icons = {
            HealthStatus.OK: "✓",
            HealthStatus.WARNING: "⚠",
            HealthStatus.DEGRADED: "⚠",
            HealthStatus.ERROR: "✗",
        }
        return icons.get(status, "?")
