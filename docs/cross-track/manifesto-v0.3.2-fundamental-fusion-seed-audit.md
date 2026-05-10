# Manifesto v0.3.2 — Fundamental Fusion Seed Audit

Status: cross-track bridge patch; program-internal; not a theorem claim.

This document captures the in-chat v0.3.2 upgrade to the Yang-Mills cross-track manifesto. It belongs in `SocioProphet/yang-mills` because the repository is the working home for fixed-spacing strong-coupling SU(2), Lane II sharpening, Lane III obstruction taxonomy, Lane VII spin-network closure, and related lane-bridge artifacts.

## Claim boundary

This patch does not claim a continuum Yang-Mills construction, a weak-coupling theorem, an SU(N >= 3) theorem, an asymptotic-freedom trajectory theorem, a Clay submission, or quark confinement.

It also does not claim that the finite Galerkin cutoff `H_{1/2}` is invariant under the full OS transfer matrix, complete in the OS Hilbert space, or sufficient for the Lane I theorem track.

## Fundamental fusion seed

For SU(2), the spin-`1/2` representation generates the representation ring under fusion. In the integer representation convention

```text
n = 2j
```

the fundamental representation is `n = 1`. For `n >= 1`, the character recursion is

```text
chi_1 chi_n = chi_{n+1} + chi_{n-1}
```

with boundary case

```text
chi_1 chi_0 = chi_1.
```

Equivalently, tensoring by the fundamental representation advances or lowers the integer representation label by one unit, subject to the SU(2) Clebsch-Gordan admissibility constraints.

Thus the `Jmax = 1/2` fixture, containing the `n = 0` and `n = 1` sectors, is the minimal nontrivial fusion-generated Galerkin seed of the Lane B tower. Higher cutoff sectors, beginning with `n = 2` at `Jmax = 1`, are representation-theoretically fused descendants of this seed.

This is a representation-ring naturality statement only.

## Registry caution

The embedded fixture indices

```text
[0, 1, 3, 4, 5]
```

inside the `Jmax = 1` registry are consistent with the fundamental-seed interpretation. Under the current registry reading, the omitted index `2` corresponds to `Phi_200`, the first pure `n = 2` / `j = 1` descendant, and is therefore excluded from the `Jmax = 1/2` seed.

This index correspondence must be checked directly against the Phase 3a basis registry before it is used as evidentiary language. Until that registry check is recorded, the conservative claim is only that the noncontiguous embedding is consistent with the fusion-hierarchy reading.

## Gegenbauer convention

Phase 3d outputs using Gegenbauer notation must record the channel convention explicitly. For total channel `ell`, the Peter-Weyl / Gegenbauer basis uses parameter

```text
alpha = ell + 1.
```

This is a finite-cutoff basis convention for the Lane B audit, not a theorem-level assertion.

## Phase 3d fundamental-subspace audit

Phase 3d must test whether the `Jmax = 1/2` fixture is merely representation-natural or also spectrally privileged inside the full `Jmax = 1` transfer matrix.

Let the registered raw basis be `Phi_i`. Let

```text
F = [0, 1, 3, 4, 5]
```

be the embedded `Jmax = 1/2` fixture index set, after explicit Phase 3a registry verification.

Let `B_F` be the `14 x 5` coordinate-selection matrix whose columns are the standard basis vectors indexed by `F`.

The raw Gram and transfer matrices are

```text
G_ij = <Phi_i, Phi_j>
K_ij = <Phi_i, T Phi_j>.
```

Use a sector-respecting whitening map

```text
W = G^{-1/2},
```

computed block-by-block on the Peter-Weyl / parity decomposition. The preferred convention is the positive Hermitian inverse square root on each sector block. If another whitening convention is used, it must be recorded, and every analytic comparison target must be transformed using the same convention.

The whitened transfer matrix is

```text
K_orth = W* K W.
```

Construct an orthonormal basis `Q_F` for

```text
range(W^{-1} B_F)
```

and define the Euclidean orthogonal projection

```text
P_F = Q_F Q_F*.
```

Equivalently, `P_F` is the whitened-coordinate form of the `G`-orthogonal projection onto the raw embedded fixture subspace. Let

```text
P_D = I - P_F
```

denote the fused-descendant complement.

Report the leakage ratios

```text
L_{F->D} = ||P_D K_orth P_F||_F / ||K_orth P_F||_F
L_{D->F} = ||P_F K_orth P_D||_F / ||K_orth P_D||_F.
```

For every low eigenvector `v_i` of `K_orth`, normalized in the whitened Euclidean inner product, report the fundamental mass

```text
m_F(v_i) = ||P_F v_i||^2.
```

In particular, report `m_F(v_0)` for the vacuum/top eigenvector.

## Null models

Raw leakage values are not interpretable without baselines.

Primary null: sector-matched random subspaces. Since the embedded `Jmax = 1/2` seed has scalar dimension `4`, vector dimension `1`, and tensor dimension `0`, sample random subspaces from

```text
Gr(4, 9)_scalar x Gr(1, 4)_vector
```

with no tensor component. Report empirical percentiles for the observed leakage ratios.

Secondary null: unstructured `Gr(5, 14)` random subspaces in the whitened space.

Block-diagonal null: if the transfer matrix were exactly block diagonal with respect to

```text
H_1 = H_F \oplus H_D,
```

then both leakage ratios would be zero.

If a denominator is numerically zero, record the case explicitly. Do not silently regularize.

## Registry audit

Before using the noncontiguous embedding as evidence for the fusion hierarchy, Phase 3d must record a registry table with:

```text
index, basis label, sector ell, integer labels n_P/n_Q, seed/descendant status, inclusion/exclusion reason.
```

At minimum, it must verify `F = [0, 1, 3, 4, 5]` and determine whether `index 2 = Phi_200` under the Phase 3a registry convention. If not, the skip-index interpretation must be withdrawn or rewritten.

## Falsification gates for v0.4 thesis

Candidate v0.4 thesis:

> The Lane B Galerkin tower is naturally organized as a fundamental-fusion hierarchy, with `Jmax = 1/2` as the primitive seed and higher `Jmax` sectors as systematically fused descendants.

The representation-theoretic motivation is sound. Its spectral strengthening is falsifiable.

F1 — vacuum non-dominance: if `m_F(v_0) <= 1/2`, the seed is not spectrally dominant for the vacuum/top eigenvector at `Jmax = 1`.

F2 — generic leakage: if either `L_{F->D}` or `L_{D->F}` is at or above the median of the sector-matched random-subspace null, the embedded seed has no special transfer-coupling structure at `Jmax = 1`.

F3 — loss of primitive nonabelian channel: if the `Phi_111` channel is not the first or leading genuinely nonabelian relative-orientation signal at `Jmax = 1`, and a fused `n = 2` descendant provides the dominant nonabelian channel under a predeclared diagnostic, then the primitive-nonabelian reading of `Phi_111` is cutoff-specific rather than structural.

## Promotion rule

The v0.4 thesis may be promoted only if all of the following hold:

1. Phase 3a registry audit confirms the embedded index interpretation, including index `2`.
2. `m_F(v_0) > 1/2`.
3. Both leakage ratios are below the sector-matched random-subspace median.
4. `Phi_111` remains the first or leading genuinely nonabelian relative-orientation channel under the predeclared diagnostic.
5. Whitening, scalar-factorization, self-adjointness, sector-leakage, fixture-regression, and Gram-conditioning residuals remain within the Phase 3d acceptance budget.

If any condition fails, the conclusion is not program failure. The correct conclusion is that the fundamental-fusion seed is representation-natural but not spectrally dominant at this cutoff, or that the first fused-descendant layer materially reorganizes the transfer spectrum.

## Cross-program boundary

Cross-program analogies to Lawful Learning, Temporal Mechanics, Hopf-rung scaffolding, or proof-character dynamics are documented separately. They are not load-bearing for any Yang-Mills claim in this manifesto patch.
