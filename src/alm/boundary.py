"""Resonant boundary conditioning without gates or clamps.

Phase 6 introduces a deterministic boundary envelope that modulates the
FUTURE slice using smooth trigonometric responses. The envelope is derived
from proximity to the physical grid edges and applies uniformly across all
registers and lanes to preserve symmetry while avoiding branch-based
thresholding.
"""

from __future__ import annotations

import numpy as np

from .constants import GRID_COLS, GRID_ROWS


def boundary_envelope(
    resonance: float = 0.15, phase: float = 0.0, rows: int = GRID_ROWS, cols: int = GRID_COLS
) -> np.ndarray:
    """Compute a smooth boundary weighting field.

    The envelope is constructed from the minimum distance to any boundary and
    translated through a sinusoid to keep the response resonant rather than
    clipped. The resulting mask is positive and broadcastable over registers
    and lanes.
    """

    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be positive")

    row_grid, col_grid = np.meshgrid(np.arange(rows), np.arange(cols), indexing="ij")

    edge_distance = np.minimum.reduce(
        [row_grid, col_grid, rows - 1 - row_grid, cols - 1 - col_grid]
    ).astype(np.float32)

    max_distance = edge_distance.max()
    if max_distance == 0:
        raise ValueError("boundary envelope requires a non-degenerate grid")

    proximity = 1.0 - edge_distance / max_distance
    harmonic_phase = np.pi * proximity + phase
    harmonic = np.sin(harmonic_phase)

    envelope = 1.0 + resonance * harmonic
    return envelope[..., None, None]


def apply_resonant_boundary(target_slice: np.ndarray, resonance: float = 0.15, phase: float = 0.0) -> np.ndarray:
    """Apply the resonant boundary envelope in-place and return the slice."""

    if target_slice.shape[:2] != (GRID_ROWS, GRID_COLS):
        raise ValueError("target_slice must start with (GRID_ROWS, GRID_COLS) dimensions")

    mask = boundary_envelope(resonance=resonance, phase=phase)
    target_slice *= mask.astype(target_slice.dtype)
    return target_slice


__all__ = ["apply_resonant_boundary", "boundary_envelope"]
