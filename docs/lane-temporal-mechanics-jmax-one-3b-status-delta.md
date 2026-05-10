# Lane Temporal-Mechanics Jmax = 1 Phase 3b — Status Delta

**Track**: `docs/lane-temporal-mechanics-jmax-one-3b-status-delta.md`
**Date**: 2026-05-09
**Predecessor**: Phase 3a — Jmax = 1 basis registry (referee-pending).

## What this delta records

Phase 3b — Jmax = 1 Gram matrix — is locked at the inner-product structure layer. The 14×14 Gram matrix in the Phase 3a natural polynomial basis is computed by Monte Carlo Haar integration (N = 2×10⁶ samples). It is verified to be diagonal at MC noise floor, with:

- Block-decoupling by inversion-symmetry parity (even 10 ⊥ odd 4): max off-block 9.8×10⁻⁴
- Block-decoupling by (j_P, j_Q) Peter-Weyl inequivalence: max off-block 1.5×10⁻³
- Within-rep ℓ-orthogonality: max off-diagonal 4.7×10⁻⁴
- Truncation to indices [0, 1, 3, 4, 5] yields the 5×5 identity Gram matching Jmax = 1/2 fixture: max error 1.2×10⁻³

All within 3× MC noise floor of 7×10⁻⁴.

Diagonal entries match closed-form analytical norms² for all 14 entries:
- 10 entries are unit-norm by character orthonormality / v0.9.27 §19 Phi_111 normalization
- 4 raw entries (Phi_211, Phi_121, Phi_221, Phi_222) have normalizers 4√2, 4√2, 8√3, 12/√5 respectively, all matching MC values to 3-4 figures

A machine-readable `gram_matrix.json` is exported for downstream import.

## Phase plan position

Execution order **2 → 3a → 3b → 3c → 4 → 3d → 5 → 6**.

| Phase | Status |
|---|---|
| 1 | Closed (PR #16) |
| 2 | Referee-pending |
| 3a | Referee-pending |
| **3b** | **This delta — referee-pending** |
| 3c | Pending |
| 4 | Scheduled |
| 3d, 5, 6 | Scheduled |

## What changed by this deliverable

Before Phase 3b, the basis labels were enumerated (Phase 3a) but no inner-product values existed. After Phase 3b:

- The 14 basis polynomial forms have closed-form norms² and orthonormalizers.
- The Gram matrix is verified block-diagonal, confirming Phase 3a's parity / rep / ℓ decomposition operationally.
- The 5×5 truncation regression on the Gram matrix is verified — first concrete numerical reduction from Jmax = 1 to the verified Jmax = 1/2 fixture.

## What this deliverable does NOT advance

Per Phase 3b source.md §7 sealed non-claim box, this deliverable does not produce any transfer-matrix entry, eigenvalue, V_phi111 reproduction, or β-trend interpretation. It is Gram-only.

## Items unblocked by Phase 3b

1. **Phase 3c (truncation regression)** can now use the verified Gram-block truncation as the structural foundation for the transfer-matrix truncation check.
2. **Phase 3d (spectrum)** has the explicit orthonormalized basis forms ready for transfer-matrix entry computation.
3. **Phase 5 (3j/6j R-table)** has the analytical norm² targets (1/32, 1/192, 5/144) for cross-validating the literal Wigner-Eckart spherical-tensor construction.

## Successor pointer

Phase 3c: Jmax = 1 → Jmax = 1/2 truncation regression. Computes selected Jmax = 1 transfer-matrix entries on the truncation indices [0, 1, 3, 4, 5] and verifies they reproduce the Phase 2 fixture targets (V_phi111 = 0.28492504932..., scalar A entries, λ_0 = 1.854445...).

## No-claim discipline

This delta records a Gram-structure deliverable. It does not claim any new theorem, derivation, or technical result beyond the inner-product structure operations.
