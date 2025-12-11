"""Tests for Chromatic Memory System integration."""
from ctl import memory
from ctl.tensor_r_update import update_tensor_r_cell
from ctl_tests.ctl_mock_data import generate_l_sequence
from ctl_tests.ctl_testing_utils import initialize_r_cell, load_tensor_r_config


def test_memory_reinforces_and_snaps():
    mem_cfg = memory.load_memory_config()
    state = memory.init_memory_state()
    l_cells = generate_l_sequence(length=3, start_tone=3, tone_step=0)

    for cell in l_cells:
        state = memory.update_memory_state(state, cell, mem_cfg, coherence=0.9)

    snapped_tone = memory.snap_to_nearest_memory_tone(5, state, mem_cfg)
    snapped_hue = memory.snap_to_nearest_memory_hue([32, 62, 92], state, mem_cfg)

    assert snapped_tone == 3
    assert snapped_hue in [peak["hue"] for peak in state["hue_peaks"]]


def test_memory_match_boosts_tensor_r_intensity():
    config = load_tensor_r_config()
    mem_cfg = memory.load_memory_config()
    state = memory.init_memory_state()
    l_prev, l_curr = generate_l_sequence(length=2, start_tone=4, tone_step=0)

    r_prev = initialize_r_cell(l_prev, config)
    # Seed memory with the first observation
    state = memory.update_memory_state(state, l_prev, mem_cfg, coherence=r_prev.get("coherence", 1.0))

    r_next = update_tensor_r_cell(
        r_prev,
        l_prev,
        l_curr,
        config,
        flip_history=None,
        memory_state=state,
        memory_config=mem_cfg,
    )

    assert r_next["intensity"] > r_prev["intensity"]
    assert state["tone_peaks"] and state["hue_peaks"]
