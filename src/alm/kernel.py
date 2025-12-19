"""Scalar relational kernel for the ALM stencil."""

from __future__ import annotations

import numpy as np

from .bias import future_bias
from .coefficients import CoefficientTables
from .constants import NUM_REGISTERS
from .state import StencilBuffers
from .topology import DEFAULT_TOPOLOGY, NeighborTopology, aggregate_neighbors
from .validators import require_scalar


def scalar_step(
    buffers: StencilBuffers,
    coefficients: CoefficientTables,
    topology: NeighborTopology = DEFAULT_TOPOLOGY,
    pressure: float = 1.0,
    decay: float = 0.0,
) -> None:
    """Advance the FUTURE slice using the relational scalar kernel."""

    pressure_scalar = require_scalar(pressure, "pressure")
    decay_scalar = require_scalar(decay, "decay")

    now = buffers.now.data
    recent = buffers.recent.data
    stable = buffers.stable.data

    neighbor_sum = aggregate_neighbors(now, topology)
    future = buffers.future.data

    bias = future_bias(now, recent, stable)
    fast_residual = now - recent
    slow_residual = now - stable

    for target in range(NUM_REGISTERS):
        coupling = np.zeros_like(future[..., target, :])
        for source in range(NUM_REGISTERS):
            coupling += neighbor_sum[..., source, :] * coefficients.gamma[target, source]

        update = (
            coefficients.alpha[target] * fast_residual[..., target, :]
            + coefficients.beta[target] * slow_residual[..., target, :]
            + coupling
        )

        future[..., target, :] = (
            now[..., target, :]
            + pressure_scalar * (update + bias[..., target, :])
            - decay_scalar * slow_residual[..., target, :]
        )


__all__ = ["scalar_step"]
