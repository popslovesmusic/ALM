from ctl.attractors import build_attractors
from ctl.clusters import cluster_symbols
from ctl.phrase import build_phrases
from ctl.self_consistency import evaluate_consistency
from ctl.symbols import form_symbols


def _pipeline_objects():
    cells = [
        {"tone": 1, "hue": (10, 12, 14), "polarity": 1, "intensity": 1.0, "timestamp": 0},
        {"tone": 3, "hue": (12, 14, 16), "polarity": 1, "intensity": 1.2, "timestamp": 1},
        {"tone": 4, "hue": (14, 16, 18), "polarity": -1, "intensity": 1.3, "timestamp": 2},
        {"tone": 6, "hue": (16, 18, 20), "polarity": 1, "intensity": 1.4, "timestamp": 3},
    ]
    symbols = form_symbols(cells)
    clusters = cluster_symbols(symbols)
    attractors = build_attractors(clusters)
    phrases = build_phrases(symbols, clusters)
    return symbols, clusters, attractors, phrases


def test_consistency_scoring_balances_components():
    symbols, clusters, attractors, phrases = _pipeline_objects()
    metrics = evaluate_consistency(symbols, clusters, attractors, phrases)
    assert metrics["final_score"] >= 0
    assert metrics["symbol_score"] > 0
