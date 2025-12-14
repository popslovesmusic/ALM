# Getting Started with MGFTS

This guide walks new contributors through the minimum steps to launch, validate, and extend a project using the Meta-Global File Template System (MGFTS). It complements the main README by providing a hands-on path from cloning the repository to running compliance checks across Layers 1–7.

## Who this is for
- First-time contributors who need a guided path through MGFTS conventions.
- Maintainers who want a repeatable onboarding script for new projects.
- Reviewers who need a checklist-oriented view of MGFTS deliverables.

## Prerequisites
- **Python** available in your environment (the validation and scaffolding scripts are Python-based and rely only on the standard library).
- Permission to initialize Git repositories on your machine.
- A working shell environment where you can run `python` commands.

## Step 1 — Clone and inspect the toolkit
1. Clone the repository and switch into it:
   ```bash
   git clone <repo-url> mgfts-toolkit
   cd mgfts-toolkit
   ```
2. Skim the governance anchors in `mgfts/`:
   - `AGENTS.md` for agent behavior
   - `COMPLIANCE_CHARTER.md` and `PRESERVATION_PROTOCOL.md` for required practices
   - `GLOBAL_CONCEPT_VAULT.json5` for registered concepts and ontology fields
   - `templates/` and `meta_schemas/` for reusable scaffolds and validators

## Step 2 — Scaffold a new project
Create a project from the provided generator:
```bash
python scripts/create_new_project.py my-awesome-project
```
This produces a ready-to-validate workspace with:
- Standardized layout (src/tests/docs/mgfts) anchored to Layer 1.
- Governance files copied into the new `mgfts/` directory.
- Template placeholders for code, tests, configs, and ontology records.

## Step 3 — Run your first validation
From the newly created project root:
```bash
python scripts/validate_project.py .
```
You will see a per-layer summary with concealment/coherence indicators. To focus on specific layers:
```bash
python scripts/validate_project.py . --layers 1,2
python scripts/validate_project.py . --layers 1,2,7 --severity high
```
Use `--output report.json` to capture machine-readable reports that mirror `mgfts/meta_schemas/mgfts_report.schema.json5`.

## Step 4 — Work with templates
Templates live in `mgfts/templates/` and `mgfts/meta_templates/`.
- Copy the closest template to your target location.
- Replace placeholder variables (e.g., `{{MODULE_DESCRIPTION}}`, ontology predicate stubs) with project-specific values.
- Keep the structure intact so meta-schemas remain valid.

Common starting points:
- `python_module.py.template` and `python_test.py.template` for code/tests.
- `config.json5.template` for configuration blocks.
- `ontology_record.json5.template` for Layer 7 concept predicates and truth maintenance.

## Step 5 — Add or update ontology entries
When a feature introduces a new concept or changes an existing one:
1. Start from `templates/ontology_record.json5.template` and fill in:
   - `existence.predicates` and `evidence`
   - `truth_maintenance.source_of_truth` and `revision_triggers`
   - `relationships` to related concepts
2. Merge the record into `GLOBAL_CONCEPT_VAULT.json5`.
3. Re-run validation with ontology checks enabled:
   ```bash
   python scripts/validate_project.py . --layers 1,2,7
   ```
4. Address ONTO findings (missing predicates, stale evidence, or orphaned relationships) before committing.

## Step 6 — Keep governance artifacts aligned
- Update `CHANGELOG.md` when you add features, templates, or governance rules.
- Refresh `README.md` sections that describe new workflows, validation flags, or template usage.
- Include rationale in commit messages to satisfy the Aletheia Principle (reduce concealment) and GVP (preserve coherence).

## Step 7 — Contributor workflow checklist
- [ ] Read the applicable `AGENTS.md` scope and project governance files.
- [ ] Create or update files using the closest template.
- [ ] Update `GLOBAL_CONCEPT_VAULT.json5` for new or revised concepts.
- [ ] Run `python scripts/validate_project.py .` (and add `--layers` for focus areas).
- [ ] Capture validation output if submitting a report.
- [ ] Document changes in `CHANGELOG.md` and `README.md` as needed.
- [ ] Commit with a clear message tying the change to concealment reduction and coherence gains.

## Next steps and deeper references
- Layer-by-layer specifications live under `mgfts/specs/`.
- Schema definitions for reports and vault entries are in `mgfts/meta_schemas/`.
- Governance rationale and axioms are documented in `mgfts/COMPLIANCE_CHARTER.md` and `mgfts/CONSTITUTIONAL_AXIOMS.md`.
