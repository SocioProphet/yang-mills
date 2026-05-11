# Yang-Mills Source Manifest — Moves 4 / 1 / 2

Repo-visible source manifest for the next execution tranche. Derived from the project file inventory and the frontier-state correction recorded on 2026-05-11.

The manifest binds each move to its load-bearing artifacts, records the non-claim boundaries those artifacts already pin, and fixes the execution order. Adjacent frameworks are mapped out of the YM lane so they cannot displace Move 4 / Move 2 work.

---

## Execution order (fixed)

| # | Move | Status | Blocking on |
|---|------|--------|-------------|
| 1 | **Move 4** — cross-reference hardening, v0.18.1 -> v0.18.2 | *materially ready* | nothing; source + survey both present |
| 2 | **Move 1** — arXiv/CMP publication packaging | *ready after Move 4* | Move 4 sign-off |
| 3 | **Move 2** — Wigner-gate G1/G2 progress | *reinforced; not optional* | symbolic 5x5 derivation, grid-vs-Galerkin comparison |
| 4 | **Lane VII** — synthesis lane | *active but conditional* | does not supersede Moves 4/2 until KP / closure gates move |
| — | Part Two / Part Three / v4.x | *backlog / frontier inputs* | held until Jmax=1 unblocks |

---

## Move 4 — cross-reference hardening

**Goal.** v0.18.1 obstruction survey -> v0.18.2, cross-referenced against the v0.14.4 constants table and non-claim box.

**Load-bearing sources.**

- `strong_coupling_lattice_mass_gap_seed_v0_14_4.pdf` — 2.0 MB
  *(`.tex` source not present in project drive; flag as missing if the GitHub repo carries it separately)*
- `ym_obstruction_survey_v0_18_1.pdf` — 3.1 MB

**Non-claim boundaries already pinned by v0.14.4 (do not erode in v0.18.2):**

- fixed-spacing
- strong-coupling
- gauge group SU(2)
- **not** continuum
- **not** SU(N >= 3)
- **not** Clay-eligible

**Action.** Pull the v0.14.4 constants table; verify each constant referenced in v0.18.1 against it; reconcile any drift; emit v0.18.2 with explicit cross-reference table and unchanged non-claim box.

---

## Move 1 — publication packaging

**Goal.** Package v0.14.4 (post-Move-4 reconciliation) for arXiv submission and CMP review pipeline.

**Anchor source.** `strong_coupling_lattice_mass_gap_seed_v0_14_4.pdf`. v0.14.4 already contains:

- arXiv-first submission strategy
- primary arXiv categories: **math-ph**, **hep-lat**
- secondary arXiv category (possible): **math.SP**
- primary journal target: **Communications in Mathematical Physics (CMP)**

**Action.** Once Move 4 is signed off, this is packaging and verification work only — no new mathematical claims. Verify the non-claim box, scrub forward-references to backlog items (Part Two / Three / v4.x), and assemble the arXiv tarball.

---

## Move 2 — Wigner-gate G1 / G2

**Goal.** Clear the two symbolic gates that currently block Jmax=1 scale-up.

**Load-bearing sources.**

- `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_20_complete_integrated_full_program_paper_expanded.pdf` — 2.3 MB
- `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.pdf` — 3.7 MB
- `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_28_full_running_copy_strategy_alignment.pdf` — 4.3 MB

**Gates as stated by v0.9.20 (verbatim posture):**

- **G1 (symbolic).** The symbolic 5x5 Wigner derivation is *not* complete. The Phi_111 structural-zero rule is plausible but **unproven**.
- **G2 (numerical).** Grid-vs-Galerkin comparison is **absent**.

**Consequence.** Jmax=1 is blocked until G1 and G2 pass. This is the substantive content of issue #30; Move 2 is not optional.

**Action.** Two parallel sub-tracks:

1. Symbolic — complete the 5x5 Wigner derivation; prove (or replace) the Phi_111 structural-zero rule.
2. Numerical — produce the grid-vs-Galerkin comparison artifact.

---

## Lane VII — boundary reference

**Source.** `lane_vii_consolidation_v2_0_1.pdf` — 1.3 MB.

**What v2.0.1 establishes (under normalized hypotheses):**

- tree Frobenius closure — proven
- one-cycle Frobenius closure — proven
- factorable two-cycle Frobenius closure — proven

**What v2.0.1 explicitly does *not* claim:**

- arbitrary cyclic Frobenius closure — **main open theorem**
- KP wall movement — not claimed
- v0.14.4 extension — not claimed
- continuum construction — not claimed
- Clay implication — not claimed

**Role in tranche.** Boundary reference for the adapter; ensures Lane VII language in v0.18.2 and the Move 1 packaging does not over-claim. Lane VII work continues in parallel but is **not permitted to displace Move 4 or Move 2** until KP-insertion / closure gates move.

---

## Backlog — Part Two / Part Three / v4.x

Inventoried as frontier inputs for the *next* tranche (N=3, Jmax=1, registry, coefficient constraints, orbit closure, K3 / face-regression, channel-product). Held until G1/G2 pass.

**Part Two track**
- `yang_mills_program_part_two_proof_strategy_roadmap.pdf`
- `yang_mills_program_part_two_v0_8_jmax1_scalar_restriction_gate_2.pdf`
- `YangMills_Program_Part_Two_v1_6__N3_Registry_Gate_Current_Upstream_Mount.pdf`
- `yang_mills_program_part_two_v2_9_wilson_n3_schema_s3_harness_full_running.pdf`

**Part Three v3.x progression**
- `yang_mills_program_part_three_v3_0_wilson_schema_face_regression.pdf`
- `yang_mills_program_part_three_v3_4_coefficient_constraints_s3_block_harness.pdf`
- `yang_mills_program_part_three_v3_7_full_running_manuscript.pdf`
- `yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.pdf`
- `yang_mills_program_part_three_v3_13_response_diagnostics_full_running.pdf`
- `yang_mills_program_part_three_v3_14_pair_lift_orbit25.pdf`
- `yang_mills_program_part_three_v3_15_orbit25_projection_closure.pdf`
- `yang_mills_program_part_three_v3_16_source_scalar_retriage.pdf`

**v4.x / Phase 4**
- `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.pdf`
- `yang_mills_phase4_v4_1_closure_addendum.pdf`

**Surface-expansion / related**
- `ym_strong_coupling_surface_expansion_v0_5.pdf`

---

## Lane VII supporting series (held with Lane VII)

- `lane_vii_holographic_invariant_memorandum_v0_1.pdf`
- `lane_vii_global_spin_network_closure_target_v0_5.pdf`
- `lane_vii_channel_aggregation_and_program_consolidation_v0_8.pdf`
- `lane_vii_cyclic_channel_vertex_audit_v1_0.pdf`
- `lane_vii_local_vertex_formula_identification_v1_10_1.pdf`

---

## Adjacent / out-of-lane

These do **not** move the Yang-Mills frontier state. Listed for inventory completeness and mapped to their correct adjacent lanes.

| Artifact | Lane |
|---|---|
| `brownian_holonomy_interface_v0_5.pdf` | adjacent apparatus / interface |
| `Lawful_Learning_Enriched_Specification_V2.pdf` | **hphd-zeta-mirror-lattice** (not yang-mills) |
| `Universal_Imitation_Games_Final_Arxiv.pdf` | adjacent framework |
| `CHAPTER1-QUANTUMSYMMETRY-OCT5.pdf` | adjacent framework |
| `temporal_mechanics_v0_24_1_reconstructed_full_source.pdf` | temporal-mechanics secondary line |
| `time_theory_draft_v23_layout_exec.pdf` | temporal-mechanics secondary line |
| `manuscript_v2_section1_with_figures.pdf` | manuscript fragment — verify provenance |
| `unification_graph_1.png` | figure |

---

## External references (bibliography pool)

Numbered / opaque-filename PDFs to be re-keyed with proper bib entries in Move 1 packaging.

- `0204014v1.pdf`
- `0912_4875.pdf`
- `1505_05069v2.pdf`
- `1609_08086.pdf`
- `186319421PB.pdf`
- `186319421PB1.pdf` ⚠️ byte-identical duplicate of `186319421PB.pdf` — dedupe before manifest commit
- `2369545.pdf`
- `bee519cca2da6543c2dedf64b9af3eed_MIT8_821S15_Lec24.pdf` *(MIT 8.821 Lecture 24)*
- `lecturesGQ.pdf`
- `paper43342.pdf`
- `rstb_2017_0374.pdf` *(Phil. Trans. Roy. Soc. B)*
- `s1005201971611.pdf`

---

## Inventory accounting

Uploaded transfer payload: **7 files**, containing the six load-bearing PDFs and this manifest.

Earlier project-drive inventory counted **46** files. Original expected count was 63, leaving **17 files unaccounted for**. Reconcile against the GitHub repo before treating the 46-file inventory as complete.

Known gaps to chase in the repo:

- `.tex` sources for v0.14.4 and v0.18.1 (PDFs only in transfer payload)
- Any additional v0.9.2x temporal-mechanics drafts
- Lane VII v2.0.1 `.tex` source

---

## Immediate next action

Commit this manifest, then begin Move 4: pull the v0.14.4 constants table, walk it against v0.18.1, emit v0.18.2 with cross-reference table appended and the non-claim box unchanged.
