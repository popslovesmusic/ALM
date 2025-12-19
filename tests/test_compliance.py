import pytest

from alm.compliance import COMPONENT_REFERENCES, component_references, references_for


EXPECTED_KEYS = {
    "state.StencilBuffers",
    "coefficients.CoefficientTables",
    "kernel.scalar_step",
    "avx2.avx2_step",
    "ingest.IngestController",
}


def test_component_references_are_copied():
    mapping = component_references()
    assert EXPECTED_KEYS.issubset(mapping.keys())

    original = references_for("kernel.scalar_step")
    mapping["kernel.scalar_step"].append("dummy")

    assert references_for("kernel.scalar_step") == original


def test_references_for_unknown_component():
    with pytest.raises(KeyError):
        references_for("unknown.component")


def test_component_references_non_empty():
    for key, references in COMPONENT_REFERENCES.items():
        assert references, f"references missing for {key}"
        for ref in references:
            assert ref.startswith("docs/blueprint/")
