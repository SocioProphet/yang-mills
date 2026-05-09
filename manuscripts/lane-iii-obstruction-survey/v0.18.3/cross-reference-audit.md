# Lane III v0.18.3-FRI Cross-Reference Audit

## Strong-Coupling Polymer Methods and the Clay Yang-Mills Mass Gap: A Survey of Obstructions

Michael D. Heller  
SocioProphet Research  
Working cross-reference audit. May 2026.

## 1. Scope statement

This document resolves the v0.18.2 cross-reference punch-list against the available v0.14.4 source. It is a citation-resolution audit, not a re-derivation. Its function is to give the v0.18.3 manuscript exact v0.14.4 anchors for each load-bearing citation.

It does not alter the substantive non-claim boundary of v0.18.1 / v0.18.2: no continuum Yang-Mills construction, no Clay-level claim, and no extension of v0.14.4.

## 2. v0.14.4 anchor coordinates

The v0.14.4 source confirms the constants and proof gates used in Lane III:

| Quantity / object | v0.14.4 anchor |
| --- | --- |
| Wilson weight expansion `W_beta` | Section 2, Wilson data and constants |
| Bessel coefficient formula `c_j(beta)` | Section 2 |
| Normalized ratio `r_j(beta)` | Section 2 |
| Activity majorant `Q(beta)` | Section 2 and Lemma 8.2 |
| `M_0=20e` | Section 2 and Lemma 8.3 |
| `D_inc <= 21` | Section 2 and Definition 8.1 |
| `a_*` | Section 2 and Proposition 8.4 |
| `q_KP` | Section 2 and Proposition 8.4 |
| `beta_*` | Section 2 and Appendix A |
| `m_beta=-log(M_0 Q(beta))` | Theorem 8.7, Corollary 11.2, Theorem 12.1 |

## 3. CR-1 through CR-11 resolution table

| CR | v0.18.x target | v0.14.4 location | Supporting content | v0.18.3 phrasing |
| --- | --- | --- | --- | --- |
| CR-1 | Plaquette weight expansion | Section 2 | `W_beta(g)=e^{beta cos theta_g}=sum_j c_j(beta) chi_j(g)`, with `c_j(beta)=I_{2j}(beta)-I_{2j+2}(beta)=2 d_j beta^{-1} I_{2j+1}(beta)>0`. | Cite as `[v0.14.4, Section 2]` after the Wilson character expansion. |
| CR-2 | Normalized plaquette density | Section 2 and Theorem 3.2 proof | Section 2 defines `r_j(beta)=c_j/(d_j c_0)=I_{2j+1}/I_1`; the DLR proof writes `p_beta(U)=W_beta(U)/c_0(beta)=1+h_beta(U)` and `h_beta=sum_{j>0}d_j r_j chi_j`. | Cite as `[v0.14.4, Section 2 and Theorem 3.2 proof]` after the normalized-density line. |
| CR-3 | Topology-blind activity bound | Section 2 and Lemma 8.2 | Section 2 defines `Q(beta)=sum_{j>0}d_j^2 r_j(beta)`; Lemma 8.2 states `|z(Gamma)| <= Q(beta)^{|Gamma|}`. | Cite as `[v0.14.4, Section 2 and Lemma 8.2]`. |
| CR-4 | Adjacency degree and incidence constant | Section 2 and Definition 8.1 | Definition 8.1 states `Delta_square <= 4(2(d-1)-1)=20` for `d=4`, hence `D_inc=1+Delta_square <= 21`; Section 2 records `D_inc=21`. | Cite as `[v0.14.4, Definition 8.1]`. |
| CR-5 | Rooted-animal entropy | Lemma 8.3 | Lemma 8.3 states `N_A^{root}(p) <= M_0^{A-1}` with `M_0=20e`. | Cite as `[v0.14.4, Lemma 8.3]`. |
| CR-6 | KP criterion | Proposition 8.4 | Proposition 8.4 states the KP convergence condition `Q(beta)e^a(D_inc+aM_0)<=a`. | Cite as `[v0.14.4, Proposition 8.4]`. |
| CR-7 | Optimized constants | Section 2, Proposition 8.4, Appendix A | Section 2 records `a_*`, `q_KP`, and `beta_*`; Proposition 8.4 states the optimized condition; Appendix A tabulates the numerical constants. | Cite as `[v0.14.4, Section 2, Proposition 8.4, and Appendix A]`. |
| CR-8 | Mayer-Ursell denominator cancellation | Lemma 8.5 and Lemma 8.6 | Lemma 8.5 states connected source-cluster cancellation via source derivatives of `log Z`; Lemma 8.6 supplies connecting-cluster geometry. | Cite as `[v0.14.4, Lemmas 8.5 and 8.6]`. |
| CR-9 | Decay rate | Theorem 8.7 | Theorem 8.7 states connected-support decay for every `m<m_beta`, where `m_beta=-log(M_0 Q(beta))`. | Cite as `[v0.14.4, Theorem 8.7]`. |
| CR-10 | OS-Seiler Hilbert space and transfer gap | Theorem 7.1, Theorem 11.1, Corollary 11.2, Theorem 12.1 | Theorem 7.1 proves Wilson-loop and OS Hilbert-space equality; Theorem 11.1 proves the transfer spectral gap; Corollary 11.2 gives endpoint inclusion; Theorem 12.1 gives the cumulative theorem. | Cite as `[v0.14.4, Theorem 7.1, Theorem 11.1, Corollary 11.2, and Theorem 12.1]`. |
| CR-11 | Evidence object | Appendix B and Appendix A | Appendix A gives numerical constants; Appendix B gives the machine-readable summary/evidence object. | Cite as `[v0.14.4, Appendices A and B]`. |

## 4. Additive confirmations beyond the punch-list

The v0.14.4 source confirms three items that strengthen v0.18.3 without changing its claim boundary.

1. **DLR uniqueness inline.** The status box and Section 1 state that the gauge-invariant infinite-volume DLR state is derived inline from polymer convergence.
2. **Localized RP norm.** Proposition 6.1 gives a localized RP norm bound, supporting the OS Hilbert-space equality proof.
3. **Companion-lane positioning.** Section 14.3 positions quantitative sharpening, obstruction survey, and RG-interface work as companion lanes after fixed-spacing submission.

## 5. Non-claim box

This audit does not claim:

- to rederive v0.14.4;
- to change v0.18.1 / v0.18.2 substantive content;
- to prove any new theorem;
- to extend v0.14.4;
- to supply continuum Yang-Mills construction;
- to make a Clay-level claim.

Positive claims:

- the 11 v0.18.2 cross-reference targets now have exact v0.14.4 anchors;
- the v0.18.3 manuscript can remove the `blocked on v0.14.4 source` notice;
- v0.18.3 can cite v0.14.4 without inventing lemma/proposition references.

## 6. Hopf-shell main/aux carry-forward

The v0.18.2 recommendation to split the Hopf-shell scaffold into a main obstruction survey plus auxiliary scaffold remains unchanged. The cross-reference audit does not affect that decision.

## 7. Bibliography normalization

Add the v0.14.4 manuscript entry if it is not already present in v0.18.3:

```bibtex
@misc{heller-v0144,
  author = {Heller, Michael D.},
  title = {Strong-Coupling Lattice Mass-Gap Seed v0.14.4},
  note = {Internal manuscript, CMP pre-submission consolidation},
  year = {2026}
}
```

## 8. v0.18.3 production checklist

1. Insert CR-1 through CR-11 citations in the v0.18.3 manuscript.
2. Add or normalize the v0.14.4 bibliography entry.
3. Remove the `blocked on v0.14.4 source` lock notice from the production note.
4. Preserve the non-claim box.
5. Compile twice with `pdflatex`.
6. Regenerate manifest and SHA256 hashes.
7. Package source, bibliography, PDF, README, and checksums.

## 9. Methodology discipline notes

This audit follows Methodology Manifesto v0.1:

- claim ledger discipline: citation-resolution only, no re-derivation;
- non-claim box discipline: no expansion of theorem scope;
- lane fallback discipline: Lane III hardens the survey while Lane VII remains proof-target work.

## 10. Audit summary

All 11 v0.18.2 cross-reference targets are now resolved to exact v0.14.4 anchors. v0.18.3 is ready for manuscript integration and build packaging.
