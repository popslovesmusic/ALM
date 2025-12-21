Phase 0 Authority Declaration

Authority Order
- Governance acknowledged per agents.md and agents_plan.md.

Canonical Paths
- alm/core (C++ build under CMake); marker: CANONICAL_EXECUTION; build gate: root CMakeLists.txt.

Non-Canonical Reference/Validation Paths
- src/alm (Python reference set); marker: REFERENCE_ONLY.
- tests (validation harnesses); marker: REFERENCE_ONLY.
- Support artifacts: pyproject.toml, dir.py, .gitignore.

Documentation Paths
- docs/ (blueprints, theory, related context, tests_and_support); marker: FROZEN_NO_EDITS.
- Top-level governance and notes: agents.md, agents_plan.md, ALM Practitioner Notes.md, ALM_READINESS_REPORT.md, What to Do With Existing Files.md, gemini.md.bak.
- Legacy archive: docs/legacy/ (bucket D).

Frozen Zones
- Canonical execution frozen until Phase 1: alm/core (FROZEN_NO_EDITS).
- Non-canonical reference frozen: src/alm (FROZEN_NO_EDITS), tests (FROZEN_NO_EDITS).
- Documentation frozen: docs/ (FROZEN_NO_EDITS) and all listed top-level documentation files.

Phase Boundaries
- Phase 0 active; no advancement beyond Phase 0 authorized.

Classification Counts (buckets A/B/C/D)
- A (Canonical Execution): 19 files (alm/core, including markers and include assets).
- B (Reference/Validation): 43 files (src/alm, tests, pyproject.toml, dir.py, .gitignore, root CMakeLists.txt).
- C (Documentation/Descriptive): 49 files (docs/ excluding legacy, top-level governance/notes files).
- D (Legacy/Archived): 12 files (docs/legacy/ subtree).

Blockers
- None detected during authority establishment.
