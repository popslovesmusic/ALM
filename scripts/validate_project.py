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
        layers: Optional[List[int]] = None,
        verify_artifacts: bool = False
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
        self.verify_artifacts = verify_artifacts

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

    def _load_json5(self, path: Path) -> Dict[str, Any]:
        """Load a JSON5-like file by stripping line comments for JSON parsing."""
        config_text = path.read_text()
        lines = []
        for line in config_text.split("\n"):
            if "//" in line:
                line = line.split("//", 1)[0]
            lines.append(line)
        clean_json = "\n".join(lines)
        return json.loads(clean_json)

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

            # Layer 5: Ecological Intelligence
            if 5 in self.layers:
                self._validate_layer_5_ecological()

            # Layer 6: Formal Verification
            if 6 in self.layers:
                self._validate_layer_6_formal()

            # Layer 7: Ontological foundation
            if 7 in self.layers:
                self._validate_layer_7_ontology()

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

        # Optional ecological configuration hint for Layer 5
        ecology_path = self.mgfts_path / "config" / "layer5_ecology.json5"
        if ecology_path.exists():
            self.result.metadata.setdefault("layer5_ecology", {})["config_path"] = str(ecology_path)

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
            config = self._load_json5(config_path)

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

    def _validate_layer_5_ecological(self) -> None:
        """Validate Layer 5: Ecological intelligence configuration and signals."""
        logger.info("Validating Layer 5: Ecological intelligence...")

        ecology_path = self.mgfts_path / "config" / "layer5_ecology.json5"
        if not ecology_path.exists():
            self.result.add_violation(Violation(
                code="ECO-001",
                message="Ecological configuration missing (layer5_ecology.json5)",
                path=str(ecology_path),
                severity=Severity.MEDIUM,
                layer=5,
                suggestion="Create mgfts/config/layer5_ecology.json5 with collector toggles and thresholds"
            ))
            return

        try:
            ecology_config = self._load_json5(ecology_path)
        except json.JSONDecodeError as e:
            self.result.add_violation(Violation(
                code="ECO-002",
                message=f"Invalid JSON in ecological configuration: {e}",
                path=str(ecology_path),
                severity=Severity.CRITICAL,
                layer=5,
                suggestion="Fix JSON/JSON5 syntax before running ecological checks"
            ))
            return

        collectors = ecology_config.get("pattern_collectors", [])
        enabled_collectors = [c for c in collectors if c.get("enabled")]
        required_collectors = {"governance_pattern", "code_churn_pattern"}
        missing_collectors = [c for c in required_collectors if c not in {c.get("name") for c in collectors}]

        for collector in missing_collectors:
            self.result.add_violation(Violation(
                code="ECO-003",
                message=f"Required ecological collector missing: {collector}",
                path=str(ecology_path),
                severity=Severity.HIGH,
                layer=5,
                suggestion="Declare the collector in pattern_collectors and enable it"
            ))

        for collector in collectors:
            if collector.get("name") in required_collectors and not collector.get("enabled"):
                self.result.add_violation(Violation(
                    code="ECO-004",
                    message=f"Required ecological collector disabled: {collector.get('name')}",
                    path=str(ecology_path),
                    severity=Severity.MEDIUM,
                    layer=5,
                    suggestion="Enable the collector to satisfy Layer 5 coverage"
                ))

        metrics = ecology_config.get("health_metrics", {})
        if not metrics:
            self.result.add_violation(Violation(
                code="ECO-005",
                message="Health metrics missing in ecological configuration",
                path=str(ecology_path),
                severity=Severity.MEDIUM,
                layer=5,
                suggestion="Add ecological_health, concealment_surface, and pattern_reuse thresholds"
            ))

        thresholds_defined = sum(1 for values in metrics.values() if isinstance(values, dict) and values)
        collector_coverage = len(enabled_collectors) / max(len(collectors), 1)
        metric_coverage = thresholds_defined / max(len(metrics), 1)
        ecological_health_score = round((collector_coverage + metric_coverage) / 2, 2)

        # Warn if ecological health is below target thresholds
        ecological_target = metrics.get("ecological_health", {}).get("target", 0.0)
        warn_below = metrics.get("ecological_health", {}).get("warn_below", 0.0)
        if ecological_target and ecological_health_score < warn_below:
            self.result.add_violation(Violation(
                code="ECO-006",
                message=("Ecological health score below warn threshold; enable more collectors or define thresholds "
                         "to align with Aletheia/GVP."),
                path=str(ecology_path),
                severity=Severity.LOW,
                layer=5,
                suggestion="Increase active collectors and set metric targets to raise ecological health"
            ))

        self.result.metadata["layer5_ecology"] = {
            "collectors_total": len(collectors),
            "collectors_enabled": len(enabled_collectors),
            "thresholds_defined": thresholds_defined,
            "ecological_health_score": ecological_health_score,
            "config_path": str(ecology_path),
        }
        self.result.scores["layer_5_ecological_health"] = ecological_health_score

    def _validate_layer_6_formal(self) -> None:
        """Validate Layer 6: Formal verification readiness and artifacts."""
        logger.info("Validating Layer 6: Formal verification...")

        config_path = self.mgfts_path / "config" / "layer6_verification.json5"
        default_patterns = [
            "*.smt2", "*.smt", "*.smtlib", "*.v", "*.thy", "*.lean",
            "*.tla", "*.cfg", "*.als", "*.smv", "*.dfy", "*.fst", "*.lh",
            "*.l6spec", "*.contracts"
        ]
        proof_dirs: List[str] = ["verification", "proofs"]
        artifact_patterns: List[str] = default_patterns
        targets: List[Dict[str, Any]] = []
        tools: List[Dict[str, Any]] = []
        validation_checks: List[Dict[str, Any]] = []

        if not config_path.exists():
            self.result.add_violation(Violation(
                code="FORM-001",
                message="Layer 6 verification configuration missing (layer6_verification.json5)",
                path=str(config_path),
                severity=Severity.MEDIUM,
                layer=6,
                suggestion="Create mgfts/config/layer6_verification.json5 (see template)"
            ))
        else:
            try:
                config = self._load_json5(config_path)
                proof_dirs = config.get("proof_dirs", proof_dirs)
                artifact_patterns = config.get("artifact_patterns", default_patterns)
                targets = config.get("targets", [])
                tools = config.get("tools", [])
            except json.JSONDecodeError as e:
                self.result.add_violation(Violation(
                    code="FORM-006",
                    message=f"Invalid JSON in Layer 6 configuration: {e}",
                    path=str(config_path),
                    severity=Severity.CRITICAL,
                    layer=6,
                    suggestion="Fix JSON/JSON5 syntax in layer6_verification.json5"
                ))
                self.result.metadata["layer6_verification"] = {"config_path": str(config_path)}
                self.result.scores["layer_6_formal"] = 0.0
                return

        proof_artifacts: List[Path] = []
        scanned_dirs: List[str] = []
        missing_dirs: List[str] = []

        for dir_name in proof_dirs:
            dir_path = self.project_path / dir_name
            if dir_path.exists() and dir_path.is_dir():
                scanned_dirs.append(str(dir_path))
                for pattern in artifact_patterns:
                    proof_artifacts.extend(dir_path.rglob(pattern))
            else:
                missing_dirs.append(str(dir_path))

        if not proof_artifacts:
            self.result.add_violation(Violation(
                code="FORM-002",
                message="No formal verification artifacts found in configured proof directories",
                path=", ".join(scanned_dirs or proof_dirs),
                severity=Severity.MEDIUM,
                layer=6,
                suggestion="Add proof artifacts (e.g., .smt2, .v, .tla) or update proof_dirs"
            ))

        targets_without_artifacts = []
        for target in targets:
            if not target.get("artifacts"):
                targets_without_artifacts.append(target.get("name", "unnamed_target"))
                continue
            for art in target.get("artifacts", []):
                art_path = self.project_path / art
                if not art_path.exists():
                    targets_without_artifacts.append(target.get("name", art))

        if targets_without_artifacts:
            self.result.add_violation(Violation(
                code="FORM-003",
                message=f"Verification targets missing artifacts: {', '.join(sorted(set(targets_without_artifacts)))}",
                path=str(config_path),
                severity=Severity.MEDIUM,
                layer=6,
                suggestion="Attach proof files to targets or mark status with rationale"
            ))

        active_tools = [t for t in tools if t.get("enabled")]
        if not tools or not active_tools:
            self.result.add_violation(Violation(
                code="FORM-004",
                message="No formal verification tools registered or enabled",
                path=str(config_path),
                severity=Severity.MEDIUM,
                layer=6,
                suggestion="Register and enable at least one verification tool entry"
            ))

        if self.verify_artifacts and proof_artifacts:
            for artifact in proof_artifacts:
                try:
                    size = artifact.stat().st_size
                    if size == 0:
                        self.result.add_violation(Violation(
                            code="FORM-005",
                            message=f"Proof artifact is empty: {artifact}",
                            path=str(artifact),
                            severity=Severity.LOW,
                            layer=6,
                            suggestion="Populate artifact with proof obligations or remove stale entry"
                        ))
                        validation_checks.append({
                            "artifact": str(artifact),
                            "status": "failed",
                            "reason": "empty file"
                        })
                    else:
                        validation_checks.append({
                            "artifact": str(artifact),
                            "status": "ok",
                            "bytes": size
                        })
                except OSError as e:
                    self.result.add_violation(Violation(
                        code="FORM-005",
                        message=f"Unable to read proof artifact: {artifact} ({e})",
                        path=str(artifact),
                        severity=Severity.LOW,
                        layer=6,
                        suggestion="Ensure artifact is accessible for optional checks"
                    ))
                    validation_checks.append({
                        "artifact": str(artifact),
                        "status": "failed",
                        "reason": str(e)
                    })
        elif self.verify_artifacts:
            validation_checks.append({"status": "skipped", "reason": "no artifacts found"})

        target_count = len(targets)
        declared_artifacts = sum(len(t.get("artifacts", [])) for t in targets) if targets else 0
        coverage_components = [
            1.0 if config_path.exists() else 0.0,
            1.0 if proof_artifacts else 0.0,
            1.0 if active_tools else 0.0,
            (declared_artifacts / target_count) if target_count else 0.0,
        ]
        coverage_score = round(sum(coverage_components) / len(coverage_components), 2)

        self.result.metadata["layer6_verification"] = {
            "config_path": str(config_path),
            "proof_directories_scanned": scanned_dirs,
            "missing_proof_directories": missing_dirs,
            "artifact_count": len(proof_artifacts),
            "targets_declared": target_count,
            "tools_registered": [t.get("name") for t in tools],
            "tools_enabled": [t.get("name") for t in active_tools],
            "validation_checks": validation_checks,
            "coverage_score": coverage_score,
        }
        self.result.scores["layer_6_formal"] = coverage_score

    def _validate_layer_7_ontology(self) -> None:
        """Validate Layer 7: Ontological completeness and truth maintenance."""
        logger.info("Validating Layer 7: Ontology...")

        vault_path = self.mgfts_path / "GLOBAL_CONCEPT_VAULT.json5"
        if not vault_path.exists():
            self.result.add_violation(Violation(
                code="ONTO-001",
                message="GLOBAL_CONCEPT_VAULT.json5 missing; cannot evaluate ontology",
                path=str(vault_path),
                severity=Severity.HIGH,
                layer=7,
                suggestion="Restore mgfts/GLOBAL_CONCEPT_VAULT.json5 from governance templates"
            ))
            return

        try:
            vault = self._load_json5(vault_path)
        except json.JSONDecodeError as e:
            self.result.add_violation(Violation(
                code="ONTO-006",
                message=f"Invalid JSON in concept vault: {e}",
                path=str(vault_path),
                severity=Severity.CRITICAL,
                layer=7,
                suggestion="Fix JSON/JSON5 syntax or regenerate from ontology template"
            ))
            return

        concepts = vault.get("concepts", [])
        ontology_rules = vault.get("ontology", {})
        relationships = vault.get("relationships", [])
        concept_ids = {concept.get("id") for concept in concepts if concept.get("id")}

        if not concepts:
            self.result.add_violation(Violation(
                code="ONTO-002",
                message="Concept vault has no concepts to validate",
                path=str(vault_path),
                severity=Severity.HIGH,
                layer=7,
                suggestion="Populate concepts and existence predicates using ontology_record template"
            ))
            return

        if not ontology_rules.get("existence_predicates"):
            self.result.add_violation(Violation(
                code="ONTO-006",
                message="Ontology existence_predicates are not defined",
                path=str(vault_path),
                severity=Severity.MEDIUM,
                layer=7,
                suggestion="Declare ontology.existence_predicates to describe project-wide existence checks"
            ))

        evidence_warnings: List[str] = []
        with_predicates = 0
        with_truth = 0

        for concept in concepts:
            concept_id = concept.get("id", "<unknown>")
            existence = concept.get("existence") or {}
            truth = concept.get("truth_maintenance") or {}

            predicates = existence.get("predicates", [])
            if predicates:
                with_predicates += 1
                for evidence_path in existence.get("evidence", []) or []:
                    evidence_full = self.project_path / evidence_path
                    if evidence_path and not evidence_full.exists():
                        evidence_warnings.append(f"{concept_id}:{evidence_path}")
            else:
                self.result.add_violation(Violation(
                    code="ONTO-002",
                    message=f"Concept {concept_id} missing existence predicates",
                    path=str(vault_path),
                    severity=Severity.HIGH,
                    layer=7,
                    suggestion="Add predicates via ontology_record template"
                ))

            if truth.get("source_of_truth") and truth.get("conflict_resolution"):
                with_truth += 1
            else:
                self.result.add_violation(Violation(
                    code="ONTO-003",
                    message=f"Concept {concept_id} missing truth maintenance fields",
                    path=str(vault_path),
                    severity=Severity.HIGH,
                    layer=7,
                    suggestion="Specify source_of_truth and conflict_resolution in truth_maintenance"
                ))

        for rel in relationships:
            if rel.get("from") not in concept_ids or rel.get("to") not in concept_ids:
                self.result.add_violation(Violation(
                    code="ONTO-004",
                    message="Relationship references unknown concept",
                    path=str(vault_path),
                    severity=Severity.MEDIUM,
                    layer=7,
                    suggestion="Ensure relationship endpoints reference valid concept IDs"
                ))

        for warning in evidence_warnings:
            concept_id, evidence_path = warning.split(":", 1)
            self.result.add_violation(Violation(
                code="ONTO-005",
                message=f"Evidence path missing for concept {concept_id}: {evidence_path}",
                path=str(self.project_path / evidence_path),
                severity=Severity.LOW,
                layer=7,
                suggestion="Update evidence path or provide documented justification"
            ))

        existence_coverage = round(with_predicates / max(len(concepts), 1), 2)
        truth_coverage = round(with_truth / max(len(concepts), 1), 2)
        layer7_score = round((existence_coverage + truth_coverage) / 2, 2)

        self.result.metadata["layer7_ontology"] = {
            "concepts": len(concepts),
            "concepts_with_predicates": with_predicates,
            "concepts_with_truth_maintenance": with_truth,
            "existence_coverage": existence_coverage,
            "truth_maintenance_coverage": truth_coverage,
            "evidence_missing": evidence_warnings,
            "ontology_rules_defined": bool(ontology_rules)
        }
        self.result.scores["layer_7"] = layer7_score
        self.result.scores["layer_7_ontological"] = layer7_score

    def _compute_scores(self) -> None:
        """Compute compliance scores."""
        # Overall score (inverse of violation count, normalized)
        total_possible = len(self.layers) * 10  # 10 checks per layer
        total_violations = len(self.result.violations) + (len(self.result.warnings) * 0.5)
        overall_score = max(0.0, 1.0 - (total_violations / total_possible))
        self.result.scores["overall"] = round(overall_score, 2)

        # Layer-specific scores
        for layer in self.layers:
            existing_score = self.result.scores.get(f"layer_{layer}")
            if existing_score is not None:
                layer_score = existing_score
            else:
                layer_violations = self.result.get_violations_by_layer(layer)
                layer_score = max(0.0, 1.0 - (len(layer_violations) / 10.0))
                if layer == 5 and "layer5_ecology" in self.result.metadata:
                    layer_score = self.result.metadata["layer5_ecology"].get("ecological_health_score", layer_score)
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

    layer6_meta = result.metadata.get("layer6_verification")
    if layer6_meta:
        lines.append("Layer 6 Verification Summary:")
        lines.append(f"  Proof artifacts: {layer6_meta.get('artifact_count', 0)}")
        lines.append(f"  Proof dirs scanned: {', '.join(layer6_meta.get('proof_directories_scanned', [])) or 'none'}")
        lines.append(f"  Tools enabled: {', '.join(layer6_meta.get('tools_enabled', [])) or 'none'}")
        lines.append(f"  Coverage score: {layer6_meta.get('coverage_score', 0.0):.2f}")
        if layer6_meta.get("validation_checks"):
            lines.append("  Validation checks:")
            for check in layer6_meta.get("validation_checks", []):
                status = check.get("status", "unknown")
                lines.append(f"    - {status}: {check.get('artifact', check.get('reason', ''))}")
        lines.append("")

    layer7_meta = result.metadata.get("layer7_ontology")
    if layer7_meta:
        lines.append("Layer 7 Ontology Summary:")
        lines.append(f"  Concepts with predicates: {layer7_meta.get('concepts_with_predicates', 0)}/{layer7_meta.get('concepts', 0)}")
        lines.append(f"  Concepts with truth maintenance: {layer7_meta.get('concepts_with_truth_maintenance', 0)}/{layer7_meta.get('concepts', 0)}")
        lines.append(f"  Existence coverage: {layer7_meta.get('existence_coverage', 0.0):.2f}")
        lines.append(f"  Truth maintenance coverage: {layer7_meta.get('truth_maintenance_coverage', 0.0):.2f}")
        if layer7_meta.get("evidence_missing"):
            lines.append("  Evidence paths missing:")
            for warning in layer7_meta.get("evidence_missing", []):
                lines.append(f"    - {warning}")
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

    parser.add_argument(
        "--verify-artifacts",
        action="store_true",
        help="Run optional Layer 6 proof artifact checks"
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
            layers=layers,
            verify_artifacts=args.verify_artifacts
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
