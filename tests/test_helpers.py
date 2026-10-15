import copy
import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result
prepare = module("prepare_env").prepare
calculate = module("score_setup").calculate

class EnvTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True, capture_output=True)
        (self.root / ".gitignore").write_text(".env\n.env.*\n!.env.example\n")

    def test_creates_empty_fields_and_is_idempotent(self):
        self.assertEqual(prepare(self.root, ["SERVICE_API_KEY", "SERVICE_API_KEY"]), ["SERVICE_API_KEY"])
        before = (self.root / ".env").read_bytes()
        self.assertEqual(before, b"SERVICE_API_KEY=\n")
        self.assertEqual(prepare(self.root, ["SERVICE_API_KEY"]), [])
        self.assertEqual((self.root / ".env").read_bytes(), before)

    def test_preserves_existing_values_comments_and_line_endings(self):
        before = b"# local\r\nexport SERVICE_API_KEY=dummy-test-value\r\nOTHER=leave-this"
        (self.root / ".env").write_bytes(before)
        self.assertEqual(prepare(self.root, ["SERVICE_API_KEY", "NEW_KEY"]), ["NEW_KEY"])
        self.assertEqual((self.root / ".env").read_bytes(), before + b"\r\nNEW_KEY=\r\n")

    def test_rejects_unignored_and_tracked_files(self):
        (self.root / ".gitignore").write_text("")
        with self.assertRaises(ValueError):
            prepare(self.root, ["KEY"])
        self.assertFalse((self.root / ".env").exists())
        (self.root / ".env").write_text("KEY=dummy-test-value")
        subprocess.run(["git", "-C", str(self.root), "add", ".env"], check=True, capture_output=True)
        (self.root / ".gitignore").write_text(".env\n")
        with self.assertRaises(ValueError):
            prepare(self.root, ["NEW_KEY"])

    def test_rejects_values_in_variable_argument(self):
        for names in ([], ["KEY=secret"], ["KEY\nBAD"], ["../KEY"]):
            with self.assertRaises(ValueError):
                prepare(self.root, names)
        self.assertFalse((self.root / ".env").exists())

    def test_env_example_remains_publishable(self):
        (self.root / ".env.example").write_text("SERVICE_API_KEY=\n")
        prepare(self.root, ["SERVICE_API_KEY"])
        result = subprocess.run(["git", "-C", str(self.root), "status", "--short", "--untracked-files=all"], check=True, capture_output=True, text=True)
        self.assertIn(".env.example", result.stdout)
        self.assertNotIn("?? .env\n", result.stdout)

class ScoreTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "categories": {c: [{"score": 5, "evidence": "verified test fixture"} for _ in range(5)]
                           for c in ("context", "connections", "capabilities", "cadence")},
            "manual_only": False, "successful_due_runs": 2, "material_conflict": False,
        }

    def test_complete_evidence_can_reach_100(self):
        self.assertEqual(calculate(self.data)["score"], 100)

    def test_material_conflict_and_missing_runs_cap_score(self):
        self.data["material_conflict"] = True
        self.assertEqual(calculate(self.data)["score"], 84)
        self.data["successful_due_runs"] = 1
        self.assertEqual(calculate(self.data)["score"], 69)

    def test_weak_category_cannot_be_hidden_by_strong_others(self):
        for item in self.data["categories"]["connections"]:
            item["score"] = 1
        self.assertEqual(calculate(self.data)["score"], 49)

    def test_manual_cadence_cap_precedes_total_cap(self):
        self.data["manual_only"] = True
        result = calculate(self.data)
        self.assertEqual(result["raw_sum"], 100)
        self.assertEqual(result["categories"]["cadence"], 10)
        self.assertEqual(result["score"], 69)

    def test_unassessed_is_partial_but_checked_missing_is_zero(self):
        self.data["categories"]["context"][0]["score"] = None
        self.assertIsNone(calculate(self.data)["score"])
        self.data["categories"]["context"][0]["score"] = 0
        self.assertEqual(calculate(self.data)["score"], 69)

    def test_missing_safeguards_cap_overall_score(self):
        for category, index in (("connections", 2), ("capabilities", 3)):
            bad = copy.deepcopy(self.data)
            bad["categories"][category][index]["score"] = 0
            self.assertEqual(calculate(bad)["score"], 49)

    def test_invalid_or_unsupported_scores_are_rejected(self):
        for value in (2, 4, 6, True, "5"):
            bad = copy.deepcopy(self.data)
            bad["categories"]["context"][0]["score"] = value
            with self.assertRaises(ValueError):
                calculate(bad)
        self.data["categories"]["context"][0]["evidence"] = ""
        with self.assertRaises(ValueError):
            calculate(self.data)

if __name__ == "__main__":
    unittest.main()
