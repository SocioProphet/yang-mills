#!/usr/bin/env python3
"""Validate that files with .pdf extension are real PDF byte streams.

The current archive includes several files named .pdf that are actually ZIP
page/text bundles. This script prevents those artifacts from being mistaken for
journal-ready PDFs or passed into PDF tooling that expects a %PDF header.

Usage:
    python scripts/check_pdf_headers.py path/to/file.pdf path/to/tree

Exit codes:
    0 - all checked .pdf files have %PDF headers
    1 - one or more .pdf files are missing or malformed
"""

from __future__ import annotations

import argparse
import pathlib
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class PdfHeaderResult:
    path: pathlib.Path
    ok: bool
    header: bytes
    reason: str


def iter_pdf_paths(inputs: list[pathlib.Path]) -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for item in inputs:
        if item.is_dir():
            paths.extend(sorted(p for p in item.rglob("*.pdf") if p.is_file()))
        elif item.is_file() and item.suffix.lower() == ".pdf":
            paths.append(item)
        elif item.exists():
            continue
        else:
            paths.append(item)
    return paths


def check_pdf_header(path: pathlib.Path) -> PdfHeaderResult:
    if not path.exists():
        return PdfHeaderResult(path=path, ok=False, header=b"", reason="missing file")
    if not path.is_file():
        return PdfHeaderResult(path=path, ok=False, header=b"", reason="not a regular file")
    try:
        with path.open("rb") as handle:
            header = handle.read(5)
    except OSError as exc:
        return PdfHeaderResult(path=path, ok=False, header=b"", reason=f"read error: {exc}")

    if header == b"%PDF-":
        return PdfHeaderResult(path=path, ok=True, header=header, reason="ok")
    if header.startswith(b"PK"):
        return PdfHeaderResult(path=path, ok=False, header=header, reason="ZIP payload with .pdf extension")
    return PdfHeaderResult(path=path, ok=False, header=header, reason="missing %PDF header")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=pathlib.Path, help="PDF files or directories to scan")
    args = parser.parse_args(argv)

    pdf_paths = iter_pdf_paths(args.paths)
    if not pdf_paths:
        print("No .pdf files found.")
        return 0

    failures: list[PdfHeaderResult] = []
    for path in pdf_paths:
        result = check_pdf_header(path)
        status = "OK" if result.ok else "FAIL"
        header_display = result.header.hex() if result.header else "<none>"
        print(f"{status}\t{path}\t{result.reason}\theader={header_display}")
        if not result.ok:
            failures.append(result)

    if failures:
        print(f"\n{len(failures)} malformed .pdf file(s) detected.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
