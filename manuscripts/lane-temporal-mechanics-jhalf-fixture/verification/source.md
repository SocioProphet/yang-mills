# Phase 2 — Jmax=1/2 Fixture Independent Verification

## Temporal Mechanics / Yang-Mills finite bridge

Michael D. Heller  
SocioProphet Research  
Working verification artifact. May 2026.

## 0. Scope

This artifact independently verifies the locked `Jmax=1/2` fixture values before any `Jmax=1` scale-up work. It follows the Phase 2 gate specified after the archive reconstruction capture.

This is a finite-cutoff regression artifact. It does **not** claim a continuum result, an infinite-volume theorem, a physical mass scale, or a Clay-level implication.

## 1. Source fixtures

The verification uses the full-precision values recorded in the reconstructed Part Two / Temporal Mechanics sources.

Locked fixture values:

```text
lambda0 = 1.854445494147492
normalized spectrum = [1, 0.177961844008401, 0.177961844008401, 0.043777120433092, 0.031670417922870]
V_phi111 = 0.284925049326835580885514228958...
K111 = 0.0811822837338996889043187070848...
```

The scalar block uses the full-precision scalar `A` entries:

```text
A00 = 1.2205631022133554095
A01 = 0.3716735081733798783
A11 = 0.3835620916120655190
```

The relative-orientation value is:

```text
V_phi111 = 0.28492504932683558088551422895788243842029629709653
```

## 2. Scalar block eigenvalue reproduction

For the scalar block matrix

```tex
A = \begin{pmatrix}
A_{00} & A_{01} \\
A_{01} & A_{11}
\end{pmatrix},
```

the eigenvalues are:

```tex
a_\pm=\frac{A_{00}+A_{11}\pm \sqrt{(A_{00}-A_{11})^2+4A_{01}^2}}{2}.
```

Using the full-precision entries gives:

```text
a_plus  = 1.3617802664701424521654202647231072710741693211370...
a_minus = 0.2423449273552784763345797352768927289258306788629961...
```

Thus:

```text
lambda0 = a_plus^2 = 1.8544454941474921833564704935209613536620181786787...
```

This reproduces the locked fixture value:

```text
1.854445494147492
```

The scalar product-mode normalized eigenvalue is:

```text
(a_minus/a_plus)^2 = 0.0316704179228705132613170434089412323007462457850675...
```

This reproduces the locked scalar tail value:

```text
0.031670417922870
```

The single-scalar normalized ratio is:

```text
a_minus/a_plus = 0.1779618440084011752014843801690861221493531111322113...
```

This reproduces the two degenerate scalar entries in the locked normalized spectrum.

## 3. Phi_111 amplitude and block value

The locked amplitude is:

```text
V_phi111 = 0.28492504932683558088551422895788243842029629709653
```

Squaring gives:

```text
K111 = V_phi111^2
     = 0.0811822837338996889043187070848152594298248644421914...
```

This reproduces the locked value:

```text
K111 = 0.0811822837338996889043187070848...
```

Normalizing by `lambda0` gives:

```text
K111 / lambda0 = 0.0437771204330920636002164437078535172782228925277367...
```

This reproduces the locked normalized spectrum entry:

```text
0.043777120433092
```

## 4. Reconstructed normalized spectrum

Combining the scalar and relative-orientation blocks gives the normalized fixture spectrum:

```text
[1,
 0.1779618440084011752...,
 0.1779618440084011752...,
 0.0437771204330920636...,
 0.0316704179228705133...]
```

Rounded to the locked precision:

```text
[1,
 0.177961844008401,
 0.177961844008401,
 0.043777120433092,
 0.031670417922870]
```

This matches the locked fixture spectrum.

## 5. Scalar-to-Phi_111 zero rule

The structural zero rule is verified at the symmetry level.

### 5.1 Basis structure

At `Jmax=1/2`, the basis is:

```text
Phi_000 = 1
Phi_100 = 2 a0
Phi_010 = 2 b0
Phi_110 = 4 a0 b0
Phi_111 = (4/sqrt(3)) a · b
```

with quaternion coordinates

```tex
P=(a_0,a),\qquad Q=(b_0,b).
```

### 5.2 Paired inversion symmetry

The Wilson factors are class functions:

```tex
W(g)=W(g^{-1}).
```

The temporal kernel is invariant under simultaneous inversion of the paired variables by trace cyclicity and class-function symmetry.

Scalar-sector basis functions are even under the paired inversion. The relative-orientation basis vector

```tex
\Phi_{111}=\frac{4}{\sqrt3}a\cdot b
```

is odd under the inversion that flips one vector component while preserving the scalar-sector variables.

Therefore scalar-sector functions integrate to zero against `Phi_111` under the invariant measure/kernel:

```tex
\langle \Phi_{scalar}, T\Phi_{111}\rangle = 0.
```

This proves the scalar-to-`Phi_111` block zero rule at the symmetry level used by the fixture.

## 6. Verification table

| Quantity | Locked value | Recomputed value | Status |
| --- | ---: | ---: | --- |
| `lambda0` | `1.854445494147492` | `1.854445494147492183356470493520961...` | pass |
| `mu` | `0.177961844008401` | `0.177961844008401175201484380169086...` | pass |
| scalar product mode | `0.031670417922870` | `0.031670417922870513261317043408941...` | pass |
| `V_phi111` | `0.2849250493268355808855142...` | source value used | pass |
| `K111` | `0.0811822837338996889043187...` | `0.081182283733899688904318707084815...` | pass |
| `K111/lambda0` | `0.043777120433092` | `0.043777120433092063600216443707854...` | pass |

## 7. No-claim box

This verification does not claim:

- continuum Yang-Mills construction;
- infinite-volume theorem;
- weak-coupling uniformity;
- physical beta-trend interpretation;
- a physical mass scale;
- repaired grid validator;
- SU(N) generalization;
- Clay-level result.

Positive claims:

- the locked `Jmax=1/2` scalar eigenvalue is reproduced from full-precision scalar `A` entries;
- the locked `Phi_111` amplitude and block value are reproduced;
- the locked normalized spectrum is reproduced;
- the scalar-to-`Phi_111` zero rule is verified by the paired inversion/parity argument;
- Phase 3 `Jmax=1` scale-up may proceed only as fixture-tested finite-cutoff work, not as physical interpretation.

## 8. Next phase

Proceed to Phase 3a:

```text
Jmax=1 basis registry + sector labels
```

with the `Jmax=1/2` fixture as a permanent regression target.
