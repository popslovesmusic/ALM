import numpy as np
import pytest

from alm import (
    GRID_COLS,
    GRID_ROWS,
    DeterministicConfig,
    FocusTracker,
    IngestController,
    StencilBuffers,
    avx2_step,
    build_canonical_coefficients,
    exercise_cadence,
    scalar_step,
)


def _buffers(seed: int) -> StencilBuffers:
    return StencilBuffers.build(DeterministicConfig(seed=seed).initializer())


def _frames_and_jitter(rng: np.random.Generator, steps: int):
    frames = [rng.standard_normal((GRID_ROWS, GRID_COLS), dtype=np.float32) for _ in range(steps)]
    jitters = [rng.standard_normal((GRID_ROWS, GRID_COLS), dtype=np.float32) * 0.1 for _ in range(steps)]
    return frames, jitters


def test_exercise_cadence_scalar_vs_avx2_equivalence():
    rng = np.random.default_rng(8)
    frames, jitters = _frames_and_jitter(rng, 4)
    pressures = [0.9, 1.0, 0.95, 1.05]
    decays = [0.0, 0.01, 0.02, 0.02]

    coefficients = build_canonical_coefficients()

    scalar_buffers = _buffers(seed=22)
    avx_buffers = _buffers(seed=22)

    scalar_focus = FocusTracker()
    avx_focus = FocusTracker()

    ingest_scalar = IngestController(scale=0.6)
    ingest_avx = IngestController(scale=0.6)

    exercise_cadence(
        scalar_buffers,
        coefficients,
        ingest_scalar,
        scalar_focus,
        frames,
        jitters,
        pressures=pressures,
        decays=decays,
        engine=scalar_step,
        boundary_phase=0.1,
    )

    exercise_cadence(
        avx_buffers,
        coefficients,
        ingest_avx,
        avx_focus,
        frames,
        jitters,
        pressures=pressures,
        decays=decays,
        engine=avx2_step,
        boundary_phase=0.1,
    )

    np.testing.assert_allclose(
        scalar_buffers.future.data, avx_buffers.future.data, rtol=1e-5, atol=1e-5
    )


def test_exercise_cadence_produces_finite_state():
    rng = np.random.default_rng(13)
    frames, jitters = _frames_and_jitter(rng, 3)

    buffers = _buffers(seed=5)
    coefficients = build_canonical_coefficients()

    exercise_cadence(
        buffers,
        coefficients,
        IngestController(scale=0.4),
        FocusTracker(),
        frames,
        jitters,
        pressures=1.1,
        decays=0.05,
    )

    assert np.isfinite(buffers.future.data).all()
