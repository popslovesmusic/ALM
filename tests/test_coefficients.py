import numpy as np

from alm import (
    CoefficientTables,
    NUM_REGISTERS,
    build_canonical_coefficients,
    lane_pair_index,
)
from alm.coefficients import (
    ALPHA_PAIR_SIGNS,
    BETA_PAIR_SIGNS,
    GAMMA_DIAGONAL_SIGNS,
    LANE_AMPLITUDE,
    OFF_DIAGONAL_SCALE,
)


def _expected_pattern(pair_signs, amplitude):
    pair_signs = np.asarray(pair_signs, dtype=np.float32)
    front = pair_signs * amplitude
    base12 = np.concatenate([front, front[::-1]])
    return np.concatenate([base12, base12, np.zeros(8, dtype=np.float32)])


def test_coefficients_shapes_and_readonly():
    tables = build_canonical_coefficients()

    assert isinstance(tables, CoefficientTables)
    assert tables.alpha.shape == (NUM_REGISTERS, 32)
    assert tables.beta.shape == (NUM_REGISTERS, 32)
    assert tables.gamma.shape == (NUM_REGISTERS, NUM_REGISTERS, 32)

    assert not tables.alpha.flags.writeable
    assert not tables.beta.flags.writeable
    assert not tables.gamma.flags.writeable


def test_pair_symmetry_and_aux_isolation():
    tables = build_canonical_coefficients()

    for lane in range(32):
        pair_lane = lane_pair_index(lane)
        for register in range(NUM_REGISTERS):
            assert tables.alpha[register, lane] == tables.alpha[register, pair_lane]
            assert tables.beta[register, lane] == tables.beta[register, pair_lane]
            for source in range(NUM_REGISTERS):
                assert (
                    tables.gamma[register, source, lane]
                    == tables.gamma[register, source, pair_lane]
                )

    assert np.allclose(tables.alpha[..., 24:], 0.0)
    assert np.allclose(tables.beta[..., 24:], 0.0)
    assert np.allclose(tables.gamma[..., 24:], 0.0)


def test_canonical_lane_values_and_norms():
    tables = build_canonical_coefficients()

    expected_alpha = _expected_pattern(ALPHA_PAIR_SIGNS, LANE_AMPLITUDE)
    expected_beta = _expected_pattern(BETA_PAIR_SIGNS, LANE_AMPLITUDE)
    expected_gamma_diag = _expected_pattern(GAMMA_DIAGONAL_SIGNS, LANE_AMPLITUDE)
    expected_gamma_off = _expected_pattern(
        GAMMA_DIAGONAL_SIGNS, LANE_AMPLITUDE * OFF_DIAGONAL_SCALE
    )

    np.testing.assert_allclose(tables.alpha[0], expected_alpha)
    np.testing.assert_allclose(tables.beta[0], expected_beta)
    np.testing.assert_allclose(tables.gamma[0, 0], expected_gamma_diag)
    np.testing.assert_allclose(tables.gamma[0, 1], expected_gamma_off)

    assert np.isclose(np.linalg.norm(tables.alpha[0]), 1.0)
    assert np.isclose(np.linalg.norm(tables.beta[0]), 1.0)
    assert np.isclose(np.linalg.norm(tables.gamma[0, 0]), 1.0)
    assert np.isclose(np.linalg.norm(tables.gamma[0, 1]), 0.5)
