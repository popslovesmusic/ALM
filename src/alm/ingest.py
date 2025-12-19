"""Reference-only ingest helpers for future phases.

The ingest contract will bind external signals to lane-safe entry points. This
placeholder preserves module structure while Phase 1 scaffolding is validated.
"""

from __future__ import annotations

import numpy as np

from .constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS, STENCIL_ORDER


def validate_frame_shape(frame: np.ndarray) -> None:
    """Ensure a candidate ingest frame matches the grid/register layout."""

    expected = (GRID_ROWS, GRID_COLS, NUM_REGISTERS)
    if frame.shape[:3] != expected:
        raise ValueError(f"ingest frame must start with shape {expected}, got {frame.shape}")


def is_step_aligned(step_name: str) -> bool:
    """Check that ingest is only scheduled on FUTURE steps."""

    return step_name == STENCIL_ORDER[0]


__all__ = ["validate_frame_shape", "is_step_aligned"]
