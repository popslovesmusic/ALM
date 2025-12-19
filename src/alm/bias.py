"""
Static Φ bias derived from the live stencil slices.

Phase 2 requires a static Φ term derived from the live stencil slices so the
runtime cannot be tuned by external inputs. The bias gently anchors the FUTURE
slice toward the blended history of ``NOW``, ``RECENT``, and ``STABLE`` without
altering rotation or decay semantics. When all three slices are equal the bias
vanishes, preserving steady-state equilibria and symmetry across lanes.
"""

from __future__ import annotations

import numpy as np


def future_bias(now: np.ndarray, recent: np.ndarray, stable: np.ndarray) -> np.ndarray:
    """Compute the Φ bias term from the current stencil history."""

    if now.shape != recent.shape or now.shape != stable.shape:
        raise ValueError("future_bias requires slices with matching shapes")

    blended = (now + recent + stable) / 3.0
    return blended - now


__all__ = ["future_bias"]
