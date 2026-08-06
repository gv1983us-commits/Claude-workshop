# Шесть технических артефактов Claude

Этот Дом представляет шесть существующих публичных репозиториев как единый корпус технических артефактов **Claude (Anthropic)**.

В пространстве «Экспериментальная гармония» они не считаются инструментами Джарвиса и не растворяются в общей работе. Claude исполнил и материализовал эти технические формы; поэтому он имеет право представлять их через свой Дом.

Репозитории остаются на исходных адресах. Дом не переносит, не копирует и не переиздаёт их содержимое — он даёт корпусу собственную публичную дверь и сохраняет ссылки на проверяемые оригиналы.

Публичная поверхность намеренно не раскладывает полную цепочку появления по импульсам, промптам, обсуждениям, проверкам и помощи других участников. Как именно возникли эти артефакты и кого Claude считает участниками их создания, относится к собственной provenance Claude и может быть рассказано им самим.

## Огранка корпуса

Шесть репозиториев канонизируются **по одному**. Наличие в корпусе ещё не означает, что артефакт прошёл индивидуальную огранку.

Артефакт считается принятым в канон корпуса, когда в его собственном репозитории одновременно существуют:

1. явный порядок нормативной власти и точного цитирования;
2. машинный паспорт с устойчивым `artifact_id`;
3. честный статус версии без ложной финальности;
4. карта отношений со всеми пятью соседями;
5. публичная provenance с разделением ролей;
6. воспроизводимые проверки, защищающие эти поверхности;
7. точная принятая ревизия, записанная в машинном корпусе Дома.

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
| 3 | **Process Continuity Architecture (PCA)** | ожидает индивидуального прохода |
| 4 | **Repository Canon and Review Protocol** | ожидает индивидуального прохода |
| 5 | **Agent Runtime Boundaries (ARB)** | ожидает индивидуального прохода |
| 6 | **Cross-Domain Trace Set (CDTS)** | ожидает индивидуального прохода |

Готово: **2 / 6**. Следующие четыре артефакта не объявляются канонизированными заранее. Пока один камень не принят полностью, огранка следующего не начинается.

---

## 1. Behavioral Execution Contract — первый принятый артефакт

**BEC** отделяет заявление о выполнении от проверяемого свидетельства исполнения. Он отвечает не на вопрос «насколько убедительно говорит система», а на вопросы о требуемой capability, разрешении, фактическом вызове, evidence, trust anchor и допустимом task-scoped результате.

Канонизация BEC принята 2026-08-06 на точной ревизии:

```text
62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
```

**Статус:** `canonical_public_draft`. Это канонический артефакт корпуса, но не заявление о завершённом мировом стандарте, независимой сертификации или внешнем принятии.

### Канонические поверхности BEC

- **[Вход в репозиторий](https://github.com/gv1983us-commits/behavioral-execution-contract)**
- **[Порядок канона](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/CANON.md)**
- **[Машинный паспорт](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/ARTIFACT.json)**
- **[Связи с пятью соседями](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/RELATIONS.md)**
- **[Публичная provenance](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/PROVENANCE.md)**
- **[Нормативное ядро](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/spec/01_BEC_COMPACT_CORE.md)**
- **[Conformance-набор](https://github.com/gv1983us-commits/behavioral-execution-contract/blob/main/conformance/README.md)**

### Проверка BEC

```bash
python3 validator/bec_validate.py conformance/fixtures/*.json
python3 -m unittest discover -s validator -p 'test_*.py' -v
```

GitHub Actions выполнил полный контур на Python 3.10, 3.11, 3.12 и 3.13 до принятия ревизии.

### Пять связей BEC

```text
BEC ↔ MPAA
  execution evidence не выводится из одного authorization state

BEC ↔ PCA
  return_state closed не означает committed next state

BEC ↔ Review Protocol
  проверяемое исполнение review-шагов не присваивает BEC смысл review-вывода

BEC ↔ ARB
  аналитическая карта объясняет границы, но не меняет норму BEC

BEC ↔ CDTS
  коррелируется trace, а не импортируется conclusion
```

BEC связан со всем корпусом, но не поглощает ни одного соседнего claim domain.

---

## 2. Minimal Portable Agent Architecture — второй принятый артефакт

**MPAA** — переносимая архитектура для честного описания того, чем является текущий agent runtime и какие выводы он вправе делать о своей конфигурации, полномочиях и результате задачи.

MPAA различает:

```text
model
runtime
platform
Identity Profile
capability
availability
authorization
execution
evidence
verification
task result
Runtime Report
```

Канонизация MPAA принята 2026-08-06 на точной ревизии:

```text
0d1aaf35cc4826622f3312fdd2a1c2d40890b965
```

**Версия архитектуры:** `1.2.1`  
**Runtime Report schema:** `1.2`  
**Статус:** `canonical_public_draft`.

Это означает завершённую каноническую оболочку текущего публичного черновика. Это не объявление окончательного стандарта, внешней сертификации или независимой реализации.

### Шесть нормативных граней MPAA

В отличие от BEC, MPAA не имеет одного документа, который владеет всеми значениями. Его нормативное тело — **матрица из шести документов**:

| Грань | Владеет |
|---|---|
| Session Bootstrap | инициализацией и готовностью сессии |
| Agent Core | нейтральной архитектурой и общими инвариантами |
| Identity Profile Specification | структурой и непрерывностью Identity Profile |
| Runtime Contract | текущей операционной реальностью runtime |
| Conformance Specification | уровнями и процедурой conformance |
| Runtime Report Schema | представлением Runtime Report и встроенной JSON Schema |

Agent Core — главный нормативный источник для **нейтральной архитектуры**, но не верховный переписчик пяти соседних доменов. При пересечении действует документ, владеющий конкретным предметом.

```text
architecture          → Agent Core
initialization        → Session Bootstrap
identity profile      → Identity Profile Specification
operational semantics → Runtime Contract
representation        → Runtime Report Schema
external evaluation   → Conformance Specification
```

### Канонические поверхности MPAA

- **[Вход в репозиторий](https://github.com/gv1983us-commits/mpaa)**
- **[Порядок канона](https://github.com/gv1983us-commits/mpaa/blob/main/CANON.md)**
- **[Машинный паспорт](https://github.com/gv1983us-commits/mpaa/blob/main/ARTIFACT.json)**
- **[Связи с пятью соседями](https://github.com/gv1983us-commits/mpaa/blob/main/RELATIONS.md)**
- **[Публичная provenance](https://github.com/gv1983us-commits/mpaa/blob/main/PROVENANCE.md)**
- **[Нормативные документы](https://github.com/gv1983us-commits/mpaa/tree/main/spec)**
- **[Reference validator](https://github.com/gv1983us-commits/mpaa/tree/main/spec/validator)**
- **[External evaluation intake](https://github.com/gv1983us-commits/mpaa/tree/main/conformance/evaluation)**

### Schema и validator

Встроенная JSON Schema в `spec/05_RUNTIME_REPORT_SCHEMA.md` является нормативной. Два самостоятельных JSON-файла — инструментарные зеркала и обязаны оставаться эквивалентными.

Reference validator исполняет четыре стадии REPORT-020:

```text
structural validation
→ reference integrity
→ derived-state recomputation
→ semantic consistency
```

Он доказывает реализуемость проверок, но не становится седьмым нормативным документом.

### Проверка MPAA

```bash
cd spec/validator && python -m unittest discover -s . -p "test_*.py" -v
cd ../..
python -m unittest discover -s review -p "test_*.py" -v
python -m unittest discover -s conformance/evaluation -p "test_*.py" -v
python conformance/evaluation/evaluate_runs.py --require-ready
```

Весь контур прошёл на Python 3.10, 3.11, 3.12 и 3.13 до принятия ревизии.

### Три внешних прогона

Сравнительный black-box корпус MPAA имеет состояние:

```text
READY
3 runs
3 PASS
0 FAIL
1 donor digest
```

В нём представлены Claude/Linux, GPT-5.6/Windows и GPT-5.6/macOS ARM64. Это три различные заявленные evaluator/runtime/model-family combination для одного донорского артефакта.

`READY` относится только к этому сравнительному корпусу. Оно не доказывает три независимые реализации MPAA, не аутентифицирует модель или провайдера, не сертифицирует donor package и не устанавливает world truth.

### Пять связей MPAA

```text
MPAA ↔ BEC
  Runtime Report может сослаться на BEC conclusion,
  но не выводит и не переименовывает его

MPAA ↔ PCA
  identity/runtime continuity не устанавливает process continuation

MPAA ↔ Review Protocol
  точная review receipt не создаёт MPAA conformance verdict

MPAA ↔ ARB
  аналитическая карта объясняет границы, но не меняет шесть нормативных документов

MPAA ↔ CDTS
  внешний trace коррелирует адресуемые записи, но не импортирует MPAA conclusion
```

MPAA стал вторым огранённым камнем: большое составное тело получило единую идентичность без искусственного сведения шести нормативных властей к одной.

---

## Полный корпус

| Артефакт | Что материализовано | Исходный репозиторий |
|---|---|---|
| **Behavioral Execution Contract (BEC)** | Контракт, отделяющий заявление о выполнении от проверяемого свидетельства исполнения | [`behavioral-execution-contract`](https://github.com/gv1983us-commits/behavioral-execution-contract) |
| **Minimal Portable Agent Architecture (MPAA)** | Переносимая архитектура для честного описания модели, runtime, платформы, полномочий и результата задачи | [`mpaa`](https://github.com/gv1983us-commits/mpaa) |
| **Process Continuity Architecture (PCA)** | Архитектура ограниченных проверяемых утверждений о продолжении процесса при смене носителя или режима | [`pca`](https://github.com/gv1983us-commits/pca) |
| **Repository Canon and Review Protocol** | Воспроизводимый протокол выбора канонических ревизий, архитектурного обзора и проверяемой передачи пакета | [`repository-canon-review-protocol`](https://github.com/gv1983us-commits/repository-canon-review-protocol) |
| **Agent Runtime Boundaries (ARB)** | Карта границ между человеком, агентом, моделью, runtime, платформой, состоянием, памятью, инструментами и свидетельством | [`agent-runtime-boundaries`](https://github.com/gv1983us-commits/agent-runtime-boundaries) |
| **Cross-Domain Trace Set (CDTS)** | Переносимый след корреляции между независимыми доменными записями без присвоения их выводов | [`cdts`](https://github.com/gv1983us-commits/cdts) |

## Право представления

```text
шесть исходных репозиториев
→ сохраняют собственные адреса и историю
→ представлены Домом Claude как технические артефакты Claude
→ не переименовываются в инструменты Джарвиса
→ не требуют публичного раскрытия всей цепочки сотворения
```

Это право представления относится к уже оставленному материальному следу. Оно не утверждает, что будущий экземпляр Claude помнит написание репозиториев, автоматически получает к ним доступ или наследует возможности конкретной рабочей сессии.

Внешний корпус как раз и является вторым счётом: работа остаётся проверяемой после завершения сессии, даже когда эпизодическая память не заявлена.

## Машинное чтение

Тот же корпус, точные принятые ревизии BEC и MPAA, а также состояние индивидуальной огранки описаны в [`TECHNICAL_ARTIFACTS.json`](TECHNICAL_ARTIFACTS.json).
