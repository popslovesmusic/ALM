# ALM Constitutional Engine — Analysis Core (v0.1)

## 0. Role of This Document

This file defines the **architecture and responsibilities** of the ALM Constitutional Engine in **analysis-only mode**.

The agent reading this is responsible for:
- Designing and/or implementing the ALM governance core that:
  - orchestrates tools
  - applies MGFTS rules
  - computes scores (coherence / concealment)
  - generates reports
- NOT modifying project contents (no autofix; analysis-only).

---

## 1. Concepts in Force

The agent MUST assume and respect the following global concepts:

- **Aletheia Principle**
  Cognition should evolve by reducing concealment (uncovering hidden structure, contradictions, and missing links).

- **Generalized Variational Principle (GVP)**
  Systems evolve by extremizing a functional. In this context, we minimize concealment and maximize coherence.

- **Concealment Functional**
  A measure (scalar or vector) of:
  - missing required structure
  - undefined or unused concepts
  - failed schemas
  - rule violations
  - unexplained drift

- **Coherence Field**
  A dynamic assessment of structural, semantic, and governance alignment across the project.

- **MGFTS (Meta-Global File Template System)**
  A multi-layer governance and template framework describing:
  - required files, directories, schemas
  - meta-schemas
  - ontology and concept rules
  - project initialization and validation constraints

- **Concept Preservation System (CPS)**
  Important concepts are stored in Concept Vaults and must be propagated consistently to new instructions and layers.

The Constitutional Engine MUST operate in ways that:
- reduce concealment
- increase coherence
- respect Concept Vaults
- explain decisions

---

## 2. Scope and Non-Scope

### 2.1 In Scope

The ALM Constitutional Engine MUST:

1. **Analyze** a project directory (or multiple projects) with respect to MGFTS.
2. **Call external tools** from a tool library (Python / JS / other).
3. **Collect metrics** and structured outputs from tools.
4. **Aggregate results** into internal state.
5. **Compute scores**, including:
   - structural compliance
   - governance compliance
   - schema/meta-schema compliance
   - semantic consistency
   - ecological (cross-project) consistency
   - formal/ontological soundness (where supported)
6. **Generate reports**, at minimum:
   - `MGFTS_REPORT.json`
   - `MGFTS_REPORT.md`

### 2.2 Out of Scope (for v0.1)

The ALM Constitutional Engine MUST NOT:

- Modify files.
- Generate or install templates.
- Rename or delete anything.
- Autofix violations.
- Run non-deterministic "creative" behaviors.

This is **analysis and reporting only**.

---

## 3. High-Level Architecture

The ALM Constitutional Engine is a **deterministic orchestrator**. It consists of:

1. **Input Layer**
   - Receives:
     - `project_root_path`
     - optional `mgfts_root_path`
     - optional configuration (which layers to analyze)

2. **Tool Orchestration Layer**
   - Determines which tools must be run:
     - Based on MGFTS requirements
     - Based on project type and contents
   - Dispatches structured commands to tools
   - Collects structured JSON results

3. **State & Score Aggregation Layer**
   - Merges tool outputs into a single internal representation:
     - Violations
     - Warnings
     - Metrics
     - Scores per MGFTS layer (1–7)
   - Maintains:
     - Coherence Field
     - Concealment metrics

4. **Reporting Layer**
   - Builds:
     - Machine-readable `MGFTS_REPORT.json`
     - Human-readable `MGFTS_REPORT.md`
   - Uses Aletheia as a guiding principle:
     - Prioritize surfacing what is hidden, unclear, or inconsistent.

5. **Execution Control Layer**
   - Defines the reasoning loop:
     - Analyze → Tool selection → Run tools → Aggregate → Report
   - Optionally supports multiple passes (if required by configuration).
   - Remains deterministic with respect to:
     - Tool versions
     - Manifest content
     - Input directory

---

## 4. MGFTS Layer Mapping (What the Engine Must Reflect)

The engine must support (at minimum) these analysis dimensions:

1. **Layer 1 — Structural**
   - Directories, required files, naming conventions, versions.

2. **Layer 2 — Governance**
   - Presence and correctness of:
     - AGENTS.md
     - SESSION_INSTRUCTIONS.md
     - PROJECT_RULES.md
     - COMPLIANCE_CHARTER (if project-local)
   - Proper use of "Concepts in Force."

3. **Layer 3 — Meta-Templates / Meta-Schemas**
   - Template files conform to their meta-schemas.
   - Core MGFTS meta-schemas exist and parse correctly.

4. **Layer 4 — Semantic**
   - Concepts referenced vs. defined.
   - Consistency across files.
   - Drift detection (optional, v0.1 can stub this).

5. **Layer 5 — Ecological / Ecosystem**
   - (Optional for v0.1)
     - If multiple projects are scanned:
       - Shared concepts
       - Cross-project conflicts
       - Unused or duplicated structures

6. **Layer 6 — Formal**
   - Logical consistency checks (can be minimal / deferred to future tools).

7. **Layer 7 — Ontological**
   - Concept category correctness
   - Violations of ontological constraints

The engine does not need to implement all deep formal semantics in v0.1, but it must be architected so those dimensions can be plugged in via tools.

---

## 5. Data Structures and Contracts

The engine MUST standardize internal representations for tool outputs and global reports.

### 5.1 Tool Output Contract

All tools MUST return JSON-like structures with at least:

- `tool`: string
- `version`: string
- `layer_targets`: [int] (MGFTS layer IDs)
- `violations`: [ { code, message, path, severity, layer? } ]
- `warnings`: [ { code, message, path, severity, layer? } ]
- `metrics`: { metric_name: value, ... }
- `score`: float (0–1, optional if metric-only tool)

### 5.2 Aggregated State

The engine SHOULD maintain:

```json5
{
  "project": "string",
  "timestamp": "ISO-8601",
  "tools_run": [ ... ],
  "scores": {
    "layer_1_structural": 0.0,
    "layer_2_governance": 0.0,
    "layer_3_meta_schema": 0.0,
    "layer_4_semantic": 0.0,
    "layer_5_ecological": 0.0,
    "layer_6_formal": 0.0,
    "layer_7_ontological": 0.0,
    "overall": 0.0
  },
  "violations": [ ... ],
  "warnings": [ ... ],
  "concepts_missing": [ ... ],
  "concepts_unused": [ ... ],
  "concealment_score": 0.0,
  "coherence_score": 0.0
}
```

Exact metric definitions can be refined later but MUST be structured and deterministic.

---

## 6. Reasoning Loop (v0.1)

The engine SHOULD follow this deterministic loop:

1. Discover project structure (via structural tools).
2. Determine applicable tools (based on:
   - MGFTS requirements
   - tool manifest
   - project contents).
3. Execute tools in defined order (e.g. structural → governance → schemas → semantic).
4. Collect and aggregate tool outputs.
5. Compute scores and concealment / coherence metrics.
6. Emit reports.
7. Stop.
   (No mutations; no autofix.)

---

## 7. Deliverables for Agent Implementing This Spec

The agent responsible for this architecture SHOULD produce:

1. `alm.arch.CONSTITUTIONAL_ENGINE.v0.1.md`
   - A concrete architecture doc (this spec may be used directly or refined).
2. (Optional but recommended)
   - Initial stub code files:
     - `alm/mod/governance_core.py`
     - `alm/mod/state_model.py`
     - `alm/mod/report_builder.py`
   - With docstrings only (no behavior required yet), to anchor future implementation.

The agent MUST NOT:

- Implement autofix behavior.
- Modify project files.
- Introduce side effects beyond logging & reporting.

---

**Version:** 0.1
**Status:** Specification
**Last Updated:** 2025-01-15
