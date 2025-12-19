"""Performance profiling and SIMD hardening utilities."""

import numpy as np
import pytest

from alm import (
    ALLOWED_AVX2_INTRINSICS,
    L2_CACHE_BUDGET_BYTES,
    residency_report,
    stencil_payload_bytes,
    validate_intrinsics_used,
)


def test_residency_report_headroom_and_budget() -> None:
    report = residency_report()

    assert report["payload_bytes"] == stencil_payload_bytes()
    assert report["budget_bytes"] == L2_CACHE_BUDGET_BYTES
    assert report["within_budget"] is True
    assert report["headroom_bytes"] == L2_CACHE_BUDGET_BYTES - stencil_payload_bytes()


def test_residency_report_detects_overflow() -> None:
    report = residency_report(np.float64)

    assert report["within_budget"] is False
    assert report["headroom_bytes"] == L2_CACHE_BUDGET_BYTES - stencil_payload_bytes(np.float64)


def test_intrinsic_allowlist_rejects_disallowed_ops() -> None:
    allowed = list(ALLOWED_AVX2_INTRINSICS)
    # Adding a forbidden intrinsic should trigger validation
    with pytest.raises(ValueError, match="disallowed AVX2 intrinsics"):
        validate_intrinsics_used(allowed + ["_mm256_hadd_ps"])


def test_intrinsic_allowlist_accepts_subset() -> None:
    subset = ALLOWED_AVX2_INTRINSICS[:3]

    validate_intrinsics_used(subset)
