"""Performance and residency hardening for stencil buffers."""

import numpy as np
import pytest

from alm import (
    GRID_COLS,
    GRID_ROWS,
    LANES,
    NUM_REGISTERS,
    L2_CACHE_BUDGET_BYTES,
    StateSlice,
    assert_cache_residency,
    slice_payload_bytes,
    stencil_payload_bytes,
)


def test_slice_requires_contiguous_memory() -> None:
    non_contiguous = np.asfortranarray(
        np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=np.float32)
    )

    with pytest.raises(ValueError, match="C-contiguous"):
        StateSlice(non_contiguous)


def test_stencil_payload_within_cache_budget() -> None:
    payload = assert_cache_residency()

    assert payload == stencil_payload_bytes()
    assert payload <= L2_CACHE_BUDGET_BYTES


def test_double_precision_payload_rejected() -> None:
    with pytest.raises(ValueError, match="exceeds budget"):
        assert_cache_residency(np.float64)

    assert stencil_payload_bytes(np.float64) > L2_CACHE_BUDGET_BYTES
    assert slice_payload_bytes(np.float64) == stencil_payload_bytes(np.float64) / 4
