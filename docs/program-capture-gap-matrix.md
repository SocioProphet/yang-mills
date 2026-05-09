# Yang-Mills Program Capture Gap Matrix

Status: repository capture ledger.
Date: 2026-05-09.

## Purpose

This matrix records what the `SocioProphet/yang-mills` repository currently captures versus what was developed in the working program sequence. It is meant to prevent chat-work from remaining uncaptured and to keep proof claims, diagnostics, sidecars, and exports separated.

## Capture status legend

- **Captured**: present in repository as source/status/manifest content.
- **Partially captured**: present as planning/status/manifest, but canonical source/export is missing.
- **Missing**: not yet present in repository.
- **Parked**: intentionally not active, but should be preserved as a diagnostic/sidecar artifact.

## Repository seed status

| Area | Status | Repository evidence | Gap |
| --- | --- | --- | --- |
| README / claim policy | Captured | `README.md` | Needs periodic update as lanes mature. |
| Archive inventory | Captured | `docs/archive-inventory.md` | Needs recovered canonical sources. |
| v0.14.4 theorem anchor | Partially captured | README + archive inventory constants | Editable TeX/Markdown source missing; PDF/page-bundle source recovery still P0. |
| v0.18.1 obstruction survey | Partially captured | `manuscripts/v0.18.1-obstruction-survey/split-plan.md`; stochastic delta | Actual split manuscripts v0.18.2 external + companion missing. |
| Lane II theorem target | Captured initial target | `manuscripts/lane-ii-fiber-sensitive-sharpening/theorem-target.md` | Later Lane II v0.1-v0.5-B chain not captured as source. |
| PDF header guardrail | Captured | `scripts/check_pdf_headers.py` | Needs CI and manifest validation integration. |

## Lane-by-lane capture matrix

### Lane I — fixed-spacing theorem track

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| v0.14.4 theorem source | Missing canonical editable source | Recover/reconstruct TeX or Markdown source. |
| v0.14.4 PDF/page bundle evidence | Partially captured in archive inventory | Store evidence path and source-hash ledger. |
| Proof dependency graph | Missing | Add DLR, polymer convergence, KP, OS-Seiler, transfer-gap graph. |
| Claim-scope ledger | Missing | Add reviewer-facing non-claim ledger to theorem source. |

### Lane II — fiber-sensitive / screen-fiber precursor

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| Initial theorem target | Captured | Already in `manuscripts/lane-ii-fiber-sensitive-sharpening/theorem-target.md`. |
| Lane II v0.1 Peter-Weyl feasibility | Missing | Add as `manuscripts/lane-ii-fiber-sensitive-sharpening/v0.1/`. |
| Lane II v0.2 fundamental surface entropy gate | Missing | Add as versioned source. |
| Lane II v0.3 Catalan-dimension negative result | Missing | Add as versioned source. |
| Lane II v0.4 valuated behavioral spin-network candidate | Missing | Add as versioned source/patch. |
| Lane II v0.5-A/B Frobenius normalization audit | Missing | Add as diagnostic source. |
| Integration into Lane VII | Partially captured | Lane VII status records that Lane II supplies the bulk behavior. |

### Lane III — obstruction survey

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| v0.18.1 split plan | Captured | Present. |
| 2026 stochastic delta | Captured | Present. |
| v0.18.2 referee-conservative survey | Missing | Create external manuscript source. |
| Program-context companion | Missing | Create companion source. |
| Bibliography hardening | Missing | Add BibTeX and DOI ledger. |
| v0.14.4 cross-reference audit | Missing | Depends on theorem source recovery. |

### Lane IV — interface specification

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| Lane IV v0.1-FRI preservation ideals | Missing | Add source. |
| v0.2-E Bałaban interface matrix | Missing | Add source. |
| v0.2-F transfer-compatible RG schema | Missing | Add source. |
| v0.3-A/B/C bridge/RCP sequence | Missing | Add source. |
| v0.4-FRI consolidation | Missing | Add source and claim boundary. |
| Status | Parked | Repository should preserve as sidecar/interface-specification track. |

### Lane V — Brownian Holonomy diagnostic sidecar

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| v0.1-v0.5 Brownian Holonomy sequence | Missing | Add as diagnostic sidecar, not theorem-track. |
| Test III A/B/C decomposition | Missing | Preserve exact/rough/reconstruction separation. |
| Status | Parked | Do not promote to theorem-track without new proof-facing content. |

### Lane VI — spherical/simplicial regulator diagnostic

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| v0.1-FRI S^4 minimal triangulation diagnostic | Missing | Add source: `partial Delta^5`, `kappa_1=4`, `M0_simp=9e`. |
| v0.2-FRI barycentric subdivision failure | Missing | Add source: `kappa_1=14`, target revised to `kappa_1<=6`. |
| v0.3-FRI stacked/edge-regular audit | Missing | Add source: stacked refinement failure, near-edge-regular target. |
| Status | Parked | Regulator diagnostic only unless transfer/reflection structure is built. |

### Lane VII — holographic screen-invariant synthesis

| Artifact / topic | Status | Required capture |
| --- | --- | --- |
| Lane VII status ledger | Captured | `docs/lane-vii-status.md`. |
| Lane VII artifact manifest | Captured | `docs/lane-vii-artifact-manifest.md`. |
| Lane VII manuscript folder README | Captured | `manuscripts/lane-vii-holographic-invariants/README.md`. |
| v0.1 PDF/TeX export | Partially captured | Hashes recorded; source/PDF not yet committed. |
| v0.5 PDF/TeX export | Partially captured | Hashes recorded; source/PDF not yet committed. |
| v0.8 PDF/TeX export | Partially captured | Hashes recorded; source/PDF not yet committed. |
| v1.0 PDF/TeX export | Partially captured | Hashes recorded; source/PDF not yet committed. |
| v1.2 PDF/TeX export | Partially captured | Hashes recorded; source/PDF not yet committed. |
| Active theorem target | Captured in status | Cyclic Frobenius closure / subexponential cycle defect. |

## Export package capture policy

For each exportable artifact, repository capture should include:

```text
manuscripts/<lane>/<version>/source.tex
manuscripts/<lane>/<version>/README.md
manuscripts/<lane>/<version>/manifest.json
```

PDFs should be added through one of:

1. Git LFS;
2. GitHub Release assets;
3. artifact storage with SHA256 in repo manifest;
4. direct binary-safe commit path if available.

Do not rename ZIP/page bundles as PDFs. `scripts/check_pdf_headers.py` must pass on all committed `.pdf` files.

## Immediate capture issues

| Issue | Purpose |
| --- | --- |
| #4 | Capture Lane VII TeX/PDF exports as canonical repository artifacts. |
| TBD | Recover v0.14.4 editable source. |
| TBD | Capture Lane IV v0.4 consolidation. |
| TBD | Capture Lane V Brownian Holonomy sidecar. |
| TBD | Capture Lane VI spherical/simplicial diagnostic. |
| TBD | Split Lane III v0.18.2 external + companion. |

## Current program direction to preserve

The current proof-facing program direction is:

```text
Lane VII -> cyclic Frobenius closure -> KP insertion audit -> conditional certificate-wall sharpening.
```

The active theorem target is:

```tex
|Contr(\Gamma)| <= C(\gamma) e^{o(|\Gamma|)} \prod_\ell \sqrt{C_{n_\ell/2}}.
```

No repository text should state that this theorem has already been proved.

## Next recommended PRs

1. Import Lane VII TeX sources and release/binary PDF artifacts.
2. Capture Lane IV v0.4 consolidation as sidecar/interface-specification source.
3. Capture Lane VI v0.1-v0.3 spherical regulator diagnostic.
4. Capture Lane V Brownian Holonomy v0.5 diagnostic sidecar.
5. Recover v0.14.4 and v0.18.1 editable sources.
6. Create CI for PDF headers, TeX build, artifact manifest validation, and source hash receipts.
