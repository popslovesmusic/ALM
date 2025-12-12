# ALM Reporting Engine Specification (MGFTS Reports)

## 0. Purpose

This document instructs the agent to design the **Reporting Engine** for the ALM Constitutional Engine.

The Reporting Engine:
- takes aggregated analysis state
- produces:
  - `MGFTS_REPORT.json` (machine-readable)
  - `MGFTS_REPORT.md` (human-readable)

---

## 1. Concepts in Force

- **Aletheia Principle:**
  The report should highlight areas of concealment: missing structure, undefined concepts, violations.

- **Coherence Field:**
  The report should show how coherent the project is across MGFTS layers.

- **Layered MGFTS Model (1–7):**
  The report must reflect per-layer scores and issues.

---

## 2. Inputs to the Reporting Engine

The Reporting Engine SHOULD receive a data structure with:

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

Exact structure can be adjusted but MUST be deterministic and documented.

---

## 3. JSON Report (`MGFTS_REPORT.json`)

The JSON report MUST:

- Serialize the aggregated state.
- Use stable key ordering (for diffing and tests).
- Include:
  - scores
  - violations
  - warnings
  - tools_run
  - derived indicators (e.g. "pass/fail thresholds").

The agent SHOULD define a JSON schema for this file, e.g.:

`mgfts/meta_schemas/mgfts_report.schema.json5`

---

## 4. Markdown Report (`MGFTS_REPORT.md`)

The Markdown report MUST be human-friendly.

Recommended sections:

1. **Header**
   - Project name
   - Scan time
   - MGFTS version
   - ALM-GOV engine version
2. **Summary Table**
   - Per-layer scores:
     - Structural
     - Governance
     - Meta-schema
     - Semantic
     - Ecological
     - Formal
     - Ontological
   - Overall score
   - Concealment vs Coherence
3. **Key Findings**
   - Top N serious violations
   - Top N warnings
   - Missing or undefined core concepts
   - Critical structural gaps
4. **Layer-by-Layer Analysis**
   - Per layer:
     - Score explanation
     - List of relevant violations
     - Notes
5. **Concept View**
   - Missing concepts (referenced but undefined)
   - Unused concepts (defined but never referenced)
6. **Aletheia & Coherence Commentary**
   - Short narrative describing:
     - Where concealment is concentrated.
     - How coherence could be increased (descriptive, no instructions to change files).

---

## 5. Deliverables for Agent

The agent SHOULD:

1. Draft `alm/mod/reporting_engine_design.md`
   - Summarizing the above behavior.
2. Optionally create stub code files:
   - `alm/mod/report_writer_json.py`
   - `alm/mod/report_writer_md.py`

With function signatures and docstrings only.

The agent MUST NOT:

- Implement business logic for the entire Constitutional Engine here.
- Attempt to modify any project content.

---

**Version:** 1.0
**Status:** Specification
**Last Updated:** 2025-01-15
