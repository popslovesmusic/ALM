"""Sequence-level behavior tests for Tensor R."""
from ctl_tests.ctl_mock_data import generate_contrasting_l_sequence, generate_l_sequence
from ctl_tests.ctl_testing_utils import build_r_sequence, load_tensor_r_config


def test_sequence_stability_bounds():
    config = load_tensor_r_config()
    l_seq = generate_contrasting_l_sequence(length=5)
    r_seq = build_r_sequence(l_seq, config)

    assert len(r_seq) == len(l_seq)

    # Tone jumps should be limited by max_jump constraint
    for prev, curr in zip(r_seq, r_seq[1:]):
        assert abs(curr["tone"] - prev["tone"]) <= config["behaviors"]["tone_constraints"]["max_jump"]

    # Intensities should remain within configured ceiling
    intens_constraint = config["behaviors"]["intensity_constraints"]["saturation_factor"]
    assert all(cell["intensity"] <= 3.0 * intens_constraint for cell in r_seq)


def test_polarity_tracks_input_changes():
    config = load_tensor_r_config()
    l_seq = generate_l_sequence(length=6, start_tone=3, tone_step=1)
    r_seq = build_r_sequence(l_seq, config)

    # Count polarity flips in L vs R
    l_flips = sum(1 for a, b in zip(l_seq, l_seq[1:]) if a["polarity"] != b["polarity"])
    r_flips = sum(1 for a, b in zip(r_seq, r_seq[1:]) if a["polarity"] != b["polarity"])

    assert r_flips <= l_flips + 1  # R is allowed to smooth rapid oscillations
    assert r_seq[-1]["polarity"] in {1, -1}
