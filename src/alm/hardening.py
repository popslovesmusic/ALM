"""Hardening helpers for cadence and stress validation."""

from __future__ import annotations

from typing import Callable, Iterable, Iterator

import numpy as np

from .boundary import apply_resonant_boundary
from .coefficients import CoefficientTables
from .focus import FocusTracker
from .ingest import IngestController
from .topology import DEFAULT_TOPOLOGY, NeighborTopology
from .state import StencilBuffers
from .kernel import scalar_step
from .avx2 import avx2_step


Engine = Callable[[StencilBuffers, CoefficientTables, NeighborTopology, float, float], None]


def exercise_cadence(
    buffers: StencilBuffers,
    coefficients: CoefficientTables,
    ingest_controller: IngestController,
    focus_tracker: FocusTracker,
    frames: Iterable[np.ndarray],
    jitters: Iterable[np.ndarray],
    topology: NeighborTopology = DEFAULT_TOPOLOGY,
    pressures: Iterable[float] | float = 1.0,
    decays: Iterable[float] | float = 0.0,
    engine: Engine = scalar_step,
    boundary_phase: float = 0.0,
) -> None:
    """Run a sequence of ingest/focus/kernel steps to stress cadence."""

    pressure_iter = _as_iterator(pressures, "pressures")
    decay_iter = _as_iterator(decays, "decays")

    for frame, jitter in zip(frames, jitters):
        pressure_value = next(pressure_iter)
        decay_value = next(decay_iter)

        ingest_controller.ingest(buffers, frame)

        focus_map = focus_tracker.handoff(jitter, pressure=pressure_value)

        engine(
            buffers,
            coefficients,
            topology=topology,
            pressure=pressure_value,
            decay=decay_value,
        )

        future = buffers.future.data
        apply_resonant_boundary(future, phase=boundary_phase)
        future *= focus_map.astype(future.dtype)[..., None, None]

        ingest_controller.advance(buffers)


def _as_iterator(value: Iterable[float] | float, label: str) -> Iterator[float]:
    if isinstance(value, (int, float)):
        while True:
            yield float(value)
    else:
        consumed = False
        last_value = None
        for entry in value:
            consumed = True
            last_value = float(entry)
            yield last_value
        if not consumed:
            raise ValueError(f"{label} iterable must provide at least one value")
        while True:
            assert last_value is not None
            yield last_value


__all__ = ["exercise_cadence", "Engine", "avx2_step", "scalar_step"]
