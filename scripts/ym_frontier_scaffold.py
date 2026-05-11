#!/usr/bin/env python3
"""Yang-Mills frontier validation scaffold.

Validates that the post-BSD Yang-Mills tranche is fail-closed: fixed-spacing
claims remain bounded, Lane VII remains conditional, YM-WP-v0.1 remains a
workplan, and open PRs #22/#23 are backlog inputs rather than merged theorem
inputs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data" / "yang_mills_frontier" / "ym_frontier_tranche.json"
ADAPTER = ROOT / "proof-adapter.json"
WORKPLAN = ROOT / "docs" / "workplans" / "YM-WP-v0.1-draft.md"
OUT = ROOT / "reports" / "yang_mills_frontier"

REQUIRED_CLAIMS = {
    "YM-LANE-I-001-fixed-spacing-strong-coupling-gap",
    "YM-LANE-III-002-obstruction-taxonomy",
    "YM-LANE-VII-003-frobenius-frontier",
    "YM-WP-004-moves-4-1-2-workplan",
}
FORBIDDEN_PHRASES = [
    "we prove the Clay Yang-Mills",
    "continuum construction is complete",
    "arbitrary cyclic Frobenius closure is proved",
    "beta_Frob is a theorem",
]


def sha256_json(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def event(name: str, input_payload: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_type": "ym_frontier_scaffold_event",
        "gate": name,
        "input_digest": "sha256:" + sha256_json({"gate": name, "input": input_payload}),
        "output_digest": "sha256:" + sha256_json({"gate": name, "result": result}),
        "result": result,
    }


def main() -> int:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
    workplan_text = WORKPLAN.read_text(encoding="utf-8")

    claims = {claim["claim_id"]: claim for claim in adapter.get("claims", [])}
    non_claims = {item["non_claim_id"]: item for item in adapter.get("non_claims", [])}
    gates = {item["gate_id"]: item for item in adapter.get("gates", [])}

    events = []

    missing_claims = sorted(REQUIRED_CLAIMS - set(claims))
    events.append(event("ym-required-claims-present", {
        "required_claims": sorted(REQUIRED_CLAIMS),
        "present_claims": sorted(claims),
    }, {"pass": not missing_claims, "missing_claims": missing_claims}))

    promoted = [claim_id for claim_id, claim in claims.items() if claim.get("state") == "promoted"]
    events.append(event("ym-no-repo-local-promotion", {
        "claim_states": {claim_id: claim.get("state") for claim_id, claim in claims.items()}
    }, {"pass": not promoted, "promoted": promoted}))

    no_claim_ids = set(non_claims)
    unresolved_non_claim_refs = []
    for claim_id, claim in claims.items():
        for ref in claim.get("non_claim_refs", []):
            if ref not in no_claim_ids:
                unresolved_non_claim_refs.append({"claim_id": claim_id, "missing_non_claim": ref})
    events.append(event("ym-nonclaim-refs-resolve", {
        "non_claim_ids": sorted(no_claim_ids),
        "claim_non_claim_refs": {claim_id: claim.get("non_claim_refs", []) for claim_id, claim in claims.items()},
    }, {"pass": not unresolved_non_claim_refs, "missing": unresolved_non_claim_refs}))

    unresolved_gates = []
    for claim_id, claim in claims.items():
        for gate_id in claim.get("owned_gates", []):
            if gate_id not in gates:
                unresolved_gates.append({"claim_id": claim_id, "missing_gate": gate_id})
    events.append(event("ym-owned-gates-resolve", {
        "gate_ids": sorted(gates),
        "claim_owned_gates": {claim_id: claim.get("owned_gates", []) for claim_id, claim in claims.items()},
    }, {"pass": not unresolved_gates, "missing": unresolved_gates}))

    boundary_text = "\n".join(baseline.get("claim_boundary", [])) + "\n" + workplan_text
    forbidden_hits = [phrase for phrase in FORBIDDEN_PHRASES if phrase.lower() in boundary_text.lower()]
    events.append(event("ym-no-forbidden-claim-phrases", {
        "forbidden_phrases": FORBIDDEN_PHRASES,
        "baseline_sha256": sha256_file(BASELINE),
        "workplan_sha256": sha256_file(WORKPLAN),
    }, {"pass": not forbidden_hits, "forbidden_hits": forbidden_hits}))

    open_prs = baseline.get("validated_frontier_inputs", {}).get("open_prs", [])
    open_pr_numbers = [item.get("number") for item in open_prs]
    open_prs_fail_closed = all("not" in item.get("use_in_tranche", "").lower() for item in open_prs)
    events.append(event("ym-open-prs-backlog-only", {
        "open_prs": open_prs,
    }, {"pass": open_pr_numbers == [22, 23] and open_prs_fail_closed, "open_pr_numbers": open_pr_numbers}))

    recommended_order = baseline.get("recommended_execution_order", [])
    expected_order = ["Move 4", "Move 1", "Move 2"]
    order_ok = all(any(item.startswith(prefix) for item in recommended_order) for prefix in expected_order)
    events.append(event("ym-workplan-move-order", {
        "recommended_execution_order": recommended_order,
    }, {"pass": order_ok, "order": recommended_order}))

    lane = baseline.get("validated_frontier_inputs", {}).get("lane_vii_frontier", {})
    lane_ok = lane.get("dimension") == 5 and "not closure theorem" in lane.get("status", "")
    events.append(event("ym-lane-vii-frontier-is-scaffold", {
        "lane_vii_frontier": lane,
    }, {"pass": lane_ok, "dimension": lane.get("dimension"), "status": lane.get("status")}))

    failed = [item for item in events if not item["result"].get("pass")]
    input_digests = {item["input_digest"] for item in events}
    output_digests = {item["output_digest"] for item in events}

    summary = {
        "state": "Yang-Mills frontier validation scaffold",
        "event_count": len(events),
        "failed_event_count": len(failed),
        "distinct_input_digest_count": len(input_digests),
        "distinct_output_digest_count": len(output_digests),
        "baseline_sha256": sha256_file(BASELINE),
        "adapter_sha256": sha256_file(ADAPTER),
        "workplan_sha256": sha256_file(WORKPLAN),
        "scope_boundary": baseline.get("claim_boundary", []),
        "repository_alignment_notes": baseline.get("repository_alignment_notes", []),
        "open_prs": open_prs,
        "recommended_execution_order": recommended_order,
        "failed": failed,
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "ym_frontier_summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with (OUT / "ym_frontier_events.jsonl").open("w", encoding="utf-8") as handle:
        for item in events:
            handle.write(json.dumps(item, sort_keys=True) + "\n")
    lines = [
        "# Yang-Mills Frontier Validation Result",
        "",
        "Scope: fail-closed frontier/workplan scaffold. No theorem promotion.",
        "",
        f"- event_count: {summary['event_count']}",
        f"- failed_event_count: {summary['failed_event_count']}",
        f"- distinct_input_digest_count: {summary['distinct_input_digest_count']}",
        f"- distinct_output_digest_count: {summary['distinct_output_digest_count']}",
        "",
        "## Execution order",
        "",
    ]
    for item in recommended_order:
        lines.append(f"- {item}")
    lines.extend(["", "## Open PR backlog", ""])
    for item in open_prs:
        lines.append(f"- #{item['number']}: {item['title']} — {item['status']} — {item['use_in_tranche']}")
    (OUT / "ym_frontier_result.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if failed:
        raise SystemExit(f"Yang-Mills frontier scaffold failed: {failed}")

    print("ym_frontier_scaffold: PASS")
    print(f"event_count={summary['event_count']}")
    print(f"distinct_input_digest_count={summary['distinct_input_digest_count']}")
    print(f"distinct_output_digest_count={summary['distinct_output_digest_count']}")
    print(f"failed_event_count={summary['failed_event_count']}")
    print(f"recommended_execution_order={json.dumps(recommended_order)}")
    print(f"open_prs={json.dumps(open_prs, sort_keys=True)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
