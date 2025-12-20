from pathlib import Path

import pytest

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
from alm.constants import L2_CACHE_BUDGET_BYTES, STENCIL_ORDER
from alm.performance import (
    ALLOWED_AVX2_INTRINSICS,
    extract_build_guard_markers,
    collect_intrinsics_from_tree,
    extract_intrinsics_from_header,
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
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
>>>>>>> theirs
=======
    parse_forbidden_flags,
    parse_compile_options,
    parse_global_compile_options,
>>>>>>> theirs
=======
    parse_canonical_compile_options,
    parse_forbidden_flags,
    parse_compile_options,
    parse_global_compile_options,
>>>>>>> theirs
=======
    parse_canonical_compile_options,
    parse_canonical_compile_option_allowlist,
    parse_forbidden_flags,
    parse_compile_options,
    parse_global_compile_options,
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
    parse_canonical_compile_options,
    parse_canonical_compile_option_allowlist,
    parse_forbidden_flags,
    parse_flag_scopes,
    parse_compile_options,
    parse_global_compile_options,
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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
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
=======
>>>>>>> theirs
    expected_block_bytes = geom_constants["kLaneCount"] * 4  # sizeof(float)
    expected_array_bytes = expected_block_bytes * geom_constants["kLaneBlocks"]
    expected_frame_bytes = expected_array_bytes * geom_constants["kRegisterCount"]
    expected_stencil_bytes = expected_slice_bytes * geom_constants["kStencilSlices"]
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
=======
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
        "kStencilBytesLiteral"
    ]
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
=======
>>>>>>> theirs
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
=======
>>>>>>> theirs
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
=======
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


def test_core_compile_options_include_warning_hardening():
    cmake_lists = Path("alm/core/CMakeLists.txt")
    options = set(parse_compile_options(cmake_lists))

    required = {"-Wall", "-Wextra", "-Wpedantic"}
    missing = required.difference(options)

    if missing:
        pytest.fail(f"missing warning hardening options for canonical build: {sorted(missing)}")


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
def test_core_cmake_rejects_forbidden_fast_math_flags():
    cmake_lists = Path("alm/core/CMakeLists.txt")
    forbidden = set(parse_forbidden_flags(cmake_lists))

    expected = {
        "-ffast-math",
        "-Ofast",
        "-ffinite-math-only",
        "-funsafe-math-optimizations",
    }

    missing = expected.difference(forbidden)
    if missing:
        pytest.fail(f"missing forbidden flag guard entries: {sorted(missing)}")

    content = cmake_lists.read_text(encoding="utf-8")
    for scope in (
        "CMAKE_CXX_FLAGS",
        "CMAKE_CXX_FLAGS_RELEASE",
        "CMAKE_CXX_FLAGS_RELWITHDEBINFO",
        "CMAKE_CXX_FLAGS_MINSIZEREL",
        "CMAKE_CXX_FLAGS_DEBUG",
    ):
        assert scope in content

    assert "Forbidden compiler flag detected" in content


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
=======
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
def test_core_compile_options_source_from_canonical_list():
    top_level_canonical = set(parse_canonical_compile_options(Path("CMakeLists.txt")))
    assert top_level_canonical, "canonical compile options must be defined at the project root"

    cmake_lists = Path("alm/core/CMakeLists.txt")
    options = set(parse_compile_options(cmake_lists))
    missing = top_level_canonical.difference(options)

    if missing:
        pytest.fail(f"core compile options diverged from canonical list: {sorted(missing)}")

    content = cmake_lists.read_text(encoding="utf-8")
    assert "ALM_CANONICAL_COMPILE_OPTIONS" in content
    assert "Canonical compile options must be provided" in content


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
def test_canonical_compile_option_allowlist_freezes_permitted_options():
    cmake_lists = Path("CMakeLists.txt")
    allowlist = set(parse_canonical_compile_option_allowlist(cmake_lists))
    canonical = set(parse_canonical_compile_options(cmake_lists))

    assert allowlist, "canonical compile option allowlist must be defined at the project root"
    assert canonical == allowlist

    content = cmake_lists.read_text(encoding="utf-8")
    assert "Non-canonical compile option detected" in content
    assert "Canonical compile option missing" in content

    core_content = Path("alm/core/CMakeLists.txt").read_text(encoding="utf-8")
    assert "Non-canonical compile option detected in core scope" in core_content
    assert "Canonical compile option missing from core scope" in core_content


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
def test_top_level_flag_scopes_use_canonical_allowlist_string():
    cmake_lists = Path("CMakeLists.txt")
    scopes = parse_flag_scopes(cmake_lists)

    expected = "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}"
    for scope in (
        "CMAKE_CXX_FLAGS",
        "CMAKE_CXX_FLAGS_RELEASE",
        "CMAKE_CXX_FLAGS_RELWITHDEBINFO",
        "CMAKE_CXX_FLAGS_MINSIZEREL",
        "CMAKE_CXX_FLAGS_DEBUG",
    ):
        assert scopes.get(scope) == expected


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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def test_top_level_cmake_constrains_compiler_and_flags():
    cmake_lists = Path("CMakeLists.txt")
    content = cmake_lists.read_text(encoding="utf-8")

    assert "CMAKE_CXX_COMPILER_ID MATCHES \"GNU|Clang\"" in content
    assert "check_cxx_compiler_flag" in content
    for flag in ("-mavx2", "-fno-fast-math", "-ffp-contract=off"):
        assert flag in content


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
def test_top_level_compile_options_pin_avx2_and_deterministic_fp():
    cmake_lists = Path("CMakeLists.txt")
    options = set(parse_global_compile_options(cmake_lists))

    required = {"-mavx2", "-fno-fast-math", "-ffp-contract=off"}
    missing = required.difference(options)

    if missing:
        pytest.fail(f"missing required global compile options for deterministic AVX2 build: {sorted(missing)}")


def test_top_level_compile_options_include_warning_hardening():
    cmake_lists = Path("CMakeLists.txt")
    options = set(parse_global_compile_options(cmake_lists))

    required = {"-Wall", "-Wextra", "-Wpedantic"}
    missing = required.difference(options)

    if missing:
        pytest.fail(f"missing global warning hardening options: {sorted(missing)}")


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
def test_top_level_cmake_rejects_forbidden_fast_math_flags():
    cmake_lists = Path("CMakeLists.txt")
    forbidden = set(parse_forbidden_flags(cmake_lists))

    expected = {
        "-ffast-math",
        "-Ofast",
        "-ffinite-math-only",
        "-funsafe-math-optimizations",
    }

    missing = expected.difference(forbidden)
    if missing:
        pytest.fail(f"missing forbidden flag guard entries: {sorted(missing)}")

    content = cmake_lists.read_text(encoding="utf-8")
    for scope in (
        "CMAKE_CXX_FLAGS",
        "CMAKE_CXX_FLAGS_RELEASE",
        "CMAKE_CXX_FLAGS_RELWITHDEBINFO",
        "CMAKE_CXX_FLAGS_MINSIZEREL",
        "CMAKE_CXX_FLAGS_DEBUG",
    ):
        assert scope in content

    assert "Forbidden compiler flag detected" in content


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
=======
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
def test_core_flag_scopes_use_canonical_allowlist_string():
    top_level_allowlist = parse_canonical_compile_option_allowlist(Path("CMakeLists.txt"))
    assert top_level_allowlist

    scopes = parse_flag_scopes(Path("alm/core/CMakeLists.txt"))

    expected = "${ALM_CANONICAL_COMPILE_OPTIONS_STRING}"
    for scope in (
        "CMAKE_CXX_FLAGS",
        "CMAKE_CXX_FLAGS_RELEASE",
        "CMAKE_CXX_FLAGS_RELWITHDEBINFO",
        "CMAKE_CXX_FLAGS_MINSIZEREL",
        "CMAKE_CXX_FLAGS_DEBUG",
    ):
        assert scopes.get(scope) == expected


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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def test_top_level_canonical_compile_options_match_global_application():
    cmake_lists = Path("CMakeLists.txt")
    canonical = set(parse_canonical_compile_options(cmake_lists))
    options = set(parse_global_compile_options(cmake_lists))

    assert canonical, "canonical compile options list must be declared at top level"
    assert canonical == options


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
def test_cxx_standard_enforced_without_extensions():
    top_level = Path("CMakeLists.txt").read_text(encoding="utf-8")
    core = Path("alm/core/CMakeLists.txt").read_text(encoding="utf-8")

    assert "CMAKE_CXX_STANDARD 20" in top_level
    assert "CMAKE_CXX_STANDARD_REQUIRED ON" in top_level
    assert "CMAKE_CXX_EXTENSIONS OFF" in top_level

    assert "CXX_STANDARD 20" in core
    assert "CXX_STANDARD_REQUIRED YES" in core
    assert "CXX_EXTENSIONS NO" in core


def test_build_guards_cover_binary32_and_avx2_requirements():
    build_header = Path("alm/core/include/alm/build.hpp")
    markers = extract_build_guard_markers(build_header)

    required = {
        "__cplusplus >= 202002L",
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
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
>>>>>>> theirs
=======
        "sizeof(void*) == 8",
        "std::endian::native == std::endian::little",
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
    }

    missing = required.difference(markers)

    if missing:
        pytest.fail(f"missing build guard markers: {sorted(missing)}")
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


def test_core_cmake_rejects_non_64bit_layouts():
    cmake_lists = Path("alm/core/CMakeLists.txt").read_text(encoding="utf-8")

    assert "CMAKE_SIZEOF_VOID_P" in cmake_lists
    assert "requires 64-bit pointers" in cmake_lists
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
    assert "CMAKE_CXX_BYTE_ORDER" in cmake_lists
    assert "requires little-endian layout" in cmake_lists
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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    assert "CMAKE_CXX_BYTE_ORDER" in cmake_lists
    assert "requires little-endian layout" in cmake_lists


def test_top_level_cmake_rejects_non_64bit_or_big_endian():
    cmake_lists = Path("CMakeLists.txt").read_text(encoding="utf-8")

    assert "CMAKE_SIZEOF_VOID_P" in cmake_lists
    assert "requires 64-bit pointers" in cmake_lists
    assert "CMAKE_CXX_BYTE_ORDER" in cmake_lists
    assert "TestBigEndian" in cmake_lists
    assert "requires little-endian layout" in cmake_lists
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
