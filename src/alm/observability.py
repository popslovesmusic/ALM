"""Passive observability helpers for the ALM stencil.

Phase 7 introduces observables that expose stencil state without altering
rotation, pressure channels, or topology. All helpers return copies so callers
cannot accidentally mutate the live buffers while computing spiral projections
or archival snapshots.
"""

from __future__ import annotations

<<<<<<< ours
<<<<<<< ours
from typing import Dict, Iterable
=======
=======
>>>>>>> theirs
import hashlib
from collections import deque
from dataclasses import dataclass
from typing import Deque, Dict, Iterable, List, Tuple
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs

import numpy as np

from .constants import GRID_COLS, GRID_ROWS, NUM_REGISTERS, STENCIL_ORDER
from .state import StencilBuffers


def _resolve_slice(stencil: StencilBuffers, name: str) -> np.ndarray:
    normalized = name.strip().upper()
    if normalized not in STENCIL_ORDER:
        raise KeyError(f"Unknown stencil slice '{name}'")

    return getattr(stencil, normalized.lower()).data


def observable_snapshot(
    stencil: StencilBuffers, slices: Iterable[str] = STENCIL_ORDER
) -> Dict[str, np.ndarray]:
    """Return copies of the requested stencil slices.

    The returned arrays are detached from the live buffers to guarantee passive
    observation. Callers may mutate the copies without affecting the stencil or
    its rotation order.
    """

    snapshot: Dict[str, np.ndarray] = {}
    for name in slices:
        slice_data = _resolve_slice(stencil, name)
        snapshot[name.upper()] = slice_data.copy()

    return snapshot


def spiral_components(state_slice: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Compute radial magnitude and angular phase for spiral observables.

    Radial magnitude uses the L2 norm across the four registers to capture
    persistence, while angular phase derives from the R/G registers to preserve
    the dual-frequency orientation without mutating the payload.
    """

    expected_shape = (GRID_ROWS, GRID_COLS, NUM_REGISTERS, state_slice.shape[-1])
    if state_slice.shape[:3] != expected_shape[:3]:
        raise ValueError(
            f"state_slice must have leading shape {expected_shape[:3]},"
            f" got {state_slice.shape[:3]}"
        )

    radial = np.linalg.norm(state_slice, axis=2)
    angular = np.arctan2(state_slice[..., 1, :], state_slice[..., 0, :])
    return radial, angular


def spiral_observation(
    stencil: StencilBuffers, slice_name: str = "NOW"
) -> Dict[str, np.ndarray]:
    """Produce passive spiral observables from a stencil slice.

    The observation is returned as detached arrays keyed by ``radial`` and
    ``angular`` to allow downstream instrumentation without altering the live
    stencil payload.
    """

    slice_data = _resolve_slice(stencil, slice_name)
    radial, angular = spiral_components(slice_data)
    return {"radial": radial.copy(), "angular": angular.copy()}


__all__ = ["observable_snapshot", "spiral_components", "spiral_observation"]
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs


@dataclass(frozen=True)
class TraceRetentionPolicy:
    """Retention policy for diagnostic traces."""

    window: int = 64
    durable: bool = True

    def __post_init__(self) -> None:
        if self.window <= 0:
            raise ValueError("window must be a positive integer")


def _copy_observation(observation: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    return {key: value.copy() for key, value in observation.items()}


def observation_fingerprint(observation: Dict[str, np.ndarray]) -> str:
    """Compute a deterministic fingerprint for an observation payload."""

    digest = hashlib.sha256()
    for key in sorted(observation):
        digest.update(key.encode("utf-8"))
        digest.update(observation[key].tobytes())
    return digest.hexdigest()


class TraceRecorder:
    """Non-intrusive trace recorder with bounded retention."""

    def __init__(self, policy: TraceRetentionPolicy = TraceRetentionPolicy()):
        self.policy = policy
        self._window: Deque[Tuple[int, Dict[str, np.ndarray]]] = deque(
            maxlen=policy.window
        )
        self._archive: List[Tuple[int, Dict[str, np.ndarray]]] | None = (
            [] if policy.durable else None
        )

    def record(self, step: int, observation: Dict[str, np.ndarray]) -> None:
        """Record a passive observation with retention and optional durability."""

        safe_obs = _copy_observation(observation)
        entry = (step, safe_obs)
        self._window.append(entry)
        if self._archive is not None:
            self._archive.append(entry)

    @property
    def window(self) -> List[Tuple[int, Dict[str, np.ndarray]]]:
        return [(step, _copy_observation(obs)) for step, obs in self._window]

    @property
    def archive(self) -> List[Tuple[int, Dict[str, np.ndarray]]]:
        if self._archive is None:
            return []
        return [(step, _copy_observation(obs)) for step, obs in self._archive]

    def window_fingerprints(self) -> List[str]:
        return [observation_fingerprint(obs) for _, obs in self._window]

    def archive_fingerprints(self) -> List[str]:
        if self._archive is None:
            return []
        return [observation_fingerprint(obs) for _, obs in self._archive]


__all__ += [
    "TraceRecorder",
    "TraceRetentionPolicy",
    "observation_fingerprint",
]
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
