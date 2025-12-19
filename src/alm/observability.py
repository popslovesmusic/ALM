"""Passive observability utilities (placeholder for later phases)."""

from __future__ import annotations

import numpy as np

from .constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS


def snapshot_scalar_field(state_slice: np.ndarray) -> np.ndarray:
    """Return a copy of a scalar field for offline analysis."""

    expected = (GRID_ROWS, GRID_COLS, NUM_REGISTERS, state_slice.shape[-1])
    if state_slice.shape[:3] != expected[:3]:
        raise ValueError("observability snapshot shape mismatch")

    return np.array(state_slice, copy=True)


__all__ = ["snapshot_scalar_field"]
