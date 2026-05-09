# Phase 3a — Jmax=1 Basis Registry and Sector Labels

## Temporal Mechanics / Yang-Mills finite bridge

Michael D. Heller  
SocioProphet Research  
Working registry artifact. May 2026.

## 0. Scope

This artifact opens Phase 3a of the `Jmax=1` scale-up after the Phase 2 `Jmax=1/2` fixture verification.

The deliverable is a basis registry only:

- `Jmax=1` label set;
- ordering convention;
- sector tags;
- plaquette-swap symmetry map;
- `Jmax=1/2` truncation subset.

This artifact does **not** compute a Gram matrix, transfer matrix, spectrum, vacuum decomposition, coefficient graph, beta trend, scale proxy, physical mass, or continuum statement.

## 1. Source convention

The representation-basis Galerkin construction uses triples

```tex
(j,k,\ell),
```

where `j` and `k` label the SU(2) representation content carried by the two plaquette variables `P` and `Q`, and `ell` labels the intermediate channel under residual diagonal conjugation.

Use integer labels:

```tex
n=2j,\qquad m=2k.
```

Then at cutoff `Jmax`, set:

```tex
L=2Jmax.
```

The admissible labels are:

```tex
0\le n,m\le L,\qquad 0\le \ell\le \min(n,m).
```

The finite dimension is:

```tex
\dim H_{phys}(Jmax)=\sum_{n=0}^{L}\sum_{m=0}^{L}(\min(n,m)+1)
=\frac{(L+1)(L+2)(2L+3)}6.
```

For `Jmax=1`, `L=2`, hence:

```tex
\dim H_{phys}(1)=14.
```

This agrees with the Part Two v2.9 Appendix F readiness statement.

## 2. Label convention

The registry label is:

```tex
\Phi_{n m \ell}.
```

Examples:

```text
Phi_000 = vacuum
Phi_100 = spin-1/2 on P only
Phi_010 = spin-1/2 on Q only
Phi_111 = relative-orientation vector channel at Jmax=1/2
Phi_222 = new rank-2 relative-orientation channel at Jmax=1
```

## 3. Ordering convention

The ordering is chosen to preserve the `Jmax=1/2` fixture order as a truncation subset. The basis order is:

| Index | Label | `(n,m,ell)` | `(j,k,ell)` | Sector tags |
| ---: | --- | --- | --- | --- |
| 0 | `Phi_000` | `(0,0,0)` | `(0,0,0)` | vacuum, scalar_even, jhalf_fixture |
| 1 | `Phi_100` | `(1,0,0)` | `(1/2,0,0)` | scalar_even, jhalf_fixture, p_only |
| 2 | `Phi_010` | `(0,1,0)` | `(0,1/2,0)` | scalar_even, jhalf_fixture, q_only |
| 3 | `Phi_200` | `(2,0,0)` | `(1,0,0)` | scalar_even, new_jmax1, p_only |
| 4 | `Phi_110` | `(1,1,0)` | `(1/2,1/2,0)` | scalar_even, jhalf_fixture, mixed_two_plaquette |
| 5 | `Phi_111` | `(1,1,1)` | `(1/2,1/2,1)` | relative_orientation_vector, jhalf_fixture, mixed_two_plaquette |
| 6 | `Phi_020` | `(0,2,0)` | `(0,1,0)` | scalar_even, new_jmax1, q_only |
| 7 | `Phi_210` | `(2,1,0)` | `(1,1/2,0)` | scalar_even, new_jmax1, mixed_two_plaquette |
| 8 | `Phi_211` | `(2,1,1)` | `(1,1/2,1)` | relative_orientation_vector, new_jmax1, mixed_two_plaquette |
| 9 | `Phi_120` | `(1,2,0)` | `(1/2,1,0)` | scalar_even, new_jmax1, mixed_two_plaquette |
| 10 | `Phi_121` | `(1,2,1)` | `(1/2,1,1)` | relative_orientation_vector, new_jmax1, mixed_two_plaquette |
| 11 | `Phi_220` | `(2,2,0)` | `(1,1,0)` | scalar_even, new_jmax1, mixed_two_plaquette |
| 12 | `Phi_221` | `(2,2,1)` | `(1,1,1)` | relative_orientation_vector, new_jmax1, mixed_two_plaquette |
| 13 | `Phi_222` | `(2,2,2)` | `(1,1,2)` | relative_orientation_rank2, new_jmax1_tensor, mixed_two_plaquette |

The corresponding machine-readable registry is stored in:

```text
manuscripts/lane-temporal-mechanics-jmax1/phase3a-basis-registry/basis_registry.json
```

## 4. `Jmax=1/2` truncation subset

The `Jmax=1/2` fixture corresponds to all labels with:

```tex
\max(n,m)\le1.
```

In the Phase 3a ordering these are indices:

```text
[0, 1, 2, 4, 5]
```

with labels:

```text
Phi_000, Phi_100, Phi_010, Phi_110, Phi_111.
```

This exactly recovers the locked fixture label set:

```text
(0,0,0), (1/2,0,0), (0,1/2,0), (1/2,1/2,0), (1/2,1/2,1).
```

This is the permanent regression subset for Phase 3b and Phase 3c.

## 5. New `Jmax=1` labels

The new labels introduced at `Jmax=1` are:

```text
Phi_200, Phi_020, Phi_210, Phi_211, Phi_120, Phi_121, Phi_220, Phi_221, Phi_222.
```

They divide into:

### One-plaquette spin-1 scalar labels

```text
Phi_200, Phi_020
```

### Mixed scalar labels

```text
Phi_210, Phi_120, Phi_220
```

### Mixed relative-orientation vector labels

```text
Phi_211, Phi_121, Phi_221
```

### New rank-2 relative-orientation channel

```text
Phi_222
```

This last label is the first `ell=2` channel and is new at `Jmax=1`.

## 6. Plaquette-swap symmetry

The swap symmetry `P <-> Q` maps:

```text
Phi_100 <-> Phi_010
Phi_200 <-> Phi_020
Phi_210 <-> Phi_120
Phi_211 <-> Phi_121
```

and fixes:

```text
Phi_000, Phi_110, Phi_111, Phi_220, Phi_221, Phi_222.
```

Phase 3b and later matrices must respect this symmetry unless an explicitly asymmetric source or boundary condition is introduced.

## 7. Sector tags

The registry uses the following sector tags:

- `vacuum`
- `scalar_even`
- `relative_orientation_vector`
- `relative_orientation_rank2`
- `new_jmax1_tensor`
- `p_only`
- `q_only`
- `mixed_two_plaquette`
- `jhalf_fixture`
- `new_jmax1`

The first Phase 3b Gram check should group rows/columns by these tags and verify that the `jhalf_fixture` sub-block reproduces the identity Gram gate.

## 8. Phase 3a result

Phase 3a establishes:

```tex
\dim H_{phys}(Jmax=1)=14.
```

It provides a deterministic basis ordering and sector registry.

It identifies the exact `Jmax=1/2` regression subspace:

```text
indices [0,1,2,4,5]
```

and marks the new `Jmax=1` degrees of freedom.

## 9. Non-claim box

This artifact does not claim:

- a Gram matrix;
- a transfer matrix;
- a spectrum;
- a vacuum decomposition;
- a coefficient graph;
- beta-trend behavior;
- a scale proxy;
- physical mass interpretation;
- continuum Yang-Mills construction;
- infinite-volume theorem;
- Clay-level result.

Positive claims:

- the `Jmax=1` physical basis has 14 labels under the declared `(n,m,ell)` convention;
- the `Jmax=1/2` fixture embeds as the five-label subset `[0,1,2,4,5]`;
- the new `Jmax=1` labels and sector tags are explicitly registered;
- plaquette-swap symmetry is specified;
- Phase 3b may proceed to Gram-matrix verification using this registry.

## 10. Next phase

Proceed to Phase 3b:

```text
Jmax=1 Gram matrix
```

Minimum deliverables:

1. numerical Gram matrix in the declared 14-label order;
2. symbolic/structural identity claims where available;
3. verification that the `Jmax=1/2` sub-block at indices `[0,1,2,4,5]` is the identity;
4. no transfer matrix or spectral claims until Phase 3c/3d.
