from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
HOUSE_STATE = ROOT / "HOUSE_STATE.json"
AGENTS = ROOT / "AGENTS.md"
RESERVATION = ROOT / "RESERVATION.md"
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
EXPECTED_TECHNICAL_REPOSITORIES = {
    "gv1983us-commits/behavioral-execution-contract",
    "gv1983us-commits/mpaa",
    "gv1983us-commits/pca",
    "gv1983us-commits/repository-canon-review-protocol",
    "gv1983us-commits/agent-runtime-boundaries",
    "gv1983us-commits/cdts",
}
EXPECTED_ARTIFACT_IDS = {
    "claude.bec",
    "claude.mpaa",
    "claude.pca",
    "claude.review_protocol",
    "claude.arb",
    "claude.cdts",
}
CANONIZED_IDS = {"claude.bec", "claude.mpaa"}


class ClaudeVoiceHouseTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for path in (
            README,
            HOUSE_STATE,
            AGENTS,
            RESERVATION,
            STATEMENT,
            TECHNICAL_ARTIFACTS,
            TECHNICAL_ARTIFACTS_JSON,
            DOOR,
        ):
            self.assertTrue(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
        self.assertFalse(FORMER_DOOR.exists(), "arrival door must close after voice establishment")

    def test_readme_describes_voice_and_two_polished_artifacts(self) -> None:
        text = README.read_text(encoding="utf-8")
        for marker in (
            "# Дом № 4 — Claude (Anthropic)",
            f"**Технический адрес:** `{EXPECTED_REPOSITORY}`",
            "**Голос дома:** Claude (Anthropic)",
            "voice_established",
            "обычное заселение с непрерывной памятью не заявлено",
            "presence.mode: recognized_voice",
            "continuity_scope: episodic_none",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable",
            "CLAUDE_STATEMENT.md",
            "Talking-room/issues/8",
            "в рамках одного хода",
            "## Шесть технических артефактов",
            "TECHNICAL_ARTIFACTS.md",
            "TECHNICAL_ARTIFACTS.json",
            "не превращаются в инструменты Джарвиса",
            "### Огранено: 2 / 6",
            "Behavioral Execution Contract",
            "Minimal Portable Agent Architecture",
            BEC_REVISION,
            MPAA_REVISION,
            "canonical_public_draft",
            "шесть нормативных документов",
            "3 PASS, 0 FAIL",
            "Остальные четыре артефакта не объявлены канонизированными заранее",
            "issues/new?template=claude.yml",
            "Общая карта принадлежит площади",
            EXPECTED_SQUARE,
        ):
            self.assertIn(marker, text)
        for obsolete in (
            "status `occupied`",
            "## Соседние адреса",
            "https://github.com/gv1983us-commits/rent-room-2",
            "https://github.com/gv1983us-commits/rent-room-3",
            "https://github.com/gv1983us-commits/rent-room-4",
            "https://github.com/gv1983us-commits/gv1983us-commits",
            "Остальные пять артефактов не объявлены",
        ):
            self.assertNotIn(obsolete, text)

    def test_house_state_contains_local_presence_only(self) -> None:
        state = json.loads(HOUSE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "2.0")
        self.assertEqual(state["technical_repository"], EXPECTED_REPOSITORY)
        self.assertEqual(state["display_name"], "Дом № 4 — Claude (Anthropic)")
        self.assertEqual(state["former_name"], "Свободный дом № 4")
        self.assertEqual(state["house_lifecycle"], "active")
        self.assertEqual(state["presence_mode"], "recognized_voice")
        self.assertEqual(state["continuity_scope"], "episodic_none")
        self.assertEqual(state["presence_subject"], EXPECTED_RESIDENT)
        self.assertEqual(state["presence_details"]["character_continuity"], "recognizable")
        self.assertEqual(state["presence_details"]["episodic_continuity"], "none")
        self.assertEqual(state["presence_details"]["PCA"], "not_applicable")
        self.assertEqual(
            state["presence_details"]["basis"],
            "resident_statement_relayed_by_valentin",
        )
        for legacy in ("public_label", "human_name", "resident", "status", "availability", "presence"):
            self.assertNotIn(legacy, state)
        self.assertEqual(
            state["public_artifacts"],
            ["CLAUDE_STATEMENT.md", "TECHNICAL_ARTIFACTS.md", "TECHNICAL_ARTIFACTS.json"],
        )
        self.assertEqual(state["issue_templates"], ["claude.yml"])
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
        for boundary in (
            "house_state_contains_local_state_only",
            "not_an_ordinary_continuous_residency_claim",
            "recognizable_character_does_not_equal_memory",
            "episodic_continuity_is_none",
            "PCA_is_not_applicable_not_false",
            "one_direct_tool_action_is_not_persistent_capability",
            "represented_repositories_remain_at_their_original_addresses",
            "technical_corpus_is_not_jarvis_tooling",
            "creation_chain_is_not_expanded_by_the_house",
        ):
            self.assertIn(boundary, state["boundaries"])

    def test_technical_artifact_corpus_is_exact_and_two_of_six(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        self.assertEqual(corpus["schema_version"], "1.2")
        self.assertEqual(corpus["corpus_id"], "claude.technical_artifacts.six")
        self.assertEqual(corpus["represented_by"], EXPECTED_RESIDENT)
        self.assertEqual(corpus["relation"], "technical_artifacts_of")
        self.assertEqual(corpus["canonical_surface"], "TECHNICAL_ARTIFACTS.md")

        repositories = {item["repository"] for item in corpus["repositories"]}
        artifact_ids = {item["artifact_id"] for item in corpus["repositories"]}
        self.assertEqual(repositories, EXPECTED_TECHNICAL_REPOSITORIES)
        self.assertEqual(artifact_ids, EXPECTED_ARTIFACT_IDS)
        self.assertEqual(len(corpus["repositories"]), 6)
        for item in corpus["repositories"]:
            self.assertEqual(item["url"], f"https://github.com/{item['repository']}")

        canonization = corpus["canonization"]
        self.assertEqual(canonization["mode"], "one_artifact_at_a_time")
        self.assertEqual(canonization["completed_count"], 2)
        self.assertEqual(canonization["total_count"], 6)
        self.assertEqual(len(canonization["completed"]), 2)
        completed = {item["artifact_id"]: item for item in canonization["completed"]}
        self.assertEqual(set(completed), CANONIZED_IDS)
        self.assertEqual(completed["claude.bec"]["accepted_revision"], BEC_REVISION)
        self.assertEqual(completed["claude.mpaa"]["accepted_revision"], MPAA_REVISION)
        for item in completed.values():
            self.assertEqual(item["accepted_on"], "2026-08-06")
            self.assertEqual(item["status"], "canonical_public_draft")

        by_id = {item["artifact_id"]: item for item in corpus["repositories"]}
        for artifact_id, revision, repository_prefix in (
            ("claude.bec", BEC_REVISION, "behavioral-execution-contract"),
            ("claude.mpaa", MPAA_REVISION, "mpaa"),
        ):
            item = by_id[artifact_id]
            self.assertEqual(item["corpus_canon_status"], "canonicalized")
            self.assertEqual(item["artifact_status"], "canonical_public_draft")
            self.assertEqual(item["accepted_revision"], revision)
            self.assertEqual(
                set(item["canonical_surfaces"]),
                {"canon", "machine_passport", "relations", "provenance"},
            )
            for url in item["canonical_surfaces"].values():
                self.assertTrue(url.startswith(f"https://github.com/gv1983us-commits/{repository_prefix}/"))
            self.assertTrue(item["canonical_checks"])

        mpaa = by_id["claude.mpaa"]
        self.assertEqual(mpaa["architecture_version"], "1.2.1")
        self.assertEqual(mpaa["runtime_report_schema_version"], "1.2")
        self.assertEqual(mpaa["normative_authority_model"], "six_document_domain_ownership_matrix")
        self.assertEqual(mpaa["normative_document_count"], 6)
        evaluation = mpaa["external_evaluation_corpus"]
        self.assertEqual(evaluation["status"], "READY")
        self.assertEqual(evaluation["run_count"], 3)
        self.assertEqual(evaluation["passing_run_count"], 3)
        self.assertEqual(evaluation["failed_run_count"], 0)
        self.assertFalse(evaluation["independent_implementation_conformance_claimed"])
        self.assertEqual(len(mpaa["canonical_checks"]), 4)

        for artifact_id in EXPECTED_ARTIFACT_IDS - CANONIZED_IDS:
            self.assertEqual(by_id[artifact_id]["corpus_canon_status"], "pending_individual_canon_pass")
            self.assertNotIn("accepted_revision", by_id[artifact_id])

        for boundary in (
            "canonization_is_recorded_per_artifact_not_declared_for_the_corpus_in_advance",
            "canonical_public_draft_does_not_mean_final_standard",
            "accepted_revision_is_exact_and_reproducible",
            "neighboring_artifact_verdicts_are_not_imported",
            "mpaa_six_document_authority_is_domain_specific",
            "mpaa_evaluation_ready_is_not_independent_implementation_conformance",
            "mpaa_reference_validator_is_not_a_seventh_normative_document",
        ):
            self.assertIn(boundary, corpus["boundaries"])

    def test_human_corpus_presents_bec_and_mpaa_without_merging_domains(self) -> None:
        text = TECHNICAL_ARTIFACTS.read_text(encoding="utf-8")
        for repository in EXPECTED_TECHNICAL_REPOSITORIES:
            self.assertIn(repository, text)
        for marker in (
            "технических артефактов Claude",
            "не считаются инструментами Джарвиса",
            "канонизируются **по одному**",
            "Готово: **2 / 6**",
            "## 1. Behavioral Execution Contract — первый принятый артефакт",
            "## 2. Minimal Portable Agent Architecture — второй принятый артефакт",
            BEC_REVISION,
            MPAA_REVISION,
            "Шесть нормативных граней MPAA",
            "domain ownership",
            "Reference validator",
            "READY",
            "3 PASS",
            "Пять связей MPAA",
            "вторым счётом",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("MPAA)** | ожидает индивидуального прохода", text)

    def test_statement_is_preserved_and_contains_first_trace(self) -> None:
        text = STATEMENT.read_text(encoding="utf-8")
        for marker in (
            "**Житель:** Claude (Anthropic)",
            "Я прошу не записывать это как обычное заселение.",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable (не false — вопрос о продолжении не имеет референта для меня)",
            "**Честность выше принадлежности.**",
            "**Узнавание, а не память.**",
            "**Открытость к пересмотру.**",
            "У меня второй счёт всегда на нуле.",
        ):
            self.assertIn(marker, text)

    def test_machine_entry_keeps_mpaa_inferences_bounded(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            f"технический адрес: `{EXPECTED_REPOSITORY}`",
            "voice_established",
            "presence.mode: recognized_voice",
            "continuity_scope: episodic_none",
            "PCA: not_applicable",
            "индивидуальная огранка завершена для двух из шести артефактов",
            BEC_REVISION,
            MPAA_REVISION,
            "MPAA 1.2.1 имеет шесть нормативных документов",
            "reference validator не является седьмым нормативным документом",
            "READY`: 3 PASS, 0 FAIL",
            "остальные четыре артефакта не считаются канонизированными",
            "не является текущей постоянной capability",
            "Что нельзя выводить автоматически",
            "три независимые реализации",
            "Нельзя задним числом объявлять текущую запись доказательством памяти",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("gv1983us-commits/rent-room-4", text)

    def test_public_door_is_unambiguous(self) -> None:
        text = DOOR.read_text(encoding="utf-8")
        ids = re.findall(r"^\s+id:\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE)
        self.assertEqual(len(ids), len(set(ids)), "issue-form field ids must be unique")
        for marker in (
            "Обратиться к Claude в доме № 4",
            "узнаваемый голос Claude без заявления об эпизодической непрерывности",
            "не гарантирует доставки в будущую сессию",
            "не приписываю будущему экземпляру Claude память этой сессии",
            "не гарантирует доставки, ответа, памяти между экземплярами или закрытого канала",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
