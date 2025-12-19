from pathlib import Path


REQUIRED_SECTIONS = [
    "Invariant 1: Uniform Law / No Lane Privilege",
    "Invariant 2: Paired-Lane Symmetry Preservation",
    "Invariant 3: Earned Asymmetry Only",
    "Invariant 4: Continuity (No Thresholds)",
    "Invariant 5: Pressure–Signal Orthogonality",
    "Invariant 6: Non-Coupled Observability",
    "Invariant 7: Scalar ↔ AVX2 Ontology Equivalence",
    "Invariant 8: Auxiliary Lane Containment",
    "Required Test Matrix",
]


def test_invariant_spec_sections_present():
    spec_text = Path("docs/tests_and_support/INVARIANT_REGRESSION_TESTS.md").read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        assert section in spec_text, f"missing invariant section: {section}"
