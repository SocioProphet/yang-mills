from pathlib import Path
import os
import unittest


ROOT = Path(__file__).resolve().parents[1]
HELLER_GODEL_COMMIT = "fb6b866f1b9b4089629cac18c179c32863bf42e4"
HELLER_DIRAC_COMMIT = "e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993"
CANONICAL_SCHEMA_NAMES = {
    "claim_ledger_row.schema.json",
    "event_ir.schema.json",
    "proof_artifact.schema.json",
    "calibration_bundle.schema.json",
}


class TestDependencyPins(unittest.TestCase):
    def test_dependencies_file_pins_both_upstreams(self) -> None:
        text = (ROOT / "DEPENDENCIES.md").read_text(encoding="utf-8")
        self.assertIn(HELLER_GODEL_COMMIT, text)
        self.assertIn(HELLER_DIRAC_COMMIT, text)
        self.assertIn("HG-MTH-007", text)
        self.assertIn("A-HG-MTH-006", text)
        self.assertIn("HD-FND-001", text)
        self.assertIn("HD-FND-003", text)
        self.assertIn("HD-FND-006", text)
        self.assertIn("HD-FND-010", text)
        self.assertIn("A-HD-FT-001", text)
        self.assertIn("A-HD-FND-001", text)

    def test_bridge_citation_anchor_exists(self) -> None:
        path = ROOT / "docs" / "scope" / "yang-mills-bridge-citation.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("HG-MTH-007", text)
        self.assertIn("A-HG-MTH-006", text)
        self.assertIn(HELLER_GODEL_COMMIT, text)
        self.assertIn(HELLER_DIRAC_COMMIT, text)

    def test_no_local_canonical_schema_shadowing(self) -> None:
        local_schemas = ROOT / "schemas"
        if not local_schemas.exists():
            return
        local_names = {path.name for path in local_schemas.rglob("*.json")}
        shadowed = sorted(local_names & CANONICAL_SCHEMA_NAMES)
        self.assertFalse(shadowed, f"local schemas shadow canonical PFK schemas: {shadowed}")

    def test_heller_godel_paths_resolve_when_available(self) -> None:
        hg_root_value = os.environ.get("HELLER_GODEL_ROOT")
        if not hg_root_value:
            self.skipTest("HELLER_GODEL_ROOT not set; dependency-resolution check runs in workflow")
        hg_root = Path(hg_root_value)
        required = [
            hg_root / "docs" / "framework-core" / "universal-bridge" / "HG-MTH-007-yang-mills-bridge-spec.md",
            hg_root / "proof_fabric_kernel" / "schemas" / "claim_ledger_row.schema.json",
            hg_root / "proof_fabric_kernel" / "schemas" / "event_ir.schema.json",
            hg_root / "proof_fabric_kernel" / "schemas" / "proof_artifact.schema.json",
            hg_root / "proof_fabric_kernel" / "schemas" / "calibration_bundle.schema.json",
        ]
        missing = [str(path) for path in required if not path.exists()]
        self.assertFalse(missing, f"Missing Heller-Godel paths: {missing}")

    def test_heller_dirac_paths_resolve_when_available(self) -> None:
        hd_root_value = os.environ.get("HELLER_DIRAC_ROOT")
        if not hd_root_value:
            self.skipTest("HELLER_DIRAC_ROOT not set; dependency-resolution check runs in workflow")
        hd_root = Path(hd_root_value)
        foundations = hd_root / "docs" / "foundations"
        for ident in ["HD-FND-001", "HD-FND-003", "HD-FND-006", "HD-FND-010"]:
            matches = list(foundations.glob(f"{ident}-*.md"))
            self.assertTrue(matches, f"Missing {ident} at Heller-Dirac pin {HELLER_DIRAC_COMMIT}")


if __name__ == "__main__":
    unittest.main()
