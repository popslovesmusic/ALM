"""Focus handoff logic under jitter while preserving orthogonality."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .constants import GRID_COLS, GRID_ROWS


def _normalize_focus(focus: np.ndarray) -> np.ndarray:
    total = float(focus.sum())
    if total == 0.0:
        raise ValueError("focus map cannot sum to zero")
    return focus / total


@dataclass
class FocusTracker:
    """Maintains a smooth focus field that transfers under jitter."""

    inertia: float = 0.85
    slip: float = 0.15
    focus_map: np.ndarray = field(
        default_factory=lambda: _normalize_focus(
            np.ones((GRID_ROWS, GRID_COLS), dtype=np.float32)
        )
    )

    def __post_init__(self) -> None:
        focus_arr = np.asarray(self.focus_map, dtype=np.float32)
        if focus_arr.shape != (GRID_ROWS, GRID_COLS):
            raise ValueError(
                f"focus_map must have shape {(GRID_ROWS, GRID_COLS)}, got {focus_arr.shape}"
            )

        object.__setattr__(self, "focus_map", _normalize_focus(focus_arr))

    def handoff(self, jitter: np.ndarray, pressure: float = 1.0) -> np.ndarray:
        """Transfer focus using resonant blending independent of pressure."""

        jitter_arr = np.asarray(jitter, dtype=np.float32)
        if jitter_arr.shape != (GRID_ROWS, GRID_COLS):
            raise ValueError(
                f"jitter must have shape {(GRID_ROWS, GRID_COLS)}, got {jitter_arr.shape}"
            )

        harmonic = np.sin(jitter_arr) + np.cos(jitter_arr * 0.5 + np.pi / 4.0)
        harmonic = harmonic - harmonic.mean()

        blended = self.inertia * self.focus_map + self.slip * (harmonic + 1.0)
        updated = _normalize_focus(blended)

        object.__setattr__(self, "focus_map", updated)
        return self.focus_map


__all__ = ["FocusTracker"]
