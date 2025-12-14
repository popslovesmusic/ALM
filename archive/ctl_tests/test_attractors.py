from ctl.attractors import build_attractors, summarize_attractors, update_attractors
from ctl.clusters import cluster_symbols
from ctl.symbols import form_symbols


def _clusters():
    cells = [
        {"tone": 0, "hue": (5, 5, 5), "polarity": 1, "intensity": 1.0, "timestamp": 0},
        {"tone": 1, "hue": (8, 8, 8), "polarity": 1, "intensity": 1.1, "timestamp": 1},
        {"tone": 3, "hue": (20, 25, 30), "polarity": -1, "intensity": 1.2, "timestamp": 2},
        {"tone": 4, "hue": (22, 27, 32), "polarity": -1, "intensity": 1.3, "timestamp": 3},
    ]
    return cluster_symbols(form_symbols(cells))


def test_attractor_build_and_update():
    clusters = _clusters()
    attractors = build_attractors(clusters)
    assert len(attractors) == len(clusters)
    summary = summarize_attractors(attractors)
    assert summary["mean_activation"] >= 0

    updated = update_attractors(attractors, clusters)
    assert updated[0].energy != attractors[0].energy or updated[0].activation == attractors[0].activation
