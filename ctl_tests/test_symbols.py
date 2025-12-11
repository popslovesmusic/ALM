from ctl.symbols import form_symbols, summarize_symbols


def _sample_cells():
    return [
        {"tone": 2, "hue": (10, 20, 30), "polarity": 1, "intensity": 0.9, "timestamp": 0},
        {"tone": 3, "hue": (12, 22, 32), "polarity": 1, "intensity": 1.2, "timestamp": 1},
        {"tone": 5, "hue": (14, 24, 36), "polarity": -1, "intensity": 1.5, "timestamp": 2},
        {"tone": 6, "hue": (16, 26, 38), "polarity": 1, "intensity": 1.1, "timestamp": 3},
    ]


def test_symbol_roles_and_labels():
    symbols = form_symbols(_sample_cells())
    assert len(symbols) == 4
    roles = [s.role for s in symbols]
    assert "peak" in roles
    # Labels encode tone and hue bands
    assert symbols[0].label.startswith("T")
    assert symbols[2].polarity == -1


def test_symbol_summary_balances_intensity_and_polarity():
    symbols = form_symbols(_sample_cells())
    summary = summarize_symbols(symbols)
    assert summary["count"] == 4
    assert summary["mean_tone"] > 3
    assert summary["peak_ratio"] > 0
