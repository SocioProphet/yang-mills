# Lane II Fiber-Sensitive Sharpening - Theorem Target

Status: theorem-track planning document.

## Purpose

Lane II should produce the next theorem-track artifact after v0.14.4. The target is not a Clay-level result and not a continuum result. The target is a quantitative sharpening of the fixed-spacing strong-coupling theorem by replacing the topology-blind rooted plaquette-animal entropy constant

```text
M0 = 20e ~= 54.365636569180904
```

with an effective entropy constant that counts a smaller, boundary-sensitive class of objects.

## Why this matters

v0.18.1 identifies the KP wall and the geometry wall as distinct. The KP certificate wall occurs when the optimized Kotecky-Preiss sufficient condition stops certifying absolute convergence:

```text
qKP = 0.006311768836893038
beta* = 0.006296889394074993
```

The weaker rooted-animal geometry wall is

```text
Q(beta) < 1/M0 = 1/(20e) ~= 0.018393972058572116
beta_geo ~= 0.018268566487422343
```

This means the current proof has certificate slack: the KP wall appears before the cruder geometry-only wall. Lane II should use that diagnosis to replace the counting object rather than merely retune the KP optimization.

## Object hierarchy

The current v0.14.4 majorant counts all rooted connected plaquette animals. Lane II should refine the hierarchy:

```text
P_all(A)  superset  P_A(gamma)  superset  S_A(gamma)  superset  S_rep_A(gamma)  superset  S_cancel_A(gamma)
```

Working interpretation:

- `P_all(A)`: all connected plaquette animals of size A rooted at a plaquette.
- `P_A(gamma)`: boundary-reaching connected plaquette animals of size A relevant to loop boundary gamma.
- `S_A(gamma)`: admissible embedded or immersed plaquette surfaces of area A with boundary gamma.
- `S_rep_A(gamma)`: representation-admissible surface/polymer configurations surviving the SU(2) character/Haar constraints.
- `S_cancel_A(gamma)`: configurations after representation-theoretic and Mayer-Ursell cancellation.

Corresponding entropy constants:

```text
M0 -> M_fib(gamma) -> M_surf(gamma) -> M_rep(gamma) -> M_cancel(gamma)
```

The first theorem should target `M_surf`, not `M_cancel`. The representation and cancellation layers are likely harder and should be second-stage refinements.

## First concrete theorem target

### Theorem target A: boundary-surface entropy replacement

Let `gamma` be a fixed rectangular Wilson loop or, more generally, a fixed finite lattice loop with a chosen spanning plaquette surface. Let `S_A(gamma)` denote the class of connected plaquette surfaces with boundary gamma and area A, rooted by a boundary plaquette or another canonical boundary marker. Prove an estimate of the form

```text
#S_A(gamma) <= C_gamma * M_surf^(A - A_min(gamma))
```

where:

- `A_min(gamma)` is the minimal plaquette area of a surface spanning gamma;
- `C_gamma` depends on gamma but not on separation/time extent in the transfer-gap estimate after normalization;
- `M_surf < M0 = 20e` is explicit;
- the estimate is uniform over the classes of loops needed by the connected-support decay theorem.

A successful theorem then replaces the topology-blind factor `M0 Q(beta)` by `M_surf Q(beta)` in the relevant geometry tail, subject to proof that the polymer expansion contribution can be reorganized over this smaller class without losing absolute-convergence control.

## Second concrete theorem target

### Theorem target B: representation-admissible entropy replacement

Define `S_rep_A(gamma)` as the subclass of `S_A(gamma)` whose plaquette representation labels satisfy the edge-incidence constraints imposed by SU(2) Haar integration. Prove

```text
#S_rep_A(gamma) <= C_gamma * M_rep^(A - A_min(gamma))
```

with explicit `M_rep <= M_surf`, and ideally strict inequality. This theorem requires a clean representation-label grammar for admissibility.

## Third concrete theorem target

### Theorem target C: cancellation-aware bound

After a stable surface/representation grammar exists, identify a signed or weighted cancellation quotient. The target is not a bare cardinality bound but an activity-weighted estimate:

```text
sum_{sigma in S_rep_A(gamma)} |effective_weight_after_cancellation(sigma)| <= C_gamma * (M_cancel Q(beta))^A
```

This is likely a later paper. It should not block the first Lane II theorem.

## Numerical payoff table

The following table uses the same `Q(beta)` convention as v0.14.4/v0.18.1 and solves `Q(beta_wall) = 1/M_eff`. It is only a payoff diagnostic; it is not a theorem.

| Entropy reduction | M_eff | 1/M_eff | beta geometry wall |
| ---: | ---: | ---: | ---: |
| 0% / baseline | 54.3656365692 | 0.0183939721 | 0.0182685665 |
| 10% reduction | 48.9290729123 | 0.0204377467 | 0.0202831239 |
| 25% reduction | 40.7742274269 | 0.0245252961 | 0.0243032094 |
| 33.3% reduction | 36.2437577128 | 0.0275909581 | 0.0273104181 |
| 50% reduction | 27.1828182846 | 0.0367879441 | 0.0362920532 |

Interpretation: even a modest explicit reduction of the entropy constant materially widens the geometry-control window. This does not remove the finite-window limitation, because any finite entropy constant still gives a finite strong-coupling window and the continuum trajectory requires `beta_lat(a) -> infinity`.

## Proof obligations

1. **Boundary normalization.** Define the admissible loop family needed by the transfer-gap proof and normalize constants so that `C_gamma` does not destroy the large-separation decay estimate.
2. **Surface extraction.** Show that every polymer contributing to the Wilson-loop connected-correlation numerator maps to at least one boundary-reaching plaquette surface or controlled surface-like core.
3. **Multiplicity control.** Bound the number of polymers mapping to the same surface core, or absorb the multiplicity into an explicit corrected entropy constant.
4. **Uniformity.** Make constants independent of finite volume and stable under the infinite-volume DLR limit.
5. **Compatibility with KP.** State whether the new estimate replaces only the geometry tail or also enters the KP incompatible-polymer sum. These are different upgrades.
6. **Representation grammar.** For target B, define admissible SU(2) label configurations at edges and plaquettes.
7. **Cancellation discipline.** For target C, never convert signed cancellation into a theorem without absolute or conditionally justified convergence controls.

## Minimal publishable Lane II paper

A first Lane II paper can be publishable if it proves target A with any explicit `M_surf < M0`, propagates the replacement through the fixed-spacing transfer-gap theorem, and clearly states the resulting improved certified window. It does not need to solve representation cancellation.

## Non-claim box

This Lane II program does not claim:

- a continuum Yang-Mills construction;
- a Clay mass-gap proof;
- control along `beta_lat(a) -> infinity`;
- SU(N) for N >= 3;
- that `beta*` is a true convergence boundary;
- that the surface entropy constant exists below `M0` without proof;
- that cancellation can be used without a justified convergence framework.

## Next two proof moves

1. Define `S_A(gamma)` for rectangular loops and prove a first crude bound using surface-growth rather than animal-growth combinatorics.
2. Build a transfer-gap compatibility lemma showing exactly where `M_surf` may replace `M0` without invalidating the v0.14.4 proof chain.
