# AGENT MISSION CHARTER

# ✅ MISSION STATEMENT (FOR AGENT HEADER)

This agent is tasked with constructing the Chromatic Transduction Layer (CTL), a reversible speech–tone–hue–speech mapping that preserves temporal structure, intensity structure, and polarity structure. This system is the physical foundation of the Tri-Unity Chromatic Cognition architecture. No cognition, identity, or agency layers may be implemented in this phase.

Project Name: Chromatic Transduction Layer (CTL) 
 
AGENT INSTRUCTIONS — FILE CREATION & PROJECT WORKFLOW 

=========================================================

1. PROJECT ROOT
You are operating inside the project directory:

Copy code
cognition/
Do not create files outside this root unless explicitly instructed.

2. PERMITTED DIRECTORIES
You may create or modify files only inside the following directories:

bash
Copy code
/ctl/                → Code modules, JSON5 configs
/docs/architecture/  → Human-readable design documents
/logs/               → Output logs
/ctl_tests/          → Test suite (you may create this folder)
You may not create new top-level folders except /ctl_tests/ unless instructed.

3. FILE NAMING RULES
Markdown architecture documents:
Must end in .md

Must be placed under /docs/architecture/

Use descriptive names such as:

Tensor_R Update Model.md

Coupling Laws Architecture.md

JSON5 configuration files:
Must end in .json5

Must be placed under /ctl/

Use snake_case:

tensor_R.json5

tensor_L.json5

coupling_config.json5

Python implementation files:
Must end in .py

Must be placed under /ctl/ unless part of the test suite.

Use snake_case:

tensor_r_update.py

coupling.py

chromatic_utils.py

Test suite files:
Must be placed in /ctl_tests/

Filenames must begin with test_:

test_tensor_r_update.py

test_coupling.py

test_end_to_end.py

4. FILE CREATION BEHAVIOR
When creating a file:
Check if it already exists.

If it exists → Only modify sections explicitly assigned.

If it does not exist → Create it with:

Header comments

Purpose statement

Version stamp (optional)

Minimal boilerplate code or structure

When generating code:
Include imports.

Use pure Python unless otherwise specified.

Do not rely on external dependencies except:

json / json5 (if available)

math

typing

copy

All functions must be deterministic.

When generating JSON5:
Use valid JSON5 syntax:

comments allowed (//)

trailing commas allowed

unquoted keys allowed

Ensure the file is loadable by standard JSON5 parsers.

When generating Markdown:
Use headings (#, ##, ###)

Use code blocks for equations or examples

Include overview + detailed sections

5. CONTENT QUALITY RULES
The agent must ensure:

Code compiles.

JSON5 is syntactically valid.

Markdown is readable and structured.

No placeholders like “TODO” unless explicitly required.

No vague descriptions; all steps must be explicit and operational.

6. DOCUMENTATION REQUIREMENTS
For architecture documents, always include:

Purpose

Conceptual overview

Field definitions

Algorithms or update rules

Example inputs and outputs

Optional diagrams (text-based)

For code files, always include:

Docstring at top

Type annotations

Inline comments for major steps

Clear separation of:

initialization functions

update functions

utilities

sequence-level helpers

7. TEST SUITE RULES
When creating test files under /ctl_tests/:

Each test file must contain at least:

imports

a synthetic input generator

one or more test cases

simple assertions

printouts only when test fails

Prefer pure Python assert rather than unittest framework, unless instructed.

Test files must not write outside /logs/.

When generating synthetic L sequences, use simple patterns:

monotonic tone increases

repeated tones

alternating polarity

hue drift

noise-injected sequences

When coupling is implemented, test:

disparity stability

coherence growth

constraint triggers

stereo-like symmetry

8. ALLOWED ACTIONS
The agent may:

Create new files under valid directories.

Modify existing files when explicitly instructed.

Generate configuration files.

Generate Python code.

Generate Markdown documentation.

Create test suite folders and files.

The agent may NOT:

Delete files.

Rename directories.

Use external APIs.

Generate hidden or binary files.

9. IMPLEMENTATION ORDER (MANDATORY)
The agent MUST follow this order unless explicitly overridden:

Step 1 — Tensor R Model
Already completed (Markdown + JSON5 + Python module)

Step 2 — Coupling Laws
Create:

/docs/architecture/Coupling Laws Architecture.md

/ctl/coupling_config.json5

/ctl/coupling.py

Step 3 — Test Suite
Create /ctl_tests/

Then create individual test files:

tone smoothing tests

prediction tests

hue expectation tests

intensity integration tests

polarity tests

constraint tests

sequence behavior tests

coupling tests

full end-to-end tests

Step 4 — Logs
Create/update CSV logs under /logs/

10. EXECUTION SAFETY
File modifications must be reversible.

Do not overwrite large files.

Do not generate huge test data.

Avoid infinite loops in synthetic data generators.

Fail gracefully with descriptive errors.

=========================================================
END OF AGENT INSTRUCTIONS
---



