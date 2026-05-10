# Source Bundle README — Original Notes

This file preserves the original README shipped inside `yang mills capture bundle 2026 05 09.zip`. The repo ingest adapts storage policy by committing UTF-8 source/evidence files and hash-registering reconstructed PDF distribution artifacts for binary-safe storage.

---

# Yang-Mills Program — Capture Bundle 2026-05-09

This bundle consolidates six deliverables produced after PR #16 (Lane III v0.18.2/v0.18.3 audits, merged commit 4781279) into a single repo-layout drop.

The contents are partitioned cleanly so each item can be captured as one PR or split into multiple PRs at the user's discretion. None of these files conflict with files already on `main`.

## Contents at a glance

| Area | What | Files | Suggested PR scope |
|---|---|---|---|
| 1. Recovered sources | 9 reconstructed PDFs from zip-disguised-as-PDF originals + 9 text extracts + 1 archive-reconstruction note | 18 + 1 = 19 | "Recover corrupted source manuscripts (Lane I/Phase Two/Three/Four track sources)" |
| 2. Phase 2 | Jmax = 1/2 fixture independent verification, six checks all PASS | 3 + 1 = 4 | "Lane Temporal-Mechanics Jmax = 1/2 fixture verification" |
| 3. Phase 3a | Jmax = 1 basis registry + sector labels (14-entry registry) | 4 + 1 = 5 | "Lane Temporal-Mechanics Jmax = 1 basis registry (Phase 3a)" |
| 4. Phase 3b | Jmax = 1 Gram matrix (Monte Carlo, 14×14 block-diagonal verified) | 4 + 1 = 5 | "Lane Temporal-Mechanics Jmax = 1 Gram matrix (Phase 3b)" |
| 5. Phase 3c | Jmax = 1 → Jmax = 1/2 truncation regression, four checks all PASS at machine precision | 4 + 1 = 5 | "Lane Temporal-Mechanics Jmax = 1 truncation regression (Phase 3c)" |
| 6. Phase 4 | Methodology Manifesto v0.2 (9 disciplines, 5-witness validation) | 1 + 1 = 2 | "Methodology Manifesto v0.2 cross-track refresh" |

Total: **40 new files** across 6 manuscript subdirectories and `docs/`.

## Layout (drop-in to repo root)

```text
manuscripts/
  _recovered-sources/
    heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.{pdf,txt}
    yang_mills_program_part_two_proof_strategy_roadmap.{pdf,txt}
    yang_mills_program_part_three_v3_7_full_running_manuscript.{pdf,txt}
    yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.{pdf,txt}
    yang_mills_program_part_three_v3_13_response_diagnostics_full_running.{pdf,txt}
    yang_mills_program_part_three_v3_14_pair_lift_orbit25.{pdf,txt}
    yang_mills_program_part_three_v3_15_orbit25_projection_closure.{pdf,txt}
    yang_mills_program_part_three_v3_16_source_scalar_retriage.{pdf,txt}
    yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.{pdf,txt}
  lane-temporal-mechanics-jhalf-fixture/
    verification/
      source.md
      verify.py
      verify_output.txt
  lane-temporal-mechanics-jmax-one/
    basis-registry/
      source.md
      registry_check.py
      registry_check_output.txt
      basis_registry.json
    gram-matrix/
      source.md
      gram.py
      gram_output.txt
      gram_matrix.json
    truncation-regression/
      source.md
      truncation.py
      truncation_output.txt
      truncation_check.json
  methodology/
    manifesto-v0.2/
      source.md
docs/
  archive-reconstruction-2026-05-09.md
  lane-temporal-mechanics-jhalf-fixture-verification-status-delta.md
  lane-temporal-mechanics-jmax-one-3a-status-delta.md
  lane-temporal-mechanics-jmax-one-3b-status-delta.md
  lane-temporal-mechanics-jmax-one-3c-status-delta.md
  methodology-manifesto-v0.2-status-delta.md
```

## Capture order recommendation

If splitting into multiple PRs, the natural dependency order is:

1. Recovered sources (item 1) — independent; restores readable source corpus
2. Manifesto v0.2 (item 6) — process artifact; can land independently of the technical work
3. Phase 2 (item 2) — gates the Jmax = 1 work
4. Phase 3a (item 3) — depends on Phase 2 fixture being verified
5. Phase 3b (item 4) — depends on Phase 3a registry
6. Phase 3c (item 5) — depends on Phase 3b orthonormalizers; closes Jmax = 1 → Jmax = 1/2 regression

The 6 phases can also be captured as a single PR if the referee prefers monolithic review.

## Technical results summary

- **Phase 2 V_phi111 verification**: V_phi111 = 0.28492504932683558088... reproduced to 16+ figures by independent quadrature on v0.9.27 §19 explicit integral. K_111 = V² and K_111/λ_0 = normalized Phi_111 cascade verified at float64 noise floor.
- **Phase 3a registry**: 14 = 9 scalar + 4 vector + 1 tensor; 14 = 10 even-parity + 4 odd-parity by inversion-symmetry; truncation map [0,1,3,4,5] → 5 verified Jmax = 1/2 fixture labels.
- **Phase 3b Gram**: 14×14 Gram matrix block-diagonal at MC noise floor; analytical norms² match for all 14 entries; truncation gives 5×5 identity.
- **Phase 3c truncation**: A(1) entries reproduced to 9 figures (App A precision floor); A⊗A normalized spectrum to 16 figures (float64 noise); λ_0 = 1.854445494147494 vs target 1.854445494147492 (2.4×10⁻¹⁵). Convention finding documented: M_γ = exp(γ a_0), not exp(γ χ_{1/2}) as v0.9.27 §19 verbal text suggests.
- **Manifesto v0.2**: 9 disciplines, 5-witness validation. New disciplines: Convention-anchor pinning (8) and Independent-pipeline verification with precision floor (9).

## What this bundle does NOT contain

- Phase 3d (Jmax = 1 spectrum / vacuum / sector graph): in-progress, not yet a deliverable.
- Phase 5 (literal Varshalovich 3j/6j R-table): not started.
- Phase 6 (Lane VII v1.19 theta-graph Schatten allocation): not started.
- Any continuum, infinite-volume, weak-coupling, SU(N≥3), or Clay-relevance result.

The non-claim discipline of every individual deliverable is preserved.
