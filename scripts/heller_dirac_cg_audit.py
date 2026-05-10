#!/usr/bin/env python3
"""Finite Clebsch-Gordan audit for the Heller-Dirac sidecar.

This script regenerates the small-n tables used by
`manuscripts/heller-dirac/07-cg-audit-n2-n4.md` and verifies the projector
identities exactly.

Dependency:
    sympy

Example:
    python scripts/heller_dirac_cg_audit.py --n 2 3 4
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


def state_terms(n: int, ell: int, M: int) -> list[tuple[sp.Expr, sp.Rational, sp.Rational]]:
    """Nonzero product-cell expansion terms for |ell,M>."""
    j = sp.Rational(n - 1, 2)
    terms: list[tuple[sp.Expr, sp.Rational, sp.Rational]] = []
    for m_plus, m_minus in product_basis_for_M(j, sp.Rational(M, 1)):
        coeff = cg(j, m_plus, m_minus, ell, sp.Rational(M, 1))
        if coeff != 0:
            terms.append((coeff, m_plus, m_minus))
    return terms


def projector_block(j: sp.Rational, ell: int, M: sp.Rational) -> sp.Matrix:
    """Rank-one block projector Pi_{ell,M} on the fixed-M product-cell basis."""
    basis = product_basis_for_M(j, M)
    coeffs = [cg(j, m_plus, m_minus, ell, M) for m_plus, m_minus in basis]
    vector = sp.Matrix(coeffs)
    return sp.simplify(vector * vector.T)


def allowed_M_values(j: sp.Rational) -> list[sp.Rational]:
    """M values for D^j tensor D^j."""
    return [sp.Rational(k, 1) for k in range(-int(2 * j), int(2 * j) + 1)]


def verify_projectors(n_values: Iterable[int]) -> bool:
    """Verify completeness, idempotence, and orthogonality for each n."""
    all_ok = True
    for n in n_values:
        j = sp.Rational(n - 1, 2)
        print(f"\n## n={n}, j={sp.latex(j)}")
        for M in allowed_M_values(j):
            basis = product_basis_for_M(j, M)
            if not basis:
                continue

            ells = [ell for ell in range(0, int(2 * j) + 1) if abs(M) <= ell]
            projectors = [(ell, projector_block(j, ell, M)) for ell in ells]

            identity = sp.eye(len(basis))
            projector_sum = sum((P for _, P in projectors), sp.zeros(len(basis), len(basis)))
            completeness_residual = sp.simplify(projector_sum - identity)
            completeness_ok = completeness_residual == sp.zeros(len(basis), len(basis))

            product_ok = True
            for ell, P in projectors:
                for ell2, Q in projectors:
                    expected = P if ell == ell2 else sp.zeros(len(basis), len(basis))
                    residual = sp.simplify(P * Q - expected)
                    if residual != sp.zeros(len(basis), len(basis)):
                        product_ok = False

            all_ok = all_ok and completeness_ok and product_ok
            status = "OK" if completeness_ok and product_ok else "FAIL"
            print(f"M={M}: block={len(basis)}x{len(basis)}, ell={ells}, {status}")

    return all_ok


def latex_ket(m_plus: sp.Rational, m_minus: sp.Rational) -> str:
    return rf"\lvert {sp.latex(m_plus)},{sp.latex(m_minus)}\rangle"


def latex_term(coeff: sp.Expr, m_plus: sp.Rational, m_minus: sp.Rational, first: bool) -> str:
    """Format a signed term for Markdown math output."""
    coeff = sp.simplify(coeff)
    if coeff == 1:
        body = latex_ket(m_plus, m_minus)
        return body if first else f" + {body}"
    if coeff == -1:
        body = latex_ket(m_plus, m_minus)
        return f"-{body}" if first else f" - {body}"

    negative = coeff.could_extract_minus_sign()
    abs_coeff = -coeff if negative else coeff
    body = f"{sp.latex(abs_coeff)}{latex_ket(m_plus, m_minus)}"
    if first:
        return f"-{body}" if negative else body
    return f" - {body}" if negative else f" + {body}"


def expansion_latex(n: int, ell: int, M: int) -> str:
    terms = state_terms(n, ell, M)
    return "".join(latex_term(coeff, m_plus, m_minus, index == 0) for index, (coeff, m_plus, m_minus) in enumerate(terms))


def print_tables(n_values: Iterable[int]) -> None:
    for n in n_values:
        j = sp.Rational(n - 1, 2)
        print(f"\n# n={n}, j={sp.latex(j)}")
        for ell in range(int(2 * j), -1, -1):
            for M in range(ell, -ell - 1, -1):
                print(rf"|{ell},{M}> = {expansion_latex(n, ell, M)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run finite Heller-Dirac Clebsch-Gordan audits.")
    parser.add_argument("--n", nargs="+", type=int, default=[2, 3, 4], help="Principal shell values to audit.")
    parser.add_argument("--tables", action="store_true", help="Print exact CG expansion tables.")
    args = parser.parse_args()

    if args.tables:
        print_tables(args.n)

    ok = verify_projectors(args.n)
    if ok:
        print("\nRESULT: exact projector audit passed.")
        return 0

    print("\nRESULT: projector audit failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
