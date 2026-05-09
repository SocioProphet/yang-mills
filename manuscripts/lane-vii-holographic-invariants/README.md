# Lane VII Holographic Screen-Invariant Synthesis

Status: canonical manuscript folder for Lane VII artifacts.

## Purpose

Lane VII consolidates the Yang-Mills strong-coupling program around a holographic screen-invariant formulation. It interprets Lane II polymer refinements, Lane VI regulator diagnostics, Lane IV preimage/interface discipline, and Brownian Holonomy cautions as input to a single proof-facing question:

```tex
\text{Does the Wilson-screen fiber entropy admit a Frobenius spin-network closure strong enough to improve the v0.14.4 KP certificate?}
```

## Current state

The current consolidated artifact is:

```text
Lane VII Consolidation v1.2-FRI
Screen Fiber Entropy, Spin-Network Closure, and the Frobenius Aggregation Frontier
```

The current main theorem target is the Frobenius Closure Theorem for arbitrary cyclic channel graphs:

```tex
|Contr(\Gamma)| <= C(\gamma) e^{o(|\Gamma|)} \prod_\ell \sqrt{C_{n_\ell/2}}.
```

The proved partial result is the tree-Frobenius aggregation theorem under normalized tree-tensor hypotheses. The first cyclic rank-2 test saturates Frobenius and demotes global operator closure to a sectoral/cancellation-dependent branch.

## Version chain

| Version | Role |
| --- | --- |
| v0.1-FRI | Defines generalized holography as invariant descent through screen projection and selects activity-weighted Wilson-screen fiber entropy as primary KP-compatible invariant. |
| v0.5-FRI | Specifies global spin-network closure theorem target and literature spine. |
| v0.8-FRI | Consolidates Channel Aggregation Lemma target and current program direction. |
| v1.0-FRI | Introduces cyclic-channel/normalized vertex audit and tree-Frobenius theorem direction. |
| v1.2-FRI | Framework/theorem consolidation paper: tree-Frobenius theorem, two-rank-2 cycle test, Frobenius frontier. |

## Repository capture status

This PR captures Lane VII status and artifact hashes. TeX/PDF source import is tracked in `docs/lane-vii-artifact-manifest.md` and follow-up backlog items.

Canonical source policy:

1. TeX/Markdown source is the source of truth.
2. PDFs are distribution builds.
3. Binary PDFs should be added through a binary-safe path: release assets, Git LFS, or artifact storage.
4. Every artifact must have claim scope, build receipt, and SHA256 hash.

## Claim boundary

Lane VII does not currently claim:

- proof of Frobenius closure for arbitrary cyclic channel graphs;
- proof of KP insertion of the Frobenius hybrid activity;
- movement of the v0.14.4 certificate wall as a theorem;
- continuum Yang-Mills construction;
- Clay-level result.

Lane VII does currently claim:

- a formal screen-invariant framework for the program;
- a screen-transfer architecture for Wilson-screen fiber entropy;
- a closure hierarchy `q_op <= q_Frob <= q_Cat`;
- tree-Frobenius aggregation under normalized tree-tensor hypotheses;
- a two-rank-2 cyclic test that saturates Frobenius and refutes global operator closure;
- a precise next theorem target: cyclic Frobenius closure / subexponential cycle defect.

## Next work

1. Import TeX source for v0.1, v0.5, v0.8, v1.0, and v1.2.
2. Attach PDFs through binary-safe distribution path.
3. Add build receipts for all Lane VII artifacts.
4. Attempt Lane VII v1.3: cyclic Frobenius closure for beta_1 = 1 and beta_1 = 2 cases.
5. After closure proof or obstruction, run KP insertion audit.
