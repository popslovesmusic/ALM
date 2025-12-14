"""Phase 4 meta-cognition pipeline tests."""

import os

from ctl.meta_symbols import derive_meta_symbols, summarize_meta_symbols, write_meta_symbol_metrics
from ctl.narrative import build_narrative, summarize_episodes, write_narrative_metrics
from ctl.feedback import compute_feedback, write_feedback_signal
from ctl.self_model import initialize_self_model, update_self_model, write_self_model_snapshot
from ctl.meta_consistency import evaluate_meta_consistency, write_meta_consistency_metrics
from ctl.symbols import form_symbols
from ctl.clusters import cluster_symbols
from ctl.phrase import build_phrases
from ctl_tests.ctl_mock_data import generate_l_sequence


def test_meta_pipeline_end_to_end(tmp_path) -> None:
    l_seq = generate_l_sequence(length=8, start_tone=2, tone_step=1)
    symbols = form_symbols(l_seq)
    clusters = cluster_symbols(symbols)
    phrases = build_phrases(symbols, clusters)

    meta_symbols = derive_meta_symbols(symbols, clusters, phrases)
    assert meta_symbols, "Meta-symbols should be produced from phrases"

    episodes = build_narrative(meta_symbols, phrases)
    assert episodes, "Narrative episodes should be created"

    self_model = initialize_self_model()
    feedback = compute_feedback(meta_symbols, episodes, stability=self_model.stability)
    updated_model = update_self_model(self_model, feedback, meta_consistency=0.8)

    metrics = evaluate_meta_consistency(meta_symbols, episodes, updated_model)
    assert 0.0 <= metrics["reflection_stability"] <= 1.0
    assert updated_model.posture in {"predictive", "reactive", "stable"}

    # Confirm summaries remain bounded
    meta_summary = summarize_meta_symbols(meta_symbols)
    episode_summary = summarize_episodes(episodes)
    assert meta_summary["count"] == len(meta_symbols)
    assert episode_summary["count"] == len(episodes)

    # Confirm logging writes within temporary directory
    meta_path = write_meta_symbol_metrics(meta_symbols, log_dir=str(tmp_path))
    narrative_path = write_narrative_metrics(episodes, log_dir=str(tmp_path))
    feedback_path = write_feedback_signal(feedback, log_dir=str(tmp_path))
    self_model_path = write_self_model_snapshot(updated_model, log_dir=str(tmp_path))
    meta_consistency_path = write_meta_consistency_metrics(metrics, log_dir=str(tmp_path))

    for path in [meta_path, narrative_path, feedback_path, self_model_path, meta_consistency_path]:
        assert os.path.exists(path)
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read().strip()
            assert content, f"Expected log content for {path}"
