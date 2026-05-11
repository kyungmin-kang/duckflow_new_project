# DuckFlow Project Input Discovery

Use this reference when a project does not keep everything in one obvious place.

## Principle

Do not require exact filenames.

DuckFlow project setup should work when:

- docs live under `docs/planning/`, `specs/`, or another subfolder
- SQL is split across several files
- OpenAPI/contracts are split or moved
- some of the expected inputs do not exist yet

## Search Order

### Hero and planning docs

Search for likely project-facing docs under:

- `docs/`
- `docs/planning/`
- `specs/`
- `planning/`
- `architecture/`

Look for files matching themes such as:

- goal
- principles
- conventions
- agent rules
- ADRs
- pages
- API contracts

### SQL

Search under:

- `sql/`
- `sql/schema/`
- `db/`
- `database/`
- `migrations/`

Aggregate multiple schema files if needed.

### OpenAPI and contracts

Search under:

- `openapi/`
- `api/`
- `contracts/`
- `specs/`

Accept either a single contract file or a split set.

### Sample data and fixtures

Search under:

- `data/`
- `fixtures/`
- `samples/`
- `mock-data/`

## If Inputs Are Missing

Create the smallest starter set needed to proceed:

- `docs/project-goal.md`
- `docs/product-principles.md`
- `docs/coding-conventions.md`
- `docs/agent-rules.md`
- `docs/key-adrs.md`
- `docs/pages.md`
- `docs/api-contracts.md`
- `sql/schema.sql`
- `openapi/local-api.yaml`
- `duckflow.project.yaml`

## Scaffolding Rule

Prefer existing files over creating new ones.

Only scaffold missing files that are needed to make DuckFlow usable from minute 1.

When scaffolding:

- keep content minimal and explicit
- record assumptions
- wire the created files into `hero`, related files, and the project YAML
