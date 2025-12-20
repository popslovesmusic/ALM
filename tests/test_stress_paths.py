import numpy as np
import pytest

from alm.constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS, STENCIL_ORDER
from alm.focus import FocusTracker
from alm.ingest import is_step_aligned, validate_frame_shape
from alm.observability import snapshot_scalar_field


def test_ingest_alignment_and_shape_guards():
    frame = np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS), dtype=np.float32)
    validate_frame_shape(frame)

    with pytest.raises(ValueError):
        validate_frame_shape(np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS - 1), dtype=np.float32))

    assert is_step_aligned(STENCIL_ORDER[0])
    for step in STENCIL_ORDER[1:]:
        assert not is_step_aligned(step)


def test_focus_handoff_preserves_normalization_under_jitter():
    rng = np.random.default_rng(0)
    jitter = rng.standard_normal((GRID_ROWS, GRID_COLS), dtype=np.float32)

    tracker = FocusTracker()
    initial = tracker.focus_map.copy()
    updated = tracker.handoff(jitter)

    assert updated.shape == (GRID_ROWS, GRID_COLS)
    assert np.isclose(updated.sum(), 1.0)
    assert not np.allclose(updated, initial)

    with pytest.raises(ValueError):
        tracker.handoff(np.zeros((GRID_ROWS - 1, GRID_COLS), dtype=np.float32))


def test_observability_snapshot_is_copy_and_shape_checked():
    state = np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS, 4), dtype=np.float32)
    snap = snapshot_scalar_field(state)

    assert snap.shape == state.shape
    assert np.array_equal(snap, state)
    snap[0, 0, 0, 0] = 1.0
    assert state[0, 0, 0, 0] == 0.0

    with pytest.raises(ValueError):
        snapshot_scalar_field(np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS - 1, 4), dtype=np.float32))

