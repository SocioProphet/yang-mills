# Dependencies

## Upstream

This repository consumes from two upstream framework repositories. Both pins are required for citation-surface validation.

| Repository | Commit SHA | Role |
|---|---|---|
| `SocioProphet/Heller-Godel` | `fb6b866f1b9b4089629cac18c179c32863bf42e4` | Framework core; framework objects (`HG-*`); PFK operational substrate (`PFK-*`); framework anti-seed (`A-HG-*`, `A-PFK-*`) |
| `SocioProphet/Heller-Dirac` | `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993` | Co-foundational spectral / Hopf / time / field scaffold; spectral-triple vocabulary (`HD-*`); Heller-Dirac anti-seed (`A-HD-*`) |

Both pins are not floating. Re-pinning requires an explicit dependency PR.

## Cited objects

### From Heller-Godel @ `fb6b866f1b9b4089629cac18c179c32863bf42e4`

#### Framework-grade (HG-*)

| Identifier | Role | Notes |
|---|---|---|
| `HG-FND-*` | Foundational vocabulary | typing only; specific identifiers cited at point of use |
| `HG-MTH-005` | Universal Bridge formal specification | parent / general bridge axiom; does not transfer proofs |
| `HG-MTH-007` | Universal Bridge: Yang-Mills gauge domain extension | canonical YM bridge spec; yang-mills is the primary consumer |

#### PFK operational substrate

| Identifier | Role | Yang-Mills use |
|---|---|---|
| `PFK-OP-001` | Event ingestion | future receipt emission |
| `PFK-OP-030` | Calibration operator | numerical baselines for Wilson-lattice checks |
| `PFK-SCHEMA-001..004` | claim ledger / Event-IR / proof artifact / calibration bundle | future typed receipts |

#### Framework anti-seed

| Identifier | Applies because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs |
| `A-HG-MTH-002` | Catalan / mu2 fixture is not Clay progress |
| `A-HG-MTH-003` | fixture-grade and theorem-grade citations must not be mixed |
| `A-HG-MTH-004` | Standard Conjectures / related conjectural apparatus cited diagnostically are not assumed |
| `A-HG-MTH-005` | barrier-diagnostic frame is not a circumvention recipe |
| `A-HG-MTH-006` | component apparatus is not Clay-grade Yang-Mills resolution |

#### PFK anti-seed

| Identifier | Applies because |
|---|---|
| `A-PFK-OP-001` | operator invocation is not evidence |
| `A-PFK-PROTOCOL-001` | null passage is not theorem-grade |
| `A-PFK-PROTOCOL-002` | window-shopping prevention |
| `A-PFK-SCHEMA-001` | schema validity is not content validity |
| `A-PFK-SCHEMA-002` | schema-version drift; pins are not floating |
| `A-PFK-VAL-001` | validator green is not audit completion |

### From Heller-Dirac @ `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`

#### Foundational (HD-FND-*)

| Identifier | Role in Yang-Mills citation |
|---|---|
| `HD-FND-001` | spectral triple definition, cited through HG-MTH-007 Component 3 |
| `HD-FND-003` | KO-dimension table, including KO-dim 6 Standard Model context |
| `HD-FND-006` | spectral action principle, cited through HG-MTH-007 Component 3 |
| `HD-FND-010` | Hopf-algebra action on spectral triple, cited for Connes-Kreimer renormalization scaffold context |

#### Heller-Dirac anti-seed (A-HD-*)

| Identifier | Applies because |
|---|---|
| `A-HD-FT-001` | AQFT axioms are not constructive existence |
| `A-HD-HA-001` | Hopf-scaffold encoding is not renormalizability proof |
| `A-HD-NC-001` | noncommutative-geometric reformulation is not proof |
| `A-HD-SP-001` | analog spectral data is not target spectral data |
| `A-HD-FND-001` | HD-FND identifiers are reference surface, not reproof |

## Citation form

```text
[HG-MTH-005 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[HG-MTH-007 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[PFK-SCHEMA-001 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[A-HG-MTH-006 @ fb6b866f1b9b4089629cac18c179c32863bf42e4]
[HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-003 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-006 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-010 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-FT-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-HA-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-NC-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-SP-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[A-HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```

## Forbidden edges

- `yang-mills` -> any other Clay-program repo.
- `yang-mills` -> Heller-Godel-other-than-pinned-commit.
- `yang-mills` -> Heller-Dirac-other-than-pinned-commit.
- `yang-mills` -> constructive QFT / spectral-action methodology beyond what HG-MTH-007 cites diagnostically.

## Scope discipline unchanged

The yang-mills v0.14.4 scope discipline is preserved:

- gauge group: `SU(2)`;
- lattice: Wilson lattice gauge theory on `Z^4`;
- lattice spacing: fixed `a > 0`;
- coupling window: `beta < beta* = 0.006296889394074993`;
- output: positive transfer gap above the vacuum in the infinite-volume gauge-invariant Osterwalder-Seiler reflection-positive Hilbert space.

This dependency update does not promote v0.14.4 to a continuum construction, Clay Millennium proof, weak-coupling theorem, `SU(N>=3)` theorem, or asymptotic-freedom trajectory result.

## Schema-version pinning policy

Both upstream pins are fixed. Re-pinning either upstream requires a dedicated migration PR and validation of all affected citations.
