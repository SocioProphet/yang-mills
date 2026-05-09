# Lane VII Artifact Manifest

Status: export manifest seeded from local Lane VII PDF/TeX builds.
Date: 2026-05-09.

## Policy

Markdown/LaTeX source is canonical. PDFs are distribution artifacts. The current GitHub content API path used in this pass captures source/hash metadata first; binary PDFs may be attached later through release assets, Git LFS, or a binary-safe upload path.

## Exported artifacts

| Version | Title | Local source file | TeX SHA256 | Local PDF file | PDF SHA256 | Status |
| --- | --- | --- | --- | --- | --- | --- |
| v0.1-FRI | Holographic Invariant Memorandum | `lane_vii_holographic_invariant_memorandum_v0_1.tex` | `969b469ef5689c11550b57a6f3e842a87424622d012d1231f8d306aaa290028f` | `lane_vii_holographic_invariant_memorandum_v0_1.pdf` | `8b1902450371bbcab1880914a3eb6b128c64f7227bcb6dca8ec0f56ac052f50c` | Exported locally; first Lane VII synthesis artifact. |
| v0.5-FRI | Global Spin-Network Closure Target and Literature Spine | `lane_vii_global_spin_network_closure_target_v0_5.tex` | `8debfd97432f248b92cfb41f4839d6fa22e50f575b4111e2ffbdd9d031373c88` | `lane_vii_global_spin_network_closure_target_v0_5.pdf` | `76bbfee09c47a7d129e7d2fde83d5de4c889568092246b10af17390144ac0a55` | Exported locally; closure theorem target and literature spine. |
| v0.8-FRI | Channel Aggregation and Program Consolidation | `lane_vii_channel_aggregation_and_program_consolidation_v0_8.tex` | `d6f6d549df3dc27a9cdc147f5abfb67656afeeacb670f556871a0985ddb78805` | `lane_vii_channel_aggregation_and_program_consolidation_v0_8.pdf` | `fbf2b51883836239ca0f465b75f3da0bb88ff327d816932db619ee3758e4dfdb` | Exported locally; Channel Aggregation Lemma target. |
| v1.0-FRI | Cyclic Channel Defects, Normalized Vertex Audit, and Program Consolidation | `lane_vii_cyclic_channel_vertex_audit_v1_0.tex` | `3a3ee8526dabba5e02e3afdcfcbdc8523165dafe3b75ff4840ce70b0984d1037` | `lane_vii_cyclic_channel_vertex_audit_v1_0.pdf` | `ec2adc9073d4e30916ec15425feed6634d16008f73f88f05f660cd1043ee3de0` | Exported locally; tree theorem + cycle-defect target. |
| v1.2-FRI | Screen Fiber Entropy, Spin-Network Closure, and the Frobenius Aggregation Frontier | `lane_vii_screen_fiber_spin_network_frobenius_frontier_v1_2.tex` | `1d9643b97e8de5bd2e017de03a4d5c4f6b7ca492436e16a887c7e280d0a21dcc` | `lane_vii_screen_fiber_spin_network_frobenius_frontier_v1_2.pdf` | `826b197dc8945b16c83adf8c525be3ab0504e4ac72e2130b981bc5ae62eb5956` | Exported locally; framework/theorem consolidation paper. |

## Claim boundary for all artifacts

The Lane VII exports do not claim:

- continuum Yang-Mills construction;
- Clay mass-gap proof;
- weak-coupling/asymptotic-freedom control;
- extension to SU(N >= 3);
- movement of the v0.14.4 KP wall as a theorem;
- proof of Frobenius closure for arbitrary cyclic channel graphs;
- proof that the Frobenius hybrid activity can be inserted into the v0.14.4 KP certificate.

## Positive program state

The artifact chain establishes:

1. generalized holography as invariant descent through screen projection;
2. Wilson-screen fiber entropy as the KP-compatible primary invariant;
3. screen-transfer architecture and closure hierarchy;
4. tree-Frobenius aggregation theorem under normalized hypotheses;
5. two-rank-2 cycle test that saturates Frobenius and demotes global operator closure;
6. arbitrary cyclic Frobenius closure as the active theorem target.

## Missing repository captures

Still to add in later PRs:

- actual TeX sources under `manuscripts/lane-vii-holographic-invariants/` for each exported version;
- binary PDFs via binary-safe path or Git LFS/release assets;
- Lane IV consolidation artifacts;
- Brownian Holonomy v0.5 sidecar;
- Lane VI spherical/simplicial regulator notes;
- build receipts for all Lane VII exports.
