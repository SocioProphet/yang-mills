# Heller-Dirac b0: quantum-defect deformation as radial-action phase defect

Status: program-context mathematical sidecar.  
Claim class: semiclassical and representation-theoretic formalization of the Rydberg-Ritz quantum-defect layer.  
Non-claims: this file does not predict empirical defect constants from first principles, does not change the Yang-Mills theorem track, and does not replace angular SU(2) integrality by nonintegral orbit labels.

## 0. Purpose

This note formalizes step (b) of the Heller-Dirac build order:

```text
(c) geometric foundation -> (b) quantum-defect deformation -> (a) relativistic/Dirac extension
```

Step (c) gave the exact Coulomb shell:

```math
\mathcal H_n
\cong D^{(j)}_+\otimes D^{(j)}_-,
\qquad
j=\frac{n-1}{2},
```

with diagonal decomposition

```math
D^{(j)}\otimes D^{(j)}
= \bigoplus_{\ell=0}^{2j}D^{(\ell)}.
```

The Coulomb Hamiltonian depends only on `n`, so every `ell` layer in the same principal shell is degenerate. Quantum defects are the controlled failure of that degeneracy for real alkali-like atoms and other Rydberg systems with a nontrivial core.

The key correction from the first draft is:

```text
quantum defects do not make the angular coadjoint orbit nonintegral;
quantum defects deform the radial action / short-range phase attached to each ell layer.
```

## 1. Empirical Rydberg-Ritz layer

For a hydrogenic one-electron ion, the bound energies scale as

```math
E_n = -\frac{R_M Z^2}{n^2},
```

where `R_M` is the Rydberg constant corrected for nuclear mass. For a Rydberg electron outside a core, the effective series is commonly written

```math
E_{n\ell}
\simeq
-\frac{R_M Z_c^2}{(n-\delta_\ell)^2}
= -\frac{R_M Z_c^2}{(n^*)^2},
\qquad
n^* = n-\delta_\ell.
```

Here `Z_c` is the core charge seen by the Rydberg electron and `\delta_\ell` is the quantum defect. If fine structure is being resolved, replace `\delta_\ell` by `\delta_{\ell j_{\mathrm{tot}}}`.

For higher precision or lower members of a series, use the extended Ritz form

```math
\delta_\ell(n)
= \delta_{\ell,0}
+ \frac{a_\ell}{(n-\delta_{\ell,0})^2}
+ \frac{b_\ell}{(n-\delta_{\ell,0})^4}
+ \cdots.
```

Interpretation:

```text
low ell:  larger defect, dominated by core penetration;
high ell: smaller defect, dominated by polarization and asymptotic corrections;
ell -> large: defect generally trends toward the hydrogenic value.
```

This preserves rotational SO(3) but breaks the hidden Coulomb SO(4). The magnetic degeneracy over `m=-ell,...,ell` remains unless additional fields or spin-dependent interactions are introduced.

## 2. Action-angle formulation

For a central effective potential, use radial momentum

```math
p_r(r;E,L)
= \sqrt{2m(E-V_{\mathrm{eff}}(r))-\frac{L^2}{r^2}}.
```

The radial action is

```math
I_r(E,L)
= \frac{1}{2\pi}\oint p_r\,dr
= \frac{1}{\pi}\int_{r_-}^{r_+}p_r\,dr.
```

With the Langer correction,

```math
L_\ell = \hbar\left(\ell+\frac12\right),
```

and the Coulomb EBK rule reads

```math
I_r + L_\ell = \hbar n,
\qquad
n=n_r+\ell+1.
```

The quantum-defect deformation replaces this by

```math
I_r^{\mathrm{eff}}(E,\ell)+L_\ell
= \hbar(n-\delta_\ell).
```

Equivalently,

```math
I_r^{\mathrm{eff}}(E,\ell)
=\hbar\left(n_r+\frac12-\delta_\ell\right).
```

Thus `\delta_\ell` is a radial phase/action defect, not an angular orbit-volume defect.

## 3. Symplectic reading

The Coulomb shell admits the compact angular model

```math
\mathcal M_n = \mathcal O_j^+\times\mathcal O_j^-.
```

This is the correct object for the exact SO(4) degeneracy. Once the core is introduced, the hidden SO(4) symmetry is broken. The surviving clean symmetry is ordinary rotational SO(3), so the angular leaf remains

```math
\mathcal O_\ell\cong S^2_\ell,
\qquad
\int_{S^2}\omega_\ell = 4\pi\ell\hbar,
\qquad
\dim Q(\mathcal O_\ell)=2\ell+1.
```

The defect is attached to the radial circle/phase over that angular leaf. A useful schematic phase-space form is

```math
\omega
= dI_r\wedge d\theta_r
+ dL\wedge d\theta_L
+ dL_z\wedge d\phi.
```

The quantum defect modifies the radial holonomy:

```math
\theta_r \mapsto \theta_r - 2\pi\delta_\ell
```

or, equivalently, shifts the radial action level by `\hbar\delta_\ell`. This is the clean geometric version of the phrase "the shell tears." It tears along `ell`-multiplet sheets in energy, while the angular coadjoint orbit remains integrally quantized.

Incorrect wording to avoid:

```text
The Bloch spheres acquire nonintegral radii j* = (n-delta_ell-1)/2.
```

Correct wording:

```text
The angular orbit O_ell remains integral. The radial action over O_ell receives an ell-dependent phase defect, producing E_{nell} instead of E_n.
```

## 4. Operator-level deformation

Let `N` denote the nominal principal-shell operator and let `\Pi_\ell` be the projector onto the diagonal `D^(ell)` summand inside the shell. The defect layer can be represented by a diagonal operator

```math
\widehat\Delta
= \sum_{\ell=0}^{n-1}\delta_\ell\,\Pi_\ell.
```

At the effective spectral level,

```math
\widehat H_{\mathrm{defect}}
\simeq
-R_M Z_c^2\,(N-\widehat\Delta)^{-2}.
```

This is not meant as a microscopic Hamiltonian for the core. It is a compact operator calculus for the Rydberg-Ritz energy assignment.

In the spherical basis,

```math
\widehat\Delta |\ell,m\rangle
= \delta_\ell |\ell,m\rangle.
```

In the product/parabolic cell basis,

```math
|m_+,m_-\rangle = |j,m_+\rangle\otimes |j,m_-\rangle,
```

the same operator is nonlocal across cells:

```math
\langle m_+,m_-|\widehat\Delta|m'_+,m'_-\rangle
=
\sum_{\ell,m}
\delta_\ell\,
\langle j,m_+;j,m_-|\ell,m\rangle
\langle \ell,m|j,m'_+;j,m'_-\rangle.
```

Because `m=m_++m_-=m'_++m'_-`, the kernel preserves anti-diagonal `m` but mixes cells within the same anti-diagonal according to Clebsch-Gordan weights.

This is the precise answer to the cell-picture question:

```text
quantum defects are simple in the spherical ell basis;
quantum defects look like a structured nonlocal kernel in the product-cell basis.
```

## 5. Relation to the sum/difference variables

The exact Coulomb shell has

```math
L=J_+ + J_-,
\qquad
A=J_+ - J_-.
```

The diagonal sum `L` labels the spherical multiplet. The anti-diagonal difference `A` is the Runge-Lenz direction and is responsible for the hidden degeneracy across different `ell` values.

A short-range core perturbs the Runge-Lenz conservation law. In operator language,

```math
[H_{\mathrm{core}},L^2]=0,
\qquad
[H_{\mathrm{core}},L_z]=0,
\qquad
[H_{\mathrm{core}},A]\neq 0
```

for a central but non-Coulomb core correction. Therefore the defect deformation preserves `ell,m` but breaks the exact SO(4) relation connecting different `ell` layers.

This is why the hyperbolic bridge matters later. The difference variable `A` is the compact precursor of a boost-like generator in the scattering algebra. Quantum defects are the first controlled place where the manuscript must distinguish:

```text
surviving compact rotations: L;
broken hidden Coulomb direction: A;
later relativistic branch bookkeeping: Dirac kappa and energy sign.
```

## 6. Corrected Heller-Dirac dictionary for step (b)

| Object | Coulomb c0 reading | Quantum-defect b0 reading |
|---|---|---|
| Principal shell `n` | Exact SO(4) multiplet with dimension `n^2` | Nominal series index; energy depends on `n-delta_ell` |
| `D^(ell)` layer | Degenerate orbital multiplet inside `H_n` | Energy sheet labelled by `ell` |
| `m` values | Magnetic states inside `D^(ell)` | Still degenerate under central spinless core correction |
| Product cell `(m_+,m_-)` | Parabolic/product basis vector | Not defect-diagonal; defect kernel is CG-rotated |
| Anti-diagonal `m_+ + m_-` | Fixed `L_z=m\hbar` | Preserved by central defects but not an energy layer by itself |
| Difference `m_+-m_-` | Runge-Lenz/parabolic coordinate | The coordinate most directly associated with broken hidden symmetry |
| `A=J_+-J_-` | Conserved Runge-Lenz direction | No longer conserved for non-Coulomb central core |
| Angular orbit `O_ell` | Quantizes to `2ell+1` | Remains integral; not replaced by `ell-delta` |
| Radial action | Coulomb action closes with `n` | Shifted by `delta_ell` |

## 7. Acceptance checks for this step

A correct Heller-Dirac quantum-defect section must pass these checks:

1. It preserves angular SU(2) integrality.
2. It identifies quantum defect with radial phase/action deformation.
3. It makes `E_{n\ell}` depend on `n-\delta_\ell`.
4. It keeps central-potential `m` degeneracy unless an explicit symmetry-breaking term is added.
5. It says SO(4) is broken to SO(3), not that SO(4) survives unchanged.
6. It explains why the product-cell picture is not the defect-diagonal basis.
7. It gives the Clebsch-Gordan kernel that translates the defect operator back into the cell chart.
8. It prepares the next Dirac step by leaving room for spin, `j_{\mathrm{tot}}`, `\kappa`, and positive/negative energy branches.

## References and anchors

- NIST Atomic Spectroscopy, "Term Series, Quantum Defects, and Spectral-line Series," for the Rydberg-Ritz and extended Ritz quantum-defect formulas.
- Standard EBK/Langer quantization references for the radial-action form of the Coulomb spectrum.
- Standard quantum-defect theory references for the interpretation of core penetration, core polarization, and energy-dependent defect expansions.
- The c0 Heller-Dirac symplectic-coupling note in this repository for the `SO(4) -> SU(2)_+ x SU(2)_-` shell construction and Clebsch-Gordan dictionary.
