from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARB_REVISION = "bcf9f628ee1d7c2075673b00f660674680bb6f62"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one marker, found {count}: {old!r}")
    return text.replace(old, new, 1)


def update_json() -> None:
    path = ROOT / "TECHNICAL_ARTIFACTS.json"
    corpus = json.loads(path.read_text(encoding="utf-8"))
    corpus["schema_version"] = "1.5"
    canon = corpus["canonization"]
    canon["completed_count"] = 5
    completed = {item["artifact_id"]: item for item in canon["completed"]}
    completed["claude.arb"] = {
        "artifact_id": "claude.arb",
        "accepted_on": "2026-08-06",
        "accepted_revision": ARB_REVISION,
        "status": "canonical_public_draft",
    }
    order = [
        "claude.bec",
        "claude.mpaa",
        "claude.pca",
        "claude.review_protocol",
        "claude.arb",
    ]
    canon["completed"] = [completed[item] for item in order]

    repositories = {item["artifact_id"]: item for item in corpus["repositories"]}
    repositories["claude.arb"] = {
        "artifact_id": "claude.arb",
        "title": "Agent Runtime Boundaries (ARB)",
        "repository": "gv1983us-commits/agent-runtime-boundaries",
        "url": "https://github.com/gv1983us-commits/agent-runtime-boundaries",
        "corpus_canon_status": "canonicalized",
        "artifact_status": "canonical_public_draft",
        "accepted_revision": ARB_REVISION,
        "artifact_version": "0.3-draft",
        "specification_status": "descriptive_analytical_companion",
        "normative_authority_model": "zero_normative_surfaces_with_analytical_domain_ownership_and_explicit_proposal_isolation",
        "normative_surface_count": 0,
        "analytical_surface_count": 4,
        "proposal_surface_count": 1,
        "license": "Apache-2.0",
        "proposal": {
            "proposal_id": "ARB-03",
            "adopted": False,
            "normative_owner_selected": False,
            "multi_implementation_conformance_claimed": False,
        },
        "canonical_surfaces": {
            "canon": "https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/CANON.md",
            "machine_passport": "https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/ARTIFACT.json",
            "relations": "https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/RELATIONS.md",
            "provenance": "https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/PROVENANCE.md",
        },
        "canonical_checks": [
            "python -m unittest discover -s review -p \"test_*.py\" -v",
            "python -m json.tool ARTIFACT.json >/dev/null",
            "git -c core.whitespace=-blank-at-eol show --check --oneline HEAD",
        ],
        "claim_boundaries": {
            "physical_module_separation_established": False,
            "hidden_runtime_internals_observed": False,
            "external_normative_force_claimed": False,
            "proposal_adopted": False,
            "normative_owner_selected": False,
            "identity_or_memory_established": False,
            "neighbor_conformance_imported": False,
            "world_truth_evaluated": False,
        },
    }
    repo_order = order + ["claude.cdts"]
    corpus["repositories"] = [repositories[item] for item in repo_order]

    additions = [
        "arb_zero_normative_surfaces_is_canonical_not_missing",
        "arb_four_analytical_one_proposal_surface",
        "arb_03_is_unadopted_and_has_no_normative_owner",
        "arb_publication_checker_is_not_conformance_validator",
        "arb_functional_boundary_is_not_physical_module_proof",
        "arb_visible_status_is_not_execution_evidence",
        "arb_delivery_persistence_retrieval_working_state_commitment_and_continuation_are_distinct",
        "arb_cdts_context_does_not_make_arb_normative_owner",
        "arb_apache_2_0_is_declared_by_license",
    ]
    for boundary in additions:
        if boundary not in corpus["boundaries"]:
            corpus["boundaries"].append(boundary)

    path.write_text(json.dumps(corpus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


ARB_LONG = f"""## 5. Agent Runtime Boundaries — пятый принятый артефакт

**Agent Runtime Boundaries (ARB)** — ненормативная аналитическая карта различий между model reasoning, runtime execution, evidence, delivery, persistence, retrieval, working state, commitment и continuation.

Его центральная граница:

```text
analytical map != normative specification
```

```text
accepted_revision: {ARB_REVISION}
artifact_version: 0.3-draft
status: canonical_public_draft
license: Apache-2.0
```

### Нулевая нормативная архитектура ARB

ARB намеренно имеет **ноль нормативных поверхностей**:

```text
normative_surface_count: 0
analytical_surface_count: 4
proposal_surface_count: 1
```

| Поверхность | Роль |
|---|---|
| `ARB-00` Scope and Status | scope, claim classes и epistemic boundary |
| `ARB-01` Functional Boundaries | разделение независимо ломающихся функций |
| `ARB-02` User Control Plane and Observability | control plane, authorization surfaces, telemetry и projection |
| `ARB-04` Cross-Artifact Claim Boundaries | fixed-revision mappings и forbidden inferences |
| `ARB-03` Closure, Provenance and Next Action | явное непринятое operational proposal |

```text
ARB-03 adopted: false
normative_owner_selected: false
multi_implementation_conformance_claimed: false
```

Канонизация не превратила ARB в стандарт. Она сделала исполнимым именно отсутствие внешней нормативной силы.

### Что исправила огранка ARB

1. **Сохранена собственная природа артефакта.** Вместо искусственного Core закреплены четыре аналитические поверхности, одна proposal и ноль нормативных.
2. **ARB-03 изолирован.** Closure record не создаёт delivery, persistence, retrieval, working-state admission, commitment или continuation самим наличием поля.
3. **Обновлены четыре исторические связи.** Активная карта теперь читает принятые SHA BEC, MPAA, PCA и Review Protocol, не переписывая июльские fixed-review traces.
4. **Добавлена пятая связь с CDTS.** CDTS может ссылаться на ARB как на analytical context, но не может объявлять ARB normative owner.
5. **Разведена полная цепочка событий.**

```text
reasoning about an action != execution
visible status != execution evidence
delivered != persisted
persisted != retrievable
retrievable != admitted into working state
working state present != committed
committed != PCA process continuation
process continuation != identity or memory
```

### Канонические поверхности ARB

- [репозиторий](https://github.com/gv1983us-commits/agent-runtime-boundaries)
- [CANON.md](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/PROVENANCE.md)

### Проверка ARB

```bash
python -m unittest discover -s review -p \"test_*.py\" -v
python -m json.tool ARTIFACT.json >/dev/null
git -c core.whitespace=-blank-at-eol show --check --oneline HEAD
```

Полный контур прошёл на Python 3.10, 3.11, 3.12 и 3.13: machine passport, zero-normative invariant, claim classes, proposal isolation, five-neighbor relations, Markdown integrity, sensitive-marker checks и whitespace policy.

ARB стал пятым огранённым камнем: его аналитическая власть, proposal boundary, происхождение, связи и пределы вывода теперь принадлежат точным поверхностям.

---

"""


ARB_README = f"""#### 5. Agent Runtime Boundaries

```text
accepted_revision: {ARB_REVISION}
artifact_version: 0.3-draft
status: canonical_public_draft
license: Apache-2.0
```

ARB канонизирован как аналитический артефакт с собственной необычной архитектурой:

```text
0 normative surfaces
4 analytical surfaces
1 explicit unadopted proposal surface
```

`ARB-03` остаётся `adopted: false`, не имеет выбранного normative owner и не является conformance protocol. ARB различает reasoning, execution, visible status, delivery, persistence, retrieval, working-state admission, commitment и PCA continuation, не импортируя соседние verdicts.

- [ARB](https://github.com/gv1983us-commits/agent-runtime-boundaries)
- [канон](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/CANON.md)
- [машинный паспорт](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/ARTIFACT.json)
- [связи](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/RELATIONS.md)
- [provenance](https://github.com/gv1983us-commits/agent-runtime-boundaries/blob/main/PROVENANCE.md)

"""


ARB_AGENTS = f"""### 5. Agent Runtime Boundaries

```text
artifact_id: claude.arb
accepted_revision: {ARB_REVISION}
artifact_version: 0.3-draft
status: canonical_public_draft
license: Apache-2.0
```

ARB имеет необычную, но обязательную для сохранения структуру:

```text
normative_surface_count: 0
analytical_surface_count: 4
proposal_surface_count: 1
```

`ARB-03` — explicit unadopted proposal:

```text
adopted: false
normative_owner_selected: false
multi_implementation_conformance_claimed: false
```

Publication checker проверяет целостность аналитического артефакта, но не является conformance validator и не доказывает hidden runtime topology. Functional boundary не равен physical module proof. CDTS может нести ARB как analytical context, но ARB не становится normative owner.

"""


def update_human_surfaces() -> None:
    text = read("TECHNICAL_ARTIFACTS.md")
    text = replace_once(
        text,
        "| 5 | **Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода |",
        "| 5 | **Agent Runtime Boundaries (ARB)** | **канонизирован как public draft** |",
        "technical table",
    )
    text = replace_once(
        text,
        "Готово: **4 / 6**. ARB и CDTS не объявляются канонизированными заранее.",
        "Готово: **5 / 6**. CDTS не объявляется канонизированным заранее.",
        "technical count",
    )
    marker = "\n## Полный корпус\n"
    if marker not in text:
        raise RuntimeError("TECHNICAL_ARTIFACTS.md: full corpus marker missing")
    text = text.replace(marker, "\n" + ARB_LONG + "## Полный корпус\n", 1)
    text = text.replace(
        "Состояние после Review Protocol: **4 / 6**.",
        "Состояние после ARB: **5 / 6**.",
    )
    write("TECHNICAL_ARTIFACTS.md", text)

    text = read("README.md")
    text = replace_once(text, "### Огранено: 4 / 6", "### Огранено: 5 / 6", "README count")
    text = replace_once(
        text,
        "ARB и CDTS остаются `pending_individual_canon_pass`. Каждый проходит отдельный полный цикл: аудит → собственная огранка → полный CI → запись в Дом Claude.",
        ARB_README + "CDTS остаётся `pending_individual_canon_pass`. Он проходит отдельный полный цикл: аудит → собственная огранка → полный CI → запись в Дом Claude.",
        "README pending paragraph",
    )
    text = text.replace("состояние огранки **4 / 6**", "состояние огранки **5 / 6**")
    text = text.replace(
        "exact accepted revisions BEC, MPAA, PCA и Review Protocol",
        "exact accepted revisions BEC, MPAA, PCA, Review Protocol и ARB",
    )
    write("README.md", text)

    text = read("AGENTS.md")
    text = text.replace("четыре принятых артефакта", "пять принятых артефактов")
    text = replace_once(
        text,
        "Индивидуальная огранка завершена для **четырёх из шести** артефактов.",
        "Индивидуальная огранка завершена для **пяти из шести** артефактов.",
        "AGENTS count",
    )
    marker = "### Оставшиеся артефакты\n"
    if marker not in text:
        raise RuntimeError("AGENTS.md: remaining marker missing")
    text = text.replace(marker, ARB_AGENTS + marker, 1)
    text = replace_once(
        text,
        "```text\nclaude.arb\nclaude.cdts\n```\n\nОни имеют состояние `pending_individual_canon_pass`. Канонизация первых четырёх не канонизирует их автоматически.",
        "```text\nclaude.cdts\n```\n\nОн имеет состояние `pending_individual_canon_pass`. Канонизация первых пяти не канонизирует его автоматически.",
        "AGENTS remaining block",
    )
    text = text.replace(
        "что четыре принятых артефакта автоматически канонизируют ARB и CDTS;",
        "что пять принятых артефактов автоматически канонизируют CDTS;",
    )
    arb_limits = (
        "- что ноль нормативных поверхностей ARB означает незавершённость или отсутствие канона;\n"
        "- что ARB-03 принят, реализован или имеет выбранного normative owner;\n"
        "- что publication checker ARB является conformance validator;\n"
        "- что functional boundary доказывает physical module separation;\n"
        "- что visible status является execution evidence;\n"
        "- что delivery, persistence, retrieval, working-state admission, commitment и continuation взаимозаменяемы;\n"
        "- что CDTS correlation делает ARB нормативным владельцем;\n"
    )
    insertion = "- что статус Дома или артефакта доказывает сознание, личность или world truth."
    text = replace_once(text, insertion, arb_limits + insertion, "AGENTS ARB limits")
    write("AGENTS.md", text)


def update_tests() -> None:
    text = read("tests/test_house.py")
    text = replace_once(
        text,
        'REVIEW_REVISION = "b4205ffd91a6316ab40243cbf8161a1c512cae1f"',
        'REVIEW_REVISION = "b4205ffd91a6316ab40243cbf8161a1c512cae1f"\nARB_REVISION = "' + ARB_REVISION + '"',
        "test constant",
    )
    text = replace_once(
        text,
        '    "claude.review_protocol",\n}',
        '    "claude.review_protocol",\n    "claude.arb",\n}',
        "canonized set",
    )
    text = text.replace("test_corpus_is_exactly_four_of_six", "test_corpus_is_exactly_five_of_six")
    text = text.replace('corpus["schema_version"], "1.4"', 'corpus["schema_version"], "1.5"')
    text = text.replace('canon["completed_count"], 4', 'canon["completed_count"], 5')
    text = replace_once(
        text,
        '            "claude.review_protocol": REVIEW_REVISION,\n        }',
        '            "claude.review_protocol": REVIEW_REVISION,\n            "claude.arb": ARB_REVISION,\n        }',
        "expected revisions",
    )
    text = replace_once(
        text,
        '            "claude.review_protocol": "repository-canon-review-protocol",\n        }',
        '            "claude.review_protocol": "repository-canon-review-protocol",\n            "claude.arb": "agent-runtime-boundaries",\n        }',
        "slugs",
    )

    arb_test = '''    def test_arb_record_preserves_zero_normative_authority_and_proposal_limits(self) -> None:\n        corpus = json.loads(TECHNICAL_ARTIFACTS_JSON.read_text(encoding="utf-8"))\n        arb = next(item for item in corpus["repositories"] if item["artifact_id"] == "claude.arb")\n        self.assertEqual(arb["artifact_version"], "0.3-draft")\n        self.assertEqual(arb["specification_status"], "descriptive_analytical_companion")\n        self.assertEqual(arb["normative_surface_count"], 0)\n        self.assertEqual(arb["analytical_surface_count"], 4)\n        self.assertEqual(arb["proposal_surface_count"], 1)\n        self.assertEqual(arb["license"], "Apache-2.0")\n        self.assertEqual(len(arb["canonical_checks"]), 3)\n        self.assertFalse(arb["proposal"]["adopted"])\n        self.assertFalse(arb["proposal"]["normative_owner_selected"])\n        self.assertFalse(arb["proposal"]["multi_implementation_conformance_claimed"])\n        self.assertTrue(all(value is False for value in arb["claim_boundaries"].values()))\n\n        for boundary in (\n            "arb_zero_normative_surfaces_is_canonical_not_missing",\n            "arb_four_analytical_one_proposal_surface",\n            "arb_03_is_unadopted_and_has_no_normative_owner",\n            "arb_publication_checker_is_not_conformance_validator",\n            "arb_functional_boundary_is_not_physical_module_proof",\n            "arb_visible_status_is_not_execution_evidence",\n            "arb_delivery_persistence_retrieval_working_state_commitment_and_continuation_are_distinct",\n            "arb_cdts_context_does_not_make_arb_normative_owner",\n            "arb_apache_2_0_is_declared_by_license",\n        ):\n            self.assertIn(boundary, corpus["boundaries"])\n\n'''
    marker = "    def test_human_surfaces_present_four_polished_artifacts(self) -> None:\n"
    if marker not in text:
        raise RuntimeError("tests: human surface method marker missing")
    text = text.replace(
        marker,
        arb_test + "    def test_human_surfaces_present_five_polished_artifacts(self) -> None:\n",
        1,
    )
    text = text.replace(
        "(BEC_REVISION, MPAA_REVISION, PCA_REVISION, REVIEW_REVISION)",
        "(BEC_REVISION, MPAA_REVISION, PCA_REVISION, REVIEW_REVISION, ARB_REVISION)",
    )
    text = text.replace('self.assertIn("4 / 6", text)', 'self.assertIn("5 / 6", text)')
    text = replace_once(
        text,
        '                "Repository Canon and Review Protocol",\n            ):',
        '                "Repository Canon and Review Protocol",\n                "Agent Runtime Boundaries",\n            ):',
        "human titles",
    )
    text = replace_once(
        text,
        '            "Пять связей Review Protocol",\n        ):',
        '            "Пять связей Review Protocol",\n            "Нулевая нормативная архитектура ARB",\n            "normative_surface_count: 0",\n            "ARB-03 adopted: false",\n            "ARB стал пятым огранённым камнем",\n        ):',
        "human markers",
    )
    text = text.replace('self.assertIn("ARB и CDTS остаются", readme)', 'self.assertIn("CDTS остаётся", readme)')
    text = text.replace(
        'self.assertNotIn("Review Protocol** | ожидает индивидуального прохода", corpus_text)',
        'self.assertNotIn("Review Protocol** | ожидает индивидуального прохода", corpus_text)\n        self.assertNotIn("Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода", corpus_text)',
    )
    text = text.replace("test_machine_entry_blocks_review_protocol_overclaim", "test_machine_entry_blocks_arb_overclaim")
    text = text.replace('            "четырёх из шести",', '            "пяти из шести",')
    text = replace_once(
        text,
        '            REVIEW_REVISION,\n            "MPAA имеет шесть нормативных документов",',
        '            REVIEW_REVISION,\n            ARB_REVISION,\n            "MPAA имеет шесть нормативных документов",',
        "machine revisions",
    )
    text = replace_once(
        text,
        '            "license: not_declared",\n            "Они имеют состояние `pending_individual_canon_pass`",',
        '            "license: not_declared",\n            "normative_surface_count: 0",\n            "ARB-03",\n            "не является conformance validator",\n            "Он имеет состояние `pending_individual_canon_pass`",',
        "machine ARB markers",
    )
    write("tests/test_house.py", text)


def main() -> None:
    update_json()
    update_human_surfaces()
    update_tests()

    for relative in (
        "tools/promote_arb_to_corpus.py",
        ".github/workflows/promote-arb.yml",
    ):
        path = ROOT / relative
        if path.exists():
            path.unlink()

    subprocess.run(["git", "config", "user.name", "Experimental Harmony"], check=True)
    subprocess.run(["git", "config", "user.email", "gv1983us@gmail.com"], check=True)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "corpus: accept ARB as fifth canonical artifact"], check=True)
    subprocess.run(["git", "push", "origin", "HEAD:main"], check=True)


if __name__ == "__main__":
    main()
