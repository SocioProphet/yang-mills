# Heller-Dirac t0: dictionary, low-n tests, and failure traps

Status: program-context audit file.  
Purpose: keep the Heller-Dirac sidecar mathematically checkable while the c0/b0/a0 notes evolve.

## 0. Test principle

Every Heller-Dirac statement must survive conversion among four coordinate systems:

```text
1. product/parabolic cell basis:       |j,m_+>|j,m_->
2. spherical orbital basis:            |ell,m>
3. defect channel basis:               |ell,m> with energy E_{n ell}
4. relativistic spinor basis:          |kappa,m_j> with branch label
```

The core sanity rule is:

```text
basis change is not new physics;
Hamiltonian/channel diagonalization is physics.
```

The Tetryonics-style triangle is therefore a basis chart, not the final physics by itself.

## 1. Universal decomposition test

For principal shell `n`, set

```math
j=\frac{n-1}{2}.
```

The product shell is

```math
\mathcal H_n = D^{(j)}\otimes D^{(j)}.
```

The spherical decomposition must be

```math
D^{(j)}\otimes D^{(j)}
=\bigoplus_{\ell=0}^{2j}D^{(\ell)}.
```

Dimension audit:

```math
(2j+1)^2=\sum_{\ell=0}^{2j}(2\ell+1)=n^2.
```

This is the first invariant. Any drawing or interpretation that does not reproduce this count is not representing the hydrogenic SO(4) shell correctly.

## 2. Low-n audit table

| `n` | `j=(n-1)/2` | Product dimension | Decomposition | Dimension sum |
|---:|---:|---:|---|---:|
| 1 | 0 | 1 | `D^0` | 1 |
| 2 | 1/2 | 4 | `D^1 ⊕ D^0` | 3+1=4 |
| 3 | 1 | 9 | `D^2 ⊕ D^1 ⊕ D^0` | 5+3+1=9 |
| 4 | 3/2 | 16 | `D^3 ⊕ D^2 ⊕ D^1 ⊕ D^0` | 7+5+3+1=16 |

This is the minimum table that should appear in any expository Heller-Dirac manuscript section.

## 3. n=2 explicit Clebsch-Gordan test

For `n=2`, `j=1/2`. Write

```text
|+> = |1/2, +1/2>
|-> = |1/2, -1/2>
```

The product cells are

```text
|++>, |+->, |-+>, |-->
```

The spherical basis is

```math
|1,1\rangle = |++\rangle,
```

```math
|1,0\rangle = \frac{1}{\sqrt2}(|+-\rangle+|-+\rangle),
```

```math
|1,-1\rangle = |--\rangle,
```

```math
|0,0\rangle = \frac{1}{\sqrt2}(|+-\rangle-|-+\rangle).
```

Immediate consequences:

```text
1. The stretched corners |++> and |--> are pure ell=1 states.
2. The mixed corners |+-> and |-+> are not pure ell=0 states.
3. The ell=0 state is an antisymmetric CG combination.
4. The anti-diagonal m=0 contains both ell=1 and ell=0.
```

This is the simplest finite counterexample to the mistaken claim that a raw cell or anti-diagonal is already an orbital multiplet.

## 4. Defect operator test in n=2

Let the defect operator be diagonal in the spherical basis:

```math
\widehat\Delta = \delta_1\Pi_1 + \delta_0\Pi_0.
```

In the product basis restricted to the `m=0` anti-diagonal `{|+->,|-+>}`, use

```math
\Pi_1 = |1,0\rangle\langle 1,0|,
\qquad
\Pi_0 = |0,0\rangle\langle 0,0|.
```

Then

```math
\widehat\Delta_{m=0}
=\frac12
\begin{pmatrix}
\delta_1+\delta_0 & \delta_1-\delta_0\\
\delta_1-\delta_0 & \delta_1+\delta_0
\end{pmatrix}
```

in the ordered basis `(|+->,|-+>)`.

This is the cleanest finite proof of the b0 claim:

```text
defects are diagonal in ell;
defects are generally nonlocal/mixing in the product-cell basis.
```

If `delta_1=delta_0`, the matrix becomes a scalar and the Coulomb degeneracy is restored at this level. If `delta_1 != delta_0`, the defect layer splits the ell channels.

## 5. Sum/difference test

For the two orbit points

```math
x_+=j\hbar\widehat\Omega_+,
\qquad
x_-=j\hbar\widehat\Omega_-,
```

define

```math
L=x_++x_-,
\qquad
A=x_+-x_-.
```

The invariant checks are

```math
L\cdot A=0,
```

```math
|L|^2+|A|^2=4j^2\hbar^2,
```

```math
|L|=2j\hbar\cos(\Theta/2),
\qquad
|A|=2j\hbar\sin(\Theta/2).
```

Interpretation checks:

```text
L is diagonal angular momentum.
A is anti-diagonal Runge-Lenz direction.
The difference variable is not a finite-difference derivative.
The difference variable is the hidden Coulomb coordinate and the hyperbolic bridge.
```

## 6. Dirac kappa mapping test

Once spin is active, replace orbital-only labels by `kappa` and total angular labels.

For `kappa` convention used in the a0 note:

```math
j_{\mathrm{tot}}=|\kappa|-\frac12.
```

The orbital angular momentum associated with the upper component is

```math
\ell = \begin{cases}
\kappa, & \kappa>0,\\
-\kappa-1, & \kappa<0.
\end{cases}
```

The lower spinor component carries the paired angular harmonic with `-kappa`. Therefore a valid Dirac lift must pass this check:

```text
one Dirac channel pairs two orbital angular sectors through the spinor structure.
```

The nonrelativistic limit may collapse the small component, but the relativistic bookkeeping must not erase it.

## 7. Failure traps

### Trap 1: raw cell equals orbital state

Incorrect:

```text
A triangle cell is an ell multiplet.
```

Correct:

```text
A triangle cell is a product/parabolic weight vector. The ell multiplet is a CG-summed spherical state.
```

### Trap 2: anti-diagonal equals ell

Incorrect:

```text
m_+ + m_- fixes ell.
```

Correct:

```text
m_+ + m_- fixes L_z=m hbar. Multiple ell values may live on the same anti-diagonal.
```

### Trap 3: quantum defect makes angular orbit nonintegral

Incorrect:

```text
j becomes j*=(n-delta-1)/2 inside the SU(2) orbit.
```

Correct:

```text
The angular orbit remains integral. The radial action receives an ell-dependent phase defect.
```

### Trap 4: Dirac means just adding spin labels

Incorrect:

```text
Dirac = nonrelativistic ell plus spin as an afterthought.
```

Correct:

```text
Dirac reorganizes angular states by kappa, pairs large/small spinor components, and introduces energy-branch bookkeeping.
```

### Trap 5: particle zoo follows immediately

Incorrect:

```text
Dirac-Coulomb labels already give all internal particle charges.
```

Correct:

```text
Hydrogenic Dirac labels give spinor/angular/branch structure. Full particle taxonomy requires a later field and internal-gauge layer.
```

## 8. Minimal acceptance suite

Before merging future Heller-Dirac changes, check that the manuscript still satisfies:

1. `sum_{ell=0}^{n-1}(2ell+1)=n^2`.
2. `m=m_++m_-` is distinguished from `ell`.
3. `A=J_+-J_-` is identified as Runge-Lenz, not as a discrete derivative.
4. quantum defects modify radial action, not angular SU(2) integrality.
5. the defect operator is diagonal in `ell` but CG-rotated in product cells.
6. Dirac lift uses `kappa`, `j_tot`, spinor spherical harmonics, and branch labels.
7. particle-zoo claims remain deferred until field/operator and internal-gauge labels are explicitly introduced.

## 9. Next audit work

The next useful hardening pass is computational:

```text
- generate CG tables for n=2,3,4;
- verify projector identities Pi_ell Pi_ell'=delta_ell,ell' Pi_ell;
- generate defect matrices in the product-cell basis;
- add a small symbolic notebook or script once the repo accepts executable artifacts for this lane.
```
