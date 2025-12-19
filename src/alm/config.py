"""Deterministic configuration helpers for stencil initialization."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER

ArrayInitializer = Callable[[str], np.ndarray]


@dataclass(frozen=True)
class DeterministicConfig:
    """Static configuration for building stencil buffers."""

    seed: int = 0
    dtype: np.dtype = np.float32

    def initializer(self) -> ArrayInitializer:
        """Return a deterministic initializer for each stencil slice."""

        rng = np.random.default_rng(self.seed)

        def _init(_: str) -> np.ndarray:
            return rng.standard_normal(
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )

        return _init

    def zeros(self) -> ArrayInitializer:
        """Return a zeroed initializer for stencil slices."""

        def _init(_: str) -> np.ndarray:
            return np.zeros(
                (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )

        return _init

    def validate_stencil_names(self) -> None:
        """Validate that the stencil order aligns with the blueprint contract."""

        if STENCIL_ORDER != ("FUTURE", "NOW", "RECENT", "STABLE"):
            raise ValueError("Stencil ordering deviates from the blueprint contract")
