# Relational Kernel Law Spec v0.1

## 0\. Purpose

Define the exact update law for the per-cell registers:  
X≡(R,G,B,I)  
X≡(R,G,B,I)  
where each register is a SIMD vector of lanes (e.g., 32 lanes per register), and updates are:

* branchless  
* symmetry-preserving  
* residual-based  
* dual-frequency (fast angular \+ slow radial)  
* pressure-governed, with pressure not stored in payload lanes

---

## 1\. Notation

### 1.1 Indices

* Cell index:   
* c  
* c (in a 10×10 grid)  
* Neighbor set:   
* N(c)  
* N(c) (implementation chooses topology; spec supports any fixed set)  
* Register index:   
* k∈{R,G,B,I}  
* k∈{R,G,B,I}  
* Lane index:   
* ℓ∈{0,…,L−1}  
* ℓ∈{0,…,L−1} with   
* L=32  
* L=32 typical  
* Phase pair index:   
* p(ℓ)  
* p(ℓ) identifies lane pairing; each lane has partner   
* ℓˉ  
* ℓ  
* ˉ

### 1.2 State tensors (per cell)

For each register   
k  
k, define two coupled components:

* fast (angular) state:   
* kf(c)∈RL  
* k  
* f  
* ​  
* (c)∈R  
* L  
* slow (radial/persistence) state:   
* ks(c)∈RL  
* k  
* s  
* ​  
* (c)∈R  
* L

The payload lanes are the concatenation of these across registers (implementation may store as separate arrays or packed, but semantics must remain).

### 1.3 Pressures (orthogonal inputs)

Pressure fields are scalars or vectors outside payload lanes:

* overwrite pressure:   
* Pow(c)  
* P  
* ow  
* ​  
* (c)  
* bandwidth pressure:   
* Pbw(c)  
* P  
* bw  
* ​  
* (c)  
* focus intensity:   
* F(c)∈\[0,1\]  
* F(c)∈\[0,1\]

These may be scalars or per-lane vectors, but must not be stored inside   
R,G,B,I  
R,G,B,I lanes.  
---

## 2\. Coefficients (12×12 chromaticity as lane algebra)

All lane differentiation is parametric via coefficient vectors.

### 2.1 Lane coefficient vectors

For each register   
k  
k, define coefficient vectors:

* self-coupling:   
* αk∈RL  
* α  
* k  
* ​  
* ∈R  
* L  
* neighbor-coupling:   
* βk∈RL  
* β  
* k  
* ​  
* ∈R  
* L  
* cross-register mixing coefficients:   
* Γ∈R4×4×L  
* Γ∈R  
* 4×4×L

where   
Γk←j\[ℓ\]  
Γ  
k←j  
​  
\[ℓ\] multiplies register   
j  
j’s contribution into register   
k  
k, lane   
ℓ  
ℓ.  
The “12 hue / 12 tone” structure is encoded by periodic structure in   
α,β,Γ  
α,β,Γ across lanes (e.g., mod-12 groups). No branching is permitted.  
---

## 3\. Neighborhood aggregation (purely linear, branchless)

For any register component   
k\\\*  
k  
\\\*  
​  
 where   
∗∈{f,s}  
∗∈{f,s}:

### 3.1 Neighbor mean (or weighted sum)

⟨k\\\*(c)⟩  ≡  ∑n∈N(c)wn k\\\*(n)  
⟨k  
\\\*  
​  
(c)⟩≡  
n∈N(c)  
∑  
​  
w  
n  
​  
k  
\\\*  
​  
(n)  
with fixed weights   
wn  
w  
n  
​  
 (e.g., uniform   
wn=1∣N∣  
w  
n  
​  
\=  
∣N∣  
1  
​  
).

### 3.2 Mixed “field input” per register

Define the mixed input vector to register   
k  
k:  
U\\\*(k,c)  ≡  ∑j∈{R,G,B,I}Γk←j⊙(αj⊙j\\\*(c)  +  βj⊙⟨j\\\*(c)⟩)  
U  
\\\*  
​  
(k,c)≡  
j∈{R,G,B,I}  
∑  
​  
Γ  
k←j  
​  
⊙(α  
j  
​  
⊙j  
\\\*  
​  
(c)+β  
j  
​  
⊙⟨j  
\\\*  
​  
(c)⟩)  
where   
⊙  
⊙ is elementwise (lane-wise) multiplication.  
This is the only place the chromatic algebra needs to appear: in   
Γ,α,β  
Γ,α,β.  
---

## 4\. Residual definition (the “difference that survives”)

For each register   
k  
k and component   
∗  
∗:  
Δ\\\*(k,c)  ≡  U\\\*(k,c)  −  k\\\*(c)  
Δ  
\\\*  
​  
(k,c)≡U  
\\\*  
​  
(k,c)−k  
\\\*  
​  
(c)  
This residual is the driver of evolution. Balanced states yield small residuals.  
---

## 5\. Dual-frequency dynamics (fast angular \+ slow radial)

### 5.1 Fast update law (interaction \+ rotation)

Fast dynamics must support “angular motion.” Use a fixed skew-symmetric cross-coupling matrix   
A  
A across registers:  
Let   
Xf(c)=\[Rf,Gf,Bf,If\]T  
X  
f  
​  
(c)=\[R  
f  
​  
,G  
f  
​  
,B  
f  
​  
,I  
f  
​  
\]  
T  
 as 4 vectors of length   
L  
L. Define:  
Rot(Xf)  ≡  A Xf  
Rot(X  
f  
​  
)≡AX  
f  
​  
with a constant 4×4 matrix   
A  
A satisfying   
AT=−A  
A  
T  
\=−A. A minimal, practical choice:  
A=\[0−ω00ω0−ω00ω0−ω00ω0\]  
A=  
​  
0  
ω  
0  
0  
​  
−ω  
0  
ω  
0  
​  
0  
−ω  
0  
ω  
​  
0  
0  
−ω  
0  
​  
​  
applied lane-wise (same   
A  
A for all lanes).   
ω  
ω is a scalar constant.  
Then the fast update is:  
Xf′(c)  =  Xf(c)  +  ηf Δf(c)  +  ηr Rot(Xf(c))  
X  
f  
′  
​  
(c)=X  
f  
​  
(c)+η  
f  
​  
Δ  
f  
​  
(c)+η  
r  
​  
Rot(X  
f  
​  
(c))  
where   
Δf(c)=\[Δf(R,c),Δf(G,c),Δf(B,c),Δf(I,c)\]T  
Δ  
f  
​  
(c)=\[Δ  
f  
​  
(R,c),Δ  
f  
​  
(G,c),Δ  
f  
​  
(B,c),Δ  
f  
​  
(I,c)\]  
T  
.

ηf,ηr  
η  
f  
​  
,η  
r  
​  
 are scalars (or per-lane vectors, but scalars are simpler and safe).

### 5.2 Slow update law (persistence accumulation \+ decay)

Slow dynamics represent “radius / persistence.” They must be driven by fast energy without thresholds.  
Define per-register fast energy proxy (lane-wise):  
Ek(c)≡ρ(kf(c))  
E  
k  
​  
(c)≡ρ(k  
f  
​  
(c))  
where   
ρ(⋅)  
ρ(⋅) is a smooth even function, e.g.:

* ρ(x)=x2  
* ρ(x)=x  
* 2  
*  (fast, branchless)  
* optionally   
* ρ(x)=x21+x2  
* ρ(x)=  
* 1+x  
* 2  
* x  
* 2  
* ​  
*  (soft saturation, still branchless)

Then:  
ks′(c)  =  (1−λk) ks(c)  +  ηs Ek(c)  
k  
s  
′  
​  
(c)=(1−λ  
k  
​  
)k  
s  
​  
(c)+η  
s  
​  
E  
k  
​  
(c)  
with   
λk∈(0,1)  
λ  
k  
​  
∈(0,1) being the baseline decay for register   
k  
k, and   
ηs  
η  
s  
​  
 a scalar gain.  
---

## 6\. Pressure integration (orthogonal modulation only)

Pressures may modulate decay and/or gains, but must not gate execution.

### 6.1 Effective decay (example; continuous, monotone)

Define a continuous map:  
λkeff(c)=λk⋅(1+abwPbw(c)+aowPow(c))  
λ  
k  
eff  
​  
(c)=λ  
k  
​  
⋅(1+a  
bw  
​  
P  
bw  
​  
(c)+a  
ow  
​  
P  
ow  
​  
(c))  
where   
abw,aow≥0  
a  
bw  
​  
,a  
ow  
​  
≥0.  
Then replace   
(1−λk)  
(1−λ  
k  
​  
) with   
(1−λkeff(c))  
(1−λ  
k  
eff  
​  
(c)) in the slow update. This yields “pressure-scaled decay” with no thresholds.

### 6.2 Focus modulation (example; continuous)

Allow focus to modulate input coupling strength:  
βjeff(c)=βj⋅(1+bF(c))  
β  
j  
eff  
​  
(c)=β  
j  
​  
⋅(1+bF(c))  
This makes the kernel more/less receptive without ever branching.  
---

## 7\. Paired-lane symmetry invariants (must hold by construction)

Define lane pairing by an involution   
ℓˉ  
ℓ  
ˉ  
 and sign   
s(ℓ)∈{+1,−1}  
s(ℓ)∈{+1,−1} such that:  
s(ℓˉ)=−s(ℓ),ℓˉˉ=ℓ  
s(  
ℓ  
ˉ  
)=−s(ℓ),  
ℓ  
ˉ  
ˉ  
\=ℓ

### 7.1 Symmetry condition (neutral input)

If initial state satisfies paired antisymmetry for all registers and components:  
k\\\*(c)\[ℓˉ\]=−k\\\*(c)\[ℓ\]  
k  
\\\*  
​  
(c)\[  
ℓ  
ˉ  
\]=−k  
\\\*  
​  
(c)\[ℓ\]  
and neighbor states satisfy the same relation, then the update must preserve it:  
k\\\*′(c)\[ℓˉ\]=−k\\\*′(c)\[ℓ\]  
k  
\\\*  
′  
​  
(c)\[  
ℓ  
ˉ  
\]=−k  
\\\*  
′  
​  
(c)\[ℓ\]

### 7.2 Sufficient condition on coefficients

This is guaranteed if coefficient vectors and mixing satisfy:

* αk\[ℓˉ\]=αk\[ℓ\]  
* α  
* k  
* ​  
* \[  
* ℓ  
* ˉ  
* \]=α  
* k  
* ​  
* \[ℓ\]  
* βk\[ℓˉ\]=βk\[ℓ\]  
* β  
* k  
* ​  
* \[  
* ℓ  
* ˉ  
* \]=β  
* k  
* ​  
* \[ℓ\]  
* Γk←j\[ℓˉ\]=Γk←j\[ℓ\]  
* Γ  
* k←j  
* ​  
* \[  
* ℓ  
* ˉ  
* \]=Γ  
* k←j  
* ​  
* \[ℓ\]

and all functions used are odd/even appropriately:

* residual is odd if inputs are odd  
* energy proxy   
* ρ  
* ρ is even, so slow state becomes symmetric (often desired) or can be stored as non-paired lanes if designed that way

If you want slow state to also be antisymmetric, use an odd persistence proxy instead of   
ρ  
ρ, but the standard “radius” behavior typically uses an even proxy.  
---

## 8\. Scalar and SIMD forms (side-by-side)

### 8.1 Scalar lane law (reference)

For a single lane   
ℓ  
ℓ:  
U\\\*(k,c,ℓ)=∑jΓk←j(ℓ)(αj(ℓ) j\\\*(c,ℓ)+βj(ℓ) ⟨j\\\*(c,ℓ)⟩)  
U  
\\\*  
​  
(k,c,ℓ)=  
j  
∑  
​  
Γ  
k←j  
​  
(ℓ)(α  
j  
​  
(ℓ)j  
\\\*  
​  
(c,ℓ)+β  
j  
​  
(ℓ)⟨j  
\\\*  
​  
(c,ℓ)⟩)  
Δ\\\*(k,c,ℓ)=U\\\*(k,c,ℓ)−k\\\*(c,ℓ)  
Δ  
\\\*  
​  
(k,c,ℓ)=U  
\\\*  
​  
(k,c,ℓ)−k  
\\\*  
​  
(c,ℓ)  
Xf′(c,ℓ)=Xf(c,ℓ)+ηfΔf(c,ℓ)+ηrAXf(c,ℓ)  
X  
f  
′  
​  
(c,ℓ)=X  
f  
​  
(c,ℓ)+η  
f  
​  
Δ  
f  
​  
(c,ℓ)+η  
r  
​  
AX  
f  
​  
(c,ℓ)  
ks′(c,ℓ)=(1−λkeff(c))ks(c,ℓ)+ηsρ(kf(c,ℓ))  
k  
s  
′  
​  
(c,ℓ)=(1−λ  
k  
eff  
​  
(c))k  
s  
​  
(c,ℓ)+η  
s  
​  
ρ(k  
f  
​  
(c,ℓ))

### 8.2 SIMD vector law

All equations lift by replacing scalar multiplication with lane-wise vector ops:

* αk,βk,Γk←j  
* α  
* k  
* ​  
* ,β  
* k  
* ​  
* ,Γ  
* k←j  
* ​  
*  are vectors  
* k\\\*  
* k  
* \\\*  
* ​  
*  are vectors  
* ρ  
* ρ is elementwise  
* A  
* A mixes registers (vector-to-vector)

---

## 9\. Minimal acceptance checks for this spec (kernel-level)

To treat this as “done,” the implementation must demonstrate:

1. Scalar ↔ AVX2 equivalence for identical coefficients and inputs (within tolerance).  
2. Symmetry preservation under paired antisymmetric initialization.  
3. No gating: removing pressure inputs (setting to zero) changes only coefficients, not control flow.  
4. Residual neutrality: if   
5. U\\\*=k\\\*  
6. U  
7. \\\*  
8. ​  
9. \=k  
10. \\\*  
11. ​  
12. , then   
13. Δ\\\*=0  
14. Δ  
15. \\\*  
16. ​  
17. \=0 and only rotation/decay terms act.

