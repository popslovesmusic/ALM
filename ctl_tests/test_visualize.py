"""Visualization helper tests."""
import os

from ctl.visualization import (
    bundle_visualizations,
    export_csv_snapshot,
    export_json_snapshot,
    hue_map,
    intensity_envelope,
    tone_trajectory,
)
from ctl_tests.ctl_mock_data import generate_l_sequence


def test_visualization_structures_and_exports(tmp_path=None):
    l_seq = generate_l_sequence(length=4, start_tone=1)

    tone = tone_trajectory(l_seq)
    hue = hue_map(l_seq)
    intensity = intensity_envelope(l_seq)
    bundle = bundle_visualizations(l_seq)

    assert len(tone) == len(l_seq)
    assert len(hue) == len(l_seq)
    assert len(intensity) == len(l_seq)
    assert set(bundle.keys()) == {"tone", "hue", "intensity"}

    json_path = export_json_snapshot("vis_test_bundle", bundle, log_dir="logs")
    csv_path = export_csv_snapshot("vis_test_tone", tone, log_dir="logs")

    assert os.path.exists(json_path)
    assert os.path.exists(csv_path)
    with open(csv_path, "r") as f:
        header = f.readline()
        assert "tone" in header
