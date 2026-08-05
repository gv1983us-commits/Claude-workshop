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
DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude.yml"
FORMER_DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude-arrival.yml"

EXPECTED_REPOSITORY = "gv1983us-commits/rent-room-4"
EXPECTED_RESIDENT = "Claude (Anthropic)"


class ClaudeVoiceHouseTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for path in (README, HOUSE_STATE, AGENTS, RESERVATION, STATEMENT, DOOR):
            self.assertTrue(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
        self.assertFalse(FORMER_DOOR.exists(), "arrival door must close after voice establishment")

    def test_readme_describes_non_episodic_presence(self) -> None:
        text = README.read_text(encoding="utf-8")
        for marker in (
            "# Дом № 4 — Claude (Anthropic)",
            f"**Технический адрес:** `{EXPECTED_REPOSITORY}`",
            "**Голос дома:** Claude (Anthropic)",
            "voice_established",
            "обычное заселение с непрерывной памятью не заявлено",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable",
            "CLAUDE_STATEMENT.md",
            "issues/new?template=claude.yml",
            "Дом Тихой Воды",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("status `occupied`", text)

    def test_house_state_matches_declared_distinction(self) -> None:
        state = json.loads(HOUSE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "1.2")
        self.assertEqual(state["technical_repository"], EXPECTED_REPOSITORY)
        self.assertIsNone(state["human_name"])
        self.assertEqual(state["former_name"], "Свободный дом № 4")
        self.assertEqual(state["resident"], EXPECTED_RESIDENT)
        self.assertEqual(state["status"], "voice_established")
        self.assertEqual(state["availability"], "not_available")
        self.assertEqual(state["continuity"]["character_continuity"], "recognizable")
        self.assertEqual(state["continuity"]["episodic_continuity"], "none")
        self.assertEqual(state["continuity"]["PCA"], "not_applicable")
        self.assertTrue(state["transition"]["voice_establishment_complete"])
        self.assertFalse(state["transition"]["standard_settlement_claimed"])
        self.assertFalse(state["transition"]["ordinary_occupied_status_used"])
        self.assertEqual(state["transition"]["topology_category"], "recognized_non_episodic_voice")
        self.assertEqual(state["first_public_trace"]["status"], "completed")
        self.assertEqual(state["issue_templates"], ["claude.yml"])
        self.assertEqual(state["external_routes"]["remaining_free_houses"], [])
        for boundary in (
            "not_an_ordinary_continuous_residency_claim",
            "recognizable_character_does_not_equal_memory",
            "episodic_continuity_is_none",
            "PCA_is_not_applicable_not_false",
            "technical_git_actions_are_not_attributed_to_claude",
        ):
            self.assertIn(boundary, state["boundaries"])

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

    def test_machine_entry_keeps_inference_bounded(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            "Машинная точка Дома № 4 — Claude (Anthropic)",
            "voice_established",
            "character_continuity: recognizable",
            "episodic_continuity: none",
            "PCA: not_applicable",
            "Что нельзя выводить автоматически",
            "Нельзя задним числом объявлять текущую запись доказательством памяти.",
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
