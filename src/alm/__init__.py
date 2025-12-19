"""Reference Python scaffolding for the ALM blueprint."""

from .config import DeterministicConfig
from .constants import GRID_COLS, GRID_ROWS, LANES, NUM_REGISTERS, STENCIL_ORDER
from .kernel import scalar_step
from .state import (
    StateSlice,
    StencilBuffers,
    assert_cache_residency,
    slice_payload_bytes,
    stencil_payload_bytes,
)

__all__ = [
    "DeterministicConfig",
    "GRID_COLS",
    "GRID_ROWS",
    "LANES",
    "NUM_REGISTERS",
    "STENCIL_ORDER",
    "StateSlice",
    "StencilBuffers",
    "assert_cache_residency",
    "slice_payload_bytes",
    "stencil_payload_bytes",
    "scalar_step",
]
