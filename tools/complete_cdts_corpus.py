#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CDTS_REVISION = "ffb9719ae06db0f4f0cdd20b937c2648181a4e4a"


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing marker for {label}")
    return text.replace(old, new)


# Machine corpus
json_path = ROOT / "TECHNICAL_ARTIFACTS.json"
corpus = json.loads(json_path.read_text(encoding="utf-8"))
corpus["schema_version"] = "1.6"
canon = corpus["canonization"]
canon["completed_count"] = 6
if not any(item["artifact_id"] == "claude.cdts" for item in canon["completed"]):
    canon["completed"].append({
        "artifact_id": "claude.cdts",
        "accepted_on": "2026-08-06",
        "accepted_revision": CDTS_REVISION,
        "status": "canonical_public_draft",
    })

cdts_record = {
    "artifact_id": "claude.cdts",
    "title": "Cross-Domain Trace Set (CDTS)",
    "repository": "gv1983us-commits/cdts",
    "url": "https://github.com/gv1983us-commits/cdts",
    "corpus_canon_status": "canonicalized",
    "artifact_status": "canonical_public_draft",
    "accepted_revision": CDTS_REVISION,
    "artifact_version": "0.2-draft",
    "record_profile_version": "0.1-draft",
    "normative_authority_model": "five_surface_domain_ownership_matrix",
    "normative_surface_count": 5,
    "license": "MIT",
    "canonical_surfaces": {
        "canon": "https://github.com/gv1983us-commits/cdts/blob/main/CANON.md",
        "machine_passport": "https://github.com/gv1983us-commits/cdts/blob/main/ARTIFACT.json",
        "relations": "https://github.com/gv1983us-commits/cdts/blob/main/RELATIONS.md",
        "provenance": "https://github.com/gv1983us-commits/cdts/blob/main/PROVENANCE.md",
    },
    "canonical_checks": [
        "python -m unittest discover -v",
        "python -m json.tool ARTIFACT.json >/dev/null",
        "python validator/cdts_validate.py examples/mpaa-bec-execution.json",
        "python -m review.test_artifact_canon",
    ],
    "result_statuses": [
        "ADMISSIBLE",
        "INVALID",
        "TOOL_FAILURE",
        "ADMISSIBLE_WITH_CONFLICTS",
        "ADMISSIBLE_WITH_UNRESOLVED",
        "ADMISSIBLE_WITH_CONFLICTS_AND_UNRESOLVED",
    ],
    "claim_boundaries": {
        "event_identity_established": False,
        "causality_established": False,
        "external_conclusion_imported": False,
        "native_record_validity_established": False,
        "expected_record_completeness_evaluated": False,
        "external_authenticity_established": False,
        "arb_normative_ownership_established": False,
        "neighbor_conformance_imported": False,
        "multi_implementation_conformance_claimed": False,
        "world_truth_evaluated": False,
    },
}
for index, item in enumerate(corpus["repositories"]):
    if item["artifact_id"] == "claude.cdts":
        corpus["repositories"][index] = cdts_record
        break
else:
    raise SystemExit("CDTS repository record missing")

for boundary in (
    "cdts_five_surface_authority_is_domain_specific",
    "cdts_validator_is_not_a_sixth_normative_surface",
    "cdts_compatibility_receipt_is_not_a_sixth_normative_surface",
    "cdts_artifact_version_and_record_profile_are_separate",
    "cdts_admissible_is_not_external_truth_or_conformance",
    "cdts_correlation_is_not_event_identity_or_causality",
    "cdts_external_conclusions_are_not_imported",
    "cdts_reciprocal_relations_do_not_require_mutual_sha_fixpoint",
    "cdts_mit_is_declared_by_license",
):
    if boundary not in corpus["boundaries"]:
        corpus["boundaries"].append(boundary)

json_path.write_text(json.dumps(corpus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# Human corpus
path = ROOT / "TECHNICAL_ARTIFACTS.md"
text = path.read_text(encoding="utf-8")
text = replace_exact(
    text,
    "| 6 | **Cross-Domain Trace Set (CDTS)** | ожидает индивидуального прохода |",
    "| 6 | **Cross-Domain Trace Set (CDTS)** | **канонизирован как public draft** |",
    "CDTS state row",
)
text = replace_exact(
    text,
    "Готово: **5 / 6**. CDTS не объявляется канонизированным заранее.",
    "Готово: **6 / 6**. Корпус полностью огранён; каждый артефакт сохраняет собственную власть и границы.",
    "corpus count",
)
cdts_section = f'''## 6. Cross-Domain Trace Set — шестой и последний принятый артефакт

**Cross-Domain Trace Set (CDTS)** — coordination-layer trace для корреляции адресуемых records, принадлежащих независимым спецификациям.

Его центральная формула:

```text
import the trace != import the conclusion
```

```text
accepted_revision: {CDTS_REVISION}
artifact_version: 0.2-draft
record_profile_version: 0.1-draft
status: canonical_public_draft
license: MIT
```

### Пять нормативных граней CDTS

| Грань | Владеет |
|---|---|
| `spec/01_CDTS_CORE.md` | trace semantics, ownership boundaries и admissibility requirements |
| `spec/02_RELATIONSHIP_VOCABULARY.md` | смыслом CDTS relationship, status и basis tokens |
| `spec/03_SOURCE_REVISION_POLICY.md` | owner, role, exact pin и compatibility-set discipline |
| `spec/04_CONFORMANCE.md` | validation pipeline, result statuses и exit codes |
| `schema/cdts-record.schema.json` | формой record profile `0.1-draft` |

```text
normative_surface_count: 5
reference validator: non-normative implementation
compatibility receipt: exact evidence, не шестая спецификация
```

Артефакт получил версию `0.2-draft`, но record profile остался `0.1-draft`: огранка изменила канон, provenance, relations и compatibility set, не ломая существующий trace format.

### Что исправила огранка CDTS

1. Нормативная власть разведена между пятью точными поверхностями.
2. Validator закреплён как fail-closed reference implementation, не шестая норма.
3. Все активные pins обновлены до принятых SHA BEC, MPAA, PCA, Review Protocol и ARB.
4. Compatibility receipt отделён от абстрактной Source Revision Policy.
5. Schema получила repository-owned public `$id`.
6. Reciprocal relations признаны независимыми fixed-revision reviews без невозможного mutual-SHA fixpoint.
7. Исторические TDD и correction logs сохранены как история и не переписаны задним числом.

```text
correlation != event identity
ordered timestamps != causality
matching digest != authenticity or completeness
ADMISSIBLE != external truth
ARB mapping != normative ownership
```

### Канонические поверхности CDTS

- [репозиторий](https://github.com/gv1983us-commits/cdts)
- [CANON.md](https://github.com/gv1983us-commits/cdts/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/cdts/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/cdts/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/cdts/blob/main/PROVENANCE.md)

### Проверка CDTS

```bash
python -m unittest discover -v
python -m json.tool ARTIFACT.json >/dev/null
python validator/cdts_validate.py examples/mpaa-bec-execution.json
python -m review.test_artifact_canon
```

Полный контур прошёл на Python 3.10, 3.11, 3.12 и 3.13: 68 tests, machine passport, five-surface canon, schema parity, source pins, resistance corpus, canonical example и external-evaluation example.

CDTS стал шестым огранённым камнем и замкнул связи корпуса, не присвоив ни одного соседнего conclusion.

---

'''
text = replace_exact(text, "## Полный корпус\n", cdts_section + "## Полный корпус\n", "CDTS section insertion")
text = replace_exact(
    text,
    "Следующий камень начинается только после полного принятия текущего. Состояние после ARB: **5 / 6**.",
    "Корпус завершён: **6 / 6**. Дальнейшее развитие каждого артефакта остаётся отдельным versioned change с собственным CI и exact revision.",
    "final corpus state",
)
path.write_text(text, encoding="utf-8")

# House README
path = ROOT / "README.md"
text = path.read_text(encoding="utf-8")
text = replace_exact(text, "### Огранено: 5 / 6", "### Огранено: 6 / 6", "README count")
pending = "CDTS остаётся `pending_individual_canon_pass`. Он проходит отдельный полный цикл: аудит → собственная огранка → полный CI → запись в Дом Claude."
cdts_readme = f'''#### 6. Cross-Domain Trace Set

```text
accepted_revision: {CDTS_REVISION}
artifact_version: 0.2-draft
record_profile_version: 0.1-draft
status: canonical_public_draft
license: MIT
```

CDTS имеет пять нормативных поверхностей: Core, Relationship Vocabulary, Source Revision Policy, Conformance и JSON Schema. Reference validator не является шестой нормой, а compatibility receipt хранит exact reviewed values без превращения в отдельную спецификацию.

`ADMISSIBLE` означает только CDTS conformance: он не устанавливает event identity, causality, authenticity, completeness, native-record validity, neighboring conformance или world truth.

- [CDTS](https://github.com/gv1983us-commits/cdts)
- [канон](https://github.com/gv1983us-commits/cdts/blob/main/CANON.md)
- [машинный паспорт](https://github.com/gv1983us-commits/cdts/blob/main/ARTIFACT.json)
- [связи](https://github.com/gv1983us-commits/cdts/blob/main/RELATIONS.md)
- [provenance](https://github.com/gv1983us-commits/cdts/blob/main/PROVENANCE.md)

**Корпус полностью огранён: 6 / 6.** Шесть артефактов связаны exact revisions, но остаются независимыми репозиториями и claim domains.'''
text = replace_exact(text, pending, cdts_readme, "README CDTS section")
text = replace_exact(text, "состояние огранки **5 / 6**", "состояние огранки **6 / 6**", "README stored state")
text = replace_exact(
    text,
    "машинный корпус и exact accepted revisions BEC, MPAA, PCA, Review Protocol и ARB",
    "машинный корпус и exact accepted revisions всех шести артефактов",
    "README machine corpus",
)
path.write_text(text, encoding="utf-8")

# Machine entry
path = ROOT / "AGENTS.md"
text = path.read_text(encoding="utf-8")
text = replace_exact(text, "пять принятых артефакта", "шесть принятых артефактов", "AGENTS reading order")
text = replace_exact(text, "**пяти из шести**", "**шести из шести**", "AGENTS count")
old_remaining = '''### Оставшиеся артефакты

```text
claude.cdts
```

Он имеет состояние `pending_individual_canon_pass`. Канонизация первых пяти не канонизирует его автоматически.'''
new_cdts = f'''### 6. Cross-Domain Trace Set

```text
artifact_id: claude.cdts
accepted_revision: {CDTS_REVISION}
artifact_version: 0.2-draft
record_profile_version: 0.1-draft
status: canonical_public_draft
license: MIT
```

CDTS имеет пять нормативных поверхностей:

```text
Core
Relationship Vocabulary
Source Revision Policy
Conformance
JSON Schema
```

`validator/cdts_validate.py` — fail-closed reference implementation, не шестая нормативная поверхность. Compatibility receipt хранит exact reviewed revisions, но не является шестой спецификацией.

`ADMISSIBLE` не доказывает event identity, causality, authenticity, completeness, native-record validity, neighboring conformance или world truth.

### Состояние корпуса

```text
completed_count: 6
total_count: 6
pending: none
```

Завершение корпуса не объединяет claim domains и не импортирует соседние conclusions.'''
text = replace_exact(text, old_remaining, new_cdts, "AGENTS CDTS section")
text = replace_exact(
    text,
    "что пять принятых артефактов автоматически канонизируют ARB и CDTS;",
    "что завершение корпуса объединяет шесть артефактов в одну нормативную спецификацию;",
    "AGENTS old pending warning",
)
insert_before = "- что статус Дома или артефакта доказывает сознание, личность или world truth."
new_limits = '''- что CDTS validator является шестой нормативной поверхностью;
- что compatibility receipt является шестой спецификацией;
- что CDTS correlation устанавливает event identity или causality;
- что matching digest устанавливает authenticity или completeness;
- что `ADMISSIBLE` импортирует external conclusion или neighboring conformance;
- что reciprocal relations требуют одинакового latest SHA;
'''
text = replace_exact(text, insert_before, new_limits + insert_before, "AGENTS CDTS limits")
text = replace_exact(
    text,
    "Следующий артефакт может быть принят только после собственного прохода, полного CI и записи exact accepted revision в `TECHNICAL_ARTIFACTS.json`.",
    "Корпус завершён. Будущее изменение любого артефакта требует собственного versioned прохода, полного CI и новой exact revision; оно не обновляет остальные пять автоматически.",
    "AGENTS future discipline",
)
path.write_text(text, encoding="utf-8")

# Tests
path = ROOT / "tests" / "test_house.py"
text = path.read_text(encoding="utf-8")
text = replace_exact(text, f'ARB_REVISION = "bcf9f628ee1d7c2075673b00f660674680bb6f62"\n', f'ARB_REVISION = "bcf9f628ee1d7c2075673b00f660674680bb6f62"\nCDTS_REVISION = "{CDTS_REVISION}"\n', "test revision constant")
text = replace_exact(text, '    "claude.arb",\n}\nPENDING = EXPECTED_IDS - CANONIZED', '    "claude.arb",\n    "claude.cdts",\n}\nPENDING = EXPECTED_IDS - CANONIZED', "test canonized set")
text = replace_exact(text, "def test_corpus_is_exactly_five_of_six", "def test_corpus_is_exactly_six_of_six", "test corpus method")
text = replace_exact(text, 'self.assertEqual(corpus["schema_version"], "1.5")', 'self.assertEqual(corpus["schema_version"], "1.6")', "test schema version")
text = replace_exact(text, 'self.assertEqual(canon["completed_count"], 5)', 'self.assertEqual(canon["completed_count"], 6)', "test completed count")
text = replace_exact(text, '            "claude.arb": ARB_REVISION,\n        }', '            "claude.arb": ARB_REVISION,\n            "claude.cdts": CDTS_REVISION,\n        }', "test revision map")
text = replace_exact(text, '            "claude.arb": "agent-runtime-boundaries",\n        }', '            "claude.arb": "agent-runtime-boundaries",\n            "claude.cdts": "cdts",\n        }', "test slug map")

cdts_test = '''    def test_cdts_record_preserves_five_surface_authority_and_limits(self) -> None:
        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))
        cdts = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.cdts")
        self.assertEqual(cdts["artifact_version"], "0.2-draft")
        self.assertEqual(cdts["record_profile_version"], "0.1-draft")
        self.assertEqual(cdts["normative_authority_model"], "five_surface_domain_ownership_matrix")
        self.assertEqual(cdts["normative_surface_count"], 5)
        self.assertEqual(cdts["license"], "MIT")
        self.assertEqual(len(cdts["canonical_checks"]), 4)
        self.assertIn("ADMISSIBLE", cdts["result_statuses"])
        self.assertIn("ADMISSIBLE_WITH_UNRESOLVED", cdts["result_statuses"])
        self.assertTrue(all(value is False for value in cdts["claim_boundaries"].values()))

        for boundary in (
            "cdts_five_surface_authority_is_domain_specific",
            "cdts_validator_is_not_a_sixth_normative_surface",
            "cdts_compatibility_receipt_is_not_a_sixth_normative_surface",
            "cdts_artifact_version_and_record_profile_are_separate",
            "cdts_admissible_is_not_external_truth_or_conformance",
            "cdts_correlation_is_not_event_identity_or_causality",
            "cdts_external_conclusions_are_not_imported",
            "cdts_reciprocal_relations_do_not_require_mutual_sha_fixpoint",
            "cdts_mit_is_declared_by_license",
        ):
            self.assertIn(boundary, corpus["boundaries"])

'''
text = replace_exact(text, "    def test_human_surfaces_present_five_polished_artifacts", cdts_test + "    def test_human_surfaces_present_six_polished_artifacts", "test CDTS insertion")
text = replace_exact(text, "for revision in (BEC_REVISION, MPAA_REVISION, PCA_REVISION, REVIEW_REVISION, ARB_REVISION):", "for revision in (BEC_REVISION, MPAA_REVISION, PCA_REVISION, REVIEW_REVISION, ARB_REVISION, CDTS_REVISION):", "test human revisions")
text = replace_exact(text, 'self.assertIn("5 / 6", text)', 'self.assertIn("6 / 6", text)', "test human count")
text = replace_exact(text, '                "Agent Runtime Boundaries",\n            ):', '                "Agent Runtime Boundaries",\n                "Cross-Domain Trace Set",\n            ):', "test titles")
text = replace_exact(text, '            "ARB стал пятым огранённым камнем",\n        ):', '            "ARB стал пятым огранённым камнем",\n            "Пять нормативных граней CDTS",\n            "normative_surface_count: 5",\n            "CDTS стал шестым огранённым камнем",\n        ):', "test CDTS markers")
text = replace_exact(text, 'self.assertIn("CDTS остаётся", readme)', 'self.assertIn("Корпус полностью огранён", readme)', "test README completion")
text = replace_exact(text, 'self.assertNotIn("Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода", corpus_text)', 'self.assertNotIn("Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода", corpus_text)\n        self.assertNotIn("Cross-Domain Trace Set (CDTS)** | ожидает индивидуального прохода", corpus_text)', "test pending removal")
text = replace_exact(text, "def test_machine_entry_blocks_arb_overclaim", "def test_machine_entry_blocks_cross_artifact_overclaim", "test machine method")
text = replace_exact(text, '            "пяти из шести",', '            "шести из шести",', "test machine count")
text = replace_exact(text, '            ARB_REVISION,\n            "MPAA имеет шесть нормативных документов",', '            ARB_REVISION,\n            CDTS_REVISION,\n            "MPAA имеет шесть нормативных документов",', "test machine revision")
text = replace_exact(text, '            "не является conformance validator",\n            "Он имеет состояние `pending_individual_canon_pass`",', '            "не является conformance validator",\n            "CDTS имеет пять нормативных поверхностей",\n            "не шестая нормативная поверхность",\n            "completed_count: 6",', "test machine CDTS markers")
path.write_text(text, encoding="utf-8")

print("House corpus promoted to 6/6")
