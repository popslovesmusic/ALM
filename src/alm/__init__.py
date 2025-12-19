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
<<<<<<< ours
=======
    LANES,
>>>>>>> theirs
    LANES_PER_BLOCK,
    NUM_REGISTERS,
    REGISTER_NAMES,
    STENCIL_ORDER,
)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
from .state import StateSlice, StencilBuffers

__all__ = [
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
from .coefficients import (
    CoefficientTables,
    build_canonical_coefficients,
    lane_pair_index,
)
<<<<<<< ours
<<<<<<< ours
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
=======
from .ingest import INGEST_REGISTER_INDEX, IngestController
=======
from .ingest import INGEST_REGISTER_INDEX, IngestController
from .kernel import scalar_step
>>>>>>> theirs
from .state import StateSlice, StencilBuffers
from .topology import (
    DEFAULT_NEIGHBOR_OFFSETS,
    DEFAULT_TOPOLOGY,
    NeighborTopology,
    aggregate_neighbors,
)

__all__ = [
    "DEFAULT_NEIGHBOR_OFFSETS",
    "DEFAULT_TOPOLOGY",
    "CoefficientTables",
    "DeterministicConfig",
    "GRID_COLS",
    "GRID_ROWS",
    "INGEST_REGISTER_INDEX",
    "IngestController",
    "LANE_BLOCKS",
<<<<<<< ours
=======
    "LANES",
>>>>>>> theirs
    "LANES_PER_BLOCK",
    "NUM_REGISTERS",
    "NeighborTopology",
    "REGISTER_NAMES",
<<<<<<< ours
=======
    "scalar_step",
>>>>>>> theirs
    "STENCIL_ORDER",
    "aggregate_neighbors",
    "build_canonical_coefficients",
    "lane_pair_index",
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
    "StateSlice",
    "StencilBuffers",
]
