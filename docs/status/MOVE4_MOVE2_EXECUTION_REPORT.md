# Move 4 / Move 2 Execution Report

**Date:** 2026-05-11
**Source basis:** Files received under `YangMillstransfer.zip`
(SHA-256 `e9b6a26391b17858377362a15593e6a44c15fe004a91401c18bb034314e628a1`,
7 files, validated via `yang-mills#31` and recorded in
`docs/status/YM_SOURCE_TRANSFER_RESULT.md`).

---

## Files read end-to-end

| File | Pages | Status |
|---|---|---|
| `strong_coupling_lattice_mass_gap_seed_v0_14_4` | 15 | full read, constants extracted |
| `ym_obstruction_survey_v0_18_1` | 18 | full read, all v0.14.4 references located |
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_20` | 12 | scanned for G1/G2 gate definitions |
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27` | 34 | scanned for Wigner translation precursor |
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_28` | 37 | full §21 read (Wigner/Peter-Weyl convention) |

**Data-shape note for the repo record.** The `.pdf` extensions in
`YangMillstransfer.zip` are ZIP archives of per-page JPEG + extracted `.txt`
+ `manifest.json`, not true PDF objects. This is the existing project-drive
format. No remediation is required for Move 4/2 execution because the
`.txt` payloads are clean. If a future tranche needs true PDF objects (for
e.g. font-embedding audits or referee-style annotation), this is recorded
here as a known format constraint.

---

## Move 4 — completed

**Deliverable:** `v0_18_2_cross_reference_addendum.md`.

**What was done.**

1. Every numerical constant carried by v0.18.1 from v0.14.4 was verified
   against the v0.14.4 source. **No drift detected** across 16 quantities
   ($M_0$, $D_{\mathrm{inc}}$, $a^*$, $q_{\mathrm{KP}}$, $\beta^*$,
   $Q(\beta^*)$, $\Delta_\square$, KP condition, activity bound, rooted
   entropy, gap formula, Wilson weight, character expansion, normalized
   channel, topology-blind tail, derived ratios $q_{\mathrm{geo}}$,
   $q_{\mathrm{KP}}/q_{\mathrm{geo}}$, $m_{\beta^*}$).

2. Every version-label reference in v0.18.1 to v0.14.4 was resolved to an
   exact lemma/proposition/theorem pointer with page reference. 19 distinct
   pointers were tabulated.

3. The v0.18.1 self-recorded debt was closed:
   - Page 3 production-and-status-note: "Exact v0.14.4 lemma/proposition
     cross-references remain deliberately unasserted" — **closed**.
   - Page 15 errata: "Remaining known debt: ... line-by-line audit against
     the v0.14.4 source once that source is available" — **closed**.

4. Non-claim alignment between v0.14.4 §15 and v0.18.1 §13 was verified.
   v0.18.1's box is complementary (survey-specific disclaimers added on
   top of v0.14.4's theorem-method disclaimers). The cross-document common
   denominator is the "lattice gap is not a continuum gap" statement.
   **No realignment required.**

5. v0.14.4 will be added as numbered reference [52] in the v0.18.2
   bibliography. Inline replacements specified throughout v0.18.1 §2, §3,
   §10, §11, §12.

**What was not done (and is correctly out of scope for Move 4).**

- Lane II §11 entropy-refinement sequence
  $M_0 \to M_{\mathrm{fib}} \to M_{\mathrm{surf}} \to M_{\mathrm{rep}}
  \to M_{\mathrm{cancel}}$ remains a forward program.
- Lane IV §12 boundary-data package $B_\beta$ remains a specification.
- v0.18 errata bullets (i)–(iv) editorial items are within v0.18.2 copy-
  editing scope, separate from the cross-reference work.

**v0.18.2 production step.** Apply the §3 pointer replacements inline,
insert the §5 bibliography entry, recompile. No mathematical content
changes.

**Move 4 ⇒ Move 1 unblock.** Move 1 (v0.14.4 arXiv/CMP package) is now
fully unblocked. v0.14.4 §14.1 already declares arXiv categories (math-ph
primary, hep-lat cross-list, math.SP possible) and journal targets (CMP
primary; Ann. Henri Poincaré, Lett. Math. Phys. as backups). Move 1
packaging requires no further input from Move 4.

---

## Move 2 — convention declaration and basis freeze completed

**Deliverable:** `move2_wigner_conventions_freeze_v0_1.md`.

**What was done.**

1. **Integer label convention** $n = 2j$ declared and table of small-$n$
   roles provided.

2. **Audit-basis enumeration frozen** in order
   $(\Phi_{000}, \Phi_{100}, \Phi_{010}, \Phi_{110}, \Phi_{111})$ with
   explicit quaternion forms and sector labels.

3. **Block decomposition frozen** as scalar $4\times 4$ + $\Phi_{111}$
   $1\times 1$, parity-protected by inversion symmetry.

4. **Peter–Weyl / Wigner form** for $\Phi_{111}$ declared:
   $\Phi_{111}(P,Q) = (1/\sqrt{3})\sum_M (-1)^M T_M(P) T_{-M}(Q)$
   with the standard complex spherical-basis convention
   $T_{\pm 1} = \mp(X_1 \pm iX_2)/\sqrt{2}$, $T_0 = X_3$.

5. **Wigner–Eckart form** for the $\Phi_{111}$ block declared:
   $B^{(1)}_{r,n}(\gamma) = \sum_m a_m(\gamma) R^{(1)}_{m,n,r}$
   with $R^{(1)}_{m,n,r}$ identified as the $\ell=1$-preserving recoupling
   coefficient.

6. **Inversion-symmetry zero rule** (v0.9.28 §21.3) recorded verbatim with
   proof structure as the structural-zero theorem protecting the 4+1
   decomposition.

7. **3j/6j convention** discipline declared. Working choice: Edmonds with
   $R^{(1)}_{0,1,1} > 0$ as the global sign gauge. Alternate conventions
   (Varshalovich–Moskalev–Khersonskii, Racah) listed as acceptable
   substitutes if explicitly flagged.

8. **Numerical anchors** locked at $\beta_t = \beta_s = 1$:
   - scalar spectrum $[1, 0.17796184, 0.17796184, 0.03167042]$;
   - $\Phi_{111} = 0.04377712$;
   - $V = 0.284925049327$.

9. **G1 acceptance criterion:** reproduce $V$ symbolically from the
   $R^{(1)}_{m,1,r}$ table in the declared 3j/6j convention, without
   quaternion/Haar arithmetic in the final certificate.

10. **G2 acceptance criterion:** reproduce both the scalar 4×4 spectrum
    and the $\Phi_{111}$ value from a deterministic reduced-coordinate
    grid using the projection/measure/half-density convention declared in
    `CONVENTIONS.md`.

11. **Jmax = 1 scale-up** held until G1, G2, and repository-grade
    reproduction gates pass.

**What is correctly not closed by Move 2 (still open).**

- G1: the explicit $R^{(1)}_{m,1,r}$ table itself.
- G2: the grid-projection repair.
- Repository-grade reproduction (code + fixtures regenerating basis,
  matrices, spectra, graphs, tables, PDF outputs).

These are the actual symbolic / numerical work tracks. Move 2 (basis
freeze) creates the **fixed reference** against which they are evaluated.

---

## Files for download

- `v0_18_2_cross_reference_addendum.md` — Move 4 deliverable.
- `move2_wigner_conventions_freeze_v0_1.md` — Move 2 basis-freeze deliverable.
- This report.

---

## Updated frontier state

```
Move 4 — COMPLETE.
  v0.18.1 → v0.18.2 cross-reference table populated.
  All 16 carried constants verified against v0.14.4. No drift.
  v0.14.4 numbered bibliography slot specified.
  v0.18.2 is now packaging-only work.

Move 1 — UNBLOCKED, ready to package.
  v0.14.4 §14.1 already declares arXiv categories and journal targets.
  No further input required from Move 4.

Move 2 — BASIS-FREEZE COMPLETE; G1 and G2 still open.
  Wigner / Peter-Weyl convention declared.
  Jmax=1/2 audit-basis ordering frozen.
  Block decomposition 4+1 frozen with structural-zero protection.
  Numerical anchors at β_t = β_s = 1 locked.
  3j/6j convention working choice: Edmonds with R^(1)_{0,1,1} > 0.
  Jmax = 1 scale-up explicitly held.

Lane VII v2.0.1 — UNCHANGED.
  Boundary reference. Does not supersede Move 4 or Move 2.
```

---

## No claims made

No theorem was proved. No mass gap was claimed (lattice, fixed-spacing,
continuum, or Clay). No SU($N \geq 3$) result was claimed. No
asymptotic-freedom trajectory result was claimed. No G1 closure was
claimed. No G2 closure was claimed. No wall movement was claimed in
v0.18.2 — v0.18.2 is editorial cross-reference work over v0.18.1.

The v0.14.4 scoped claim (SU(2), fixed spacing $a > 0$, $\beta < \beta^* =
0.006296889394074993$, positive transfer gap above vacuum on the
infinite-volume gauge-invariant OS reflection-positive Hilbert space) is
unchanged.
