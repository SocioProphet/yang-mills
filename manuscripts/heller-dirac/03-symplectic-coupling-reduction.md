# Heller-Dirac c0: coupling-orbit foliation of the hydrogenic SO(4) shell

Status: program-context mathematical sidecar.  
Claim class: established hydrogenic representation geometry plus Heller-Dirac interpretation.  
Non-claims: this file does not assert a Yang-Mills theorem, a continuum mass-gap result, a new hydrogen spectrum theorem, or a first-principles quantum-defect prediction.

## 0. Purpose

This note formalizes step (c) of the Heller-Dirac build order:

```text
(c) geometric foundation -> (b) quantum-defect deformation -> (a) relativistic/Dirac extension
```

The target is to make the Tetryonics-style cell drawing mathematically legible as a hydrogenic SO(4) / SU(2) x SU(2) representation chart, then to identify the correct symplectic object whose quantization gives the ordinary orbital multiplets.

The central correction is terminological and structural:

- the product shell is a product of two SU(2) coadjoint orbits;
- the diagonal angular-momentum map gives a coupling foliation by fixed resultant angular momentum;
- the two-dimensional sphere that quantizes to `D^(ell)` is the resultant coadjoint orbit, not the full Marsden-Weinstein multiplicity quotient;
- the full SU(2) reduction at fixed `ell` is zero-dimensional in this equal-spin case, matching the Clebsch-Gordan multiplicity one.

## 1. Hydrogenic SO(4) shell and normalization

For a bound hydrogenic principal shell `n >= 1`, set

```math
j = \frac{n-1}{2}.
```

The Pauli/Fock/Bargmann dynamical symmetry rewrites the bound-state shell as two equal SU(2) factors. With `L` the angular momentum and `A` the suitably normalized Runge-Lenz vector on the fixed energy shell, define

```math
J_+ = \frac{1}{2}(L + A),
\qquad
J_- = \frac{1}{2}(L - A).
```

Quantum mechanically these generate commuting SU(2) algebras, and the principal shell carries

```math
\mathcal H_n \cong D^{(j)}_+ \otimes D^{(j)}_- ,
\qquad
j = \frac{n-1}{2}.
```

Therefore

```math
\dim \mathcal H_n = (2j+1)^2 = n^2.
```

Classically, the corresponding geometric model is the product of two coadjoint orbits

```math
\mathcal M_n = \mathcal O_j^+ \times \mathcal O_j^-
\cong S^2_j \times S^2_j,
```

with Kirillov-Kostant-Souriau form

```math
\omega_n
= j\hbar\,\sin\theta_+\,d\theta_+\wedge d\phi_+
+ j\hbar\,\sin\theta_-\,d\theta_-\wedge d\phi_- .
```

Here the orbit label `j` is the geometric-quantization label. Operator Casimirs use `j(j+1)\hbar^2`; the coadjoint-orbit radius convention uses `j\hbar`. The distinction matters only when comparing exact finite-`j` operator spectra against the semiclassical orbit geometry.

## 2. Diagonal SU(2), moment map, and coupling radius

The physical orbital angular momentum is the diagonal generator

```math
L = J_+ + J_-.
```

On the coadjoint-orbit product, write points as unit Bloch vectors `\widehat\Omega_\pm`:

```math
x_\pm = j\hbar\,\widehat\Omega_\pm \in \mathcal O_j^\pm.
```

The diagonal SU(2) moment map is

```math
\mu:\mathcal M_n\to \mathfrak{su}(2)^*\cong \mathbb R^3,
\qquad
\mu(\widehat\Omega_+,\widehat\Omega_-)
= j\hbar(\widehat\Omega_+ + \widehat\Omega_-).
```

Let `\Theta` be the opening angle between the two Bloch vectors. Then

```math
|\mu|^2
= (j\hbar)^2\bigl(2 + 2\cos\Theta\bigr)
= 4j^2\hbar^2\cos^2(\Theta/2).
```

The Bohr-Sommerfeld coupling values are

```math
|\mu| = \ell\hbar,
\qquad
\ell = 0,1,\dots,2j=n-1.
```

Using the orbit-label convention, the fixed-opening-angle relation is

```math
\boxed{\cos\Theta_\ell = \frac{\ell^2}{2j^2}-1.}
```

The extremes are correct:

```text
ell = 2j  ->  Theta = 0      -> aligned vectors, maximal orbital multiplet.
ell = 0   ->  Theta = pi     -> antiparallel vectors, scalar multiplet.
```

Finite-`j` operator comparisons should use the Casimir-matched convention

```math
|L|^2 = \ell(\ell+1)\hbar^2,
\qquad
|J_\pm|^2 = j(j+1)\hbar^2,
```

which gives

```math
\cos\Theta^{\mathrm{Cas}}_\ell
= \frac{\ell(\ell+1)}{2j(j+1)}-1.
```

The Heller-Dirac manuscript should state which convention is being used. The geometric-quantization lane uses the orbit-label convention because it reproduces the coadjoint-orbit volume and the `2\ell+1` dimension exactly.

## 3. Coupling foliation versus full symplectic reduction

For a coupling value `\ell`, define

```math
\Sigma_\ell
= \{(\widehat\Omega_+,\widehat\Omega_-)\in S^2_j\times S^2_j
: |\mu| = \ell\hbar\}.
```

For generic `0 < ell < 2j`, this is a three-dimensional submanifold: one scalar constraint inside the four-dimensional product.

The internal relative phase around the resultant vector is a circle. Quotienting by that circle gives the resultant coadjoint orbit

```math
\Sigma_\ell / U(1)_{\widehat L}
\cong \mathcal O_\ell
\cong S^2_\ell.
```

This quotient keeps the direction of `L` as physical data. It is therefore the orbit whose quantization gives the representation `D^(ell)`.

This must not be confused with the full Marsden-Weinstein reduction by the diagonal SU(2). The full reduced multiplicity space is

```math
\mathcal M_n //_{\mathcal O_\ell} SU(2)
= \mu^{-1}(\mathcal O_\ell)/SU(2),
```

which is zero-dimensional for the equal-spin tensor product. That zero-dimensional quotient records the Clebsch-Gordan multiplicity one:

```math
D^{(j)}\otimes D^{(j)}
= \bigoplus_{\ell=0}^{2j} D^{(\ell)}.
```

Thus the correct geometric statement is:

```text
fixed coupling radius -> circle quotient -> resultant orbit O_ell -> quantizes to D^(ell);
full diagonal SU(2) quotient -> point -> multiplicity one.
```

Endpoint note. At `ell=0` and `ell=2j`, the generic principal-bundle description becomes singular. At `ell=0`, the resultant direction is undefined before quotienting and the orbit `O_0` is a point. At `ell=2j`, the two Bloch vectors are aligned and the relative circle collapses. These are the expected boundary strata of the coupling polytope.

## 4. Quantization of the resultant orbit

The resultant orbit `\mathcal O_\ell\cong S^2` carries

```math
\omega_\ell
= \ell\hbar\,\sin\vartheta\,d\vartheta\wedge d\varphi.
```

Its symplectic area is

```math
\int_{S^2}\omega_\ell = 4\pi\ell\hbar.
```

The prequantum line has Chern number

```math
c_1 = \frac{1}{2\pi\hbar}\int_{S^2}\omega_\ell = 2\ell.
```

Holomorphic quantization of `CP^1` with line bundle `\mathcal O(2\ell)` gives

```math
\dim H^0(CP^1,\mathcal O(2\ell)) = 2\ell+1.
```

Therefore the coupling foliation reproduces the entire shell dimension:

```math
\sum_{\ell=0}^{2j} (2\ell+1)
= (2j+1)^2
= n^2.
```

This is the SU(2) Clebsch-Gordan case of the broader principle that quantization and reduction are compatible: the resultant orbit carries the irreducible representation, while the full reduced quotient carries the multiplicity.

## 5. Clebsch-Gordan coefficients as the transition matrix

Use normalized SU(2) coherent states

```math
|j,z\rangle
= (1+|z|^2)^{-j}
\sum_{m=-j}^{j}
\binom{2j}{j+m}^{1/2}
 z^{j+m}|j,m\rangle.
```

Then the product coherent state is

```math
|z_+,z_-\rangle
= |j,z_+\rangle\otimes |j,z_-\rangle.
```

Expanding into the diagonal angular-momentum basis gives

```math
\langle \ell,m|z_+,z_-\rangle
=
\sum_{m_+ + m_- = m}
\langle \ell,m|j,m_+;j,m_-\rangle
\frac{\binom{2j}{j+m_+}^{1/2} z_+^{j+m_+}}{(1+|z_+|^2)^j}
\frac{\binom{2j}{j+m_-}^{1/2} z_-^{j+m_-}}{(1+|z_-|^2)^j}.
```

The Clebsch-Gordan coefficient is the exact unitary transition coefficient between:

```text
product/parabolic weight coordinates: |j,m_+> |j,m_->
spherical/orbital coordinates:        |ell,m>
```

This is the mathematical content behind the Tetryonics drawing. A cell is not itself an orbital multiplet. A cell is a product-weight basis vector. The orbital multiplet is obtained by Clebsch-Gordan summation over cells.

## 6. Corrected Tetryonics-to-geometry dictionary

| Tetryonics / cell-language object | Heller-Dirac geometric object | Correct mathematical reading |
|---|---|---|
| Cell labelled `(m_+,m_-)` | Product weight vector | `|j,m_+>\otimes |j,m_->`; simultaneous eigenstate of `J^+_z,J^-_z` |
| Classical shadow of a cell | Point or small packet on `S^2_j x S^2_j` | Exact `J_z` eigenstates are not coherent points; they localize semiclassically as latitude data |
| Anti-diagonal `m_+ + m_- = m` | Fixed `L_z` subspace | Since `L_z=J^+_z+J^-_z`, this fixes magnetic quantum number `m`, not `ell` |
| Difference `m_+ - m_-` | Runge-Lenz/parabolic separator | Since `A_z=J^+_z-J^-_z`, this is the natural parabolic coordinate |
| Spherical `ell` layer | Resultant coadjoint orbit `O_ell` | Quantizes to `D^(ell)` of dimension `2ell+1` |
| Cell weight inside `|ell,m>` | Clebsch-Gordan coefficient | `\langle j,m_+;j,m_-|\ell,m\rangle` with `m_+ + m_- = m` |
| Corner `(j,j)` | Stretched product cell | Pure top state of `D^(2j)`: `|2j,2j>` |
| Corners `(j,-j)` and `(-j,j)` | Extreme parabolic / Runge-Lenz-polarized cells | They are not pure `ell=0`; the `ell=0` state is a CG-weighted alternating sum over all `(m,-m)` cells |
| `L_\pm` operation | Diagonal SU(2) raising/lowering | Preserves `ell` in the spherical basis and sends `m -> m\pm1`; in the product basis it produces a two-term move to neighboring anti-diagonals |
| `J^+_\pm` or `J^-_\pm` alone | One-factor shift | Generally mixes `ell` after CG rotation |

The triangle is therefore best read as a parabolic weight chart for `D^(j)_+ \otimes D^(j)_-`. The spherical basis is obtained by Clebsch-Gordan rotation. The same shell admits both descriptions:

```text
parabolic basis: natural for Stark / Runge-Lenz splitting;
spherical basis: natural for central, Zeeman, spin-orbit, and Dirac angular structure.
```

## 7. What this sets up for step (b): quantum defects

The clean product shell relies on exact Coulomb symmetry. In a real alkali-like atom, the outer electron sees an effective core. Short-range penetration and polarization break SO(4) while preserving ordinary rotational SO(3) to a good approximation.

The empirical Rydberg-Ritz form is

```math
E_{n\ell}
\simeq
-\frac{R_M Z_c^2}{(n-\delta_\ell)^2},
\qquad
n^* = n-\delta_\ell.
```

The formal geometric lesson is not that `j` should simply be replaced by a non-half-integer `j^*`. That would destroy the integrality condition required for SU(2) coadjoint-orbit quantization. The better reading is:

```text
angular orbit O_ell remains integrally quantized;
quantum defect enters as a radial action / short-range phase defect attached to the ell leaf.
```

In EBK/Langer language, the effective action may be represented schematically as

```math
I_{\mathrm{eff}}(E,\ell)
= I_r(E,\ell) + L_{\mathrm{Langer}}
= \hbar(n-\delta_\ell),
```

with

```math
L_{\mathrm{Langer}}\sim \hbar(\ell+\tfrac12),
\qquad
I_r \sim \hbar(n_r+\tfrac12-\delta_\ell),
\qquad
n=n_r+\ell+1.
```

Thus step (b) should deform the radial action and the energy assignment of each `ell` leaf, not the integrality of the angular orbit. The degeneracy no longer runs over all `ell` at fixed nominal `n`; instead, each `ell` layer receives a defect-dependent energy.

Corrected wording:

```text
The Coulomb shell tears along CG ell-multiplet layers, not along raw anti-diagonals.
Anti-diagonals are fixed L_z slices. Quantum defects are ell-dependent splittings.
```

If an energy-dependent defect is needed, use the extended Ritz form

```math
\delta_\ell(E) = \delta_{\ell,0} + \frac{a}{(n-\delta_{\ell,0})^2}
+ \frac{b}{(n-\delta_{\ell,0})^4}+\cdots.
```

## 8. What this sets up for step (a): Dirac extension

The relativistic extension changes the angular bookkeeping. The nonrelativistic orbital `L` is no longer the final conserved angular label; the Dirac-Coulomb problem uses total angular momentum

```math
J = L + S
```

and Dirac's angular operator usually encoded by `\kappa = \pm(j_{\mathrm{tot}}+1/2)`. The bound-state Dirac energy can be written in the form

```math
E_{n\kappa}
= mc^2\left[1+
\frac{(Z\alpha)^2}{\left(n-|\kappa|+\sqrt{\kappa^2-(Z\alpha)^2}\right)^2}
\right]^{-1/2}.
```

Thus the Heller-Dirac extension should be organized as:

```text
SO(4) orbital shell
-> diagonal SU(2) orbital coupling ell
-> radial quantum-defect deformation attached to ell
-> spinor/Dirac lift replacing ell-only labels by total angular and kappa labels
-> positive/negative energy branch bookkeeping, where Dirac's hole/sea picture becomes structurally relevant.
```

Dirac's name is therefore not ceremonial. The hole/sea picture indicates that the relativistic layer is a branch-and-charge accounting system, not merely a small perturbative correction to the nonrelativistic geometry.

## 9. Definition-of-done for this c0 note

This c0 formalization is complete when the repository contains:

1. the orbit-product model `S^2_j x S^2_j`;
2. the diagonal moment map `mu=J_+ + J_-`;
3. the fixed-opening-angle relation for `ell`;
4. the distinction between coupling-orbit quotient and full Marsden-Weinstein reduction;
5. the quantization calculation giving `2ell+1`;
6. the Clebsch-Gordan transition formula;
7. the corrected Tetryonics dictionary;
8. the precise handoff to quantum-defect deformation;
9. the precise handoff to the Dirac/kappa layer;
10. explicit non-claim boundaries.

## References and anchors

- V. Guillemin and S. Sternberg, "Geometric Quantization and Multiplicities of Group Representations," Inventiones Mathematicae 67 (1982), 515-538.
- G. J. Maclay, "Dynamical Symmetries of the H Atom, One of the Most Important Tools of Modern Physics: SO(4) to SO(4,2)," Symmetry 12(8), 1323 (2020).
- NIST Atomic Spectroscopy, "Term Series, Quantum Defects, and Spectral-line Series," including Rydberg-Ritz and extended Ritz quantum-defect formulas.
- Standard Dirac-Coulomb spectrum references for the `n, kappa` energy formula and the replacement of orbital-only labels by total-angular spinor labels.
- Standard SU(2) coherent-state and Clebsch-Gordan representation theory references for the coherent overlap formula.
