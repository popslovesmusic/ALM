import numpy as np

from alm.boundary import apply_resonant_boundary, boundary_envelope
from alm.constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS
from alm.focus import FocusTracker


def test_boundary_envelope_resonant_behavior():
    envelope = boundary_envelope(resonance=0.2, phase=np.pi / 4)

    assert envelope.shape == (GRID_ROWS, GRID_COLS, 1, 1)
    assert np.all(envelope > 0)

    center = envelope[GRID_ROWS // 2, GRID_COLS // 2, 0, 0]
    edge = envelope[0, 0, 0, 0]

    assert not np.isclose(center, edge)
    assert envelope.std() > 0.0


def test_resonant_boundary_preserves_lane_symmetry():
    rng = np.random.default_rng(0)
    slice_data = rng.standard_normal((GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES)).astype(
        np.float32
    )

    masked = apply_resonant_boundary(slice_data.copy(), resonance=0.3)
    expected = slice_data * boundary_envelope(resonance=0.3)

    assert np.allclose(masked, expected)

    lane_difference = masked[..., 0] - masked[..., 1]
    expected_difference = expected[..., 0] - expected[..., 1]
    assert np.allclose(lane_difference, expected_difference)


def test_focus_handoff_orthogonal_to_pressure():
    jitter = np.sin(np.linspace(0.0, np.pi, GRID_ROWS * GRID_COLS)).reshape(GRID_ROWS, GRID_COLS)

    tracker_a = FocusTracker()
    focus_low_pressure = tracker_a.handoff(jitter, pressure=0.25)

    tracker_b = FocusTracker()
    focus_high_pressure = tracker_b.handoff(jitter, pressure=2.0)

    assert np.allclose(focus_low_pressure, focus_high_pressure)
    assert np.isclose(focus_low_pressure.sum(), 1.0)


def test_focus_handoff_conserves_topology_under_jitter():
    tracker = FocusTracker()
    jitter = np.zeros((GRID_ROWS, GRID_COLS), dtype=np.float32)
    focus = tracker.handoff(jitter)

    assert np.allclose(focus, np.full((GRID_ROWS, GRID_COLS), 1.0 / (GRID_ROWS * GRID_COLS)))

    jitter_wave = np.sin(np.linspace(0, 2 * np.pi, GRID_ROWS * GRID_COLS)).reshape(
        GRID_ROWS, GRID_COLS
    )

    shifted_focus = tracker.handoff(jitter_wave)
    assert np.isclose(shifted_focus.sum(), 1.0)
    assert shifted_focus.min() > 0.0
