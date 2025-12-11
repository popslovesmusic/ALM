"""
Multi-tensor assembly utilities for coordinating multiple R fibers in parallel.

This module keeps Tensor L fixed and instantiates multiple Tensor R sequences
using the existing update functions. It also aggregates fiber outputs to create
a combined representation and exposes simple comparison helpers for coherence
and disparity monitoring.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

from ctl.coupling import compute_coupling_metrics, process_coupling_sequence
from ctl.tensor_r_update import update_tensor_r_sequence

ChromaticCell = Dict[str, Any]
Config = Dict[str, Any]


class MultiTensorAssembly:
    """Manage multiple Tensor R fibers driven by a shared Tensor L."""

    def __init__(
        self,
        r_configs: Sequence[Config],
        coupling_config: Optional[Config] = None,
    ) -> None:
        self.r_configs = list(r_configs)
        self.coupling_config = coupling_config

    def run_r_fibers(self, l_sequence: List[ChromaticCell]) -> List[List[ChromaticCell]]:
        """Instantiate R sequences for each configured fiber."""
        results: List[List[ChromaticCell]] = []
        for cfg in self.r_configs:
            results.append(update_tensor_r_sequence(l_sequence, cfg))
        return results

    def aggregate_states(
        self,
        r_sequences: Sequence[List[ChromaticCell]],
        weights: Optional[Sequence[float]] = None,
    ) -> List[ChromaticCell]:
        """Combine multiple R sequences into a single aggregated stream."""
        if not r_sequences:
            return []

        min_length = min(len(seq) for seq in r_sequences)
        weights_resolved = _normalize_weights(weights, len(r_sequences))
        aggregated: List[ChromaticCell] = []

        for idx in range(min_length):
            cells = [seq[idx] for seq in r_sequences]
            aggregated.append(_aggregate_cells(cells, weights_resolved))
        return aggregated

    def summarize_fibers(
        self, l_sequence: List[ChromaticCell], r_sequences: List[List[ChromaticCell]]
    ) -> List[Dict[str, float]]:
        """Compute coupling metrics per fiber relative to the shared L."""
        if not self.coupling_config:
            return []
        return [
            compute_coupling_metrics(l_sequence, r_seq, self.coupling_config) for r_seq in r_sequences
        ]

    def run_full(
        self,
        l_sequence: List[ChromaticCell],
        weights: Optional[Sequence[float]] = None,
    ) -> Dict[str, Any]:
        """Run fibers, aggregate them, and compute optional coupling summaries."""
        r_sequences = self.run_r_fibers(l_sequence)
        aggregated = self.aggregate_states(r_sequences, weights=weights)
        coupling_metrics: List[Dict[str, float]] = []
        if self.coupling_config:
            coupling_metrics = self.summarize_fibers(l_sequence, r_sequences)

        return {
            "r_sequences": r_sequences,
            "aggregated": aggregated,
            "coupling_metrics": coupling_metrics,
        }

    def compare_aggregated_to_l(self, l_sequence: List[ChromaticCell], aggregated: List[ChromaticCell]) -> Dict[str, float]:
        """Compare the aggregated R representation back to L."""
        if not self.coupling_config:
            return {}
        return compute_coupling_metrics(l_sequence, aggregated, self.coupling_config)


def run_multi_tensor(
    l_sequence: List[ChromaticCell],
    r_configs: Sequence[Config],
    coupling_config: Optional[Config] = None,
    weights: Optional[Sequence[float]] = None,
) -> Dict[str, Any]:
    """Convenience wrapper for MultiTensorAssembly.run_full."""
    assembly = MultiTensorAssembly(r_configs, coupling_config=coupling_config)
    return assembly.run_full(l_sequence, weights=weights)


def couple_fiber_snapshots(
    l_sequence: List[ChromaticCell],
    r_sequences: Sequence[List[ChromaticCell]],
    coupling_config: Config,
) -> List[Dict[str, Any]]:
    """Run coupling on each fiber and return per-step/per-sumary snapshots."""
    snapshots: List[Dict[str, Any]] = []
    for r_seq in r_sequences:
        snapshots.append(process_coupling_sequence(l_sequence, r_seq, coupling_config))
    return snapshots


def _normalize_weights(weights: Optional[Sequence[float]], count: int) -> List[float]:
    if weights is None or len(weights) != count:
        return [1.0 / max(1, count)] * max(1, count)
    total = sum(weights) or 1.0
    return [w / total for w in weights]


def _aggregate_cells(cells: Sequence[ChromaticCell], weights: Sequence[float]) -> ChromaticCell:
    tone = 0.0
    intensity = 0.0
    hue_acc = [0.0, 0.0, 0.0]
    coherence = 0.0
    polarity_votes = 0.0

    for cell, w in zip(cells, weights):
        tone += w * cell.get("tone", 0)
        intensity += w * float(cell.get("intensity", 0.0))
        coherence += w * float(cell.get("coherence", 1.0))
        polarity_votes += w * float(cell.get("polarity", 1))
        hue_vals = cell.get("hue", [0, 0, 0])
        for idx, val in enumerate(hue_vals):
            hue_acc[idx] += w * float(val)

    aggregated_cell: ChromaticCell = {
        "tone": int(round(tone)) % 12,
        "hue": [int(round(x)) for x in hue_acc],
        "intensity": intensity,
        "polarity": 1 if polarity_votes >= 0 else -1,
        "timestamp": cells[0].get("timestamp", 0.0),
        "coherence": coherence,
    }
    return aggregated_cell


__all__ = [
    "MultiTensorAssembly",
    "run_multi_tensor",
    "couple_fiber_snapshots",
]
