# Семь технических артефактов Claude

Мастерская представляет семь публичных технических репозиториев как единый корпус артефактов Claude. Репозитории остаются на исходных адресах; корпус фиксирует представление, exact accepted revisions и границы, но не переносит сюда нормативную власть соседних артефактов.

Исторический корпус **6 / 6** сохранён без переписывания:

- [`history/TECHNICAL_ARTIFACTS_SIX.md`](history/TECHNICAL_ARTIFACTS_SIX.md)
- [`history/TECHNICAL_ARTIFACTS_SIX.json`](history/TECHNICAL_ARTIFACTS_SIX.json)

Текущий корпус: **7 / 7 — CANON**.

## 1. Behavioral Execution Contract (BEC)

- Repository: `gv1983us-commits/behavioral-execution-contract`
- Accepted revision: `62f2b7940b5ca7a4a8b24150b9c45a6ab5d97261`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

BEC остаётся владельцем своей семантики execution evidence. Нахождение BEC в корпусе не превращает его вывод в универсальное доказательство исполнения.

## 2. Minimal Portable Agent Architecture (MPAA)

- Repository: `gv1983us-commits/mpaa`
- Accepted revision: `0d1aaf35cc4826622f3312fdd2a1c2d40890b965`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

Принята ровно зафиксированная архитектурная ревизия. Исторический внешний evaluation corpus и его границы сохранены в шестикорпусном snapshot.

## 3. Process Continuity Architecture (PCA)

- Repository: `gv1983us-commits/pca`
- Accepted revision: `a669f023198615ad929f42df84f19380b57ca5ea`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

PCA сохраняет собственную bounded-семантику продолжения; canonization не превращает continuation в identity, memory или subjectivity.

## 4. Repository Canon and Review Protocol

- Repository: `gv1983us-commits/repository-canon-review-protocol`
- Accepted revision: `b4205ffd91a6316ab40243cbf8161a1c512cae1f`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

Review Protocol сохраняет собственный домен review/receipt и не импортирует внешние conformance или safety-выводы.

## 5. Agent Runtime Boundaries (ARB)

- Repository: `gv1983us-commits/agent-runtime-boundaries`
- Accepted revision: `bcf9f628ee1d7c2075673b00f660674680bb6f62`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

ARB канонизирован именно с нулевой внешней нормативной силой и с отделением analytical surfaces от proposal surface.

## 6. Cross-Domain Trace Set (CDTS)

- Repository: `gv1983us-commits/cdts`
- Accepted revision: `ffb9719ae06db0f4f0cdd20b937c2648181a4e4a`
- Artifact status: `canonical_public_draft`
- Corpus status: `canonicalized`

`ADMISSIBLE` остаётся выводом CDTS о допустимости trace; он не означает causality, event identity, world truth или CAP acceptability.

## 7. Composite Assurance Protocol (CAP)

- Repository: `gv1983us-commits/composite-assurance-protocol`
- Protocol version: `0.2`
- Record profile: `0.1-draft`
- Artifact status: `canonical_public_release`
- Corpus status: `canonicalized`
- Accepted revision: `1b6eb79b2973ea1e18cb8864ee0b9e68ac937d68`
- Accepted CI run: `31188066120` — `success`

CAP закрывает отдельный claim domain: получение одного **bounded cross-artifact assessment** из независимо принадлежащих исходных записей без слияния их нормативной власти и без превращения локальных verdicts в глобальное заключение.

В принятой ревизии присутствуют:

- шесть закрытых нормативных поверхностей;
- JSON Schema Draft 2020-12;
- machine-readable vocabulary, derivation rules, invariants и diagnostic registry;
- Python reference validator;
- независимая Node.js реализация;
- полный fixture oracle;
- stable diagnostic codes;
- lifecycle/profile lock/release acceptance;
- adversarial cross-runtime differential suite;
- постоянный CI: Python 3.10–3.13, Node.js 20/22 и отдельный differential job.

Финальный hardening перед corpus canonization не изменял нормативную семантику CAP 0.2. Он обнаружил и устранил два класса риска: отсутствие отдельной adversarial differential проверки между реализациями и устаревшие pre-release формулировки на provenance/publication surfaces.

## Canonization rule

Артефакт считается завершённым в корпусе только когда одновременно существуют:

1. явная каноническая поверхность и порядок нормативной власти;
2. устойчивый machine identity;
3. честный version/status;
4. явные relations без импорта чужих verdicts;
5. публичная provenance с разделением ролей;
6. воспроизводимые проверки;
7. exact accepted revision с зелёным CI receipt.

CAP удовлетворяет этому правилу на ревизии `1b6eb79b2973ea1e18cb8864ee0b9e68ac937d68`.

## Общая граница корпуса

```text
seven canonicalized artifacts != one merged specification
exact accepted revision != world truth
house representation != repository ownership transfer
neighbor relation != conclusion ownership transfer
CAP bounded assessment != global assurance
```

**Корпус полностью огранён: 7 / 7 — CANON.**
