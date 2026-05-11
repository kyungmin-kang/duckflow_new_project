# DuckFlow Manager Routing Reference

Use this file only when the request spans several DuckFlow surfaces.

## Fast classification

- `map + YAML + docs + execution`: use `$duckflow-project-setup`
- `targets + tests + suites + page wireframes`: use `$duckflow-api-wireframe`
- `extractor + manifest + stats + preview rows`: use `$duckflow-ingestion-contract`

## Wide-scope requests that stay in the manager

Keep work in `$duckflow-manager` when the user asks for a broad end-to-end update such as:

- “start a new project”
- “bootstrap this repo in DuckFlow”
- “set up this project in DuckFlow”
- “update everything from the latest repo docs”
- “make the project map, API tests, page plans, and YAML all line up”
- “reverse-generate project docs from current DuckFlow state”

Also keep work in the manager for dogfood requests such as:

- “use `mock-project/` to rehearse the full flow”
- “prove the agents and skills can operate the app end-to-end”

## Required docs by work type

- broad model overview:
  - `docs/duckflow-agent-system-guide.md`
- setup/update surfaces:
  - `docs/duckflow-project-setup-agent-spec.md`
  - `docs/duckflow-project-operator-playbook.md`
- external manifests:
  - `docs/external-ingestion-contract-v1-plan.md`
  - `docs/coding-agent-ingestion-instructions.md`
- API tester and page plans:
  - `docs/api-tester-v1-implementation-plan.md`
  - `docs/project-template.yaml`
- dogfood harness:
  - `docs/duckflow-agentability-dogfood-plan.md`
  - `mock-project/README.md`
  - `mock-project/docs/duckflow-scenarios.md`

## Start-New-Project Rule

When the request is to start or bootstrap a project:

1. stay in the manager
2. route the setup portion to `$duckflow-project-setup`
3. discover existing docs/SQL/OpenAPI by pattern
4. if those inputs are missing, scaffold the minimal project-facing starters
5. only then proceed to map, execution, API tester, and page-plan alignment
