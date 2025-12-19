"""Ingest lane handling synchronized with stencil advancement."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

<<<<<<< ours
<<<<<<< ours
from .constants import GRID_COLS, GRID_ROWS, REGISTER_NAMES
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, REGISTER_NAMES
>>>>>>> theirs
=======
from .constants import GRID_COLS, GRID_ROWS, LANES, REGISTER_NAMES
>>>>>>> theirs
from .state import StencilBuffers

INGEST_REGISTER_INDEX = REGISTER_NAMES.index("I")


@dataclass
class IngestController:
    """Coordinate ingest frames so they remain orthogonal to pressure channels."""

    scale: float = 1.0
    _applied_this_step: bool = field(default=False, init=False, repr=False)

    @property
    def register_index(self) -> int:
        return INGEST_REGISTER_INDEX

    def ingest(self, buffers: StencilBuffers, frame: np.ndarray) -> None:
        """Inject an external frame into the FUTURE slice once per step."""

        if self._applied_this_step:
            raise RuntimeError("ingest already applied for this step; advance first")

        frame_arr = np.asarray(frame)
<<<<<<< ours
<<<<<<< ours
        if frame_arr.shape != (GRID_ROWS, GRID_COLS):
            raise ValueError("ingest frame must have shape (GRID_ROWS, GRID_COLS)")

        target = buffers.future.data[..., self.register_index]
        buffers.future.data[..., self.register_index] = target + frame_arr.astype(target.dtype) * self.scale
=======
=======
>>>>>>> theirs
        if frame_arr.shape == (GRID_ROWS, GRID_COLS):
            frame_arr = np.broadcast_to(frame_arr[..., None], (GRID_ROWS, GRID_COLS, LANES))
        if frame_arr.shape != (GRID_ROWS, GRID_COLS, LANES):
            raise ValueError(
                "ingest frame must have shape (GRID_ROWS, GRID_COLS) or (GRID_ROWS, GRID_COLS, LANES)"
            )

        target = buffers.future.data[..., self.register_index, :]
        buffers.future.data[..., self.register_index, :] = target + frame_arr.astype(target.dtype) * self.scale
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
        self._applied_this_step = True

    def advance(self, buffers: StencilBuffers) -> None:
        """Rotate the stencil and clear the ingest guard for the next step."""

        buffers.advance()
        self._applied_this_step = False


__all__ = ["INGEST_REGISTER_INDEX", "IngestController"]
