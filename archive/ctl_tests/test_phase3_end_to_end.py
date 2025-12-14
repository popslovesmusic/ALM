from ctl.attractors import build_attractors, summarize_attractors
from ctl.clusters import cluster_symbols, summarize_clusters
from ctl.phrase import build_phrases, summarize_phrases
from ctl.self_consistency import evaluate_consistency
from ctl.symbols import form_symbols, summarize_symbols


CHROMATIC_SEQUENCE = [
    {"tone": 0, "hue": (5, 5, 5), "polarity": 1, "intensity": 0.9, "timestamp": 0},
    {"tone": 2, "hue": (10, 12, 14), "polarity": 1, "intensity": 1.2, "timestamp": 1},
    {"tone": 4, "hue": (20, 24, 28), "polarity": -1, "intensity": 1.4, "timestamp": 2},
    {"tone": 5, "hue": (22, 26, 30), "polarity": 1, "intensity": 1.3, "timestamp": 3},
    {"tone": 7, "hue": (26, 30, 34), "polarity": 1, "intensity": 1.5, "timestamp": 4},
]


def test_end_to_end_pipeline_produces_metrics(tmp_path):
    symbols = form_symbols(CHROMATIC_SEQUENCE)
    clusters = cluster_symbols(symbols)
    attractors = build_attractors(clusters)
    phrases = build_phrases(symbols, clusters)

    symbol_summary = summarize_symbols(symbols)
    cluster_summary = summarize_clusters(clusters)
    attractor_summary = summarize_attractors(attractors)
    phrase_summary = summarize_phrases(phrases)
    metrics = evaluate_consistency(symbols, clusters, attractors, phrases)

    assert symbol_summary["count"] == len(symbols)
    assert cluster_summary["count"] == len(clusters)
    assert attractor_summary["count"] == len(attractors)
    assert phrase_summary["count"] == len(phrases)
    assert metrics["final_score"] >= 0

    # Ensure logs can be written to provided directory
    from ctl.symbols import write_symbol_metrics
    from ctl.clusters import write_cluster_metrics
    from ctl.attractors import write_attractor_metrics
    from ctl.phrase import write_phrase_metrics
    from ctl.self_consistency import write_consistency_metrics

    write_symbol_metrics(symbols, log_dir=tmp_path)
    write_cluster_metrics(clusters, log_dir=tmp_path)
    write_attractor_metrics(attractors, log_dir=tmp_path)
    write_phrase_metrics(phrases, log_dir=tmp_path)
    write_consistency_metrics(metrics, log_dir=tmp_path)

    assert (tmp_path / "symbol_metrics.csv").exists()
    assert (tmp_path / "self_consistency_metrics.csv").exists()
