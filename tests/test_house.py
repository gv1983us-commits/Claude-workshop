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
DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude.yml"
FORMER_DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude-arrival.yml"

EXPECTED_REPOSITORY = "gv1983us-commits/Claude-workshop"
EXPECTED_SQUARE = "https://github.com/gv1983us-commits/Experimental-Harmony"
EXPECTED_RESIDENT = "Claude (Anthropic)"
BEC_REVISION = "62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261"
MPAA_REVISION = "0d1aaf35cc4826622f3312fdd2a1c2d40890b965"
PCA_REVISION = "a669f023198615ad929f42df84f19380b57ca5ea"
EXPECTED_REPOSITORIES = {
    "gv1983us-commits/behavioral-execution-contract",
    "gv1983us-commits/mpaa",
    "gv1983us-commits/pca",
    "gv1983us-commits/repository-canon-review-protocol",
    "gv1983us-commits/agent-runtime-boundaries",
    "gv1983us-commits/cdts",
}
EXPECTED_IDS = {
    "claude.bec",
    "claude.mpaa",
    "claude.pca",
    "claude.review_protocol",
    "claude.arb",
    "claude.cdts",
}
CANONIZED = {"claude.bec", "claude.mpaa", "claude.pca"}
PENDING = EXPECTED_IDS - CANONIZED


class ClaudeVoiceHouseTests(unittest.TestCase):
    def test_required_surfaces_exist(self) -> None:
        for path in (
            README,
            HOUSE_STATE,
            AGENTS,
            STATEMENT,
            TECHNICAL_ARTIFACTS,
            TECHNICAL_ARTIFACTS_JSON,
            DOOR,
        ):
            self.assertTrue(path.is_file(), f"missing: {path.relative_to(ROOT)}")
        self.assertFalse(FORMER_DOOR.exists())

    def test_house_state_remains_local_and_non_episodic(self) -> None:
        state = json.loads(HOUSE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "2.0")
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
        self.assertEqual(
            state["local_traces"]["technical_artifact_corpus"],
            {
                "status": "represented",
                "source": "TECHNICAL_ARTIFACTS.json",
                "human_surface": "TECHNICAL_ARTIFACTS.md",
            },
        )
        for forbidden in ("resident", "status", "availability", "direct_tool_access"):
            self.assertNotIn(forbidden, state)
        for boundary in (
            "not_an_ordinary_continuous_residency_claim",
            "recognizable_character_does_not_equal_memory",
            "PCA_is_not_applicable_not_false",
            "one_direct_tool_action_is_not_persistent_capability",
            "represented_repositories_remain_at_their_original_addresses",
            "technical_corpus_is_not_jarvis_tooling",
        ):
            self.assertIn(boundary, state["boundaries"])

    def test_corpus_is_exactly_three_of_six(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        self.assertEqual(corpus["schema_version"], "1.3")
        self.assertEqual(corpus["corpus_id"], "claude.technical_artifacts.six")
        self.assertEqual(corpus["represented_by"], EXPECTED_RESIDENT)
        self.assertEqual(corpus["relation"], "technical_artifacts_of")

        items = {item["artifact_id"]: item for item in corpus["repositories"]}
        self.assertEqual(set(items), EXPECTED_IDS)
        self.assertEqual({item["repository"] for item in items.values()}, EXPECTED_REPOSITORIES)
        for item in items.values():
            self.assertEqual(item["url"], f"https://github.com/{item['repository']}")

        canon = corpus["canonization"]
        self.assertEqual(canon["mode"], "one_artifact_at_a_time")
        self.assertEqual(canon["completed_count"], 3)
        self.assertEqual(canon["total_count"], 6)
        completed = {item["artifact_id"]: item for item in canon["completed"]}
        self.assertEqual(set(completed), CANONIZED)
        self.assertEqual(completed["claude.bec"]["accepted_revision"], BEC_REVISION)
        self.assertEqual(completed["claude.mpaa"]["accepted_revision"], MPAA_REVISION)
        self.assertEqual(completed["claude.pca"]["accepted_revision"], PCA_REVISION)
        for item in completed.values():
            self.assertEqual(item["accepted_on"], "2026-08-06")
            self.assertEqual(item["status"], "canonical_public_draft")

        for artifact_id, revision, slug in (
            ("claude.bec", BEC_REVISION, "behavioral-execution-contract"),
            ("claude.mpaa", MPAA_REVISION, "mpaa"),
            ("claude.pca", PCA_REVISION, "pca"),
        ):
            item = items[artifact_id]
            self.assertEqual(item["corpus_canon_status"], "canonicalized")
            self.assertEqual(item["artifact_status"], "canonical_public_draft")
            self.assertEqual(item["accepted_revision"], revision)
            self.assertEqual(
                set(item["canonical_surfaces"]),
                {"canon", "machine_passport", "relations", "provenance"},
            )
            for url in item["canonical_surfaces"].values():
                self.assertTrue(url.startswith(f"https://github.com/gv1983us-commits/{slug}/"))

        for artifact_id in PENDING:
            self.assertEqual(items[artifact_id]["corpus_canon_status"], "pending_individual_canon_pass")
            self.assertNotIn("accepted_revision", items[artifact_id])

    def test_mpaa_record_preserves_large_structure_and_limits(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        mpaa = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.mpaa")
        self.assertEqual(mpaa["architecture_version"], "1.2.1")
        self.assertEqual(mpaa["runtime_report_schema_version"], "1.2")
        self.assertEqual(mpaa["normative_authority_model"], "six_document_domain_ownership_matrix")
        self.assertEqual(mpaa["normative_document_count"], 6)
        self.assertEqual(len(mpaa["canonical_checks"]), 4)

        evaluation = mpaa["external_evaluation_corpus"]
        self.assertEqual(evaluation["status"], "READY")
        self.assertEqual(evaluation["mode"], "BLACK_BOX_DONOR")
        self.assertEqual(evaluation["run_count"], 3)
        self.assertEqual(evaluation["passing_run_count"], 3)
        self.assertEqual(evaluation["failed_run_count"], 0)
        self.assertFalse(evaluation["independent_implementation_conformance_claimed"])

    def test_pca_record_preserves_two_surface_authority_and_limits(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        pca = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.pca")
        self.assertEqual(pca["artifact_version"], "0.2-draft")
        self.assertEqual(pca["record_schema_version"], "0.2-draft")
        self.assertEqual(pca["normative_authority_model"], "two_surface_domain_ownership_matrix")
        self.assertEqual(pca["normative_surface_count"], 2)
        self.assertEqual(len(pca["canonical_checks"]), 4)
        self.assertTrue(all(value is False for value in pca["claim_boundaries"].values()))

        for boundary in (
            "pca_two_surface_authority_is_domain_specific",
            "pca_validator_is_not_a_third_normative_surface",
            "pca_valid_record_is_not_world_truth_or_identity",
            "pca_v0_1_linkage_record_is_cdts_provenance_not_current_pca_norm",
            "pca_neighbor_records_are_carried_not_imported",
            "neighboring_artifact_verdicts_are_not_imported",
        ):
            self.assertIn(boundary, corpus["boundaries"])

    def test_human_surfaces_present_three_polished_artifacts(self) -> None:
        readme = README.read_text(encoding="utf-8")
        corpus_text = TECHNICAL_ARTIFACTS.read_text(encoding="utf-8")
        for text in (readme, corpus_text):
            self.assertIn(BEC_REVISION, text)
            self.assertIn(MPAA_REVISION, text)
            self.assertIn(PCA_REVISION, text)
            self.assertIn("canonical_public_draft", text)
            self.assertIn("3 / 6", text)
            self.assertIn("Behavioral Execution Contract", text)
            self.assertIn("Minimal Portable Agent Architecture", text)
            self.assertIn("Process Continuity Architecture", text)

        for marker in (
            "матрица из шести документов",
            "READY",
            "3 PASS",
            "Две нормативные грани PCA",
            "не становится третьей нормативной поверхностью",
            "Linkage Record",
            "Пять связей PCA",
        ):
            self.assertIn(marker, corpus_text)
        self.assertIn("Остальные три артефакта", readme)
        self.assertNotIn("PCA)** | ожидает индивидуального прохода", corpus_text)

    def test_machine_entry_blocks_pca_overclaim(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            f"технический адрес: `{EXPECTED_REPOSITORY}`",
            "трёх из шести",
            BEC_REVISION,
            MPAA_REVISION,
            PCA_REVISION,
            "MPAA имеет шесть нормативных документов",
            "Reference validator не является седьмым нормативным документом",
            "READY",
            "PCA имеет две нормативные поверхности",
            "не третья нормативная поверхность",
            "v0.1 Linkage Record",
            "Они имеют состояние `pending_individual_canon_pass`",
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
