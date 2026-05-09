# Lane VII Consolidation v2.0.1-FRI

## Polish Patch Before Rank-5 Stress Test

Michael D. Heller  
SocioProphet Research  
Working consolidation patch. May 2026.

## 0. Status

v2.0.1 supersedes v2.0 at the editorial and precision layer only. It does not add a new theorem. It corrects notation, restores the standing hypotheses, sharpens the local-to-global rank-2 theorem, fixes version sequencing, and adds the missing reference spine.

The next research tranche remains:

```text
Lane VII v1.14-FRI: Three-Plane Rank-5 Vertex Stress Test
```

No new wall movement, KP insertion, continuum construction, or Clay-level implication is claimed.

## 1. Threshold notation fix

Use natural logarithm for residual log-density:

```tex
\Lambda_{\mathrm{res}}(\Gamma)=\frac1{|\Gamma|}\sum_v \log \lambda_v.
```

The Frobenius route survives if

```tex
\limsup_{|\Gamma|\to\infty}\Lambda_{\mathrm{res}}(\Gamma)<\log\left(\frac{2}{5^{1/3}}\right).
```

Numerically:

```text
log(2/5^{1/3}) ~= 0.15667
```

For fundamental residual loops only, where each residual loop contributes a factor 2, this is equivalent to the base-2 condition:

```tex
\rho_{1/2}<\log_2\left(\frac{2}{5^{1/3}}\right)\approx0.226024.
```

For mixed-spin residual loops, the correct condition is:

```tex
\sum_j \rho_j\log(2j+1)<\log\left(\frac{2}{5^{1/3}}\right).
```

## 2. Standing hypotheses box

**H1. Unitary TL/Wigner normal form.** The spin-network contraction is expressed in an orthonormal Wigner/Temperley-Lieb basis. Pure recoupling transformations are represented by dimension-weighted Racah `F`-moves, dimension-weighted `9j` changes of basis, or higher `3nj` unitary basis transformations when justified.

**H2. Normalized vertex tensors.** Local vertex tensors used in tree and cycle aggregation are contractive in the relevant channel Hilbert spaces:

```tex
\|T_v\|_{\mathrm{op}}\le 1.
```

When this is not known, it must be audited or moved into the residual defect ledger.

**H3. Boundary-source uniformity.** Wilson-screen boundary data contribute only a prefactor `C(gamma)` with no exponential growth in polymer area.

**H4. Absolute-majorant discipline.** All signs, Wigner phases, twist signs, and orientation phases are discarded under absolute value unless a separate cancellation theorem is proved:

```tex
\left|\sum_\alpha \epsilon_\alpha A_\alpha\right|\le\sum_\alpha |A_\alpha|.
```

**H5. Canonical decomposition convention.** Local vertex audits are relative to the canonical decomposition convention `D_can` until a confluence theorem or minimization principle is proved.

## 3. Local-to-global rank-2 theorem rewrite

**Theorem.** For the two-plane fundamental local assignment in unitary TL/Wigner normal form, with shared edge channel

```tex
H_4=\operatorname{Inv}(V_{1/2}^{\otimes4}),\qquad \dim H_4=2,
```

the normalized local vertex audit satisfies:

```tex
\|\mathcal E_v^{\mathrm{cut}}\|_{\mathrm{op}}\le1
```

in the boundary-cut sub-case, while in the closed-cycle sub-case the contraction can saturate Frobenius scale:

```tex
|\operatorname{Contr}|=2=\sqrt2\,\sqrt2.
```

No additional residual `E`-class vertex defect remains beyond the expected closure scale, and the result is invariant under unitary changes among the standard rank-2 coupling trees. Therefore the local vertex audit reproduces the global Lane VII closure hierarchy at the first nontrivial channel rank:

```tex
q_{\mathrm{op}}\le q_{\mathrm{Frob}}\le q_{\mathrm{Cat}},
```

with operator closure sectoral and Frobenius closure the cyclic mainline.

Proof sketch: the boundary-cut case is operator-norm Cauchy-Schwarz applied to `P_4`; the closed-cycle case is the aligned rank-2 trace `Tr(PUQV)=2`, saturating `sqrt(2)sqrt(2)`; path-independence follows from unitary Racah recoupling among rank-2 coupling bases.

## 4. Raw `3nj` warning

A raw `3nj` symbol is a scalar coefficient or matrix entry, not a unitary operator by itself. Unitarity belongs to the correctly dimension-weighted recoupling matrix acting between orthonormal coupling bases. Therefore raw `6j`, `9j`, or higher `3nj` evaluations must never be treated as norm-neutral unless the dimension weights and basis-change interpretation have been explicitly supplied.

This is load-bearing for the Cherrington-Christensen `48j` package audit.

## 5. Versioning convention

Use this convention going forward:

- `v2.0.x` denotes consolidation/framework-paper snapshots.
- `v1.14`, `v1.15`, ... denote research tranches continuing the Lane VII proof sequence.

The next research tranche is:

```text
Lane VII v1.14-FRI: Three-Plane Rank-5 Vertex Stress Test
```

## 6. Next tranche: rank-5 stress test

Activate three coordinate planes sharing one edge:

```tex
(12)+(13)+(14).
```

The shared `e_1` edge sees six fundamental strands:

```tex
H_6=\operatorname{Inv}(V_{1/2}^{\otimes6}),\qquad \dim H_6=C_3=5.
```

The expected closure scales are:

```tex
1,\qquad \sqrt5,\qquad 5.
```

The boundary-cut case is expected to be operator-safe. The closed-cycle aligned case is expected to saturate Frobenius:

```tex
|\operatorname{Contr}|=5=\sqrt5\,\sqrt5.
```

Path-independence must be checked across multiple `H_6` coupling trees.

## 7. Reference spine

1. M. D. Heller, *Strong-Coupling Lattice Mass-Gap Seed v0.14.4*, internal manuscript, 2026.
2. J. W. Cherrington and J. D. Christensen, *A dual non-Abelian Yang-Mills amplitude in four dimensions*, Nuclear Physics B 813(3), 370-382, 2009. arXiv:0808.3624.
3. M. P. Reisenberger, *Worldsheet formulations of gauge theories and gravity*, arXiv:gr-qc/9412035, 1994.
4. L. Freidel and J. Hnybida, *On the exact evaluation of spin networks*, arXiv:1201.3613, 2012.
5. L. Freidel and J. Hnybida, *A discrete and coherent basis of intertwiners*, arXiv:1305.3326, 2013.
6. N. Crampe, L. Poulain d'Andecy, and L. Vinet, *Temperley-Lieb, Brauer and Racah algebras and other centralizers of su(2)*, arXiv:1905.06346, 2019.
7. F. M. Goodman and H. Wenzl, *The Temperley-Lieb algebra at roots of unity*, Pacific Journal of Mathematics 161(2), 307-334, 1993.
8. J. S. Carter, D. E. Flath, and M. Saito, *The Classical and Quantum 6j-Symbols*, Princeton University Press, 1995.
9. L. H. Kauffman and S. L. Lins, *Temperley-Lieb Recoupling Theory and Invariants of 3-Manifolds*, Princeton University Press, 1994.
10. R. Oeckl and H. Pfeiffer, *The dual of pure non-Abelian lattice gauge theory as a spin foam model*, Nuclear Physics B 598(1-2), 400-426, 2001.
11. NIST Digital Library of Mathematical Functions, Chapter 34, *3j, 6j, 9j Symbols*.

## 8. Non-claim box

This patch does not claim Frobenius closure for arbitrary cyclic channel graphs, KP insertion, movement of the v0.14.4 wall, a continuum Yang-Mills construction, or any Clay-level result. It is a consolidation-polish patch and a protocol update before the rank-5 stress test.
