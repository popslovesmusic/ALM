"""Compliance reference mapping for ALM components."""

from __future__ import annotations

from typing import Dict, List, Mapping


COMPONENT_REFERENCES: Mapping[str, List[str]] = {
    "state.StencilBuffers": [
        "docs/blueprint/Time Stencil Mechanics.md",
        "docs/blueprint/TIME_STENCIL_MECHANICS.md",
    ],
    "coefficients.CoefficientTables": [
        "docs/blueprint/COEFFICIENT CANONICALIZATION CONTRACT.md",
        "docs/blueprint/ALM Lane Map and Coefficient Tables Spec v0.md",
    ],
    "kernel.scalar_step": ["docs/blueprint/Relational Kernel Law Spec v0.md"],
    "avx2.avx2_step": [
        "docs/blueprint/AVX2_KERNEL_RULES.md",
        "docs/blueprint/SIMD as Ontology.md",
    ],
    "ingest.IngestController": ["docs/blueprint/TOPOLOGY & INGEST CONTRACT.md"],
    "performance.validate_intrinsics_used": ["docs/blueprint/AVX2_KERNEL_RULES.md"],
    "performance.residency_report": ["docs/blueprint/CACHE_RESIDENCY_PROOF.md"],
    "observability.observable_snapshot": ["docs/blueprint/SPIRAL_OBSERVABLES.md"],
    "focus.FocusTracker": ["docs/blueprint/JITTER_FOCUS_TRANSFER.md"],
    "boundary.apply_resonant_boundary": [
        "docs/blueprint/Resonant Semantic Conditioning via Dynamic Boundary Constraints.md"
    ],
}


def component_references() -> Dict[str, List[str]]:
    """Return a copy of the component→reference mapping."""

    return {key: list(value) for key, value in COMPONENT_REFERENCES.items()}


def references_for(component: str) -> List[str]:
    """Return references for the provided component key."""

    if component not in COMPONENT_REFERENCES:
        raise KeyError(f"unknown component reference: {component}")
    return list(COMPONENT_REFERENCES[component])


__all__ = ["component_references", "references_for", "COMPONENT_REFERENCES"]
