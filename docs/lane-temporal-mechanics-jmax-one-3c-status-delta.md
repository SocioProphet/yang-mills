# Lane Temporal-Mechanics Jmax = 1 Phase 3c — Status Delta

**Track**: `docs/lane-temporal-mechanics-jmax-one-3c-status-delta.md`
**Date**: 2026-05-09
**Predecessor**: Phase 3b — Jmax = 1 Gram matrix (referee-pending).

## What this delta records

Phase 3c — Jmax = 1 → Jmax = 1/2 truncation regression — passes all four checks at machine precision:
- C1: V_phi111 = 0.28492504932683558... (16-figure agreement, Phase 2 V6 re-confirmed)
- C2: Scalar A(1) matrix matches v2.9 Appendix A to 9-figure precision (App A's published precision floor)
- C3: A⊗A normalized spectrum matches v2.9 §F.2 to float64 noise (5×10⁻¹⁶)
- C4: λ_0 = 1.854445494147494 vs target 1.854445494147492 (2.4×10⁻¹⁵ diff, float64 noise)

Full 5-dim spectrum [1, 0.17796184, 0.17796184, 0.04377712, 0.03167042] reproduced to 15+ figures across every rank.

## Convention finding (must be flagged for referee)

A discrepancy between v0.9.27 §19 verbal description ("M_γ = exp(γ χ_{1/2}(P))") and v2.9 Appendix A numerical convention ("M_γ = exp(γ a_0)" effectively) is documented. The v2.9 App A convention is taken as load-bearing for Phase 3d; Phase 5 (literal 3j/6j R-table) is the natural place for first-principles resolution.

## Phase plan position

Execution order **2 → 3a → 3b → 3c → 4 → 3d → 5 → 6**. Position: 3c locked, Phase 4 next.

## What this deliverable does NOT advance

Per Phase 3c source.md §8: no full 14-dim Jmax = 1 transfer matrix (3d), no β-trend (blocked per v2.9 §F.6), no R-table (5), no continuum / SU(N) / Clay claims. Convention finding documented but not resolved at first-principles level.

## Successor pointer

Phase 4: Manifesto v0.2 cross-track refresh. Five-witness validation across Lane III, Lane VII, temporal mechanics monograph, temporal mechanics computation, and Yang-Mills Program Part Two.

## No-claim discipline

This delta records a numerical-regression deliverable. It does not claim any new theorem or derivation. The convention finding is a methodological observation, not a new technical result.
