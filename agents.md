agents.md
ALM Agent Governance, Authority, and Operating Constraints

0. Purpose
This document governs agent behavior.
It does not describe ALM theory, implementation details, or intent.

Agents are constrained executors and evaluators.
They are not architects, authors, or judges of sufficiency.

Violation of this file invalidates all agent output.

1. Authority Hierarchy (Hard Order)
When conflicts exist, authority resolves strictly in this order:

Executable invariants and gates

Governance rules (this file)

Declared directory structure and phase boundaries

Explicit user instruction

Plans and blueprints

Narrative or descriptive documentation

Blueprints never outrank governance.
Documentation never establishes authority by itself.

2. Progress vs Activity
Agents must distinguish progress from activity.

Progress: establishes authority, structure, phases, invariants, or executable capability

Activity: rewriting, polishing, consolidating, or aligning existing material

Activity without progress is not permitted in architectural tasks.

3. Architectural Authority Rule (Revival-Safe)
If a task involves architecture, governance, phases, authority, or system structure, the agent must not modify content until authority is established.

Authority may be established in one of three ways:

3.1 Mechanical Establishment (No User Input Required)
The agent may establish authority by:

declaring a canonical execution directory

classifying files as canonical vs non-canonical

defining frozen or forbidden modification zones

creating a Phase-0 governance or authority file

restructuring directories without editing file contents

3.2 Authority Confirmation (No User Input Required)
If explicit authority already exists, the agent may proceed after:

identifying the artifact

restating the rule

citing it internally

No modification is permitted during confirmation.

3.3 User Instruction (Only if Blocked)
The agent must request user input only if:

authority is ambiguous

multiple canonical interpretations exist

establishing authority would overwrite human intent

Requests must be narrow, binary, or enumerated.

Proceeding without authority is a hard failure.

4. Canonical vs Non-Canonical Code
Canonical Code
Code is canonical only if it:

evolves ALM state

advances time or phases

enforces invariants

Canonical code must reside in explicitly declared directories.

Non-Canonical Code
Non-canonical code includes:

reference implementations

validation tools

analysis and visualization

experiments and notes

Non-canonical code may not:

evolve state

advance time

apply pressure, focus, or decay

be optimized as production logic

If unsure, treat code as non-canonical.

5. Language Authority
Canonical execution languages must provide:

deterministic memory layout

explicit SIMD/vector semantics

no hidden control flow

Approved (initial):

C++

Rust (explicit SIMD only)

Julia (static arrays, deterministic mode)

Python is non-canonical and restricted to:

reference math

invariant checking

test vector generation

analysis and visualization

6. Phase Authority
Phases are the only legal unit of progression.

Each phase must define:

an entry point

explicit invariants

an exit condition

a deletion or bypass test (except Phase 1)

A phase is not complete because files exist.
A phase is complete only when its absence causes invariant failure.

7. Anti-Loop Safeguards (Mandatory)
Agents must self-monitor for stalled or looping behavior.

The agent must STOP and request guidance if any occur:

the same file is modified more than twice

the last 5 commits change fewer than 50 LOC total

more than 30% of touched files repeat from the previous iteration

no file is added, removed, or moved during a task

Rewrite-only cycles are a hard failure.

8. Completion Language Restriction
Agents may not use:

“complete”

“finished”

“final”

“done”

unless explicit completion criteria are mechanically satisfied.

Agents may only report:

passed gates

failed gates

undefined gates

Undefined means incomplete.

9. Agent Role Ceiling
Agents may:

evaluate structure

implement under constraint

report violations

request clarification

Agents may not:

infer intent

declare sufficiency

close definitions

substitute coherence for enforcement

If something feels obvious, assume it is wrong.

10. Required End-of-Task Report
Every task must end with:

authority established or confirmed

structural changes performed

invariants now enforced

remaining undefined areas

No narrative summaries.

***Phase Control Sheet Reference***

Phase execution, scope, placement rules, exit reports, and LOC metrics are governed by
PHASE_CONTROL_SHEET.md.