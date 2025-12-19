from pathlib import Path

import pytest

from alm.constants import L2_CACHE_BUDGET_BYTES
from alm.performance import (
    ALLOWED_AVX2_INTRINSICS,
<<<<<<< ours
=======
    collect_intrinsics_from_tree,
>>>>>>> theirs
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


<<<<<<< ours
def test_cxx_residency_constants_are_literal_and_consistent():
    header = Path("alm/core/include/alm/performance.hpp")
    constants = parse_cxx_constants(header)

    required = {"kL2CacheBudgetBytes", "kStencilBytesLiteral", "kCacheHeadroomBytes"}
    missing = required.difference(constants)
    if missing:
        pytest.fail(f"missing residency constants in C++ header: {sorted(missing)}")

    assert constants["kStencilBytesLiteral"] <= constants["kL2CacheBudgetBytes"]
    assert constants["kCacheHeadroomBytes"] == constants["kL2CacheBudgetBytes"] - constants[
=======
def test_all_headers_intrinsics_constrained_to_allow_list():
    headers_root = Path("alm/core/include/alm")
    intrinsics = collect_intrinsics_from_tree(headers_root)
    validate_intrinsics_used(intrinsics)
    for intrinsic in intrinsics:
        assert intrinsic in ALLOWED_AVX2_INTRINSICS


def test_cxx_residency_constants_are_literal_and_consistent():
    performance_header = Path("alm/core/include/alm/performance.hpp")
    constants_header = Path("alm/core/include/alm/constants.hpp")

    perf_constants = parse_cxx_constants(performance_header)
    geom_constants = parse_cxx_constants(constants_header)

    required = {
        "kL2CacheBudgetBytes",
        "kSliceElementsLiteral",
        "kSliceBytesLiteral",
        "kStencilBytesLiteral",
        "kCacheHeadroomBytes",
    }
    missing = required.difference(perf_constants)
    if missing:
        pytest.fail(f"missing residency constants in C++ header: {sorted(missing)}")

    expected_elements = (
        geom_constants["kRegisterCount"] * geom_constants["kLaneBlocks"] * geom_constants["kLaneCount"]
    )
    expected_slice_bytes = expected_elements * 4  # sizeof(float)
    expected_stencil_bytes = expected_slice_bytes * perf_constants["kStencilSlices"]

    assert perf_constants["kSliceElementsLiteral"] == expected_elements
    assert perf_constants["kSliceBytesLiteral"] == expected_slice_bytes
    assert perf_constants["kStencilBytesLiteral"] == expected_stencil_bytes
    assert perf_constants["kStencilBytesLiteral"] <= perf_constants["kL2CacheBudgetBytes"]
    assert perf_constants["kCacheHeadroomBytes"] == perf_constants["kL2CacheBudgetBytes"] - perf_constants[
>>>>>>> theirs
        "kStencilBytesLiteral"
    ]
