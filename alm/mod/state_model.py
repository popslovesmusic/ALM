"""ALM Constitutional Engine - State Model

This module defines the internal state representation for the Constitutional Engine.

The StateModel aggregates:
- Tool execution results
- Violations and warnings
- Metrics per layer
- Scores per layer
- Coherence and concealment measures
- Concept usage statistics

Author: ALM Constitutional Engine
Version: 0.1.0
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Violation:
    """Represents a compliance violation."""

    code: str
    message: str
    path: str
    severity: str  # critical|high|medium|low
    layer: Optional[int] = None
    tool: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "code": self.code,
            "message": self.message,
            "path": self.path,
            "severity": self.severity,
            "layer": self.layer,
            "tool": self.tool
        }


@dataclass
class Warning:
    """Represents a compliance warning."""

    code: str
    message: str
    path: str
    severity: str
    layer: Optional[int] = None
    tool: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "code": self.code,
            "message": self.message,
            "path": self.path,
            "severity": self.severity,
            "layer": self.layer,
            "tool": self.tool
        }


@dataclass
class LayerScore:
    """Score for a single MGFTS layer."""

    layer: int
    score: float  # 0-1
    violations: int = 0
    warnings: int = 0
    metrics: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "layer": self.layer,
            "score": self.score,
            "violations": self.violations,
            "warnings": self.warnings,
            "metrics": self.metrics
        }


class StateModel:
    """Aggregated state for Constitutional Engine analysis.

    This class maintains the complete state of the analysis,
    aggregating results from all tools into a unified representation.
    """

    def __init__(self, project: str):
        """Initialize state model.

        Parameters
        ----------
        project : str
            Project name or path
        """
        self.project = project
        self.timestamp = datetime.utcnow().isoformat() + "Z"

        # Tool execution tracking
        self.tools_run: List[Dict[str, Any]] = []

        # Violations and warnings
        self.violations: List[Violation] = []
        self.warnings: List[Warning] = []

        # Scores per layer (1-7)
        self.layer_scores: Dict[int, LayerScore] = {
            i: LayerScore(layer=i, score=1.0) for i in range(1, 8)
        }

        # Concept tracking
        self.concepts_missing: List[str] = []
        self.concepts_unused: List[str] = []
        self.concepts_referenced: Dict[str, int] = {}

        # Global metrics
        self.coherence_score: float = 1.0
        self.concealment_score: float = 0.0
        self.overall_score: float = 1.0

        # Additional metrics
        self.metrics: Dict[str, Any] = {}

    def add_tool_result(self, tool_result: Dict[str, Any]) -> None:
        """Add results from a tool execution.

        Parameters
        ----------
        tool_result : dict
            Tool output following MGFTS tool contract
        """
        tool_name = tool_result.get("tool", "unknown")
        tool_version = tool_result.get("version", "unknown")

        # Track tool execution
        self.tools_run.append({
            "tool": tool_name,
            "version": tool_version,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        })

        # Add violations
        for v in tool_result.get("violations", []):
            self.violations.append(Violation(
                code=v["code"],
                message=v["message"],
                path=v["path"],
                severity=v["severity"],
                layer=v.get("layer"),
                tool=tool_name
            ))

        # Add warnings
        for w in tool_result.get("warnings", []):
            self.warnings.append(Warning(
                code=w["code"],
                message=w["message"],
                path=w["path"],
                severity=w["severity"],
                layer=w.get("layer"),
                tool=tool_name
            ))

        # Update layer scores
        target_layers = tool_result.get("layer_targets", [])
        tool_score = tool_result.get("score")

        if tool_score is not None:
            for layer in target_layers:
                if layer in self.layer_scores:
                    # Average scores from multiple tools
                    current = self.layer_scores[layer].score
                    self.layer_scores[layer].score = (current + tool_score) / 2

        # Update layer violation/warning counts
        for v in tool_result.get("violations", []):
            layer = v.get("layer")
            if layer and layer in self.layer_scores:
                self.layer_scores[layer].violations += 1

        for w in tool_result.get("warnings", []):
            layer = w.get("layer")
            if layer and layer in self.layer_scores:
                self.layer_scores[layer].warnings += 1

        # Merge metrics
        tool_metrics = tool_result.get("metrics", {})
        for key, value in tool_metrics.items():
            metric_key = f"{tool_name}.{key}"
            self.metrics[metric_key] = value

        # Handle concept-specific outputs
        if "concepts_missing" in tool_result:
            self.concepts_missing.extend(tool_result["concepts_missing"])

        if "concepts_unused" in tool_result:
            self.concepts_unused.extend(tool_result["concepts_unused"])

    def set_coherence_score(self, score: float) -> None:
        """Set the coherence field score.

        Parameters
        ----------
        score : float
            Coherence score (0-1)
        """
        self.coherence_score = max(0.0, min(1.0, score))

    def set_concealment_score(self, score: float) -> None:
        """Set the concealment functional score.

        Parameters
        ----------
        score : float
            Concealment score (0-1, higher = more concealment)
        """
        self.concealment_score = max(0.0, min(1.0, score))

    def compute_overall_score(self) -> float:
        """Compute overall compliance score.

        Aggregates layer scores with weighting:
        - Layers 1-3: 50% (structural, governance, meta)
        - Layers 4-7: 30% (semantic, ecological, formal, ontological)
        - Coherence: 10%
        - Concealment: 10% (inverted)

        Returns
        -------
        float
            Overall score (0-1)
        """
        # Layer scores with weights
        layer_1_3 = sum(self.layer_scores[i].score for i in range(1, 4)) / 3
        layer_4_7 = sum(self.layer_scores[i].score for i in range(4, 8)) / 4

        # Weighted combination
        score = (
            0.5 * layer_1_3 +
            0.3 * layer_4_7 +
            0.1 * self.coherence_score +
            0.1 * (1.0 - self.concealment_score)  # Lower concealment = better
        )

        self.overall_score = max(0.0, min(1.0, score))
        return self.overall_score

    def get_violations_by_severity(self) -> Dict[str, List[Violation]]:
        """Group violations by severity.

        Returns
        -------
        dict
            Violations grouped by severity level
        """
        groups: Dict[str, List[Violation]] = {
            "critical": [],
            "high": [],
            "medium": [],
            "low": []
        }

        for v in self.violations:
            if v.severity in groups:
                groups[v.severity].append(v)

        return groups

    def get_violations_by_layer(self) -> Dict[int, List[Violation]]:
        """Group violations by MGFTS layer.

        Returns
        -------
        dict
            Violations grouped by layer
        """
        groups: Dict[int, List[Violation]] = {}

        for v in self.violations:
            if v.layer:
                if v.layer not in groups:
                    groups[v.layer] = []
                groups[v.layer].append(v)

        return groups

    def to_dict(self) -> Dict[str, Any]:
        """Convert state to dictionary representation.

        Returns
        -------
        dict
            Complete state as dictionary
        """
        return {
            "project": self.project,
            "timestamp": self.timestamp,
            "tools_run": self.tools_run,
            "scores": {
                f"layer_{i}_{'structural' if i==1 else 'governance' if i==2 else 'meta_schema' if i==3 else 'semantic' if i==4 else 'ecological' if i==5 else 'formal' if i==6 else 'ontological'}": self.layer_scores[i].score
                for i in range(1, 8)
            } | {"overall": self.overall_score},
            "violations": [v.to_dict() for v in self.violations],
            "warnings": [w.to_dict() for w in self.warnings],
            "concepts_missing": list(set(self.concepts_missing)),
            "concepts_unused": list(set(self.concepts_unused)),
            "concealment_score": self.concealment_score,
            "coherence_score": self.coherence_score,
            "metrics": self.metrics,
            "summary": {
                "total_violations": len(self.violations),
                "total_warnings": len(self.warnings),
                "critical_violations": len([v for v in self.violations if v.severity == "critical"]),
                "high_violations": len([v for v in self.violations if v.severity == "high"])
            }
        }
