# Lane VII Consolidation v2.0.2-FRI

## Screen Fiber Entropy, Spin-Network Closure, and the Finite Local Fundamental Catalogue

Michael D. Heller  
SocioProphet Research  
Working consolidation draft. May 2026.

## Abstract

This memorandum updates Lane VII Consolidation v2.0.1 through the v1.17 local fundamental catalogue enumeration. The framework, formalism, screen-transfer architecture, closure hierarchy, standing hypotheses, and core theorem scaffolding remain unchanged. Three substantive additions are recorded.

First, the multi-thick representative audit covering `(2,2)`, `(3,2)`, `(3,3)`, and `(2,2,2)`-cycle sectors establishes Frobenius control across the leading multi-thick channel-pattern representatives. The `(3,2)` mixed-rank case is Frobenius-subcritical via rectangular partial-isometry analysis, and the `(2,2,2)` cycle is Frobenius-subcritical via Schatten-3 Hölder.

Second, the full local fundamental catalogue is enumerated as the `B_4` quotient of the parity-admissible space: `rank_F2(A)=7`, `|ker A|=2^17=131072`, `|ker A / B_4|=560`, with `58` distinct sorted edge-rank profiles.

Third, the smallest-case framing is corrected: the smallest parity-admissible local assignment has area `3` with rank profile `(1,1,1,0,0,0,0,0)`, not the area-4 planar patch. The v1.12-v1.16 audits remain valid as channel-pattern stress tests rather than minimal-area catalogue representatives.

The local fundamental defect-free theorem is now a finite verification problem over 560 orbit classes. Subsequent v1.18 work shows that the orbit catalogue is high-Betti dominated; that later result is not folded into this v2.0.2 snapshot except as a note in the status ledger. No KP wall movement, v0.14.4 extension, continuum Yang-Mills construction, or Clay-level implication is claimed.

## 1. Program context and claim boundary

The theorem-track anchor remains the fixed-spacing strong-coupling SU(2) Wilson lattice mass-gap seed theorem v0.14.4 with its constants `M_0`, `D_inc`, `q_KP`, and `beta_*`, all preserved without modification. Lane II's polymer-sharpening question is absorbed into the Lane VII screen-fiber formulation.

This v2.0.2 consolidation does not claim arbitrary cyclic Frobenius closure, KP insertion of a Frobenius hybrid activity, movement of the v0.14.4 wall, a continuum Yang-Mills construction, or a Clay-level result. It is a framework consolidation with partial closure theorems, local catalogue enumeration, and multi-thick representative audits.

## 2. Carried-forward framework

The following material carries forward from v2.0.1 without substantive change:

- generalized holography formalism `(B,S,pi,I)`;
- Yang-Mills polymer screen fiber;
- screen-transfer architecture;
- closure hierarchy `q_op <= q_Frob <= q_Cat`;
- standing hypotheses H1-H5;
- tree-Frobenius aggregation theorem;
- one-cycle and factorable two-cycle closure results;
- cyclic rank-2 test and operator refutation;
- recoupling unitarity with raw-`3nj` warning;
- Cherrington-Christensen normalized vertex-edge package definition.

## 3. Multi-thick channel representative audits

The first multi-thick sectors are `(2,2)`, `(3,2)`, `(3,3)`, and `(2,2,2)`-cycle, with rank profiles indicating active thick-edge multiplicities. Audits are at the channel-graph level under H1-H5.

### 3.1 Sector `(2,2)`

Two distinct edges have rank `r=2`, hence channel dimension `C_2=2` at each.

Boundary-cut case:

```tex
\|P_4 \otimes P_4\|_{op}=1.
```

Single closed equal-rank two-projector cycle:

```tex
|Tr(PUQV)| \le 2 = \sqrt{2}\sqrt{2},
```

with equality in the aligned case. Frobenius is tight; Catalan is safe but loose.

Independent product-of-cycles topologies may yield product values, but those are products of already-controlled cycles and should not be conflated with a single coupled cycle.

### 3.2 Sector `(3,2)`

One edge has rank `r=3` with channel dimension `C_3=5`; one edge has rank `r=2` with channel dimension `C_2=2`.

Boundary-cut case:

```tex
\|P_6 \otimes P_4\|_{op}=1.
```

Single mixed-rank closed cycle requires rectangular partial isometries between `H_6` and `H_4`. Its trace rank is bounded by the smaller channel dimension:

```tex
|Contr| \le \min(5,2)=2 < \sqrt{10}=\sqrt{5}\sqrt{2}.
```

Thus the genuinely mixed `(3,2)` coupled cycle is Frobenius-subcritical. Values such as `10=5*2` belong to independent product-of-cycles topologies, not to a single mixed two-projector cycle.

### 3.3 Sector `(3,3)`

Two distinct edges have rank `r=3`, hence channel dimension `C_3=5` at each.

Boundary-cut case:

```tex
\|P_6 \otimes P_6\|_{op}=1.
```

Single closed equal-rank two-projector cycle:

```tex
|Tr(PUQV)| \le 5 = \sqrt{5}\sqrt{5},
```

with equality in the aligned case. Frobenius is tight; Catalan is safe but loose.

### 3.4 Sector `(2,2,2)`-cycle

Three rank-2 channels form a 3-cycle:

```tex
Tr(P_1 U_1 P_2 U_2 P_3 U_3).
```

Schatten-3 Hölder gives:

```tex
|Tr(P_1 U_1 P_2 U_2 P_3 U_3)|
  <= \|P_1\|_3\|P_2\|_3\|P_3\|_3
  = (2^{1/3})^3 = 2.
```

The naive Frobenius product is:

```tex
(\sqrt{2})^3=2\sqrt{2}.
```

So the 3-cycle is Frobenius-subcritical with slack. The aligned case attains the Schatten-3 bound `2`.

## 4. Local-to-global consistency through multi-thick sectors

### Theorem 3' — Multi-thick local-to-global consistency

In the normalized local audit through fundamental ranks `C_1=1`, `C_2=2`, `C_3=5` and the leading multi-thick sectors `(2,2)`, `(3,2)`, `(3,3)`, and `(2,2,2)`-cycle:

1. boundary-cut configurations are operator-safe;
2. closed two-projector equal-rank cycles are Frobenius-tight at the aligned case;
3. closed mixed-rank cycles and three-projector cycles are Frobenius-subcritical;
4. Catalan/rank scale is safe but loose throughout;
5. no additional residual `E`-class vertex defect appears in any audited sector;
6. path-independence holds under unitary changes among standard coupling-tree bases at all audited ranks via dimension-weighted recoupling unitarity.

This extends the local-to-global consistency statement from single-edge ranks to the leading multi-thick configurations. It does not enumerate all orbit classes and does not prove arbitrary cyclic Frobenius closure.

## 5. Local fundamental catalogue enumeration

The local fundamental catalogue is the parity-admissible quotient

```tex
\mathcal C_{fund}=\{S\subseteq\mathcal P_v:Ax=0\}/B_4,
```

where `P_v` is the set of 24 plaquette quadrants incident to a cubic 4D lattice vertex, `A` is the edge-incidence matrix over `F_2`, and `B_4` is the hyperoctahedral group of order 384.

Direct enumeration establishes:

```tex
rank_{F_2}(A)=7,
|ker A|=2^{17}=131072,
|\mathcal C_{fund}|=560.
```

The 560 orbit classes realize 58 distinct sorted edge-rank profiles.

## 6. Smallest-case correction

The smallest nontrivial parity-admissible local assignment has area 3 with rank profile

```text
(1,1,1,0,0,0,0,0),
```

not the area-4 planar patch. One representative is three plaquette quadrants forming a local triangle on three oriented edge directions. Each of the three involved edges appears in exactly two plaquettes, satisfying parity.

The v1.12 area-4 planar patch is one of the area-4 orbit classes, not the catalogue minimum. The v1.12-v1.16 audits remain valid as channel-pattern stress tests.

## 7. Catalogue distributions

The orbit count by local area is symmetric under complement. The maximum area stratum is at area 12 with 88 orbits.

The orbit count by number of thick edges is complement-symmetric. Orbits with at most one thick edge total 74; the remaining 486 are multi-thick. The multi-thick regime is therefore dominant.

The orbit count by maximum rank is:

```text
max rank 0: 1
max rank 1: 32
max rank 2: 397
max rank 3: 130
```

Most catalogue classes have maximum rank 2. Rank-3 classes are substantial but not dominant.

## 8. Refined open theorem

### Conjecture 1 — Frobenius closure with subcritical residual defect

Let `Gamma` be a fundamental admissible cubic Wilson polymer. Suppose the standing hypotheses H1-H5 hold and residual blocks satisfy

```tex
\limsup_{|\Gamma|\to\infty}\frac1{|\Gamma|}\sum_v\log\|\mathcal E_v\|_{op}<\log(2/5^{1/3}).
```

Then the Frobenius hybrid activity remains improving at the KP exponential scale.

### Local Catalogue Frobenius Safety Conjecture

For every orbit class `[S]` in `ker A / B_4`, the normalized local residual block either:

1. is operator-safe in boundary-cut topology;
2. is Frobenius-tight or Frobenius-subcritical in closed-cycle topology;
3. has no extra `E`-class residual block beyond the expected projector closure scale.

Equivalently, `D_vert^[S]=1` after R/O/L/V/E ledger allocation.

This is now a finite verification problem over 560 orbit classes. Later v1.18 work shows that most orbits have high-Betti components, so a general Eulerian Schatten/Frobenius theorem is needed rather than representative auditing alone.

## 9. Conditional certificate consequence

If arbitrary cyclic Frobenius closure is proved, all local catalogue orbits are subcritical/defect-free, the Wilson-screen-to-dual-package bridge is established, and KP insertion succeeds, the candidate hybrid activity remains:

```tex
Q_{hyb}^{Frob}(\beta)=Q(\beta)-4r_{1/2}(\beta)+2r_{1/2}(\beta)5^{1/3}.
```

The candidate wall remains approximately:

```text
beta_Frob ~= 0.00735851805.
```

This is conditional and not a theorem.

## 10. Open problems and next research directions

1. **Eulerian channel-graph Schatten/Frobenius bound.** The v1.18 orbit-reduction audit shows that 527 of 560 orbit classes contain high-Betti components. The next theorem target is a general norm allocation theorem for Eulerian channel graphs.
2. **Wilson-screen-to-dual-package bridge lemma.** Prove that the Lane VII Wilson-screen polymer contraction is represented by the normalized Cherrington-Christensen / Oeckl-Pfeiffer dual vertex-edge package with correct source insertion.
3. **KP insertion audit.** Only after closure and bridge results are established.
4. **Lane III v0.18 closing and methodology manifesto.** Track-balance work remains active through Issues #12 and #13.

## 11. Non-claim box

This memorandum does not claim:

- Frobenius closure for arbitrary cyclic channel graphs;
- defect-freeness of all 560 orbit classes;
- proof of the Wilson-screen to dual-package bridge;
- KP insertion of the Frobenius hybrid activity;
- movement of the v0.14.4 wall;
- extension of v0.14.4;
- continuum Yang-Mills construction;
- any Clay-level implication.

Positive claims:

- Lane VII has a screen-fiber entropy formulation of the polymer-sharpening problem;
- tree-like, one-cycle, and factorable two-cycle channel graphs satisfy Frobenius closure under H1-H5;
- global operator closure is refuted in cyclic channels;
- dimension-weighted recouplings are unitary; raw `3nj` scalars are not automatically norm-neutral;
- the normalized Cherrington-Christensen vertex-edge package is the correct local audit object;
- single-edge local audits at ranks `C_1,C_2,C_3` agree with the Frobenius mainline;
- multi-thick channel sectors `(2,2)`, `(3,2)`, `(3,3)`, and `(2,2,2)`-cycle are Frobenius-controlled, with `(3,2)` and `(2,2,2)` strictly Frobenius-subcritical in their coupled-cycle forms;
- the local fundamental catalogue is the finite quotient `ker A / B_4` with 560 orbit classes across 58 sorted rank profiles;
- the local catalogue problem is now a finite verification problem, subsequently sharpened by v1.18 to a high-Betti Eulerian norm-allocation theorem target.

## 12. References

Same reference spine as v2.0.1, with Lane VII v1.15-v1.18 internal tranches added as program references.
