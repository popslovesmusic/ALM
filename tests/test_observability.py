import numpy as np

from alm import DeterministicConfig, StencilBuffers, observable_snapshot, spiral_components, spiral_observation


def test_observable_snapshot_returns_detached_copies():
    config = DeterministicConfig(seed=7)
    buffers = StencilBuffers.build(config.initializer())

    snapshot = observable_snapshot(buffers, slices=["NOW", "RECENT"])

    snapshot["NOW"][0, 0, 0, 0] = 999.0
    assert buffers.now.data[0, 0, 0, 0] != 999.0

    buffers.recent.data[0, 1, 0, 0] = -123.0
    assert snapshot["RECENT"][0, 1, 0, 0] != -123.0


def test_spiral_components_shape_and_values():
    data = np.zeros((10, 10, 4, 32), dtype=np.float32)
    data[..., 0, :] = 1.0
    data[..., 1, :] = 1.0
    data[..., 2, :] = 2.0
    data[..., 3, :] = 0.5

    radial, angular = spiral_components(data)

    expected_radial = np.sqrt(1.0 + 1.0 + 4.0 + 0.25)
    assert radial.shape == (10, 10, 32)
    assert np.allclose(radial, expected_radial)

    expected_angle = np.arctan2(1.0, 1.0)
    assert angular.shape == (10, 10, 32)
    assert np.allclose(angular, expected_angle)


def test_spiral_observation_is_passive():
    config = DeterministicConfig(seed=11)
    buffers = StencilBuffers.build(config.initializer())

    observation = spiral_observation(buffers, slice_name="FUTURE")

    observation["radial"][0, 0, 0] = 0.0
    observation["angular"][0, 0, 0] = 0.0

    future_radial, future_angle = spiral_components(buffers.future.data)
    assert future_radial[0, 0, 0] != 0.0
    assert future_angle[0, 0, 0] != 0.0


def test_resolves_unknown_slice_name():
    config = DeterministicConfig(seed=5)
    buffers = StencilBuffers.build(config.initializer())

    try:
        observable_snapshot(buffers, slices=["INVALID"])
    except KeyError:
        pass
    else:
        raise AssertionError("Expected KeyError for unknown slice name")
