# Lane VII Holographic Invariant Program Status

Status: canonical program-status ledger updated through Lane VII v2.0.1-FRI.
Date: 2026-05-09.

## Purpose

Lane VII is the active synthesis/proof-target lane for the Yang-Mills strong-coupling program. It reframes Lane II polymer sharpening as a Wilson-screen fiber entropy problem and reduces the wall-moving candidate to global spin-network Frobenius closure plus KP insertion.

## Claim boundary

Lane VII does **not** currently claim:

- continuum Yang-Mills construction;
- Clay Millennium mass-gap proof;
- weak-coupling or asymptotic-freedom control;
- extension beyond fixed-spacing strong-coupling SU(2) Wilson lattice gauge theory;
- proof of Frobenius closure for arbitrary cyclic channel graphs;
- proof that the Frobenius hybrid activity can be inserted into the v0.14.4 KP certificate;
- movement of the v0.14.4 certificate wall as a theorem.

## Current artifact / tranche chain

| Version | Status | Core result |
| --- | --- | --- |
| v0.1-FRI | Exported locally | Defines generalized holography via `(B,S,pi,I)` and selects activity-weighted Wilson-screen fiber entropy as the primary KP-compatible invariant. |
| v0.5-FRI | Exported locally | Concentrates Lane VII around the global spin-network closure theorem target. |
| v0.8-FRI | Exported locally | Formalizes the Channel Aggregation Lemma target and closure hierarchy. |
| v1.0-FRI | Exported locally | Introduces tree-Frobenius theorem direction and cyclic trace/cycle-defect obstruction. |
| v1.2-FRI | Exported locally | Framework/theorem consolidation: tree-Frobenius theorem, two-rank-2 cycle test, operator demotion, Frobenius frontier. |
| v1.3-FRI | Chat draft | Proves one-cycle Frobenius closure and factorable two-cycle closure under normalized hypotheses. |
| v1.4-FRI | Chat draft | Proves dimension-weighted Racah F-move unitarity/contractivity. |
| v1.5-FRI | Chat draft | Proves dimension-weighted 9j recoupling matrix unitarity; distinguishes recoupling operators from vertex evaluations. |
| v1.6-FRI | Exported locally | Identifies residual non-recouping trace/loop density after unitary normal form as the obstruction. |
| v1.7.1-FRI | Chat draft | Corrects residual threshold and introduces spin-weighted residual ledger. |
| v1.8-FRI | Chat draft | Audits elementary TL loops, theta/bubble identities, and 9j loops as non-residual. |
| v1.9-FRI | Chat draft, superseded | Reduces catalogue ambiguity but over-scalarizes the residual object. |
| v1.9.1-FRI | Exported locally; source committed | Corrects residual scalar notation to typed residual operator/tensor block and demotes catalogue completeness to hypothesis. |
| v1.10.1-FRI | Exported locally | Identifies Cherrington-Christensen 48j local package and normalized vertex-edge protocol. |
| v1.11-FRI | Chat draft | Defines normalized 48j package with sign/phase and path-dependence discipline. |
| v1.12-FRI | Chat draft | Shows smallest planar four-plaquette case is defect-free but degenerate. |
| v1.13-FRI | Chat draft | Two-plane rank-2 local audit: boundary-cut is operator-safe; closed-cycle is Frobenius-tight; no extra residual defect. |
| v2.0.1-FRI | Source captured | Consolidation polish: threshold notation, standing hypotheses, rank-2 local-to-global theorem rewrite, raw 3nj warning, versioning cleanup, references. |

## Primary invariant

The primary KP-facing invariant is the activity-weighted Wilson-screen fiber entropy:

```tex
h_\gamma(\beta)=\limsup_{A\to\infty}\frac1A\log B_A(\gamma;\beta)
```

with source-uniform majorant target:

```tex
B_A(\gamma;\beta) \le C(\gamma) q_{scr}(\beta)^A.
```

## Closure hierarchy

For a thick fundamental link with `n=2m` strands:

```tex
C_m = dim Inv(V_{1/2}^{\otimes 2m}),
||P_{2m}||_{op}=1,
||P_{2m}||_{HS}=sqrt(C_m),
||P_{2m}||_1=C_m.
```

Thus:

```tex
q_op <= q_Frob <= q_Cat.
```

Program status:

- Catalan/rank closure is safe but non-improving in the cubic regulator.
- Operator closure is sectoral: true for trees/cut channels but refuted in cyclic rank-2 traces.
- Frobenius closure is the cyclic mainline.

## Proved / audited partial results

1. Tree-Frobenius aggregation under normalized tree-tensor hypotheses.
2. One-cycle Frobenius closure under normalized hypotheses.
3. Factorable two-cycle Frobenius closure under normalized hypotheses.
4. Two-rank-2 cyclic trace saturates Frobenius and refutes global operator closure.
5. Dimension-weighted Racah F-move and 9j recoupling maps are unitary as changes between orthonormal bases.
6. Planar smallest local case is defect-free but degenerate.
7. Two-plane rank-2 local case reproduces the global hierarchy locally and shows no extra E-class residual block.

## Residual-defect condition

The candidate Frobenius wall is conditional not only on Frobenius closure and KP insertion but also on residual defect control.

The exact spin-weighted residual condition is:

```tex
\sum_j \rho_j \log(2j+1) < \log(2/5^{1/3}).
```

For fundamental residual loops only:

```text
rho_{1/2} < log_2(2/5^{1/3}) ~= 0.226024
```

The active residual object is typed as an operator/tensor block:

```tex
\mathcal E: H_{in} \to H_{out},
\lambda=||\mathcal E||_{op}
```

unless another norm is explicitly justified by the contraction structure.

## Conditional certificate consequence

If arbitrary cyclic Frobenius closure is proved, residual defect is subcritical, and KP insertion is valid, the candidate hybrid activity is:

```tex
Q_{hyb}^{Frob}(\beta)=Q(\beta)-4r_{1/2}(\beta)+2r_{1/2}(\beta)5^{1/3}.
```

The corresponding candidate wall is approximately:

```text
beta_Frob ~= 0.00735851805
```

This is conditional and not a theorem.

## Current next research target

```text
Lane VII v1.14-FRI: Three-Plane Rank-5 Vertex Stress Test
```

Scope:

1. activate three coordinate planes `(12)+(13)+(14)`;
2. study the shared `e_1` edge with six fundamental strands:
   `H_6 = Inv(V_{1/2}^{\otimes 6})`, `dim H_6 = C_3 = 5`;
3. separate boundary-cut and closed-cycle sub-cases;
4. test operator/Frobenius/Catalan scales `1`, `sqrt(5)`, `5`;
5. verify path-independence across multiple `H_6` coupling trees;
6. classify whether any residual `E`-class block remains.

## Progress threshold / fallback boundary

Lane VII remains active while each tranche either proves a new class of closure, narrows the obstruction to a more concrete algebraic object, or produces a quantitative defect bound.

Lane VII should pause and revive narrower Lane II work if two consecutive Lane VII tranches only rename the obstruction without a new theorem, computation, or defect estimate; or if residual defect density is shown to be Catalan-scale for generic cubic polymers.

See `docs/lane-vii-progress-thresholds.md` for the explicit decision ledger.

## Relation to other lanes

- Lane I: v0.14.4 remains the theorem-track anchor.
- Lane II: supplies cubic polymer behavior and remains backup if Lane VII becomes Catalan-scale or non-KP-compatible.
- Lane III: supplies obstruction taxonomy and non-claim discipline.
- Lane IV: supplies preimage/interface discipline.
- Lane V/Brownian Holonomy: parked diagnostic sidecar.
- Lane VI: parked spherical/simplicial regulator diagnostic.
- Lane VII: active synthesis/proof-target lane.
