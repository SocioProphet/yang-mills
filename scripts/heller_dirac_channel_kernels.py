#!/usr/bin/env python3
"""Symbolic channel-kernel matrices for the Heller-Dirac sidecar.

This script computes the product-cell matrix form of

    Delta = sum_ell delta_ell Pi_ell

on each fixed-M block of D^j tensor D^j. It complements
`scripts/heller_dirac_cg_audit.py`: the CG audit verifies projectors; this
script uses those projectors to display the channel kernel in the product-cell
basis.

Dependency:
    sympy

Example:
    python scripts/heller_dirac_channel_kernels.py --n 3 4
"""

from __future__ import annotations

import argparse
from typing import Iterable

import sympy as sp
from sympy.physics.wigner import clebsch_gordan


def m_values(j: sp.Rational) -> list[sp.Rational]:
    """Return m=-j,-j+1,...,+j as exact rationals."""
    two_j = int(2 * j)
    return [sp.Rational(k, 2) for k in range(-two_j, two_j + 1, 2)]


def product_basis_for_M(j: sp.Rational, M: sp.Rational) -> list[tuple[sp.Rational, sp.Rational]]:
    """Product-cell basis vectors |m_+,m_-> at fixed M=m_+ + m_-."""
    values = set(m_values(j))
    return [(m_plus, M - m_plus) for m_plus in m_values(j) if M - m_plus in values]


def cg(j: sp.Rational, m_plus: sp.Rational, m_minus: sp.Rational, ell: int, M: sp.Rational) -> sp.Expr:
    """Exact Clebsch-Gordan coefficient <j,m+;j,m-|ell,M>."""
    return sp.simplify(clebsch_gordan(j, j, ell, m_plus, m_minus, M))


def projector_block(j: sp.Rational, ell: int, M: sp.Rational) -> sp.Matrix:
    """Rank-one block projector Pi_{ell,M} on the fixed-M product-cell basis."""
    basis = product_basis_for_M(j, M)
    coeffs = [cg(j, m_plus, m_minus, ell, M) for m_plus, m_minus in basis]
    vector = sp.Matrix(coeffs)
    return sp.simplify(vector * vector.T)


def delta_symbols(max_ell: int) -> tuple[sp.Symbol, ...]:
    return tuple(sp.symbols(f"delta_{ell}") for ell in range(max_ell + 1))


def channel_kernel_block(n: int, M: sp.Rational) -> tuple[list[tuple[sp.Rational, sp.Rational]], sp.Matrix]:
    """Return basis and symbolic Delta block for a principal shell n and total M."""
    j = sp.Rational(n - 1, 2)
    max_ell = int(2 * j)
    basis = product_basis_for_M(j, M)
    deltas = delta_symbols(max_ell)
    matrix = sp.zeros(len(basis), len(basis))
    for ell in range(max_ell + 1):
        if abs(M) <= ell:
            matrix += deltas[ell] * projector_block(j, ell, M)
    return basis, sp.simplify(matrix)


def verify_coulomb_limit(n_values: Iterable[int]) -> bool:
    """Check that equal channel shifts collapse each block to a scalar matrix."""
    ok = True
    for n in n_values:
        j = sp.Rational(n - 1, 2)
        max_ell = int(2 * j)
        subs = {sp.symbols(f"delta_{ell}"): sp.Symbol("delta") for ell in range(max_ell + 1)}
        for M_int in range(-max_ell, max_ell + 1):
            M = sp.Rational(M_int, 1)
            basis, block = channel_kernel_block(n, M)
            residual = sp.simplify(block.subs(subs) - sp.Symbol("delta") * sp.eye(len(basis)))
            block_ok = residual == sp.zeros(len(basis), len(basis))
            ok = ok and block_ok
            status = "OK" if block_ok else "FAIL"
            print(f"n={n}, M={M}: Coulomb-limit scalar collapse {status}")
    return ok


def print_blocks(n_values: Iterable[int]) -> None:
    for n in n_values:
        j = sp.Rational(n - 1, 2)
        max_ell = int(2 * j)
        print(f"\n## n={n}, j={sp.latex(j)}")
        for M_int in range(-max_ell, max_ell + 1):
            M = sp.Rational(M_int, 1)
            basis, block = channel_kernel_block(n, M)
            print(f"\nM={M}; basis={basis}")
            print(sp.latex(block))


def main() -> int:
    parser = argparse.ArgumentParser(description="Compute Heller-Dirac fixed-M channel-kernel blocks.")
    parser.add_argument("--n", nargs="+", type=int, default=[3, 4], help="Principal shell values to audit.")
    parser.add_argument("--print-blocks", action="store_true", help="Print LaTeX matrices for the requested blocks.")
    args = parser.parse_args()

    if args.print_blocks:
        print_blocks(args.n)

    ok = verify_coulomb_limit(args.n)
    if ok:
        print("\nRESULT: channel-kernel Coulomb-limit audit passed.")
        return 0

    print("\nRESULT: channel-kernel Coulomb-limit audit failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
