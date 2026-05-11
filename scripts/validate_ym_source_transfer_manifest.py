#!/usr/bin/env python3
"""Validate the Yang-Mills source-transfer manifest.

This validator checks the source-transfer contract for Move 4 / Move 1 / Move 2.
It does not require the PDF payload to be committed to the repository. The
payload is identified by source ZIP SHA-256 and per-file SHA-256s; the repo
records the role mapping and claim boundary.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_JSON = ROOT / "data" / "yang_mills_frontier" / "ym_source_transfer_manifest.json"
MANIFEST_MD = ROOT / "docs" / "source-manifests" / "YM_SOURCE_MANIFEST.md"
OUT = ROOT / "reports" / "yang_mills_frontier"

EXPECTED_FILES = {
    "strong_coupling_lattice_mass_gap_seed_v0_14_4.pdf",
    "ym_obstruction_survey_v0_18_1.pdf",
    "heller_yang_mills_temporal_mechanics_whitepaper_v0_9_20_complete_integrated_full_program_paper_expanded.pdf",
    "heller_yang_mills_temporal_mechanics_whitepaper_v0_9_27_full_running_copy_wigner_gate.pdf",
    "heller_yang_mills_temporal_mechanics_whitepaper_v0_9_28_full_running_copy_strategy_alignment.pdf",
    "lane_vii_consolidation_v2_0_1.pdf",
    "YM_SOURCE_MANIFEST.md",
}

EXPECTED_ROLE_KEYS = {"move_4", "move_1", "move_2", "lane_vii_boundary", "manifest"}
EXPECTED_ZIP_SHA = "e9b6a26391b17858377362a15593e6a44c15fe004a91401c18bb034314e628a1"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_json(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def event(gate: str, input_payload: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_type": "ym_source_transfer_manifest_event",
        "gate": gate,
        "input_digest": "sha256:" + sha256_json({"gate": gate, "input": input_payload}),
        "output_digest": "sha256:" + sha256_json({"gate": gate, "result": result}),
        "result": result,
    }


def main() -> int:
    manifest = json.loads(MANIFEST_JSON.read_text(encoding="utf-8"))
    md_text = MANIFEST_MD.read_text(encoding="utf-8")
    files = manifest.get("files", [])
    file_paths = {item["path"] for item in files}
    roles = manifest.get("load_bearing_roles", {})

    events: list[dict[str, Any]] = []

    events.append(event("ym-transfer-zip-identity", {
        "source_upload": manifest.get("source_upload", {}),
    }, {
        "pass": manifest.get("source_upload", {}).get("sha256") == EXPECTED_ZIP_SHA,
        "sha256": manifest.get("source_upload", {}).get("sha256"),
        "size_bytes": manifest.get("source_upload", {}).get("size_bytes"),
        "file_count": manifest.get("source_upload", {}).get("file_count"),
    }))

    missing_files = sorted(EXPECTED_FILES - file_paths)
    extra_files = sorted(file_paths - EXPECTED_FILES)
    events.append(event("ym-transfer-file-set", {
        "expected_files": sorted(EXPECTED_FILES),
        "observed_files": sorted(file_paths),
    }, {
        "pass": not missing_files and not extra_files and len(files) == 7,
        "missing_files": missing_files,
        "extra_files": extra_files,
        "count": len(files),
    }))

    bad_hashes = [item for item in files if len(item.get("sha256", "")) != 64]
    bad_sizes = [item for item in files if item.get("size_bytes", 0) <= 0]
    events.append(event("ym-transfer-file-hashes-and-sizes", {
        "files": files,
    }, {
        "pass": not bad_hashes and not bad_sizes,
        "bad_hash_count": len(bad_hashes),
        "bad_size_count": len(bad_sizes),
    }))

    missing_roles = sorted(EXPECTED_ROLE_KEYS - set(roles))
    role_paths = {path for paths in roles.values() for path in paths}
    unresolved_role_paths = sorted(role_paths - file_paths)
    events.append(event("ym-transfer-role-mapping", {
        "roles": roles,
        "file_paths": sorted(file_paths),
    }, {
        "pass": not missing_roles and not unresolved_role_paths,
        "missing_roles": missing_roles,
        "unresolved_role_paths": unresolved_role_paths,
    }))

    boundaries = "\n".join(manifest.get("claim_boundary", [])) + "\n" + md_text
    required_boundary_terms = [
        "does not claim any new Yang-Mills theorem",
        "does not claim continuum construction",
        "does not move the v0.14.4 fixed-spacing strong-coupling wall",
        "does not close G1/G2 Wigner gates",
    ]
    missing_boundary_terms = [term for term in required_boundary_terms if term.lower() not in boundaries.lower()]
    events.append(event("ym-transfer-nonclaim-boundary", {
        "required_boundary_terms": required_boundary_terms,
        "manifest_json_sha256": sha256_file(MANIFEST_JSON),
        "manifest_md_sha256": sha256_file(MANIFEST_MD),
    }, {
        "pass": not missing_boundary_terms,
        "missing_boundary_terms": missing_boundary_terms,
    }))

    md_required = ["Move 4", "Move 1", "Move 2", "Lane VII", "17 files unaccounted for"]
    missing_md_terms = [term for term in md_required if term not in md_text]
    events.append(event("ym-transfer-human-manifest-coverage", {
        "required_terms": md_required,
        "manifest_md_sha256": sha256_file(MANIFEST_MD),
    }, {
        "pass": not missing_md_terms,
        "missing_terms": missing_md_terms,
    }))

    failed = [item for item in events if not item["result"].get("pass")]
    input_digests = {item["input_digest"] for item in events}
    output_digests = {item["output_digest"] for item in events}

    summary = {
        "state": "Yang-Mills source-transfer manifest validation",
        "event_count": len(events),
        "failed_event_count": len(failed),
        "distinct_input_digest_count": len(input_digests),
        "distinct_output_digest_count": len(output_digests),
        "source_upload": manifest.get("source_upload"),
        "roles": roles,
        "manifest_json_sha256": sha256_file(MANIFEST_JSON),
        "manifest_md_sha256": sha256_file(MANIFEST_MD),
        "claim_boundary": manifest.get("claim_boundary", []),
        "failed": failed,
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ym_source_transfer_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with (OUT / "ym_source_transfer_events.jsonl").open("w", encoding="utf-8") as handle:
        for item in events:
            handle.write(json.dumps(item, sort_keys=True) + "\n")

    lines = [
        "# Yang-Mills Source Transfer Validation Result",
        "",
        "Scope: source availability manifest only. No theorem promotion.",
        "",
        f"- event_count: {summary['event_count']}",
        f"- failed_event_count: {summary['failed_event_count']}",
        f"- distinct_input_digest_count: {summary['distinct_input_digest_count']}",
        f"- distinct_output_digest_count: {summary['distinct_output_digest_count']}",
        f"- source_zip_sha256: {summary['source_upload']['sha256']}",
        f"- source_file_count: {summary['source_upload']['file_count']}",
        "",
        "## Load-bearing roles",
        "",
    ]
    for key, value in roles.items():
        lines.append(f"- {key}: {', '.join(value)}")
    (OUT / "ym_source_transfer_result.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if failed:
        raise SystemExit(f"Yang-Mills source-transfer manifest validation failed: {failed}")

    print("ym_source_transfer_manifest: PASS")
    print(f"event_count={summary['event_count']}")
    print(f"distinct_input_digest_count={summary['distinct_input_digest_count']}")
    print(f"distinct_output_digest_count={summary['distinct_output_digest_count']}")
    print(f"failed_event_count={summary['failed_event_count']}")
    print(f"source_zip_sha256={summary['source_upload']['sha256']}")
    print(f"source_file_count={summary['source_upload']['file_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
