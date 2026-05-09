# Lane VII Artifact Manifest

Status: export manifest seeded from local Lane VII PDF/TeX builds and chat/source tranche ledger.
Date: 2026-05-09.

## Policy

Markdown/LaTeX source is canonical. PDFs are distribution artifacts. Binary PDFs may be attached later through release assets, Git LFS, or a binary-safe upload path.

## Exported artifacts

| Version | Title | Local source file | TeX SHA256 | Local PDF file | PDF SHA256 | Status |
| --- | --- | --- | --- | --- | --- | --- |
| v0.1-FRI | Holographic Invariant Memorandum | `lane_vii_holographic_invariant_memorandum_v0_1.tex` | `969b469ef5689c11550b57a6f3e842a87424622d012d1231f8d306aaa290028f` | `lane_vii_holographic_invariant_memorandum_v0_1.pdf` | `8b1902450371bbcab1880914a3eb6b128c64f7227bcb6dca8ec0f56ac052f50c` | Exported locally; first Lane VII synthesis artifact. |
| v0.5-FRI | Global Spin-Network Closure Target and Literature Spine | `lane_vii_global_spin_network_closure_target_v0_5.tex` | `8debfd97432f248b92cfb41f4839d6fa22e50f575b4111e2ffbdd9d031373c88` | `lane_vii_global_spin_network_closure_target_v0_5.pdf` | `76bbfee09c47a7d129e7d2fde83d5de4c889568092246b10af17390144ac0a55` | Exported locally; closure theorem target and literature spine. |
| v0.8-FRI | Channel Aggregation and Program Consolidation | `lane_vii_channel_aggregation_and_program_consolidation_v0_8.tex` | `d6f6d549df3dc27a9cdc147f5abfb67656afeeacb670f556871a0985ddb78805` | `lane_vii_channel_aggregation_and_program_consolidation_v0_8.pdf` | `fbf2b51883836239ca0f465b75f3da0bb88ff327d816932db619ee3758e4dfdb` | Exported locally; Channel Aggregation Lemma target. |
| v1.0-FRI | Cyclic Channel Defects, Normalized Vertex Audit, and Program Consolidation | `lane_vii_cyclic_channel_vertex_audit_v1_0.tex` | `3a3ee8526dabba5e02e3afdcfcbdc8523165dafe3b75ff4840ce70b0984d1037` | `lane_vii_cyclic_channel_vertex_audit_v1_0.pdf` | `ec2adc9073d4e30916ec15425feed6634d16008f73f88f05f660cd1043ee3de0` | Exported locally; tree theorem + cycle-defect target. |
| v1.2-FRI | Screen Fiber Entropy, Spin-Network Closure, and the Frobenius Aggregation Frontier | `lane_vii_screen_fiber_spin_network_frobenius_frontier_v1_2.tex` | `1d9643b97e8de5bd2e017de03a4d5c4f6b7ca492436e16a887c7e280d0a21dcc` | `lane_vii_screen_fiber_spin_network_frobenius_frontier_v1_2.pdf` | `826b197dc8945b16c83adf8c525be3ab0504e4ac72e2130b981bc5ae62eb5956` | Exported locally; framework/theorem consolidation paper. |
| v1.6-FRI | First Non-Recoupling Vertex Audit | `lane_vii_first_non_recoupling_vertex_audit_v1_6.tex` | `5a01cdf0495f666cd548b7d4a5e9d2499ead13f154e2913309455f58408155a5` | `lane_vii_first_non_recoupling_vertex_audit_v1_6.pdf` | `5be7fbc7468247df174ea4b5f3afcaf0b65fde3962a655403aef0fa2e3bf8652` | Exported locally; recoupling/non-recouping vertex audit and residual trace/loop density obstruction. |
| v1.9.1-FRI | Residual Operator Patch and Canonical Vertex-Audit Protocol | `lane_vii_residual_operator_patch_v1_9_1.tex` | `3cd6245198716910e8a016d8ff07cc0fff25dfdbdeea0c63570efa60d20c49b3` | `lane_vii_residual_operator_patch_v1_9_1.pdf` | `927bb81e3a07238b275f5f35f0f906702ddf117b147ebefcbc4f8602b761e91f` | Exported locally; corrective patch replacing scalar residual with typed residual operator and defining v1.10 vertex-formula extraction target. |

## Source-captured artifacts not yet exported

| Version | Title / role | Repository source | Status |
| --- | --- | --- | --- |
| v2.0.1-FRI | Polish Patch Before Rank-5 Stress Test | `manuscripts/lane-vii-holographic-invariants/v2.0.1/source.md` | Source captured; not yet exported as PDF. Consolidation precision patch and protocol update before v1.14. |

## Chat-draft tranches not yet exported

| Version | Title / role | Status | Core result |
| --- | --- | --- | --- |
| v1.3-FRI | Cyclic Channel Frobenius Closure Attempt I | Chat draft, not yet exported | Proved one-cycle Frobenius closure under normalized hypotheses; factorable two-cycle case positive; coupled-cycle vertex norm identified as obstruction. |
| v1.4-FRI | Multi-Channel Vertex Normalization Audit | Chat draft, not yet exported | Proved normalized Racah F-move unitarity/contractivity; reduced obstruction to higher-valent Wilson/Reisenberger vertices. |
| v1.5-FRI | Minimal 9j Vertex Normal-Form Audit | Chat draft, not yet exported | Proved dimension-weighted 9j recoupling matrix is unitary; distinguished recoupling operators from vertex evaluations. |
| v1.7.1-FRI | Residual Threshold Correction and Spin-Weighted Defect Ledger | Chat draft, not yet exported | Corrected residual threshold to `log_2(2/5^{1/3}) = 0.226024...`, added spin-weighted defect condition, and specified canonical decomposition algorithm. |
| v1.8-FRI | First Residual Loop Computation | Chat draft, not yet exported | Audited elementary TL loops, theta/bubble identities, and 9j loops as non-residual under normalized Wigner/TL form. |
| v1.9-FRI | Connected Residual Evaluation Search | Chat draft, not yet exported | Reduced catalogue ambiguity but over-scalarized the residual object; patched by v1.9.1. |
| v1.10.1-FRI | Local Vertex Formula Identification and Normalized Package Protocol | Exported locally but not yet in manifest hash table | Identifies Cherrington-Christensen 48j vertex package and normalizes the vertex-edge protocol. |
| v1.11-FRI | Normalized 48j Vertex Package Definition and Sign/Path Discipline | Chat draft, not yet exported | Transcribes vertex/edge formula structure, fixes sign/path rules, defines normalized package for computation. |
| v1.12-FRI | Smallest-Case Residual Block Norm Audit I | Chat draft, not yet exported | Shows planar four-plaquette smallest case is defect-free but degenerate. |
| v1.13-FRI | Two-Plane Fundamental Vertex Stress Test | Chat draft, not yet exported | Shows boundary-cut rank-2 channel is operator-safe; closed rank-2 cycle saturates Frobenius; local-to-global consistency at rank 2. |

These chat-draft tranches should be exported or folded into the next consolidation artifact before external circulation.

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
6. one-cycle and factorable two-cycle Frobenius closure in chat-draft form;
7. normalized Racah F-move and dimension-weighted 9j recoupling unitarity in chat-draft form;
8. residual threshold/spin-weighted ledger and canonical decomposition protocol;
9. residual operator patch: the active object is `E_cub^fund` as a typed operator/tensor block, not a scalar;
10. rank-2 local audit: operator-safe when cut, Frobenius-tight when closed;
11. v2.0.1 consolidation-polish source captured before rank-5 stress test;
12. arbitrary cyclic Frobenius closure as the active theorem target.

## Missing repository captures

Still to add in later PRs:

- actual TeX sources under `manuscripts/lane-vii-holographic-invariants/` for each exported version;
- binary PDFs via binary-safe path or Git LFS/release assets;
- exported sources for v1.3, v1.4, v1.5, v1.7.1, v1.8, v1.9, v1.10.1, v1.11, v1.12, and v1.13, or an explicit consolidation absorbing them;
- Lane IV consolidation artifacts;
- Brownian Holonomy v0.5 sidecar;
- Lane VI spherical/simplicial regulator notes;
- build receipts for all Lane VII exports.
