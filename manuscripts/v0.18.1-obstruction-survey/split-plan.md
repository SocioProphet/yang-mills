# v0.18.1 Obstruction Survey Split Plan

Status: planning document for Lane III hardening.

## Decision

Split v0.18.1 into two artifacts before external mathematical-physics review.

1. **Referee-conservative obstruction taxonomy.** This is the journal/arXiv-facing survey. It should minimize internal program vocabulary and foreground standard constructive-QFT, lattice-gauge, stochastic-quantization, loop-equation, AQFT, and RG language.
2. **Program-context shell/interface companion.** This preserves the Hopf-shell, Einstein-Heller, and neural-operator interface language as a research-program alignment document. It can be public later, but it should not be forced to carry the first external-review pass.

The split does not reject the shell scaffold. It assigns the scaffold to the right audience and protects the technical obstruction taxonomy from avoidable framing risk.

## External artifact: recommended title

`Strong-Coupling Polymer Methods and the Clay Yang-Mills Mass Gap: A Survey of Obstructions`

Recommended subtitle:

`Certificate Walls, Counting Walls, Gauge Quotients, and Continuum Reconstruction`

Avoid `shell`, `Hopf`, `Matryoshka`, `Einstein-Heller`, and `neural operator` in the title/subtitle of the referee-conservative version.

## External artifact: keep

- Abstract, rewritten without Hopf-shell or neural-operator references.
- Introduction and motivation for a survey companion to v0.14.4.
- Taxonomy of obstruction types:
  - certificate wall;
  - fiber-counting wall;
  - renormalization/preservation wall;
  - quotient-state-space wall;
  - continuum reconstruction/preimage wall.
- KP certificate wall and KP-versus-geometry-wall analysis.
- Wilson-loop image/preimage discipline, moved earlier.
- Embedded-surface and polymer-fiber hierarchy.
- Balaban/RG discussion, rewritten as preservation of estimates across scale transformations rather than shell-map language.
- Stochastic quantization discussion, updated for the 2026 3D uniqueness result.
- Cluster expansions as certificate-producing locality machinery.
- Loop equations and embedded-surface calculi.
- AQFT/pAQFT/factorization-algebra bridge as standards vocabulary for future interface specification.
- Lane II and Lane IV as future work, but stated conservatively.
- Non-claim box.

## External artifact: move out

Move these into the program-context companion:

- Hopf-Matryoshka shell-stack definition.
- Typed-placeholder caution for non-S^3 shell layers.
- Sub-Riemannian Hopf-fibration note.
- Einstein-Heller Interface Program alignment paragraph.
- Neural-operator callout.
- Any references whose only role is internal vocabulary alignment or computational surrogate framing.

## External rewrite mapping

| v0.18.1 phrase | External-track replacement |
| --- | --- |
| shell map | renormalization/comparison map |
| shell-local theorem | fixed-spacing local theorem or fixed-spacing lattice theorem |
| evidence object inside one shell | explicit certificate/evidence ledger |
| Hopf-shell projection/preimage interface | projection/reconstruction interface |
| S^3 placement | optional one-sentence note: SU(2) is diffeomorphic to S^3; no further use |
| internal substrate | omit |
| learned surrogate shell map | omit or move to companion |

## External section order

1. Introduction: what v0.14.4 proves and why a boundary survey is needed.
2. Image/preimage discipline for Wilson observables and reconstruction.
3. Obstruction taxonomy.
4. KP certificate wall.
5. Fiber-counting wall and surface/preimage hierarchy.
6. Renormalization and preservation walls.
7. Stochastic quantization and gauge-quotient state spaces.
8. Cluster expansions and locality certificates.
9. Loop equations and surface calculi.
10. Structural QFT specification languages.
11. Position of v0.14.4.
12. Lane II and Lane IV future work.
13. Non-claim box.
14. References.

## Program-context companion: recommended title

`Hopf-Shell and Learned-Operator Interface Notes for the Yang-Mills Obstruction Program`

Recommended subtitle:

`Auxiliary Classification Scaffold, Typed Projection Discipline, and Computational Diagnostics`

## Program-context companion: keep and expand

- Hopf tower and typed-placeholder discipline.
- SU(2) ~= S^3 placement, carefully scoped.
- Internal substrate vocabulary alignment.
- Einstein-Heller projection/fiber/semantic-lift analogy.
- Neural operators as empirical diagnostics, not proof apparatus.
- Explicit non-claim box stronger than v0.18.1.
- Mapping table back to the external obstruction taxonomy.

## Required hardening before arXiv/journal exposure

- Recover exact v0.14.4 source and replace approximate section references with line-checked references.
- Replace all extracted-PDF artifacts with editable LaTeX source.
- Fix the table-of-contents artifact where Section 3 appears as `13 Hopf-Shell...` in extracted text.
- Standardize beta constants and preserve enough significant digits for reproducibility.
- Add a short referee cover note explaining that the document is a survey/positioning paper, not a theorem paper.
- Add a one-page claim-scope ledger at the front.

## Current judgment

The technical obstruction taxonomy is strong enough to survive external review if separated from internal research-program vocabulary. The shell/interface material is useful, but it should be advanced as a companion rather than as mandatory framing for the mathematical survey.
