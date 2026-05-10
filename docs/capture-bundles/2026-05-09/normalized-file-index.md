# Yang-Mills Capture Bundle 2026-05-09 — Normalized File Index

Source: `yang-mills-capture-normalized-2026-05-09.zip`.
SHA-256: `4fd1895ed5b603863a40f00f0697e493fa0455e2f13a88cca60a6605938a29a0`.
Bytes: `8319272`.

This index records the normalized bundle shape and intended repository expansion policy. The full per-artifact hash ledger for reconstructed PDFs and recovered text extracts is in `artifact-manifest.md`.

## Bundle inventory by class

| Class | Count | Repo handling |
|---|---:|---|
| Markdown/source reports | 15 | status/capture docs are committed in this PR; long manuscript sources are indexed for expansion |
| Python verification scripts | 4 | indexed for deterministic expansion by `scripts/ingest_yang_mills_capture_2026_05_09.py` |
| JSON fixtures/results | 4 | indexed for deterministic expansion by ingest script |
| Verification output logs | 4 | indexed for deterministic expansion by ingest script |
| Recovered text extracts | 9 | hash-registered; intended repo paths under `manuscripts/_recovered-sources/` |
| Reconstructed PDFs | 9 | distribution artifacts only; keep binary-safe via Git LFS, release assets, or artifact bucket |

## UTF-8 files intended for repository expansion

```text
docs/archive-reconstruction-2026-05-09.md
docs/capture-bundles/2026-05-09/artifact-manifest.json
docs/lane-temporal-mechanics-jhalf-fixture-verification-status-delta.md
docs/lane-temporal-mechanics-jmax-one-3a-status-delta.md
docs/lane-temporal-mechanics-jmax-one-3b-status-delta.md
docs/lane-temporal-mechanics-jmax-one-3c-status-delta.md
docs/methodology-manifesto-v0.2-status-delta.md
manuscripts/_recovered-sources/heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_13_response_diagnostics_full_running.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_14_pair_lift_orbit25.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_15_orbit25_projection_closure.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_16_source_scalar_retriage.txt
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_7_full_running_manuscript.txt
manuscripts/_recovered-sources/yang_mills_program_part_two_proof_strategy_roadmap.txt
manuscripts/_recovered-sources/yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.txt
manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/source.md
manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/verify.py
manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/verify_output.txt
manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/basis_registry.json
manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/registry_check.py
manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/registry_check_output.txt
manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/source.md
manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/gram.py
manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/gram_matrix.json
manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/gram_output.txt
manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/source.md
manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/source.md
manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/truncation.py
manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/truncation_check.json
manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/truncation_output.txt
manuscripts/methodology/manifesto-v0.2/source.md
```

## Distribution PDFs hash-registered but not expanded by ingest script

```text
manuscripts/_recovered-sources/heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_13_response_diagnostics_full_running.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_14_pair_lift_orbit25.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_15_orbit25_projection_closure.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_16_source_scalar_retriage.pdf
manuscripts/_recovered-sources/yang_mills_program_part_three_v3_7_full_running_manuscript.pdf
manuscripts/_recovered-sources/yang_mills_program_part_two_proof_strategy_roadmap.pdf
manuscripts/_recovered-sources/yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.pdf
```

## Local ingest dry-run summary

Using the normalized bundle with SHA `4fd1895ed5b603863a40f00f0697e493fa0455e2f13a88cca60a6605938a29a0`, the conservative ingest plan writes 32 UTF-8 files and skips 13 files: 9 reconstructed PDFs plus 4 already-preserved capture README/report files.

Expected write classes:

```text
markdown: 11
text-extract: 9
json: 4
script: 4
verification-output: 4
```

Expected skip classes:

```text
distribution-pdf: 9
markdown: 4
```
