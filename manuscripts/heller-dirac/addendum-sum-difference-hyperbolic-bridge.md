# Heller-Dirac addendum: sum/difference variables and the hyperbolic bridge

Status: program-context addendum to the Heller-Dirac symplectic-coupling note.  
Claim class: structural clarification of the Coulomb `SO(4)` variables and their continuation to the scattering / hyperbolic algebra.  
Non-claims: this file does not assert a new spectrum theorem, a Yang-Mills theorem, or a completed Dirac extension.

## 1. Core correction

The two-sphere product should not be read as two physical spheres separated by an ordinary spatial distance. It is a product of two equal `SU(2)` coadjoint orbits:

```math
\mathcal M_n = \mathcal O_j^+ \times \mathcal O_j^-,
\qquad
x_\pm = j\hbar\,\widehat\Omega_\pm.
```

There are two natural linear combinations:

```math
L = x_+ + x_-,
\qquad
A = x_+ - x_-.
```

The sum variable `L` is the physical orbital angular momentum. The difference variable `A` is the normalized Runge-Lenz direction on the fixed Coulomb energy shell. Thus the apparent distance between the two Bloch endpoints is not incidental; it is the anti-diagonal hidden-symmetry coordinate.

## 2. Geometry of the opening angle

Let `r=j\hbar` and let `\Theta` be the angle between `\widehat\Omega_+` and `\widehat\Omega_-`. Then

```math
|L|^2 = |x_+ + x_-|^2
= 2r^2(1+\cos\Theta)
= 4r^2\cos^2(\Theta/2),
```

while

```math
|A|^2 = |x_+ - x_-|^2
= 2r^2(1-\cos\Theta)
= 4r^2\sin^2(\Theta/2).
```

The variables are orthogonal:

```math
L\cdot A = (x_+ + x_-)\cdot(x_+ - x_-)
= |x_+|^2-|x_-|^2=0,
```

and satisfy the compact-shell constraint

```math
|L|^2 + |A|^2 = 4r^2.
```

Therefore the opening angle `\Theta` encodes an exchange between ordinary orbital angular momentum and the hidden Runge-Lenz/eccentricity direction.

Extreme cases:

```text
Theta = 0      ->  x_+ and x_- aligned      -> |L| maximal, |A| zero.
Theta = pi     ->  x_+ and x_- antiparallel -> |L| zero,    |A| maximal.
```

This is the precise sense in which the product-sphere picture contains a difference operator. It is not a finite-difference derivative. It is the anti-diagonal moment-map coordinate.

## 3. Algebraic bridge to hyperbolic geometry

For the Coulomb problem, the angular momentum and Runge-Lenz vector obey the Poisson-bracket structure

```math
\{L_i,L_j\}=\epsilon_{ijk}L_k,
\qquad
\{L_i,A_j\}=\epsilon_{ijk}A_k,
\qquad
\{A_i,A_j\}=-2mH\,\epsilon_{ijk}L_k.
```

The sign of the energy controls the symmetry type.

For bound states, `H<0`. After normalizing

```math
B = \frac{A}{\sqrt{-2mH}},
```

one gets

```math
\{B_i,B_j\}=+\epsilon_{ijk}L_k.
```

Then

```math
J_+ = \frac{1}{2}(L+B),
\qquad
J_- = \frac{1}{2}(L-B)
```

generate two compact `SU(2)` algebras:

```math
SO(4) \cong \frac{SU(2)_+\times SU(2)_-}{\mathbb Z_2}.
```

For scattering states, `H>0`. With

```math
B = \frac{A}{\sqrt{2mH}},
```

the sign flips:

```math
\{B_i,B_j\}=-\epsilon_{ijk}L_k.
```

This is the Lorentz algebra:

```math
SO(3,1),
```

with `L` rotation-like and `B` boost-like. At `H=0`, the contraction is the Euclidean algebra `E(3)`.

Thus the same anti-diagonal difference variable that appears innocently inside the compact bound-state shell is also the variable that becomes boost-like in the hyperbolic scattering sector.

## 4. Heller-Dirac interpretation

The Heller-Dirac reading should preserve three layers:

```text
compact bound shell:        SO(4)  -> two SU(2) Bloch spheres;
parabolic hidden direction: A=J_+-J_- -> Runge-Lenz / eccentricity coordinate;
hyperbolic continuation:    SO(3,1) -> the same difference variable becomes boost-like.
```

This is the structural reason the sum/difference split matters. It is not merely a convenient coordinate transform. It identifies the exact hinge between:

1. spherical orbital multiplets;
2. parabolic/Stark coordinates;
3. hyperbolic scattering geometry;
4. the later Dirac layer, where spinor, branch, and charge bookkeeping must be added without destroying the sum/difference architecture.

## 5. Implementation consequence for the manuscript

The main symplectic-coupling note should keep `L=J_++J_-` as the diagonal moment map. But the Heller-Dirac manuscript should explicitly introduce the anti-diagonal companion:

```math
A = J_+ - J_-.
```

Recommended wording:

```text
The coupling angle is simultaneously a diagonal-angular-momentum coordinate and an anti-diagonal Runge-Lenz coordinate. The diagonal sum gives the spherical/orbital multiplet. The anti-diagonal difference records the hidden Coulomb direction and is the compact precursor of the boost-like generator in the hyperbolic/scattering continuation.
```

This resolves the apparent ambiguity in the phrase "distance between the Bloch spheres." The relevant distance is the norm of the difference between the two orbit points, not a physical separation between two spheres.
