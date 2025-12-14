# Layer 7 Ontological Foundation Specification

## 0. Purpose

This specification defines how MGFTS-enabled projects implement **Layer 7 (Ontological Foundation)**. It prescribes the canonical schema for concept definitions, the structure of existence predicates, and the truth-maintenance processes that keep the Global Concept Vault coherent as projects evolve.

Layer 7 ensures that every declared concept, entity, or relationship is grounded in explicit, testable predicates with lifecycle rules and evidence trails. Validation and reporting engines MUST be able to measure ontological completeness and highlight concealment introduced by undefined existence criteria.

---

## 1. Canonical Concept Schema (Layer 7 Fields)

All Layer 7-aware concept records MUST extend the following schema additions (see `mgfts/meta_schemas/concept_vault.schema.json5`):

- **`existence`** _(object, required)_
  - `predicates` _(array<string>, min 1)_: Atomic conditions that must hold for the concept to be considered present.
  - `ceases_when` _(array<string>, optional)_: Conditions that invalidate the concept.
  - `evidence` _(array<string>, optional)_: File paths, reports, or scripts that demonstrate the predicates.
  - `validation` _(object, optional)_: `{ method, frequency, steward }` describing how and how often predicates are checked.
- **`truth_maintenance`** _(object, required)_
  - `source_of_truth` _(string)_: Authoritative document or repository path for the concept.
  - `assertion_policy` _(string)_: How new statements are admitted (e.g., `closed_world`, `open_world`).
  - `revision_triggers` _(array<string>)_: Events that force reevaluation (e.g., "schema change", "governance update").
  - `conflict_resolution` _(string)_: Strategy when predicates disagree (e.g., `prefer_evidence`, `manual_review`).
- **`relationships`** _(array<object>, optional)_
  - `from`, `to`, `type`, `description`: Explicit edges to other concept IDs, harmonized with vault-level `relationships`.

Projects MAY add domain-specific fields, but the Layer 7 fields above are mandatory for vault compliance.

---

## 2. Existence Predicates

Existence predicates SHOULD be:

- **Atomic and Testable**: Each predicate is measurable (`has_unique_identifier`, `has_authentication_method`).
- **Composable**: Higher-order predicates may reference other concept predicates (e.g., `user_exists AND session_active`).
- **Traceable**: Predicates map to evidence paths, validation scripts, or data sources.
- **Lifecycle-Aware**: Include `ceases_when` conditions (archival, revocation, expiration).

**Predicate Template (`mgfts/templates/ontology_record.json5.template`):**
```json5
{
  id: "{{CONCEPT_ID}}",
  name: "{{CONCEPT_NAME}}",
  existence: {
    predicates: ["{{PREDICATE_1}}", "{{PREDICATE_2}}"],
    ceases_when: ["{{RETIREMENT_RULE}}"],
    evidence: ["{{EVIDENCE_PATH}}"],
    validation: { method: "{{CHECK_METHOD}}", frequency: "{{CADENCE}}", steward: "{{OWNER}}" }
  },
  truth_maintenance: {
    source_of_truth: "{{AUTHORITATIVE_DOC}}",
    assertion_policy: "closed_world",
    revision_triggers: ["schema change", "governance update"],
    conflict_resolution: "prefer_evidence"
  }
}
```

---

## 3. Truth Maintenance & Ontology Health

Layer 7 integrates a lightweight Truth Maintenance System (TMS):

- **Source-of-Truth Anchors**: Each concept declares `source_of_truth` and evidence pointers; validators check that anchors exist.
- **Change Propagation**: `revision_triggers` dictate when predicates must be re-evaluated (e.g., after Layer 5 ecological warnings or Layer 6 proof failures).
- **Conflict Handling**: `conflict_resolution` determines whether conflicting predicates are resolved automatically or escalated.
- **Metrics**: Validators compute `existence_coverage` (ratio of concepts with predicates) and `truth_maintenance_coverage` (ratio with complete TMS fields) and publish into Layer 7 scores.

---

## 4. Validation Expectations

Validation tools MUST enforce:

1. **Schema Conformance**: `GLOBAL_CONCEPT_VAULT.json5` validates against `concept_vault.schema.json5` (Layer 3 → Layer 7 bridge).
2. **Existence Completeness**: Every concept has ≥1 predicate; missing predicates trigger `ONTO-002` (critical) violations.
3. **Truth Maintenance Readiness**: Missing `source_of_truth` or `conflict_resolution` triggers `ONTO-003` (high) violations.
4. **Relationship Integrity**: Relationship edges MUST reference valid concept IDs; orphaned edges trigger `ONTO-004` (medium).
5. **Evidence Reachability**: Evidence paths should exist when provided; missing paths raise `ONTO-005` (warning) unless marked optional.

Layer 7 validation is invoked via `python scripts/validate_project.py . --layers 1,2,7` (or combined with other layers). Scores are aggregated into MGFTS reports under `layer_7_ontological` and surfaced in dashboards.

---

## 5. Workflows

- **Authoring Concepts**: Use `mgfts/templates/ontology_record.json5.template` to draft new concepts with predicates and truth maintenance blocks. Commit updates to `GLOBAL_CONCEPT_VAULT.json5`.
- **Schema Updates**: Evolve the vault schema through `mgfts/meta_schemas/concept_vault.schema.json5`; bump `vault_version` and add an evolution entry.
- **Validation Loop**: Run `scripts/validate_project.py` with Layer 7 enabled. Address violations by adding predicates, evidence paths, or relationship fixes.
- **Reporting**: Layer 7 coverage feeds MGFTS reports and compliance scoring. Combine with Layer 5 ecological signals (to prioritize ontology refresh) and Layer 6 proof statuses (to ensure truths are backed by evidence).

---

## 6. Deliverables

- **Schema**: `mgfts/meta_schemas/concept_vault.schema.json5`
- **Templates**: `mgfts/templates/ontology_record.json5.template`
- **Validator Hooks**: Layer 7 checks in `scripts/validate_project.py`
- **Specification**: This document (`mgfts/specs/LAYER_7_ONTOLOGY_SPEC.md`)

These deliverables collectively operationalize ontological governance, ensuring that concepts have explicit existence criteria, verifiable truths, and healthy relationships across MGFTS projects.
