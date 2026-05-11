# Finite-Part Boundary Constant Principle

Status: program-context memorandum. Not theorem-track. Not referee material.  
Home lane: Lane III (obstruction survey, program-context companion), with Lane IV (interface specification) cross-reference.  
Version: v0.1  
Date: 2026-05-11

## Discipline header

This memorandum is program-context, not theorem-track. Nothing in it claims:

- a continuum Yang-Mills construction;
- a Clay Millennium proof;
- a weak-coupling result;
- an `SU(N >= 3)` result;
- an asymptotic-freedom trajectory result;
- a strengthening of the v0.14.4 scoped claim.

It articulates an organizing principle for what kind of invariant a future mass-gap proof, Clay-class or otherwise, would have to exhibit. It is intended to sharpen the obstruction taxonomy in Lane III and inform interface design in Lane IV. It does not feed Lane I.

## 1. The scalar prototype: Euler's constant gamma

The Euler-Mascheroni constant is

$$
\gamma = \lim_{n\to\infty}\left(\sum_{k=1}^{n}\frac{1}{k} - \log n\right) \approx 0.5772156649\ldots.
$$

`gamma` is the finite residue obtained when a discrete divergent sum is compared against its canonical continuous logarithmic divergence. It appears in identifiable form across analysis, number theory, special functions, probability, and physics.

| Context | Appearance |
| --- | --- |
| Harmonic asymptotics | $H_n = \log n + \gamma + \frac{1}{2n} - \frac{1}{12n^2} + \cdots$ |
| Riemann zeta | $\zeta(s) = \frac{1}{s-1} + \gamma + \cdots$; here $\gamma = \gamma_0$, the first Stieltjes constant |
| Zeta-value series | $\gamma = \sum_{m\geq 2}(-1)^m \zeta(m)/m$ |
| Gamma function | $\Gamma'(1) = -\gamma$ and $\Gamma(\varepsilon) = 1/\varepsilon - \gamma + O(\varepsilon)$ |
| Digamma | $\psi(1) = -\gamma$ |
| Prime products (Mertens) | $\prod_{p\leq x}(1-1/p) \sim e^{-\gamma}/\log x$ |
| Gumbel extreme-value law | mean $= \mu + \gamma\beta$ |
| Integral form | $\gamma = -\int_0^\infty e^{-x}\log x\,dx$ |

In every appearance, `gamma` is the finite part after subtracting a universal logarithmic divergence. This operation matters more than the numerical value.

## 2. Three regimes for invariants in mathematical physics

We organize structural constants in three regimes. This is a working taxonomy, not a theorem.

### Regime 1 - algebraic closure constants

Roots of integer polynomials arising from finite-state recurrences and closure relations. Examples include the golden ratio `phi` and the plastic constant `rho`, the real root of $x^3=x+1$.

### Regime 2 - torsion / phase constants

Sign-lifts, spin structures, monodromy phases, Floquet/Klein-bottle parity, center-symmetry sectors, and other finite-order sector data.

### Regime 3 - renormalized finite-defect constants

Finite residues after subtraction of universal divergences. `gamma` is the cleanest scalar example; higher Stieltjes constants, zeta residues, and finite parts of Euler products are siblings.

Yang-Mills mass-gap content lives primarily in Regime 3, with Regime 2 governing sector signs, center symmetry, and topological charge selection, and Regime 1 appearing in transfer-matrix, polymer, and recursion closure structures.

## 3. The finite-part operation, schematically

For `gamma`:

$$
H_n = \underbrace{\log n}_{\text{universal divergence}} + \underbrace{\gamma}_{\text{finite residue}} + o(1).
$$

For a Yang-Mills cutoff object $A_{\Lambda,a}$ with cutoffs $(a,L=|\Lambda|)$:

$$
A_{\Lambda,a} = D^{\mathrm{univ}}_{\Lambda,a} + I_{\mathrm{YM}} + o(1),
$$

where $D^{\mathrm{univ}}_{\Lambda,a}$ is a universal, local, gauge-invariant divergent part removable by local counterterms, and $I_{\mathrm{YM}}$ is the candidate finite-part invariant.

Formally:

$$
\Gamma_{\mathrm{YM}} \coloneqq \operatorname{FP}_{a\to 0,\,L\to\infty}\left(\mathcal{A}^{\mathrm{YM}}_{a,L} - D^{\mathrm{univ}}_{a,L}\right).
$$

Existence of $\Gamma_{\mathrm{YM}}$ is the analogue of Euler's existence statement for $\gamma$. Existence alone is insufficient for Yang-Mills.

## 4. The biting requirement

For `gamma`, existence is the entire content. For Yang-Mills, the finite part must additionally have spectral force: it must enforce, or be equivalent to, a positive transfer-Hamiltonian gap.

Weak, incorrect version: `$\gamma$ appears in regularization, therefore Yang-Mills is solved.`

Strong, disciplined version: any Clay-class proof would have to exhibit a $\Gamma_{\mathrm{YM}}$ that is:

1. canonical;
2. regulator-stable;
3. gauge-invariant;
4. reflection-positive;
5. demonstrably tied to uniform exponential clustering of connected gauge-invariant correlations.

## 5. The Finite-Part Boundary Constant Principle

**Principle.** A Yang-Mills mass-gap construction at any scale beyond the fixed-spacing finite-lattice level must:

1. Define a cutoff gauge-invariant object $\mathcal{A}^{\mathrm{YM}}_{a,L}$.
2. Identify a universal divergent part $D^{\mathrm{univ}}_{a,L}$ that is local, gauge-invariant, and regulator-stable.
3. Define the finite part $\Gamma_{\mathrm{YM}} = \operatorname{FP}(\mathcal{A}^{\mathrm{YM}}_{a,L} - D^{\mathrm{univ}}_{a,L})$ and prove that it is canonical, independent of regulator and presentation choices within a specified class.
4. Prove that the existence and structure of $\Gamma_{\mathrm{YM}}$ imply uniform exponential decay of connected gauge-invariant Euclidean correlations:

$$
|\langle O(x)O(0)\rangle_c| \leq C_O e^{-m|x|}, \qquad m>0,
$$

with $m$ independent of $(a,L)$.

5. Use Osterwalder-Schrader / Osterwalder-Seiler reflection positivity to upgrade Euclidean decay to a positive Hamiltonian gap $\Delta_{\mathrm{YM}}\geq m>0$.

Compressed form:

$$
\operatorname{FP}(\text{cutoff YM}) \Rightarrow \text{uniform clustering} \Rightarrow \text{OS reconstruction} \Rightarrow \Delta_{\mathrm{YM}}>0.
$$

This is not a proof. It is a discipline. It identifies the minimal content a proof must carry.

## 6. Candidate Gamma_YM identifications (open)

Each candidate below is a possible concrete realization of $\Gamma_{\mathrm{YM}}$. Each must be tested against the biting requirement.

| Candidate | Source artifact | Biting test |
| --- | --- | --- |
| Renormalized $\log Z$ finite part | v0.14.4 partition-function machinery | Does it bound transfer-matrix spectral-radius separation? |
| Strong-coupling threshold $\beta^* = 0.006296889394074993$ | v0.14.4 | Is $\beta^*$ regulator-stable as $a\to 0$? Almost certainly not, but the renormalized analogue might be. |
| Polymer convergence radius | v0.14.4 / Lane II | Does its existence force uniform clustering? Already used; this is Lane I's actual mechanism. |
| Renormalized string tension $\sigma_R$ | Future Lane IV interface | Is $\sigma_R$ the natural $\Gamma_{\mathrm{YM}}$ at the strong-coupling / weak-coupling boundary? |
| Spectral $\zeta_{\mathrm{YM}}(s)$ residue at relevant pole | Open; needs Lane III development | A first-Stieltjes-constant analogue of a Yang-Mills spectral zeta object is the most literal $\gamma$-analogue. |

Note: the Lane I theorem already uses polymer convergence-radius machinery. What this principle adds is the reframing: the polymer radius is one realization of $\Gamma_{\mathrm{YM}}$ at fixed spacing. The Clay question is whether a renormalized version survives the relevant limits.

## 7. Obstruction translation table (Lane III input)

Each obstruction catalogued in v0.18.1 should be classified by which clause of the Finite-Part Boundary Constant Principle it blocks. This is the proposed organizing axis for the program-context companion of the v0.18.1 split.

| Blocks clause | Obstruction class |
| --- | --- |
| (1) Cutoff object definition | Gauge-fixing ambiguity, Gribov copies, lattice-action choice freedom |
| (2) Universal divergence identification | Non-local counterterm requirements; regulator dependence of $D^{\mathrm{univ}}$ |
| (3) Canonical finite part | Scheme dependence, presentation dependence, non-uniqueness of $\operatorname{FP}$ |
| (4) Uniform clustering | Loss of polymer convergence; topology-blind entropy bounds; volume-dependence of decay rate |
| (5) OS reconstruction | Loss of reflection positivity under limits; sector mixing |

Each v0.18.1 obstruction should receive a classification tag from this table. This makes the obstruction survey legible against a single principle rather than as an undifferentiated list.

## 8. Connection to existing constructive QFT

The finite-part operation is not novel as an operation. It is the operation underlying every constructive QFT program:

- Glimm-Jaffe $\varphi^4_2$ and $\varphi^4_3$ constructions;
- Brydges-Federbush-Battle cluster expansions;
- Balaban's lattice Yang-Mills renormalization-group programs;
- BPHZ renormalization;
- Epstein-Glaser causal renormalization.

What this memorandum adds is not a method. It is a discipline:

1. name the finite part;
2. demand that it be canonical;
3. demand that it bite.

The third demand is the one routinely under-emphasized. Many constructive programs reach existence of a finite limit without reaching the gap, and require additional independent arguments, such as cluster expansions, contour methods, or supersymmetric methods, to obtain spectral consequences. This memorandum identifies the gap-producing property as part of the finite-part design specification, not an addendum.

## 9. Relation to the v0.14.4 scoped claim

The v0.14.4 theorem produces a positive transfer gap in the fixed-spacing `SU(2)` strong-coupling regime. In this regime, the finite-part operation is trivial: there is no divergence to subtract because the cutoff is fixed. The polymer convergence radius and the threshold $\beta^*$ play the role of gap-producing finite-part data.

The Finite-Part Boundary Constant Principle therefore does not apply to v0.14.4 directly. It applies to any future construction that attempts to remove cutoffs while preserving the gap: Lane IV interface work and the Clay-class problem proper.

Stating this explicitly protects the Lane I theorem from continuum-language contamination.

## 10. Open status

Established:

- the `gamma` identities cited above are standard results.

Proposed:

- the three-regime taxonomy;
- the Finite-Part Boundary Constant Principle;
- the obstruction translation table.

Open:

- concrete identification of $\Gamma_{\mathrm{YM}}$;
- whether the spectral $\zeta_{\mathrm{YM}}$ first-Stieltjes-constant route is viable;
- whether the renormalized string tension is the natural $\Gamma_{\mathrm{YM}}$ at the strong-coupling / weak-coupling interface;
- whether any candidate in Section 6 satisfies the biting requirement.

## Appendix A. Irrationality status of gamma

It is unknown whether $\gamma$ is rational, irrational, algebraic, or transcendental. This is referenced only as a reminder that even the prototype constant in Regime 3 is mathematically incomplete. The Yang-Mills finite-part invariant need not be a concrete real number; it may be a structural object, such as a spectral residue, a partition-function germ, or a convergence radius, whose value is theory-determined.

## Appendix B. The plastic constant footnote

The plastic constant $\rho\approx 1.3247$, the real root of $x^3=x+1$, is Regime 1: algebraic. It does not connect to $\gamma$ through any standard deep identity. The two constants are different species and should not be conflated. It is listed here only to prevent that confusion in subsequent program memoranda.
