from pathlib import Path

import pytest

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
from alm.constants import L2_CACHE_BUDGET_BYTES
from alm.performance import (
    ALLOWED_AVX2_INTRINSICS,
<<<<<<< ours
<<<<<<< ours
=======
    collect_intrinsics_from_tree,
>>>>>>> theirs
=======
    collect_intrinsics_from_tree,
>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
from alm.constants import L2_CACHE_BUDGET_BYTES, STENCIL_ORDER
from alm.performance import (
    ALLOWED_AVX2_INTRINSICS,
    collect_intrinsics_from_tree,
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
    extract_intrinsics_from_header,
=======
    extract_intrinsics_from_header,
    parse_compile_options,
>>>>>>> theirs
=======
    extract_intrinsics_from_header,
    parse_compile_options,
>>>>>>> theirs
=======
    extract_intrinsics_from_header,
    parse_compile_options,
>>>>>>> theirs
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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
        "kRegisterBlockBytesLiteral",
        "kRegisterArrayBytesLiteral",
        "kFrameBytesLiteral",
>>>>>>> theirs
=======
        "kRegisterBlockBytesLiteral",
        "kRegisterArrayBytesLiteral",
        "kFrameBytesLiteral",
>>>>>>> theirs
=======
        "kRegisterBlockBytesLiteral",
        "kRegisterArrayBytesLiteral",
        "kFrameBytesLiteral",
>>>>>>> theirs
=======
        "kRegisterBlockBytesLiteral",
        "kRegisterArrayBytesLiteral",
        "kFrameBytesLiteral",
>>>>>>> theirs
=======
        "kRegisterBlockBytesLiteral",
        "kRegisterArrayBytesLiteral",
        "kFrameBytesLiteral",
>>>>>>> theirs
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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    expected_stencil_bytes = expected_slice_bytes * perf_constants["kStencilSlices"]

    assert perf_constants["kSliceElementsLiteral"] == expected_elements
    assert perf_constants["kSliceBytesLiteral"] == expected_slice_bytes
    assert perf_constants["kStencilBytesLiteral"] == expected_stencil_bytes
    assert perf_constants["kStencilBytesLiteral"] <= perf_constants["kL2CacheBudgetBytes"]
    assert perf_constants["kCacheHeadroomBytes"] == perf_constants["kL2CacheBudgetBytes"] - perf_constants[
>>>>>>> theirs
=======
    expected_block_bytes = geom_constants["kLaneCount"] * 4  # sizeof(float)
    expected_array_bytes = expected_block_bytes * geom_constants["kLaneBlocks"]
    expected_frame_bytes = expected_array_bytes * geom_constants["kRegisterCount"]
    expected_stencil_bytes = expected_slice_bytes * perf_constants["kStencilSlices"]
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    expected_block_bytes = geom_constants["kLaneCount"] * 4  # sizeof(float)
    expected_array_bytes = expected_block_bytes * geom_constants["kLaneBlocks"]
    expected_frame_bytes = expected_array_bytes * geom_constants["kRegisterCount"]
    expected_stencil_bytes = expected_slice_bytes * geom_constants["kStencilSlices"]
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

    assert perf_constants["kRegisterBlockBytesLiteral"] == expected_block_bytes
    assert perf_constants["kRegisterArrayBytesLiteral"] == expected_array_bytes
    assert perf_constants["kFrameBytesLiteral"] == expected_frame_bytes
    assert perf_constants["kSliceElementsLiteral"] == expected_elements
    assert perf_constants["kSliceBytesLiteral"] == expected_slice_bytes
    assert perf_constants["kFrameBytesLiteral"] == perf_constants["kSliceBytesLiteral"]
    assert perf_constants["kStencilBytesLiteral"] == expected_stencil_bytes
    assert perf_constants["kStencilBytesLiteral"] <= perf_constants["kL2CacheBudgetBytes"]
    assert perf_constants["kCacheHeadroomBytes"] == perf_constants["kL2CacheBudgetBytes"] - perf_constants[
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
        "kStencilBytesLiteral"
    ]
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
        "kStencilBytesLiteral"
    ]


def test_cpp_stencil_slice_count_matches_python_ordering():
    constants_header = Path("alm/core/include/alm/constants.hpp")
    cpp_constants = parse_cxx_constants(constants_header)

    assert cpp_constants["kStencilSlices"] == len(STENCIL_ORDER)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
=======
=======
>>>>>>> theirs


def test_core_cmake_constrains_compiler_and_flags():
    cmake_lists = Path("alm/core/CMakeLists.txt")
    content = cmake_lists.read_text(encoding="utf-8")

    assert "CMAKE_CXX_COMPILER_ID MATCHES \"GNU|Clang\"" in content
    assert "check_cxx_compiler_flag" in content
    for flag in ("-mavx2", "-fno-fast-math", "-ffp-contract=off"):
        assert flag in content
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs


def test_core_compile_options_pin_avx2_and_deterministic_fp():
    cmake_lists = Path("alm/core/CMakeLists.txt")
    options = set(parse_compile_options(cmake_lists))

    required = {"-mavx2", "-fno-fast-math", "-ffp-contract=off"}
    missing = required.difference(options)

    if missing:
        pytest.fail(f"missing required compile options for deterministic AVX2 build: {sorted(missing)}")
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
