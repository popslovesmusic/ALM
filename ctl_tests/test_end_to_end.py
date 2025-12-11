"""End-to-end CTL pipeline tests with logging."""
import os

from ctl.coupling import (
    compute_coupling_metrics,
    load_coupling_config,
    log_coupling_metrics,
    log_end_to_end_summary,
    log_tensor_r_behavior,
    process_coupling_sequence,
    summarize_coupled_sequence,
)
from ctl.multi_tensor import MultiTensorAssembly
from ctl_tests.ctl_mock_data import generate_l_sequence
from ctl_tests.ctl_testing_utils import build_r_sequence, load_tensor_r_config


LOG_DIR = "logs"


def test_pipeline_and_logs(tmp_path=None):
    coupling_cfg = load_coupling_config()
    tensor_r_cfg = load_tensor_r_config()

    l_seq = generate_l_sequence(length=6, start_tone=0, tone_step=2)
    r_seq = build_r_sequence(l_seq, tensor_r_cfg)

    metrics = compute_coupling_metrics(l_seq, r_seq, coupling_cfg)
    bundle = process_coupling_sequence(l_seq, r_seq, coupling_cfg)
    coupled = bundle["coupled"]

    summary = summarize_coupled_sequence(coupled)

    log_coupling_metrics(metrics, LOG_DIR)
    log_tensor_r_behavior(r_seq, LOG_DIR)
    log_end_to_end_summary(summary, LOG_DIR)

    assert metrics["agreement"] > 0.4
    assert metrics["coherence_score"] > 0.2
    assert summary["input_length"] == len(coupled)

    # Ensure logs were created and appended
    for filename in ["coupling_metrics.csv", "tensor_r_behavior.csv", "end_to_end_summary.csv"]:
        path = os.path.join(LOG_DIR, filename)
        assert os.path.exists(path)
        with open(path, "r") as f:
            lines = [line for line in f.readlines() if line.strip()]
            assert len(lines) >= 1
            if filename == "end_to_end_summary.csv":
                assert "coherence_mean" in lines[0]

    # Multi-tensor check: second fiber should align with L similarly
    assembly = MultiTensorAssembly([tensor_r_cfg, tensor_r_cfg], coupling_config=coupling_cfg)
    multi_output = assembly.run_full(l_seq)
    assert len(multi_output["r_sequences"]) == 2
    assert multi_output["coupling_metrics"]
