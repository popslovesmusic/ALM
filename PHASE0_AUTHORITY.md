Phase 0 Authority Declaration

Authority Order
- Governance acknowledged per agents.md and agents_plan.md.

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
Authority Status
- Authority mechanically established in Phase 0 for structural enforcement only.

>>>>>>> theirs
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
Authority Status
- Authority mechanically established in Phase 0 for structural enforcement only.

Gate Artifacts (present on disk)
- alm/core/CANONICAL_EXECUTION
- alm/core/FROZEN_NO_EDITS
- src/alm/FROZEN_NO_EDITS
- src/alm/REFERENCE_ONLY
- tests/FROZEN_NO_EDITS
- tests/REFERENCE_ONLY
- docs/FROZEN_NO_EDITS

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
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

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
Phase 0 Report (per agents.md §10)
- Authority established or confirmed: yes (Phase 0 declaration and markers).
- Structural changes performed: marker files placed for canonical, reference, and documentation scopes.
- Invariants now enforced: modification freezes applied to canonical execution, reference/validation, and documentation zones.
- Remaining undefined areas: none flagged in Phase 0; later phases may introduce new invariants.

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
Classification Counts (buckets A/B/C/D)
- A (Canonical Execution): 19 files (alm/core, including markers and include assets).
- B (Reference/Validation): 43 files (src/alm, tests, pyproject.toml, dir.py, .gitignore, root CMakeLists.txt).
- C (Documentation/Descriptive): 49 files (docs/ excluding legacy, top-level governance/notes files).
- D (Legacy/Archived): 12 files (docs/legacy/ subtree).

Blockers
- None detected during authority establishment.
