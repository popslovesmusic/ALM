# Phase 6 Compliance Checklist

This document provides a detachable checklist for operating within Phase 6 while honoring local constraints and the global AGENTS doctrine. It records no runtime data and introduces no dependencies.

## Entry
- Load `agents.md` and `CONSTRAINTS.MD` before any activity.
- Confirm that Phase 6 remains observational-only and has no authority over Phases 1–5.

## Execution Guardrails
- Treat upstream event traces as immutable inputs; avoid writes, scheduling changes, or background tasks.
- Limit operations to relational constructions and structural transforms permitted by `CONSTRAINTS.MD` (e.g., weighted graphs, Laplacians, diffusion maps).
- Exclude semantic steps: no labels, rankings, thresholds, or feedback into ALM.

## Output Discipline
- Emit only read-only structural artifacts such as AtlasFrame coordinates, eigenvalue spectra, or tolerance-aware signatures when explicitly requested.
- Ensure outputs are deterministic within floating-point tolerance and fully detachable without affecting Phases 1–5.

## Verification
- Plan detachment, read-only, and threshold audits prior to completion to confirm causal isolation and adherence to the whitelist operations.
