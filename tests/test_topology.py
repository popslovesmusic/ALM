import numpy as np

from alm.constants import GRID_COLS, GRID_ROWS, LANES
from alm.topology import DEFAULT_NEIGHBOR_OFFSETS, DEFAULT_TOPOLOGY, aggregate_neighbors


def test_topology_has_uniform_neighbors_and_wraps():
    assert len(DEFAULT_NEIGHBOR_OFFSETS) == 12
    assert np.isclose(DEFAULT_TOPOLOGY.weight * 12, 1.0)

    neighbors = list(DEFAULT_TOPOLOGY.neighbors_of(0, 0))
    coords = {coord for coord, _ in neighbors}
    expected = {
        ((-1 + GRID_ROWS) % GRID_ROWS, 0),
        (1 % GRID_ROWS, 0),
        (0, (-1 + GRID_COLS) % GRID_COLS),
        (0, 1 % GRID_COLS),
        ((-2 + GRID_ROWS) % GRID_ROWS, 0),
        (2 % GRID_ROWS, 0),
        (0, (-2 + GRID_COLS) % GRID_COLS),
        (0, 2 % GRID_COLS),
        ((-1 + GRID_ROWS) % GRID_ROWS, (-1 + GRID_COLS) % GRID_COLS),
        ((-1 + GRID_ROWS) % GRID_ROWS, 1 % GRID_COLS),
        (1 % GRID_ROWS, (-1 + GRID_COLS) % GRID_COLS),
        (1 % GRID_ROWS, 1 % GRID_COLS),
    }

    assert coords == expected
    assert all(np.isclose(weight, DEFAULT_TOPOLOGY.weight) for _, weight in neighbors)


def test_aggregate_neighbors_matches_manual_average():
    field = (
        np.arange(GRID_ROWS * GRID_COLS, dtype=np.float32)
        .reshape(GRID_ROWS, GRID_COLS, 1, 1)
        .repeat(LANES, axis=-1)
    )

    aggregated = aggregate_neighbors(field)

    def manual_average(r, c):
        values = []
        for (nrow, ncol), _ in DEFAULT_TOPOLOGY.neighbors_of(r, c):
            values.append(field[nrow, ncol])
        stacked = np.stack(values, axis=0)
        return stacked.mean(axis=0)

    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            assert np.allclose(aggregated[row, col], manual_average(row, col))
