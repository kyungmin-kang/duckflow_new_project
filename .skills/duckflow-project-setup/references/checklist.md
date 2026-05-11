# DuckFlow Project Setup Checklist

## Surfaces to consider

- `environment`
- `hero`
- `database_catalogs`
- `sources`
- `tables`
- `nodes`
- `edges`
- `custom_views`
- `compute_nodes`
- `dependencies`
- `execution_control_nodes`
- `execution_control_edges`
- `api_targets`
- `api_tests`
- `api_suites`
- `api_page_plans`
- `view_layouts`
- `group_notes`

## Inputs that commonly drive updates

- repo docs
- spec docs
- task docs
- ADRs
- OpenAPI files
- SQL files
- database catalogs
- imported manifest snapshots
- current DuckFlow YAML exports

## Input discovery reminder

- Do not assume fixed filenames.
- Search common roots such as:
  - `docs/`
  - `docs/planning/`
  - `specs/`
  - `sql/`
  - `sql/schema/`
  - `db/`
  - `openapi/`
  - `contracts/`
  - `data/`
  - `fixtures/`
- If the repo is early-stage, create the smallest starter set needed to proceed.

## Minimum onboarding deliverables

1. hero docs wired up
2. core sources and tables
3. core runtime nodes and edges
4. execution-control graph
5. API tester catalog if relevant
6. YAML bundle or canonical export
