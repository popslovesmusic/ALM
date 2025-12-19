"""Performance and hardening utilities for the ALM runtime envelope."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import numpy as np

from .constants import L2_CACHE_BUDGET_BYTES
from .state import stencil_payload_bytes

# Allowed AVX2 intrinsic names drawn from the blueprint governance. These mirror
# the branchless, lane-uniform operations permitted for the SIMD path and avoid
# reductions, shuffles, or masked control flow.
ALLOWED_AVX2_INTRINSICS = (
    "_mm256_set1_ps",
    "_mm256_setzero_ps",
    "_mm256_load_ps",
    "_mm256_loadu_ps",
    "_mm256_store_ps",
    "_mm256_add_ps",
    "_mm256_sub_ps",
    "_mm256_mul_ps",
    "_mm256_fmadd_ps",
)

_INTRINSIC_PATTERN = re.compile(r"_mm256_[A-Za-z0-9_]+")
_CONST_PATTERN = re.compile(
    r"inline constexpr std::size_t\s+(?P<name>k[A-Za-z0-9_]+)\s*=\s*(?P<value>[0-9_]+)U?;"
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


def extract_intrinsics_from_header(header: Path) -> Sequence[str]:
    """Parse AVX2 intrinsic names from a C++ header for allow-list checks."""

    content = header.read_text(encoding="utf-8")
    return sorted(set(_INTRINSIC_PATTERN.findall(content)))


<<<<<<< ours
=======
def collect_intrinsics_from_tree(root: Path, pattern: str = "*.hpp") -> Sequence[str]:
    """Aggregate unique AVX2 intrinsics across a header tree for compliance checks."""

    intrinsics: set[str] = set()
    for header in root.rglob(pattern):
        if not header.is_file():
            continue
        intrinsics.update(extract_intrinsics_from_header(header))
    return sorted(intrinsics)


>>>>>>> theirs
def parse_cxx_constants(header: Path) -> Mapping[str, int]:
    """Extract literal std::size_t constants from a C++ header."""

    content = header.read_text(encoding="utf-8")
    matches = _CONST_PATTERN.finditer(content)
    parsed = {match.group("name"): int(match.group("value")) for match in matches}
    return parsed


__all__ = [
    "ALLOWED_AVX2_INTRINSICS",
<<<<<<< ours
=======
    "collect_intrinsics_from_tree",
>>>>>>> theirs
    "extract_intrinsics_from_header",
    "parse_cxx_constants",
    "residency_report",
    "validate_intrinsics_used",
]
