# Heller-Dirac f0: finite-part boundary constants and channel defects

Status: program-context sidecar note.  
Source prompt: finite-part boundary constant principle v0.1.  
Claim class: translation of a Yang-Mills finite-part discipline into Heller-Dirac channel language.  
Non-claims: this file does not assert a Yang-Mills theorem, a continuum construction, a Clay result, a first-principles quantum-defect computation, or a completed particle taxonomy.

## 0. Purpose

The finite-part boundary constant memorandum introduces a useful discipline:

```text
identify the universal divergent/background part;
subtract it canonically;
name the finite residue;
require that the residue bite, meaning it must force an observable or spectral consequence.
```

For Yang-Mills, that memorandum uses Euler's constant as the scalar prototype and frames a hypothetical finite part `Gamma_YM` whose existence would still be insufficient unless it implies uniform clustering and a positive Hamiltonian gap.

For Heller-Dirac, the same discipline applies at a different substrate level. The relevant finite part is not a Yang-Mills mass-gap invariant. It is the finite channel boundary phase/action residue created by matching a short-range core or relativistic inner region to the outer Coulomb/Dirac-Coulomb problem.

In Heller-Dirac notation, the finite residue is the quantum defect:

```math
\Gamma_{\mathrm{HD},\ell}(E) \equiv \hbar\,\delta_\ell(E)
```

or, after the Dirac lift,

```math
\Gamma_{\mathrm{HD},\kappa}(E) \equiv \hbar\,\delta_\kappa(E).
```

The sign convention depends on whether the radial action is written as `I_r=\hbar(n_r+1/2-\delta)` or as a boundary phase shift. The invariant content is the finite channel residue, not the sign.

## 1. Scalar prototype and translation

The scalar prototype is Euler's constant:

```math
\gamma=\lim_{n\to\infty}\left(H_n-\log n\right).
```

This has the form

```math
\text{discrete cutoff object}
=
\text{universal divergent comparison term}
+
\text{finite residue}
+o(1).
```

Heller-Dirac uses the same operation, but not the same object. The channel action has the schematic form

```math
I_{r,\ell}^{\mathrm{full}}(E;\varepsilon,R)
=
I_{r,\ell}^{\mathrm{Coul}}(E;\varepsilon,R)
+D_{\ell}^{\mathrm{univ}}(\varepsilon,R)
-\hbar\delta_\ell(E)
+o(1),
```

where:

```text
I_full      = radial action for the effective core/inner-region problem;
I_Coul      = reference Coulomb radial action;
D_univ      = convention-dependent universal comparison/divergent term;
hbar delta  = finite channel boundary residue.
```

Equivalently,

```math
\hbar\delta_\ell(E)
=
-\operatorname{FP}_{\varepsilon\to0,\,R\to\infty}
\left(
I_{r,\ell}^{\mathrm{full}}(E;\varepsilon,R)
-I_{r,\ell}^{\mathrm{Coul}}(E;\varepsilon,R)
-D_{\ell}^{\mathrm{univ}}(\varepsilon,R)
\right).
```

This is the finite-part boundary constant form of the quantum defect.

## 2. Three-regime taxonomy in Heller-Dirac language

The finite-part memorandum separates constants into three regimes. Heller-Dirac inherits all three, but with different concrete roles.

| Regime | General form | Heller-Dirac instance |
|---|---|---|
| Algebraic closure constants | finite recurrence / closure constants | finite Clebsch-Gordan dimensions, projector ranks, low-`n` channel matrices |
| Torsion / phase constants | sign, parity, monodromy, spin lifts | spinor sign conventions, `kappa` sign, parity, large/small component pairing |
| Renormalized finite-defect constants | finite residues after subtracting reference divergences | `delta_ell(E)`, `delta_kappa(E)`, channel boundary phase/action defects |

Thus the Heller-Dirac sidecar is not only a representation chart. It has a finite-part layer: the real-atom correction is the finite residue produced when the actual inner/core boundary condition is compared to the reference Coulomb or Dirac-Coulomb boundary condition.

## 3. Heller-Dirac finite-part boundary constant principle

Principle. A Heller-Dirac channel-defect construction must:

1. Define a channel-resolved cutoff/matching object `A_{HD,\lambda}(E;\varepsilon,R)`, where `\lambda` is `ell` in the nonrelativistic layer or `kappa` in the Dirac layer.
2. Identify a universal reference part `D^{univ}_{\lambda}(\varepsilon,R)` determined by the chosen Coulomb or Dirac-Coulomb outer problem and matching convention.
3. Define the finite part

```math
\Gamma_{\mathrm{HD},\lambda}(E)
=\operatorname{FP}
\left(A_{\mathrm{HD},\lambda}(E;\varepsilon,R)
-D^{\mathrm{univ}}_{\lambda}(\varepsilon,R)
\right).
```

4. Relate it to the dimensionless defect by

```math
\Gamma_{\mathrm{HD},\lambda}(E)=\hbar\delta_\lambda(E)
```

up to the declared sign convention.

5. Prove that the residue bites spectrally by producing the channel energy shift:

```math
E_{n\ell}\simeq -\frac{R_M Z_c^2}{(n-\delta_\ell)^2}
```

or, in the Dirac layer, by the channel replacement

```math
n_r+\gamma_\kappa
\leadsto
n_r+\gamma_\kappa-\delta_\kappa(E).
```

Compressed form:

```text
FP(channel boundary matching)
-> quantum defect delta_lambda
-> channel energy splitting
-> basis-kernel consequences in product-cell coordinates.
```

This is not a first-principles theory of the numerical defect constants. It is the correct structural placement of the constants inside Heller-Dirac.

## 4. The biting requirement for Heller-Dirac

Weak version to avoid:

```text
There is a finite residue in the radial problem, therefore the Heller-Dirac theory is solved.
```

Strong version:

```text
A Heller-Dirac finite-part boundary constant must be canonical within a declared matching class, stable under reference-coordinate changes, channel-resolved, compatible with angular SU(2) integrality, and demonstrably tied to the observed or modeled channel energy splitting.
```

For the sidecar currently in this repository, the biting checks are finite and modest:

1. `delta_ell` is diagonal in the spherical `ell` basis.
2. The same operator becomes a Clebsch-Gordan-rotated kernel in the product-cell basis.
3. Equal channel shifts collapse to a scalar operator and restore the Coulomb degeneracy.
4. The Dirac lift refines `ell` to `kappa` without erasing spinor branch structure.
5. No finite residue is allowed to promote a Yang-Mills theorem-track claim.

## 5. Relationship to existing Heller-Dirac files

| Existing file | Finite-part interpretation |
|---|---|
| `03-symplectic-coupling-reduction.md` | supplies the exact Coulomb reference shell and angular channel labels |
| `04-quantum-defect-deformation.md` | identifies `delta_ell` as radial-action phase defect |
| `05-dirac-kappa-extension.md` | refines the channel from `ell` to `kappa` |
| `07-cg-audit-n2-n4.md` | verifies the projector basis where the channel residue is diagonal |
| `08-channel-kernels-n3-n4.md` | verifies the product-cell kernel form and scalar-collapse limit |

The finite-part note therefore does not replace the earlier notes. It supplies the missing organizing principle: `delta` is a finite boundary constant.

## 6. Explicit separation from Yang-Mills Gamma_YM

The source memorandum defines a Yang-Mills candidate finite part schematically as

```math
\Gamma_{\mathrm{YM}}
=\operatorname{FP}(\mathcal A_{a,L}^{\mathrm{YM}}-D_{a,L}^{\mathrm{univ}}).
```

Heller-Dirac must not conflate this with its own channel constants.

| Object | Substrate | Biting requirement |
|---|---|---|
| `Gamma_YM` | cutoff gauge-field theory / Yang-Mills interface | uniform clustering and OS-positive Hamiltonian gap |
| `Gamma_HD,ell` | nonrelativistic radial channel matching | Rydberg-Ritz channel splitting |
| `Gamma_HD,kappa` | Dirac-Coulomb spinor channel matching | relativistic channel splitting with branch bookkeeping |

The analogy is methodological, not a transfer of theorem status.

## 7. SocioSphere gate implication

The proof adapter should treat this note as a boundary/check discipline. The relevant gate is not a theorem gate. It is a claim-boundary gate:

```text
hd-finite-part-boundary-constant
```

Expected content:

```text
Heller-Dirac finite-part constants are radial/channel boundary residues that organize quantum defects. They do not constitute a Yang-Mills finite part, a continuum mass-gap invariant, a first-principles defect prediction, or a completed particle taxonomy.
```

## 8. Acceptance checks

A future Heller-Dirac finite-part expansion must pass these checks:

1. It names the reference problem being subtracted: Coulomb or Dirac-Coulomb.
2. It names the cutoff/matching parameters.
3. It states the universal/background comparison term.
4. It defines the finite part as a channel quantity.
5. It gives the sign convention relating the finite part to `delta_ell` or `delta_kappa`.
6. It demonstrates the spectral consequence: energy shift, splitting, or scalar-collapse restoration.
7. It preserves angular integrality and does not replace SU(2) orbit labels by nonintegral defects.
8. It preserves the Yang-Mills non-claim boundary.

## 9. Source memorandum anchors

The source memorandum contributes the following imported concepts:

- Euler's constant as finite residue after subtracting a universal logarithmic divergence.
- The three-regime taxonomy: algebraic closure constants, torsion/phase constants, and renormalized finite-defect constants.
- The finite-part principle: define the cutoff object, subtract the universal divergent/reference part, name the finite residue, and require it to bite.
- The non-claim discipline: finite-part language by itself does not prove a spectral theorem.

The Heller-Dirac adaptation keeps those ideas but changes the substrate from Yang-Mills cutoff fields to Coulomb/Dirac-Coulomb channel matching.
