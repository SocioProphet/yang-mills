# Yang-Mills Archive Reconstruction — 2026-05-09

## Status

The reconstruction bundle was uploaded to the session workspace and verified locally:

```text
yang_mills_archive_reconstruction_2026_05_09.zip
```

A duplicate uploaded path was also present:

```text
yang_mills_archive_reconstruction_2026_05_09(1).zip
```

Both ZIP files have identical SHA256:

```text
a9482d5aff11067980b1c384cf715ed99991c13bed9135f789443156bb19ae5d
```

Verified uploaded ZIP size:

```text
8233525 bytes
```

## Repository capture boundary

The ZIP itself is not committed to this repository in this PR. This document records the verified checksum and contents. The binary bundle should be uploaded through a binary-safe path such as Git LFS, release assets, or a direct repository upload if policy allows.

Once binary upload is completed, update this document with repository paths or release asset URLs. Until then, the repo records hashes and validation results but not the binary content.

## Verified contents

The bundle contains 19 files under `clean_pdfs/`:

- 9 reconstructed PDFs;
- 9 matching `.txt` searchable extracts;
- 1 aggregate `README.md`.

PDF page count total: 102.

All 9 PDFs passed `pdfinfo` validation in the local workspace. Each `.txt` extract has page markers matching its paired PDF page count.

## File hashes and page counts

| PDF | Pages | PDF SHA256 | Text extract | Text SHA256 | Text page markers |
| --- | ---: | --- | --- | --- | ---: |
| `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.pdf` | 34 | `e4acb9853e0d23c91d3cae137e7a1ef335bbf9b56769e711dbdae408c7517a2b` | `heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.txt` | `fc56868f755a161d4f278e517d370e3c76f72a7b72c43518aab637c47fe98343` | 34 |
| `yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.pdf` | 4 | `c04ac5579f2806eecb21c68025cdd792d6f8f6921b8eee9922a713e69705c223` | `yang_mills_program_part_three_v3_11_first_bulk_orbit_closure.txt` | `d9492d47a78b127e9c750c17b28e93941db87d9d6a3f7e9dadfd293010c28a45` | 4 |
| `yang_mills_program_part_three_v3_13_response_diagnostics_full_running.pdf` | 5 | `52c3d66200d5edc05b51da7d817dceff93c228d7602952bf46ff400b9e8d28a7` | `yang_mills_program_part_three_v3_13_response_diagnostics_full_running.txt` | `7f8021cea083d29a605a0f350ede05b2fe207d9ed06ef261d636d9589aa6617b` | 5 |
| `yang_mills_program_part_three_v3_14_pair_lift_orbit25.pdf` | 6 | `4cf940f3c11d0f72f6d043c3dff902a4e0a0b97fd494a4f73912caee4ad262a4` | `yang_mills_program_part_three_v3_14_pair_lift_orbit25.txt` | `cc4becd9229b7988f0a553bdbb43e5caa01d24fb8f073fb55403a02789cfd29c` | 6 |
| `yang_mills_program_part_three_v3_15_orbit25_projection_closure.pdf` | 9 | `fdcfd12f6adf31be53585d7190e9af459ea62c381299605391721307860f18be` | `yang_mills_program_part_three_v3_15_orbit25_projection_closure.txt` | `31c296f083eedd1fd703b10da3b6936b66377a895a4899b4efc3e257a192d808` | 9 |
| `yang_mills_program_part_three_v3_16_source_scalar_retriage.pdf` | 3 | `36926cce33c5a965c620bf430daf691c1fac56e995f61dea48d366b834606051` | `yang_mills_program_part_three_v3_16_source_scalar_retriage.txt` | `a3d0b8ccd761a2071e0f5aded14eb28e934bd5d25836816e8fb8c59187cb1df6` | 3 |
| `yang_mills_program_part_three_v3_7_full_running_manuscript.pdf` | 22 | `2cd9dca4711d68c7d535740f813ae41776529267e262733868636e563ef43505` | `yang_mills_program_part_three_v3_7_full_running_manuscript.txt` | `77654ebb1ca16e226eafd521be67c6f530342267bbbc5637ead96ac2367e10cb` | 22 |
| `yang_mills_program_part_two_proof_strategy_roadmap.pdf` | 15 | `7278c9f3e87073cdf0f26633b22d545b6fc4e195b8e72aea041e947ea0770392` | `yang_mills_program_part_two_proof_strategy_roadmap.txt` | `54e00aeb8e06eec1ff8ae4a2c1f20eccd2d0fa68fb73c036cf8574ccd42283b9` | 15 |
| `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.pdf` | 4 | `8dd149bd327d697095850464dc0784c4a9e864ab0c4fdee881f156fbabc52925` | `yang_mills_program_v4_0_k3_product_formula_face_regression_spectra.txt` | `164ed5e2e8a55b55b8a88b18d5bf7f859efab3cfb0bc7257b07dec0359dcb340` | 4 |

Aggregate README hash:

```text
eeac544cc2f024b4dcb4f5520d3219e09b879d3654cb431cf59c7f4a90262f71
```

## Canonical placement plan

Suggested placement after binary-safe upload:

- temporal mechanics materials: `manuscripts/temporal-mechanics/`
- Program Part Two materials: `manuscripts/program-part-two/`
- Program Part Three materials: `manuscripts/program-part-three/`
- Program Part Four materials: `manuscripts/program-part-four/`
- this reconstruction report: `docs/archive-reconstruction-2026-05-09.md`

Original corrupt zip-as-PDF files may be retained under a `/raw/` subtree if archival of the upload artifact is desired, but they should not be canonical references.

## Technical note

The reconstruction report states that no derivations were recreated. The v0.9.27 Section 19 quaternion/Haar integral and Section 21.2 Wigner/Peter-Weyl translation reportedly survived the reconstruction.

An independent numerical verification of `V_phi111 = 0.28492504932683558088...` at `beta=1` should be captured separately in the Phase 2 fixture verification artifact.

## Claim boundary

This document does not claim:

- the binary reconstruction bundle is committed to the repository;
- OCR/text extraction quality has been independently audited beyond page-marker count consistency;
- the reconstructed PDFs are canonical until uploaded through a binary-safe path and referenced by repository path or release asset URL.

Positive claims:

- the uploaded ZIP was accessible in the session workspace;
- the uploaded ZIP SHA256 is recorded;
- all contained PDFs passed metadata validation;
- per-file hashes and page counts are recorded;
- canonical placement and binary upload requirements are specified.
