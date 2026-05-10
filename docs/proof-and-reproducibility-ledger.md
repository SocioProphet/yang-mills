# Yang-Mills Program Proof and Reproducibility Ledger

Date: 2026-05-09

## Purpose

This ledger orders the current Yang-Mills program work into four classes:

1. proved finite claims;
2. reproduced computations and checksums;
3. conditional theorem targets;
4. explicit non-claims.

It also corrects the older workplan against the current repository state.

## Current corrected state

The older planning note is directionally useful but stale in several places. Current state:

- v0.14.4 remains the theorem-track anchor: fixed-spacing, strong-coupling SU(2), explicit transfer gap, no continuum/Clay claim.
- Lane III v0.18.3 cross-reference audit is now captured and merged; the v0.18.1/v0.18.2 cross-reference debt is no longer open at the audit layer.
- The archive reconstruction bundle has verified ZIP/PDF/text hashes recorded; binary upload remains pending.
- Phase 2 `Jmax=1/2` fixture independent verification is captured and merged.
- Phase 3a `Jmax=1` basis registry is captured and merged.
- The next temporal-mechanics task is Phase 3b: `Jmax=1` Gram matrix.
- Lane VII is current through v2.0.2 / v1.18.1 in source/status form; its next theorem target is v1.19, the Eulerian channel-graph Schatten allocation theorem.
- Methodology Manifesto v0.1 is captured as working source.

## Proved finite claims

| Claim | Status | Source artifact | Claim boundary |
| --- | --- | --- | --- |
| v0.14.4 fixed-spacing strong-coupling SU(2) transfer gap | theorem-track anchor | `Strong-Coupling Lattice Mass-Gap Seed v0.14.4` | Fixed lattice spacing and strong coupling only; no continuum/Clay claim. |
| Tree-Frobenius aggregation under normalized hypotheses | proved finite theorem | Lane VII v1.2 / v2.0.x consolidation | Conditional on normal-form hypotheses. |
| One-cycle Frobenius closure under normalized hypotheses | proved finite theorem | Lane VII v1.3 chat/source status | Conditional on normal-form and source-uniformity hypotheses. |
| Factorable two-cycle Frobenius closure | proved finite theorem | Lane VII v1.3 chat/source status | Factorable cycles only. |
| Operator closure refuted in cyclic category | proved finite counterexample | Lane VII rank-2 cyclic test | Refutes global operator closure, not sectoral operator safety. |
| Dimension-weighted Racah / 9j recoupling unitarity | finite representation-theory result | Lane VII v1.4-v1.6 | Applies to dimension-weighted recoupling matrices, not raw 3nj scalar entries. |
| Single-edge local audits at C1=1, C2=2, C3=5 | local finite audits | Lane VII v1.12-v1.14, v2.0.1 | Channel-pattern audits; not full catalogue closure. |
| Multi-thick representative audits | local finite audits | Lane VII v1.16 / v2.0.2 | Representative/channel-pattern audits; v1.18 shows high-Betti general theorem is still needed. |

## Reproduced computations and checksum artifacts

| Computation / artifact | Status | Result | Source / repo path |
| --- | --- | --- | --- |
| Lane III v0.18.3 cross-reference audit | merged | CR-1..CR-11 resolved against v0.14.4 anchors | `manuscripts/lane-iii-obstruction-survey/v0.18.3/cross-reference-audit.md` |
| Archive reconstruction hash ledger | merged | ZIP SHA256 `a9482d5aff11067980b1c384cf715ed99991c13bed9135f789443156bb19ae5d`; 9 PDFs, 102 pages; text marker counts match | `docs/archive-reconstruction-2026-05-09.md` |
| Phase 2 `Jmax=1/2` fixture verification | merged | `lambda0`, normalized spectrum, `V_phi111`, `K111`, zero rule reproduced | `manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/source.md` |
| Phase 3a `Jmax=1` basis registry | merged | 14 basis labels; `Jmax=1/2` subset `[0,1,2,4,5]` | `manuscripts/lane-temporal-mechanics-jmax1/phase3a-basis-registry/` |
| Local fundamental catalogue enumeration | computed/source-captured | `rank(A)=7`, `2^17`, `560` orbits, `58` profiles | Lane VII v1.17 / v2.0.2 source |
| Orbit reduction audit | computed/source-captured | 33 immediately covered; 527 high-Betti unresolved | Lane VII v1.18 source/status |

## Conditional theorem targets

| Target | Current status | Blocking gate | Next action |
| --- | --- | --- | --- |
| Lane VII arbitrary Eulerian channel-graph Frobenius/Schatten allocation | open | Need general theorem for high-Betti Eulerian local channel graphs | v1.19 theorem attempt. |
| Wilson-screen to dual-package bridge lemma | open | Need proof that Wilson-screen polymer contraction is represented by normalized Cherrington-Christensen/Oeckl-Pfeiffer package | After v1.19 or in parallel if needed. |
| KP insertion of Frobenius hybrid activity | open | Requires closure + bridge + source-uniformity | Later audit only. |
| `Jmax=1` Gram matrix | open | Need Phase 3b computation in declared 14-label registry | Immediate temporal next step. |
| `Jmax=1` truncation check | open | Requires Gram/matrix construction and regression to Phase 2 fixture | Phase 3c. |
| `Jmax=1` spectrum / vacuum decomposition / coefficient graph | open | Requires Phase 3b and Phase 3c | Phase 3d. |
| Literal 3j/6j appendix for `Phi_111` | open | Convention-completeness after fixture verification | Phase 5. |
| Lane III final v0.18.3 manuscript package | open | Need manuscript integration, build, checksums | Separate production step after audit. |

## Explicit non-claims

The program does not currently claim:

- continuum Yang-Mills construction;
- Clay Millennium mass gap proof;
- weak-coupling or asymptotic-freedom control;
- physical scale interpretation for finite `Jmax` computations;
- `a -> 0` survival of a mass gap;
- SU(N) for N >= 3 as closed theorem track;
- KP wall movement as a theorem;
- arbitrary cyclic Frobenius closure;
- Wilson-screen-to-dual-package bridge;
- KP insertion of the Frobenius hybrid activity.

## Corrected priority order

The older proposed order is updated as follows.

### Immediate active sequence

1. Phase 3b — `Jmax=1` Gram matrix.
2. Phase 3c — `Jmax=1 -> Jmax=1/2` truncation regression.
3. Methodology Manifesto v0.2 cross-track refresh after Phase 3c.
4. Phase 3d — `Jmax=1` spectrum / vacuum decomposition / coefficient graph / sector tags.
5. Literal `3j/6j` appendix for `Phi_111`.
6. Lane VII v1.19 — Eulerian channel-graph Schatten allocation theorem.

### Parallel production lane

- v0.14.4 arXiv/CMP submission packaging remains highest external-impact work, but it is editorial/submission work rather than new mathematics.
- Lane III v0.18.3 manuscript integration and build package should proceed when submission packaging is active.

### Parked tracks

- Lane II bulk polymer route remains backup.
- Lane IV continuum-preimage remains parked specification/continuum-interface lane.
- Lane VI simplicial regulator remains parked diagnostic.
- Brownian Holonomy remains parked diagnostic sidecar.
- Heller-Winters, Heller-Godel, K3 product-formula, constrained spectral learning, and other parallel programs remain separate unless explicitly reactivated.

## Next reproducibility scripts needed

1. Phase 3b Gram-matrix generator in the Phase 3a basis order.
2. Phase 3c truncation regression script selecting indices `[0,1,2,4,5]`.
3. Lane VII v1.19 graph-norm allocation checker for representative Eulerian graphs.
4. Lane III v0.18.3 production script for final build/checksum package.

## Verdict

The program is in order at the documentation and finite-claim ledger level through Phase 3a. The next proof/reproducibility task is Phase 3b, not more status capture.
