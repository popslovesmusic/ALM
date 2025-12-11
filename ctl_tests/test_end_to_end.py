"""End-to-end CTL pipeline tests with logging."""
import os

from ctl.coupling import (
    apply_coupling,
    compute_coupling_metrics,
    load_coupling_config,
    log_coupling_metrics,
    log_end_to_end_summary,
    log_tensor_r_behavior,
    summarize_coupled_sequence,
)
from ctl_tests.ctl_mock_data import generate_l_sequence
from ctl_tests.ctl_testing_utils import build_r_sequence, load_tensor_r_config


LOG_DIR = "logs"


def test_pipeline_and_logs(tmp_path=None):
    coupling_cfg = load_coupling_config()
    tensor_r_cfg = load_tensor_r_config()

    l_seq = generate_l_sequence(length=6, start_tone=0, tone_step=2)
    r_seq = build_r_sequence(l_seq, tensor_r_cfg)

    metrics = compute_coupling_metrics(l_seq, r_seq, coupling_cfg)
    coupled = apply_coupling(l_seq, r_seq, coupling_cfg)

    summary = summarize_coupled_sequence(coupled)

    log_coupling_metrics(metrics, LOG_DIR)
    log_tensor_r_behavior(r_seq, LOG_DIR)
    log_end_to_end_summary(summary, LOG_DIR)

    assert metrics["agreement"] > 0.4
    assert summary["input_length"] == len(coupled)

    # Ensure logs were created and appended
    for filename in ["coupling_metrics.csv", "tensor_r_behavior.csv", "end_to_end_summary.csv"]:
        path = os.path.join(LOG_DIR, filename)
        assert os.path.exists(path)
        with open(path, "r") as f:
            lines = [line for line in f.readlines() if line.strip()]
            assert len(lines) >= 1
