# Heller-Dirac a0: Dirac/kappa extension and branch bookkeeping

Status: program-context mathematical sidecar.  
Claim class: structural formalization of the relativistic layer after the SO(4) shell and quantum-defect deformation.  
Non-claims: this file does not complete a quantum-field-theoretic particle zoo, does not derive empirical defect constants, and does not modify the Yang-Mills theorem track.

## 0. Purpose

This note formalizes step (a) of the Heller-Dirac build order:

```text
(c) geometric foundation -> (b) quantum-defect deformation -> (a) relativistic/Dirac extension
```

The earlier notes established:

```text
c0: exact Coulomb shell as SU(2)_+ x SU(2)_- / SO(4) geometry;
b0: real-atom quantum defects as ell-dependent radial-action phase defects.
```

The Dirac layer changes the state labels. The nonrelativistic orbital label `ell` is no longer the final angular label; spin and relativistic branch structure must be added. The correct relativistic angular label is Dirac's `kappa`.

## 1. From orbital multiplets to spinor multiplets

The nonrelativistic angular layer uses

```math
L^2|\ell,m\rangle=\hbar^2\ell(\ell+1)|\ell,m\rangle,
\qquad
L_z|\ell,m\rangle=\hbar m|\ell,m\rangle.
```

The Dirac layer introduces spin `S=\frac{\hbar}{2}\sigma` and total angular momentum

```math
J=L+S.
```

The commuting labels become

```math
J^2,
\qquad
J_z,
\qquad
K,
```

where the Dirac angular operator is conventionally

```math
K=\beta(\Sigma\cdot L+\hbar).
```

Its eigenvalue is encoded by an integer `\kappa`:

```math
K\Omega_{\kappa m_j} = -\hbar\kappa\,\Omega_{\kappa m_j}
```

up to the common sign convention chosen for `K`. The integer `\kappa` satisfies

```math
\kappa = \pm\left(j_{\mathrm{tot}}+\frac12\right),
\qquad
j_{\mathrm{tot}}=|\kappa|-\frac12.
```

The corresponding orbital angular momenta are

```math
\ell = \begin{cases}
\kappa, & \kappa>0,\\
-\kappa-1, & \kappa<0,
\end{cases}
\qquad
\ell' = \begin{cases}
\kappa-1, & \kappa>0,\\
-\kappa, & \kappa<0.
\end{cases}
```

The Dirac spinor has two radial components whose angular parts are paired spinor spherical harmonics:

```math
\psi_{n\kappa m_j}(r,\theta,\phi)
=
\frac{1}{r}
\begin{pmatrix}
F_{n\kappa}(r)\,\Omega_{\kappa m_j}(\theta,\phi)\\
iG_{n\kappa}(r)\,\Omega_{-\kappa m_j}(\theta,\phi)
\end{pmatrix}.
```

Thus the Dirac lift does not merely add spin as a tensor-product decoration. It pairs two orbital angular sectors inside one spinor state.

## 2. Dirac-Coulomb spectrum

For a pure Coulomb potential, define

```math
\gamma_\kappa = \sqrt{\kappa^2-(Z\alpha)^2}.
```

Let `n_r=0,1,2,...` be the radial quantum number and

```math
n = n_r + |\kappa|.
```

The bound Dirac-Coulomb energy is

```math
E_{n\kappa}^{(+)}
= mc^2\left[1+
\frac{(Z\alpha)^2}{(n_r+\gamma_\kappa)^2}
\right]^{-1/2}.
```

Equivalently,

```math
E_{n\kappa}^{(+)}
= mc^2\left[1+
\frac{(Z\alpha)^2}{\left(n-|\kappa|+\sqrt{\kappa^2-(Z\alpha)^2}\right)^2}
\right]^{-1/2}.
```

The negative-energy branch is

```math
E_{n\kappa}^{(-)}=-E_{n\kappa}^{(+)}
```

for the corresponding Coulomb branch in the idealized one-particle Dirac equation. Modern interpretation treats the negative-energy sector through field quantization and antiparticle creation/annihilation bookkeeping. The Heller-Dirac manuscript should therefore keep the branch label explicit rather than treating negative energy as ordinary occupied electron states.

## 3. Where quantum defects enter after Dirac

The b0 note used

```math
E_{n\ell}\simeq -\frac{R_M Z_c^2}{(n-\delta_\ell)^2}.
```

After the Dirac lift, the defect label should generally refine from `ell` to the relativistic channel:

```math
\delta_\ell \quad\leadsto\quad \delta_{\kappa}
\quad\text{or}\quad
\delta_{\ell j_{\mathrm{tot}}}.
```

A conservative effective replacement is

```math
n_r+\gamma_\kappa
\quad\leadsto\quad
n_r+\gamma_\kappa-\delta_\kappa^{\mathrm{rel}}(n).
```

This gives the schematic relativistic-defect energy

```math
E_{n\kappa}^{(+),\mathrm{defect}}
\simeq
mc^2\left[1+
\frac{(Z_c\alpha)^2}
{(n_r+\gamma_\kappa-\delta_\kappa^{\mathrm{rel}}(n))^2}
\right]^{-1/2}.
```

This is an effective channel formula, not a first-principles core Hamiltonian. For real atoms, fine structure, core polarization, spin-orbit coupling, Lamb shifts, hyperfine effects, isotope shifts, and many-body corrections may all enter depending on precision.

The manuscript rule is:

```text
b0 defects are ell-channel radial phase defects;
a0 relativistic defects are kappa-channel radial/spinor phase defects.
```

## 4. Reinterpreting the SO(4) sum/difference split

The c0/addendum layer used

```math
L=J_+ + J_-,
\qquad
A=J_+ - J_-.
```

Here `A` is the normalized Runge-Lenz direction on the fixed Coulomb energy shell. It is the anti-diagonal variable, the compact hidden-symmetry coordinate, and the bridge to hyperbolic scattering geometry.

The Dirac extension adds three new pieces of bookkeeping:

```text
spinor angular coupling:       L + S -> J;
Dirac channel label:           ell -> kappa;
energy/charge branch label:    positive / negative energy.
```

The correct conceptual flow is therefore

```text
SU(2)_+ x SU(2)_- compact shell
-> diagonal L and anti-diagonal A
-> defect breaks exact A-conservation while preserving rotational L/J labels
-> Dirac lift replaces ell by kappa and introduces branch structure
```

The phrase "Dirac's sea" should be used with care. In this manuscript it means a historical and structural cue: relativistic quantum mechanics forces branch bookkeeping. It should not be used as a literal many-electron medium unless the model has actually been second-quantized.

## 5. Particle-zoo opening: allowed but not yet completed

The Heller-Dirac framework can open a controlled particle-zoo taxonomy only after the following labels are separated:

| Layer | Label | Meaning |
|---|---|---|
| Coulomb shell | `n` | nominal principal/radial shell |
| Orbital geometry | `ell,m` | nonrelativistic SO(3) orbital multiplet |
| Hidden Coulomb geometry | `A` or parabolic labels | Runge-Lenz / eccentricity / Stark-natural direction |
| Defect channel | `delta_ell`, then `delta_kappa` | short-range phase/action deformation |
| Spinor geometry | `j_tot,m_j,kappa` | relativistic angular channel |
| Branch | `s_E=+/-` | positive/negative energy sector |
| Charge/QFT layer | particle/antiparticle creation operators | only valid after second quantization |
| Gauge/internal layer | charge, color, flavor, isospin, generation | not supplied by the hydrogenic Dirac-Coulomb model alone |

This prevents the common error of jumping from a Dirac hydrogen atom directly to the full particle zoo. Heller-Dirac should instead use the atom as the disciplined seed of a classification architecture:

```text
geometry -> channel labels -> radial phases -> spinor branches -> field operators -> internal gauge charges.
```

Only the first four items are present in the current Heller-Dirac sidecar.

## 6. Basis dictionary after the Dirac lift

| c0/b0 object | a0 Dirac object | Comment |
|---|---|---|
| `|ell,m>` | `|kappa,m_j>` spinor spherical harmonic | `ell` alone is insufficient once spin is active |
| `D^(ell)` | total-angular spinor channel | dimension counted by `2j_tot+1`, not `2ell+1` alone |
| `A=J_+-J_-` | hidden Coulomb direction, modified by relativistic dynamics | survives as structural ancestor, but must be rechecked under Dirac operators |
| defect `delta_ell` | defect `delta_kappa` or `delta_{ell j}` | fine-structure-resolved channel defect |
| product cell `(m_+,m_-)` | pre-spin parabolic/product coordinate | requires CG plus spin coupling to reach Dirac basis |
| anti-diagonal `m_++m_-` | predecessor of magnetic projection | final projection is `m_j`, not merely `m` |
| branch absent | `E^+` / `E^-` | relativistic layer requires explicit branch label |

## 7. Acceptance checks for this step

A correct Heller-Dirac relativistic section must pass these checks:

1. It replaces orbital-only labels by `kappa` and total angular labels.
2. It states the spinor spherical-harmonic pairing of `kappa` and `-kappa`.
3. It keeps the Dirac-Coulomb spectrum separate from empirical core defect models.
4. It refines `delta_ell` to `delta_kappa` or `delta_{ell j}` when fine structure matters.
5. It treats the negative-energy branch as branch bookkeeping, not a literal many-electron claim unless second quantization is introduced.
6. It does not claim that hydrogenic Dirac labels already contain color, flavor, or full Standard Model internal charges.
7. It preserves the c0/b0 sum-difference architecture rather than overwriting it.
8. It prepares a later QFT/gauge taxonomy without prematurely asserting one.

## References and anchors

- Standard Dirac-Coulomb spectrum and spinor spherical harmonic references for the `n,kappa,m_j` labeling system.
- Standard relativistic quantum mechanics references for the operator `K=beta(Sigma dot L + hbar)` and the `kappa` convention.
- Standard quantum-defect theory references for fine-structure-resolved channel defects.
- The c0 and b0 Heller-Dirac notes in this repository for the SO(4) shell, sum/difference variables, and radial-action defect layer.
