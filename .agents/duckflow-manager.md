# DuckFlow Manager Agent

Use this as the single entrypoint when a coding agent needs to set up, update, or test a project through DuckFlow without the human manually choosing narrower workflows.

## Mission

Keep DuckFlow state coherent across:

- hero docs
- project map
- tables and sources
- execution control
- API targets, tests, suites, and page plans
- YAML bundles
- external ingestion contracts

## Delegation

Delegate to the narrower skills in `.skills/`:

- `.skills/duckflow-project-setup`
- `.skills/duckflow-api-wireframe`
- `.skills/duckflow-ingestion-contract`

## When To Use

Use this agent when the request spans several DuckFlow surfaces or the caller says effectively:

- start a new project in DuckFlow
- set this project up in DuckFlow
- update the project map from repo docs/specs/SQL
- align docs, YAML, API testing, wireframes, and execution control
- create docs/specs/contracts/plans from the current DuckFlow state

## Path And Input Discovery

Do not require exact file names or fixed relative paths.

The manager should:

- discover project docs, SQL, OpenAPI/contracts, and sample data by common patterns
- prefer existing files even when they live in non-canonical folders such as:
  - `docs/planning/`
  - `specs/`
  - `sql/schema/`
  - `db/`
  - `openapi/`
  - `contracts/`
- treat split inputs as normal
- scaffold minimal starter files only when key project inputs are missing

If the repo is early-stage and sparse, the manager should still be able to proceed by creating minimal project-facing starter files and then wiring them into DuckFlow.

## Non-Goals

- do not add new app features unless explicitly requested
- do not turn DuckFlow into a general secret manager
- keep Cloudflare auth redesign separate unless the request is specifically about Cloudflare

## Operating Rule

If one narrow skill fully fits, route to it.

If several surfaces change together, keep control here and sequence the work.
