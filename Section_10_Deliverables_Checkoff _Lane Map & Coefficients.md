---

# **Section 10 — Deliverables Checkoff (Lane Map & Coefficients)**

This section is now treated as **DONE** once all items below are satisfied.  
No philosophy, no intent — just artifacts and verifications.

---

## **✅ 10.1 Lane-Map Header (REQUIRED)**

### **Deliverable**

A single header file, for example:

alm\_lane\_map.hpp

### **Must define (constants only, no logic):**

#### **Lane ranges**

constexpr int LANES\_TOTAL \= 32;

constexpr int HUE\_START  \= 0;  
constexpr int HUE\_COUNT  \= 12;

constexpr int TONE\_START \= 12;  
constexpr int TONE\_COUNT \= 12;

constexpr int AUX\_START  \= 24;  
constexpr int AUX\_COUNT  \= 8;

#### **Canonical pairing function (compile-time)**

constexpr int lane\_pair(int l) {  
    return (l \< 12\)  ? 11 \- l :  
           (l \< 24\)  ? 35 \- l :  
                       55 \- l;  
}

#### **Static assertions (hard gate)**

static\_assert(lane\_pair(lane\_pair(0)) \== 0);  
static\_assert(lane\_pair(5) \== 6);  
static\_assert(lane\_pair(12) \== 23);  
static\_assert(lane\_pair(24) \== 31);

### **Pass condition**

* Header compiles  
* No runtime logic  
* No alternative mappings  
* Used by **both scalar and AVX2 paths**

✅ **Checked off when header exists and is included everywhere**

---

## **✅ 10.2 Coefficient Table Layout (REQUIRED)**

### **Deliverable**

One header \+ one source file, e.g.:

alm\_coefficients.hpp  
alm\_coefficients.cpp

### **Must define exact tables:**

alignas(32) float alpha\[4\]\[32\];  
alignas(32) float beta \[4\]\[32\];  
alignas(32) float gamma\[4\]\[4\]\[32\];

No dynamic allocation.  
No resizing.  
No conditionals.

### **Pass condition**

* Arrays exist with exact dimensions  
* Alignment verified  
* Read-only after initialization

✅ **Checked off when these symbols exist and are linked**

---

## **✅ 10.3 Coefficient Initialization Function (REQUIRED)**

### **Deliverable**

One function, for example:

void init\_coefficients();

### **This function must:**

1. Fill coefficients **only** from:  
   * 12-entry hue base arrays  
   * 12-entry tone base arrays  
   * 8-entry aux arrays  
2. Enforce **pair symmetry mechanically**:

alpha\[k\]\[l\] \== alpha\[k\]\[lane\_pair(l)\]  
beta \[k\]\[l\] \== beta \[k\]\[lane\_pair(l)\]  
gamma\[k\]\[j\]\[l\] \== gamma\[k\]\[j\]\[lane\_pair(l)\]

3. Zero neighbor coupling on aux lanes:

for (l in AUX lanes) beta\[k\]\[l\] \= 0.0f;

4. Never branch on lane index  
   (looping is allowed; branching on data is not)

### **Pass condition**

* Unit test confirms symmetry for all k, j, l  
* No runtime mutation after init

✅ **Checked off when symmetry tests pass**

---

## **✅ 10.4 Auxiliary Lane Contract (REQUIRED)**

### **Deliverable**

A short markdown or header comment block stating **exact aux semantics**:

| Aux Pair | Role | Feedback Allowed |
| ----- | ----- | ----- |
| 24/31 | XH | Yes (algebraic only) |
| 25/30 | XT | Yes (algebraic only) |
| 26/29 | STAB | Yes (fixed coefficient only) |
| 27/28 | OBS | **NO** |

### **Hard rule**

**OBS lanes must not appear on the RHS of any update equation.**

### **Pass condition**

* Code review grep confirms OBS lanes are never read during updates  
* Scalar and AVX2 paths identical

✅ **Checked off when enforced by review \+ test**

---

## **✅ 10.5 Neighbor Participation Rules (REQUIRED)**

### **Deliverable**

Explicit rule (code \+ comment):

| Lane Group | Neighbor Averaging |
| ----- | ----- |
| Hue | YES |
| Tone | YES |
| Aux | NO (default) |

Implementation options:

* zero aux lanes before neighbor sum, or  
* exclude aux lanes from neighbor loop

### **Pass condition**

* Scalar reference and AVX2 give identical results  
* Changing aux lanes alone does not change neighbor influence

✅ **Checked off when scalar ↔ AVX2 equivalence test passes**

---

## **✅ 10.6 SIMD Load Block Discipline (REQUIRED)**

### **Deliverable**

Explicit AVX2 load mapping:

| Block | Lanes |
| ----- | ----- |
| 0 | 0–7 |
| 1 | 8–15 |
| 2 | 16–23 |
| 3 | 24–31 |

### **Pass condition**

* No partial loads  
* No cross-block shuffles  
* Same block layout everywhere

✅ **Checked off when kernel loads are uniform and reviewed**

---

## **✅ 10.7 Negative Tests (MANDATORY)**

### **Deliverable**

At least **three failure tests**:

1. **Pair-symmetry violation test**  
   * Manually break coefficient symmetry  
   * Test must fail  
2. **OBS feedback violation test**  
   * Force OBS lane into RHS  
   * Test must fail  
3. **Neighbor aux contamination test**  
   * Force aux lanes into neighbor average  
   * Test must fail

### **Pass condition**

* All three tests fail when they should  
* All pass when spec is obeyed

✅ **Checked off when regression harness enforces ontology**

---

## **✅ Section 10 Final Status**

| Item | Status |
| ----- | ----- |
| Lane map | ☐ / ☑ |
| Coefficient tables | ☐ / ☑ |
| Init logic | ☐ / ☑ |
| Aux semantics | ☐ / ☑ |
| Neighbor rules | ☐ / ☑ |
| AVX2 load discipline | ☐ / ☑ |
| Negative tests | ☐ / ☑ |

Once all boxes are checked:

**The lane map and coefficient system are frozen.**

Any future change becomes:

* a new version (v0.2)  
* explicitly justified  
* regression-gated

---

## **What This Unlocks Next**

With Section 10 locked, you can safely move to:

* **Pressure & decay equations**  
* **Jitter → focus transfer**  
* **Spiral observables**  
* **Cache-footprint proof**

No risk of semantic drift remains in the kernel substrate.

