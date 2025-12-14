# First Project Walkthrough

Use this playbook to take a new MGFTS-based project from empty repository to a validated contribution. The steps emphasize how to keep structural, governance, and ontological artifacts in sync.

## 1) Initialize the project
```bash
python scripts/create_new_project.py aurora-monitor
cd aurora-monitor
```
What you should see:
- `src/`, `tests/`, and `docs/` directories populated from templates.
- `mgfts/` copied with governance anchors, templates, and schemas.
- A git repository initialized with an initial commit (if you keep the defaults).

## 2) Add a feature from templates
1. Create a module from the Python template:
   ```bash
   cp mgfts/templates/python_module.py.template src/telemetry.py
   ```
2. Replace placeholders inside `src/telemetry.py` (description, author, version, class/function names).
3. Add a matching test file from `python_test.py.template` under `tests/`.
4. Note any new concepts (e.g., "Telemetry Stream" or "Sampling Window").

## 3) Register ontology information
For each new concept:
1. Copy the ontology template:
   ```bash
   cp mgfts/templates/ontology_record.json5.template mgfts/telemetry_stream.onto.json5
   ```
2. Fill in:
   - `existence.predicates` describing how the concept exists in the system
   - `truth_maintenance.source_of_truth` referencing evidence (docs/specs/tests)
   - `relationships` linking to existing concepts (e.g., Observation, Signal)
3. Merge the completed block into `mgfts/GLOBAL_CONCEPT_VAULT.json5`.
4. Delete the temporary `.onto.json5` helper file after merging.

## 4) Run focused validations
- Structural and governance checks:
  ```bash
  python scripts/validate_project.py . --layers 1,2
  ```
- Include ontology coverage and ONTO codes:
  ```bash
  python scripts/validate_project.py . --layers 1,2,7 --severity high --output mgfts_report.json
  ```
- Inspect `mgfts_report.json` against `mgfts/meta_schemas/mgfts_report.schema.json5` if you need machine-readable results.

## 5) Document and commit
1. Update `CHANGELOG.md` with a brief entry for the new feature and ontology additions.
2. Add a short note to `README.md` or project docs describing how to use the new module.
3. Confirm the checklist:
   - [ ] Templates were used (no custom drift)
   - [ ] Ontology predicates and evidence added
   - [ ] Validation passed (or warnings triaged)
4. Commit with a message that references concealment reduction (Aletheia) and coherence improvements (GVP).

## 6) Common troubleshooting signals
- **Missing predicates (ONTO-001)**: Add `existence.predicates` and `truth_maintenance` fields for the concept in the vault.
- **Orphaned relationships (ONTO-004)**: Ensure related concepts exist and include reciprocal links where appropriate.
- **Template drift warnings**: Re-copy templates and re-apply minimal edits to stay aligned with meta-schemas.

By following this walkthrough, you create auditable links among templates, code, governance files, and ontological evidence while keeping MGFTS validation green.
