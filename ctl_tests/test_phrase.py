from ctl.clusters import cluster_symbols
from ctl.phrase import build_phrases, summarize_phrases
from ctl.symbols import form_symbols


def _symbols():
    cells = [
        {"tone": 2, "hue": (10, 15, 20), "polarity": 1, "intensity": 1.2, "timestamp": 0},
        {"tone": 3, "hue": (12, 18, 22), "polarity": 1, "intensity": 1.3, "timestamp": 1},
        {"tone": 5, "hue": (15, 20, 25), "polarity": -1, "intensity": 1.1, "timestamp": 2},
        {"tone": 6, "hue": (16, 24, 28), "polarity": 1, "intensity": 1.4, "timestamp": 3},
        {"tone": 7, "hue": (18, 26, 30), "polarity": 1, "intensity": 1.5, "timestamp": 4},
    ]
    return form_symbols(cells)


def test_phrase_building_detects_motifs():
    symbols = _symbols()
    clusters = cluster_symbols(symbols)
    phrases = build_phrases(symbols, clusters)
    assert len(phrases) >= 1
    assert phrases[0].motif.startswith("ascending") or phrases[0].motif.endswith("soft")


def test_phrase_summary_reports_cadence():
    symbols = _symbols()
    phrases = build_phrases(symbols, cluster_symbols(symbols))
    summary = summarize_phrases(phrases)
    assert summary["count"] >= 1
    assert summary["mean_cadence"] >= 0
