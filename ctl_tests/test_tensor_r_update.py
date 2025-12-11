"""Unit tests for Tensor R update behaviors."""
from ctl.tensor_r_update import update_tensor_r_cell
from ctl_tests.ctl_mock_data import generate_l_sequence
from ctl_tests.ctl_testing_utils import initialize_r_cell, load_tensor_r_config


def test_tone_smoothing_and_prediction():
    config = load_tensor_r_config()
    l_seq = generate_l_sequence(length=2, start_tone=2, tone_step=6)
    r_prev = initialize_r_cell(l_seq[0], config)

    r_next = update_tensor_r_cell(r_prev, l_seq[0], l_seq[1], config)

    # With lambda=0.65 and alpha=0.25, blended tone should be pulled toward 8 then nudged forward
    assert r_next["tone"] == 6
    assert r_next["constraint_flag"] == "OK"
    assert r_next["intensity"] > r_prev["intensity"]


def test_tone_constraint_and_reset():
    config = load_tensor_r_config()
    l_prev = generate_l_sequence(length=1, start_tone=0)[0]
    l_curr = generate_l_sequence(length=1, start_tone=11)[0]
    r_prev = initialize_r_cell(l_prev, config)

    r_next = update_tensor_r_cell(r_prev, l_prev, l_curr, config)

    # Jump from 0 to 11 exceeds max_jump=5 → tone should be preserved and warning raised
    assert r_next["tone"] == r_prev["tone"]
    assert r_next["constraint_flag"] == "WARN"


def test_polarity_over_oscillation_detection():
    config = load_tensor_r_config()
    l_prev, l_curr = generate_l_sequence(length=2, start_tone=4)
    r_prev = initialize_r_cell(l_prev, config)

    flip_history = [1, -1, 1, -1, 1, -1, 1, -1, 1]
    r_next = update_tensor_r_cell(r_prev, l_prev, l_curr, config, flip_history=flip_history)

    assert r_next["polarity"] == 1
    assert r_next["constraint_flag"] == "VIOLATION"
