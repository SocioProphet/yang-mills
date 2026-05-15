# Dependencies

## Upstream

| Repository | Commit SHA | Cited content |
|---|---|---|
| `SocioProphet/Heller-Godel` | `0ef1cab4c525fd004e38fa9a92f7e911acbbc976` | Framework objects (`HG-*`) from `docs/framework-core/`; PFK operational substrate from `proof_fabric_kernel/` |

## Cited objects

### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing only; specific identifiers cited at point of use |
| `HG-EX-001` | Catalan / mu_2 fixture | available for any mu_2 parity computation in SU(2) representation theory if such computation enters the manuscript |
| `HG-MTH-001` | Universal Bridge method-grade analogy | cited as conceptual scaffold for cross-Clay claim-discipline pattern; does not transfer proofs |

### PFK operational substrate (canonical seed-tree identifiers)

The yang-mills program consumes the canonical seed-tree operator catalog from `SocioProphet/Heller-Godel/proof_fabric_kernel/`. Citation uses the operator identifiers currently registered in the seed tree:

| Identifier | Catalog role | Yang-Mills use |
|---|---|---|
| `PFK-OP-001` | Event ingestion | for any future receipt emission from Lane II measurements |
| `PFK-OP-010` | Phase-map operator | available if Lane II quantitative work uses phase-space methods |
| `PFK-OP-020` | Null-model operator | required for any descriptive-grade empirical claim |
| `PFK-OP-030` | Calibration operator | for numerical-baseline sanity checks |
| `PFK-OP-040` | Catalan / mu_2 fixture operator | unused initially; reserved for future cross-program work |
| `PFK-OP-050` | PrimeStatsProtocol operator family | required for any empirical claim |

### PFK schema paths (by canonical path, identifiers TBD)

PFK schemas are cited by exact path until granular `PFK-SCHEMA-*` identifiers are registered in a subsequent Heller-Godel registry-expansion PR:

| Schema path | Role |
|---|---|
| `proof_fabric_kernel/schemas/event_ir.schema.json` | Event-IR records for operator invocations |
| `proof_fabric_kernel/schemas/proof_artifact.schema.json` | proof-step envelopes |
| `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | numerical baseline checks |
| `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | claim ledger rows |

## Citation form

When citing a framework or PFK object in this repository, use:

```text
[HG-FND-001 @ 0ef1cab4c525fd004e38fa9a92f7e911acbbc976]
[PFK-OP-050 @ 0ef1cab4c525fd004e38fa9a92f7e911acbbc976]
[proof_fabric_kernel/schemas/event_ir.schema.json @ 0ef1cab4c525fd004e38fa9a92f7e911acbbc976]
```

The commit SHA is the merged Heller-Godel commit, not the current `main` HEAD. This guarantees citation stability across upstream schema evolution.

## Forbidden edges

- `yang-mills` -> any other Clay-program repo (no horizontal dependencies between Clay targets)
- `yang-mills` -> Heller-Godel-other-than-pinned-commit (no floating `main` references)
- `yang-mills` -> automorphic / number-theoretic methodology from RH or Hodge programs except through the Universal Bridge method-grade analogy (`HG-MTH-001`)

## Scope discipline (unchanged by this declaration)

The yang-mills program's v0.14.4 scope discipline is preserved:

- Gauge group: SU(2)
- Lattice: Wilson lattice gauge theory on `Z^4`
- Lattice spacing: fixed `a > 0`
- Coupling window: `beta < beta* = 0.006296889394074993`
- Output: positive transfer gap above the vacuum in the infinite-volume gauge-invariant Osterwalder-Seiler reflection-positive Hilbert space

This declaration does not:

- Promote v0.14.4 to a continuum construction
- Promote v0.14.4 to a Clay Millennium proof
- Promote v0.14.4 to a weak-coupling theorem
- Promote v0.14.4 to an SU(N>=3) theorem
- Promote v0.14.4 to an asymptotic-freedom trajectory result

Per forward anti-seed convention, pending Heller-Godel PFK registry expansion:

- the Universal Bridge is method-grade analogy only; it does not transfer proofs from RH-program work to YM-program work;
- PFK operator invocation is not evidence for any YM Clay statement.

## When this declaration triggers downstream work

A future yang-mills PR that emits empirical receipts (Lane II fiber-sensitive sharpening numerical work) will need to:

1. add an `experiments/` directory analogous to `Heller-Winters-Theorem/experiments/candidate-c/`;
2. add a `tests/test_yang_mills_emission.py` validator using the same pattern as HW PR #39;
3. add a CI workflow checking out Heller-Godel at the pinned commit and running the validator;
4. emit PFK-schema-conformant receipts for each Lane II measurement.

This DEPENDENCIES PR establishes the pin and the citation surface. It does not yet trigger receipt emission; receipts come in a subsequent Lane II PR.

## Schema-version pinning policy

Schema major-version changes are breaking. Re-pinning the Heller-Godel commit SHA requires re-verifying any existing receipts under `experiments/` against the new schemas. Until empirical receipts exist in this repo, the pin can be advanced more freely; once receipts exist, re-pinning is a migration event.

This is per forward anti-seed convention `A-PFK-SCHEMA-002` (schema-version drift), which will canonicalize in the upstream PFK registry-expansion PR.
