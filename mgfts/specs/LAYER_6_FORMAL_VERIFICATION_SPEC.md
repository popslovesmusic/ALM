# Layer 6 Formal Verification Specification

## 0. Purpose

This specification defines how MGFTS-enabled projects implement **Layer 6 (Formal Verification)**. It enumerates supported proof systems and tooling, identifies expected verification targets, and prescribes a reporting schema so validation and reporting engines can score and surface formal assurance status.

---

## 1. Supported Proof Systems & Tooling

- **SMT/Solvers**: Z3, CVC5; accepted artifact extensions: `.smt2`, `.smt`, `.smtlib`.
- **Interactive Theorem Provers**: Coq (`.v`), Isabelle (`.thy`), Lean (`.lean`).
- **Model Checkers**: TLA+ (`.tla` / `.cfg`), Alloy (`.als`), NuSMV (`.smv`).
- **Refinement / Typed Proofs**: Dafny (`.dfy`), F* (`.fst`), Liquid Haskell (`.lh`).
- **Runtime Verification / Contracts**: OPA/OPL contract specs, property files (`.l6spec`, `.contracts`).

### Tool Registration (mgfts/config/layer6_verification.json5)

Each tool entry SHOULD include:

```json5
{
  name: "z3",
  type: "smt_solver",        // smt_solver | theorem_prover | model_checker | refinement
  enabled: true,
  artifact_patterns: ["*.smt2"],
  targets: ["safety"],        // e.g., safety, liveness, invariants
  command: "z3 -smt2 {artifact}",
  optional: true               // only run when --verify-artifacts is passed
}
```

- Tool entries MUST declare the artifact patterns they can check.
- Optional tools MUST NOT be executed unless the validator is invoked with `--verify-artifacts`.

---

## 2. Verification Targets

Projects SHOULD enumerate verification targets in `mgfts/config/layer6_verification.json5` under `targets`:

- **Safety invariants** (e.g., "transactions are conserved").
- **Liveness properties** (e.g., "requests eventually receive responses").
- **Refinement relations** (e.g., "implementation refines spec"), referencing `spec_path`.
- **Interface contracts** (e.g., pre/post-conditions) mapped to code modules.
- **Temporal properties** tied to state machines or protocols.

Each target entry SHOULD include:

```json5
{
  name: "payment_invariant",
  type: "safety",
  artifacts: ["verification/payments/payment_invariant.smt2"],
  spec_path: "docs/specs/Payments.md",
  status: "pending" // pending | proved | disproved | partial
}
```

Targets without associated artifacts MUST be flagged as concealment risks (missing proofs).

---

## 3. Proof Artifact Locations

- Default search roots: `/verification/`, `/proofs/`, and any `proof_dirs` listed in configuration.
- Accepted artifact patterns (extensible): `*.smt2`, `*.v`, `*.lean`, `*.tla`, `*.cfg`, `*.als`, `*.smv`, `*.dfy`, `*.fst`, `*.lh`, `*.l6spec`, `*.contracts`.
- Optional reports: `verification/report/*.json` or `.md` summarizing proof outcomes.

Artifacts SHOULD be grouped by target (e.g., `verification/<target_name>/artifact.ext`) and accompanied by a stub derived from `mgfts/templates/proof_obligation.md.template` when proofs are pending.

---

## 4. Reporting Schema (Layer 6)

Layer 6 data MUST flow into `MGFTS_REPORT.json` and `MGFTS_REPORT.md` through the following structure:

```json5
layer6: {
  proof_artifacts_found: 0,
  proof_directories_scanned: [],
  tools_registered: [],
  targets: [
    {
      name: "string",
      type: "safety|liveness|refinement|contract",
      status: "pending|proved|disproved|partial",
      artifacts: ["paths..."],
      tool: "optional tool hint"
    }
  ],
  coverage_score: 0.0,      // artifacts + target coverage
  validation_checks: []      // optional check outputs or skipped reasons
}
```

- `coverage_score` SHOULD reward presence of configuration, targets, and artifacts (0.0–1.0).
- `validation_checks` SHOULD record whether optional tool executions were requested or skipped.
- Missing config or zero artifacts MUST reduce Layer 6 scores and be surfaced as violations.

---

## 5. Validator Expectations

- The validator MUST scan configured proof directories and recognized patterns.
- When `--verify-artifacts` is provided, the validator SHOULD run lightweight checks (file exists & non-empty) and record results under `validation_checks`.
- Layer 6 score aggregation MUST be included in overall scoring and layer breakdowns.
- Violations MUST include guidance:
  - `FORM-001`: Missing `mgfts/config/layer6_verification.json5`.
  - `FORM-002`: No proof artifacts found in configured directories.
  - `FORM-003`: Targets declared without artifacts.
  - `FORM-004`: Verification tool registry empty or disabled.
  - `FORM-005`: Optional checks requested but artifacts failed basic sanity (empty or unreadable).
  - `FORM-006`: Layer 6 configuration invalid or unreadable.

---

## 6. Deliverables

- Configuration template: `mgfts/templates/verification_config.json5.template`.
- Proof obligation template: `mgfts/templates/proof_obligation.md.template`.
- Registered defaults: `mgfts/config/layer6_verification.json5` seeded with common tools, targets, and patterns.

---

**Version:** 1.0.0  
**Status:** Specification  
**Last Updated:** 2025-02-01
