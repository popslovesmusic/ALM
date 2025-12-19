"""Vectorized AVX2-equivalent kernel path.

Phase 5 mirrors the scalar relational kernel with an AVX2-friendly
formulation. While implemented in NumPy here, the data flow matches the
intrinsic-friendly structure: branchless, fully uniform across lanes, and
expressed as fused vector operations that can be ported directly to the
allowed AVX2 instructions.
"""

from __future__ import annotations

import numpy as np

from .coefficients import CoefficientTables
from .state import StencilBuffers
from .topology import DEFAULT_TOPOLOGY, NeighborTopology, aggregate_neighbors
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
from .validators import require_scalar
>>>>>>> theirs
=======
from .validators import require_scalar
>>>>>>> theirs
=======
from .validators import require_scalar
>>>>>>> theirs


def avx2_step(
    buffers: StencilBuffers,
    coefficients: CoefficientTables,
    topology: NeighborTopology = DEFAULT_TOPOLOGY,
    pressure: float = 1.0,
    decay: float = 0.0,
) -> None:
    """Advance the FUTURE slice using an AVX2-aligned update rule.

    The computation is structured as straight-line vector math with no
    branching or masking. Neighbor aggregation is applied uniformly, and the
    canonical coefficient tables broadcast across the lane dimension to keep
    parity with the scalar path while matching the SIMD simultaneity contract.
    """

<<<<<<< ours
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
=======
    pressure_scalar = require_scalar(pressure, "pressure")
    decay_scalar = require_scalar(decay, "decay")

>>>>>>> theirs
    now = buffers.now.data
    recent = buffers.recent.data
    stable = buffers.stable.data

    fast_residual = now - recent
    slow_residual = now - stable

    neighbor_sum = aggregate_neighbors(now, topology)

    coupling = np.einsum("...sl,tsl->...tl", neighbor_sum, coefficients.gamma)

    alpha = coefficients.alpha[np.newaxis, np.newaxis, :, :]
    beta = coefficients.beta[np.newaxis, np.newaxis, :, :]

    update = alpha * fast_residual + beta * slow_residual + coupling

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    buffers.future.data[:] = now + pressure * update - decay * slow_residual
=======
    buffers.future.data[:] = now + pressure_scalar * update - decay_scalar * slow_residual
>>>>>>> theirs
=======
    buffers.future.data[:] = now + pressure_scalar * update - decay_scalar * slow_residual
>>>>>>> theirs
=======
    buffers.future.data[:] = now + pressure_scalar * update - decay_scalar * slow_residual
>>>>>>> theirs


def avx2_equivalent_step(
    buffers: StencilBuffers,
    coefficients: CoefficientTables,
    topology: NeighborTopology = DEFAULT_TOPOLOGY,
    pressure: float = 1.0,
    decay: float = 0.0,
) -> None:
    """Alias for parity with the scalar path to ease deterministic checks."""

    avx2_step(buffers, coefficients, topology=topology, pressure=pressure, decay=decay)


__all__ = ["avx2_step", "avx2_equivalent_step"]
