"""Performance and hardening utilities for the ALM runtime envelope."""

from __future__ import annotations

from typing import Iterable, Mapping

import numpy as np

from .constants import L2_CACHE_BUDGET_BYTES
from .state import stencil_payload_bytes

# Allowed AVX2 intrinsic names drawn from the blueprint governance. These mirror
# the branchless, lane-uniform operations permitted for the SIMD path and avoid
# reductions, shuffles, or masked control flow.
ALLOWED_AVX2_INTRINSICS = (
    "_mm256_set1_ps",
    "_mm256_load_ps",
    "_mm256_store_ps",
    "_mm256_add_ps",
    "_mm256_sub_ps",
    "_mm256_mul_ps",
    "_mm256_fmadd_ps",
)


def residency_report(
    dtype: np.dtype = np.float32, budget_bytes: int = L2_CACHE_BUDGET_BYTES
) -> Mapping[str, int | bool]:
    """Return a residency snapshot for the four-slice stencil payload."""

    payload = stencil_payload_bytes(dtype)
    headroom = budget_bytes - payload
    return {
        "payload_bytes": payload,
        "budget_bytes": budget_bytes,
        "headroom_bytes": headroom,
        "within_budget": payload <= budget_bytes,
    }


def validate_intrinsics_used(intrinsics: Iterable[str]) -> None:
    """Ensure the provided intrinsics stay within the allowed AVX2 set."""

    invalid = sorted(set(intrinsics).difference(ALLOWED_AVX2_INTRINSICS))
    if invalid:
        raise ValueError(
            "Encountered disallowed AVX2 intrinsics: " + ", ".join(invalid)
        )


__all__ = ["ALLOWED_AVX2_INTRINSICS", "residency_report", "validate_intrinsics_used"]
