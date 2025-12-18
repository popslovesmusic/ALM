# Document Organization Report

Here is the organization of your project documents, categorized into Canonical, Foundational Prime References, Legacy, and Related References, ordered by importance or use within their categories:

---

### **A. Canonical Documents (Governing the ALM Project Implementation)**

These documents represent the current, actionable blueprint and its direct supporting specifications. They are the authoritative source for project governance and implementation details.

1.  **Primary Blueprint (Highest Authority & Central Hub):**
    *   `A Relational Semantic Substrate Bluprint.md`
        *   *Role:* This document explicitly establishes the overall governance rules, core philosophy, high-level architecture, roadmap, and integrates/references all other canonical specifications. It is the single source of truth for the project's direction.

2.  **Core Technical Specifications (Foundational for Implementation Detail):**
    *   `Relational Kernel Law Spec v0.md`
        *   *Role:* Provides the exact mathematical and algorithmic update laws for the ALM kernel, detailing the physics of semantic evolution.
    *   `AVX2_KERNEL_RULES.md`
        *   *Role:* Mandates strict coding rules, allowed/forbidden intrinsics, branchless patterns, and performance invariants for the AVX2 implementation, enforcing SIMD as ontology.
    *   `CACHE_RESIDENCY_PROOF.md`
        *   *Role:* Offers rigorous proof of L2 cache residency and defines memory footprint constraints, ensuring deterministic, cache-bounded evolution.
    *   `TIME_STENCIL_MECHANICS.md` (and `Time Stencil Mechanics.md`)
        *   *Role:* Defines the precise temporal structure, rotation mechanics, read/write permissions for the 4-slice time stencil, and future-bias semantics. (Note: These two files appear to be identical duplicates. The uppercase version was read last).
    *   `PRESSURE_AND_DECAY_LAWS.md`
        *   *Role:* Specifies the lawful modulation of rates by pressure, including mathematical decay laws, and details how pressure influences but does not control the system.
    *   `PRESSURE_SIGNAL_ORTHOGONALITY.md`
        *   *Role:* Enforces the strict separation and non-interaction between pressure and signal channels, preventing hidden control or goal-directedness.
    *   `JITTER_FOCUS_TRANSFER.md`
        *   *Role:* Defines jitter measurement, the canonical transfer function to focus, and the strict, lawful uses of focus in modulating sensitivity.
    *   `ALM Lane Map and Coefficient Tables Spec v0.md`
        *   *Role:* Details exact lane assignments, coefficient table layout, generation rules, pairing symmetry, and auxiliary lane roles.
    *   `SPIRAL_OBSERVABLES.md`
        *   *Role:* Defines how emergent spiral behavior is measured as read-only diagnostics (angular, radial components) without any feedback into the kernel.

3.  **Implementation & Verification Support (Directly Enabling Coding and Testing):**
    *   `INVARIANT_REGRESSION_TESTS.md`
        *   *Role:* Specifies the non-negotiable regression test suite to enforce ALM's ontology, invariants, and philosophical commitments.
    *   `Section_10_Deliverables_Checkoff _Lane Map & Coefficients.md`
        *   *Role:* Provides a practical, actionable checklist for verifying the implementation of the lane map and coefficient system deliverables.
    *   `scalar ↔ AVX2 equivalence test harness .md`
        *   *Role:* Offers concrete code for a test harness to verify the numerical equivalence between scalar and AVX2 implementations, crucial for determinism.

---

### **B. Foundational Prime References (Underlying Theoretical Basis)**

These documents provide the core philosophical and theoretical groundwork upon which the Canonical Blueprint (Section A) is built, as indicated by their placement in `source material/prime references`. They offer the deep *why* behind ALM's design.

*   `source material/prime references/Foundational Background Theory.md`
        *   *Role:* Outlines the core motivation, insights, and conceptual commitments of ALM.
*   `source material/prime references/Foundational Background Theory Report.md`
        *   *Role:* Likely a summary or analysis of the foundational theory.
*   `source material/prime references/Invariants of SIMD-Based Being.md`
        *   *Role:* Explores the philosophical implications of SIMD as an ontological principle.
*   `source material/prime references/Intended Usage of the DASE Engine.md`
        *   *Role:* Provides context on how the DASE engine is intended to be used within the broader system.
*   `source material/prime references/incompatible with SIMD as ontology.md`
        *   *Role:* Highlights concepts or approaches that directly conflict with ALM's core SIMD ontology.

---

### **C. Legacy Documents (Historical, Superseded, or Internal Reports)**

These documents are either historical artifacts, have been superseded by more current and authoritative specifications (especially the Canonical Documents), or are internal analysis reports generated during our process. They no longer hold governing authority for the project.

*   `ALM_Project_Analysis.md` (Superseded by 'A Relational Semantic Substrate Bluprint.md', content integrated and refined)
*   `ALM_Definition_Gaps_Report.md` (Internal analysis report of philosophical/theoretical gaps)
*   `ALM_Technical_Definition_Gaps_Report.md` (Internal analysis report of technical/code gaps)
*   `Blueprint_Assessment_Report.md` (Internal assessment of blueprint's completeness)
*   `source material/legacy/project-plan.md` (The original high-level project plan, superseded)
*   `source material/legacy/ALM bullet point.md` (Earlier, more detailed high-level plan)
*   `source material/legacy/The Spiral Concept in ALM.md` (Core theoretical discussion on spirals, principles now integrated into Canonical Blueprint)
*   `source material/legacy/10x10_Substrate_12x12_Relational_Model.md` (Earlier conceptual clarification on spatial vs. relational scales, integrated)
*   `source material/legacy/What Is Already Strong and Should Not Be Changed.md` (Feedback document, its content and refinements are integrated into Canonical Blueprint)
*   `source material/legacy/SIMD as Ontology.md` (Earlier conceptual document, its principles are now central to Canonical Blueprint and AVX2 rules)
*   `source material/legacy/ALM_Plan_Readiness_Report.md` (Likely an older planning document or report, superseded)
*   `source material/legacy/dir.py` (A utility script for directory listing, not project documentation itself)
*   `.gitignore` (Standard version control configuration file)

---

### **D. Related References (External Project Context)**

These documents describe other related projects, systems, or broader contextual information. They are valuable for understanding the ecosystem and potential applications but are not direct ALM specifications or foundational theory.

*   `source material/related references/DASE_OPERATIONS_MANUAL.md` (Operational manual for the DASE engine)
*   `source material/related references/chrocog.txt` (Analysis of Chromatic-Cognition/Soundlab project)
*   `source material/related references/Chromatic Cognition System.txt` (Recursive analysis of Chromatic Cognition System)
*   `source material/related references/chromatic-cognition-narrative.txt` (Narrative synthesis of Chromatic-Cognition)
*   `source material/related references/chromatic-cognition.txt` (Project analysis of Chromatic-Cognition)
*   `source material/related references/Chromatic-Cognition2.txt` (Deep-dive report on Chromatic-Cognition2)
*   `source material/related references/Chromatic-Cognitions.txt` (Project analysis of Chromatic-Cognition, another variant)
*   `source material/related references/core.txt` (Chromatic Cognition Core text/documentation synthesis)
*   `source material/related references/Medical Image Analysis.txt` (Report on Medical Image Analysis Repository)
