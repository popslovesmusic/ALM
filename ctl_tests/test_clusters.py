from ctl.clusters import cluster_symbols, summarize_clusters
from ctl.symbols import form_symbols


def _sample_symbols():
    cells = [
        {"tone": 1, "hue": (10, 20, 30), "polarity": 1, "intensity": 1.0, "timestamp": 0},
        {"tone": 2, "hue": (11, 21, 31), "polarity": 1, "intensity": 1.1, "timestamp": 1},
        {"tone": 6, "hue": (60, 50, 40), "polarity": -1, "intensity": 1.2, "timestamp": 2},
        {"tone": 7, "hue": (62, 52, 42), "polarity": -1, "intensity": 1.3, "timestamp": 3},
    ]
    return form_symbols(cells)


def test_clusters_respect_similarity_thresholds():
    clusters = cluster_symbols(_sample_symbols())
    assert len(clusters) == 2
    assert clusters[0].polarity == 1
    assert clusters[1].polarity == -1


def test_cluster_summary_tracks_coherence():
    clusters = cluster_symbols(_sample_symbols())
    summary = summarize_clusters(clusters)
    assert summary["count"] == 2
    assert summary["mean_coherence"] > 0
