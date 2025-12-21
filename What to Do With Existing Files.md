What to Do With Existing Files (Canonical Policy)
Principle (Non-Negotiable)
Existing files are evidence, not authority.
Authority is granted only by placement and classification, not by content quality or intent.

Step 1 — Classify Everything (No Editing)
Every existing file must be placed into exactly one of these buckets.
This step is mechanical only: moves, folders, marker files. No edits.

A. Canonical Execution (Very Small Set)
Criteria

Evolves ALM state

Advances time/phases

Enforces invariants

Action

Place under the declared canonical path (e.g., alm/core/…)

If already there, leave content untouched

If content is mixed, extract nothing yet (that is Phase 1+)

Rule

If a file might be canonical but is ambiguous, treat it as non-canonical for now.

B. Reference / Validation (Large Set)
Criteria

Python implementations

Scalar math

Validators

Coefficient checks

Analysis, plotting, harnesses

Action

Move to reference/ (or equivalent)

Freeze content

Add a one-line marker file in the directory:

nginx
Copy code
NON_CANONICAL_REFERENCE
Rule

Reference code may explain the system, but may never be the system.

C. Documentation (Descriptive Only)
Criteria

Blueprints

Plans

Practitioner notes

Journals

PDFs

Theory narratives

Action

Move to docs/

Subdivide into:

docs/blueprint/

docs/legacy/

docs/notes/

Do not consolidate, rewrite, or dedupe

Rule

Documentation describes constraints; it does not enforce them.

D. Legacy / Archived
Criteria

Superseded plans

Historical experiments

Files no longer referenced by governance

Action

Move to docs/legacy_ARCHIVED_DO_NOT_USE/

Add a top-level README stating:

“Archived. Not authoritative.”

Step 2 — Freeze by Default
After classification:

All non-canonical directories are frozen

Canonical directories are frozen until Phase 1 begins

Any edit outside the active phase is a hard failure

Add marker files where needed:

objectivec
Copy code
FROZEN_NO_EDITS
CANONICAL_EXECUTION
REFERENCE_ONLY
These markers are governance signals, not documentation.

Step 3 — Do NOT “Fix” Mixed Files Yet
If a file contains:

theory + code

reference + execution

multiple phases

Do nothing now.

Why:

Extraction is Phase work

Phase work requires invariants

Invariants do not exist yet

Mixed files are tolerated temporarily but disempowered by placement.

Step 4 — When Existing Files Are Allowed to Change
Existing files may be edited only when all are true:

The phase that governs them is active

The file is in a canonical directory

The edit advances enforcement, not clarity

A deletion test exists (or is being created)

Otherwise: hands off.

Step 5 — What the Agent Must Report (Required)
For existing files, the agent’s report must include only:

Count of files in each class (A/B/C/D)

Canonical execution paths

Frozen zones

Any ambiguous files deferred

No opinions. No summaries.

One-Sentence Law (Put This in Your Head)
Existing files are inert until governance gives them force.

