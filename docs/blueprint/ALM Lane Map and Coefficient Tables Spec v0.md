# ALM Lane Map and Coefficient Tables Spec v0.1

## 0\. Scope

This spec defines:

1. Exact lane assignment for a 32-lane register vector  
2. Canonical meaning of each lane group (Hue/Tone/Aux)  
3. Coefficient table layout and access rules  
4. Coefficient generation constraints (mod-12 periodicity, pairing symmetry)  
5. How auxiliary lanes participate in the kernel update (without becoming a control channel)

This spec does not define:

* neighborhood topology   
* N(c)  
* N(c)  
* ingest format  
* pressure mechanics beyond orthogonality

---

## 1\. Canonical Lane Map (L \= 32\)

Each register vector (for each of R,G,B,I and for each component fast/slow if stored separately) has exactly 32 lanes indexed   
ℓ=0..31  
ℓ=0..31.

### 1.1 Lane groups

Hue lanes (12):

* Hue lane indices:   
* ℓ∈\[0..11\]  
* ℓ∈\[0..11\]  
* Semantic: “chromatic hue relational basis”

Tone lanes (12):

* Tone lane indices:   
* ℓ∈\[12..23\]  
* ℓ∈\[12..23\]  
* Semantic: “chromatic tone relational basis”

Aux lanes (8):

* Aux lane indices:   
* ℓ∈\[24..31\]  
* ℓ∈\[24..31\]  
* Semantic: reserved for stabilizers / cross-terms / observables (defined below)

This matches the project’s declared 12+12+8 structure   
ALM\_Project\_Analysis  
.  
---

## 2\. Lane Pairing (SIMD Ontology Symmetry)

We require an involutive pairing function   
ℓˉ  
ℓ  
ˉ  
 that pairs lanes within each group.

### 2.1 Pairing rule (fixed)

For Hue lanes:

* If   
* ℓ∈\[0..11\]  
* ℓ∈\[0..11\]:  
* ℓˉ=11−ℓ  
* ℓ  
* ˉ  
* \=11−ℓ

For Tone lanes:

* If   
* ℓ∈\[12..23\]  
* ℓ∈\[12..23\]:  
* ℓˉ=35−ℓ(since 12↦23,  13↦22,… )  
* ℓ  
* ˉ  
* \=35−ℓ(since 12↦23,13↦22,…)

For Aux lanes:

* If   
* ℓ∈\[24..31\]  
* ℓ∈\[24..31\]:  
* ℓˉ=55−ℓ(since 24↦31,  25↦30,… )  
* ℓ  
* ˉ  
* \=55−ℓ(since 24↦31,25↦30,…)

This yields pairs:

* Hue: (0,11), (1,10), …, (5,6)  
* Tone: (12,23), …, (17,18)  
* Aux: (24,31), …, (27,28)

### 2.2 Pair-symmetry constraint on coefficients

For every coefficient vector   
q\[ℓ\]  
q\[ℓ\] used in the kernel (including   
α,β,Γ  
α,β,Γ multipliers):  
q\[ℓ\]=q\[ℓˉ\]  
q\[ℓ\]=q\[  
ℓ  
ˉ  
\]  
This is the mechanical condition that ensures symmetry can be preserved without branching.  
---

## 3\. Hue/Tone Indexing Semantics (mod-12 structure)

Hue basis index:  
h(ℓ)=ℓfor ℓ∈\[0..11\]  
h(ℓ)=ℓfor ℓ∈\[0..11\]  
Tone basis index:  
t(ℓ)=ℓ−12for ℓ∈\[12..23\]  
t(ℓ)=ℓ−12for ℓ∈\[12..23\]  
Both are interpreted mod 12 for coefficient generation rules:

* h∈Z12  
* h∈Z  
* 12  
* ​  
* t∈Z12  
* t∈Z  
* 12  
* ​

This is how 12×12 chromaticity becomes “parametric lane algebra”   
ALM\_Project\_Analysis  
.  
---

## 4\. Auxiliary Lanes (24..31) — Exact Roles

Aux lanes must not become “hidden control.” Their roles must be algebraic, continuous, and (ideally) derivable from payload rather than independently authored.  
We define 8 aux lanes as four paired concepts:

### 4.1 Aux lane definitions

| Aux lanes | Name | Intended content | Must be computed how |
| :---- | :---- | :---- | :---- |
| 24 & 31 | XH (cross-hue) | hue↔tone cross-term accumulator (low-order) | algebraic combination of hue & tone lanes |
| 25 & 30 | XT (cross-tone) | complementary cross-term accumulator | algebraic combination |
| 26 & 29 | STAB | stabilizer / damping basis | fixed coefficient scaling only (no branching) |
| 27 & 28 | OBS | observability basis (non-coupled) | write-only side-channel preferred; if in-lane, must not feed back |

Important enforcement:

* OBS lanes must never feed back into evolution terms. If you store OBS inside the 32-lane payload for convenience, you must guarantee the kernel ignores them in all future updates (except decay-to-zero). This is consistent with the “non-coupled observability” requirement   
  ALM\_Project\_Analysis  
* .

### 4.2 Cross-term computation (canonical, branchless)

Define (elementwise per lane) the following derived vectors per register/component (computed on the fly; not stored unless needed):  
Let:

* H  
* H \= hue subvector lanes \[0..11\]  
* T  
* T \= tone subvector lanes \[12..23\] remapped to \[0..11\] by subtracting 12

Define a cross correlation proxy (per register/component):  
CHT\[i\]=H\[i\]⋅T\[i\]  
C  
HT  
​  
\[i\]=H\[i\]⋅T\[i\]  
Then set aux lanes:

* XH pair (24/31) is proportional to   
* ∑iwiCHT\[i\]  
* ∑  
* i  
* ​  
* w  
* i  
* ​  
* C  
* HT  
* ​  
* \[i\] with fixed weights   
* wi  
* w  
* i  
* ​  
*  (e.g., uniform)  
* XT pair (25/30) is proportional to   
* ∑iwi′CHT\[(i+6) mod 12\]  
* ∑  
* i  
* ​  
* w  
* i  
* ′  
* ​  
* C  
* HT  
* ​  
* \[(i+6)mod12\] (phase-shifted coupling)  
* STAB pair (26/29) is a pure damping basis value (e.g.,   
* \+1  
* \+1 in both lanes multiplied by coefficient)  
* OBS pair (27/28) is reserved (preferably unused in payload; if used, write-only)

This yields cross-terms without inventing new semantic channels.  
---

## 5\. Coefficient Table Layout

We now specify the precise coefficient objects used by the kernel law.  
Recall from the Kernel Law Spec:

* αk\[ℓ\]  
* α  
* k  
* ​  
* \[ℓ\] self coupling  
* βk\[ℓ\]  
* β  
* k  
* ​  
* \[ℓ\] neighbor coupling  
* Γk←j\[ℓ\]  
* Γ  
* k←j  
* ​  
* \[ℓ\] cross-register mixing

### 5.1 Canonical coefficient table structure

Define:

* Registers are indexed:

* R=0,  G=1,  B=2,  I=3  
* R=0,G=1,B=2,I=3  
* Lanes are 0..31

Coefficients:

1. alpha\[4\]\[32\] (float32)  
2. beta\[4\]\[32\] (float32)  
3. gamma\[4\]\[4\]\[32\] (float32)

All coefficients are static tables in v0.1.

### 5.2 Alignment and AVX2 access

AVX2 is 256-bit wide, i.e., 8 float32 lanes per vector register.  
Therefore the canonical load blocks are:

* Block 0: lanes 0..7  
* Block 1: lanes 8..15  
* Block 2: lanes 16..23  
* Block 3: lanes 24..31

All coefficient arrays must be aligned to 32 bytes minimum (64 or 128 alignment acceptable). Your prior plan mentions alignas(128) for TensorCluster; coefficient arrays may use alignas(32) or higher.

### 5.3 Read-only guarantee

Coefficient tables are read-only at runtime. If you later allow adaptation, it must occur via separate staging and atomic swap of whole tables, never per-step mutation.  
---

## 6\. Coefficient Generation Rules (mod-12 periodicity and symmetry)

This section defines constraints (not a single numeric instance). It guarantees chromatic structure and preserves SIMD ontology.

### 6.1 Hue and Tone base coefficients

For hue lanes   
ℓ=0..11  
ℓ=0..11 with   
h=ℓ  
h=ℓ:  
αk\[ℓ\]=AkH\[h\]  
α  
k  
​  
\[ℓ\]=A  
k  
H  
​  
\[h\]  
βk\[ℓ\]=BkH\[h\]  
β  
k  
​  
\[ℓ\]=B  
k  
H  
​  
\[h\]  
For tone lanes   
ℓ=12..23  
ℓ=12..23 with   
t=ℓ−12  
t=ℓ−12:  
αk\[ℓ\]=AkT\[t\]  
α  
k  
​  
\[ℓ\]=A  
k  
T  
​  
\[t\]  
βk\[ℓ\]=BkT\[t\]  
β  
k  
​  
\[ℓ\]=B  
k  
T  
​  
\[t\]  
Where   
AkH,BkH,AkT,BkT  
A  
k  
H  
​  
,B  
k  
H  
​  
,A  
k  
T  
​  
,B  
k  
T  
​  
 are length-12 tables per register.

### 6.2 Aux coefficient rule

Aux lanes   
ℓ=24..31  
ℓ=24..31:  
αk\[ℓ\]=AkAux\[ℓ−24\]  
α  
k  
​  
\[ℓ\]=A  
k  
Aux  
​  
\[ℓ−24\]  
βk\[ℓ\]=0(default; prevents neighbor coupling via aux)  
β  
k  
​  
\[ℓ\]=0(default; prevents neighbor coupling via aux)  
Rationale: aux lanes should not participate in spatial neighbor mixing unless explicitly justified.

### 6.3 Pair symmetry constraint (mandatory)

For all coefficient vectors:  
q\[ℓ\]=q\[ℓˉ\]  
q\[ℓ\]=q\[  
ℓ  
ˉ  
\]  
This implies:

* AkH\[h\]=AkH\[11−h\]  
* A  
* k  
* H  
* ​  
* \[h\]=A  
* k  
* H  
* ​  
* \[11−h\]  
* AkT\[t\]=AkT\[11−t\]  
* A  
* k  
* T  
* ​  
* \[t\]=A  
* k  
* T  
* ​  
* \[11−t\]  
  (and same for   
* B  
* B, and for   
* Γ  
* Γ lane-wise)

This “even symmetry” is the simplest consistent choice.

### 6.4 Cross-register mixing coefficients 

### Γ

### Γ

For each target register   
k  
k and source register   
j  
j:  
Γk←j\[ℓ\]={Gk←jH\[h(ℓ)\]ℓ∈\[0..11\]Gk←jT\[t(ℓ)\]ℓ∈\[12..23\]Gk←jAux\[ℓ−24\]ℓ∈\[24..31\]  
Γ  
k←j  
​  
\[ℓ\]=  
⎩  
⎨  
⎧  
​  
G  
k←j  
H  
​  
\[h(ℓ)\]  
G  
k←j  
T  
​  
\[t(ℓ)\]  
G  
k←j  
Aux  
​  
\[ℓ−24\]  
​  
ℓ∈\[0..11\]  
ℓ∈\[12..23\]  
ℓ∈\[24..31\]  
​  
Where   
GH  
G  
H  
 and   
GT  
G  
T  
 are 12-entry tables and   
GAux  
G  
Aux  
 is 8-entry.  
Default structural constraint (recommended for v0.1):

* Allow only “near-diagonal” cross-coupling among R,G,B and limit I to stabilizing terms:  
  * I←I  
  * I←I strong  
  * R,G,B←I  
  * R,G,B←I weak damping or normalization  
  * I←R,G,B  
  * I←R,G,B weak aggregation

This keeps I as an inertial/persistence channel rather than a control channel.  
---

### 6.5 Canonical instantiated tables (v1.0)

This section fixes all numeric freedom by deriving concrete 32-lane tables from the constitutional base sequence in the **COEFFICIENT CANONICALIZATION CONTRACT** while enforcing pair symmetry.

**Definitions:**

* Base sequence (length 12): `S = [+1, 0, −1, 0, +1, 0, −1, 0, +1, 0, −1, 0]`.  
* Pair map for hue/tone lanes: pairs are (0,11), (1,10), (2,9), (3,8), (4,7), (5,6).  
* Pair-symmetric seed (length 6) from `S`: `P = [ +0.5, −0.5, −0.5, +0.5, +0.5, −0.5 ]` where each entry applies to its paired lanes.  
* Normalization constant to satisfy ‖·‖₂ ≤ 1 when expanded across hue and tone: `c = 1/√6 ≈ 0.40824829`.  
* Lane amplitude (after symmetry + normalization): `a = 0.5 * c ≈ 0.20412415`.

**Lane expansion helper:** For a pair-sign vector `[p0..p5]`, the 12-lane array is `[p0, p1, p2, p3, p4, p5, p5, p4, p3, p2, p1, p0] * a` to enforce `q[ℓ] = q[ℓˉ]`. The tone group (lanes 12–23) repeats the same 12 values. Aux lanes (24–31) are zero unless noted.

#### α (state interaction, per register)

* Pair-sign vector: `[+1, −1, −1, +1, +1, −1]`.  
* Lanes 0–11: `[+a, −a, −a, +a, +a, −a, −a, +a, +a, −a, −a, +a]`.  
* Lanes 12–23: same as lanes 0–11.  
* Lanes 24–31: all `0` (aux ingest/damping handled elsewhere).  
* Applies identically to R, G, B, I to preserve chromatic symmetry.

#### β (neighbor coupling, per register)

* Pair-sign vector: rotate the α pair vector by +1 in pair space → `[−1, −1, +1, +1, −1, +1]`.  
* Lanes 0–11: `[−a, −a, +a, +a, −a, +a, +a, −a, −a, +a, +a, −a]`.  
* Lanes 12–23: same as lanes 0–11.  
* Lanes 24–31: all `0` (aux neighbor coupling remains disabled by rule 6.2).  
* Applies identically to R, G, B, I.

#### Γ (cross-register mixing)

* Diagonal (k ← k): pair-sign vector = rotate `P` by +3 in pair space with sign inversion → `[−1, −1, +1, −1, +1, +1]`.  
  * Lanes 0–11: `[−a, −a, +a, −a, +a, +a, +a, +a, −a, +a, −a, −a]`.  
  * Lanes 12–23: same as lanes 0–11.  
  * Lanes 24–31: `0`.  
* Off-diagonal (k ← j, j ≠ k): use the same lane pattern scaled by 0.5 to keep ‖·‖₂ ≤ 1.  
  * Off-diagonal amplitude: `a_off = a / 2 ≈ 0.10206207`.  
  * Lanes 0–11: `[−a_off, −a_off, +a_off, −a_off, +a_off, +a_off, +a_off, +a_off, −a_off, +a_off, −a_off, −a_off]`.  
  * Lanes 12–23: same as lanes 0–11.  
  * Lanes 24–31: `0`.

**Checks (apply per vector):**

1. Pair symmetry: `q[ℓ] = q[ℓˉ]` holds by construction for all α, β, Γ vectors.  
2. Norm bounds: hue+tone expansion yields ‖α‖₂ = ‖β‖₂ ≈ 0.999, ‖Γ_diag‖₂ ≈ 0.999, ‖Γ_off‖₂ ≈ 0.499, all within the `≤ 1` constraint (aux zeros preserve these bounds).  
3. Rotation differentiation: α, β, and Γ use distinct pair-space rotations (0, +1, +3 with inversion), preserving the canonical family differentiation while satisfying lane pairing.

These tables are canonical and must be regenerated exactly; no runtime tuning or alternative scaling is permitted.

## 7\. How 12×12 Relational Algebra Appears Without 144 Lanes

You correctly want 12×12 structure but only have 32 lanes. The canonical method is:

* Hue lanes represent basis components in   
* Z12  
* Z  
* 12  
* ​  
* Tone lanes represent basis components in   
* Z12  
* Z  
* 12  
* ​  
* The 12×12 interaction is realized by coefficient-mediated cross-terms, not by enumerating 144 lanes.

The cross-terms (XH/XT) provide a low-order coupling summary of hue↔tone interactions without expanding dimensionality.  
This is consistent with “lane differentiation is exclusively coefficients”   
ALM\_Project\_Analysis  
.  
---

## 8\. Kernel Participation Rules (What gets included in updates)

To make the law spec deterministic, define:

### 8.1 Which lanes participate in neighbor averaging

* Hue lanes: YES  
* Tone lanes: YES  
* Aux lanes: NO (default), except STAB if explicitly enabled later

So for neighbor mean   
⟨k\\\*(c)⟩  
⟨k  
\\\*  
​  
(c)⟩, the aux lanes are treated as zero or ignored (implementation chooses but must match scalar reference).

### 8.2 Which lanes participate in residual evolution

* Hue lanes: YES  
* Tone lanes: YES  
* XH/XT: YES, but only via algebraic derived values  
* STAB: YES, but coefficient-controlled only  
* OBS: NO (must not feed back)
