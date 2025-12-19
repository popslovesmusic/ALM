"""Placeholder SIMD module.

Python is non-canonical for SIMD execution; this module intentionally raises to
prevent accidental use as a production path. It remains as a scaffold for
future reference-only vector experiments.
"""

from __future__ import annotations


def step(*_: object, **__: object) -> None:
    raise NotImplementedError("AVX2 path is not available in the Python reference")


__all__ = ["step"]
