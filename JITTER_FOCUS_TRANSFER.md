---

# **JITTER\_FOCUS\_TRANSFER.md**

**Version:** v0.1 (canonical)  
**Status:** REQUIRED / BLOCKING  
**Scope:** ALM / DASE ingest \+ kernel modulation

---

## **1\. Purpose**

This document defines **jitter as proprioceptive signal** and specifies the **only lawful mapping** from jitter to focus.

Jitter measures *instability of arrival*, not semantic content.  
Focus modulates *sensitivity*, not control.

If jitter is undefined, focus becomes arbitrary.  
If focus gates execution, ontology is violated.

---

## **2\. Definitions**

### **2.1 Ingest Stream**

Let the ingest stream be a sequence of frames indexed by (n):

* Frame size: (N) samples (default: 256\)  
* Nominal clock: (f\_0) (default: 215 kHz)  
* Frame arrival timestamps: (t\_n)

The engine **must not assume perfect periodicity**.

---

### **2.2 Jitter (Measured Quantity)**

Jitter is defined as **temporal deviation from nominal cadence**.

Define expected arrival time:  
\[  
\\hat{t}\_n \= t\_0 \+ \\frac{nN}{f\_0}  
\]

Define instantaneous timing error:  
\[  
\\delta\_n \= t\_n \- \\hat{t}\_n  
\]

---

## **3\. Jitter Metric (Canonical)**

Jitter is not a point value. It is a **local variance estimate**.

### **3.1 Windowed Jitter Energy**

Over a rolling window of (W) frames (default: (W=8)):

\[  
J(n) \= \\sqrt{  
\\frac{1}{W}  
\\sum\_{i=n-W+1}^{n}  
\\bigl(\\delta\_i \- \\bar{\\delta}\\bigr)^2  
}  
\]

Where:  
\[  
\\bar{\\delta} \= \\frac{1}{W}\\sum\_{i=n-W+1}^{n}\\delta\_i  
\]

Properties:

* Continuous  
* Non-negative  
* Insensitive to DC drift  
* Responds to burst instability

---

## **4\. Normalization**

To map jitter into a unitless domain, define a reference scale (J\_{\\text{ref}}):

\[  
\\tilde{J}(n) \= \\frac{J(n)}{J\_{\\text{ref}}}  
\]

Constraints:

* (J\_{\\text{ref}} \> 0\)  
* Chosen empirically (e.g., expected “stable” jitter)

No clamping is permitted here.

---

## **5\. Focus Definition**

Focus (F(n)) is a **continuous scalar** in (\[0,1\]) that modulates kernel sensitivity.

Interpretation:

* (F \\approx 0): relaxed, broad, low sensitivity  
* (F \\approx 1): tight, narrow, high sensitivity

Focus must:

* vary smoothly  
* never jump discontinuously  
* never encode decisions

---

## **6\. Jitter → Focus Transfer Function**

### **6.1 Canonical Transfer Function**

Define focus as a **monotone decreasing** function of normalized jitter:

\[  
F(n) \= \\frac{1}{1 \+ \\alpha,\\tilde{J}(n)^p}  
\]

Where:

* (\\alpha \> 0\) controls sensitivity  
* (p \\ge 1\) controls curvature (default (p=2))

Properties:

* Continuous  
* Smooth  
* No thresholds  
* No saturation by clamping  
* (F \\to 1\) as (J \\to 0\)  
* (F \\to 0\) asymptotically as (J \\to \\infty)

---

### **6.2 Forbidden Alternatives**

The following are **illegal**:

* Step functions  
* Piecewise mappings  
* Hard cutoffs  
* Boolean focus states  
* Hysteresis with discrete states

---

## **7\. How Focus May Be Used (Strictly Limited)**

Focus may modulate **rates only**.

### **7.1 Allowed Uses**

Focus may scale:

* neighbor coupling strength  
* decay constants  
* reinforcement gains

Example:  
\[  
\\beta\_k^{\\text{eff}} \= \\beta\_k \\cdot (1 \+ c,F)  
\]

\[  
\\lambda\_k^{\\text{eff}} \= \\lambda\_k \\cdot (1 \- d,F)  
\]

Where (c,d \\ge 0).

---

### **7.2 Explicitly Forbidden Uses**

Focus must **never**:

* enable/disable kernels  
* select registers  
* select lanes  
* select neighbors  
* alter topology  
* flip signs  
* act as a condition

---

## **8\. Focus Is Not Attention**

This distinction is critical.

* **Focus**: continuous sensitivity modulation  
* **Attention**: discrete selection or weighting of content

Attention mechanisms (hard or soft) are **not allowed** inside ALM.

Focus affects *how strongly* the same laws apply — never *what* applies.

---

## **9\. Interaction With Pressure**

Focus and pressure are orthogonal but may compound multiplicatively.

Allowed:  
\[  
\\lambda\_k^{\\text{eff}} \= \\lambda\_k \\cdot (1 \+ aP\_{\\text{ow}}) \\cdot (1 \- dF)  
\]

Forbidden:

* Focus overriding pressure  
* Pressure gating focus  
* Conditional interaction

---

## **10\. Observability**

Jitter and focus:

* may be logged  
* may be visualized  
* may be exposed to external agents

They must **not**:

* be written into payload lanes  
* be written into OBS lanes  
* feed back except through lawful scaling

---

## **11\. Required Tests (Acceptance Gates)**

The following tests are mandatory:

1. **Continuity test**  
   Small perturbations in frame timing → small perturbations in focus.  
2. **Monotonicity test**  
   Increasing jitter → non-increasing focus.  
3. **Zero-jitter limit test**  
   As (J \\to 0), (F \\to 1).  
4. **Scalar ↔ AVX2 equivalence**  
   Focus-modulated kernel outputs must match.  
5. **No gating test**  
   Instrumentation proves focus never controls branching or masks.

---

## **12\. Summary (Non-Negotiable)**

* Jitter is **measured**, not inferred  
* Focus is **computed**, not decided  
* Mapping is **continuous**, not discrete  
* Focus modulates **rates**, not structure  
* Focus is **not attention**  
* Focus cannot encode intent

**If jitter ever “decides where to look,” the system is broken.**

---

## **13\. Status After This Document**

With this document complete:

* ❌ Undefined jitter → **RESOLVED**  
* ❌ Focus ambiguity → **RESOLVED**  
* ❌ Hidden attention mechanisms → **BLOCKED**  
* ❌ Gating via instability → **FORBIDDEN**

This closes **Item 2** from the report.

---

