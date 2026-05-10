# Yang-Mills Capture Bundle 2026-05-09 — Ingest Report

Status: repo capture branch prepared.
Target repository: `SocioProphet/yang-mills`.
Target branch: `capture/2026-05-09-yang-mills-bundle`.

## Scope landed

This capture consolidates the 2026-05-09 Yang-Mills bundle into the repository's source-first layout. It lands the recovered manuscript text extracts, Phase 2 verification, Phase 3a basis registry, Phase 3b Gram matrix audit, Phase 3c truncation regression, Methodology Manifesto v0.2, and matching status-delta documents.

The reconstructed PDFs from the source bundle are distribution artifacts, not canonical source. They are therefore hash-registered in `artifact-manifest.json` and should be added through a binary-safe path: Git LFS, GitHub release assets, or the program artifact bucket.

## Normalization performed before capture

1. Replaced scratch-machine paths in executable scripts so generated JSON is written next to each script:
   - `basis-registry/registry_check.py` writes `basis_registry.json` next to the script.
   - `gram-matrix/gram.py` writes `gram_matrix.json` next to the script.
   - `truncation-regression/truncation.py` writes `truncation_check.json` next to the script.
2. Removed local scratch-path leakage from reconstructed text-extract headers.
3. Re-ran every included verification script after normalization.
4. Verified every reconstructed PDF in the source bundle begins with a valid `%PDF` header.

## Validation commands rerun

```bash
python3 manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/verify.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/registry_check.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/gram.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/truncation.py
```

## Validation outcome

- Phase 2 fixture verification: `ALL CHECKS PASS`.
- Phase 3a basis registry: `ALL CHECKS PASS`.
- Phase 3b Gram matrix: `ALL CHECKS PASS`.
- Phase 3c truncation regression: `ALL CHECKS PASS`.
- Reconstructed PDF header audit: 9 of 9 distribution PDFs start with `%PDF`.

## Claim boundary

This capture does not assert a continuum Yang-Mills construction, a weak-coupling theorem, an SU(N >= 3) theorem, an asymptotic-freedom trajectory theorem, quark confinement, or a Clay Millennium proof. It is a source/evidence capture for finite-cutoff temporal-mechanics computations and methodology discipline.

## Next executable work

The natural next technical lane is Phase 3d: construct the full `Jmax = 1` transfer matrix using the Phase 3a registry, Phase 3b orthonormalizers, and Phase 3c convention; then analyze the even-parity `10 x 10` block, odd-parity `4 x 4` block, vacuum decomposition, and sector graph.
