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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
>>>>>>> theirs
=======
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
>>>>>>> theirs
=======
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
>>>>>>> theirs
=======
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
_FORBIDDEN_FLAGS_PATTERN = re.compile(
    r"set\(ALM_FORBIDDEN_FLAGS\s+(?P<body>[^\)]*)\)", re.MULTILINE
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
)
_BUILD_GUARD_MARKERS = (
    "__cplusplus >= 202002L",
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
_COMPILE_OPTIONS_PATTERN = re.compile(
    r"target_compile_options\(alm_core\s+INTERFACE(?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
_ADD_COMPILE_OPTIONS_PATTERN = re.compile(
    r"add_compile_options\((?P<body>[^\)]*)\)", re.MULTILINE | re.DOTALL
)
_FORBIDDEN_FLAGS_PATTERN = re.compile(
    r"set\(ALM_FORBIDDEN_FLAGS\s+(?P<body>[^\)]*)\)", re.MULTILINE
>>>>>>> theirs
)
_BUILD_GUARD_MARKERS = (
    "__cplusplus >= 202002L",
    "sizeof(void*) == 8",
    "std::endian::native == std::endian::little",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    "__AVX2__",
    "__FAST_MATH__",
    "__FINITE_MATH_ONLY__",
    "numeric_limits<float>::is_iec559",
    "sizeof(float) == 4",
    "numeric_limits<float>::radix == 2",
    "numeric_limits<float>::digits == 24",
    "numeric_limits<float>::max_exponent == 128",
    "numeric_limits<float>::min_exponent == -125",
    "numeric_limits<float>::digits10 == 6",
)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs


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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def collect_intrinsics_from_tree(root: Path, pattern: str = "*.hpp") -> Sequence[str]:
    """Aggregate unique AVX2 intrinsics across a header tree for compliance checks."""

    intrinsics: set[str] = set()
    for header in root.rglob(pattern):
        if not header.is_file():
            continue
        intrinsics.update(extract_intrinsics_from_header(header))
    return sorted(intrinsics)


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def parse_cxx_constants(header: Path) -> Mapping[str, int]:
    """Extract literal std::size_t constants from a C++ header."""

    content = header.read_text(encoding="utf-8")
    matches = _CONST_PATTERN.finditer(content)
    parsed = {match.group("name"): int(match.group("value")) for match in matches}
    return parsed


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
__all__ = [
    "ALLOWED_AVX2_INTRINSICS",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
    "collect_intrinsics_from_tree",
>>>>>>> theirs
=======
    "collect_intrinsics_from_tree",
>>>>>>> theirs
=======
    "collect_intrinsics_from_tree",
>>>>>>> theirs
    "extract_intrinsics_from_header",
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def parse_compile_options(cmake_lists: Path) -> Sequence[str]:
    """Extract canonical compile options for the core target."""

    content = cmake_lists.read_text(encoding="utf-8")
    match = _COMPILE_OPTIONS_PATTERN.search(content)
    if not match:
        return []

    body = match.group("body")
    tokens: list[str] = []

    for match in re.finditer(r"\$<[^>]+>:(?P<opts>[^>]*)>", body):
        tokens.extend(match.group("opts").split())

    if not tokens:
        for raw_line in body.splitlines():
            line = raw_line.strip()
            if line:
                tokens.extend(line.split())

    return tokens


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
def parse_global_compile_options(cmake_lists: Path) -> Sequence[str]:
    """Extract project-wide compile options declared via add_compile_options."""

    content = cmake_lists.read_text(encoding="utf-8")
    matches = list(_ADD_COMPILE_OPTIONS_PATTERN.finditer(content))
    tokens: list[str] = []

    for match in matches:
        body = match.group("body")

        for expr in re.finditer(r"\$<[^>]+>:(?P<opts>[^>]*)>", body):
            tokens.extend(expr.group("opts").split())

        if not tokens:
            for raw_line in body.splitlines():
                line = raw_line.strip()
                if line:
                    tokens.extend(line.split())

    return tokens


>>>>>>> theirs
def extract_build_guard_markers(build_header: Path) -> set[str]:
    """Collect required guard markers from the build guard header."""

    content = build_header.read_text(encoding="utf-8")
    return {marker for marker in _BUILD_GUARD_MARKERS if marker in content}


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def parse_forbidden_flags(cmake_lists: Path) -> Sequence[str]:
    """Extract forbidden compiler flags declared in the core CMake configuration."""

    content = cmake_lists.read_text(encoding="utf-8")
    match = _FORBIDDEN_FLAGS_PATTERN.search(content)
    if not match:
        return []

    body = match.group("body")
    tokens: list[str] = []

    for raw in body.split():
        token = raw.strip("\" ")
        if token:
            tokens.append(token)

    return tokens


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
__all__ = [
    "ALLOWED_AVX2_INTRINSICS",
    "collect_intrinsics_from_tree",
    "extract_intrinsics_from_header",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    "parse_compile_options",
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
>>>>>>> theirs
=======
    "extract_build_guard_markers",
    "parse_forbidden_flags",
    "parse_compile_options",
    "parse_global_compile_options",
>>>>>>> theirs
    "parse_cxx_constants",
    "residency_report",
    "validate_intrinsics_used",
]
