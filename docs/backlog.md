# Yang-Mills Program Backlog

Status: running backlog seeded from the v0.18.1 review, Lane II planning pass, and Lane VII synthesis capture.

## Immediate priority

### P0 - Capture Lane VII source and export artifacts

- Store Lane VII canonical TeX sources under `manuscripts/lane-vii-holographic-invariants/`.
- Preserve generated PDFs as distribution artifacts via a binary-safe path: Git LFS, release assets, or a future artifact bucket.
- Keep `docs/lane-vii-status.md` as the current program-state ledger.
- Keep `docs/lane-vii-artifact-manifest.md` as the export/hash ledger.
- Add build receipts and source hashes for every Lane VII export.
- Do not claim the Frobenius closure theorem or a moved KP wall until the cyclic-channel theorem and KP insertion audit are proved.

### P0 - Recover editable sources

- Recover or reconstruct editable LaTeX/Markdown source for `strong_coupling_lattice_mass_gap_seed_v0_14_4`.
- Recover or reconstruct editable LaTeX/Markdown source for `ym_obstruction_survey_v0_18_1`.
- Add source hashes, build commands, and PDF build receipts.
- Add a preflight check that fails any `.pdf` file whose header is not `%PDF`.

### P0 - Split v0.18.1

- Create `v0.18.2-external` as a referee-conservative obstruction taxonomy.
- Move Hopf-shell, Einstein-Heller, and neural-operator material into a program-context companion.
- Rewrite the abstract so it does not require shell vocabulary to understand the mathematical contribution.
- Move image/preimage discipline before scaffold discussion.
- Add a claim-scope ledger before the introduction.

### P0 - Lane VII cyclic Frobenius closure target

- Attempt the Frobenius Closure Theorem for arbitrary cyclic channel graphs:
  `|Contr(Gamma)| <= C(gamma) e^{o(|Gamma|)} prod_l sqrt(C_{n_l/2})`.
- Start with beta_1 = 1 and beta_1 = 2 cyclic channel cases.
- Use spanning tree plus Schatten-Hölder strategy.
- Verify unitary Temperley-Lieb/Wigner normal form against the Reisenberger/Wilson amplitude.
- Run the KP insertion audit only after closure is established.
- Define the projection-like Wilson-screen object `Pi_screen : H_bulk -> H_screen`, including its domain, codomain, norm choice, recoupling compatibility, residual leakage object `E`, and non-claim boundary. This follows the Baez-Taylor finite-N projection bridge captured under `docs/program-context/baez-taylor-finite-n-projection-bridge.md`.

### P0 - Lane II theorem target A

- Define `S_A(gamma)` for rectangular Wilson loops.
- Prove a crude but explicit surface-growth bound with `M_surf < M0` if possible.
- Prove a transfer-gap compatibility lemma showing where `M_surf` replaces `M0`.
- Keep representation-admissible and cancellation-aware refinements as later theorem targets.

## Manuscript hardening

### v0.14.4 theorem-track hardening

- Replace image/text bundle dependence with canonical source.
- Verify every theorem, lemma, proposition, and constant against source.
- Add exact cross-references for the v0.18.2 external survey.
- Add a proof-dependency graph: DLR limit, polymer convergence, KP verification, connected-support decay, OS-Seiler Hilbert space, transfer gap.
- Add a reviewer-facing non-claim ledger near the front.

### Lane VII framework/theorem hardening

- Convert Lane VII v1.2 into canonical repository source.
- Add theorem/proposition/conjecture numbering stable across builds.
- Add a claim ledger distinguishing proved tree-Frobenius aggregation from open cyclic Frobenius closure.
- Add a source-reference ledger for Reisenberger, Aroca-Fort-Gambini, Freidel-Hnybida, Temperley-Lieb/Schur-Weyl, Kotecky-Preiss, and Osterwalder-Seiler.
- Add a proof-gate matrix: normalized vertex hypothesis, cycle defect bound, boundary prefactor uniformity, mixed-sector tail, KP insertion.

### v0.18.2 external survey hardening

- Preserve obstruction taxonomy.
- Remove program-specific vocabulary from the public mathematical spine.
- Update stochastic quantization discussion with 2026 3D gauge-covariant renormalisation uniqueness.
- Treat d = 4 as a current-method/literature wall, not as an impossibility theorem.
- Add citation-grade BibTeX.
- Add explicit distinction between failure of a certificate and nonconvergence.

### Program-context companion

- Preserve the Hopf-shell scaffold as non-load-bearing taxonomy.
- Preserve the Einstein-Heller typed projection/fiber analogy as methodology only.
- Preserve neural operators as computational diagnostics only.
- Preserve the Baez-Taylor finite-N projection bridge as methodology for explicit projection/admissibility laws; do not promote it to theorem-track machinery.
- Add an even stronger non-claim box.
- Add a mapping table back to the external obstruction taxonomy.

## Evidence and tooling

- Add `scripts/check_pdf_headers.py`.
- Add `scripts/extract_page_bundle_text.py` for archive bundles.
- Add `scripts/compute_q_beta.py` to reproduce `Q(beta)`, `beta*`, and geometry-wall estimates.
- Add `scripts/build_manuscripts.sh` once LaTeX sources exist.
- Add `scripts/build_lane_vii.sh` for Lane VII source compilation.
- Add `scripts/hash_artifacts.py` and `scripts/validate_artifact_manifest.py`.
- Add GitHub Actions for source lint, PDF header validation, manuscript build receipts, and artifact manifest validation.

## Research backlog

### Lane II - fiber-sensitive sharpening

1. Surface entropy bound for rectangular loops.
2. Boundary-uniform constants for transfer-gap observables.
3. Representation-admissible SU(2) surface grammar.
4. Multiplicity bound from polymers to surface cores.
5. Cancellation-aware weighted estimate.
6. Improved certificate-window calculation.
7. Integrate Lane VII closure findings if Frobenius closure is proved.

### Lane III - obstruction taxonomy

1. Referee-conservative split.
2. Bibliography cleanup.
3. Section 6 stochastic update.
4. Line-checked v0.14.4 references.
5. Referee cover note.
6. arXiv category strategy.

### Lane IV - interface specification

1. Boundary-data package `B_beta` schema.
2. Preservation ideals: gauge, locality, reflection positivity, observable compatibility, evidence.
3. Explicit statement of what v0.14.4 already supplies.
4. Explicit statement of what no fixed-spacing theorem can supply.
5. Compatibility matrix against Balaban-style RG, AQFT, pAQFT/factorization algebras, and lattice continuum comparison.
6. Preserve Lane IV v0.4 bridge/RCP consolidation as a side artifact.

### Lane V - Brownian Holonomy sidecar

1. Preserve v0.5 as diagnostic/cautionary sidecar.
2. Keep exact polygonal holonomy, stochastic-loop approximation, and lattice-to-continuum reconstruction separated.
3. Do not promote to theorem-track without new proof-facing content.

### Lane VI - spherical/simplicial regulator diagnostic

1. Preserve `S^4` triangulation diagnostic results.
2. Record minimal triangulation result: `partial Delta^5`, `kappa_1=4`, local `M0_simp=9e`.
3. Record barycentric subdivision failure: `kappa_1=14`.
4. Record refined target: near-edge-regular `kappa_1 <= 6` families.
5. Keep as regulator diagnostic unless reflection/transfer infrastructure is built.

### Lane VII - holographic screen-invariant synthesis

1. Store v0.1, v0.5, v0.8, v1.0, and v1.2 artifacts.
2. Define the screen-projection specification `Pi_screen : H_bulk -> H_screen` before using projection language in theorem-track drafts.
3. Attempt cyclic Frobenius closure.
4. If cyclic closure succeeds, perform KP insertion audit.
5. If cyclic closure fails at Catalan scale, classify cubic Lane VII as non-wall-moving by this route.
6. If cyclic closure is Frobenius with subexponential defect, compute improved certificate window.

## Done in this seed pass

- Identified `SocioProphet/yang-mills` as the active upstream repository.
- Confirmed the archive contains `.pdf`-named ZIP page bundles.
- Confirmed the separately supplied v0.18.1 artifact is the real Lane III PDF.
- Seeded a repository structure and branch for program work.
- Added the v0.18.1 split plan.
- Added the Lane II theorem target.
- Added the stochastic Yang-Mills 2026 literature delta.
- Added Lane VII status and artifact manifest in follow-up capture work.
