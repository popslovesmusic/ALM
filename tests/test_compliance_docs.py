from pathlib import Path

import pytest


REQUIRED_SECTIONS = [
    "Ingest, Topology, and Timing Guards",
    "Coefficient Canonicalization and Chromatic Structure",
    "Deterministic Time Stencil and Kernel Equivalence",
    "Boundary Conditioning and Focus Orthogonality",
    "Compile-Time Guardrails and Canonical Flags",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
    "Stress Resilience and Observability Traceability",
>>>>>>> theirs
=======
    "Toolchain and Architecture Enforcement",
    "Stress Resilience and Observability Traceability",
>>>>>>> theirs
=======
    "Toolchain and Architecture Enforcement",
    "Stress Resilience and Observability Traceability",
>>>>>>> theirs
]

REQUIRED_ARTIFACTS = [
    "alm/core/include/alm/topology.hpp",
    "alm/core/include/alm/ingest.hpp",
    "alm/core/include/alm/coefficients.hpp",
    "alm/core/include/alm/constants.hpp",
    "alm/core/include/alm/stencil.hpp",
    "alm/core/include/alm/kernel.hpp",
    "alm/core/include/alm/boundary.hpp",
    "alm/core/include/alm/focus.hpp",
    "alm/core/include/alm/build.hpp",
    "alm/core/checks.cpp",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
    "alm/core/include/alm/config.hpp",
>>>>>>> theirs
=======
    "alm/core/include/alm/config.hpp",
>>>>>>> theirs
    "alm/core/include/alm/observability.hpp",
    "src/alm/performance.py",
]

COVERAGE_ITEMS = [
    "tests/test_performance.py",
    "tests/test_residency.py",
    "tests/test_invariants.py",
<<<<<<< ours
<<<<<<< ours
    "tests/test_compliance_docs.py",
>>>>>>> theirs
=======
    "tests/test_hardening.py",
    "tests/test_compliance_docs.py",
>>>>>>> theirs
=======
    "tests/test_hardening.py",
    "tests/test_stress_paths.py",
    "tests/test_compliance_docs.py",
>>>>>>> theirs
]


def test_compliance_map_includes_required_sections_and_artifacts():
    compliance_map = Path("docs/COMPLIANCE_MAP.md")
    assert compliance_map.exists(), "compliance map must be present for audit traceability"

    content = compliance_map.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        assert section in content, f"missing compliance section: {section}"

    for artifact in REQUIRED_ARTIFACTS:
        assert artifact in content, f"missing implementation artifact mapping: {artifact}"


@pytest.mark.parametrize(
    "reference",
    [
        "TOPOLOGY & INGEST CONTRACT.md",
        "TIME_STENCIL_MECHANICS.md",
        "COEFFICIENT CANONICALIZATION CONTRACT.md",
        "ALM Lane Map and Coefficient Tables Spec v0.md",
        "Relational Kernel Law Spec v0.md",
        "AVX2_KERNEL_RULES.md",
        "Resonant Semantic Conditioning via Dynamic Boundary Constraints.md",
        "PRESSURE_SIGNAL_ORTHOGONALITY.md",
        "JITTER_FOCUS_TRANSFER.md",
        "CACHE_RESIDENCY_PROOF.md",
        "SIMD as Ontology.md",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
        "PRESSURE_AND_DECAY_LAWS.md",
        "SPIRAL_OBSERVABLES.md",
>>>>>>> theirs
=======
        "PRESSURE_AND_DECAY_LAWS.md",
        "SPIRAL_OBSERVABLES.md",
>>>>>>> theirs
=======
        "PRESSURE_AND_DECAY_LAWS.md",
        "SPIRAL_OBSERVABLES.md",
>>>>>>> theirs
    ],
)
def test_compliance_map_references_canonical_sources(reference):
    content = Path("docs/COMPLIANCE_MAP.md").read_text(encoding="utf-8")
    assert reference in content, f"missing blueprint reference in compliance map: {reference}"
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs


def test_compliance_map_mentions_regression_coverage():
    content = Path("docs/COMPLIANCE_MAP.md").read_text(encoding="utf-8")

    for coverage_item in COVERAGE_ITEMS:
        assert coverage_item in content, f"missing regression coverage item: {coverage_item}"
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
