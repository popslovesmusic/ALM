import numpy as np

from alm import (
    DeterministicConfig,
    GRID_COLS,
    GRID_ROWS,
    NUM_REGISTERS,
    StencilBuffers,
    build_canonical_coefficients,
    scalar_step,
)


def test_scalar_step_respects_coefficients_and_neighbors():
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())
    buffers.now.data.fill(1.0)

    coeffs = build_canonical_coefficients()
    scalar_step(buffers, coeffs)

    neighbor_sum = np.ones((GRID_ROWS, GRID_COLS, NUM_REGISTERS, 32), dtype=np.float32)
    expected = np.empty_like(buffers.future.data)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    for target in range(NUM_REGISTERS):
        coupling = sum(neighbor_sum[..., source, :] * coeffs.gamma[target, source] for source in range(NUM_REGISTERS))
        update = coeffs.alpha[target] + coeffs.beta[target] + coupling
        expected[..., target, :] = 1.0 + update
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    bias = (buffers.now.data + buffers.recent.data + buffers.stable.data) / 3.0 - buffers.now.data
    for target in range(NUM_REGISTERS):
        coupling = sum(neighbor_sum[..., source, :] * coeffs.gamma[target, source] for source in range(NUM_REGISTERS))
        update = coeffs.alpha[target] + coeffs.beta[target] + coupling
        expected[..., target, :] = 1.0 + update + bias[..., target, :]
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

    np.testing.assert_allclose(buffers.future.data, expected)


def test_scalar_step_supports_pressure_and_decay_scalars():
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())
    buffers.now.data.fill(2.0)
    buffers.stable.data.fill(1.0)

    coeffs = build_canonical_coefficients()
    scalar_step(buffers, coeffs, pressure=0.5, decay=0.25)

    fast = 2.0 - 0.0
    slow = 2.0 - 1.0
    neighbor = np.ones((GRID_ROWS, GRID_COLS, NUM_REGISTERS, 32), dtype=np.float32) * 2.0
    expected = np.empty_like(buffers.future.data)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    for target in range(NUM_REGISTERS):
        coupling = sum(neighbor[..., source, :] * coeffs.gamma[target, source] for source in range(NUM_REGISTERS))
        update = coeffs.alpha[target] * fast + coeffs.beta[target] * slow + coupling
        expected[..., target, :] = 2.0 + 0.5 * update - 0.25 * slow
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    bias = (buffers.now.data + buffers.recent.data + buffers.stable.data) / 3.0 - buffers.now.data
    for target in range(NUM_REGISTERS):
        coupling = sum(neighbor[..., source, :] * coeffs.gamma[target, source] for source in range(NUM_REGISTERS))
        update = coeffs.alpha[target] * fast + coeffs.beta[target] * slow + coupling
        expected[..., target, :] = 2.0 + 0.5 * (update + bias[..., target, :]) - 0.25 * slow
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

    np.testing.assert_allclose(buffers.future.data, expected)
