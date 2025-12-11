# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 PythonWoods

"""Performance metrics collection for plugins and commands."""

import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Metric:
    """Represents a single metric measurement."""

    name: str
    value: float
    unit: str
    timestamp: float = field(default_factory=time.time)
    labels: dict[str, str] = field(default_factory=dict)


class MetricsCollector:
    """Collects and manages performance metrics."""

    def __init__(self) -> None:
        """Initialize metrics collector."""
        self._metrics: dict[str, list[Metric]] = defaultdict(list)
        self._counters: dict[str, int] = defaultdict(int)

    def record_time(self, name: str, duration: float, **labels: str) -> None:
        """Record a time duration metric.

        Args:
            name: Metric name (e.g., "plugin.load_time")
            duration: Duration in seconds
            **labels: Optional labels for grouping/filtering
        """
        metric = Metric(name=name, value=duration, unit="seconds", labels=labels)
        self._metrics[name].append(metric)

    def increment_counter(self, name: str, value: int = 1) -> None:
        """Increment a counter metric.

        Args:
            name: Counter name (e.g., "plugin.load_count")
            value: Amount to increment (default: 1)
        """
        self._counters[name] += value

    def get_metric(self, name: str) -> list[Metric]:
        """Get all measurements for a metric.

        Args:
            name: Metric name

        Returns:
            List of metric measurements
        """
        return self._metrics.get(name, [])

    def get_counter(self, name: str) -> int:
        """Get counter value.

        Args:
            name: Counter name

        Returns:
            Counter value
        """
        return self._counters.get(name, 0)

    def get_average(self, name: str) -> float:
        """Get average value for a time metric.

        Args:
            name: Metric name

        Returns:
            Average value or 0.0 if no measurements
        """
        metrics = self._metrics.get(name, [])
        if not metrics:
            return 0.0
        return sum(m.value for m in metrics) / len(metrics)

    def get_summary(self) -> dict[str, Any]:
        """Get summary of all collected metrics.

        Returns:
            Dictionary with metrics summary
        """
        return {
            "metrics": {
                name: {
                    "count": len(measurements),
                    "average": self.get_average(name),
                    "latest": measurements[-1].value if measurements else None,
                }
                for name, measurements in self._metrics.items()
            },
            "counters": dict(self._counters),
        }

    def clear(self) -> None:
        """Clear all collected metrics."""
        self._metrics.clear()
        self._counters.clear()


# Global metrics collector instance
_global_metrics = MetricsCollector()


def get_metrics() -> MetricsCollector:
    """Get the global metrics collector instance.

    Returns:
        Global MetricsCollector instance
    """
    return _global_metrics
