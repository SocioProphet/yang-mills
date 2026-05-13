# Baez-Taylor finite-N projection bridge

Status: program-context methodology artifact.
Date: 2026-05-13.

## Purpose

This note captures the useful comparison between Baez-Taylor finite-N two-dimensional Yang-Mills strings and the SocioProphet four-dimensional Yang-Mills program.

The purpose is not to import a theorem from two dimensions into the theorem track. The purpose is to preserve a reusable proof-architecture pattern:

```text
overcomplete formal state space
    -> explicit admissibility / projection law
    -> physical or proof-facing sector
    -> controlled residual defect if projection is not closed
```

Baez-Taylor provides a clean lower-dimensional precedent for this pattern. Lane VII uses a different algebra and a harder target, but the methodological alignment is strong enough to keep as program-context guidance.

## Source anchor

Reference object: John Baez and Washington Taylor, `Strings and Two-dimensional QCD for finite N`, arXiv:hep-th/9401041.

Core source result, in this program's language:

- large-N two-dimensional Yang-Mills admits a string/branched-cover expansion;
- finite N is not merely a truncation of large N;
- finite N imposes Mandelstam / representation-theoretic identities;
- those identities can be encoded by a projection operator in the symmetric-group algebra;
- geometrically, the projector appears as a distinguished projection-point singularity in the covering-map/string picture.

## What the source gives us

Baez-Taylor starts with an extended string-state Hilbert space. At finite N, the formal string states are overcomplete. The finite-N physical Hilbert space is obtained by applying a projection operator that enforces the allowed SU(N) representation content.

In schematic form:

```text
extended string Hilbert space
    -- P_N -->
finite-N physical Hilbert space
```

Equivalently, in the partition-function formulation, the finite-N restriction on Young diagrams becomes a symmetric-group algebra projector. Inserted into the covering-map delta constraint, it appears as a local projection-point defect.

The key methodological point is that a global representation-theoretic constraint can be re-expressed as a localized geometric/topological defect.

## Comparison to this repository

This repository is not studying two-dimensional finite-N QCD as its theorem track. The theorem-track anchor remains fixed-spacing, strong-coupling SU(2) Wilson lattice gauge theory, with an explicit transfer gap in the stated strong-coupling window and no continuum or Clay claim.

Lane VII instead studies whether Wilson-screen fiber entropy, spin-network recoupling, and Frobenius/Schatten channel allocation can sharpen the strong-coupling certificate. The active object is not a symmetric-group projector. It is a screen/channel admissibility problem.

The useful analogy is:

| Baez-Taylor finite-N QCD2 | SocioProphet Yang-Mills Lane VII |
| --- | --- |
| formal string states | polymer / Wilson-screen / spin-network channel states |
| Mandelstam identities | gauge, screen, channel, and recoupling admissibility |
| symmetric-group projector P_N | candidate Wilson-screen projection or majorant Pi_screen |
| projection-point singularity | screen/interface defect or boundary compression gate |
| finite-N exactness | fixed-spacing strong-coupling certificate discipline |
| projection weights may disturb genus ordering | cyclic/high-Betti residual defects may disturb Frobenius closure |

## Proposed program object

The comparison suggests that Lane VII should define a projection-like object explicitly rather than relying only on entropy prose.

Working schematic:

```text
bulk polymer / spin-network channel space
    -- Pi_screen -->
KP-admissible Wilson-screen fiber sector
```

The active theorem target can then be phrased as a closure/leakage problem:

```text
Does Pi_screen preserve Frobenius-scale control under cyclic/high-Betti channel composition?
```

Equivalently:

```text
uncontrolled Catalan growth
    -> screen projection / Frobenius allocation
    -> residual operator E
    -> subcritical or absorbable defect
```

This is the direct methodological analogue of Baez-Taylor's finite-N projection, but the algebra is Wigner / Temperley-Lieb / SU(2) recoupling rather than symmetric-group Young-diagram projection.

## Relation to Lane VII gates

This artifact supports, but does not replace, the existing Lane VII gates:

1. Define the normalized Wilson-screen channel package.
2. Define Pi_screen or an equivalent screen-transfer projection/conditional expectation object.
3. Identify the residual object E as operator/tensor leakage when closure fails.
4. Prove or refute Frobenius/Schatten allocation on cyclic Eulerian channel graphs.
5. Only after closure, audit KP insertion.

This gives the comparison a concrete role: Baez-Taylor motivates the formal separation between an overcomplete expansion and a physical/admissible projected sector.

## Non-claims

This artifact does not claim:

- a string-theoretic solution of four-dimensional Yang-Mills;
- a continuum Yang-Mills construction;
- a Clay Millennium mass-gap proof;
- weak-coupling or asymptotic-freedom control;
- an SU(N >= 3) theorem for this repository;
- that the Baez-Taylor projector directly applies to Wilson lattice SU(2) in four dimensions;
- that symmetric-group projection replaces Wigner / Temperley-Lieb / SU(2) recoupling machinery;
- that Lane VII Frobenius closure or KP insertion is proved.

## Actionable follow-up

Add a Lane VII note or section defining the candidate screen projection object:

```text
Pi_screen : H_bulk -> H_screen
```

with:

- domain and codomain;
- norm choice: operator, Hilbert-Schmidt, trace/Frobenius, or mixed Schatten;
- compatibility with gauge invariance and Osterwalder-Seiler reflection-positive transfer structure;
- behavior under recoupling moves;
- residual object E and subcriticality criterion;
- explicit non-claim boundary.

This would convert the Baez-Taylor analogy into a proof-facing specification rather than leaving it as prose.
