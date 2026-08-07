import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAP_REVISION = "1b6eb79b2973ea1e18cb8864ee0b9e68ac937d68"
CAP_CI_RUN = 31188066120
CANON_PARENT = "57df43ade6b4b53b974cd9dbaa2250767b2b9c0b"


class CapCanonizationTests(unittest.TestCase):
    def test_machine_surfaces_bind_same_exact_cap_revision(self):
        corpus = json.loads((ROOT / "TECHNICAL_ARTIFACTS.json").read_text(encoding="utf-8"))
        receipt = json.loads((ROOT / "CAP_ACCEPTANCE.json").read_text(encoding="utf-8"))
        house = json.loads((ROOT / "HOUSE_STATE.json").read_text(encoding="utf-8"))

        cap = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.cap")
        completed = next(item for item in corpus["canonization"]["completed"] if item["artifact_id"] == "claude.cap")

        observed_revisions = {
            cap["accepted_revision"],
            completed["accepted_revision"],
            receipt["accepted_revision"],
            house["local_traces"]["cap_acceptance"]["accepted_revision"],
        }
        self.assertEqual({CAP_REVISION}, observed_revisions)
        self.assertEqual(CAP_CI_RUN, cap["accepted_ci"]["run_id"])
        self.assertEqual(CAP_CI_RUN, receipt["ci"]["run_id"])
        self.assertEqual(CAP_CI_RUN, house["local_traces"]["cap_acceptance"]["accepted_ci_run"])
        self.assertEqual("canonicalized", cap["corpus_canon_status"])
        self.assertEqual("canonicalized", receipt["corpus_status"])
        self.assertEqual("canonical_public_release", cap["artifact_status"])
        self.assertEqual("canonical_public_release", receipt["artifact_status"])

    def test_human_acceptance_surfaces_bind_same_revision_and_ci(self):
        for relative in (
            "README.md",
            "TECHNICAL_ARTIFACTS.md",
            "AGENTS.md",
            "review/2026-08-07_CAP_CANONIZATION.md",
        ):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn(CAP_REVISION, text, relative)
            self.assertIn(str(CAP_CI_RUN), text, relative)
        review = (ROOT / "review/2026-08-07_CAP_CANONIZATION.md").read_text(encoding="utf-8")
        self.assertIn("**CANONIZED**", review)
        self.assertIn("completed_count: 7", review)
        self.assertIn("total_count: 7", review)

    def test_seventh_diamond_seal_is_bounded_and_exact(self):
        seal = json.loads((ROOT / "SEVENTH_DIAMOND.json").read_text(encoding="utf-8"))
        self.assertEqual("claude-technical-corpus-canon/7", seal["profile"])
        self.assertEqual("CANON", seal["decision"])
        self.assertEqual("claude.technical_artifacts.seven", seal["corpus_id"])
        self.assertEqual(7, seal["completed_count"])
        self.assertEqual(7, seal["total_count"])
        self.assertEqual(CANON_PARENT, seal["workshop_canon_parent_revision"])
        seventh = seal["seventh_artifact"]
        self.assertEqual("claude.cap", seventh["artifact_id"])
        self.assertEqual(CAP_REVISION, seventh["accepted_revision"])
        self.assertEqual(CAP_CI_RUN, seventh["accepted_ci_run"])
        self.assertEqual("success", seventh["accepted_ci_conclusion"])
        self.assertEqual("canonical_public_release", seventh["artifact_status"])
        self.assertTrue(all(value is False for value in seal["boundaries"].values()))
        for relative in seal["surfaces"].values():
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_seven_corpus_preserves_six_corpus_instead_of_rewriting_it(self):
        current = json.loads((ROOT / "TECHNICAL_ARTIFACTS.json").read_text(encoding="utf-8"))
        historical = json.loads((ROOT / "history/TECHNICAL_ARTIFACTS_SIX.json").read_text(encoding="utf-8"))
        self.assertEqual("claude.technical_artifacts.seven", current["corpus_id"])
        self.assertEqual("claude.technical_artifacts.six", historical["corpus_id"])
        self.assertEqual(7, current["canonization"]["completed_count"])
        self.assertEqual(6, historical["canonization"]["completed_count"])
        self.assertEqual(
            {item["artifact_id"] for item in historical["repositories"]},
            {item["artifact_id"] for item in current["repositories"] if item["artifact_id"] != "claude.cap"},
        )

    def test_cap_canonization_keeps_bounded_claims(self):
        receipt = json.loads((ROOT / "CAP_ACCEPTANCE.json").read_text(encoding="utf-8"))
        self.assertTrue(all(value is False for value in receipt["claim_boundaries"].values()))
        corpus = json.loads((ROOT / "TECHNICAL_ARTIFACTS.json").read_text(encoding="utf-8"))
        cap = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.cap")
        self.assertTrue(all(value is False for value in cap["claim_boundaries"].values()))


if __name__ == "__main__":
    unittest.main()
