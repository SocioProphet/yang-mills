# Stochastic Yang-Mills Literature Delta - 2026 Pass

Status: literature-positioning note for v0.18.1 Section 6 hardening.

## Question

Does the v0.18.1 stochastic-quantization obstruction language need to change for a 2026 submission pass?

## Finding

Yes, slightly. The d = 4 criticality-wall language should remain, but Section 6.2 should acknowledge the 2026 uniqueness result for gauge-covariant renormalisation in stochastic 3D Yang-Mills-Higgs. This result strengthens the 3D state-space/renormalised-dynamics story. It does not move the four-dimensional Clay wall by itself.

The correct update is not: `stochastic quantization now reaches 4D Yang-Mills`.

The correct update is: `the subcritical 2D/3D stochastic-quantization program continues to mature, including 2026 uniqueness of the gauge-covariant 3D renormalisation; no 4D continuum Yang-Mills mass-gap construction is claimed here or found in this pass.`

## Sources to incorporate

### 2D Yang-Mills heat flow

Chandra, Chevyrev, Hairer, and Shen construct a natural state space and Markov process for the stochastic Yang-Mills heat flow in two dimensions. This supports v0.18.1's claim that the robust result in d = 2 is a state-space/Markov-process construction rather than a Clay-level four-dimensional construction.

Reference seed:

```bibtex
@article{ChandraChevyrevHairerShen2022Langevin2DYM,
  author  = {Chandra, Ajay and Chevyrev, Ilya and Hairer, Martin and Shen, Hao},
  title   = {Langevin dynamic for the 2D Yang-Mills measure},
  journal = {Publications mathematiques de l'IHES},
  volume  = {136},
  pages   = {1--147},
  year    = {2022},
  doi     = {10.1007/s10240-022-00132-0}
}
```

### 3D Yang-Mills-Higgs stochastic quantisation

Chandra, Chevyrev, Hairer, and Shen construct a nonlinear metric state space of distributions for Yang-Mills-Higgs in three dimensions, extend gauge equivalence to that state space, and define a canonical Markov process on the quotient space of gauge orbits up to possible finite-time blow-up. This supports the v0.18.1 quotient-state-space framing.

Reference seed:

```bibtex
@article{ChandraChevyrevHairerShen2024YMH3D,
  author  = {Chandra, Ajay and Chevyrev, Ilya and Hairer, Martin and Shen, Hao},
  title   = {Stochastic quantisation of Yang-Mills-Higgs in 3D},
  journal = {Inventiones mathematicae},
  volume  = {237},
  pages   = {541--696},
  year    = {2024},
  doi     = {10.1007/s00222-024-01264-2}
}
```

### 2026 uniqueness of gauge-covariant renormalisation

Chevyrev and Shen prove uniqueness of the mass renormalisation that yields gauge-covariant local solutions for stochastic 3D Yang-Mills-Higgs. This is the important post-v0.18.1 hardening update: it strengthens the 3D renormalisation story and should be added to Section 6.2.

Reference seed:

```bibtex
@article{ChevyrevShen2026GaugeCovariantRenormalisation3D,
  author  = {Chevyrev, Ilya and Shen, Hao},
  title   = {Uniqueness of Gauge Covariant Renormalisation of Stochastic 3D Yang-Mills-Higgs},
  journal = {Archive for Rational Mechanics and Analysis},
  volume  = {250},
  number  = {11},
  year    = {2026},
  doi     = {10.1007/s00205-025-02163-3}
}
```

### Chevyrev survey/review seed

Chevyrev's stochastic-quantisation survey remains useful for orienting readers around the 2D/3D constructions, quotient state spaces, gauge covariance, and open problems.

Reference seed:

```bibtex
@misc{Chevyrev2022StochasticYM,
  author       = {Chevyrev, Ilya},
  title        = {Stochastic quantisation of Yang-Mills},
  year         = {2022},
  eprint       = {2202.13359},
  archivePrefix= {arXiv},
  primaryClass = {math.PR}
}
```

## Suggested replacement for v0.18.1 Section 6.2

> In two dimensions, Chandra, Chevyrev, Hairer, and Shen construct a natural state space and Markov process for stochastic Yang-Mills heat flow. In three dimensions, related work constructs a nonlinear metric state space of distributions for Yang-Mills-Higgs, extends gauge equivalence to that state space, and defines a canonical Markov process on the quotient space of gauge orbits up to possible finite-time blow-up. A 2026 uniqueness result of Chevyrev and Shen further identifies the gauge-covariant mass renormalisation in the 3D Yang-Mills-Higgs setting. These results strengthen the quotient-state-space and gauge-covariant renormalised-dynamics side of the obstruction taxonomy, but they do not settle the three-dimensional pure Yang-Mills measure problem and do not provide a four-dimensional Clay construction.

## Suggested replacement for v0.18.1 Section 6.3

> The four-dimensional case, the dimension of the Clay problem, remains outside the constructive reach certified by the 2D/3D stochastic-quantisation results cited above. The obstruction should be stated as a present-method wall rather than an impossibility theorem: current regularity-structures and related stochastic-quantisation machinery succeeds in subcritical settings and has not, in the sources checked for this pass, produced a four-dimensional continuum Yang-Mills construction with a mass gap. The obstruction is therefore not that stochastic quantisation fails in principle, but that the presently successful state-space, quotient, and gauge-covariant renormalisation machinery has not yet crossed the d = 4 wall needed for Clay.

## Claim discipline

Do not write:

- `regularity structures cannot handle d = 4 Yang-Mills`;
- `stochastic quantisation has failed`;
- `the d = 4 wall is mathematically insurmountable`;
- `the 2026 3D uniqueness result proves a mass gap`.

Write instead:

- `the current cited constructions are 2D/3D constructions`;
- `the 2026 result strengthens gauge-covariant renormalisation uniqueness in 3D Yang-Mills-Higgs`;
- `no four-dimensional Clay-level construction is claimed in this survey`;
- `d = 4 remains a current-method obstruction in this literature pass`.

## Backlog impact

- Update v0.18.1 Section 6.2 with the 2026 uniqueness result.
- Soften Section 6.3 from `not addressed by existing techniques` to `not addressed by the 2D/3D constructions and searched 2026 literature pass`.
- Add the 2026 ARMA citation to the bibliography.
- Add a small note that the wall is methodological/current-literature, not a no-go theorem.
