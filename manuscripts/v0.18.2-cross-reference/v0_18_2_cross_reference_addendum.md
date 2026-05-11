# v0.18.2 Cross-Reference Addendum

**Scope.** Move 4 deliverable: v0.18.1 -> v0.18.2 cross-reference hardening against v0.14.4.

**Source basis.** `strong_coupling_lattice_mass_gap_seed_v0_14_4` and `ym_obstruction_survey_v0_18_1`, both hash-bound under `YangMillstransfer.zip` and validated in `yang-mills#31`.

**Claim discipline.** This addendum makes no new mathematical claim. It records constants verification, reference resolution, and non-claim alignment. v0.14.4's fixed-spacing SU(2) strong-coupling theorem boundary is unchanged. v0.18.2 remains an obstruction-survey/cross-reference hardening artifact, not a continuum construction or Clay proof.

---

## 1. Debt closed by this addendum

From v0.18.1 §Production-and-status-note (page 3, verbatim):

> "Exact v0.14.4 lemma/proposition cross-references remain deliberately
> unasserted because the exact v0.14.4 source was not found in the
> available uploaded/current file sources during this work session."

From v0.18.1 §v0.18 Errata (page 15, verbatim):

> "Remaining known debt: final publisher-style BibTeX cleanup and
> line-by-line audit against the v0.14.4 source once that source is
> available."

This addendum closes both items. The v0.14.4 source is now repo-resident
and hash-bound through the source-transfer manifest. The line-by-line audit
is recorded below in §2–§4.

---

## 2. Constants verification table

Every constant carried by v0.18.1 from v0.14.4 has been verified against
the v0.14.4 source. **No drift detected.**

| Quantity | v0.14.4 source | v0.18.1 stated | Match |
|---|---|---|---|
| $M_0 = 20e$ | $54.365636569180904$ (App. A, p. 13; §2 p. 3) | $20e \approx 54.366$ (§2.1, p. 4) | ✓ |
| $D_{\mathrm{inc}}$ | $21$ (App. A; §2 p. 3) | $D_{\mathrm{inc}} = 1+\Delta_\square = 21$ (§2.1, p. 4) | ✓ |
| $a^*$ | $0.4576898452957963$ (App. A; §2 p. 3) | $0.4576898452957963$ (§2.1, p. 5) | ✓ |
| $q_{\mathrm{KP}}$ | $0.006311768836893038$ (App. A; §2 p. 3) | $0.006311768836893038$ (§2.1, p. 5) | ✓ |
| $\beta^*$ | $0.006296889394074993$ (App. A; §2 p. 4) | $0.006296889394074993$ (§2.1, p. 5; Intro §1.1, p. 3) | ✓ |
| $Q(\beta^*) = q_{\mathrm{KP}}$ | App. A; §2 p. 4 | §2.1, p. 5 | ✓ |
| $\Delta_\square \leq 20$ on $\mathbb{Z}^4$ | Def. 8.1, p. 8 | §2.1, p. 4 | ✓ |
| KP condition $Q(\beta)e^a(D_{\mathrm{inc}} + a M_0) \leq a$ | Prop. 8.4, p. 9 | §2.1, p. 5 | ✓ |
| Activity bound $|z(\Gamma)| \leq Q(\beta)^{|\Gamma|}$ | Lemma 8.2, p. 8 | §2.1, p. 4 | ✓ |
| Rooted entropy $N_A^{\mathrm{root}} \leq M_0^{A-1}$ | Lemma 8.3, p. 8 | §2.1, p. 4 | ✓ |
| Gap formula $m_\beta = -\log(M_0 Q(\beta))$ | Thm. 11.1 / Thm. 12.1, p. 11–12 | §10, p. 13 | ✓ |
| Wilson plaquette weight $W_\beta(g) = e^{\beta \cos\theta_g}$ | §2, p. 3 | §2.1, p. 4 | ✓ |
| Character expansion $c_j(\beta) = I_{2j}(\beta) - I_{2j+2}(\beta)$ | §2, p. 3 | §2.1, p. 4 | ✓ |
| Normalized channel $r_j(\beta) = I_{2j+1}(\beta)/I_1(\beta)$ | §2, p. 3 | §2.1, p. 4 | ✓ |
| Topology-blind tail $Q(\beta) = \sum_{j>0} d_j^2 r_j(\beta)$ | §2, p. 3 | §2.1, p. 4 | ✓ |
| $q_{\mathrm{geo}} = 1/(20e)$ | (derived; not stated in v0.14.4) | $\approx 0.018394$ (§2.2, p. 5) | derived-OK |
| $q_{\mathrm{KP}}/q_{\mathrm{geo}} \approx 0.343$ | (derived) | §2.2, p. 5 | derived-OK |
| $m_{\beta^*} \approx -\log(0.343) \approx 1.07$ | (derived from Thm. 11.1) | §2.3, p. 5 | derived-OK |

**Result.** Every numerical constant in v0.18.1 that originates in v0.14.4
matches v0.14.4 to the digits stated. The three "derived-OK" entries are
quantities v0.18.1 computes from v0.14.4 inputs; the arithmetic is correct.

---

## 3. Lemma / proposition / theorem cross-reference table

Every version-label reference in v0.18.1 to v0.14.4 is now resolved to an
exact pointer.

| v0.18.1 reference | v0.14.4 target | v0.14.4 page |
|---|---|---|
| "Wilson polymer expansion as constituted in v0.14.4" (§2.1, p. 4) | §2 "Wilson data and constants" | 3–4 |
| "Wilson DLR specification" (§2.1, p. 4 inferred; §10 implicit) | Def. 3.1 "Wilson DLR specification" | 4 |
| "Gauge-invariant infinite-volume DLR state $\omega_\beta$" (§10, p. 13) | Thm. 3.2 "Gauge-invariant strong-coupling DLR limit" | 4 |
| "Local Wilson-loop polynomial algebra" (§10, p. 13; §12, p. 14) | Def. 5.1 "Local Wilson-loop polynomial algebra" | 5 |
| "Localized RP norm bound" (implicit in §10) | Prop. 6.1 "Localized RP norm bound" | 6 |
| "OS Hilbert-space equality" (§10, p. 13; §12, p. 14) | Thm. 7.1 "Wilson-loop and OS Hilbert spaces agree" | 7 |
| "Topology-blind activity bound" (§2.1, p. 4) | Lemma 8.2 "Topology-blind activity bound" | 8 |
| "Rooted plaquette-animal entropy with $M_0 = 20e$" (§2.1, p. 4) | Lemma 8.3 "Rooted plaquette-animal entropy" | 8 |
| "Kotecky–Preiss criterion verified in v0.14.4" (§2.1, p. 5) | Prop. 8.4 "Kotecky–Preiss verification" | 9 |
| "Mayer–Ursell denominator-cancellation argument" (§2.3, p. 5) | Lemma 8.5 "Denominator cancellation and connected source clusters" | 9 |
| "Connecting-cluster geometry" (implicit, §2) | Lemma 8.6 "Connecting-cluster geometry" | 10 |
| "Connected-correlation decay theorem" (implicit, §2.3) | Thm. 8.7 "Full connected-support strong-coupling decay" | 10 |
| "Discrete transfer operator $T_1$" (§10, p. 13) | §10 "Discrete transfer operator and spectral bookkeeping" | 10 |
| "Local strong convergence of transfers" (implicit, §10) | Prop. 10.1 | 11 |
| "Spectral gap $m_\beta$ above vacuum" (§10, p. 13) | Thm. 11.1 "Fixed-lattice-spacing transfer spectral gap" | 11 |
| "Endpoint spectral inclusion" (implicit) | Cor. 11.2 "Endpoint spectral inclusion" | 11 |
| "Cumulative fixed-spacing gap statement" (§1.1, p. 3 inline quote) | Thm. 12.1 "Cumulative fixed-spacing strong-coupling gap" | 12 |
| "Evidence object $E_{\mathrm{KP}} = (Q(\beta), M_0, D_{\mathrm{inc}}, a^*, q_{\mathrm{KP}}, \beta^*)$" (§3.4, p. 7; §10, p. 13) | App. A "Numerical constants" + §2 | 3–4, 13 |
| "Boundary data package $B_\beta$" (§12, p. 14) | aggregated from Def. 3.1, Thm. 3.2, Def. 5.1, Thm. 7.1, Thm. 11.1, App. A | — |
| Non-claim alignment (v0.18.1 §13) | v0.14.4 §15 "Not claimed" | 12–13 |

---

## 4. Non-claim box alignment

v0.14.4 §15 "Not claimed" and v0.18.1 §13 "Non-Claim Box" are
**complementary** rather than identical. v0.14.4 disclaims items its proof
method cannot reach. v0.18.1 adds survey-specific disclaimers covering the
auxiliary scaffolds it introduces (Hopf-shell language, neural-operator
callout, Einstein–Heller v1.6 companion).

Verification:

- v0.14.4 §15 items {continuum existence, asymptotic-freedom control,
  physical-scale gap, SU($N\geq 3$), Clay} ⊂ {disclaimers implicit or
  explicit in v0.18.1}. The v0.18.1 statement "a lattice gap is not a
  continuum gap" (§13 bullet 4) is the cross-document common denominator.
- v0.18.1 §13 items {Hopf geometry does not derive YM dynamics; an image
  does not determine its preimage; the continuum preimage fiber is not
  asserted nonempty; regularity-structures impossibility is not asserted;
  Einstein–Heller v1.6 is not a YM proof; neural operators do not certify a
  mass gap; obstructions catalogued are not asserted insurmountable} are
  survey-specific and do not require v0.14.4 counterparts.

**Conclusion.** Non-claim discipline is consistent. v0.18.2 inherits v0.18.1
§13 verbatim with one editorial change recorded in §5 below.

---

## 5. Bibliography update for v0.18.2

v0.18.1's bibliography (refs [1]–[51]) lacks a numbered entry for v0.14.4
because the source was unavailable at writing time. v0.18.2 adds:

```
[52] M. D. Heller. Strong-Coupling Lattice Mass-Gap Seed v0.14.4: CMP
     Pre-Submission Consolidation and Fixed-Spacing Transfer Gap.
     SocioProphet Research, May 2026. Source-transfer manifest in
     yang-mills#31; hash-bound under the v0.14.4 file SHA-256
     recorded in docs/status/YM_SOURCE_TRANSFER_RESULT.md.
```

Inline replacements throughout the v0.18.1 text:

- "v0.14.4" → "v0.14.4 [52]" at the first occurrence in each section.
- Constants and theorem citations in §2.1, §2.2, §2.3, §3.4, §10, §11, §12
  receive parenthetical labels per the §3 cross-reference table — e.g.,
  "the Kotecky–Preiss criterion verified in v0.14.4 [52, Prop. 8.4]".

These are editorial. They modify no claim.

---

## 6. Items requiring no change in v0.18.2

For the record, the following v0.18.1 content is unmodified by Move 4:

- All obstruction-type definitions (§1.2).
- The KP certificate-wall analysis (§2).
- The Hopf-shell auxiliary-scaffold framing (§3) including the
  removability disclaimer and the typed-placeholder caution.
- The image/preimage discipline (§4).
- The RG-as-shell-map analysis, including the Balaban-program treatment
  (§5).
- The stochastic-quantization quotient-preimage analysis (§6).
- The cluster-expansion locality-machine analysis (§7).
- The loop-equation / embedded-surface analysis (§8).
- The structural-/categorical-/neural-operator section (§9).
- The Lane II fiber-sensitive sharpening reframing (§11).
- The Lane IV interface-specification reframing (§12).
- The non-claim box (§13), with the §4 editorial alignment noted above.

---

## 7. Forward debt — what v0.18.2 still leaves open

Closed by this addendum: cross-reference debt, constants drift audit,
bibliography slot for v0.14.4.

Not addressed by this addendum (deferred to later v0.18.x or downstream
moves):

- Lane II §11 entropy-refinement sequence
  $M_0 \to M_{\mathrm{fib}}(\gamma) \to M_{\mathrm{surf}}(\gamma) \to M_{\mathrm{rep}}(\gamma) \to M_{\mathrm{cancel}}(\gamma)$
  remains a target program, not a deliverable.
- Lane IV §12 boundary-data package $B_\beta$ is a specification, not a
  constructed interface.
- v0.18 errata bullet (i)–(iv) editorial items (Einstein–Heller paragraph
  non-load-bearing flag, typed-placeholder caution, consolidated
  non-claims, publisher-style BibTeX cleanup) are within scope of v0.18.2
  copy editing but do not affect the cross-reference work above.

---

## 8. Sign-off

Move 4 deliverable produced. No drift detected. No mathematical claim
modified. Cross-reference table populated. Bibliography slot added.
Non-claim box alignment verified.

v0.18.2 is now packaging-only work: apply §3 pointer replacements inline,
insert §5 bibliography entry, recompile.

Move 1 (v0.14.4 arXiv/CMP package) is unblocked. v0.14.4 §14.1 already
declares the arXiv categories (math-ph primary, hep-lat cross-list, math.SP
possible secondary) and journal targets (CMP primary; Ann. Henri Poincaré,
Lett. Math. Phys., Rev. Math. Phys. as backups). Move 1 packaging requires
no further work from Move 4 beyond confirmation that the v0.14.4 source is
repo-resident and hash-bound — already true under `yang-mills#31`.
