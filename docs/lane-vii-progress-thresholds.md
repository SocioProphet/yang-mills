# Lane VII Progress Thresholds and Fallback Ledger

Status: governance ledger for Lane VII research continuation.
Date: 2026-05-09.

## Purpose

Lane VII is the current active synthesis/proof-target lane. It has produced real narrowing: tree-Frobenius aggregation, cyclic operator refutation, one-cycle Frobenius closure, recoupling unitarity, and residual non-recouping vertex obstruction.

This ledger defines when Lane VII is considered to be making proof-facing progress and when the program should pause Lane VII and revive narrower Lane II or other lanes.

## Active theorem target

The active theorem target remains cyclic Frobenius closure / subexponential residual defect:

```tex
|Contr(\Gamma)| <= C(\gamma) e^{o(|\Gamma|)} \prod_\ell \sqrt{C_{n_\ell/2}}.
```

Conditional wall target if closure and KP insertion both succeed:

```text
beta_Frob ~= 0.00735851805
```

This is not a theorem yet.

## What counts as progress

A Lane VII tranche counts as proof-facing progress if it does at least one of the following:

1. proves Frobenius closure for a new nontrivial class of channel graphs;
2. proves that a recoupling or vertex class is unitary/contractive/bounded with explicit norm;
3. identifies a concrete obstruction with an explicit defect factor;
4. proves the defect factor is subexponential in area;
5. proves the defect factor is absorbable into a still-improving activity constant;
6. proves a negative result that forces a clean route change.

## What does not count as enough progress

A tranche is insufficient if it only:

1. renames the obstruction without proving a new estimate;
2. adds a new formal layer without a computation/theorem/defect bound;
3. introduces a new screen/invariant vocabulary without KP-facing consequence;
4. postpones all quantitative work to a future tranche;
5. broadens the program surface without reducing the Frobenius-closure question.

## Pause thresholds

Pause Lane VII and revive narrower Lane II or another lane if any of the following occurs:

1. Two consecutive Lane VII tranches fail to produce a theorem, computation, defect estimate, or hard obstruction.
2. Residual vertex/cycle defect is shown to be Catalan-scale for generic cubic polymers.
3. Boundary/source prefactors grow exponentially with polymer area in the Wilson-screen setup.
4. Frobenius closure is shown not to be KP-insertable even when local/channel estimates hold.
5. The active theorem target splits into more than two unclosed sub-obstructions without resolving any previous obstruction.

## Continue thresholds

Continue Lane VII if any of the following occurs:

1. Residual vertex defect is absent after unitary normal form decomposition.
2. Residual vertex defect is present but subexponential.
3. Residual vertex defect is exponential with a constant that still leaves a wall-moving activity.
4. Cyclic Frobenius closure is proved for beta_1=1 and beta_1=2 plus a credible induction path exists.
5. KP insertion audit identifies no structural barrier after closure.

## Lane II fallback

Lane II should be revived if Lane VII route becomes Catalan-scale or not KP-insertable.

Lane II fallback target:

```text
Surface / representation / cancellation entropy estimates on the original cubic regulator.
```

Specifically:

1. return to `S_A(gamma)` surface entropy for rectangular Wilson loops;
2. recover representation-admissible grammar from Lane II v0.1-v0.5;
3. use Lane VII results only as diagnostics, not as load-bearing theorem claims;
4. attempt a narrower fixed-spacing certificate sharpening that does not depend on arbitrary cyclic Frobenius closure.

## Lane VI fallback

Lane VI should be revived if cubic regulator closure becomes Catalan-scale but regulator geometry remains promising.

Lane VI fallback target:

```text
near-edge-regular triangulated S^4 regulator families with kappa_1 <= 6.
```

This remains a diagnostic lane until reflection/transfer structure is built.

## Current next decision

Proceed to:

```text
Lane VII v1.7-FRI: Residual Vertex Defect Density Audit
```

Success criterion:

- identify the first non-recouping Wilson/Reisenberger vertex;
- count residual closed-loop/trace factors after unitary recoupling decomposition;
- classify defect density as absent, subexponential, absorbable exponential, or Catalan-scale.

## Claim boundary

This ledger is governance only. It does not prove or disprove Frobenius closure, does not move the KP wall, and does not alter v0.14.4.
