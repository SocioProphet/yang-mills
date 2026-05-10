# Heller-Dirac manuscript sidecar

Status: program-context sidecar.  
Scope: formal mathematical scaffolding adjacent to the Yang-Mills program, not a theorem-track replacement and not a continuum mass-gap claim.

## Build order

The Heller-Dirac sequence is intentionally ordered as:

```text
(c) geometric foundation
-> (b) quantum-defect deformation
-> (a) relativistic / Dirac extension
-> (t) finite-table audit and regression checks
```

This ordering keeps the manuscript disciplined. The geometric hydrogenic shell must be made precise before adding real-atom defect data, the defect deformation must be clean before lifting to spinor/Dirac bookkeeping, and the finite tables must guard the basis-change claims.

## Current source files

- `03-symplectic-coupling-reduction.md` — formalizes the SO(4) shell as `S^2_j x S^2_j`, the diagonal SU(2) moment map, the coupling-orbit foliation, the quantization calculation producing `D^(ell)`, the Clebsch-Gordan transition matrix, and the corrected Tetryonics-to-geometry dictionary.
- `addendum-sum-difference-hyperbolic-bridge.md` — clarifies the diagonal and anti-diagonal variables `L=J_++J_-` and `A=J_+-J_-`, including the hyperbolic/scattering bridge.
- `04-quantum-defect-deformation.md` — treats quantum defects as radial-action phase defects attached to `ell` channels, not as nonintegral angular orbit labels.
- `05-dirac-kappa-extension.md` — lifts orbital labels to Dirac `kappa` channels and separates branch bookkeeping from later field-level particle taxonomy.
- `06-dictionary-and-tests.md` — records finite sanity checks, failure traps, and acceptance criteria.
- `07-cg-audit-n2-n4.md` — generated finite Clebsch-Gordan tables and exact projector checks for `n=2,3,4`.

## Reproducibility script

- `../../scripts/heller_dirac_cg_audit.py` — regenerates the small-`n` Clebsch-Gordan tables and verifies fixed-`M` projector completeness, idempotence, and orthogonality exactly with SymPy.

Expected command from repository root:

```bash
python scripts/heller_dirac_cg_audit.py --n 2 3 4
```

## Claim boundary

This lane may introduce interpretation, notation, and formal scaffolding. It must not silently alter theorem-track claims elsewhere in this repository.

Explicit non-claims:

- no Yang-Mills mass-gap theorem;
- no continuum limit construction;
- no Clay proof;
- no first-principles prediction of empirical quantum defects;
- no assertion that Tetryonics cells are themselves irreducible orbital multiplets;
- no replacement of SU(2) integrality by nonintegral defect labels.

## Next files planned

1. Add product-cell defect matrices for `n=3,4` in symbolic delta form.
2. Add a CI job if the repository decides to accept SymPy as a development dependency.
3. Decide whether Heller-Dirac stays here as a sidecar or moves to a dedicated repository while retaining this sidecar as a pointer.
