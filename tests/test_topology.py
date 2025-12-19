import numpy as np

from alm import (
    DEFAULT_NEIGHBOR_OFFSETS,
    DEFAULT_TOPOLOGY,
    GRID_COLS,
    GRID_ROWS,
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
    aggregate_neighbors,
)


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


def test_topology_is_symmetric():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            for (nrow, ncol), _ in DEFAULT_TOPOLOGY.neighbors_of(row, col):
                reverse_neighbors = {coord for coord, _ in DEFAULT_TOPOLOGY.neighbors_of(nrow, ncol)}
                assert (row, col) in reverse_neighbors


def test_aggregate_neighbors_matches_manual_average():
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    field = np.arange(GRID_ROWS * GRID_COLS, dtype=np.float32).reshape(GRID_ROWS, GRID_COLS, 1)
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    field = (
        np.arange(GRID_ROWS * GRID_COLS, dtype=np.float32)
        .reshape(GRID_ROWS, GRID_COLS, 1, 1)
        .repeat(LANES, axis=-1)
    )
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
    aggregated = aggregate_neighbors(field)

    def manual_average(r, c):
        values = []
        for (nrow, ncol), _ in DEFAULT_TOPOLOGY.neighbors_of(r, c):
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
            values.append(field[nrow, ncol, 0])
=======
            values.append(field[nrow, ncol, 0, 0])
>>>>>>> theirs
=======
            values.append(field[nrow, ncol, 0, 0])
>>>>>>> theirs
=======
            values.append(field[nrow, ncol, 0, 0])
>>>>>>> theirs
=======
            values.append(field[nrow, ncol, 0, 0])
>>>>>>> theirs
        return sum(values) / len(values)

    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
            assert np.isclose(aggregated[r, c, 0], manual_average(r, c))
=======
            assert np.isclose(aggregated[r, c, 0, 0], manual_average(r, c))
>>>>>>> theirs
=======
            assert np.isclose(aggregated[r, c, 0, 0], manual_average(r, c))
>>>>>>> theirs
=======
            assert np.isclose(aggregated[r, c, 0, 0], manual_average(r, c))
>>>>>>> theirs
=======
            assert np.isclose(aggregated[r, c, 0, 0], manual_average(r, c))
>>>>>>> theirs
