"""State containers and stencil rotation mechanics for the ALM runtime."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, List, MutableSequence

import numpy as np

from .config import ArrayInitializer
from .constants import (
    GRID_COLS,
    GRID_ROWS,
    LANES,
    L2_CACHE_BUDGET_BYTES,
    NUM_REGISTERS,
    STENCIL_ORDER,
)


@dataclass
class StateSlice:
    """One stencil slice covering the full 10×10 grid and four registers."""

    data: np.ndarray

    def __post_init__(self) -> None:
        expected_shape = (GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES)
        if self.data.shape != expected_shape:
            raise ValueError(
                f"StateSlice requires shape {expected_shape}, got {self.data.shape}"
            )

        if not np.issubdtype(self.data.dtype, np.floating):
            raise TypeError("StateSlice data must be a floating point array")

        if not self.data.flags["C_CONTIGUOUS"]:
            raise ValueError("StateSlice data must be C-contiguous for cache residency")

    @classmethod
    def from_initializer(cls, init: ArrayInitializer, name: str) -> "StateSlice":
        return cls(init(name))

    @classmethod
    def zeros(cls, dtype: np.dtype = np.float32) -> "StateSlice":
        return cls(np.zeros((GRID_ROWS, GRID_COLS, NUM_REGISTERS, LANES), dtype=dtype))


class StencilBuffers:
    """Holds the four rotating stencil slices with pointer-based swapping."""

    def __init__(self, slices: Iterable[StateSlice]):
        slice_list: List[StateSlice] = list(slices)
        if len(slice_list) != len(STENCIL_ORDER):
            raise ValueError(
                f"StencilBuffers requires {len(STENCIL_ORDER)} slices,"
                f" received {len(slice_list)}"
            )

        self._slices: MutableSequence[StateSlice] = deque(slice_list, maxlen=4)

    @classmethod
    def build(cls, initializer: ArrayInitializer) -> "StencilBuffers":
        """Construct buffers using a deterministic initializer per slice."""

        slices = [StateSlice.from_initializer(initializer, name) for name in STENCIL_ORDER]
        return cls(slices)

    @property
    def future(self) -> StateSlice:
        return self._slices[0]

    @property
    def now(self) -> StateSlice:
        return self._slices[1]

    @property
    def recent(self) -> StateSlice:
        return self._slices[2]

    @property
    def stable(self) -> StateSlice:
        return self._slices[3]

    def advance(self) -> None:
        """Rotate stencil pointers: FUTURE→NOW→RECENT→STABLE→FUTURE."""

        self._slices.rotate(-1)

    def snapshot(self) -> dict:
        """Return a copy of the stencil ordering for observability/testing."""

        return {
            "FUTURE": self.future.data.copy(),
            "NOW": self.now.data.copy(),
            "RECENT": self.recent.data.copy(),
            "STABLE": self.stable.data.copy(),
        }


def slice_payload_bytes(dtype: np.dtype = np.float32) -> int:
    """Return payload size in bytes for one state slice with the given dtype."""

    return GRID_ROWS * GRID_COLS * NUM_REGISTERS * LANES * np.dtype(dtype).itemsize


def stencil_payload_bytes(dtype: np.dtype = np.float32) -> int:
    """Return payload size in bytes for the full four-slice stencil."""

    return slice_payload_bytes(dtype) * len(STENCIL_ORDER)


def assert_cache_residency(
    dtype: np.dtype = np.float32, budget_bytes: int = L2_CACHE_BUDGET_BYTES
) -> int:
    """Validate the stencil payload fits within the L2 cache budget."""

    payload = stencil_payload_bytes(dtype)
    if payload > budget_bytes:
        raise ValueError(
            f"Stencil payload of {payload} bytes exceeds budget of {budget_bytes} bytes"
        )

    return payload
