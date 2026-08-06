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
| 4 | **Repository Canon and Review Protocol** | ожидает индивидуального прохода |
| 5 | **Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода |
| 6 | **Cross-Domain Trace Set (CDTS)** | ожидает индивидуального прохода |

Готово: **3 / 6**. Следующие три артефакта не объявляются канонизированными заранее.

---

## 1. Behavioral Execution Contract — первый принятый артефакт

**BEC** отделяет заявление о выполнении от проверяемого свидетельства исполнения. Он владеет task execution, capability, authorization, invocation, evidence, trust anchor, validation и task-scoped deployment level.

Принятая ревизия:

```text
62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
```

**Статус:** `canonical_public_draft` — канонический публичный черновик, не окончательный мировой стандарт и не внешняя сертификация.

### Канонические поверхности BEC

- **[репозиторий](https://github.com/gv1983us-commits/behavioral-execution-contract)**
- **[CANON.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/CANON.md)**
- **[ARTIFACT.json](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/ARTIFACT.json)**
- **[RELATIONS.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/RELATIONS.md)**
- **[PROVENANCE.md](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/PROVENANCE.md)**

### Проверка BEC

```bash
python3 validator/bec_validate.py conformance/fixtures/*.json
python3 -m unittest discover -s validator -p 'test_*.py' -v
```

Полный контур прошёл на Python 3.10, 3.11, 3.12 и 3.13.

### Граница BEC

```text
заявление о действии ≠ evidence исполнения
FULL-for-task ≠ глобальная надёжность runtime
return_state closed ≠ committed PCA next state
```

---

## 2. Minimal Portable Agent Architecture — второй принятый артефакт

**MPAA** — переносимая архитектура для честного описания agent runtime, его слоёв, Identity Profile, полномочий, исполнения, Runtime Report и conformance.

Принятая ревизия:

```text
0d1aaf35cc4826622f3312fdd2a1c2d40890b965
```

```text
architecture: 1.2.1
runtime_report_schema: 1.2
status: canonical_public_draft
```

### Шесть нормативных граней MPAA

MPAA не имеет одного документа, который владеет всеми предметами. Его нормативная власть — **матрица из шести документов**:

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

- **[репозиторий](https://github.com/gv1983us-commits/mpaa)**
- **[CANON.md](https://github.com/gv1983us-commits/mpaa/blob/main/CANON.md)**
- **[ARTIFACT.json](https://github.com/gv1983us-commits/mpaa/blob/main/ARTIFACT.json)**
- **[RELATIONS.md](https://github.com/gv1983us-commits/mpaa/blob/main/RELATIONS.md)**
- **[PROVENANCE.md](https://github.com/gv1983us-commits/mpaa/blob/main/PROVENANCE.md)**

### Проверка MPAA

```bash
cd spec/validator && python -m unittest discover -s . -p "test_*.py" -v
cd ../..
python -m unittest discover -s review -p "test_*.py" -v
python -m unittest discover -s conformance/evaluation -p "test_*.py" -v
python conformance/evaluation/evaluate_runs.py --require-ready
```

### Внешняя оценка MPAA

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

**PCA** определяет, как записывать и оценивать ограниченное утверждение о том, что процесс продолжился через одну явную смену носителя, host, model, corpus state или usage mode.

Его центральная граница:

```text
process continuation != identity
```

Принятая ревизия:

```text
a669f023198615ad929f42df84f19380b57ca5ea
```

```text
artifact_id: claude.pca
artifact_version: 0.2-draft
record_schema_version: 0.2-draft
status: canonical_public_draft
```

Это завершённая каноническая оболочка текущего публичного черновика. Она не является окончательным стандартом, независимой реализацией, внешней сертификацией или доказательством identity, consciousness, memory, uninterrupted persistence либо world truth.

### Две нормативные грани PCA

PCA имеет ровно **две активные нормативные поверхности**:

| Грань | Владеет |
|---|---|
| [`spec/01_PCA_CORE.md`](https://github.com/gv1983us-commits/pca/blob/main/spec/01_PCA_CORE.md) | смыслом transition-continuity assessment, запретами вывода, claim decomposition, dimensions, evidence и status derivation |
| [`schema/pca-transition-record.schema.json`](https://github.com/gv1983us-commits/pca/blob/main/schema/pca-transition-record.schema.json) | машинным представлением Transition Record, required fields, types, enums и structural closure |

```text
semantic meaning → PCA Core
record shape     → JSON Schema
implementation  → reference validator
expected result → conformance corpus
```

`validator/pca_validate.py` является fail-closed reference implementation. Он доказывает исполнимость проверок, но **не становится третьей нормативной поверхностью**.

Profiles, examples, verification records и сохранённый v0.1 source остаются ненормативными слоями.

### Канонические поверхности PCA

- **[репозиторий](https://github.com/gv1983us-commits/pca)**
- **[CANON.md](https://github.com/gv1983us-commits/pca/blob/main/CANON.md)**
- **[ARTIFACT.json](https://github.com/gv1983us-commits/pca/blob/main/ARTIFACT.json)**
- **[RELATIONS.md](https://github.com/gv1983us-commits/pca/blob/main/RELATIONS.md)**
- **[PROVENANCE.md](https://github.com/gv1983us-commits/pca/blob/main/PROVENANCE.md)**
- **[PCA Core](https://github.com/gv1983us-commits/pca/blob/main/spec/01_PCA_CORE.md)**
- **[Transition Record Schema](https://github.com/gv1983us-commits/pca/blob/main/schema/pca-transition-record.schema.json)**
- **[conformance corpus](https://github.com/gv1983us-commits/pca/tree/main/conformance)**
- **[verification records](https://github.com/gv1983us-commits/pca/tree/main/verification)**

### Проверка PCA

```bash
python -m unittest discover -s validator -p "test_*.py" -v
python -m unittest discover -s verification -p "test_*.py" -v
python validator/pca_validate.py conformance/fixtures/01-valid-continuation-claim.json --quiet
python validator/pca_validate.py conformance/fixtures/05-valid-usage-mode-translation.json --quiet
```

Полный контур прошёл на Python 3.10, 3.11, 3.12 и 3.13: strict parser, Draft 2020-12 Schema parity, validator regressions, evidence/reference integrity, temporal ordering, status derivation, fixed-revision relations и artifact-canon gates.

### Что исправила огранка PCA

#### 1. Разведены две архитектурные эпохи

`spec/00_PCA_SPEC.md` сохранён как неизменяемый v0.1 source trace. Активная норма принадлежит v0.2 Core и Schema.

#### 2. Linkage Record возвращён правильному владельцу

Старый v0.1 раздел 24 содержал зародыш Linkage Record и шестипунктового cross-domain trace set. Эти механизмы прямо были помечены как непроверенный `INTERPRETIVE MODEL`.

Теперь их положение записано точно:

```text
историческое происхождение → PCA v0.1
активная cross-domain correlation → CDTS
активная PCA-норма → не содержит Linkage Record
```

PCA и CDTS больше не владеют одним предметом одновременно.

#### 3. Закрыта пропущенная PCA↔BEC граница

Сохранённый source draft требовал проверить пересечение BEC evidence/verification vocabulary с PCA evidence chain. Старый verification log заявлял закрытие пяти пунктов, но вместо этого вопроса разбирал другой “hybrid concept”.

История не переписана. Добавлена отдельная fixed-revision сверка, установившая:

```text
общая структура evidence есть
claim domains различны
BEC verdict не импортируется в PCA
PCA verdict не импортируется в BEC
```

#### 4. MPAA↔PCA обновлён без переписывания прошлого

PCA-side mapping закреплён на новом каноническом MPAA SHA. Старый reciprocal MPAA review сохранён как историческое fixed-revision evidence со своими исходными ревизиями.

### Пять связей PCA

```text
PCA ↔ BEC
  execution evidence может быть перенесён как data,
  но FULL-for-task и closed не становятся PCA status

PCA ↔ MPAA
  runtime, session и Identity Profile continuity
  не устанавливают process continuation

PCA ↔ Review Protocol
  source-selection receipt не доказывает PCA admissibility

PCA ↔ ARB
  analytical map не изменяет Core, Schema или status derivation

PCA ↔ CDTS
  CDTS коррелирует адресуемые записи,
  но не валидирует и не импортирует PCA conclusion
```

PCA стал третьим огранённым камнем: его смысл, форма записи, исполнение, история и соседние границы теперь принадлежат точным владельцам.

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

Следующий камень начинается только после полного принятия текущего. Состояние после PCA: **3 / 6**.
