#!/usr/bin/env python3
"""Ingest the 2026-05-09 Yang-Mills normalized capture bundle.

This script is intentionally conservative:
- verifies the normalized bundle SHA-256 before writing;
- expands UTF-8 repo content into its intended paths;
- skips reconstructed PDFs because they are distribution artifacts that should move through
  Git LFS, release assets, or the program artifact bucket;
- refuses path traversal and absolute-path entries.

Usage from repo root:

    python3 scripts/ingest_yang_mills_capture_2026_05_09.py /path/to/yang-mills-capture-normalized-2026-05-09.zip

The script is idempotent for identical content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import zipfile

EXPECTED_ZIP_SHA256 = "4fd1895ed5b603863a40f00f0697e493fa0455e2f13a88cca60a6605938a29a0"
EXPECTED_PREFIX = "yang_mills_capture_bundle_2026_05_09/"

SKIP_SUFFIXES = {".pdf"}
SKIP_PATHS = {
    "CAPTURE_README.md",  # preserved in docs/capture-bundles/2026-05-09/source-bundle-readme.md
    "docs/capture-bundles/2026-05-09/README.md",
    "docs/capture-bundles/2026-05-09/ingest-report.md",
    "docs/capture-bundles/2026-05-09/source-bundle-readme.md",
}


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_repo_path(rel: str) -> pathlib.Path:
    p = pathlib.PurePosixPath(rel)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError(f"unsafe archive path: {rel!r}")
    return pathlib.Path(*p.parts)


def classify(path: str) -> str:
    suffix = pathlib.PurePosixPath(path).suffix.lower()
    if suffix == ".pdf":
        return "distribution-pdf"
    if suffix == ".py":
        return "script"
    if suffix == ".json":
        return "json"
    if suffix == ".txt":
        if "_recovered-sources/" in path:
            return "text-extract"
        return "verification-output"
    if suffix == ".md":
        return "markdown"
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("bundle", type=pathlib.Path)
    parser.add_argument("--repo-root", type=pathlib.Path, default=pathlib.Path.cwd())
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    bundle = args.bundle.resolve()
    repo_root = args.repo_root.resolve()

    observed = sha256_file(bundle)
    if observed != EXPECTED_ZIP_SHA256:
        print(f"ERROR: normalized bundle SHA mismatch", file=sys.stderr)
        print(f"expected: {EXPECTED_ZIP_SHA256}", file=sys.stderr)
        print(f"observed: {observed}", file=sys.stderr)
        return 2

    written = []
    skipped = []

    with zipfile.ZipFile(bundle) as zf:
        for info in sorted(zf.infolist(), key=lambda item: item.filename):
            if info.is_dir():
                continue
            name = info.filename
            if not name.startswith(EXPECTED_PREFIX):
                raise ValueError(f"unexpected archive prefix: {name!r}")
            rel = name[len(EXPECTED_PREFIX):]
            if not rel:
                continue

            artifact_class = classify(rel)
            if rel in SKIP_PATHS or pathlib.PurePosixPath(rel).suffix.lower() in SKIP_SUFFIXES:
                skipped.append({"path": rel, "class": artifact_class, "bytes": info.file_size})
                continue

            out_path = repo_root / safe_repo_path(rel)
            data = zf.read(info)

            # This capture should only write UTF-8 files. Decode first to fail before partial writes.
            try:
                data.decode("utf-8")
            except UnicodeDecodeError as exc:
                raise UnicodeDecodeError(exc.encoding, exc.object, exc.start, exc.end, f"non-UTF-8 repo content: {rel}")

            if args.dry_run:
                written.append({"path": rel, "class": artifact_class, "bytes": info.file_size, "dry_run": True})
                continue

            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(data)
            written.append({"path": rel, "class": artifact_class, "bytes": info.file_size})

    report = {
        "bundle": str(bundle),
        "repo_root": str(repo_root),
        "bundle_sha256": observed,
        "written_count": len(written),
        "skipped_count": len(skipped),
        "written": written,
        "skipped": skipped,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
