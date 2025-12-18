---

# **INGEST_LANE_BINDING.md**

**Version:** v1.0 (canonical)  
**Status:** REQUIRED / BLOCKING  
**Scope:** ALM ingest → payload binding

---

## **1. Purpose**

Define the **only lawful ingest lane binding** so external signals enter the kernel without inventing topology, control, or lane semantics. This closes the ingest lane ambiguity noted in the readiness report.

---

## **2. Ingest Frame Definition (Canonical)**

* Frame rate and size follow `JITTER_FOCUS_TRANSFER.md`: 256 samples per frame at nominal 215 kHz.  
* Each frame is mapped to **12 ingest lanes** to match the mod-12 lane ontology and the fixed neighbor degree \(|N(c)| = 12\).  
* Frames carry **signal only** (no control, no timing metadata, no pressure fields).

---

## **3. Lane Targets (Registers and Indices)**

* **Register:** `I` (ingest/persistence register) is the sole ingest target.  
* **Lanes:** hue lanes \(\ell = 0..11\) in `I` are ingest lanes.  
* **Mirror rule:** tone lanes \(\ell = 12..23\) receive the same values to preserve hue/tone symmetry; aux lanes \(\ell = 24..31\) are set to zero for ingest.

This keeps ingest orthogonal to pressure and avoids implicit control channels in R/G/B payload lanes.

---

## **4. Canonical Mapping Algorithm**

For an ingest frame `x[0..255]`:

1. **Bucket by mod-12:** For each sample index `i`, accumulate into bucket `b = i mod 12`.  
   * `bucket[b].sum += x[i]`  
   * `bucket[b].count += 1`
2. **Average per bucket:** `v[b] = bucket[b].sum / bucket[b].count` for `b = 0..11`.  
   (With a 256-sample frame, every bucket has 21 or 22 samples, so no weighting variation exists.)
3. **Write to payload:**
   * `I[NOW][b] = v[b]` for lanes `b = 0..11` (hue).  
   * `I[NOW][12 + b] = v[b]` for lanes `b = 0..11` (tone mirror).  
   * `I[NOW][24..31] = 0` (aux lanes cleared for ingest).
4. **Pair symmetry:** Because lanes `b` and `\bar{b}` share the same averaged value, the ingest write preserves the required pair symmetry \(q[\ell] = q[\bar{\ell}]\).

Properties:

* **Deterministic:** No randomness, no topology dependence, no learned parameters.  
* **Branchless:** Same operations for every frame; no gating on values or timestamps.  
* **Orthogonal to pressure:** Pressure channels remain external scalars; ingest never writes pressure.

---

## **5. Phase and Time-Stencil Interaction**

* Ingest writes land in the **NOW** slice before kernel update.  
* Rotation semantics follow `TIME_STENCIL_MECHANICS.md`; ingest does **not** alter slice order or decay.  
* Jitter handling remains as defined in `JITTER_FOCUS_TRANSFER.md`; timing deviations do not change lane mapping.

---

## **6. Validation Checks (Acceptance Gates)**

1. **Symmetry check:** After ingest, verify `I[NOW][ℓ] == I[NOW][ℓˉ]` for all hue/tone lanes.  
2. **Orthogonality check:** Confirm R/G/B lanes and all aux lanes remain unchanged by ingest.  
3. **Determinism check:** Two identical frames yield bit-identical ingest writes, independent of arrival jitter within allowed bounds.

---

## **7. Status After This Document**

* ❌ Ingest lane ambiguity → **RESOLVED**  
* ❌ Implicit control via ingest lanes → **BLOCKED**

---
