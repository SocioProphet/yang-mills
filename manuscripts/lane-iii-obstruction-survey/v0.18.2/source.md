# Lane III v0.18.2-FRI Closing Audit

## Strong-Coupling Polymer Methods and the Clay Yang-Mills Mass Gap: A Survey of Obstructions

Michael D. Heller  
SocioProphet Research  
Working closing audit. May 2026.

## Abstract

This closing audit addresses the four scope items of Issue #12 against Lane III v0.18.1: bibliography normalization, v0.14.4 cross-reference audit, math-rendering/build checklist, and v0.18.2 split discipline. Three items close at the planning/audit level in v0.18.2-FRI; the v0.14.4 cross-reference audit requires v0.14.4 source access and is specified as a punch-list deferring to v0.18.3-final.

The Hopf-shell scaffold is recommended for split into a separate auxiliary document per its own removability framing in v0.18.1. The neural-operator and Einstein-Heller paragraphs remain in the main text under their established non-load-bearing markers. No substantive content claim or non-claim is altered. v0.18.1's mathematical content is treated as referee-grade survey material; this closing audit is QA hardening only.

## 1. Status assessment against Issue #12

Lane III v0.18.1 is a submission-candidate referee package in good condition. Its substantive content includes:

- KP certificate wall description;
- Hopf-shell auxiliary scaffold;
- image/preimage discipline;
- RG, stochastic-quantization, cluster-expansion, and loop-equation taxonomic placements;
- neural-operator and structural-framework callouts;
- Lane II and Lane IV reframing;
- non-claim box discipline.

The closing work is hardening, not redrafting.

Issue #12 decomposes into four items:

1. Bibliography: closes in v0.18.2-FRI as audit plus normalization plan.
2. v0.14.4 cross-reference audit: defers to v0.18.3 pending v0.14.4 source.
3. Math-rendering/build checklist: closes as a QA checklist.
4. v0.18.2 split discipline: closes as a concrete recommendation and section map.

## 2. Bibliography audit

The v0.18.1 bibliography has 51 entries and is substantially expanded from v0.17.2. The bibliography is citation-grade. Required work is normalization rather than expansion.

### 2.1 Coverage findings

References [1]-[19] cover the constructive-QFT and lattice-gauge canon: Osterwalder-Seiler, Seiler Lecture Notes, Kotecky-Preiss, Brydges-Federbush, Glimm-Jaffe, Rivasseau, Balaban, Clay/Jaffe-Witten, Streater-Wightman, and Osterwalder-Schrader.

References [20]-[33] cover stochastic quantization, regularity structures, and 2D Yang-Mills: Hairer, Chandra-Chevyrev-Hairer-Shen, Chevyrev, Migdal, Makeenko-Migdal, Polyakov, Gross, Gross-Taylor, Witten, Driver, Sengupta, and Levy.

References [34]-[42] cover AQFT and structural frameworks: Haag-Kastler, Brunetti-Fredenhagen-Verch, Rejzner, Costello, Costello-Gwilliam, Atiyah, Lurie, and Einstein-Heller internal program material.

References [43]-[51] cover neural operators and Hopf-fibration/sub-Riemannian scaffold material: DeepONet, FNO, Neural Operator JMLR, Geo-FNO, coarse-graining-for-chaos work, NeuralOperator library, FNO practical guide, NOBLE, and Li-Zhan sub-Riemannian material.

### 2.2 Normalization recommendations

- DOI/arXiv consistency: add missing DOI/arXiv tags where available.
- Style normalization: pick full journal names or abbreviations and apply uniformly.
- Author-list normalization: decide full author list vs. `et al.` and apply uniformly.
- Citation order: topic-cluster order is acceptable; alphabetical order is also acceptable.
- BibTeX extraction: generate `references.bib` using stable keys, e.g. `kotecky-preiss-1986-cluster`.

### 2.3 Bibliography verdict

No structurally required reference is missing from v0.18.1. Bibliography hardening is a normalization/build task, not a content-expansion task.

## 3. v0.14.4 cross-reference audit punch-list

The v0.18.1 Production Note explicitly defers exact v0.14.4 lemma/proposition cross-references because the exact v0.14.4 source was not available during that work session. The audit below specifies atomic cross-reference insertions for v0.18.3 once v0.14.4 source is available.

### CR-1: Plaquette weight expansion

v0.18.1 location: Section 2.1, plaquette weight / character expansion line.

Needed: v0.14.4 reference for character expansion and closed-form plaquette activity expression.

### CR-2: Normalized plaquette density

v0.18.1 location: Section 2.1, normalized density and Bessel-ratio notation.

Needed: v0.14.4 reference for the Bessel ratio identity.

### CR-3: Topology-blind activity bound

v0.18.1 location: Section 2.1, topology-blind activity majorant.

Needed: v0.14.4 reference for the activity bound and definition of the `Q(beta)`-type majorant.

### CR-4: Adjacency degree / incidence constant

v0.18.1 location: Section 2.1, plaquette adjacency degree and incidence constant.

Needed: v0.14.4 geometric lemma about plaquette adjacency in `Z^4`.

### CR-5: Rooted-animal entropy

v0.18.1 location: Section 2.1, rooted animal / entropy bound.

Needed: v0.14.4 reference for topology-blind rooted-animal entropy bound.

### CR-6: KP criterion

v0.18.1 location: Section 2.1, optimized Kotecky-Preiss inequality.

Needed: v0.14.4 theorem/proposition containing the KP smallness condition.

### CR-7: Optimized constants

v0.18.1 location: Section 2.1, numerical constants and beta wall.

Needed: v0.14.4 numerical optimization lemma/proposition.

### CR-8: Mayer-Ursell connected-correlation theorem

v0.18.1 location: Section 2.3, denominator cancellation and termwise differentiation in source parameters.

Needed: v0.14.4 connected-correlation theorem reference.

### CR-9: Decay rate

v0.18.1 location: Section 10, connected-correlation decay-rate claim.

Needed: v0.14.4 decay-rate formula / proposition.

### CR-10: OS-Seiler Hilbert space and transfer gap

v0.18.1 location: Section 10, OS-Seiler Hilbert space and positive transfer operator with spectral gap.

Needed: v0.14.4 OS-Seiler construction and spectral-gap theorem references.

### CR-11: Evidence object

v0.18.1 location: Sections 3.4 and 10, certificate/evidence-object aggregation.

Needed: v0.14.4 reference for certificate ledger/evidence-object aggregation.

### Cross-reference verdict

The cross-reference audit is fully specified but not executable without the v0.14.4 source. v0.18.3 should insert citations of the form `[v0.14.4, Theorem N]`, `[v0.14.4, Lemma N]`, `[v0.14.4, eq. (N)]`, or `[v0.14.4, Section N]` at the 11 locations.

## 4. Math-rendering/build checklist

v0.18.2 should use the same QA discipline as the Lane VII v1.2 / v2.0.1 export packages.

1. Compile with `pdflatex` twice.
2. Verify no undefined references, missing citations, or significant overfull boxes.
3. Verify hyperref links: TOC, equation refs, citations, arXiv/DOI links.
4. Visually inspect math-heavy sections: KP setup, geometric-series wall comparison, Hopf scaffold equations, preimage hierarchy, evidence object, entropy refinement chain, and Lane IV boundary-data package.
5. Confirm bibliography rendering of all 51 references.
6. Generate manifest and SHA256 checksums for source, `.bib`, PDF, and auxiliary files.
7. Create ZIP package containing source, bibliography, compiled PDF, README, manifest, and SHA256 sums.

## 5. v0.18.2 split discipline recommendation

v0.18.1 states that the Hopf-shell scaffold is removable and not proof apparatus. v0.18.2 should make that removability operational.

### Recommended split

#### v0.18.2-main

Referee-facing obstruction survey without Hopf-shell vocabulary as proof scaffolding. Retain:

- introduction;
- KP certificate wall;
- image/preimage and Wilson-loop observable discussion, restated without Hopf-shell language;
- RG, stochastic, cluster, loop, structural framework sections;
- v0.14.4 positioning;
- Lane II and Lane IV discussion, restated as projection/preimage/interface discipline;
- non-claim box;
- errata;
- references.

#### v0.18.2-aux

Auxiliary Hopf-shell scaffold. Move:

- Hopf-Shell Interpretation section;
- Hopf-shell vocabulary in image/preimage/RG/stochastic/Lane IV sections;
- typed-placeholder discussion.

The auxiliary document should carry an abstract explicitly stating that it is a classification scaffold, not proof apparatus.

### Alternative if not split

Keep combined text but retitle the scaffold section as `Auxiliary Scaffold (Removable)` and add a referee-facing note before it.

### Split verdict

The split is recommended. It gives constructive-QFT referees a main document that stands without unfamiliar auxiliary vocabulary.

## 6. v0.18.2 and v0.18.3 scope

v0.18.2-FRI closes:

- bibliography audit and normalization plan;
- math-rendering/build checklist;
- v0.18.2 split discipline recommendation;
- v0.14.4 cross-reference specification.

v0.18.3 should close:

- all 11 exact v0.14.4 cross-reference insertions;
- final BibTeX normalization;
- final compilation;
- final ZIP package and SHA256 regeneration;
- optional actual main/aux split.

## 7. Methodology-manifesto compliance

This audit follows the Methodology Manifesto v0.1 disciplines where applicable:

- claim ledgers and non-claim boundaries;
- no invented cross-references;
- no theorem inflation;
- split discipline for auxiliary scaffold material;
- lane fallback discipline: Lane III hardens the obstruction survey while Lane VII remains proof-target work.

R/O/L/V/E, sign-majorant, path-dependence, and residual-threshold disciplines are not directly applicable to this Lane III survey-hardening artifact.

## 8. Non-claim box

This v0.18.2-FRI audit does not claim:

- to extend or modify v0.18.1 substantive content;
- to assert unverified v0.14.4 cross-references;
- to turn the survey into theorem-track proof apparatus;
- to alter v0.18.1's non-claim box;
- to provide constructive-QFT proof apparatus;
- to address the continuum Yang-Mills problem constructively;
- to extend v0.14.4;
- to make a Clay-level claim.

Positive claims:

- v0.18.1 bibliography is referee-grade and needs normalization, not expansion;
- v0.14.4 cross-reference audit decomposes into 11 atomic citation targets;
- math-rendering/build checklist is specified;
- Hopf-shell scaffold split is recommended with section-level implementation plan;
- v0.18.3 can close exact cross-references once v0.14.4 source is available.

## 9. Verdict

Lane III v0.18.1 is in good condition for referee submission after the specified hardening work. v0.18.2 closes the bibliography, build, split, and cross-reference-specification tasks at the audit level. v0.18.3 is blocked only on v0.14.4 source for exact cross-reference insertion.
