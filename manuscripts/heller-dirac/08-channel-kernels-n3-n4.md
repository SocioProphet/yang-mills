# Heller-Dirac channel kernels: symbolic product-cell matrices for n=3,4

Status: generated audit artifact.  
Scope: symbolic channel-kernel matrices for the Heller-Dirac sidecar.  
Non-claims: this file adds no new physical claim; it records the exact finite matrix form of an already-defined channel operator.

## 1. Purpose

The b0 note defines the channel operator

```math
\widehat\Delta=\sum_{\ell=0}^{n-1}\delta_\ell\Pi_\ell,
```

where `\Pi_\ell` is the projector onto the spherical `D^(ell)` channel. This operator is diagonal in the spherical basis, but generally non-diagonal in the product/parabolic cell basis.

This audit records the fixed-`M` product-cell blocks for `n=3` and `n=4`, where

```math
M=m_+ + m_-.
```

Only independent nonnegative `M` blocks are listed. The corresponding negative-`M` blocks have the same matrix form after the obvious basis reversal/sign-convention adjustment.

## 2. Conventions

For a principal shell `n`, set

```math
j=\frac{n-1}{2},
\qquad
\mathcal H_n=D^{(j)}\otimes D^{(j)}.
```

At fixed `M`, use the ordered product-cell basis

```math
B_M=\{\lvert m_+,m_-\rangle:m_++m_-=M\},
```

ordered by increasing `m_+`.

The fixed-`M` block is

```math
\Delta_M=\sum_{\ell\ge |M|}\delta_\ell\Pi_{\ell,M}.
```

## 3. n=3 channel kernels

Here `j=1` and `ell=0,1,2`.

### M=2

Basis:

```math
B_2=(\lvert 1,1\rangle).
```

```math
\Delta_2=
\begin{pmatrix}
\delta_2
\end{pmatrix}.
```

### M=1

Basis:

```math
B_1=(\lvert 0,1\rangle,\lvert 1,0\rangle).
```

```math
\Delta_1=
\begin{pmatrix}
\frac{\delta_1+\delta_2}{2} & \frac{-\delta_1+\delta_2}{2}\\
\frac{-\delta_1+\delta_2}{2} & \frac{\delta_1+\delta_2}{2}
\end{pmatrix}.
```

### M=0

Basis:

```math
B_0=(\lvert -1,1\rangle,\lvert 0,0\rangle,\lvert 1,-1\rangle).
```

```math
\Delta_0=
\begin{pmatrix}
\frac{\delta_0}{3}+\frac{\delta_1}{2}+\frac{\delta_2}{6}
& -\frac{\delta_0}{3}+\frac{\delta_2}{3}
& \frac{\delta_0}{3}-\frac{\delta_1}{2}+\frac{\delta_2}{6}\\
-\frac{\delta_0}{3}+\frac{\delta_2}{3}
& \frac{\delta_0}{3}+\frac{2\delta_2}{3}
& -\frac{\delta_0}{3}+\frac{\delta_2}{3}\\
\frac{\delta_0}{3}-\frac{\delta_1}{2}+\frac{\delta_2}{6}
& -\frac{\delta_0}{3}+\frac{\delta_2}{3}
& \frac{\delta_0}{3}+\frac{\delta_1}{2}+\frac{\delta_2}{6}
\end{pmatrix}.
```

## 4. n=4 channel kernels

Here `j=3/2` and `ell=0,1,2,3`.

### M=3

Basis:

```math
B_3=(\lvert \tfrac32,\tfrac32\rangle).
```

```math
\Delta_3=
\begin{pmatrix}
\delta_3
\end{pmatrix}.
```

### M=2

Basis:

```math
B_2=(\lvert \tfrac12,\tfrac32\rangle,\lvert \tfrac32,\tfrac12\rangle).
```

```math
\Delta_2=
\begin{pmatrix}
\frac{\delta_2+\delta_3}{2} & \frac{-\delta_2+\delta_3}{2}\\
\frac{-\delta_2+\delta_3}{2} & \frac{\delta_2+\delta_3}{2}
\end{pmatrix}.
```

### M=1

Basis:

```math
B_1=(\lvert -\tfrac12,\tfrac32\rangle,\lvert \tfrac12,\tfrac12\rangle,\lvert \tfrac32,-\tfrac12\rangle).
```

```math
\Delta_1=
\begin{pmatrix}
\frac{3\delta_1}{10}+\frac{\delta_2}{2}+\frac{\delta_3}{5}
& \frac{\sqrt3(-\delta_1+\delta_3)}{5}
& \frac{3\delta_1}{10}-\frac{\delta_2}{2}+\frac{\delta_3}{5}\\
\frac{\sqrt3(-\delta_1+\delta_3)}{5}
& \frac{2\delta_1}{5}+\frac{3\delta_3}{5}
& \frac{\sqrt3(-\delta_1+\delta_3)}{5}\\
\frac{3\delta_1}{10}-\frac{\delta_2}{2}+\frac{\delta_3}{5}
& \frac{\sqrt3(-\delta_1+\delta_3)}{5}
& \frac{3\delta_1}{10}+\frac{\delta_2}{2}+\frac{\delta_3}{5}
\end{pmatrix}.
```

### M=0

Basis:

```math
B_0=(\lvert -\tfrac32,\tfrac32\rangle,\lvert -\tfrac12,\tfrac12\rangle,\lvert \tfrac12,-\tfrac12\rangle,\lvert \tfrac32,-\tfrac32\rangle).
```

```math
\Delta_0=
\begin{pmatrix}
\frac{\delta_0}{4}+\frac{9\delta_1}{20}+\frac{\delta_2}{4}+\frac{\delta_3}{20}
& -\frac{\delta_0}{4}-\frac{3\delta_1}{20}+\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& \frac{\delta_0}{4}-\frac{3\delta_1}{20}-\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& -\frac{\delta_0}{4}+\frac{9\delta_1}{20}-\frac{\delta_2}{4}+\frac{\delta_3}{20}\\
-\frac{\delta_0}{4}-\frac{3\delta_1}{20}+\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& \frac{\delta_0}{4}+\frac{\delta_1}{20}+\frac{\delta_2}{4}+\frac{9\delta_3}{20}
& -\frac{\delta_0}{4}+\frac{\delta_1}{20}-\frac{\delta_2}{4}+\frac{9\delta_3}{20}
& \frac{\delta_0}{4}-\frac{3\delta_1}{20}-\frac{\delta_2}{4}+\frac{3\delta_3}{20}\\
\frac{\delta_0}{4}-\frac{3\delta_1}{20}-\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& -\frac{\delta_0}{4}+\frac{\delta_1}{20}-\frac{\delta_2}{4}+\frac{9\delta_3}{20}
& \frac{\delta_0}{4}+\frac{\delta_1}{20}+\frac{\delta_2}{4}+\frac{9\delta_3}{20}
& -\frac{\delta_0}{4}-\frac{3\delta_1}{20}+\frac{\delta_2}{4}+\frac{3\delta_3}{20}\\
-\frac{\delta_0}{4}+\frac{9\delta_1}{20}-\frac{\delta_2}{4}+\frac{\delta_3}{20}
& \frac{\delta_0}{4}-\frac{3\delta_1}{20}-\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& -\frac{\delta_0}{4}-\frac{3\delta_1}{20}+\frac{\delta_2}{4}+\frac{3\delta_3}{20}
& \frac{\delta_0}{4}+\frac{9\delta_1}{20}+\frac{\delta_2}{4}+\frac{\delta_3}{20}
\end{pmatrix}.
```

## 5. Coulomb-limit scalar collapse

If all channel shifts are equal,

```math
\delta_0=\delta_1=\cdots=\delta_{n-1}=\delta,
```

then every fixed-`M` block collapses to

```math
\Delta_M=\delta I_{B_M}.
```

This is the finite symbolic version of the degeneracy-restoration check: channel splitting disappears when all channel shifts are equal.

## 6. Reproducibility

The companion script `scripts/heller_dirac_channel_kernels.py` computes these blocks from the Clebsch-Gordan projectors and verifies the Coulomb-limit scalar collapse.

Expected command:

```bash
python scripts/heller_dirac_channel_kernels.py --n 3 4
```

Expected result:

```text
RESULT: channel-kernel Coulomb-limit audit passed.
```
