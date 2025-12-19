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
<<<<<<< ours
<<<<<<< ours
=======
    LANES,
>>>>>>> theirs
=======
    LANES,
>>>>>>> theirs
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
<<<<<<< ours
<<<<<<< ours
from .state import StateSlice, StencilBuffers

__all__ = [
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
from .boundary import apply_resonant_boundary, boundary_envelope
>>>>>>> theirs
from .coefficients import (
    CoefficientTables,
    build_canonical_coefficients,
    lane_pair_index,
)
<<<<<<< ours
<<<<<<< ours
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
=======
from .ingest import INGEST_REGISTER_INDEX, IngestController
from .kernel import scalar_step
from .avx2 import avx2_step, avx2_equivalent_step
>>>>>>> theirs
=======
from .focus import FocusTracker
from .ingest import INGEST_REGISTER_INDEX, IngestController
from .kernel import scalar_step
from .avx2 import avx2_step, avx2_equivalent_step
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
<<<<<<< ours
=======
    "FocusTracker",
>>>>>>> theirs
    "GRID_COLS",
    "GRID_ROWS",
    "INGEST_REGISTER_INDEX",
    "IngestController",
<<<<<<< ours
<<<<<<< ours
    "LANE_BLOCKS",
<<<<<<< ours
=======
    "LANES",
>>>>>>> theirs
=======
    "avx2_equivalent_step",
    "avx2_step",
    "LANE_BLOCKS",
    "LANES",
>>>>>>> theirs
=======
    "apply_resonant_boundary",
    "avx2_equivalent_step",
    "avx2_step",
    "boundary_envelope",
    "LANE_BLOCKS",
    "LANES",
>>>>>>> theirs
    "LANES_PER_BLOCK",
    "NUM_REGISTERS",
    "NeighborTopology",
    "REGISTER_NAMES",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
    "scalar_step",
>>>>>>> theirs
=======
    "scalar_step",
>>>>>>> theirs
=======
    "scalar_step",
>>>>>>> theirs
    "STENCIL_ORDER",
    "aggregate_neighbors",
    "build_canonical_coefficients",
    "lane_pair_index",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    "StateSlice",
    "StencilBuffers",
]
