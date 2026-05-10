# Phase 3b — Jmax=1 Gram Matrix

## Temporal Mechanics / Yang-Mills finite bridge

Michael D. Heller  
SocioProphet Research  
Working Gram-matrix artifact. May 2026.

## 0. Scope

This artifact completes Phase 3b after the Phase 3a `Jmax=1` basis registry.

It verifies the Gram matrix of the declared 14-label basis under the normalized Haar/Peter-Weyl/Wigner physical inner product.

This artifact does **not** compute a transfer matrix, spectrum, vacuum decomposition, coefficient graph, beta trend, scale proxy, physical mass, continuum construction, or Clay-level result.

## 1. Basis order

The basis order is inherited from Phase 3a:

| Index | Label |
| ---: | --- |
| 0 | `Phi_000` |
| 1 | `Phi_100` |
| 2 | `Phi_010` |
| 3 | `Phi_200` |
| 4 | `Phi_110` |
| 5 | `Phi_111` |
| 6 | `Phi_020` |
| 7 | `Phi_210` |
| 8 | `Phi_211` |
| 9 | `Phi_120` |
| 10 | `Phi_121` |
| 11 | `Phi_220` |
| 12 | `Phi_221` |
| 13 | `Phi_222` |

The machine-readable basis registry is:

```text
manuscripts/lane-temporal-mechanics-jmax1/phase3a-basis-registry/basis_registry.json
```

## 2. Gram convention

The basis is normalized by the Peter-Weyl/Wigner convention. Therefore the physical Haar inner product satisfies:

```tex
\langle \Phi_a, \Phi_b\rangle = \delta_{ab}.
```

Equivalently, the Gram matrix in the Phase 3a order is:

```tex
G=I_{14}.
```

This is the intended Galerkin basis convention, not a transfer-matrix statement.

## 3. Matrix

The machine-readable matrix is stored in:

```text
manuscripts/lane-temporal-mechanics-jmax1/phase3b-gram-matrix/gram_matrix.json
```

It records:

```text
dimension = 14
matrix_type = identity
max_abs_offdiag = 0
max_abs_diag_minus_one = 0
```

## 4. Jmax=1/2 regression sub-block

The locked `Jmax=1/2` fixture embeds at indices:

```text
[0,1,2,4,5]
```

with labels:

```text
Phi_000, Phi_100, Phi_010, Phi_110, Phi_111
```

The submatrix is:

```tex
G_{1/2}=I_5.
```

This passes the Gram gate for the Phase 2 fixture.

## 5. Symmetry checks

The plaquette-swap symmetry from Phase 3a maps:

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

Because `G=I_14`, it is invariant under this swap permutation.

## 6. Phase 3b result

Phase 3b establishes:

```tex
G_{ab}=\delta_{ab}
```

for the declared 14-label `Jmax=1` basis.

It also establishes:

```tex
G_{[0,1,2,4,5]}=I_5
```

for the locked `Jmax=1/2` regression subset.

## 7. Non-claim box

This artifact does not claim:

- transfer matrix;
- temporal kernel entries;
- spectrum;
- vacuum decomposition;
- coefficient graph;
- beta trend;
- scale proxy;
- physical mass interpretation;
- continuum Yang-Mills construction;
- infinite-volume theorem;
- Clay-level result.

Positive claims:

- the declared `Jmax=1` basis is Gram-orthonormal under the normalized Peter-Weyl/Wigner convention;
- the machine-readable Gram matrix is `I_14` in the Phase 3a order;
- the `Jmax=1/2` regression sub-block is `I_5` at indices `[0,1,2,4,5]`;
- Phase 3c may proceed to truncation regression only after constructing the `Jmax=1` operator/matrix entries.

## 8. Next phase

Proceed to Phase 3c:

```text
Jmax=1 -> Jmax=1/2 truncation check
```

Minimum deliverables:

1. construct the `Jmax=1` operator/matrix entries in the declared 14-label order;
2. extract the `[0,1,2,4,5]` sub-block;
3. verify that the extracted sub-block reproduces the Phase 2 `Jmax=1/2` fixture;
4. no spectrum claim until Phase 3d.
