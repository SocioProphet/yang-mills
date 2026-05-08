# Yang-Mills Program Backlog

Status: running backlog seeded from the v0.18.1 review and Lane II planning pass.

## Immediate priority

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
- Add an even stronger non-claim box.
- Add a mapping table back to the external obstruction taxonomy.

## Evidence and tooling

- Add `scripts/check_pdf_headers.py`.
- Add `scripts/extract_page_bundle_text.py` for archive bundles.
- Add `scripts/compute_q_beta.py` to reproduce `Q(beta)`, `beta*`, and geometry-wall estimates.
- Add `scripts/build_manuscripts.sh` once LaTeX sources exist.
- Add GitHub Actions for source lint, PDF header validation, and manuscript build receipts.

## Research backlog

### Lane II - fiber-sensitive sharpening

1. Surface entropy bound for rectangular loops.
2. Boundary-uniform constants for transfer-gap observables.
3. Representation-admissible SU(2) surface grammar.
4. Multiplicity bound from polymers to surface cores.
5. Cancellation-aware weighted estimate.
6. Improved certificate-window calculation.

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

## Done in this seed pass

- Identified `SocioProphet/yang-mills` as the active upstream repository.
- Confirmed the archive contains `.pdf`-named ZIP page bundles.
- Confirmed the separately supplied v0.18.1 artifact is the real Lane III PDF.
- Seeded a repository structure and branch for program work.
- Added the v0.18.1 split plan.
- Added the Lane II theorem target.
- Added the stochastic Yang-Mills 2026 literature delta.
