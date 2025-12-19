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
<<<<<<< ours
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
=======
    LANES,
>>>>>>> theirs
=======
    LANES,
>>>>>>> theirs
    LANES_PER_BLOCK,
=======
    LANES,
    LANES_PER_BLOCK,
    L2_CACHE_BUDGET_BYTES,
>>>>>>> theirs
=======
    LANES,
    LANES_PER_BLOCK,
    L2_CACHE_BUDGET_BYTES,
>>>>>>> theirs
    NUM_REGISTERS,
    REGISTER_NAMES,
    STENCIL_ORDER,
)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
=======
from .boundary import apply_resonant_boundary, boundary_envelope
>>>>>>> theirs
=======
from .boundary import apply_resonant_boundary, boundary_envelope
>>>>>>> theirs
=======
from .boundary import apply_resonant_boundary, boundary_envelope
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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
from .focus import FocusTracker
from .ingest import INGEST_REGISTER_INDEX, IngestController
from .kernel import scalar_step
from .avx2 import avx2_step, avx2_equivalent_step
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
from .observability import (
    observable_snapshot,
    spiral_components,
    spiral_observation,
)
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
from .state import StateSlice, StencilBuffers
=======
=======
>>>>>>> theirs
from .state import (
    StateSlice,
    StencilBuffers,
    assert_cache_residency,
    slice_payload_bytes,
    stencil_payload_bytes,
)
<<<<<<< ours
>>>>>>> theirs
=======
from .performance import (
    ALLOWED_AVX2_INTRINSICS,
    residency_report,
    validate_intrinsics_used,
)
>>>>>>> theirs
from .topology import (
    DEFAULT_NEIGHBOR_OFFSETS,
    DEFAULT_TOPOLOGY,
    NeighborTopology,
    aggregate_neighbors,
)

__all__ = [
    "DEFAULT_NEIGHBOR_OFFSETS",
    "DEFAULT_TOPOLOGY",
<<<<<<< ours
    "CoefficientTables",
    "DeterministicConfig",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
    "FocusTracker",
>>>>>>> theirs
=======
    "FocusTracker",
>>>>>>> theirs
=======
    "FocusTracker",
>>>>>>> theirs
=======
    "FocusTracker",
>>>>>>> theirs
=======
    "ALLOWED_AVX2_INTRINSICS",
    "CoefficientTables",
    "DeterministicConfig",
    "FocusTracker",
>>>>>>> theirs
    "GRID_COLS",
    "GRID_ROWS",
    "INGEST_REGISTER_INDEX",
    "IngestController",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
    "L2_CACHE_BUDGET_BYTES",
>>>>>>> theirs
=======
    "L2_CACHE_BUDGET_BYTES",
>>>>>>> theirs
    "apply_resonant_boundary",
    "avx2_equivalent_step",
    "avx2_step",
    "boundary_envelope",
    "LANE_BLOCKS",
    "LANES",
<<<<<<< ours
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
    "LANES_PER_BLOCK",
    "NUM_REGISTERS",
    "NeighborTopology",
    "REGISTER_NAMES",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
    "LANES_PER_BLOCK",
    "NUM_REGISTERS",
    "NeighborTopology",
    "residency_report",
    "REGISTER_NAMES",
>>>>>>> theirs
    "scalar_step",
    "spiral_components",
    "spiral_observation",
    "observable_snapshot",
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
    "STENCIL_ORDER",
    "aggregate_neighbors",
    "build_canonical_coefficients",
    "lane_pair_index",
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
    "assert_cache_residency",
    "slice_payload_bytes",
    "stencil_payload_bytes",
>>>>>>> theirs
=======
    "assert_cache_residency",
    "validate_intrinsics_used",
    "slice_payload_bytes",
    "stencil_payload_bytes",
>>>>>>> theirs
    "StateSlice",
    "StencilBuffers",
]
