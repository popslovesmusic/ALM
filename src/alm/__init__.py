"""ALM foundational scaffolding.

This package sets up deterministic state buffers and rotation mechanics for the
four-slice stencil described in the ALM blueprint. Phase 1 focuses on
structure; later phases fill in coefficients, topology, and kernel laws.
"""

from .config import DeterministicConfig
from .constants import (
    GRID_COLS,
    GRID_ROWS,
    LANE_BLOCKS,
    LANES_PER_BLOCK,
    NUM_REGISTERS,
    REGISTER_NAMES,
    STENCIL_ORDER,
)
<<<<<<< ours
from .state import StateSlice, StencilBuffers

__all__ = [
=======
from .coefficients import (
    CoefficientTables,
    build_canonical_coefficients,
    lane_pair_index,
)
from .state import StateSlice, StencilBuffers

__all__ = [
    "CoefficientTables",
>>>>>>> theirs
    "DeterministicConfig",
    "GRID_COLS",
    "GRID_ROWS",
    "LANE_BLOCKS",
    "LANES_PER_BLOCK",
    "NUM_REGISTERS",
    "REGISTER_NAMES",
    "STENCIL_ORDER",
<<<<<<< ours
=======
    "build_canonical_coefficients",
    "lane_pair_index",
>>>>>>> theirs
    "StateSlice",
    "StencilBuffers",
]
