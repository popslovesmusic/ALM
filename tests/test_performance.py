from pathlib import Path

import pytest

from alm.constants import L2_CACHE_BUDGET_BYTES
from alm.performance import (
    ALLOWED_AVX2_INTRINSICS,
    extract_intrinsics_from_header,
    parse_cxx_constants,
    residency_report,
    validate_intrinsics_used,
)
from alm.state import stencil_payload_bytes


def test_residency_report_matches_python_budget():
    report = residency_report()
    assert report["payload_bytes"] == stencil_payload_bytes()
    assert report["budget_bytes"] == L2_CACHE_BUDGET_BYTES
    assert report["headroom_bytes"] == report["budget_bytes"] - report["payload_bytes"]
    assert report["within_budget"]


def test_kernel_intrinsics_constrained_to_allow_list():
    header = Path("alm/core/include/alm/kernel.hpp")
    intrinsics = extract_intrinsics_from_header(header)
    validate_intrinsics_used(intrinsics)
    for intrinsic in intrinsics:
        assert intrinsic in ALLOWED_AVX2_INTRINSICS


def test_cxx_residency_constants_are_literal_and_consistent():
    header = Path("alm/core/include/alm/performance.hpp")
    constants = parse_cxx_constants(header)

    required = {"kL2CacheBudgetBytes", "kStencilBytesLiteral", "kCacheHeadroomBytes"}
    missing = required.difference(constants)
    if missing:
        pytest.fail(f"missing residency constants in C++ header: {sorted(missing)}")

    assert constants["kStencilBytesLiteral"] <= constants["kL2CacheBudgetBytes"]
    assert constants["kCacheHeadroomBytes"] == constants["kL2CacheBudgetBytes"] - constants[
        "kStencilBytesLiteral"
    ]
