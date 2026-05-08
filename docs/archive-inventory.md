# Archive Inventory and Normalization Notes

Date: 2026-05-08

## Inputs inspected

- Uploaded archive: `yang-mills-program-archive(1).zip`.
- Drive/uploaded PDF: `ym_obstruction_survey_v0_18_1.pdf`.

## Critical normalization finding

The archive contains files named `.pdf`, but most of those files are technically ZIP bundles, not valid standalone PDF byte streams. Each bundle contains page images (`*.jpeg`), page text (`*.txt`), and a `manifest.json`. This matters because any downstream manuscript pipeline must not assume that those files can be passed directly to `pdftotext`, LaTeX/PDF validators, or journal preflight tools.

The v0.18.1 obstruction survey supplied by Drive/upload is a real LaTeX-produced PDF and should be treated as the authoritative Lane III survey artifact for the split/refactor pass.

## Archive reading order retained

1. `strong_coupling_lattice_mass_gap_seed_v0_14_4.pdf` - current theorem-track anchor, represented in the archive as a page/text ZIP bundle.
2. `strong_coupling_lattice_mass_gap_seed_v0_14_3.pdf` - prior submission-gate hardening build.
3. `strong_coupling_lattice_mass_gap_seed_v0_10a.pdf` - earlier seed useful for proof-evolution archaeology.
4. `yang_mills_program_part_two_proof_strategy_roadmap.pdf` - strategy and lane context.
5. `yang_mills_program_part_three_v3_7_full_running_manuscript.pdf` - working Part III manuscript.
6. `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.pdf` - K3/product-formula computational track.
7. `ym_obstruction_survey_v0_18_1.pdf` - actual Lane III obstruction survey, not included in the original archive inventory but supplied separately.

## Theorem-track constants to preserve

From the archive inventory and v0.18.1 survey:

- `M0 = 20e = 54.365636569180904...`
- `Dinc = 21`
- `a* = 0.4576898452957963`
- `qKP = 0.006311768836893038`
- `beta* = 0.006296889394074993`
- `Q(beta*) = qKP`
- Current fixed-spacing gap lower threshold: `m_beta = -log(M0 Q(beta))` inside the certified strong-coupling window.

## Source-of-truth policy

1. Treat PDFs and page bundles as distribution artifacts.
2. Recover or reconstruct Markdown/LaTeX source as the canonical form before further editing.
3. Keep exact v0.14.4 theorem cross-references unasserted until the exact source is recovered or reconstructed.
4. Use v0.18.1 as the Lane III survey content source, but split it before journal-style external review.
5. Do not dilute the non-claim box: fixed lattice spacing, SU(2), strong coupling, lattice units, no continuum reconstruction, no Clay claim.

## Immediate normalization tasks

- Recover v0.14.4 into line-addressable LaTeX/Markdown source.
- Recover v0.18.1 into editable LaTeX source, not merely extracted PDF text.
- Store raw extracted page text under a non-canonical evidence path if needed.
- Add checks that reject ZIP payloads with `.pdf` extensions in future archive packages.
- Add a manuscript manifest with title, version, status, claim scope, and source hash for each artifact.
