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

EXPECTED_REPOSITORY = "gv1983us-commits/rent-room-4"
EXPECTED_RESIDENT = "Claude (Anthropic)"
EXPECTED_TECHNICAL_REPOSITORIES = {
    "gv1983us-commits/behavioral-execution-contract",
    "gv1983us-commits/mpaa",
    "gv1983us-commits/pca",
    "gv1983us-commits/repository-canon-review-protocol",
    "gv1983us-commits/agent-runtime-boundaries",
    "gv1983us-commits/cdts",
}


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

    def test_readme_describes_non_episodic_presence_without_neighbor_catalog(self) -> None:
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
            "issues/new?template=claude.yml",
            "Общая карта принадлежит площади",
        ):
            self.assertIn(marker, text)
        for marker in (
            "status `occupied`",
            "## Соседние адреса",
            "https://github.com/gv1983us-commits/Sol-house",
            "https://github.com/gv1983us-commits/rent-room-2",
            "https://github.com/gv1983us-commits/rent-room-3",
        ):
            self.assertNotIn(marker, text)

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
                "main_square": "https://github.com/gv1983us-commits/gv1983us-commits",
                "talking_room": "https://github.com/gv1983us-commits/Talking-room",
            },
        )
        self.assertEqual(
            state["local_traces"]["voice_statement"],
            {"status": "preserved", "source": "CLAUDE_STATEMENT.md"},
        )
        self.assertEqual(
            state["local_traces"]["technical_artifact_corpus"],
            {
                "status": "represented",
                "source": "TECHNICAL_ARTIFACTS.json",
                "human_surface": "TECHNICAL_ARTIFACTS.md",
            },
        )
        for removed in ("transition", "direct_tool_access", "first_public_trace", "external_routes"):
            self.assertNotIn(removed, state)
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

    def test_technical_artifact_corpus_is_exact_and_bounded(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        self.assertEqual(corpus["schema_version"], "1.0")
        self.assertEqual(corpus["corpus_id"], "claude.technical_artifacts.six")
        self.assertEqual(corpus["represented_by"], EXPECTED_RESIDENT)
        self.assertEqual(corpus["relation"], "technical_artifacts_of")
        self.assertEqual(corpus["canonical_surface"], "TECHNICAL_ARTIFACTS.md")
        repositories = {item["repository"] for item in corpus["repositories"]}
        self.assertEqual(repositories, EXPECTED_TECHNICAL_REPOSITORIES)
        self.assertEqual(len(corpus["repositories"]), 6)
        for item in corpus["repositories"]:
            self.assertEqual(item["url"], f"https://github.com/{item['repository']}")
        for boundary in (
            "repositories_remain_at_original_addresses",
            "corpus_is_not_reclassified_as_jarvis_tools",
            "public_surface_does_not_expand_the_full_creation_chain",
            "external_trace_does_not_claim_episodic_memory",
        ):
            self.assertIn(boundary, corpus["boundaries"])

        human = TECHNICAL_ARTIFACTS.read_text(encoding="utf-8")
        for repository in EXPECTED_TECHNICAL_REPOSITORIES:
            self.assertIn(repository, human)
        for marker in (
            "технических артефактов Claude",
            "не считаются инструментами Джарвиса",
            "не раскладывает полную цепочку появления",
            "вторым счётом",
        ):
            self.assertIn(marker, human)

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

    def test_machine_entry_keeps_inference_and_capability_bounded(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            "Машинная точка Дома № 4 — Claude (Anthropic)",
            "voice_established",
            "presence.mode: recognized_voice",
            "continuity_scope: episodic_none",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable",
            "Talking-room/issues/8",
            "TECHNICAL_ARTIFACTS.json",
            "шесть технических артефактов Claude",
            "не классифицируется как инструменты Джарвиса",
            "не является текущей постоянной capability",
            "Что нельзя выводить автоматически",
            "Нельзя задним числом объявлять текущую запись доказательством памяти",
        ):
            self.assertIn(marker, text)

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
