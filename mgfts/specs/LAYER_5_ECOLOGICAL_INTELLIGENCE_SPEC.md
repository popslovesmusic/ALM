# MGFTS Layer 5 — Ecological Intelligence Specification

**Version:** 0.2.0  
**Status:** Draft (implementation-aligned)  
**Layer:** 5 (Ecological / Ecosystem)  
**Authority:** MGFTS Governance (Aletheia + GVP compliant)

---

## 1. Purpose

Layer 5 operationalizes **ecological intelligence** by detecting emergent patterns across projects, scoring ecosystem health, and surfacing warnings that preserve Aletheia (reduced concealment) and GVP (coherent evolution). This document defines:

- Pattern detection pipelines and data contracts
- Required data inputs and aggregation surfaces
- Ecosystem health metrics and thresholds
- Reporting expectations for Constitutional and Reporting engines

---

## 2. Pattern Detection Pipelines

### 2.1 Pipeline Stages
1. **Ingest**: Collect telemetry (commits, code churn, dependency diffs), governance artifacts (AGENTS, charters), and operational signals (incident logs, validation runs).
2. **Normalize**: Standardize inputs into canonical records:
   - `artifact`: path, layer, concept references
   - `event`: actor, timestamp, type (commit, validation, incident)
   - `metric`: name, value, source, layer_targets
3. **Detect**: Run pattern collectors:
   - **Governance drift detector**: flags missing/aged governance files.
   - **Pattern reuse detector**: measures template/config reuse vs. divergence.
   - **Ecological anomaly detector**: highlights sudden metric drops or concealment spikes.
4. **Score**: Compute ecosystem health (see §4) and attach Layer 5 scorecards to `MGFTS_REPORT.*`.
5. **Report**: Emit warnings with actionable remediation and GVP/Aletheia context.

### 2.2 Required Tool Contract
Pattern collectors MUST emit JSON with:

```json5
{
  tool: "{collector_name}",
  version: "{semver}",
  layer_targets: [5],
  metrics: {
    ecological_health: 0.0-1.0,
    concealment_surface: 0.0-1.0,
    coherence_trend: -1.0-1.0,
    pattern_reuse_ratio: 0.0-1.0
  },
  warnings: [ { code, message, path?, severity, layer: 5 } ],
  violations: [ ... optional, same shape as Layer 2 checks ... ]
}
```

---

## 3. Data Inputs

Layer 5 requires cross-layer and cross-project inputs:

- **Governance artifacts**: AGENTS.md, COMPLIANCE_CHARTER, PRESERVATION_PROTOCOL, Concept Vault deltas.
- **Template adoption signals**: files created from `mgfts/templates/*`, config usage vs. drift.
- **Operational telemetry**: validation reports, incident summaries, build logs.
- **Versioned metrics**: concealment/coherence time series, Layer 1–4 scores from `validate_project.py`.
- **Ecological registries**: pattern collector manifests (`mgfts/config/layer5_ecology.json5`).

Inputs MUST be timestamped and attributable (actor, source path) to satisfy Aletheia traceability.

---

## 4. Ecosystem Health Metrics

| Metric | Definition | Target / Threshold | Governance Link |
| --- | --- | --- | --- |
| `ecological_health` | Aggregate of pattern coverage, input completeness, and drift suppression | ≥ 0.75 (warning if < 0.6) | GVP (coherence) |
| `concealment_surface` | Residual concealment detected by ecological collectors | ≤ 0.35 | Aletheia |
| `pattern_reuse_ratio` | Reused templates/configs ÷ total eligible artifacts | ≥ 0.70 | Preservation Protocol |
| `signal_freshness_days` | Avg. age of ecological signals (governance + telemetry) | ≤ 30 | Aletheia (currency) |
| `cross_layer_alignment` | Correlation of Layer 2–4 scores with Layer 5 patterns | ≥ 0.65 | GVP |

Collectors SHOULD also track **ecological debt backlog** (count of unresolved warnings) and **incident resonance** (Layer 5 signals preceding incidents).

---

## 5. Validation & Reporting Hooks

- **Configuration**: `mgfts/config/layer5_ecology.json5` MUST declare pattern collectors, data inputs, and metric thresholds (see §6).
- **Constitutional Engine**: When Layer 5 is requested, `validate_project.py` (and downstream engines) MUST:
  - Verify ecological config presence and parseable JSON5.
  - Warn if required collectors are disabled or metrics lack thresholds.
  - Compute a provisional `ecological_health` score from coverage and freshness inputs.
- **Reporting**: Add Layer 5 block to `MGFTS_REPORT.md/json` with:
  - Active collectors and last run timestamps
  - Health metrics vs. thresholds
  - Aletheia/GVP-aligned remediation text for each warning

---

## 6. Configuration Schema (Reference)

Minimal expected structure for ecological configuration:

```json5
{
  $schema: "../meta_schemas/layer5_ecology.schema.json5", // optional stub
  version: "0.2.0",
  pattern_collectors: [
    { name: "governance_pattern", enabled: true, description: "Check governance drift" },
    { name: "code_churn_pattern", enabled: true, description: "Track churn vs. tests" },
    { name: "incident_resonance", enabled: false, description: "Link incidents to signals" }
  ],
  data_inputs: {
    governance: ["mgfts/AGENTS.md", "mgfts/COMPLIANCE_CHARTER.md"],
    telemetry: ["logs/validation", "logs/incidents"],
    templates: ["mgfts/templates/*"]
  },
  health_metrics: {
    ecological_health: { target: 0.8, warn_below: 0.6 },
    concealment_surface: { ceiling: 0.35 },
    pattern_reuse_ratio: { target: 0.75, warn_below: 0.6 },
    signal_freshness_days: { ceiling: 30 }
  },
  reporting: {
    emit_layer5_block: true,
    include_audit_trail: true,
    output_paths: ["docs/MGFTS_REPORT.md", "docs/MGFTS_REPORT.json"]
  }
}
```

---

## 7. Compliance Alignment

- **Aletheia Principle**: Surface aged or missing signals, stale governance artifacts, and implicit ecological debt.
- **GVP**: Optimize for coherent ecosystem evolution by preferring reusable patterns and synchronized cross-layer metrics.
- **Preservation Protocol**: Archive ecological findings and keep metric histories to avoid knowledge loss.

---

## 8. References
- `mgfts/specs/CONSTITUTIONAL_ENGINE_ARCHITECTURE.v0.1.md` (Layer 5 plug-in requirements)
- `mgfts/templates/config.json5.template` (ecology toggles)
- `mgfts/config/layer5_ecology.json5` (default configuration)
- Aletheia Principle (δ∫C(t) dt = 0) & GVP (δS[T] = 0)

