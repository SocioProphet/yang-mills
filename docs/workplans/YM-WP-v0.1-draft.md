# Yang-Mills Program Integrated Workplan

Document ID: `YM-WP-v0.1`
Status: draft for judge review prior to upstream promotion
Scope: sequenced execution plan for Moves 4, 1, and 2 of the Yang-Mills program

## Claim discipline

This workplan does not assert any new mathematical result. It sequences already-defined workstreams against the existing manuscript corpus.

The non-claim boxes of the underlying manuscripts remain authoritative:

- `v0.14.4` is fixed-spacing, strong-coupling, SU(2) Wilson lattice gauge theory. It does not claim continuum reconstruction, weak-coupling control, SU(N) extension for N >= 3, or a Clay Yang-Mills mass-gap proof.
- `v0.18.1` is an obstruction survey between `v0.14.4` and Clay. It claims no positive bridge result.
- `v0.9.20` is a finite-cutoff diagnostic at `Jmax = 1/2`. It does not claim continuum, infinite-volume, or weak-coupling uniformity.

## Executive summary

Three moves are sequenced over an estimated 6-10 weeks of disciplined execution. None requires new mathematics; all require editing, cross-checking, symbolic derivation, and bookkeeping.

| Move | Action | Estimated effort | Dependency | Output |
|---:|---|---|---|---|
| 4 | Cross-reference pass `v0.18.1` ↔ `v0.14.4` | 0.5-1 week | none | `v0.18.2` with deferred references resolved |
| 1 | `v0.14.4` → arXiv / CMP package | 2-4 weeks | Move 4 recommended | arXiv math-ph/hep-lat and CMP package |
| 2 | Wigner-symbol derivation of `Jmax=1/2` 5x5 matrix, Gates G1/G2 | 1-2 weeks | independent | `v0.9.21` with symbolic 5x5 matrix and `Phi_111` selection rule resolved |

Recommended order: Move 4 first, Move 1 second, Move 2 in parallel with Move 1.

## Move 4 — cross-reference pass `v0.18.1` ↔ `v0.14.4`

Purpose: produce `v0.18.2` by replacing deferred references in `v0.18.1` with exact section, lemma, and proposition references in `v0.14.4`.

Required cross-reference targets:

1. KP certificate wall: cite exact polymer convergence / threshold references in `v0.14.4`.
2. Geometry-counting wall: cite animal-entropy argument and declared bound.
3. Surface-preimage wall: cite polymer activity bound and identify the structure discarded by counting.
4. OS reflection-positivity import: cite OS hyperplane convention and self-adjointness derivation.
5. DLR uniqueness step: cite DLR argument and the exact input used by the obstruction survey.
6. Numerical constants table: verify constants match `v0.14.4` to declared precision.

Acceptance gate:

- every deferred reference is replaced by a specific numbered reference;
- numerical constants match `v0.14.4`;
- a reviewer can verify each reference without ambiguity;
- changelog records `v0.18.1 -> v0.18.2`.

## Move 1 — `v0.14.4` arXiv / CMP submission package

Purpose: package the fixed-spacing strong-coupling SU(2) theorem track for public submission after the cross-reference companion is ready.

Minimum checklist:

- final typo, citation, and cross-reference pass;
- notation consistency pass;
- numerical constants reproducibility pass;
- no-claim box and abstract alignment;
- bibliography complete;
- independent reviewer pass and written resolution log;
- arXiv upload target: `math-ph`, cross-list `hep-lat`, optional `math.SP`;
- CMP submission package with cover letter preserving fixed-spacing / strong-coupling / SU(2) / non-continuum boundary.

Acceptance gate:

- `v0.14.4` has stable arXiv identifier;
- `v0.18.2` has stable arXiv identifier and cross-references `v0.14.4`;
- CMP package submitted;
- internal docs cite arXiv identifiers rather than internal-only version numbers.

## Move 2 — Wigner-symbol derivation, `Jmax=1/2` 5x5 matrix, G1/G2

Purpose: close the first finite-cutoff symbolic gate before any `Jmax=1` scaling.

G1 requires a symbolic 5x5 Wigner derivation under a declared convention. Each entry must be classified as:

- forced;
- forbidden;
- coefficient-dependent.

G2 requires the `Phi_111` structural-zero / selection-rule question to be proven or refuted.

Required steps:

1. Declare Wigner / Clebsch-Gordan phase convention.
2. Freeze basis ordering.
3. Verify temporal baseline reproduction.
4. Expand magnetic endpoint factors.
5. Reduce Haar projection to Wigner-symbol contractions.
6. Classify all 25 matrix entries.
7. Numerically verify against `v0.9.20` Appendix G1.
8. Prove or refute the `Phi_111` structural-zero rule.

Acceptance gate:

- full symbolic 5x5 matrix recorded;
- all entries classified;
- numerical agreement to declared tolerance;
- G2 recorded as proved or refuted;
- `v0.9.21` changelog closes G1/G2 or records failure mode.

## Coordination

```text
Move 4 -> Move 1
Move 2 runs in parallel
```

Suggested schedule:

- Weeks 1-2: Move 4; Move 2 convention declaration and temporal baseline.
- Weeks 3-4: Move 1 editorial passes; Move 2 entry derivation.
- Weeks 5-6: Move 1 reproducibility/reviewer pass; Move 2 final whitepaper edits.
- Weeks 7-8: submission and buffer.

## What to avoid during this tranche

- Do not push `N` past 1000 as a substitute for bridge work.
- Do not start SU(N) for N >= 4 before N = 3 closes its own gates.
- Do not invest in continuum-construction infrastructure inside this tranche.

## Out of scope

- Lane IV RG interface specification.
- N = 3 / Part Two-Three execution plan.
- Cross-corpus methodological claims, including Heller-Winters, Heegner-engine analogies, or Lawful Learning.

Note: Lawful Learning is handled through the HPhD mirror / `hphd-zeta-mirror-lattice` apparatus lane, not this Yang-Mills workplan.

## Upstream gate

This workplan is ready for upstream inclusion only after judge review verifies:

1. no new mathematical claims were introduced;
2. no continuum or Clay claims were introduced;
3. dependency graph between Moves 4, 1, and 2 is honest;
4. risk sections identify real failure modes;
5. judge feedback is incorporated or explicitly deferred.

If approved, this draft becomes `YM-WP-v0.2` and can be included as the active Yang-Mills workplan.
