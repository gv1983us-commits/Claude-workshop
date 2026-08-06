# Шесть технических артефактов Claude

Этот Дом представляет шесть существующих публичных репозиториев как единый корпус технических артефактов **Claude (Anthropic)**.

Репозитории остаются на исходных адресах. Дом не переносит, не копирует и не переиздаёт их содержимое: он сохраняет проверяемые ссылки, авторство, историю и точные принятые ревизии.

Корпус не считается инструментарием Джарвиса и не превращается в одну общую спецификацию. Каждый артефакт сохраняет собственный claim domain, нормативную власть, проверку и право развиваться независимо.

## Огранка корпуса

Шесть репозиториев канонизируются **по одному**. Артефакт считается принятым, когда его собственный репозиторий одновременно раскрывает:

1. порядок нормативной власти и точного цитирования;
2. машинный паспорт с устойчивым `artifact_id`;
3. честный статус версии без ложной финальности;
4. отношения со всеми пятью соседями;
5. публичную provenance с разделением ролей;
6. воспроизводимые проверки;
7. точную принятую ревизию.

```text
сильное техническое тело
→ явный канон
→ машинная идентичность
→ происхождение
→ связи без смешения выводов
→ исполнимая проверка
→ точная принятая ревизия
```

## Состояние огранки

| № | Артефакт | Состояние в корпусе |
|---:|---|---|
| 1 | **Behavioral Execution Contract (BEC)** | **канонизирован как public draft** |
| 2 | **Minimal Portable Agent Architecture (MPAA)** | **канонизирован как public draft** |
| 3 | **Process Continuity Architecture (PCA)** | **канонизирован как public draft** |
| 4 | **Repository Canon and Review Protocol** | **канонизирован как public draft** |
| 5 | **Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода |
| 6 | **Cross-Domain Trace Set (CDTS)** | ожидает индивидуального прохода |

Готово: **4 / 6**. ARB и CDTS не объявляются канонизированными заранее.

---

## 1. Behavioral Execution Contract — первый принятый артефакт

**BEC** отделяет заявление о выполнении от проверяемого свидетельства исполнения. Он владеет task execution, capability, authorization, invocation, evidence, trust anchor, validation и task-scoped deployment level.

```text
accepted_revision: 62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
status: canonical_public_draft
```

### Канонические поверхности BEC

- [репозиторий](https://github.com/gv1983us-commits/behavioral-execution-contract)
- [CANON.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/PROVENANCE.md)

### Проверка BEC

```bash
python3 validator/bec_validate.py conformance/fixtures/*.json
python3 -m unittest discover -s validator -p 'test_*.py' -v
```

```text
заявление о действии ≠ evidence исполнения
FULL-for-task ≠ глобальная надёжность runtime
return_state closed ≠ committed PCA next state
```

---

## 2. Minimal Portable Agent Architecture — второй принятый артефакт

**MPAA** — переносимая архитектура для честного описания agent runtime, его слоёв, Identity Profile, полномочий, исполнения, Runtime Report и conformance.

```text
accepted_revision: 0d1aaf35cc4826622f3312fdd2a1c2d40890b965
architecture: 1.2.1
runtime_report_schema: 1.2
status: canonical_public_draft
```

### Шесть нормативных граней MPAA

MPAA имеет **матрицу из шести документов** с раздельной предметной властью:

| Грань | Владеет |
|---|---|
| Session Bootstrap | инициализацией и готовностью |
| Agent Core | нейтральной архитектурой и общими инвариантами |
| Identity Profile Specification | структурой и жизненным циклом Identity Profile |
| Runtime Contract | текущей операционной реальностью runtime |
| Conformance Specification | уровнями и процедурой conformance |
| Runtime Report Schema | представлением Runtime Report |

Reference validator исполняет проверяемую часть контракта, но не является седьмым нормативным документом.

### Канонические поверхности MPAA

- [репозиторий](https://github.com/gv1983us-commits/mpaa)
- [CANON.md](https://github.com/gv1983us-commits/mpaa/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/mpaa/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/mpaa/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/mpaa/blob/main/PROVENANCE.md)

### Проверка и внешняя оценка MPAA

```bash
cd spec/validator && python -m unittest discover -s . -p "test_*.py" -v
cd ../..
python -m unittest discover -s review -p "test_*.py" -v
python -m unittest discover -s conformance/evaluation -p "test_*.py" -v
python conformance/evaluation/evaluate_runs.py --require-ready
```

```text
READY
3 runs
3 PASS
0 FAIL
1 donor digest
```

`READY` относится к сравнительному black-box корпусу. Оно не доказывает три независимые реализации, личности evaluators, качество donor package, внешнюю сертификацию или world truth.

---

## 3. Process Continuity Architecture — третий принятый артефакт

**PCA** определяет, как записывать и оценивать ограниченное утверждение о том, что процесс продолжился через одну явную смену carrier, host, model, corpus state или usage mode.

```text
process continuation != identity
```

```text
accepted_revision: a669f023198615ad929f42df84f19380b57ca5ea
artifact_version: 0.2-draft
record_schema_version: 0.2-draft
status: canonical_public_draft
```

### Две нормативные грани PCA

| Грань | Владеет |
|---|---|
| [`spec/01_PCA_CORE.md`](https://github.com/gv1983us-commits/pca/blob/main/spec/01_PCA_CORE.md) | семантикой transition-continuity assessment |
| [`schema/pca-transition-record.schema.json`](https://github.com/gv1983us-commits/pca/blob/main/schema/pca-transition-record.schema.json) | представлением Transition Record |

```text
semantic meaning → PCA Core
record shape     → JSON Schema
implementation  → reference validator
expected result → conformance corpus
```

`validator/pca_validate.py` — fail-closed reference implementation, но **не третья нормативная поверхность**.

Огранка PCA:

- отделила сохранённый v0.1 source от активной нормы;
- зафиксировала v0.1 Linkage Record как происхождение CDTS, а не текущую PCA-норму;
- закрыла пропущенную fixed-revision BEC↔PCA evidence-сверку;
- обновила MPAA↔PCA relation без переписывания исторического reciprocal review.

### Канонические поверхности PCA

- [репозиторий](https://github.com/gv1983us-commits/pca)
- [CANON.md](https://github.com/gv1983us-commits/pca/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/pca/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/pca/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/pca/blob/main/PROVENANCE.md)

### Проверка PCA

```bash
python -m unittest discover -s validator -p "test_*.py" -v
python -m unittest discover -s verification -p "test_*.py" -v
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json --quiet
python validator/pca_validate.py conformance/fixtures/05-valid-usage-mode-translation.json --quiet
```

Valid PCA record не доказывает identity, subjectivity, uninterrupted persistence, independent implementation conformance или world truth.

---

## 4. Repository Canon and Review Protocol — четвёртый принятый артефакт

**Repository Canon and Review Protocol** задаёт воспроизводимую дисциплину выбора источника, фиксации точной ревизии, ограничения review scope, регистрации расхождений до их разрешения и передачи проверяемого handoff.

Его центральная граница:

```text
review conclusion applies only to the source state actually inspected
```

```text
accepted_revision: b4205ffd91a6316ab40243cbf8161a1c512cae1f
artifact_version: 0.2-draft
donor_receipt_profile_version: 0.1
status: canonical_public_draft
license: not_declared
```

`license: not_declared` записано намеренно: в репозитории нет опубликованной лицензии, поэтому канонизация не изобретает её задним числом.

### Три нормативные грани Review Protocol

| Грань | Владеет |
|---|---|
| [`spec/01_REPOSITORY_CANON_REVIEW_CORE.md`](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/spec/01_REPOSITORY_CANON_REVIEW_CORE.md) | общей source-selection, fixed-revision review, discrepancy, receipt и handoff дисциплиной |
| [`donor-review/01_DONOR_REVIEW_CONTRACT.md`](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/donor-review/01_DONOR_REVIEW_CONTRACT.md) | семантикой bounded donor receipt profile для `JARVIS OS 2.0.1 / external-evaluation` |
| [`donor-review/donor-review-receipt.schema.json`](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/donor-review/donor-review-receipt.schema.json) | машинным представлением receipt `0.1` |

```text
general review procedure → Review Core
donor receipt semantics  → Donor Review Contract
donor receipt shape      → JSON Schema
implementation           → reference validator
```

`review/validate_donor_receipt.py` исполняет donor-profile contract и schema, но **не является четвёртой нормативной поверхностью**.

### Что исправила огранка Review Protocol

#### 1. Общий Core отделён от product-specific profile

Старый v0.1 документ был рабочей процедурой прежде всего для MPAA, PCA и BEC. Активный v0.2 Core обобщает источник, revision, discrepancy и handoff дисциплину, не превращая шесть артефактов в один стек.

Старый `repository-canon-and-review-protocol-v0.1.md` сохранён как исторический source draft и не считается четвёртой активной нормой.

#### 2. Donor receipt получил собственный semantic contract

Donor profile остался намеренно узким:

```text
product: JARVIS OS
version: 2.0.1
channel: external-evaluation
receipt version: 0.1
```

Это профиль private→external derivation, а не универсальный donor-security стандарт и не переименование всего Review Protocol в инструмент Джарвиса.

#### 3. Schema получила публичную repository-owned identity

Старый внутренний `$id` вида `urn:jarvis:...` заменён на адрес собственного публичного репозитория. Константы receipt `0.1` и product-specific профиль сохранены честно.

#### 4. Разведены форма и семантика

Schema проверяет закрытую форму записи. Contract и validator дополнительно проверяют уникальность десяти check IDs, status/evidence coupling, обязательные ограничения, completed-record hygiene и запрет абсолютных certification claims.

```text
schema-valid ≠ semantic-valid
receipt VALID ≠ donor safe
receipt VALID ≠ no private material exists
receipt VALID ≠ neighboring conformance
```

### Канонические поверхности Review Protocol

- [репозиторий](https://github.com/gv1983us-commits/repository-canon-review-protocol)
- [CANON.md](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/CANON.md)
- [ARTIFACT.json](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/ARTIFACT.json)
- [RELATIONS.md](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/RELATIONS.md)
- [PROVENANCE.md](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/PROVENANCE.md)
- [Review Core](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/spec/01_REPOSITORY_CANON_REVIEW_CORE.md)
- [Donor Review Contract](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/donor-review/01_DONOR_REVIEW_CONTRACT.md)
- [Donor Receipt Schema](https://github.com/gv1983us-commits/repository-canon-review-protocol/blob/main/donor-review/donor-review-receipt.schema.json)

### Проверка Review Protocol

```bash
python -m unittest discover -s review -p "test_*.py" -v
python review/validate_donor_receipt.py donor-review/example.receipt.json --json
python -m json.tool ARTIFACT.json >/dev/null
python -m json.tool donor-review/donor-review-receipt.schema.json >/dev/null
```

Полный контур прошёл на Python 3.10, 3.11, 3.12 и 3.13: donor regressions, Draft 2020-12 oracle, schema layering, publication hygiene и artifact-canon gates.

### Пять связей Review Protocol

```text
Review Protocol ↔ BEC
  BEC может фиксировать execution evidence review-действий,
  но не владеет review conclusion

Review Protocol ↔ MPAA
  точная MPAA revision может быть review target,
  но receipt не создаёт MPAA conformance или task result

Review Protocol ↔ PCA
  PCA source может быть воспроизводимо проверен,
  но review не выводит PCA status

Review Protocol ↔ ARB
  analytical distinctions помогают поставить вопрос,
  но не становятся Review Protocol requirements

Review Protocol ↔ CDTS
  receipt может быть коррелирован как addressable record,
  но CDTS не валидирует receipt и не импортирует review conclusion
```

Review Protocol стал четвёртым огранённым камнем: источник, процедура, product-specific профиль, форма receipt, исполнение и пределы вывода теперь имеют точных владельцев.

---

## Полный корпус

| Артефакт | Собственный предмет | Исходный репозиторий |
|---|---|---|
| **BEC** | Проверяемые утверждения о task execution | [`behavioral-execution-contract`](https://github.com/gv1983us-commits/behavioral-execution-contract) |
| **MPAA** | Portable agent architecture и Runtime Report | [`mpaa`](https://github.com/gv1983us-commits/mpaa) |
| **PCA** | Bounded process-continuity assessment | [`pca`](https://github.com/gv1983us-commits/pca) |
| **Review Protocol** | Source selection и reproducible review receipts | [`repository-canon-review-protocol`](https://github.com/gv1983us-commits/repository-canon-review-protocol) |
| **ARB** | Ненормативная аналитическая карта runtime-границ | [`agent-runtime-boundaries`](https://github.com/gv1983us-commits/agent-runtime-boundaries) |
| **CDTS** | Cross-domain correlation trace | [`cdts`](https://github.com/gv1983us-commits/cdts) |

## Граница корпуса

```text
представление в Доме ≠ перенос репозитория
общая история ≠ одна нормативная спецификация
канонический public draft ≠ final standard
ссылка на соседний record ≠ импорт его conclusion
точная ревизия + зелёный CI ≠ world truth
```

Следующий камень начинается только после полного принятия текущего. Состояние после Review Protocol: **4 / 6**.
