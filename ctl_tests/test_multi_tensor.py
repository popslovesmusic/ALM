"""Multi-tensor assembly tests."""
from ctl.multi_tensor import MultiTensorAssembly, couple_fiber_snapshots, run_multi_tensor
from ctl_tests.ctl_mock_data import generate_l_sequence
from ctl_tests.ctl_testing_utils import load_coupling_config, load_tensor_r_config


def test_multi_tensor_runs_and_aggregates():
    l_seq = generate_l_sequence(length=5, start_tone=2, tone_step=1)
    r_cfg = load_tensor_r_config()
    coupling_cfg = load_coupling_config()

    assembly = MultiTensorAssembly([r_cfg, r_cfg], coupling_config=coupling_cfg)
    r_sequences = assembly.run_r_fibers(l_seq)
    aggregated = assembly.aggregate_states(r_sequences)
    summaries = assembly.summarize_fibers(l_seq, r_sequences)

    assert len(r_sequences) == 2
    assert all(len(r) == len(l_seq) for r in r_sequences)
    assert len(aggregated) == len(l_seq)
    assert summaries and all("agreement" in s for s in summaries)

    back_compare = assembly.compare_aggregated_to_l(l_seq, aggregated)
    assert back_compare["agreement"] > 0.4


def test_multi_tensor_snapshots_and_wrapper():
    l_seq = generate_l_sequence(length=4)
    r_cfg = load_tensor_r_config()
    coupling_cfg = load_coupling_config()

    result = run_multi_tensor(l_seq, [r_cfg, r_cfg], coupling_config=coupling_cfg)
    snapshots = couple_fiber_snapshots(l_seq, result["r_sequences"], coupling_cfg)

    assert "aggregated" in result and result["aggregated"]
    assert len(snapshots) == 2
    for snap in snapshots:
        assert "per_step" in snap and "summary" in snap
        assert snap["summary"]["agreement"] >= 0.0
