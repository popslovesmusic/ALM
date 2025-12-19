import numpy as np

from alm.config import DeterministicConfig
from alm.constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
from alm.state import (
    StateSlice,
    StencilBuffers,
    assert_cache_residency,
    slice_payload_bytes,
    stencil_payload_bytes,
)


def test_state_slice_shape_and_contiguity():
    data = np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=np.float32)
    slice_obj = StateSlice(data)
    assert slice_obj.data.flags["C_CONTIGUOUS"]


def test_stencil_rotation_preserves_order():
    config = DeterministicConfig(seed=1)
    buffers = StencilBuffers.build(config.initializer())

    before = [buffers.future.data.copy(), buffers.now.data.copy(), buffers.recent.data.copy(), buffers.stable.data.copy()]

    buffers.advance()

    assert np.array_equal(buffers.future.data, before[1])
    assert np.array_equal(buffers.now.data, before[2])
    assert np.array_equal(buffers.recent.data, before[3])
    assert np.array_equal(buffers.stable.data, before[0])

    assert list(STENCIL_ORDER) == ["FUTURE", "NOW", "RECENT", "STABLE"]


def test_cache_residency_budget():
    slice_bytes = slice_payload_bytes()
    stencil_bytes = stencil_payload_bytes()
    assert stencil_bytes == slice_bytes * len(STENCIL_ORDER)
    assert_cache_residency()
