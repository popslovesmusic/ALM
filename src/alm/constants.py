"""Physical envelope constants for the ALM stencil runtime.

These values mirror the blueprint constraints for Phase 1 scaffolding.
"""

from __future__ import annotations

from typing import Tuple

GRID_ROWS: int = 10
GRID_COLS: int = 10
REGISTER_NAMES: Tuple[str, str, str, str] = ("R", "G", "B", "I")
NUM_REGISTERS: int = len(REGISTER_NAMES)

LANE_BLOCKS: int = 4
LANES_PER_BLOCK: int = 8  # 4 blocks × 8 lanes == 32 lanes total
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
LANES: int = LANE_BLOCKS * LANES_PER_BLOCK
>>>>>>> theirs
=======
LANES: int = LANE_BLOCKS * LANES_PER_BLOCK
>>>>>>> theirs
=======
LANES: int = LANE_BLOCKS * LANES_PER_BLOCK
>>>>>>> theirs
=======
LANES: int = LANE_BLOCKS * LANES_PER_BLOCK
>>>>>>> theirs

STENCIL_ORDER: Tuple[str, str, str, str] = ("FUTURE", "NOW", "RECENT", "STABLE")
