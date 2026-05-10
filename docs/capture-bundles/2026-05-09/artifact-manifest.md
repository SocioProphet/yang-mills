# Yang-Mills Capture Bundle 2026-05-09 — Artifact Manifest

Target repository: `SocioProphet/yang-mills`.
Source bundle: `yang mills capture bundle 2026 05 09.zip`.
Source bundle SHA-256: `925f8d6e69d081ee5eea798c0550276fb1fb27982f9611c22743caa59cfb49e1`.
Source bundle bytes: `8309550`.
Normalized bundle SHA-256: `5126033e8d17143e69f68f3728daf2c5c7b67119fab7606f59255a084ca4748f`.
Normalized bundle bytes: `8319272`.

## Storage policy

Markdown status deltas, capture reports, and file indexes are committed as reviewable repository content in this PR. Reconstructed PDFs are distribution artifacts and are hash-registered for binary-safe storage through Git LFS, release assets, or the program artifact bucket. Recovered text extracts, executable scripts, generated JSON fixtures, and verification logs are indexed here and in `normalized-file-index.md`; they should be expanded into repository paths in a follow-on commit or follow-on PR when connector payload limits allow bulk source expansion.

## Reconstructed PDF distribution artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.pdf` | 3675841 | `e4acb9853e0d23c91d3cae137e7a1ef335bbf9b56769e711dbdae408c7517a2b` |
| `yang_mills_program_part_two_proof_strategy_roadmap.pdf` | 1318251 | `7278c9f3e87073cdf0f26633b22d545b6fc4e195b8e72aea041e947ea0770392` |
| `yang_mills_program_part_three_v3_7_full_running_manuscript.pdf` | 1445247 | `2cd9dca4711d68c7d535740f813ae41776529267e262733868636e563ef43505` |
| `yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.pdf` | 562540 | `c04ac5579f2806eecb21c68025cdd792d6f8f6921b8eee9922a713e69705c223` |
| `yang_mills_program_part_three_v3_13_response_diagnostics_full_running.pdf` | 732611 | `52c3d66200d5edc05b51da7d817dceff93c228d7602952bf46ff400b9e8d28a7` |
| `yang_mills_program_part_three_v3_14_pair_lift_orbit25.pdf` | 838832 | `4cf940f3c11d0f72f6d043c3dff902a4e0a0b97fd494a4f73912caee4ad262a4` |
| `yang_mills_program_part_three_v3_15_orbit25_projection_closure.pdf` | 880002 | `fdcfd12f6adf31be53585d7190e9af459ea62c381299605391721307860f18be` |
| `yang_mills_program_part_three_v3_16_source_scalar_retriage.pdf` | 480697 | `36926cce33c5a965c620bf430daf691c1fac56e995f61dea48d366b834606051` |
| `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.pdf` | 578425 | `8dd149bd327d697095850464dc0784c4a9e864ab0c4fdee881f156fbabc52925` |

## Recovered text extracts indexed for repository expansion

| Extract | Bytes | SHA-256 |
|---|---:|---|
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.txt` | 57383 | `4816b143929d2bf2e3a8437eab38acdd6f194ceb8d8c2214777fe94b175d90b4` |
| `yang_mills_program_part_two_proof_strategy_roadmap.txt` | 16202 | `6af158bc4ae19e2356014baa631555573125b0f36e5d68788601f0e6dfe9a418` |
| `yang_mills_program_part_three_v3_7_full_running_manuscript.txt` | 14609 | `52dabba76ab66ac3a66c3cf507b3d11a60d556f07941960eff3f580c16551665` |
| `yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.txt` | 8463 | `b48095d4f33705e480f3a7465b84943b8d850deaa32f34dbea9e8aff2136983b` |
| `yang_mills_program_part_three_v3_13_response_diagnostics_full_running.txt` | 10628 | `a05d5829d41392dfa04fba6da1ab9a41b434dbbeb531fecc3290756e5d5488ae` |
| `yang_mills_program_part_three_v3_14_pair_lift_orbit25.txt` | 11409 | `7c359aa89df37678813aab3a0006cef4439a12f5f0a3f14c25f5cb7241decd09` |
| `yang_mills_program_part_three_v3_15_orbit25_projection_closure.txt` | 12228 | `16bb434f458a44929878e573fc797b6f3cafdec8ea88ff785f6d4e9b90e22098` |
| `yang_mills_program_part_three_v3_16_source_scalar_retriage.txt` | 6807 | `77d55e859d344dc8c016ab04db66b51bd47df353ba526022260215a3b12b0b90` |
| `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.txt` | 8705 | `c322710d4501d6a09733853942e6040f66c276763bcdeaef8dc9a404506ecf35` |

## Validation receipt

All four executable checks were rerun after normalization:

```bash
python3 manuscripts/lane-temporal-mechanics-jhalf-fixture/verification/verify.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/basis-registry/registry_check.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/gram-matrix/gram.py
python3 manuscripts/lane-temporal-mechanics-jmax-one/truncation-regression/truncation.py
```

Observed outcome: `ALL CHECKS PASS` for Phase 2, Phase 3a, Phase 3b, and Phase 3c. The reconstructed PDF header audit found 9 of 9 distribution PDFs start with `%PDF`.

## Current PR expansion status

Committed in this PR: capture README, ingest report, artifact manifest, normalized file index, preserved source-bundle README, Phase 2 status delta, Phase 3a status delta, Phase 3b status delta, Phase 3c status delta, and Methodology Manifesto v0.2 status delta.

Not yet expanded into final repository paths: recovered text extracts, executable scripts, generated JSON fixtures, verification logs, and reconstructed PDFs. These are indexed and hash-registered rather than silently omitted.
