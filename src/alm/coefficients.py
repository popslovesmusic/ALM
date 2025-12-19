"""Canonical coefficient generation for the ALM stencil.

Phase 2 locks down the α, β, and Γ coefficient families using the
constitutional base sequence and lane pairing rules described in the ALM
blueprint. Tables are regenerated deterministically to avoid hidden tuning
and are validated for pair symmetry, normalization, and aux-lane isolation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np

from .constants import NUM_REGISTERS

# Canonical constants derived from the blueprint.
PAIR_SYMMETRIC_SEED: np.ndarray = np.array(
    [0.5, -0.5, -0.5, 0.5, 0.5, -0.5], dtype=np.float32
)

NORMALIZATION_CONSTANT: float = 1.0 / np.sqrt(6.0)
LANE_AMPLITUDE: float = 0.5 * NORMALIZATION_CONSTANT
OFF_DIAGONAL_SCALE: float = 0.5

ALPHA_PAIR_SIGNS: np.ndarray = np.array([1, -1, -1, 1, 1, -1], dtype=np.float32)
BETA_PAIR_SIGNS: np.ndarray = np.array([-1, -1, 1, 1, -1, 1], dtype=np.float32)
GAMMA_DIAGONAL_SIGNS: np.ndarray = np.array(
    [-1, -1, 1, -1, 1, 1], dtype=np.float32
)


def lane_pair_index(lane: int) -> int:
    """Return the paired lane index according to the canonical map.

    Lane groupings:
    - Hue lanes: 0–11 pair as (0,11), (1,10), …, (5,6)
    - Tone lanes: 12–23 pair as (12,23), …, (17,18)
    - Aux lanes: 24–31 pair as (24,31), …, (27,28)
    """

    if not 0 <= lane < 32:
        raise ValueError("lane index must be in [0, 31]")

    if lane < 12:
        return 11 - lane
    if lane < 24:
        return 35 - lane
    return 55 - lane


def _pair_expand(pair_signs: Iterable[float], amplitude: float) -> np.ndarray:
    """Expand a 6-entry pair-sign vector into a 12-lane symmetric array."""

    pair_array = np.asarray(pair_signs, dtype=np.float32)
    if pair_array.shape != (6,):
        raise ValueError("pair_signs must have length 6")

    front = pair_array * amplitude
    return np.concatenate([front, front[::-1]])


def _expand_to_full_width(base12: np.ndarray) -> np.ndarray:
    """Repeat hue/tone coefficients and append zeroed aux lanes."""

    if base12.shape != (12,):
        raise ValueError("base12 must have length 12")

    aux = np.zeros(8, dtype=np.float32)
    return np.concatenate([base12, base12, aux])


def _validate_pair_symmetry(vector: np.ndarray) -> None:
    for lane in range(vector.shape[-1]):
        pair_lane = lane_pair_index(lane)
        if not np.isclose(vector[lane], vector[pair_lane]):
            raise ValueError(f"lane {lane} violates pair symmetry")


def _validate_norms(arr: np.ndarray) -> None:
    norms = np.linalg.norm(arr, axis=-1)
    if np.any(norms > 1.0 + 1e-6):
        raise ValueError("coefficient vector exceeds normalization bound")


def _validate_aux_zero(arr: np.ndarray) -> None:
    if np.any(arr[..., 24:]):
        raise ValueError("aux lanes must remain zero for canonical coefficients")


@dataclass(frozen=True)
class CoefficientTables:
    """Canonical coefficient tables for α, β, and Γ."""

    alpha: np.ndarray
    beta: np.ndarray
    gamma: np.ndarray

    def __post_init__(self) -> None:
        if self.alpha.shape != (NUM_REGISTERS, 32):
            raise ValueError("alpha must have shape (4, 32)")
        if self.beta.shape != (NUM_REGISTERS, 32):
            raise ValueError("beta must have shape (4, 32)")
        if self.gamma.shape != (NUM_REGISTERS, NUM_REGISTERS, 32):
            raise ValueError("gamma must have shape (4, 4, 32)")

        for arr in (self.alpha, self.beta, self.gamma):
            if not np.issubdtype(arr.dtype, np.floating):
                raise TypeError("coefficient arrays must be floating point")

        self._run_validations()
        self._freeze_arrays()

    def _run_validations(self) -> None:
        for register in range(NUM_REGISTERS):
            _validate_pair_symmetry(self.alpha[register])
            _validate_pair_symmetry(self.beta[register])
            _validate_aux_zero(self.alpha[register])
            _validate_aux_zero(self.beta[register])

            for source in range(NUM_REGISTERS):
                gamma_vec = self.gamma[register, source]
                _validate_pair_symmetry(gamma_vec)
                _validate_aux_zero(gamma_vec)

        _validate_norms(self.alpha)
        _validate_norms(self.beta)
        _validate_norms(self.gamma)

    def _freeze_arrays(self) -> None:
        for name in ("alpha", "beta", "gamma"):
            arr = getattr(self, name)
            arr.setflags(write=False)
            object.__setattr__(self, name, arr)


def build_canonical_coefficients(dtype: np.dtype = np.float32) -> CoefficientTables:
    """Construct canonical coefficient tables with validation."""

    alpha_base = _pair_expand(ALPHA_PAIR_SIGNS, LANE_AMPLITUDE)
    beta_base = _pair_expand(BETA_PAIR_SIGNS, LANE_AMPLITUDE)
    gamma_diag_base = _pair_expand(GAMMA_DIAGONAL_SIGNS, LANE_AMPLITUDE)
    gamma_off_base = _pair_expand(GAMMA_DIAGONAL_SIGNS, LANE_AMPLITUDE * OFF_DIAGONAL_SCALE)

    alpha_full = _expand_to_full_width(alpha_base).astype(dtype)
    beta_full = _expand_to_full_width(beta_base).astype(dtype)
    gamma_diag_full = _expand_to_full_width(gamma_diag_base).astype(dtype)
    gamma_off_full = _expand_to_full_width(gamma_off_base).astype(dtype)

    alpha = np.stack([alpha_full] * NUM_REGISTERS, axis=0)
    beta = np.stack([beta_full] * NUM_REGISTERS, axis=0)

    gamma = np.empty((NUM_REGISTERS, NUM_REGISTERS, 32), dtype=dtype)
    for target in range(NUM_REGISTERS):
        for source in range(NUM_REGISTERS):
            gamma[target, source] = gamma_diag_full if target == source else gamma_off_full

    return CoefficientTables(alpha=alpha, beta=beta, gamma=gamma)


__all__ = [
    "ALPHA_PAIR_SIGNS",
    "BETA_PAIR_SIGNS",
    "CoefficientTables",
    "GAMMA_DIAGONAL_SIGNS",
    "LANE_AMPLITUDE",
    "NORMALIZATION_CONSTANT",
    "OFF_DIAGONAL_SCALE",
    "PAIR_SYMMETRIC_SEED",
    "build_canonical_coefficients",
    "lane_pair_index",
]
