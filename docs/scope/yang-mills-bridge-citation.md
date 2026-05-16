# yang-mills ↔ HG-MTH-007 Citation Anchor

The yang-mills repository operates as the primary consumer of `[HG-MTH-007 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]`, the Universal Bridge specification for the Yang-Mills gauge domain.

## Bridge positioning

`HG-MTH-007` specifies the Yang-Mills bridge factorization:

```text
B_YM(G) = (M_YM, R_YM, A_YM)
```

with compact simple gauge group `G`:

- `M_YM(G)` — classical Yang-Mills action minimum modulo gauge;
- `R_YM(G)` — quantum spectral residual above the vacuum;
- `A_YM` — compiled apex obstruction: constructive QFT existence, continuum limit, and spectral-action realization.

The yang-mills v0.14.4 work sits at Component 2: continuum-limit lattice-side apparatus. It is method-grade apparatus, not Clay-grade resolution.

## Per-lane bridge positioning

| Lane | Role under HG-MTH-007 |
|---|---|
| Lane I — transfer matrix construction | Component 2 method-grade apparatus; lattice-level OS-positive Hilbert-space structure |
| Lane II — mass gap from coupling smallness | Component 2 method-grade apparatus; fixed `a > 0`, `beta < beta*` gap result |
| Lane III — gauge fixing | Component 2 method-grade apparatus; lattice-level gauge-boundary discipline |
| Lane IV — cross-checks | Component 2 audit / consistency apparatus |

All four lanes operate at fixed lattice spacing. None positions itself at the continuum apex.

## Component 1 and Component 3 status

The current yang-mills repo does not claim Component 1 or Component 3 closure:

- Component 1 — constructive QFT / OS axioms: not entered by v0.14.4.
- Component 3 — spectral-action realization: structural context only, not current apparatus.

Heller-Dirac citations used by HG-MTH-007 give this context:

```text
[HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-003 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-006 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-010 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```

Per `A-HD-FT-001`, axioms are not construction. Per `A-HD-NC-001`, reformulation is not proof. Per `A-HD-HA-001`, Hopf scaffold encoding is not analytic-control proof. Per `A-HD-SP-001`, analog spectral data is not target spectral data.

## Boundary preservation

Per `[A-HG-MTH-006 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]`, component apparatus is not Clay-grade Yang-Mills resolution.

The following non-claims are preserved:

- The lattice transfer-matrix gap is not claimed to survive the continuum limit.
- The narrow-scope theorem is not claimed to extend to `beta >= beta*`.
- The narrow-scope theorem is not claimed to extend to `SU(N)` for `N >= 3`.
- The spectral action is not claimed to construct the quantum theory.
- The Connes-Kreimer Hopf scaffold is not claimed to prove non-perturbative renormalizability.
- The four-lane decomposition is not claimed to address all three component obstructions.
- v0.14.4 is not claimed to be a Clay-grade Yang-Mills mass-gap resolution.

## Citation form

```text
[HG-MTH-007 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[A-HG-MTH-006 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-003 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-006 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-010 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-FT-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-HA-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-NC-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-SP-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```
