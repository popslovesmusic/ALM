# MGFTS Changelog

## [1.2.0] - 2025-02-20
### Added
- Layer 7 Ontological Foundation specification detailing schemas, existence predicates, and truth maintenance workflows.
- Concept vault meta-schema (`meta_schemas/concept_vault.schema.json5`) and ontology record template (`templates/ontology_record.json5.template`).
- Layer 7 validation in `scripts/validate_project.py` with ONTO codes, coverage scoring, and report summaries.

### Changed
- Expanded `GLOBAL_CONCEPT_VAULT.json5` with existence/truth-maintenance blocks for all core concepts and updated ontology metadata.
- Updated governance and README guidance to describe ontology workflows and Layer 5–7 compliance interplay.

## [1.1.0] - 2025-02-01
### Added
- Layer 5 Ecological Intelligence specification covering pattern detection pipelines, data inputs, and health metrics.
- Default ecological configuration (`mgfts/config/layer5_ecology.json5`) with collector toggles and metric thresholds.
- Validation hooks in `scripts/validate_project.py` to score ecological health and surface Layer 5 warnings.
- Governance alignment updates for Layer 5 in README, Constitutional Engine spec, and Global Concept Vault (CORE-009).

### Changed
- Configuration template now includes Layer 5 toggles and health metric placeholders.

### Notes
- Ecological reporting and remediation guidance align with Aletheia (reduce concealment) and GVP (maximize coherence).
