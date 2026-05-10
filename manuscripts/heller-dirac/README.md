# Heller-Dirac manuscript sidecar

Status: program-context sidecar.  
Scope: formal mathematical scaffolding adjacent to the Yang-Mills program, not a theorem-track replacement and not a continuum mass-gap claim.

## Build order

The Heller-Dirac sequence is intentionally ordered as:

```text
(c) geometric foundation
-> (b) quantum-defect deformation
-> (a) relativistic / Dirac extension
```

This ordering keeps the manuscript disciplined. The geometric hydrogenic shell must be made precise before adding real-atom defect data, and the defect deformation must be clean before lifting to spinor/Dirac bookkeeping.

## Current source files

- `03-symplectic-coupling-reduction.md` — formalizes the SO(4) shell as `S^2_j x S^2_j`, the diagonal SU(2) moment map, the coupling-orbit foliation, the quantization calculation producing `D^(ell)`, the Clebsch-Gordan transition matrix, and the corrected Tetryonics-to-geometry dictionary.

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

1. `04-quantum-defect-deformation.md` — radial-action deformation, Rydberg-Ritz energy assignment, and SO(4) -> SO(3) symmetry breaking.
2. `05-dirac-kappa-extension.md` — spinor lift, `kappa` labels, positive/negative energy branches, and particle-zoo bookkeeping.
3. `06-dictionary-and-tests.md` — basis-conversion tests, low-`n` examples, and a finite-table audit against Clebsch-Gordan coefficients.
