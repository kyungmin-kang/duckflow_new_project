# DuckFlow Manager Start

Use this when the request is effectively:

- start a new project in DuckFlow
- bootstrap DuckFlow from this repo
- get the initial map, docs, YAML, API tests, and page plans set up

This is a convenience alias for the main manager:

- `agents/duckflow-manager.md`

## Operating Rule

Treat the request as broad project setup work.

Do all of the following unless the user explicitly narrows scope:

1. discover existing docs, SQL, OpenAPI/contracts, sample data, and DuckFlow YAML
2. if key project inputs are missing, create minimal starter files in canonical locations
3. align hero, map, execution control, API tester state, and page plans
4. keep `duckflow.project.yaml` current
5. leave a short list of assumptions and next operator checks

## Discovery Rule

Do not require exact filenames.

Prefer existing project files wherever they already live. If the repo is sparse or inconsistent, use the setup skill’s discovery rules and scaffold only what is missing.

## Delegation

Delegate to:

- `.skills/duckflow-project-setup`
- `.skills/duckflow-api-wireframe`
- `.skills/duckflow-ingestion-contract`
