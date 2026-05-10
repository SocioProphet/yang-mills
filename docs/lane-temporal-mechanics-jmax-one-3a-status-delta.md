# Lane Temporal-Mechanics Jmax = 1 Phase 3a — Status Delta

**Track**: `docs/lane-temporal-mechanics-jmax-one-3a-status-delta.md`
**Date**: 2026-05-09
**Predecessor**: Phase 2 — Jmax = 1/2 fixture independent verification (referee-pending).

## What this delta records

Phase 3a — Jmax = 1 basis registry + sector labels — is locked at the structural enumeration layer. The 14 basis labels at Jmax = 1 are enumerated, the dimension count matches Part Two v2.9 §F.7's declared 14, sector tags are assigned (9 scalar + 4 vector + 1 tensor), inversion-symmetry parities are derived, the implied 14 = 10 + 4 block decomposition is recorded, and the explicit truncation map Jmax = 1 → Jmax = 1/2 (indices [0, 1, 3, 4, 5]) is fixed.

A machine-readable `basis_registry.json` is exported for direct import by downstream Phase 3b (Gram), Phase 3c (truncation check), and Phase 3d (spectrum) code.

## Phase plan position

Execution order **2 → 3a → 3b → 3c → 4 → 3d → 5 → 6**.

| Phase | Status |
|---|---|
| 1 — Lane III v0.18.3 cross-reference audit | Closed (PR #16 merged) |
| 2 — Jmax = 1/2 fixture independent verification | Referee-pending |
| **3a — Jmax = 1 basis registry + sector labels** | **This delta — referee-pending** |
| 3b — Jmax = 1 Gram matrix | Pending |
| 3c — Jmax = 1 → Jmax = 1/2 truncation check | Pending |
| 4 — Manifesto v0.2 cross-track refresh | Scheduled after 3c |
| 3d — Jmax = 1 spectrum + vacuum + sector graph | Scheduled after 4 |
| 5 — Literal Varshalovich 3j/6j R-table | Scheduled after 3d |
| 6 — Lane VII v1.19 theta-graph Schatten | Scheduled after 5 |

## What changed in the program by this deliverable

Before Phase 3a, the basis structure at Jmax = 1 was named at the dimension level (v2.9 §F.7: "all 14 dimensions") but no enumerated registry existed. After Phase 3a, the program has:

- A canonical 14-entry basis registry with consistent (j_P, j_Q, ℓ) labeling
- A canonical iteration ordering (j_Q outer / j_P inner / ℓ innermost) consistent with the locked Jmax = 1/2 fixture
- A canonical `basis_registry.json` data file usable by Phase 3b/3c/3d code without ambiguity
- A precomputed truncation index map [0, 1, 3, 4, 5] specifying exactly which Jmax = 1 rows/columns must reproduce the Phase 2 verified fixture
- A structural decomposition 14 = 10 + 4 by inversion-symmetry parity that constrains the Jmax = 1 transfer-matrix block structure before any numerical work

## What this deliverable does NOT advance

Per Phase 3a source.md §8 sealed non-claim box, this deliverable does not produce any Gram matrix entry, orthonormal-basis coefficient, transfer-matrix entry, eigenvalue, mass scale, or β-trend interpretation. It is a labeling-only deliverable.

## Items unblocked by Phase 3a

1. **Phase 3b (Jmax = 1 Gram matrix)** can now import the canonical `(j_P, j_Q, ℓ)` registry and compute Gram matrix entries against a fixed indexing scheme.
2. **Phase 3c (Jmax = 1 → Jmax = 1/2 truncation check)** has its regression target defined: when Phase 3b/3d code restricts to indices [0, 1, 3, 4, 5], the resulting 5 × 5 transfer matrix must match the Phase 2 verified fixture exactly.
3. **Phase 3d (spectrum)** has the block structure 14 = 10 + 4 already constrained by inversion-symmetry parity, which simplifies the eigenvalue computation into two independent blocks (10 × 10 even + 4 × 4 odd).
4. **Phase 5 (literal 3j/6j R-table)** has the basis labels for which R coefficients are required: the off-diagonal Phi_111-related entries plus the higher-(j_P, j_Q) ℓ ≠ 0 entries (Phi_211, Phi_121, Phi_221, Phi_222).

## Successor pointer

Phase 3b: Jmax = 1 Gram matrix. The 14 × 14 Gram matrix $G_{ab} = \langle \Phi_a, \Phi_b \rangle_{\text{Haar}}$ in the diagonal-Ad-invariant basis. Block-diagonal structure expected by parity (10 + 4 separate blocks; off-block entries vanish by orthogonality of inequivalent Ad reps).

## PR positioning

Suggested PR action: open a new PR adding `manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/` (with `source.md`, `registry_check.py`, `registry_check_output.txt`, `basis_registry.json`) plus this delta to `docs/`. Reference Phase 2 PR for verification-fixture provenance.

## No-claim discipline

This delta records a structural-enumeration deliverable. It does not claim any new theorem, any new derivation, or any change to the technical content of v2.9 or v0.9.27. The Phase 3a registry is a pre-numerical labeling step.
