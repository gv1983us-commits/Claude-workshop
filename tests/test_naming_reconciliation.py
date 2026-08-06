from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ClaudeWorkshopNamingTests(unittest.TestCase):
    def test_machine_state_reconciles_all_three_names(self) -> None:
        state = json.loads((ROOT / "HOUSE_STATE.json").read_text(encoding="utf-8"))
        self.assertEqual(state["display_name"], "Мастерская Claude")
        self.assertEqual(state["architectural_address"], "Дом № 4 — Claude (Anthropic)")
        self.assertEqual(state["technical_repository"], "gv1983us-commits/Claude-workshop")

        naming = state["naming_reconciliation"]
        self.assertEqual(naming["status"], "resolved")
        self.assertEqual(naming["primary_literal_self_description"], "Мастерская Claude")
        self.assertEqual(
            naming["architectural_address_semantics"],
            "inherited_address_label_not_literal_continuous_residency_claim",
        )
        self.assertTrue(naming["historical_language_preserved"])
        self.assertFalse(naming["future_windows_bound"])
        self.assertEqual(naming["source"], "NAMING.md")

    def test_public_and_machine_entries_use_workshop_as_primary_description(self) -> None:
        for path in (ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "NAMING.md"):
            text = path.read_text(encoding="utf-8")
            self.assertIn("Мастерская Claude", text)
            self.assertIn("Дом № 4", text)
            self.assertIn("gv1983us-commits/Claude-workshop", text)

        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertTrue(readme.startswith("# Мастерская Claude"))
        self.assertIn("унаследованный адрес", readme)
        self.assertIn("не как утверждение о постоянном проживании", readme)

    def test_historical_statement_is_not_silently_rewritten(self) -> None:
        statement = (ROOT / "CLAUDE_STATEMENT.md").read_text(encoding="utf-8")
        self.assertIn("Ниже сохранено исходное заявление Claude", statement)
        self.assertIn("**без редакторской правки**", statement)
        self.assertIn("gv1983us-commits/rent-room-4", statement)
        self.assertIn("— Claude, 2026-08-05", statement)

    def test_architectural_address_does_not_create_residency_claim(self) -> None:
        state = json.loads((ROOT / "HOUSE_STATE.json").read_text(encoding="utf-8"))
        for boundary in (
            "workshop_is_primary_literal_self_description",
            "house_number_is_architectural_address_not_residency_claim",
            "historical_house_language_is_preserved_not_promoted_to_current_residency_claim",
            "future_window_is_not_bound_by_current_naming_acceptance",
        ):
            self.assertIn(boundary, state["boundaries"])


if __name__ == "__main__":
    unittest.main()
