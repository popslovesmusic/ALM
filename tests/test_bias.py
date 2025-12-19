import numpy as np

from alm import DeterministicConfig, StencilBuffers, future_bias


def test_future_bias_zero_when_slices_match():
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())
    phi = future_bias(buffers.now.data, buffers.recent.data, buffers.stable.data)

    assert np.all(phi == 0)


def test_future_bias_blends_history_deterministically():
    cfg = DeterministicConfig(seed=4)
    buffers = StencilBuffers.build(cfg.initializer())
    phi_first = future_bias(buffers.now.data, buffers.recent.data, buffers.stable.data)
    phi_second = future_bias(buffers.now.data, buffers.recent.data, buffers.stable.data)

    np.testing.assert_allclose(phi_first, phi_second)

    blended = (buffers.now.data + buffers.recent.data + buffers.stable.data) / 3.0
    np.testing.assert_allclose(phi_first, blended - buffers.now.data)
