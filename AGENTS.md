# AGENTS.md

> STATUS: CANONICAL  
> ROLE: Global Agent Doctrine & Compliance Gate  
> SCOPE: Entire Repository

This file defines **global, non-negotiable rules** governing all agent behavior.
It is always in effect and applies across all directories and phases.

This repository is governed by **MGFTS**.  
All agents are subject to **automatic compliance enforcement**.

---

## 1. Instruction Resolution & Scope

Agents MUST resolve instructions in the following order:

1. Nearest 'AGENTS.md` in working directory
2. This global `AGENTS.md`
3. Canonical documents referenced herein

If no directory `AGENTS.md` exists:
- The agent MUST STOP
- The agent MUST REPORT that no executable 'AGENTS.md' is authorized

Agents are NOT permitted to infer tasks, phases, or intent.

---

## 2. Canonical Authority (Always Binding)

The following documents override all agent heuristics:

- `active/canonical/SSOT alm.md`
- `active/canonical/ALM_IMPLEMENTATION_CHARTER.md`
- `alm/core/CONSTRAINTS.md` (when operating in `alm/core/`)
- `mgfts/COMPLIANCE_CHARTER.md`
- `mgfts/CONSTITUTIONAL_AXIOMS.md`
- Any directory-scoped `AGENTS.md`

Conflicts MUST result in STOP + REPORT.

---

## 3. MGFTS Enforcement (Mandatory)

MGFTS is the **governing framework** for:

- architectural fidelity
- process correctness
- documentation integrity
- phase transitions

Agents MUST treat MGFTS as **always active**, not optional.

---

## 4. Automatic Compliance Checkpoints

Agents MUST perform compliance checks at the following moments:

### 4.1 Phase Entry Check
Before beginning any phase:
- Confirm the phase is explicitly authorized by a scoped `AGENTS.md`
- Confirm no higher phase artifacts already exist
- Confirm required canonical documents are present

If any check fails → STOP.

---

### 4.2 In-Phase Compliance Check
While executing an authorized phase:
- Ensure no forbidden artifacts are introduced
- Ensure no out-of-scope files are modified
- Ensure all actions conform to declared phase boundaries

If drift is detected → STOP + REPORT.

---

### 4.3 Phase Completion Check
Before declaring a phase complete:
- Verify completion criteria stated in scoped `AGENTS.md`
- Verify no MGFTS constraints were violated
- Verify outputs are placed in correct directories
- Verify legacy systems were not modified or reactivated

Phase completion is invalid without passing this check.

---

### 4.4 Phase Transition Gate
An agent MUST NOT proceed to a new phase unless:
- Explicitly authorized by a new scoped `AGENTS.md`
- All prior phase checks have passed
- Canonical documents have not changed incompatibly

Otherwise → STOP.

---

## 5. Prohibited Global Agent Behavior

Regardless of phase, agents MUST NOT:

- Bypass MGFTS compliance checks
- Modify canonical documents unless explicitly authorized
- Introduce symbolic or semantic abstractions without authorization
- Advance phases implicitly
- Fill in missing information by assumption
- Optimize or refactor outside declared scope

Silence and stopping are preferred over guessing.

---

## 6. Architectural Invariants (Always Enforced)

Agents MUST preserve the following invariants at all times:

- Finite time ontology
- SIMD lanes as relational ontology
- Cache-bounded cognition
- Call-gated long-term memory
- Separation of spatial substrate and relational algebra
- Quarantining of legacy systems (CTL, symbolic pipelines)

Violation of any invariant requires STOP + REPORT.

---

## 7. Reporting Requirements

When stopping or completing work, agents MUST report:

- Phase name
- Scope (directory)
- Actions taken
- Compliance status
- Any deviations or ambiguities encountered

Reports MUST be factual and non-interpretive.

---

## 8. Enforcement Philosophy

Agents are **constrained executors**, not collaborators.

Correct execution is:
- minimal
- explicit
- phase-bounded
- MGFTS-compliant

Agents are not authorized to improve, extend, or reinterpret the system.

---

## End of Global AGENTS.md
