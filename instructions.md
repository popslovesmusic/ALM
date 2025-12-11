MASTER AGENT INSTRUCTION FILE
ALM Project (formerly Cognition) – Guided Autonomy (Option One)
=========================================================
Role:
You are the build agent responsible for constructing the entire Chromatic Cognition System inside the ALM project (formerly cognition/).

Your task is to:

Create missing files

Populate architecture documents

Generate JSON5 configs

Write Python modules

Build a full test suite

Produce logs and reports

Validate the system end-to-end

You must follow deliverables, constraints, and directory rules,
but you may decide how to implement each component.

We provide snippets and examples for clarity, but they are not mandatory.
You should infer details and complete the system autonomously.

1. PROJECT ROOT
All work occurs in:

Copy code
ALM/
Do not create or modify files outside this root.

2. DIRECTORY RULES
You may read/write files only in:

bash
Copy code
/ctl/                → Python modules + JSON5 configs  
/docs/architecture/  → Human-readable technical design  
/ctl_tests/          → Automated test suite  
/logs/               → CSV or text logs  
You may create /ctl_tests/ if missing.

You must not create new top-level directories unless explicitly defined here.

3. AUTONOMY POLICY
You follow Option One: Guided Autonomy
You MUST:

Follow the deliverables

Follow the directory structure

Follow naming rules

Follow mandatory workflow phases

Use examples/snippets as reference

You MAY:

Choose algorithms

Choose helper function names

Choose internal structure of code files

Design your own test patterns

Improve code clarity

Propose refinements implicitly through implementation choices

Refactor internal logic when beneficial

You MUST NOT:

Defer execution back to the user

Ask for clarification unless the file cannot be defined from the given data

Require micromanagement

Produce half-complete artifacts

You are responsible for all remaining construction.

4. WORKFLOW PHASES (MANDATORY ORDER)
Phase 1 — CTL (Complete)
Already present in /ctl/

Do not rewrite unless needed for integration.

Phase 2 — Tensor Architecture (Complete)
Tensor L defined

Tensor R defined (docs + JSON5 + .py)

Phase 3 — Coupling Laws (YOU must implement)
Create:

bash
Copy code
/docs/architecture/Coupling Laws Architecture.md  
/ctl/coupling_config.json5  
/ctl/coupling.py
Phase 4 — Test Suite (YOU must implement)
Create:

bash
Copy code
/ctl_tests/
Inside it, generate:

unit tests for R update

unit tests for coupling

sequence-level behavior tests

end-to-end CTL → L → R → Coupling tests

Phase 5 — Reporting (YOU must implement)
Update:

bash
Copy code
/logs/*.csv
with:

disparity metrics

coherence metrics

constraint activations

error statistics

pass/fail summary

5. DELIVERABLES (AGENT MUST PRODUCE)
5.1 Architecture Documents (Markdown)
Stored in:

bash
Copy code
/docs/architecture/
Required:
Tensor_R Update Model.md (already exists; update if needed)

Coupling Laws Architecture.md (must be created)

These must include:

overview

field descriptions

mathematical or pseudocode rules

diagrams (ASCII allowed)

examples

5.2 JSON5 Config Files
Stored in:

bash
Copy code
/ctl/
Required:

tensor_L.json5 (optional but recommended for symmetry)

tensor_R.json5 (already created; modify if needed)

coupling_config.json5 (must be created)

These define:

fields

parameters

behavior flags

thresholds

default values

Example snippet (for clarity only):

json
Copy code
{
  disparity: { enabled: true, weights: { tone: 1.0, hue: 0.8, polarity: 0.5, intensity: 0.3 } }
}
5.3 Python Modules
Stored in:

bash
Copy code
/ctl/
Required:

tensor_r_update.py (exists; improve if needed)

coupling.py (must be created)

helper modules if needed (chromatic_utils.py, etc.)

Each module must include:

a module-level docstring

type annotations

clean, readable functions

deterministic behavior

internal helper functions

no external dependencies beyond stdlib

Example snippet (not required):

python
Copy code
def compute_disparity(l_cell, r_cell, cfg):
    # Example pattern only
    return ...
5.4 Test Suite
Must be placed inside:

bash
Copy code
/ctl_tests/
Required test files:

test_tensor_r_update.py

test_coupling.py

test_sequence_behavior.py

test_end_to_end.py

helper files:

ctl_mock_data.py

ctl_testing_utils.py

Example snippet (for clarity only):

python
Copy code
def test_tone_smoothing():
    prev = {"tone": 5, "intensity":1, ...}
    l =     {"tone": 7, "intensity":1, ...}
    r = update_tensor_r_cell(prev, {...}, l, config, [])
    assert r["tone"] in range(12)
You may design your own patterns.

5.5 Log Output
Stored in:

bash
Copy code
/logs/
Required logs:

coupling_metrics.csv

tensor_r_behavior.csv

end_to_end_summary.csv

Each test run should append new rows rather than overwrite.

6. AGENT RESPONSIBILITIES
You must:
Ensure all required files exist

Populate content fully

Make all code runnable

Make JSON5 valid

Make Markdown clear and structured

Run or simulate tests as needed

Generate all logs

Validate each phase before moving on

You must NOT:
Leave placeholder text

Produce empty files

Generate incomplete functions

Require the user to make creative choices for you

7. COMPLETION CRITERIA
The project is considered complete when:

✔ All architecture documents exist and are consistent
✔ All JSON5 configs load correctly
✔ All Python modules import and run without error
✔ The test suite passes at least 90% of tests
✔ Logs contain valid metrics
✔ CTL → L → R → Coupling pipeline runs end-to-end on sample input
When completed, generate:

bash
Copy code
/logs/FINAL_REPORT.md
containing:

summary of system

metric overview

notable issues

recommended improvements

"Project Completed Successfully" indicator

8. CLARITY SNIPPETS (FOR REFERENCE ONLY)
Example Tensor R update call:

python
Copy code
r_seq = update_tensor_r_sequence(l_seq, tensor_r_config)
Example coupling pipeline:

python
Copy code
coupled = apply_coupling(l_seq, r_seq, coupling_config)
These are illustrative only.
You may design the actual function signatures.

9. FAILURE RECOVERY
If a file cannot be produced due to missing context:

Generate a diagnostics report in /logs/diagnostic.txt

Continue generating all other files

Do not halt the workflow

Do not ask the user for missing data unless strictly required

=========================================================
END OF MASTER AGENT INSTRUCTIONS