"""Deterministic configuration helpers for the ALM stencil.

Phase 1 requires stable, non-adaptive initialization so subsequent phases can
layer coefficients and kernel laws without hidden tuning. This module centralizes
seed handling and array initialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
from .constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS, STENCIL_ORDER
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
>>>>>>> theirs
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
>>>>>>> theirs
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
>>>>>>> theirs
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
>>>>>>> theirs

ArrayInitializer = Callable[[str], np.ndarray]


@dataclass(frozen=True)
class DeterministicConfig:
    """Static configuration for building stencil buffers.

    Attributes:
        seed: Random seed used for deterministic initialization.
        dtype: Numeric dtype for the state buffers.
    """

    seed: int = 0
    dtype: np.dtype = np.float32

    def initializer(self) -> ArrayInitializer:
        """Return a deterministic initializer for each stencil slice.

        The initializer respects the stencil naming order so future phases can
        add slice-specific bias terms without altering rotation semantics.
        """

        rng = np.random.default_rng(self.seed)

        def _init(_: str) -> np.ndarray:
            return rng.standard_normal(
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS), dtype=self.dtype
=======
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
>>>>>>> theirs
=======
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
>>>>>>> theirs
=======
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
>>>>>>> theirs
=======
                size=(GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
>>>>>>> theirs
            )

        return _init

    def zeros(self) -> ArrayInitializer:
        """Return a zeroed initializer for stencil slices."""

        def _init(_: str) -> np.ndarray:
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
            return np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS), dtype=self.dtype)
=======
            return np.zeros(
                (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )
>>>>>>> theirs
=======
            return np.zeros(
                (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )
>>>>>>> theirs
=======
            return np.zeros(
                (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )
>>>>>>> theirs
=======
            return np.zeros(
                (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=self.dtype
            )
>>>>>>> theirs

        return _init

    def validate_stencil_names(self) -> None:
        """Validate that the stencil order aligns with the blueprint contract."""

        if STENCIL_ORDER != ("FUTURE", "NOW", "RECENT", "STABLE"):
            raise ValueError("Stencil ordering deviates from the blueprint contract")
