"""Coupling-specific tests."""
from ctl.coupling import apply_coupling, compute_coupling_metrics, load_coupling_config
from ctl_tests.ctl_mock_data import generate_contrasting_l_sequence, generate_l_sequence
from ctl_tests.ctl_testing_utils import build_r_sequence, load_tensor_r_config


def test_coupling_alignment_and_agreement_score():
    coupling_cfg = load_coupling_config()
    tensor_r_cfg = load_tensor_r_config()

    l_seq = generate_l_sequence(length=5, start_tone=1, tone_step=2)
    r_seq = build_r_sequence(l_seq, tensor_r_cfg)

    metrics = compute_coupling_metrics(l_seq, r_seq, coupling_cfg)
    coupled = apply_coupling(l_seq, r_seq, coupling_cfg)

    assert len(coupled) == len(l_seq)
    assert metrics["agreement"] > 0.5
    assert all(cell["coherence"] >= coupling_cfg["coherence"]["min_coherence"] for cell in coupled)
    assert all(cell["constraint_flag"] in {"OK", "WARN", "VIOLATION"} for cell in coupled)


def test_coupling_detects_disparity():
    coupling_cfg = load_coupling_config()

    l_seq = generate_contrasting_l_sequence(length=4)
    r_seq = [
        {"tone": 11, "hue": [20, 20, 20], "intensity": 0.5, "polarity": 1, "timestamp": i, "coherence": 1.0}
        for i in range(len(l_seq))
    ]

    coupled = apply_coupling(l_seq, r_seq, coupling_cfg)
    violations = [c for c in coupled if c["constraint_flag"] != "OK"]

    assert violations, "Expected coupling to flag disparities"
    assert any(cell["constraint_flag"] == "VIOLATION" for cell in violations)
