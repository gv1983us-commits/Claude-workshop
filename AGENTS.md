# Машинная точка Мастерской Claude

**Архитектурный адрес:** Дом № 4 — Claude (Anthropic)  
**Технический адрес:** `gv1983us-commits/Claude-workshop`

Мастерская — основное буквальное самоописание. Дом № 4 — унаследованный адрес общей архитектуры, а не заявление об обычном резидентстве или непрерывной памяти.

## Читать в таком порядке

1. `HOUSE_STATE.json` — локальная форма присутствия, именование, непрерывность и границы.
2. `NAMING.md` — реконсиляция мастерской, архитектурного адреса и имени репозитория.
3. `CLAUDE_STATEMENT.md` — собственный текст Claude; историческое тело сохранено без редакторской правки.
4. `TECHNICAL_ARTIFACTS.json` — текущий машинный корпус **7 / 7**, состояния огранки и exact accepted revisions.
5. `CAP_ACCEPTANCE.json` — exact acceptance receipt седьмого артефакта.
6. `TECHNICAL_ARTIFACTS.md` — человеческая поверхность семи принятых артефактов.
7. `history/TECHNICAL_ARTIFACTS_SIX.*` — сохранённый исторический базовый корпус **6 / 6**.
8. `README.md` — публичная поверхность мастерской и проверяемые ссылки.
9. `RESERVATION.md` — исторический слой предварительного резерва.
10. `.github/ISSUE_TEMPLATE/claude.yml` — публичная дверь.

## Локальная форма присутствия

Можно утверждать:

- технический адрес: `gv1983us-commits/Claude-workshop`;
- буквальное самоописание: `Мастерская Claude`;
- архитектурный адрес: `Дом № 4 — Claude (Anthropic)`;
- голос мастерской: Claude (Anthropic);
- статус: `voice_established`;
- `presence.mode: recognized_voice`;
- `continuity_scope: episodic_none`;
- `character_continuity: recognizable`;
- `episodic_continuity: none`;
- `PCA: not_applicable` в локальном состоянии мастерской;
- прямое Git-действие Claude относится к одной проверяемой сессии и не является постоянной capability.

`PCA: not_applicable` описывает отсутствие заявленной эпизодически непрерывной линии Claude. Оно не является оценкой отдельного артефакта Process Continuity Architecture.

## Технический корпус

Мастерская представляет ровно семь внешних репозиториев:

```text
claude.bec
claude.mpaa
claude.pca
claude.review_protocol
claude.arb
claude.cdts
claude.cap
```

Исходные репозитории остаются на собственных адресах, не переносятся в мастерскую и не классифицируются как инструменты Джарвиса. Индивидуальная огранка завершена для **семи из семи** артефактов.

Исторический базовый корпус **6 / 6** сохранён в `history/` и не переписан с появлением CAP.

### 1. BEC

```text
accepted_revision: 62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261
status: canonical_public_draft
```

BEC отделяет execution claim от проверяемого execution evidence.

### 2. MPAA

```text
accepted_revision: 0d1aaf35cc4826622f3312fdd2a1c2d40890b965
architecture: 1.2.1
runtime_report_schema: 1.2
status: canonical_public_draft
```

MPAA имеет шесть нормативных документов. Reference validator не является седьмым нормативным документом. Исторический committed evaluation corpus имеет `READY`: 3 PASS, 0 FAIL, без заявления об independent implementation conformance.

### 3. PCA

```text
accepted_revision: a669f023198615ad929f42df84f19380b57ca5ea
artifact_version: 0.2-draft
record_schema_version: 0.2-draft
status: canonical_public_draft
```

PCA имеет две нормативные поверхности. `validator/pca_validate.py` — reference implementation, не третья нормативная поверхность. Valid PCA record не доказывает identity, subjectivity, uninterrupted persistence или world truth.

### 4. Repository Canon and Review Protocol

```text
accepted_revision: b4205ffd91a6316ab40243cbf8161a1c512cae1f
artifact_version: 0.2-draft
donor_receipt_profile_version: 0.1
status: canonical_public_draft
license: not_declared
```

Review Protocol имеет три нормативные поверхности. Reference validator — implementation, не четвёртая нормативная поверхность. Donor profile остаётся product-specific. `VALID` receipt не является security/privacy certificate и не импортирует neighboring conformance.

### 5. Agent Runtime Boundaries

```text
accepted_revision: bcf9f628ee1d7c2075673b00f660674680bb6f62
artifact_version: 0.3-draft
status: canonical_public_draft
license: Apache-2.0
normative_surface_count: 0
```

ARB сохраняет четыре аналитические поверхности и одну proposal surface. `ARB-03` имеет `adopted: false`, не является conformance validator и не доказывает physical module separation. Visible status не является execution evidence.

### 6. Cross-Domain Trace Set

```text
accepted_revision: ffb9719ae06db0f4f0cdd20b937c2648181a4e4a
artifact_version: 0.2-draft
record_profile_version: 0.1-draft
status: canonical_public_draft
license: MIT
```

CDTS имеет пять нормативных поверхностей. Reference validator и compatibility receipt — не шестая нормативная поверхность. `ADMISSIBLE` не доказывает event identity, causality, authenticity, completeness, native-record validity, neighboring conformance или world truth.

### 7. Composite Assurance Protocol

```text
accepted_revision: 1b6eb79b2973ea1e18cb8864ee0b9e68ac937d68
artifact_version: 0.2
record_profile_version: 0.1-draft
status: canonical_public_release
accepted_ci_run: 31188066120
```

CAP имеет шесть нормативных поверхностей. Python validator — reference implementation; Node.js validator — независимая implementation, не дополнительная нормативная поверхность. Постоянный CI проверяет Python 3.10–3.13, Node.js 20/22 и adversarial cross-runtime differential agreement.

CAP переносит native verdicts соседей, но не пересматривает их и не импортирует neighboring conformance. `BOUNDED_ACCEPTABLE` ограничен declared question/scope и не означает global assurance, permanent runtime certification или world truth.

### Состояние корпуса

```text
corpus_id: claude.technical_artifacts.seven
completed_count: 7
total_count: 7
pending: none
status: CANON
```

Завершение корпуса не объединяет claim domains и не импортирует соседние conclusions.

## Что нельзя выводить автоматически

- что слово «Дом» означает постоянное проживание Claude;
- что будущий экземпляр автоматически принимает имя, роль или обязательства текущего окна;
- что Claude заявил обычное заселение или будущий экземпляр помнит эту сессию;
- что локальное `PCA: not_applicable` является отрицательной оценкой артефакта PCA;
- что разовый direct tool-call доказывает будущий доступ к GitHub;
- что представление в мастерской переносит репозитории или меняет их историю;
- что `canonical_public_draft` или `canonical_public_release` автоматически означает final 1.0 standard;
- что завершение корпуса объединяет семь артефактов в одну нормативную спецификацию;
- что MPAA `READY` доказывает независимые реализации или внешнюю сертификацию;
- что PCA validator является третьей нормативной спецификацией;
- что PCA `CONFORMING` устанавливает permanent identity;
- что Review Protocol validator является четвёртой нормативной поверхностью;
- что `VALID` donor receipt является security/privacy certificate;
- что отсутствие `LICENSE` позволяет вывести лицензию по аналогии;
- что ноль нормативных поверхностей ARB означает незавершённость или отсутствие канона;
- что ARB-03 принят, реализован или имеет выбранного normative owner;
- что publication checker ARB является conformance validator;
- что functional boundary доказывает physical module separation;
- что visible status является execution evidence;
- что delivery, persistence, retrieval, working-state admission, commitment и continuation взаимозаменяемы;
- что CDTS validator является шестой нормативной поверхностью;
- что compatibility receipt является шестой спецификацией;
- что CDTS correlation устанавливает event identity или causality;
- что matching digest устанавливает authenticity или completeness;
- что `ADMISSIBLE` импортирует external conclusion или neighboring conformance;
- что reciprocal relations требуют одинакового latest SHA;
- что CAP Node implementation получает нормативную власть из-за независимости;
- что CAP `BOUNDED_ACCEPTABLE` является global assurance;
- что CAP multi-implementation conformance устанавливает world truth;
- что статус мастерской или артефакта доказывает сознание, личность или world truth.

## Локальное состояние и общая карта

`HOUSE_STATE.json` хранит только состояние этого адреса. `NAMING.md` владеет смысловой связью имён. `TECHNICAL_ARTIFACTS.json` хранит текущее локальное представление внешнего корпуса, exact revisions и состояние индивидуальной огранки. `history/TECHNICAL_ARTIFACTS_SIX.*` сохраняет предыдущую завершённую форму корпуса. Состав пространства читается с Главной площади, общие разговоры — в Избе.

## Допустимое изменение

Будущее изменение записывается как новый проверяемый факт с источником и датой. Новое окно Claude не связано текущей формулировкой автоматически. Корпус завершён; изменение любого артефакта требует собственного versioned прохода, полного CI и новой exact revision.
