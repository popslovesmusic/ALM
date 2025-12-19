import numpy as np

from alm import (
    GRID_COLS,
    GRID_ROWS,
    DeterministicConfig,
    IngestController,
    StencilBuffers,
)


def test_ingest_writes_future_aux_lane_only_once():
    controller = IngestController(scale=0.5)
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())

    frame = np.ones((GRID_ROWS, GRID_COLS), dtype=np.float32)
    controller.ingest(buffers, frame)

    # Only the ingest register receives data; other registers remain zeroed.
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    for register in range(buffers.future.data.shape[-1]):
        if register == controller.register_index:
            np.testing.assert_allclose(buffers.future.data[..., register], 0.5)
        else:
            assert np.allclose(buffers.future.data[..., register], 0.0)
=======
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
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    for register in range(buffers.future.data.shape[-2]):
        if register == controller.register_index:
            np.testing.assert_allclose(buffers.future.data[..., register, :], 0.5)
        else:
            assert np.allclose(buffers.future.data[..., register, :], 0.0)
<<<<<<< ours
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
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

    # Second ingest without rotation is forbidden.
    try:
        controller.ingest(buffers, frame)
    except RuntimeError:
        pass
    else:
        raise AssertionError("second ingest should have been rejected")


def test_ingest_resets_after_advance_and_tracks_rotation():
    controller = IngestController()
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())

    first_frame = np.full((GRID_ROWS, GRID_COLS), 2.0, dtype=np.float32)
    controller.ingest(buffers, first_frame)

    controller.advance(buffers)

    # The ingested data rotates with the stencil ordering.
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    assert np.allclose(buffers.stable.data[..., controller.register_index], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index], 0.0)
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.stable.data[..., controller.register_index, :], 2.0)
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 0.0)
>>>>>>> theirs

    second_frame = np.full((GRID_ROWS, GRID_COLS), 3.0, dtype=np.float32)
    controller.ingest(buffers, second_frame)

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    assert np.allclose(buffers.future.data[..., controller.register_index], 3.0)
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs
=======
    assert np.allclose(buffers.future.data[..., controller.register_index, :], 3.0)
>>>>>>> theirs


def test_ingest_validates_frame_shape():
    controller = IngestController()
    buffers = StencilBuffers.build(DeterministicConfig(seed=0).zeros())

    bad_frame = np.ones((5, 5), dtype=np.float32)
    try:
        controller.ingest(buffers, bad_frame)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid frame shape should raise ValueError")
