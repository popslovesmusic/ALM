"""Shared validation helpers for ALM runtime parameters."""

from __future__ import annotations

import numpy as np


def require_scalar(value: float, name: str) -> float:
    """Ensure a parameter is a scalar float-like value.

    The blueprint prohibits embedding control metadata in per-cell or per-lane
    parameters such as pressure or decay. Rejecting non-scalar inputs prevents
    implicit control channels from bypassing the ontology guards.
    """

    if np.ndim(value) != 0:
        raise ValueError(f"{name} must be a scalar, received shape {np.shape(value)}")

    return float(value)


__all__ = ["require_scalar"]
