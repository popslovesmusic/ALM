"""Topology definitions for the ALM 10×10 grid.

Phase 3 establishes the fixed 12-neighbor contract with uniform weights and
static closure. The topology is toroidal to maintain a constant neighbor count
for every cell and to preserve pair symmetry across the grid.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Tuple

import numpy as np

from .constants import GRID_COLS, GRID_ROWS

NeighborOffset = Tuple[int, int]

# Twelve symmetric offsets: first- and second-order axial plus diagonals.
DEFAULT_NEIGHBOR_OFFSETS: Tuple[NeighborOffset, ...] = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-2, 0),
    (2, 0),
    (0, -2),
    (0, 2),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
)


@dataclass(frozen=True)
class NeighborTopology:
    """Static neighbor layout with uniform weights and toroidal closure."""

    offsets: Tuple[NeighborOffset, ...] = DEFAULT_NEIGHBOR_OFFSETS
    weight: float = field(default_factory=lambda: 1.0 / len(DEFAULT_NEIGHBOR_OFFSETS))
    neighbor_index: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        if not self.offsets:
            raise ValueError("NeighborTopology requires at least one offset")

        object.__setattr__(self, "offsets", tuple(self.offsets))

        index = np.empty((GRID_ROWS, GRID_COLS, len(self.offsets), 2), dtype=np.int64)
        for row in range(GRID_ROWS):
            for col in range(GRID_COLS):
                for idx, (dr, dc) in enumerate(self.offsets):
                    index[row, col, idx] = ((row + dr) % GRID_ROWS, (col + dc) % GRID_COLS)

        object.__setattr__(self, "neighbor_index", index)

    def neighbors_of(self, row: int, col: int) -> Iterable[Tuple[Tuple[int, int], float]]:
        """Yield neighbor coordinates and uniform weight for a cell."""

        for idx in range(len(self.offsets)):
            nrow, ncol = self.neighbor_index[row, col, idx]
            yield (int(nrow), int(ncol)), self.weight


DEFAULT_TOPOLOGY = NeighborTopology()


def aggregate_neighbors(field: np.ndarray, topology: NeighborTopology = DEFAULT_TOPOLOGY) -> np.ndarray:
    """Aggregate neighbor contributions with uniform weights.

    Args:
        field: Array with leading dimensions ``(GRID_ROWS, GRID_COLS, …)``.
        topology: Neighbor topology defining neighbor indices and weights.

    Returns:
        Array matching the input ``field`` shape where each cell contains the
        weighted sum of its neighbors across all remaining dimensions.
    """

    if field.shape[0] != GRID_ROWS or field.shape[1] != GRID_COLS:
        raise ValueError("field must have shape (GRID_ROWS, GRID_COLS, …)")

    neighbor_rows = topology.neighbor_index[..., 0]
    neighbor_cols = topology.neighbor_index[..., 1]
    neighbors = field[neighbor_rows, neighbor_cols]

    return neighbors.sum(axis=2) * topology.weight


__all__ = [
    "DEFAULT_NEIGHBOR_OFFSETS",
    "DEFAULT_TOPOLOGY",
    "NeighborTopology",
    "aggregate_neighbors",
]
