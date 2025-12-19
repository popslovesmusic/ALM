import numpy as np
import pytest

from alm import avx2_step, build_canonical_coefficients, scalar_step
from alm.coefficients import lane_pair_index
from alm.config import DeterministicConfig
from alm.constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS, STENCIL_ORDER
<<<<<<< ours
=======
from alm.observability import observable_snapshot
>>>>>>> theirs
from alm.state import StencilBuffers


ENGINES = {
    "scalar": scalar_step,
    "avx2": avx2_step,
}


@pytest.fixture(name="coefficients")
def coefficients_fixture():
    return build_canonical_coefficients()


def _swap_lane_pairs(array: np.ndarray) -> None:
    for lane in range(array.shape[-1]):
        pair = lane_pair_index(lane)
        if lane < pair:
            left = array[..., lane].copy()
            array[..., lane] = array[..., pair]
            array[..., pair] = left


def _build_buffers(initializer) -> StencilBuffers:
    return StencilBuffers.build(initializer)


<<<<<<< ours
=======
def _copy_buffers(buffers: StencilBuffers) -> StencilBuffers:
    clone = DeterministicConfig().zeros()
    dup = StencilBuffers.build(clone)
    for slice_name in STENCIL_ORDER:
        getattr(dup, slice_name.lower()).data[:] = getattr(
            buffers, slice_name.lower()
        ).data
    return dup


>>>>>>> theirs
@pytest.mark.parametrize("engine_name", ENGINES.keys())
@pytest.mark.parametrize("pressure", [0.0, 0.9])
def test_lane_permutation_invariance(engine_name, pressure, coefficients):
    config = DeterministicConfig(seed=42)
    baseline = _build_buffers(config.initializer())
    permuted = _build_buffers(config.initializer())

    for slice_name in STENCIL_ORDER:
        _swap_lane_pairs(getattr(permuted, slice_name.lower()).data)

    engine = ENGINES[engine_name]
    engine(baseline, coefficients, pressure=pressure)
    engine(permuted, coefficients, pressure=pressure)

    _swap_lane_pairs(permuted.future.data)
    np.testing.assert_allclose(baseline.future.data, permuted.future.data, rtol=1e-6, atol=1e-6)


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_antisymmetry_preserved(engine_name, coefficients):
    rng = np.random.default_rng(7)
    config = DeterministicConfig(seed=11)
    buffers = _build_buffers(config.zeros())

    for slice_name in STENCIL_ORDER:
        data = getattr(buffers, slice_name.lower()).data
        for lane in range(data.shape[-1]):
            if lane <= lane_pair_index(lane):
                sample = rng.standard_normal((GRID_ROWS, GRID_COLS, NUM_REGISTERS))
                data[..., lane] = sample
                data[..., lane_pair_index(lane)] = -sample

    engine = ENGINES[engine_name]
    engine(buffers, coefficients, pressure=1.1)

    for lane in range(buffers.future.data.shape[-1]):
        pair = lane_pair_index(lane)
        np.testing.assert_allclose(
            buffers.future.data[..., lane],
            -buffers.future.data[..., pair],
            rtol=1e-6,
            atol=1e-6,
        )


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_neutral_input_neutrality(engine_name, coefficients):
    def uniform(_: str) -> np.ndarray:
        return np.ones((GRID_ROWS, GRID_COLS, NUM_REGISTERS, 32), dtype=np.float32)

    buffers = _build_buffers(uniform)
    engine = ENGINES[engine_name]
    engine(buffers, coefficients, pressure=0.0)

    np.testing.assert_allclose(buffers.future.data, buffers.now.data, rtol=1e-6, atol=1e-6)


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_small_perturbation_continuity(engine_name, coefficients):
    config = DeterministicConfig(seed=99)
    baseline = _build_buffers(config.initializer())
    perturbed = _build_buffers(config.initializer())

    epsilon = 1e-4
    perturbation = np.full_like(perturbed.now.data, epsilon)
    perturbed.now.data += perturbation

    engine = ENGINES[engine_name]
    engine(baseline, coefficients, pressure=0.75)
    engine(perturbed, coefficients, pressure=0.75)

    diff = np.abs(perturbed.future.data - baseline.future.data)
    assert np.max(diff) <= 1e-2


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_pressure_injection_rejected(engine_name, coefficients):
    config = DeterministicConfig(seed=5)
    buffers = _build_buffers(config.initializer())
    engine = ENGINES[engine_name]

    with pytest.raises(ValueError):
        engine(buffers, coefficients, pressure=np.ones((GRID_ROWS, GRID_COLS)))
<<<<<<< ours
=======


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_aux_lane_isolation(engine_name, coefficients):
    rng = np.random.default_rng(22)
    config = DeterministicConfig(seed=101)
    with_aux = _build_buffers(config.zeros())
    without_aux = _build_buffers(config.zeros())

    aux_start = coefficients.alpha.shape[1] - 8
    aux_slice = slice(aux_start, coefficients.alpha.shape[1])

    for slice_name in STENCIL_ORDER:
        with_data = getattr(with_aux, slice_name.lower()).data
        without_data = getattr(without_aux, slice_name.lower()).data
        with_data[..., :aux_start] = 1.0
        without_data[..., :aux_start] = 1.0
        with_data[..., aux_slice] = rng.standard_normal(with_data[..., aux_slice].shape)
        without_data[..., aux_slice] = 0.0

    engine = ENGINES[engine_name]
    engine(with_aux, coefficients, pressure=0.5)
    engine(without_aux, coefficients, pressure=0.5)

    np.testing.assert_allclose(
        with_aux.future.data[..., :aux_start],
        without_aux.future.data[..., :aux_start],
        rtol=1e-6,
        atol=1e-6,
    )


@pytest.mark.parametrize("engine_name", ENGINES.keys())
def test_observability_feedback_prohibited(engine_name, coefficients):
    config = DeterministicConfig(seed=1337)
    baseline = _build_buffers(config.initializer())
    control = _copy_buffers(baseline)

    snapshot = observable_snapshot(baseline, slices=("NOW", "RECENT"))
    for value in snapshot.values():
        value.fill(0.0)

    engine = ENGINES[engine_name]
    engine(baseline, coefficients, pressure=0.2)
    engine(control, coefficients, pressure=0.2)

    np.testing.assert_allclose(
        baseline.future.data,
        control.future.data,
        rtol=1e-6,
        atol=1e-6,
    )


@pytest.mark.parametrize("pressure", [0.0, 0.8])
@pytest.mark.parametrize("jitter", [0.0, 0.25])
def test_equivalence_under_pressure_and_jitter(coefficients, pressure, jitter):
    config = DeterministicConfig(seed=404)
    scalar_buffers = _build_buffers(config.initializer())
    avx2_buffers = _build_buffers(config.initializer())

    if jitter != 0.0:
        scalar_buffers.now.data += jitter
        avx2_buffers.now.data += jitter

    scalar_step(scalar_buffers, coefficients, pressure=pressure)
    avx2_step(avx2_buffers, coefficients, pressure=pressure)

    np.testing.assert_allclose(
        scalar_buffers.future.data,
        avx2_buffers.future.data,
        rtol=1e-6,
        atol=1e-6,
    )
>>>>>>> theirs
