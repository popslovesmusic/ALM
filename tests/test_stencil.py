import numpy as np

from alm import DeterministicConfig, StencilBuffers, STENCIL_ORDER


def test_stencil_rotation_preserves_identity():
    config = DeterministicConfig(seed=123)
    buffers = StencilBuffers.build(config.zeros())

    initial_ids = [id(buffers.future), id(buffers.now), id(buffers.recent), id(buffers.stable)]

    buffers.advance()

    rotated_ids = [id(buffers.future), id(buffers.now), id(buffers.recent), id(buffers.stable)]

    assert rotated_ids == initial_ids[1:] + initial_ids[:1]


def test_deterministic_initializer_reproducible():
    config = DeterministicConfig(seed=42)

    buffers_a = StencilBuffers.build(config.initializer())
    buffers_b = StencilBuffers.build(config.initializer())

    for name in STENCIL_ORDER:
        np.testing.assert_allclose(
            getattr(buffers_a, name.lower()).data,
            getattr(buffers_b, name.lower()).data,
        )
