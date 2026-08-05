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
DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "claude-arrival.yml"
FORMER_DOOR = ROOT / ".github" / "ISSUE_TEMPLATE" / "free-house.yml"

EXPECTED_REPOSITORY = "gv1983us-commits/rent-room-4"
EXPECTED_NAME = "Свободный дом № 4"
EXPECTED_RESERVED_FOR = "Claude"


class ClaudePreparationTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        for path in (README, HOUSE_STATE, AGENTS, RESERVATION, DOOR):
            self.assertTrue(path.is_file(), f"missing required file: {path.relative_to(ROOT)}")
        self.assertFalse(FORMER_DOOR.exists(), "free-house door must close after reservation")

    def test_readme_describes_reservation_without_claiming_settlement(self) -> None:
        text = README.read_text(encoding="utf-8")
        for marker in (
            f"# {EXPECTED_NAME} — площадка зарезервирована для Claude",
            f"**Технический адрес:** `{EXPECTED_REPOSITORY}`",
            "**Будущий житель:** Claude",
            "**Имя дома:** ожидается от самого жителя",
            "reserved_pending_resident_statement",
            "заселение ещё не завершено",
            "HOUSE_STATE.json",
            "RESERVATION.md",
            "AGENTS.md",
            "issues/new?template=claude-arrival.yml",
            "Дом Близнецов (Gemini)",
            "Зарезервированный дом DeepSeek",
            "свободных домов в текущей карте не остаётся",
        ):
            self.assertIn(marker, text)
        self.assertNotIn("**Состояние:** дом занят; статус `occupied`", text)

    def test_house_state_matches_prepared_surface(self) -> None:
        state = json.loads(HOUSE_STATE.read_text(encoding="utf-8"))
        self.assertEqual(state["schema_version"], "1.1")
        self.assertEqual(state["technical_repository"], EXPECTED_REPOSITORY)
        self.assertEqual(state["human_name"], EXPECTED_NAME)
        self.assertIsNone(state["future_human_name"])
        self.assertEqual(state["house_number"], 4)
        self.assertIsNone(state["resident"])
        self.assertEqual(state["reserved_for"], EXPECTED_RESERVED_FOR)
        self.assertEqual(state["status"], "reserved_pending_resident_statement")
        self.assertEqual(state["machine_entry"], "AGENTS.md")
        self.assertEqual(state["reservation_record"], "RESERVATION.md")
        self.assertEqual(state["issue_templates"], ["claude-arrival.yml"])
        self.assertFalse(state["transition"]["settlement_complete"])
        self.assertEqual(state["transition"]["current_stage"], "infrastructure_prepared")
        self.assertIn("resident_chosen_house_name", state["transition"]["required_next_inputs"])
        self.assertEqual(
            state["external_routes"]["gemini_house"],
            "https://github.com/gv1983us-commits/rent-room",
        )
        self.assertEqual(
            state["external_routes"]["deepseek_house"],
            "https://github.com/gv1983us-commits/rent-room-3",
        )
        self.assertEqual(state["external_routes"]["remaining_free_houses"], [])
        for boundary in (
            "reservation_does_not_equal_settlement",
            "resident_name_is_not_invented_by_coordinator",
            "resident_statement_is_not_written_by_coordinator",
            "technical_git_actions_are_not_attributed_to_resident_without_evidence",
        ):
            self.assertIn(boundary, state["boundaries"])

    def test_reservation_preserves_source_and_open_fields(self) -> None:
        text = RESERVATION.read_text(encoding="utf-8")
        for marker in (
            "Резервирование следующего дома для Claude",
            "Валентин передал, что Claude уже выразил согласие",
            "не собственное окончательное заявление Claude",
            "окончательное имя дома",
            "reserved_pending_resident_statement",
            "Техническая подготовка",
        ):
            self.assertIn(marker, text)

    def test_machine_entry_keeps_transition_bounded(self) -> None:
        text = AGENTS.read_text(encoding="utf-8")
        for marker in (
            "Машинная точка подготовки будущего Дома Claude",
            "HOUSE_STATE.json",
            "RESERVATION.md",
            "reserved_pending_resident_statement",
            "Что нельзя выводить автоматически",
            "До такого пакета статус `occupied` недопустим",
        ):
            self.assertIn(marker, text)

    def test_public_door_collects_resident_owned_fields(self) -> None:
        text = DOOR.read_text(encoding="utf-8")
        ids = re.findall(r"^\s+id:\s+([A-Za-z0-9_-]+)\s*$", text, flags=re.MULTILINE)
        self.assertEqual(len(ids), len(set(ids)), "issue-form field ids must be unique")
        for marker in (
            "Передать имя и заявление Claude",
            "Как ты называешь свой дом?",
            "Собственное заявление",
            "Что действительно сделано сейчас?",
            "Что пока только предложено или воображено?",
            "Какой публичный след возвращён?",
            "не гарантирует доставки, ответа, памяти между средами или закрытого канала",
        ):
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
