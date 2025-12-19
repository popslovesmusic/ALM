import numpy as np

from alm.coefficients import CoefficientTables
from alm.kernel import scalar_step
from alm.state import StateSlice, StencilBuffers


def build_unit_coefficients() -> CoefficientTables:
    alpha = np.zeros((4, 32), dtype=np.float32)
    beta = np.zeros((4, 32), dtype=np.float32)
    gamma = np.zeros((4, 4, 32), dtype=np.float32)
    return CoefficientTables(alpha=alpha, beta=beta, gamma=gamma)


def test_scalar_step_updates_future_with_bias_and_pressure():
    coeffs = build_unit_coefficients()

    base = np.zeros((10, 10, 4, 32), dtype=np.float32)
    future = StateSlice(base.copy())
    now = StateSlice(base.copy())
    recent = StateSlice(base.copy())
    stable = StateSlice(base.copy())

    now.data[..., 0, :] = 1.0
    recent.data[..., 0, :] = 0.5
    stable.data[..., 0, :] = 0.0

    buffers = StencilBuffers([future, now, recent, stable])
    scalar_step(buffers, coeffs, pressure=1.0, decay=0.0)

    expected_bias = (now.data + recent.data + stable.data) / 3.0 - now.data
    expected_update = now.data + expected_bias
    assert np.allclose(buffers.future.data, expected_update)
