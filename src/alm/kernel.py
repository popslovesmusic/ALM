"""Scalar relational kernel for the ALM stencil.

Phase 4 introduces the residual-based scalar kernel that advances the FUTURE
slice using NOW/RECENT/STABLE data, canonical coefficients, and uniform
neighbor aggregation. The update is branchless and symmetric across lanes to
mirror the SIMD contract that will be enforced in the AVX2 path.
"""

from __future__ import annotations

import numpy as np

from .coefficients import CoefficientTables
from .constants import NUM_REGISTERS
from .state import StencilBuffers
from .topology import DEFAULT_TOPOLOGY, NeighborTopology, aggregate_neighbors
<<<<<<< ours
<<<<<<< ours
=======
from .validators import require_scalar
>>>>>>> theirs
=======
from .validators import require_scalar
>>>>>>> theirs


def scalar_step(
    buffers: StencilBuffers,
    coefficients: CoefficientTables,
    topology: NeighborTopology = DEFAULT_TOPOLOGY,
    pressure: float = 1.0,
    decay: float = 0.0,
) -> None:
    """Advance the FUTURE slice using the relational scalar kernel.

    The update is residual-based: both fast (NOW−RECENT) and slow
    (NOW−STABLE) components contribute, along with uniform neighbor
    aggregation weighted by the canonical Γ tables. Pressure and decay are
    multiplicative scalars that modulate the composite update without
    introducing control flow.
    """

<<<<<<< ours
<<<<<<< ours
=======
    pressure_scalar = require_scalar(pressure, "pressure")
    decay_scalar = require_scalar(decay, "decay")

>>>>>>> theirs
=======
    pressure_scalar = require_scalar(pressure, "pressure")
    decay_scalar = require_scalar(decay, "decay")

>>>>>>> theirs
    now = buffers.now.data
    recent = buffers.recent.data
    stable = buffers.stable.data

    neighbor_sum = aggregate_neighbors(now, topology)
    future = buffers.future.data

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

<<<<<<< ours
<<<<<<< ours
        future[..., target, :] = now[..., target, :] + pressure * update - decay * slow_residual[
            ..., target, :
        ]
=======
=======
>>>>>>> theirs
        future[..., target, :] = (
            now[..., target, :]
            + pressure_scalar * update
            - decay_scalar * slow_residual[..., target, :]
        )
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs


__all__ = ["scalar_step"]
