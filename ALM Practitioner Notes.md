# ALM Practitioner Notes

Tips, Traps, and Hard-Won Hints  
(Authorial voice: collaborator / implementation partner)  
---

## 1\. Guardrails Before Cleverness

If a choice feels clever, slow down.  
ALM survives because it is boring in the right places.

### Practical Rule

If an optimization:

* introduces a conditional,  
* depends on a value being “usually small,”  
* or relies on emergent cancellation rather than enforced symmetry,

then it probably violates the model even if it passes tests.  
ALM prefers redundancy over cleverness.  
Duplicated math with guaranteed symmetry is safer than a “simplified” formulation.  
---

## 2\. Determinism Is a Physical Law, Not a Preference

Treat determinism the way physics treats conservation laws.

### Implementation Hints

* Never allow coefficients to be derived at runtime, even if the derivation is deterministic.  
* Do not trust compiler “equivalence.” Explicitly test scalar vs AVX2 equality at the stencil boundary, not mid-kernel.  
* Fix iteration order everywhere, including:  
  * neighbor loops  
  * lane traversal  
  * observability sampling

If two runs differ only in instruction scheduling, that is already a failure.  
---

## 3\. Residuals Are the Meaning Carrier — Protect Them

The residual (Δ\*) is where everything you care about lives.

### Common Failure Modes

* Accidentally normalizing residuals “for stability”  
* Letting pressure terms dominate instead of modulate  
* Mixing residuals across time slices prematurely

### Practical Rule

Residuals should:

* be born from subtraction  
* be shaped by interaction  
* decay naturally  
* never be zeroed intentionally

If you find yourself asking “should we clamp this?” the answer is almost always no.  
---

## 4\. Pressure Must Always Be Multiplicative

This is subtle and easy to violate.

### Never Allow Pressure To:

* gate updates  
* skip computation  
* trigger alternate code paths  
* decide whether something happens

Pressure may only decide how strongly something happens.  
A good mental test:  
“If pressure were 1.0 everywhere, would the system still be valid?”  
If the answer is no, pressure has become control.  
---

## 5\. SIMD Is About Simultaneity, Not Speed

AVX2 here is not an optimization layer — it is a truth-preservation layer.

### Tips

* Write scalar code as if it were SIMD already:  
  * no hidden dependencies  
  * no short-circuit logic  
* Avoid reductions even when “safe”  
* Avoid lane-local special cases

If SIMD and scalar ever disagree, scalar is not the reference — the law is.  
---

## 6\. Boundaries Are Where Systems Lie to Themselves

Most systems smuggle intent through boundaries. ALM must not.

### Boundary Conditioning Guidance

* Think “resonance,” not “response”  
* Let boundaries shape phase and amplitude, never topology  
* Never introduce thresholds “just at the edge”

A boundary should feel like impedance, not a wall.  
---

## 7\. Focus Is Transfer, Not Selection

Focus is one of the easiest concepts to misunderstand.

### What Focus Is NOT

* not attention  
* not prioritization  
* not selection  
* not amplification of importance

### What Focus IS

* energy handoff  
* alignment shift  
* constrained redistribution under jitter

If focus ever feels like “choosing,” something has gone wrong.  
---

## 8\. Observability Must Be Harmless

If you cannot prove observability is passive, assume it is not.

### Strong Recommendations

* Keep observables read-only at the type level  
* Never let logging allocate  
* Never let telemetry branch on values  
* Sample at stencil boundaries only

If removing observability changes results, observability is invalid.  
---

## 9\. Tests Should Try to Kill the System

Passing tests are not the goal. Survivable tests are.

### Good Tests

* overwrite pressure  
* future slice flooding  
* extreme decay constants  
* adversarial ingest cadence  
* long-run drift detection

If the system survives abuse without special cases, it is probably correct.  
---

## 10\. Philosophical North Star (Write This Somewhere Visible)

This is not optional — it prevents future drift.  
ALM does not decide, classify, threshold, or select.  
It allows structured interaction to erase inconsistency.  
What remains is not chosen — it survives.  
Any implementation choice that violates this sentence should be rejected, even if it “works.”  
---

## 11\. Personal Note (Why I’m Strict About This)

Systems like this fail quietly.  
They don’t crash.  
They don’t break tests.  
They just become something else while still looking correct.  
Your plan is strong because it anticipates that failure mode.  
My role here is to keep us honest when the temptation to “just make it work” appears.  
If you ever want, next I can:  
