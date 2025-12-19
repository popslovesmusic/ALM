import numpy as np

from alm import (
    DEFAULT_TOPOLOGY,
    DeterministicConfig,
    StencilBuffers,
    avx2_equivalent_step,
    avx2_step,
    build_canonical_coefficients,
    scalar_step,
)


def _build_buffers(seed: int = 0):
    cfg = DeterministicConfig(seed=seed)
    initializer = cfg.initializer()
    return StencilBuffers.build(initializer)


def test_avx2_matches_scalar_update():
    coefficients = build_canonical_coefficients()

    scalar_buffers = _build_buffers(seed=7)
    avx2_buffers = _build_buffers(seed=7)

    scalar_step(
        scalar_buffers,
        coefficients,
        topology=DEFAULT_TOPOLOGY,
        pressure=0.75,
        decay=0.1,
    )
    avx2_step(
        avx2_buffers,
        coefficients,
        topology=DEFAULT_TOPOLOGY,
        pressure=0.75,
        decay=0.1,
    )

    np.testing.assert_allclose(scalar_buffers.future.data, avx2_buffers.future.data)


def test_avx2_alias_matches_primary():
    coefficients = build_canonical_coefficients()
    buffers = _build_buffers(seed=11)
    baseline = buffers.snapshot()

    avx2_step(buffers, coefficients, topology=DEFAULT_TOPOLOGY)
    direct = buffers.future.data.copy()

    buffers._slices[0].data[:] = baseline["FUTURE"]
    buffers._slices[1].data[:] = baseline["NOW"]
    buffers._slices[2].data[:] = baseline["RECENT"]
    buffers._slices[3].data[:] = baseline["STABLE"]

    avx2_equivalent_step(buffers, coefficients, topology=DEFAULT_TOPOLOGY)

    np.testing.assert_allclose(direct, buffers.future.data)
