# Yang-Mills Program

This repository is the working home for the SocioProphet Yang-Mills program artifacts: fixed-spacing strong-coupling SU(2) theorem work, obstruction-survey work, fiber-sensitive sharpening, interface-specification planning, and the Lane VII holographic screen-invariant synthesis branch.

## Current status

The current theorem-track anchor is `strong_coupling_lattice_mass_gap_seed_v0_14_4`, described in the archive inventory as a CMP pre-submission consolidation. Its scoped claim is deliberately narrow:

- Gauge group: SU(2).
- Lattice: Wilson lattice gauge theory on Z^4.
- Lattice spacing: fixed `a > 0`.
- Coupling window: `beta < beta* = 0.006296889394074993`.
- Output: positive transfer gap above the vacuum in the infinite-volume gauge-invariant Osterwalder-Seiler reflection-positive Hilbert space.

This repository must preserve the non-claim discipline: this is not a continuum construction, not a Clay Millennium proof, not a weak-coupling theorem, not an SU(N >= 3) theorem, and not an asymptotic-freedom trajectory result.

## Active program direction

Lane VII is now the synthesis/proof-target lane for the current program. It reframes the Lane II polymer sharpening work as a Wilson-screen fiber entropy problem and reduces the active wall-moving candidate to a global spin-network channel aggregation theorem.

Current Lane VII status:

- Primary invariant: activity-weighted Wilson-screen fiber entropy.
- Proof architecture: screen-transfer spectral-radius majorant.
- Closure hierarchy: `q_op <= q_Frob <= q_Cat`.
- Proved partial result: tree-Frobenius aggregation theorem under normalized tree-tensor hypotheses.
- First cyclic test: the two-rank-2 cycle saturates Frobenius scale and demotes global operator closure.
- Main open theorem: Frobenius closure for arbitrary cyclic channel graphs / subexponential cycle defect in unitary Temperley-Lieb/Wigner normal form.
- Candidate wall if Frobenius closure and KP insertion both succeed: `beta_Frob ~= 0.00735851805`.

This is a conditional research target, not a proved extension of v0.14.4.

## Program lanes

- **Lane I - fixed-spacing theorem track:** v0.14.4 source recovery, referee hardening, exact cross-reference audit, and submission packaging.
- **Lane II - fiber-sensitive quantitative sharpening:** precursor lane for screen-fiber entropy; studies boundary-fiber-sensitive surface, representation, valuation, and cancellation estimates.
- **Lane III - obstruction survey:** split v0.18.1 into a referee-conservative obstruction-taxonomy manuscript and a separate program-context companion.
- **Lane IV - interface specification:** define projection/preimage preservation requirements for any future strong-coupling/weak-coupling or lattice/continuum interface.
- **Lane V - Brownian Holonomy diagnostic sidecar:** parked diagnostic; preserves exact-versus-approximate holonomy and reconstruction cautions.
- **Lane VI - spherical/simplicial regulator diagnostic:** parked diagnostic; tests regulator-dependence of incidence and entropy constants, especially triangulated S^4.
- **Lane VII - holographic screen-invariant synthesis:** active synthesis/proof-target lane centered on screen fiber entropy, spin-network closure, and Frobenius aggregation.

## Repository policy

1. Keep theorem claims separated from survey claims, computational evidence, program vocabulary, and speculative scaffolds.
2. Every mathematical claim must be traceable to a manuscript source, a proof object, or an external reference.
3. Every non-load-bearing scaffold must be marked as removable.
4. Use Markdown/LaTeX sources as the canonical working artifacts. PDFs are distribution builds, not source of truth.
5. Keep public-review artifacts referee conservative unless the file is explicitly marked as program-context material.
6. Conditional Lane VII wall-movement candidates must remain explicitly conditional until Frobenius closure and KP insertion are proved.

## Initial seeded materials

- `docs/archive-inventory.md` - archive inventory and normalization notes.
- `docs/literature/stochastic-yang-mills-2026-delta.md` - current literature delta for the stochastic-quantization wall.
- `manuscripts/v0.18.1-obstruction-survey/split-plan.md` - how to split v0.18.1 into external and internal/program tracks.
- `manuscripts/lane-ii-fiber-sensitive-sharpening/theorem-target.md` - first concrete Lane II theorem target.
- `docs/backlog.md` - running backlog for the next manuscript passes.
- `docs/lane-vii-status.md` - current Lane VII program-state ledger.
- `docs/lane-vii-artifact-manifest.md` - Lane VII export manifest and artifact hashes.
