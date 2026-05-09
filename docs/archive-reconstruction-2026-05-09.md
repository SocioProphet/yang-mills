# Yang-Mills Archive Reconstruction — 2026-05-09

## Status

An external reconstruction bundle was reported as complete:

```text
yang_mills_archive_reconstruction_2026_05_09.zip
```

Reported size: 8.2 MB.

## Reported contents

The reported bundle contains 19 files:

- 9 clean reconstructed PDFs, 102 pages total;
- 9 matching `.txt` searchable extracts with `===== PAGE N =====` separators;
- 1 aggregate `README.md` index documenting corruption diagnosis, reconstruction method, per-file content summary, phase-relevance matrix, and repo capture suggestions.

## Repository capture boundary

The ZIP itself was not present in the accessible assistant workspace at capture time, so it has not been committed to this repository and no checksum is asserted here.

This document records the reconstruction status and intended canonical placement plan. The binary bundle should be uploaded through a binary-safe path such as Git LFS, release assets, or direct repository upload if size/policy allows. Once uploaded, update this document with:

- SHA256 of the ZIP;
- SHA256 of each reconstructed PDF;
- SHA256 of each text extract;
- repository paths or release asset URLs.

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

An independent numerical verification of `V_phi111 = 0.28492504932683558088...` at `beta=1` was reported earlier and should be captured separately in the Phase 2 fixture verification artifact.

## Claim boundary

This document does not claim:

- the binary reconstruction bundle is present in the repository;
- the ZIP or PDFs have been independently checksummed by the repository;
- OCR quality has been independently verified here;
- reconstructed PDFs are canonical until uploaded and checksummed.

Positive claims:

- the reconstruction bundle has been reported complete;
- canonical placement and checksum requirements are specified;
- Phase 2 fixture verification can proceed independently of binary archive capture.
