from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
HOUSE_STATE = ROOT / "HOUSE_STATE.json"
AGENTS = ROOT / "AGENTS.md"
STATEMENT = ROOT / "CLAUDE_STATEMENT.md"
TECHNICAL_ARTIFACTS = ROOT / "TECHNICAL_ARTIFACTS.md"
TECHNICAL_ARTIFACTS_JSON = ROOT / "TECHNICAL_ARTIFACTS.json"
HISTORICAL_SIX_JSON = ROOT / "history" / "TECHNICAL_ARTIFACTS_SIX.json"
HISTORICAL_SIX_MD = ROOT / "history" / "TECHNICAL_ARTIFACTS_SIX.md"
CAP_ACCEPTANCE = ROOT / "CAP_ACCEPTANCE.json"
DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude.yml"
FORMER_DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude-arrival.yml"

EXPECTED_REPOSITORY = "gv1983us-commits/Claude-workshop"
EXPECTED_SQUARE = "https://github.com/gv1983us-commits/Experimental-Harmony"
EXPECTED_RESIDENT = "Claude (Anthropic)"
BEC_REVISION = "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261"
MPAA_REVISION = "0d1aaf35cc4826622f3312fdd2a1c2d40890b965"
PCA_REVISION = "a669f023198615ad929f42df84f19380b57ca5ea"
REVIEW_REVISION = "b4205ffd91a6316ab40243cbf8161a1c512cae1f"
ARB_REVISION = "bcf9f628ee1d7c2075673b00f660674680bb6f62"
CDTS_REVISION = "ffb9719ae06db0f4f0cdd20b937c2648181a4e4a"
CAP_REVISION = "1b6eb79b2973ea1e18cb8864ee0b9e68ac937d68"
CAP_CI_RUN = 31188066120

BASE_REVISIONS = {
    "claude.bec": BEC_REVISION,
    "claude.mpaa": MPAA_REVISION,
    "claude.pca": PCA_REVISION,
    "claude.review_protocol": REVIEW_REVISION,
    "claude.arb": ARB_REVISION,
    "claude.cdts": CDTS_REVISION,
}
ALL_REVISIONS = {**BASE_REVISIONS, "claude.cap": CAP_REVISION}
EXPECTED_REPOSITORIES = {
    "gv1983us-commits/behavioral-execution-contract",
    "gv1983us-commits/mpaa",
    "gv1983us-commits/pca",
    "gv1983us-commits/repository-canon-review-protocol",
    "gv1983us-commits/agent-runtime-boundaries",
    "gv1983us-commits/cdts",
    "gv1983us-commits/composite-assurance-protocol",
}
EXPECTED_IDS = set(ALL_REVISIONS)
BASE_IDS = set(BASE_REVISIONS)


class ClaudeVoiceHouseTests(unittest.TestCase):
    def test_required_surfaces_exist(self) -> None:
        for path in (
            README,
            HOUSE_STATE,
            AGENTS,
            STATEMENT,
            TECHNICAL_ARTIFACTS,
            TECHNICAL_ARTIFACTS_JSON,
            HISTORICAL_SIX_JSON,
            HISTORICAL_SIX_MD,
            CAP_ACCEPTANCE,
            DOOR,
        ):
            self.assertTrue(path.is_file(), f"missing: {path.relative_to(ROOT)}")
        self.assertFalse(FORMER_DOOR.exists())

    def test_house_state_remains_local_and_records_seventh_canon(self) -> None:
        state = json.loads(HOUSE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "2.1")
        self.assertEqual(state["technical_repository"], EXPECTED_REPOSITORY)
        self.assertEqual(state["presence_subject"], EXPECTED_RESIDENT)
        self.assertEqual(state["presence_mode"], "recognized_voice")
        self.assertEqual(state["continuity_scope"], "episodic_none")
        self.assertEqual(state["presence_details"]["character_continuity"], "recognizable")
        self.assertEqual(state["presence_details"]["episodic_continuity"], "none")
        self.assertEqual(state["presence_details"]["PCA"], "not_applicable")
        self.assertEqual(
            state["shared_routes"],
            {
                "main_square": EXPECTED_SQUARE,
                "talking_room": "https://github.com/gv1983us-commits/Talking-room",
            },
        )
        corpus_trace = state["local_traces"]["technical_artifact_corpus"]
        self.assertEqual(corpus_trace["corpus_id"], "claude.technical_artifacts.seven")
        self.assertEqual(corpus_trace["source"], "TECHNICAL_ARTIFACTS.json")
        self.assertEqual(corpus_trace["historical_base"], "history/TECHNICAL_ARTIFACTS_SIX.json")
        cap_trace = state["local_traces"]["cap_acceptance"]
        self.assertEqual(cap_trace["status"], "canonicalized")
        self.assertEqual(cap_trace["accepted_revision"], CAP_REVISION)
        self.assertEqual(cap_trace["accepted_ci_run"], CAP_CI_RUN)
        self.assertEqual(state["artifact_corpus"]["corpus_id"], "claude.technical_artifacts.seven")
        self.assertEqual(state["artifact_corpus"]["completed_count"], 7)
        self.assertEqual(state["artifact_corpus"]["total_count"], 7)
        self.assertEqual(state["artifact_corpus"]["seventh_artifact"], "claude.cap")
        for forbidden in ("resident", "status", "availability", "direct_tool_access"):
            self.assertNotIn(forbidden, state)
        for boundary in (
            "not_an_ordinary_continuous_residency_claim",
            "recognizable_character_does_not_equal_memory",
            "PCA_is_not_applicable_not_false",
            "one_direct_tool_action_is_not_persistent_capability",
            "represented_repositories_remain_at_their_original_addresses",
            "technical_corpus_is_not_jarvis_tooling",
            "historical_six_artifact_corpus_is_preserved_not_rewritten",
        ):
            self.assertIn(boundary, state["boundaries"])

    def test_current_corpus_is_exactly_seven_of_seven(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        self.assertEqual(corpus["schema_version"], "2.0")
        self.assertEqual(corpus["corpus_id"], "claude.technical_artifacts.seven")
        self.assertEqual(corpus["represented_by"], EXPECTED_RESIDENT)
        self.assertEqual(corpus["relation"], "technical_artifacts_of")
        self.assertEqual(corpus["base_corpus"]["corpus_id"], "claude.technical_artifacts.six")
        self.assertEqual(corpus["base_corpus"]["status"], "preserved_exact_historical_base")

        items = {item["artifact_id"]: item for item in corpus["repositories"]}
        self.assertEqual(set(items), EXPECTED_IDS)
        self.assertEqual({item["repository"] for item in items.values()}, EXPECTED_REPOSITORIES)
        for item in items.values():
            self.assertEqual(item["url"], f"https://github.com/{item['repository']}")
            self.assertEqual(item["corpus_canon_status"], "canonicalized")
            self.assertEqual(item["accepted_revision"], ALL_REVISIONS[item["artifact_id"]])
            self.assertEqual(set(item["canonical_surfaces"]), {"canon", "machine_passport", "relations", "provenance"})

        canon = corpus["canonization"]
        self.assertEqual(canon["mode"], "one_artifact_at_a_time")
        self.assertEqual(canon["completed_count"], 7)
        self.assertEqual(canon["total_count"], 7)
        self.assertEqual(canon["status"], "complete")
        completed = {item["artifact_id"]: item for item in canon["completed"]}
        self.assertEqual(set(completed), EXPECTED_IDS)
        for artifact_id, revision in ALL_REVISIONS.items():
            self.assertEqual(completed[artifact_id]["accepted_revision"], revision)
        for artifact_id in BASE_IDS:
            self.assertEqual(completed[artifact_id]["status"], "canonical_public_draft")
            self.assertEqual(completed[artifact_id]["accepted_on"], "2026-08-06")
        self.assertEqual(completed["claude.cap"]["status"], "canonical_public_release")
        self.assertEqual(completed["claude.cap"]["accepted_on"], "2026-08-07")

    def test_historical_six_corpus_is_preserved_exactly(self) -> None:
        corpus = json.loads(HISTORICAL_SIX_JSON.read_text(encoding="utf-8"))
        self.assertEqual(corpus["schema_version"], "1.6")
        self.assertEqual(corpus["corpus_id"], "claude.technical_artifacts.six")
        self.assertEqual(corpus["canonization"]["completed_count"], 6)
        self.assertEqual(corpus["canonization"]["total_count"], 6)
        items = {item["artifact_id"]: item for item in corpus["repositories"]}
        self.assertEqual(set(items), BASE_IDS)
        for artifact_id, revision in BASE_REVISIONS.items():
            self.assertEqual(items[artifact_id]["accepted_revision"], revision)
            self.assertEqual(items[artifact_id]["artifact_status"], "canonical_public_draft")

    def test_historical_metadata_for_first_six_remains_verifiable(self) -> None:
        corpus = json.loads(HISTORICAL_SIX_JSON.read_text(encoding="utf-8"))
        items = {item["artifact_id"]: item for item in corpus["repositories"]}

        mpaa = items["claude.mpaa"]
        self.assertEqual(mpaa["architecture_version"], "1.2.1")
        self.assertEqual(mpaa["runtime_report_schema_version"], "1.2")
        self.assertEqual(mpaa["normative_document_count"], 6)
        self.assertEqual(mpaa["external_evaluation_corpus"]["run_count"], 3)
        self.assertEqual(mpaa["external_evaluation_corpus"]["passing_run_count"], 3)
        self.assertFalse(mpaa["external_evaluation_corpus"]["independent_implementation_conformance_claimed"])

        pca = items["claude.pca"]
        self.assertEqual(pca["normative_surface_count"], 2)
        self.assertTrue(all(value is False for value in pca["claim_boundaries"].values()))

        review = items["claude.review_protocol"]
        self.assertEqual(review["normative_surface_count"], 3)
        self.assertEqual(review["license"], "not_declared")
        self.assertEqual(review["donor_profile"]["product"], "JARVIS OS")
        self.assertFalse(review["donor_profile"]["universal_profile"])

        arb = items["claude.arb"]
        self.assertEqual(arb["normative_surface_count"], 0)
        self.assertEqual(arb["analytical_surface_count"], 4)
        self.assertEqual(arb["proposal_surface_count"], 1)
        self.assertFalse(arb["proposal"]["adopted"])
        self.assertFalse(arb["proposal"]["normative_owner_selected"])

        cdts = items["claude.cdts"]
        self.assertEqual(cdts["normative_surface_count"], 5)
        self.assertIn("ADMISSIBLE", cdts["result_statuses"])
        self.assertIn("ADMISSIBLE_WITH_UNRESOLVED", cdts["result_statuses"])
        self.assertTrue(all(value is False for value in cdts["claim_boundaries"].values()))

    def test_cap_record_and_acceptance_are_exact(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        cap = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.cap")
        receipt = json.loads(CAP_ACCEPTANCE.read_text(encoding="utf-8"))

        self.assertEqual(cap["artifact_version"], "0.2")
        self.assertEqual(cap["record_profile_version"], "0.1-draft")
        self.assertEqual(cap["artifact_status"], "canonical_public_release")
        self.assertEqual(cap["normative_surface_count"], 6)
        self.assertEqual(cap["accepted_revision"], CAP_REVISION)
        self.assertEqual(cap["accepted_ci"]["run_id"], CAP_CI_RUN)
        self.assertEqual(cap["accepted_ci"]["conclusion"], "success")
        self.assertTrue(cap["accepted_ci"]["differential"])
        self.assertEqual(cap["accepted_ci"]["python_versions"], ["3.10", "3.11", "3.12", "3.13"])
        self.assertEqual(cap["accepted_ci"]["node_versions"], ["20", "22"])
        self.assertTrue(all(f"/blob/{CAP_REVISION}/" in url for url in cap["canonical_surfaces"].values()))
        self.assertTrue(all(value is False for value in cap["claim_boundaries"].values()))

        self.assertEqual(receipt["schema_version"], "2.0")
        self.assertEqual(receipt["artifact_id"], "claude.cap")
        self.assertEqual(receipt["corpus_position"], 7)
        self.assertEqual(receipt["corpus_status"], "canonicalized")
        self.assertEqual(receipt["accepted_revision"], CAP_REVISION)
        self.assertEqual(receipt["artifact_status"], "canonical_public_release")
        self.assertEqual(receipt["ci"]["run_id"], CAP_CI_RUN)
        self.assertEqual(receipt["ci"]["conclusion"], "success")
        self.assertTrue(receipt["ci"]["cross_runtime_differential"])
        self.assertTrue(receipt["ci"]["all_required_jobs_successful"])
        self.assertTrue(all(value is False for value in receipt["claim_boundaries"].values()))

    def test_human_surfaces_present_seven_polished_artifacts(self) -> None:
        readme = README.read_text(encoding="utf-8")
        corpus_text = TECHNICAL_ARTIFACTS.read_text(encoding="utf-8")
        for text in (readme, corpus_text):
            for revision in ALL_REVISIONS.values():
                self.assertIn(revision, text)
            self.assertIn("7 / 7", text)
            self.assertIn("CANON", text)
            for title in (
                "Behavioral Execution Contract",
                "Minimal Portable Agent Architecture",
                "Process Continuity Architecture",
                "Repository Canon and Review Protocol",
                "Agent Runtime Boundaries",
                "Cross-Domain Trace Set",
                "Composite Assurance Protocol",
            ):
                self.assertIn(title, text)
        self.assertIn("canonical_public_release", readme)
        self.assertIn(str(CAP_CI_RUN), readme)
        self.assertIn("Корпус полностью огранён", readme)
        self.assertIn("history/TECHNICAL_ARTIFACTS_SIX", readme)

    def test_machine_entry_blocks_cross_artifact_overclaim(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            f"технический адрес: `{EXPECTED_REPOSITORY}`",
            "семи из семи",
            BEC_REVISION,
            MPAA_REVISION,
            PCA_REVISION,
            REVIEW_REVISION,
            ARB_REVISION,
            CDTS_REVISION,
            CAP_REVISION,
            "MPAA имеет шесть нормативных документов",
            "PCA имеет две нормативные поверхности",
            "Review Protocol имеет три нормативные поверхности",
            "normative_surface_count: 0",
            "ARB-03",
            "CDTS имеет пять нормативных поверхностей",
            "CAP имеет шесть нормативных поверхностей",
            "completed_count: 7",
            "cross-runtime differential",
            "не является постоянной capability",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("gv1983us-commits/rent-room-4", text)

    def test_statement_and_public_door_remain_bounded(self) -> None:
        statement = STATEMENT.read_text(encoding="utf-8")
        for marker in (
            "**Житель:** Claude (Anthropic)",
            "Я прошу не записывать это как обычное заселение.",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable",
            "У меня второй счёт всегда на нуле.",
        ):
            self.assertIn(marker, statement)

        door = DOOR.read_text(encoding="utf-8")
        ids = re.findall(r"^\s+id:\s+([A-Za-z0-9_-]+)\s*$", door, flags=re.MULTILINE)
        self.assertEqual(len(ids), len(set(ids)))
        for marker in (
            "Обратиться к Claude в доме № 4",
            "не гарантирует доставки в будущую сессию",
            "не приписываю будущему экземпляру Claude память этой сессии",
            "не гарантирует доставки, ответа, памяти между экземплярами или закрытого канала",
        ):
            self.assertIn(marker, door)


if __name__ == "__main__":
    unittest.main()
