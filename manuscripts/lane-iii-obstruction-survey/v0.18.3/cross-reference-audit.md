# Lane III Obstruction Survey — v0.18.3 Cross-Reference Audit

**Track**: `manuscripts/lane-iii-obstruction-survey/v0.18.3/`  
**Status**: Audit deliverable. Referee-pending. Source for merging into `v0.18.2/source.md` to produce `v0.18.3/source.md`.  
**Date**: 2026-05-09  
**Source authority for cross-references**: `strong_coupling_lattice_mass_gap_seed_v0_14_4.pdf` (15pp, CMP pre-submission consolidation, internal date 2026-05-07).

## 1. What this audit is and is not

This audit closes the v0.18.2 production note that explicitly deferred all v0.14.4 cross-references on the grounds that v0.14.4 source was not available at the v0.18.2 lock. With v0.14.4 source now in hand, every deferred citation has been resolved against a specific v0.14.4 location.

This audit is **not** a re-derivation of v0.14.4 results, **not** a new theorem, and **not** a replacement of v0.18.2's obstruction taxonomy. It is a citation-resolution layer that converts the v0.18.2 referee package into a v0.18.3 referee package whose cross-references are concrete.

The 11 cross-reference items (CR-1 through CR-11) are inherited from the v0.18.2-FRI closing audit punch-list.

## 2. v0.14.4 anchor coordinates

| Anchor | Value | v0.14.4 location |
| --- | --- | --- |
| beta* | `0.006296889394074993` | Section 2 (p.3), Appendix A (p.13) |
| q_KP | `0.006311768836893038` | Section 2 (p.3), Proposition 8.4 (p.9), Appendix A (p.13) |
| M0 = 20e | `54.365636569180904` | Section 2 (p.3), Lemma 8.3 (p.8), Appendix A |
| D_inc | `21 (= 1 + Delta_square <= 21)` | Section 2 (p.3), Definition 8.1 (p.8), Appendix A |
| a* | `0.4576898452957963` | Section 2 (p.3), Proposition 8.4 (p.9), Appendix A |
| Q(beta*) | `= q_KP` | Section 2 (p.3), Appendix A |
| r(beta*) | `0.0015742197477251624` | Appendix A (p.13) |
| r(1) | `0.24019372387008974` | Appendix A (p.13) |
| Q(1) | `1.4048819255110066` | Appendix A (p.13) |
| m_beta | `-log(M0 Q(beta))` | Theorem 8.7 (p.10), Corollary 11.2 (p.11), Theorem 12.1 (p.12) |

Anchor values match the constants used throughout v0.18.x. No revision of v0.18.2 numerical content is required by v0.14.4; the audit is a pointer-resolution operation only.

## 3. Cross-reference resolution table (CR-1..CR-11)

For each CR, this table gives the Lane III concept being cross-referenced, the v0.14.4 location, citation content, and a phrasing note for v0.18.3.

### CR-1 — Plaquette weight Fourier expansion

- **Lane III concept**: SU(2) plaquette weight as character expansion with explicit modified-Bessel coefficients.
- **v0.14.4 location**: Section 2 (p.3), first display equation.
- **Citation content**: The Wilson plaquette weight is `W_beta(g) = e^{beta cos theta_g} = sum_{j in 1/2 N_0} c_j(beta) chi_j(g)` with `d_j = 2j+1` and `c_j(beta) = I_{2j}(beta) - I_{2j+2}(beta) = (2d_j/beta) I_{2j+1}(beta) > 0`.
- **Phrasing for v0.18.3**: The plaquette weight expansion in v0.14.4 Section 2 supplies the modified-Bessel coefficient convention used here.

### CR-2 — Normalized plaquette density

- **Lane III concept**: Decomposition `p_beta = 1 + h_beta` with channel ratios `r_j(beta)`.
- **v0.14.4 location**: Section 2 (p.3), second/third display equations; also re-stated in proof of Theorem 3.2 (p.4).
- **Citation content**: `p_beta(U) = W_beta(U)/c_0(beta) = 1 + h_beta(U)`, with `h_beta(U) = sum_{j>0} d_j r_j(beta) chi_j(U)` and `r_j(beta) = c_j(beta)/(d_j c_0(beta)) = I_{2j+1}(beta)/I_1(beta)`.
- **Phrasing for v0.18.3**: The normalized density convention follows v0.14.4 Section 2 and is reused in v0.14.4 Theorem 3.2.

### CR-3 — Topology-blind activity bound Q(beta)

- **Lane III concept**: Single quantity `Q(beta)` controlling all plaquette-activity contributions in the polymer expansion.
- **v0.14.4 location**: Section 2 (p.3) for definition; Lemma 8.2 (p.8) for the bound.
- **Citation content**: `Q(beta) := sum_{j>0} d_j^2 r_j(beta)`; for any connected polymer `Gamma` in the normalized Wilson expansion, `|z(Gamma)| <= Q(beta)^{|Gamma|}`, since `|h_beta(U)| <= sum d_j^2 r_j(beta) = Q(beta)`.
- **Phrasing for v0.18.3**: The activity bound v0.14.4 Lemma 8.2 supplies the absolute control `|z(Gamma)| <= Q(beta)^{|Gamma|}` used here.

### CR-4 — Plaquette-adjacency incompatibility constant D_inc

- **Lane III concept**: Local graph constant controlling polymer incompatibility on the 4D plaquette-adjacency graph.
- **v0.14.4 location**: Section 2 (p.3) for value; Definition 8.1 (p.8) for derivation.
- **Citation content**: For `d=4`, `Delta_square <= 4(2(d-1) - 1) = 20` because each of the four edges of a plaquette lies in six plaquettes and the original plaquette is excluded; therefore `D_inc = 1 + Delta_square <= 21`.
- **Phrasing for v0.18.3**: The incompatibility constant `D_inc <= 21` is fixed in v0.14.4 Section 2 and derived in v0.14.4 Definition 8.1.

### CR-5 — Rooted plaquette-animal entropy M0

- **Lane III concept**: Conservative rooted-connected-animal entropy bound on the plaquette-adjacency graph.
- **v0.14.4 location**: Lemma 8.3 (p.8).
- **Citation content**: `N_A^root(p) <= M0^{A-1}` with `M0 = 20e`. The standard rooted connected-animal estimate gives connected sets of size `A` containing a fixed root bounded by `(e Delta_square)^{A-1}` on a graph of max degree `Delta_square <= 20`; `M0 = 20e` is the conservative choice.
- **Phrasing for v0.18.3**: The rooted-animal entropy bound `M0 = 20e` is fixed in v0.14.4 Lemma 8.3.

### CR-6 — Kotecky-Preiss criterion

- **Lane III concept**: KP smallness condition that drives polymer convergence, with optimization parameter `a`.
- **v0.14.4 location**: Proposition 8.4 (p.9).
- **Citation content**: The abstract polymer expansion converges absolutely if `Q(beta) e^a (D_inc + a M0) <= a`. With `a* = 0.4576898452957963`, the condition is implied by `Q(beta) < q_KP := 0.006311768836893038`. Since `Q(beta*) = q_KP`, the criterion holds for all `beta < beta* = 0.006296889394074993`.
- **Phrasing for v0.18.3**: KP convergence in the strong-coupling window is established in v0.14.4 Proposition 8.4.

### CR-7 — Optimized constants (a*, q_KP, beta*)

- **Lane III concept**: Numerical anchor triple producing the v0.14.4 strong-coupling window.
- **v0.14.4 location**: Section 2 (p.3); Proposition 8.4 (p.9); Appendix A (p.13) full constants table.
- **Citation content**: `a* = 0.4576898452957963`, `q_KP = 0.006311768836893038`, `beta* := 0.006296889394074993`, with `Q(beta*) = q_KP`, `Q(1) = 1.4048819255110066`, `r(1) = 0.24019372387008974`, `r(beta*) = 0.0015742197477251624`.
- **Phrasing for v0.18.3**: The optimized constants `a*`, `q_KP`, and `beta*` used here are those of v0.14.4 Section 2 and Appendix A.

### CR-8 — Mayer-Ursell denominator cancellation

- **Lane III concept**: Connected-source-cluster contribution to centered correlations after partition-function denominator cancellation.
- **v0.14.4 location**: Lemma 8.5 (p.9), with the connecting-cluster bound at Lemma 8.6 (p.10).
- **Citation content**: For centered local Wilson-loop polynomial observables `O_p`, `O_q` with source parameters `s,t`, the connected correlation is the second source derivative of `log Z_Lambda(s,t)` at `s=t=0`; absolute KP convergence permits termwise differentiation; the right-hand side is a Mayer-Ursell sum over connected clusters of mutually incompatible polymers and source tags; vacuum polymers and clusters touching only one source cancel; only connected clusters spanning both source supports contribute.
- **Phrasing for v0.18.3**: The denominator-cancellation step appealed to here is v0.14.4 Lemma 8.5; the geometric distance bound is v0.14.4 Lemma 8.6.

### CR-9 — Decay rate m_beta

- **Lane III concept**: Volume-uniform exponential decay rate of centered correlations in the strong-coupling window.
- **v0.14.4 location**: Theorem 8.7 (p.10) for the decay theorem; `m_beta` defined throughout, e.g. Corollary 11.2 (p.11), Theorem 12.1 (p.12).
- **Citation content**: For `beta < beta*` and centered local Wilson-loop polynomial observables `O_0`, `O_t`, `|omega_beta(O_0 O_t) - omega_beta(O_0) omega_beta(O_t)| <= C_{O,beta,m} e^{-mt}` for every `m < m_beta := -log(M0 Q(beta))`. The KP constants are volume-uniform because the incompatibility degree, activity bound, and rooted-animal entropy are local graph constants independent of `Lambda`; passing to the DLR limit preserves the bound.
- **Phrasing for v0.18.3**: The strong-coupling decay rate `m_beta = -log(M0 Q(beta))` is established in v0.14.4 Theorem 8.7.

### CR-10 — OS-Seiler reflection-positive Hilbert space and transfer spectral gap

- **Lane III concept**: OS Hilbert space construction, Wilson-loop algebra density, and transfer spectral gap above the vacuum.
- **v0.14.4 location**: Theorem 7.1 (p.7) for Wilson-loop / OS Hilbert-space equality; Theorem 11.1 (p.11) for the open-interval spectral statement; Corollary 11.2 (p.11) for the closed-endpoint statement; Theorem 12.1 (p.12) cumulative theorem.
- **Citation content**: `H_{beta,W}=H_{beta,OS}` (v0.14.4 Theorem 7.1). For `beta < beta*`, `sigma(T_1 | H_beta^0) subset [0,e^{-m}]` for every `m < m_beta` (v0.14.4 Theorem 11.1); endpoint inclusion `sigma(T_1 | H_beta^0) subset [0,e^{-m_beta}]`, `sigma(H_beta | H_beta^0) subset [m_beta, infinity]` (v0.14.4 Corollary 11.2). The cumulative theorem packages this as the fixed-spacing strong-coupling gap above the vacuum.
- **Phrasing for v0.18.3**: The Wilson-loop / OS Hilbert space equality is v0.14.4 Theorem 7.1; the transfer spectral gap is v0.14.4 Theorem 11.1 with endpoint Corollary 11.2 and cumulative form Theorem 12.1.

### CR-11 — Evidence object E_KP

- **Lane III concept**: Machine-readable artifact summarizing v0.14.4 status, gates closed, and downstream targets.
- **v0.14.4 location**: Appendix B (p.13-14).
- **Citation content**: Appendix B is a JSON record with fields `artifact` (Strong-Coupling Lattice Mass-Gap Seed v0.14.4), `status` (cmp_pre_submission_consolidation), `claim` (fixed_lattice_spacing_strong_coupling_gap_not_clay), `gauge_group` (SU(2)), `beta_threshold` (0.006296889394074993), `gates_closed`, and `next` items.
- **Phrasing for v0.18.3**: The evidence-object schema `E_KP` referenced here is v0.14.4 Appendix B (machine-readable summary).

## 4. Items v0.14.4 confirms beyond the 11-item punch-list

Three v0.14.4 items are not on the v0.18.2-FRI punch-list but are worth noting in v0.18.3 because they affect the obstruction taxonomy framing.

1. **Inline DLR-limit uniqueness proof**. v0.14.4 Theorem 3.2 and Remark 3.3 supply an inline gauge-invariant uniqueness argument using polymer convergence and boundary-cluster decay. v0.18.3 should reflect that the uniqueness gate is internal to v0.14.4 rather than merely referenced.
2. **Local RP norm control**. v0.14.4 Proposition 6.1 gives localized RP norm control with constant `B_{beta,K,h}=exp{2 beta(N_int(K,h)+S(K,h))}`. v0.18.3 should note this as the local cylinder constant feeding into Theorem 7.1.
3. **Companion-lane note**. v0.14.4 Section 14.3 explicitly lists a Clay obstruction survey as a downstream companion lane. v0.18.x is positioned within this companion-lane plan.

These items are additive. They do not change the 11-item punch-list, but they improve v0.18.3 referee-readability.

## 5. Items v0.14.4 does not settle for v0.18.x

v0.14.4 does not claim:

- continuum Yang-Mills existence;
- control along `beta(a) -> infinity`;
- a physical mass lower bound surviving `a -> 0`;
- SU(N) for N >= 3;
- a Clay Millennium proof.

The Lane III obstruction taxonomy describes precisely the gaps v0.14.4 declines to close. v0.18.3's obstruction content is unaffected by the audit; only its citations are.

## 6. Hopf-shell main/aux split

The v0.18.2-FRI closing audit recommended a main/aux split treating Hopf-shell content as removable scaffold per v0.18.1 Section 3.1. v0.14.4 does not engage the Hopf-shell question. v0.18.3 should retain the v0.18.2 main/aux structure unchanged.

## 7. Bibliography normalization

v0.18.3 should add the v0.14.4 entry:

```bibtex
@misc{heller-v0144,
  author = {Heller, Michael D.},
  title = {Strong-Coupling Lattice Mass-Gap Seed v0.14.4},
  note = {Working Yang-Mills mass-gap program manuscript, internal date 2026-05-07. CMP pre-submission consolidation. 15pp.},
  year = {2026}
}
```

The references within v0.14.4 are already part of the v0.18.x core bibliography or close enough to existing entries that no required structural additions follow from this audit.

## 8. v0.18.3 production checklist

1. For each of CR-1..CR-11, replace the v0.18.2 deferred-citation placeholder with the phrasing from Section 3.
2. Add brief acknowledgments for the three additive items in Section 4.
3. Confirm no numerical constant requires revision: anchors in Section 2 match v0.18.x values.
4. Append the v0.14.4 bibliography entry per Section 7.
5. Retain the v0.18.2 main/aux Hopf-shell structure unchanged.
6. Update the `manuscripts/lane-iii-obstruction-survey/v0.18.3/source.md` lock notice to remove the `blocked on v0.14.4 source` note.
7. Capture this audit alongside `source.md` as `manuscripts/lane-iii-obstruction-survey/v0.18.3/cross-reference-audit.md`.

## 9. Methodology discipline notes

This audit follows the disciplines codified in `manuscripts/methodology/manifesto-v0.1/source.md`:

- Discipline 1 (claim ledgers): each CR is citation-resolution only, not re-derivation;
- Discipline 2 (sealed non-claim boxes): Section 5 is the sealed non-claim box for this audit;
- Discipline 7 (lane fallback): Hopf-shell content remains removable scaffold and does not become load-bearing proof apparatus.

## 10. Audit summary

Eleven cross-references are resolved against v0.14.4:

| CR | Resolved against | Type |
| --- | --- | --- |
| CR-1 | v0.14.4 Section 2 | definitional |
| CR-2 | v0.14.4 Section 2 + Theorem 3.2 proof | definitional |
| CR-3 | v0.14.4 Section 2 + Lemma 8.2 | bound |
| CR-4 | v0.14.4 Section 2 + Definition 8.1 | definitional |
| CR-5 | v0.14.4 Lemma 8.3 | bound |
| CR-6 | v0.14.4 Proposition 8.4 | criterion |
| CR-7 | v0.14.4 Section 2 + Proposition 8.4 + Appendix A | definitional |
| CR-8 | v0.14.4 Lemma 8.5 + Lemma 8.6 | theorem |
| CR-9 | v0.14.4 Theorem 8.7 | theorem |
| CR-10 | v0.14.4 Theorem 7.1 + Theorem 11.1 + Corollary 11.2 + Theorem 12.1 | theorem |
| CR-11 | v0.14.4 Appendix B | evidence-object |

All 11 items are closed. v0.18.3 is unblocked for referee handoff once the production checklist is executed.
