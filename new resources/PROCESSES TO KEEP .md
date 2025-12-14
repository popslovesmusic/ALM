## PROCESSES TO KEEP (INCLUSIVE DRAFT)

### Signal Generation & Perturbation

* Image → Audio Sonification  
  Translates spatial image structure into time-ordered audio signals using controlled scanning and mapping strategies.  
* Parameterized Audio Synthesis  
  Generates deterministic audio waveforms from bounded frequency, amplitude, phase, and envelope parameters.  
* External Frequency Perturbation  
  Injects secondary oscillatory signals to probe system sensitivity and response dynamics.

---

### Representation & Feature Extraction

* FFT Spectral Extraction  
  Converts time-domain audio signals into stable frequency-domain representations for comparison and analysis.  
* Harmonic Peak Detection  
  Identifies dominant frequencies and harmonic relationships within FFT spectra.  
* Harmonic Tokenization  
  Discretizes spectral structure into symbolic tokens derived from invariant harmonic ratios.

---

### Vocabulary & Manifold Formation

* Latent Vocabulary Space Construction  
  Accumulates token distributions into a continuous representational space suitable for clustering and distance evaluation.  
* Token Distance Measurement  
  Computes similarity and divergence between representations using token overlap, ratios, or dispersion metrics.  
* Vocabulary Stability Testing  
  Evaluates whether generated token patterns persist across repeated identical inputs.

---

### Baselines & Evaluation

* Null Input Baseline Generation  
  Establishes reference outputs using low-structure or noise inputs to define “no vocabulary” behavior.  
* Repeatability Testing  
  Verifies deterministic output consistency under identical input and configuration conditions.  
* Separability Testing  
  Measures whether structurally different inputs produce distinguishable representations.

---

### Diagnostics & Integrity Monitoring

* Internal State Health Monitoring (CSI-like)  
  Tracks internal dynamics to detect instability, divergence, or collapse independently of task output.  
* Spectral Stability Metrics  
  Quantifies variance, drift, and decay in frequency/token space over time.  
* Damping & Stabilization Feedback  
  Applies corrective constraints when instability thresholds are exceeded.

---

### Memory & History

* State Persistence / Hysteresis  
  Maintains influence of prior internal states on future system behavior.  
* Interaction Work Logging (CPWP)  
  Records cumulative parameter changes as measures of applied effort and system bias.  
* Session Recording & Replay  
  Captures full system state evolution for deterministic playback and audit.

---

### Control & Biasing

* Parameter Bias Injection  
  Adjusts system behavior via bounded priors or attractor shaping without semantic labeling.  
* Constraint Enforcement  
  Prevents invalid or unsafe states through predefined numeric and structural limits.

---

### Infrastructure & Execution

* Deterministic Engine Execution  
  Ensures reproducible numerical behavior via fixed seeds, precision rules, and bounded operations.  
* Modular Signal Chain Orchestration  
  Composes signal generation, transformation, and analysis stages into explicit, inspectable pipelines.  
* Configuration Loading & Normalization  
  Applies standardized configuration schemas to ensure consistent runtime behavior.

---

### Validation & Governance

* Error Taxonomy & Propagation  
  Treats internal failures as first-class events with structured categorization and traceability.  
* Audit Logging & Provenance Tracking  
  Records all data, parameter, and execution context required for external review.  
* Domain Constraint Compliance (Medical-grade)  
  Enforces determinism, auditability, and safety requirements imposed by high-stakes application domains.

---

### Visualization & Interpretability

* Live Spectrum & Waveform Visualization  
  Provides real-time observation of internal signal structure without modifying behavior.  
* Decoded Field Visualization  
  Maps internal representations into human-interpretable visual forms for debugging and analysis.

---

### Meta-Processes (Keep but Flag)

* Conceptual Framing & Narrative Artifacts  
  Preserve as historical context and intuition-building material, not as architectural drivers.  
* Prototype UI Variants  
  Retain as exploration tools and reference implementations, not as core system logic.

