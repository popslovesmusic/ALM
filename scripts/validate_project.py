#!/usr/bin/env python3
"""Validate MGFTS Project Compliance

This script validates that a project meets MGFTS compliance requirements.

Usage:
    python validate_project.py <project_path> [options]

    python validate_project.py /path/to/project
    python validate_project.py . --severity high --report json

Author: ALM MGFTS System
Version: 1.0.0
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass, field
from enum import Enum
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Severity(Enum):
    """Validation violation severity levels."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class Violation:
    """Represents a compliance violation."""
    code: str
    message: str
    path: str
    severity: Severity
    layer: int
    suggestion: Optional[str] = None


@dataclass
class ValidationResult:
    """Results of project validation."""
    project_path: Path
    timestamp: str
    layers_checked: List[int]
    violations: List[Violation] = field(default_factory=list)
    warnings: List[Violation] = field(default_factory=list)
    passed: bool = True
    scores: Dict[str, float] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_violation(self, violation: Violation) -> None:
        """Add a violation."""
        if violation.severity in [Severity.CRITICAL, Severity.HIGH]:
            self.violations.append(violation)
            self.passed = False
        else:
            self.warnings.append(violation)

    def get_violations_by_severity(self, severity: Severity) -> List[Violation]:
        """Get violations of specific severity."""
        all_issues = self.violations + self.warnings
        return [v for v in all_issues if v.severity == severity]

    def get_violations_by_layer(self, layer: int) -> List[Violation]:
        """Get violations for specific layer."""
        all_issues = self.violations + self.warnings
        return [v for v in all_issues if v.layer == layer]


class ProjectValidator:
    """Validate MGFTS project compliance."""

    def __init__(
        self,
        project_path: Path,
        severity_threshold: Severity = Severity.HIGH,
        layers: Optional[List[int]] = None
    ):
        """Initialize validator.

        Args:
            project_path: Path to project root
            severity_threshold: Minimum severity to fail validation
            layers: Which layers to validate (default: all available)
        """
        self.project_path = project_path.resolve()
        self.severity_threshold = severity_threshold
        self.layers = layers or [1, 2]  # Default to structural and governance

        if not self.project_path.exists():
            raise ValueError(f"Project path does not exist: {project_path}")

        if not self.project_path.is_dir():
            raise ValueError(f"Project path is not a directory: {project_path}")

        self.mgfts_path = self.project_path / "mgfts"
        self.result = ValidationResult(
            project_path=self.project_path,
            timestamp=datetime.now().isoformat(),
            layers_checked=self.layers
        )

    def validate(self) -> ValidationResult:
        """Execute full validation.

        Returns:
            ValidationResult with all violations and scores
        """
        logger.info(f"Validating project: {self.project_path}")
        logger.info(f"Checking layers: {self.layers}")

        try:
            # Layer 1: Structural
            if 1 in self.layers:
                self._validate_layer_1_structural()

            # Layer 2: Governance
            if 2 in self.layers:
                self._validate_layer_2_governance()

            # Layer 3: Meta-Governance
            if 3 in self.layers:
                self._validate_layer_3_meta_governance()

            # Compute scores
            self._compute_scores()

            # Set final status
            self.result.passed = len(self.result.violations) == 0

            return self.result

        except Exception as e:
            logger.error(f"Validation error: {e}")
            self.result.passed = False
            self.result.metadata["error"] = str(e)
            raise

    def _validate_layer_1_structural(self) -> None:
        """Validate Layer 1: Structural compliance."""
        logger.info("Validating Layer 1: Structural...")

        # Check directory structure
        required_dirs = ["src", "tests", "docs", "mgfts"]
        for dir_name in required_dirs:
            dir_path = self.project_path / dir_name
            if not dir_path.exists():
                self.result.add_violation(Violation(
                    code="STRUCT-001",
                    message=f"Required directory missing: {dir_name}",
                    path=str(dir_path),
                    severity=Severity.HIGH,
                    layer=1,
                    suggestion=f"Create directory: mkdir {dir_path}"
                ))
            elif not dir_path.is_dir():
                self.result.add_violation(Violation(
                    code="STRUCT-002",
                    message=f"Path exists but is not a directory: {dir_name}",
                    path=str(dir_path),
                    severity=Severity.CRITICAL,
                    layer=1,
                    suggestion=f"Remove file and create directory"
                ))

        # Check for README
        readme_path = self.project_path / "README.md"
        if not readme_path.exists():
            self.result.add_violation(Violation(
                code="STRUCT-003",
                message="README.md missing",
                path=str(readme_path),
                severity=Severity.MEDIUM,
                layer=1,
                suggestion="Create README.md from template"
            ))

        # Check for CHANGELOG
        changelog_path = self.project_path / "CHANGELOG.md"
        if not changelog_path.exists():
            self.result.add_violation(Violation(
                code="STRUCT-004",
                message="CHANGELOG.md missing",
                path=str(changelog_path),
                severity=Severity.LOW,
                layer=1,
                suggestion="Create CHANGELOG.md from template"
            ))

        # Check naming conventions
        self._check_naming_conventions()

    def _check_naming_conventions(self) -> None:
        """Check file naming conventions."""
        # Check Python files use snake_case
        src_path = self.project_path / "src"
        if src_path.exists():
            for py_file in src_path.rglob("*.py"):
                # Allow __init__.py and similar
                if py_file.name.startswith("__") and py_file.name.endswith("__.py"):
                    continue

                # Check snake_case
                name_without_ext = py_file.stem
                if not name_without_ext.islower() and "_" in name_without_ext:
                    # Basic check: should be lowercase with underscores
                    if any(c.isupper() for c in name_without_ext):
                        self.result.add_violation(Violation(
                            code="STRUCT-005",
                            message=f"Python file not using snake_case: {py_file.name}",
                            path=str(py_file),
                            severity=Severity.LOW,
                            layer=1,
                            suggestion=f"Rename to use snake_case"
                        ))

    def _validate_layer_2_governance(self) -> None:
        """Validate Layer 2: Governance compliance."""
        logger.info("Validating Layer 2: Governance...")

        # Check for required governance files
        required_files = [
            ("AGENTS.md", "Agent behavior rules", Severity.CRITICAL),
            ("COMPLIANCE_CHARTER.md", "Compliance standards", Severity.CRITICAL),
            ("PRESERVATION_PROTOCOL.md", "Preservation rules", Severity.CRITICAL),
            ("GLOBAL_CONCEPT_VAULT.json5", "Concept registry", Severity.HIGH),
        ]

        for file_name, description, severity in required_files:
            file_path = self.mgfts_path / file_name
            if not file_path.exists():
                self.result.add_violation(Violation(
                    code="GOV-001",
                    message=f"Missing governance file: {file_name} ({description})",
                    path=str(file_path),
                    severity=severity,
                    layer=2,
                    suggestion=f"Copy {file_name} from MGFTS installation"
                ))

        # Check for project configuration
        config_path = self.mgfts_path / "config" / "project.json5"
        if not config_path.exists():
            self.result.add_violation(Violation(
                code="GOV-002",
                message="Project configuration missing",
                path=str(config_path),
                severity=Severity.HIGH,
                layer=2,
                suggestion="Create project.json5 configuration"
            ))
        else:
            self._validate_project_config(config_path)

        # Check for templates directory
        templates_path = self.mgfts_path / "templates"
        if not templates_path.exists():
            self.result.add_violation(Violation(
                code="GOV-003",
                message="Templates directory missing",
                path=str(templates_path),
                severity=Severity.MEDIUM,
                layer=2,
                suggestion="Copy templates from MGFTS installation"
            ))

    def _validate_project_config(self, config_path: Path) -> None:
        """Validate project configuration file."""
        try:
            # Try to parse as JSON (JSON5 compatibility)
            config_text = config_path.read_text()

            # Remove comments for basic JSON parsing
            lines = []
            for line in config_text.split("\n"):
                # Remove line comments
                if "//" in line:
                    line = line[:line.index("//")]
                lines.append(line)
            clean_json = "\n".join(lines)

            config = json.loads(clean_json)

            # Check required fields
            required_fields = ["project", "mgfts", "paths"]
            for field in required_fields:
                if field not in config:
                    self.result.add_violation(Violation(
                        code="GOV-004",
                        message=f"Configuration missing required field: {field}",
                        path=str(config_path),
                        severity=Severity.HIGH,
                        layer=2,
                        suggestion=f"Add '{field}' section to configuration"
                    ))

            # Check MGFTS configuration
            if "mgfts" in config:
                mgfts_config = config["mgfts"]
                if not mgfts_config.get("enabled", False):
                    self.result.add_violation(Violation(
                        code="GOV-005",
                        message="MGFTS validation is disabled",
                        path=str(config_path),
                        severity=Severity.LOW,
                        layer=2,
                        suggestion="Set mgfts.enabled to true"
                    ))

        except json.JSONDecodeError as e:
            self.result.add_violation(Violation(
                code="GOV-006",
                message=f"Invalid JSON in configuration: {e}",
                path=str(config_path),
                severity=Severity.CRITICAL,
                layer=2,
                suggestion="Fix JSON syntax errors"
            ))

    def _validate_layer_3_meta_governance(self) -> None:
        """Validate Layer 3: Meta-Governance compliance."""
        logger.info("Validating Layer 3: Meta-Governance...")

        # Check for meta-schemas
        meta_schemas_path = self.mgfts_path / "meta_schemas"
        if not meta_schemas_path.exists():
            self.result.add_violation(Violation(
                code="META-001",
                message="Meta-schemas directory missing",
                path=str(meta_schemas_path),
                severity=Severity.MEDIUM,
                layer=3,
                suggestion="Copy meta_schemas from MGFTS installation"
            ))

        # Check for schema validation
        # (Would integrate with actual schema validator here)

    def _compute_scores(self) -> None:
        """Compute compliance scores."""
        # Overall score (inverse of violation count, normalized)
        total_possible = len(self.layers) * 10  # 10 checks per layer
        total_violations = len(self.result.violations) + (len(self.result.warnings) * 0.5)
        overall_score = max(0.0, 1.0 - (total_violations / total_possible))
        self.result.scores["overall"] = round(overall_score, 2)

        # Layer-specific scores
        for layer in self.layers:
            layer_violations = self.result.get_violations_by_layer(layer)
            layer_score = max(0.0, 1.0 - (len(layer_violations) / 10.0))
            self.result.scores[f"layer_{layer}"] = round(layer_score, 2)

        # Severity counts
        self.result.metadata["violation_counts"] = {
            "critical": len(self.result.get_violations_by_severity(Severity.CRITICAL)),
            "high": len(self.result.get_violations_by_severity(Severity.HIGH)),
            "medium": len(self.result.get_violations_by_severity(Severity.MEDIUM)),
            "low": len(self.result.get_violations_by_severity(Severity.LOW)),
        }


def format_report_text(result: ValidationResult) -> str:
    """Format validation result as text."""
    lines = []
    lines.append("=" * 80)
    lines.append("MGFTS Project Validation Report")
    lines.append("=" * 80)
    lines.append(f"Project: {result.project_path}")
    lines.append(f"Timestamp: {result.timestamp}")
    lines.append(f"Layers Checked: {', '.join(map(str, result.layers_checked))}")
    lines.append("")

    # Summary
    status = "✅ PASSED" if result.passed else "❌ FAILED"
    lines.append(f"Status: {status}")
    lines.append(f"Overall Score: {result.scores.get('overall', 0.0):.2f}")
    lines.append("")

    # Scores
    lines.append("Layer Scores:")
    for layer in result.layers_checked:
        score = result.scores.get(f"layer_{layer}", 0.0)
        lines.append(f"  Layer {layer}: {score:.2f}")
    lines.append("")

    # Violation counts
    counts = result.metadata.get("violation_counts", {})
    lines.append("Violation Counts:")
    lines.append(f"  Critical: {counts.get('critical', 0)}")
    lines.append(f"  High: {counts.get('high', 0)}")
    lines.append(f"  Medium: {counts.get('medium', 0)}")
    lines.append(f"  Low: {counts.get('low', 0)}")
    lines.append("")

    # Violations
    if result.violations:
        lines.append("=" * 80)
        lines.append("VIOLATIONS (must fix)")
        lines.append("=" * 80)
        for v in result.violations:
            lines.append(f"\n[{v.severity.value.upper()}] {v.code}: {v.message}")
            lines.append(f"  Path: {v.path}")
            lines.append(f"  Layer: {v.layer}")
            if v.suggestion:
                lines.append(f"  Suggestion: {v.suggestion}")

    # Warnings
    if result.warnings:
        lines.append("\n" + "=" * 80)
        lines.append("WARNINGS (should fix)")
        lines.append("=" * 80)
        for v in result.warnings:
            lines.append(f"\n[{v.severity.value.upper()}] {v.code}: {v.message}")
            lines.append(f"  Path: {v.path}")
            if v.suggestion:
                lines.append(f"  Suggestion: {v.suggestion}")

    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


def format_report_json(result: ValidationResult) -> str:
    """Format validation result as JSON."""
    report = {
        "project": str(result.project_path),
        "timestamp": result.timestamp,
        "passed": result.passed,
        "layers_checked": result.layers_checked,
        "scores": result.scores,
        "metadata": result.metadata,
        "violations": [
            {
                "code": v.code,
                "message": v.message,
                "path": v.path,
                "severity": v.severity.value,
                "layer": v.layer,
                "suggestion": v.suggestion,
            }
            for v in result.violations
        ],
        "warnings": [
            {
                "code": v.code,
                "message": v.message,
                "path": v.path,
                "severity": v.severity.value,
                "layer": v.layer,
                "suggestion": v.suggestion,
            }
            for v in result.warnings
        ],
    }
    return json.dumps(report, indent=2)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate MGFTS project compliance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_project.py .
  python validate_project.py /path/to/project --severity critical
  python validate_project.py . --report json --output report.json
  python validate_project.py . --layers 1,2,3
"""
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Path to project root directory"
    )

    parser.add_argument(
        "--severity",
        choices=["critical", "high", "medium", "low"],
        default="high",
        help="Severity threshold for failures (default: high)"
    )

    parser.add_argument(
        "--layers",
        default="1,2",
        help="Layers to validate (comma-separated, default: 1,2)"
    )

    parser.add_argument(
        "--report",
        choices=["text", "json"],
        default="text",
        help="Report format (default: text)"
    )

    parser.add_argument(
        "--output", "-o",
        type=Path,
        help="Output file (default: stdout)"
    )

    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    # Parse layers
    try:
        layers = [int(l.strip()) for l in args.layers.split(",")]
        if not all(1 <= l <= 7 for l in layers):
            print("Error: Layers must be between 1 and 7")
            sys.exit(1)
    except ValueError:
        print("Error: Invalid layer specification")
        sys.exit(1)

    # Parse severity
    severity = Severity(args.severity)

    try:
        # Run validation
        validator = ProjectValidator(
            project_path=args.project_path,
            severity_threshold=severity,
            layers=layers
        )

        result = validator.validate()

        # Format report
        if args.report == "json":
            report = format_report_json(result)
        else:
            report = format_report_text(result)

        # Output report
        if args.output:
            args.output.write_text(report)
            logger.info(f"Report written to: {args.output}")
        else:
            print(report)

        # Exit code
        if result.passed:
            logger.info("✅ Validation passed")
            sys.exit(0)
        else:
            logger.error("❌ Validation failed")
            sys.exit(1)

    except Exception as e:
        logger.error(f"Validation error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(2)


if __name__ == "__main__":
    main()
