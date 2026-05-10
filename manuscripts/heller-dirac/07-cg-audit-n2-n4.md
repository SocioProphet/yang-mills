# Heller-Dirac CG audit: finite tables and projector checks

Status: generated audit artifact.  
Scope: finite Clebsch-Gordan sanity checks for the Heller-Dirac sidecar.  
Non-claims: this file does not add physics beyond the manuscript notes; it only fixes exact small-`n` transition data and projector checks.

## 1. Convention

The tables use the Condon-Shortley phase convention as implemented by `sympy.physics.wigner.clebsch_gordan`.

For each principal shell,

```math
j=\frac{n-1}{2},
\qquad
\mathcal H_n=D^{(j)}\otimes D^{(j)},
\qquad
D^{(j)}\otimes D^{(j)}=\bigoplus_{\ell=0}^{2j}D^{(\ell)}.
```

Each listed state is

```math
\lvert \ell,m\rangle
=\sum_{m_+ + m_-=m}
\langle j,m_+;j,m_-\mid \ell,m\rangle
\lvert m_+,m_-\rangle .
```

Signs depend on phase convention; projector and defect-channel checks are invariant under a consistent phase convention.

## 2. Decomposition audit

| `n` | `j` | Product dimension | Spherical decomposition | Dimension check |
|---:|---:|---:|---|---:|
| 2 | `\frac{1}{2}` | 4 | `D^1` ⊕ `D^0` | 3+1=4 |
| 3 | `1` | 9 | `D^2` ⊕ `D^1` ⊕ `D^0` | 5+3+1=9 |
| 4 | `\frac{3}{2}` | 16 | `D^3` ⊕ `D^2` ⊕ `D^1` ⊕ `D^0` | 7+5+3+1=16 |

## 3. Exact Clebsch-Gordan tables

### n=2, j=\frac{1}{2}

| `ell` | `m` | Expansion in product/parabolic cells |
|---:|---:|---|
| 1 | 1 | $\lvert \frac{1}{2},\frac{1}{2}\rangle$ |
| 1 | 0 | $\frac{\sqrt{2}}{2}\lvert - \frac{1}{2},\frac{1}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{1}{2},- \frac{1}{2}\rangle$ |
| 1 | -1 | $\lvert - \frac{1}{2},- \frac{1}{2}\rangle$ |
| 0 | 0 | $-\frac{\sqrt{2}}{2}\lvert - \frac{1}{2},\frac{1}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{1}{2},- \frac{1}{2}\rangle$ |

### n=3, j=1

| `ell` | `m` | Expansion in product/parabolic cells |
|---:|---:|---|
| 2 | 2 | $\lvert 1,1\rangle$ |
| 2 | 1 | $\frac{\sqrt{2}}{2}\lvert 0,1\rangle + \frac{\sqrt{2}}{2}\lvert 1,0\rangle$ |
| 2 | 0 | $\frac{\sqrt{6}}{6}\lvert -1,1\rangle + \frac{\sqrt{6}}{3}\lvert 0,0\rangle + \frac{\sqrt{6}}{6}\lvert 1,-1\rangle$ |
| 2 | -1 | $\frac{\sqrt{2}}{2}\lvert -1,0\rangle + \frac{\sqrt{2}}{2}\lvert 0,-1\rangle$ |
| 2 | -2 | $\lvert -1,-1\rangle$ |
| 1 | 1 | $-\frac{\sqrt{2}}{2}\lvert 0,1\rangle + \frac{\sqrt{2}}{2}\lvert 1,0\rangle$ |
| 1 | 0 | $-\frac{\sqrt{2}}{2}\lvert -1,1\rangle + \frac{\sqrt{2}}{2}\lvert 1,-1\rangle$ |
| 1 | -1 | $-\frac{\sqrt{2}}{2}\lvert -1,0\rangle + \frac{\sqrt{2}}{2}\lvert 0,-1\rangle$ |
| 0 | 0 | $\frac{\sqrt{3}}{3}\lvert -1,1\rangle - \frac{\sqrt{3}}{3}\lvert 0,0\rangle + \frac{\sqrt{3}}{3}\lvert 1,-1\rangle$ |

### n=4, j=\frac{3}{2}

| `ell` | `m` | Expansion in product/parabolic cells |
|---:|---:|---|
| 3 | 3 | $\lvert \frac{3}{2},\frac{3}{2}\rangle$ |
| 3 | 2 | $\frac{\sqrt{2}}{2}\lvert \frac{1}{2},\frac{3}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{3}{2},\frac{1}{2}\rangle$ |
| 3 | 1 | $\frac{\sqrt{5}}{5}\lvert - \frac{1}{2},\frac{3}{2}\rangle + \frac{\sqrt{15}}{5}\lvert \frac{1}{2},\frac{1}{2}\rangle + \frac{\sqrt{5}}{5}\lvert \frac{3}{2},- \frac{1}{2}\rangle$ |
| 3 | 0 | $\frac{\sqrt{5}}{10}\lvert - \frac{3}{2},\frac{3}{2}\rangle + \frac{3 \sqrt{5}}{10}\lvert - \frac{1}{2},\frac{1}{2}\rangle + \frac{3 \sqrt{5}}{10}\lvert \frac{1}{2},- \frac{1}{2}\rangle + \frac{\sqrt{5}}{10}\lvert \frac{3}{2},- \frac{3}{2}\rangle$ |
| 3 | -1 | $\frac{\sqrt{5}}{5}\lvert - \frac{3}{2},\frac{1}{2}\rangle + \frac{\sqrt{15}}{5}\lvert - \frac{1}{2},- \frac{1}{2}\rangle + \frac{\sqrt{5}}{5}\lvert \frac{1}{2},- \frac{3}{2}\rangle$ |
| 3 | -2 | $\frac{\sqrt{2}}{2}\lvert - \frac{3}{2},- \frac{1}{2}\rangle + \frac{\sqrt{2}}{2}\lvert - \frac{1}{2},- \frac{3}{2}\rangle$ |
| 3 | -3 | $\lvert - \frac{3}{2},- \frac{3}{2}\rangle$ |
| 2 | 2 | $-\frac{\sqrt{2}}{2}\lvert \frac{1}{2},\frac{3}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{3}{2},\frac{1}{2}\rangle$ |
| 2 | 1 | $-\frac{\sqrt{2}}{2}\lvert - \frac{1}{2},\frac{3}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{3}{2},- \frac{1}{2}\rangle$ |
| 2 | 0 | $-\frac{1}{2}\lvert - \frac{3}{2},\frac{3}{2}\rangle - \frac{1}{2}\lvert - \frac{1}{2},\frac{1}{2}\rangle + \frac{1}{2}\lvert \frac{1}{2},- \frac{1}{2}\rangle + \frac{1}{2}\lvert \frac{3}{2},- \frac{3}{2}\rangle$ |
| 2 | -1 | $-\frac{\sqrt{2}}{2}\lvert - \frac{3}{2},\frac{1}{2}\rangle + \frac{\sqrt{2}}{2}\lvert \frac{1}{2},- \frac{3}{2}\rangle$ |
| 2 | -2 | $-\frac{\sqrt{2}}{2}\lvert - \frac{3}{2},- \frac{1}{2}\rangle + \frac{\sqrt{2}}{2}\lvert - \frac{1}{2},- \frac{3}{2}\rangle$ |
| 1 | 1 | $\frac{\sqrt{30}}{10}\lvert - \frac{1}{2},\frac{3}{2}\rangle - \frac{\sqrt{10}}{5}\lvert \frac{1}{2},\frac{1}{2}\rangle + \frac{\sqrt{30}}{10}\lvert \frac{3}{2},- \frac{1}{2}\rangle$ |
| 1 | 0 | $\frac{3 \sqrt{5}}{10}\lvert - \frac{3}{2},\frac{3}{2}\rangle - \frac{\sqrt{5}}{10}\lvert - \frac{1}{2},\frac{1}{2}\rangle - \frac{\sqrt{5}}{10}\lvert \frac{1}{2},- \frac{1}{2}\rangle + \frac{3 \sqrt{5}}{10}\lvert \frac{3}{2},- \frac{3}{2}\rangle$ |
| 1 | -1 | $\frac{\sqrt{30}}{10}\lvert - \frac{3}{2},\frac{1}{2}\rangle - \frac{\sqrt{10}}{5}\lvert - \frac{1}{2},- \frac{1}{2}\rangle + \frac{\sqrt{30}}{10}\lvert \frac{1}{2},- \frac{3}{2}\rangle$ |
| 0 | 0 | $-\frac{1}{2}\lvert - \frac{3}{2},\frac{3}{2}\rangle + \frac{1}{2}\lvert - \frac{1}{2},\frac{1}{2}\rangle - \frac{1}{2}\lvert \frac{1}{2},- \frac{1}{2}\rangle + \frac{1}{2}\lvert \frac{3}{2},- \frac{3}{2}\rangle$ |

## 4. Projector audit

For fixed magnetic total `M=m_++m_-`, define the product-cell basis

```math
B_M=\{\lvert m_+,m_-\rangle:m_++m_-=M\}.
```

For every allowed `ell`, the rank-one block projector is

```math
\Pi_{\ell,M}
=\lvert \ell,M\rangle\langle \ell,M\rvert
\quad\text{on }B_M.
```

The audit checks

```math
\sum_{\ell\ge |M|}\Pi_{\ell,M}=I_{B_M},
\qquad
\Pi_{\ell,M}\Pi_{\ell',M}=\delta_{\ell\ell'}\Pi_{\ell,M}.
```

| `n` | Fixed-`M` block sizes | Projector identity | Orthogonality/idempotence |
|---:|---|---|---|
| 2 | `M=-1: 1x1`, `M=0: 2x2`, `M=1: 1x1` | exact zero residual | exact zero residual |
| 3 | `M=-2: 1x1`, `M=-1: 2x2`, `M=0: 3x3`, `M=1: 2x2`, `M=2: 1x1` | exact zero residual | exact zero residual |
| 4 | `M=-3: 1x1`, `M=-2: 2x2`, `M=-1: 3x3`, `M=0: 4x4`, `M=1: 3x3`, `M=2: 2x2`, `M=3: 1x1` | exact zero residual | exact zero residual |

## 5. Defect-matrix test

Let

```math
\widehat\Delta=\sum_{\ell=0}^{n-1}\delta_\ell\Pi_\ell.
```

The defect operator is diagonal in `ell` but generally non-diagonal in product cells. For `n=2`, in the `M=0` product basis

```math
(\lvert -\tfrac12,+\tfrac12\rangle,\lvert +\tfrac12,-\tfrac12\rangle),
```

the exact block is

```math
\widehat\Delta_{M=0}
=\frac12
\begin{pmatrix}
\delta_1+\delta_0 & \delta_1-\delta_0\\
\delta_1-\delta_0 & \delta_1+\delta_0
\end{pmatrix}.
```

This is the finite proof of the manuscript rule:

```text
defects are simple in the spherical ell basis;
defects are structured kernels in the product-cell basis.
```

## 6. Reproducibility

The companion script `scripts/heller_dirac_cg_audit.py` regenerates these tables and verifies the projector identities exactly using SymPy.

Expected command:

```bash
python scripts/heller_dirac_cg_audit.py --n 2 3 4
```

Expected result: all projector residuals and orthogonality/idempotence residuals are exactly zero.
