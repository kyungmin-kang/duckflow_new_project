---
name: duckflow-manager
description: Orchestrate DuckFlow project setup, map/doc sync, API and wireframe planning, YAML maintenance, and external ingestion planning. Use when a request touches multiple DuckFlow surfaces or when the caller wants one entrypoint that decides which DuckFlow workflow or companion skill to use.
---

# DuckFlow Manager

Use this skill as the single entrypoint for repo-local DuckFlow work.

It is the manager skill. Its job is to:

- inspect the request
- decide which DuckFlow surfaces are affected
- load only the relevant repo docs
- route work to the narrower DuckFlow skills when useful
- keep the result coherent across map, execution control, API tester, page plans, and YAML

Do not use this skill for generic coding tasks that do not touch DuckFlow state or DuckFlow-facing project docs.

## First Read

Always read:

- `docs/duckflow-agent-system-guide.md`

Then load narrower material only as needed:

- broad setup/update work: `references/routing.md`
- project map / execution / YAML work: use `$duckflow-project-setup`
- API tests / suites / wireframes / page plans: use `$duckflow-api-wireframe`
- external/API/object-storage ingestion contracts: use `$duckflow-ingestion-contract`

## Core Rules

- Do not add new DuckFlow app features unless the user explicitly asks.
- Prefer maintaining existing surfaces over inventing new ones.
- Keep Cloudflare auth concerns separate from general ingestion design.
- For non-Cloudflare ingestion, DuckFlow should not become the secret holder.
- Treat YAML as the interchange layer, not the sole source of truth divorced from project docs and code.

## Routing Table

### 1. Project bootstrap or refresh

Use `$duckflow-project-setup` when the request is like:

- use docs in this repo to create or update the project map
- use SQL files to create table and runtime structure
- put task/spec/contract docs onto the project map
- export or normalize the project YAML
- set up local targets, sources, nodes, edges, and execution control

### 2. API tester and page testing

Use `$duckflow-api-wireframe` when the request is like:

- create or update API targets
- define tests and suites
- lay out page components in wireframe plans
- attach UI load behavior to component-level checks
- test these UIs and tell me the results
- align page plans with existing map nodes

### 3. External ingestion setup

Use `$duckflow-ingestion-contract` when the request is like:

- build the extractor contract for an API/object-storage source
- tell project developers what hook/job/script they must build
- import schema, stats, and preview rows through manifests
- show stats and first 30 rows without handing secrets to DuckFlow

## Start-New-Project Shortcuts

This skill must support very short operator prompts such as:

- `Use .agents/duckflow-manager.md and start a new project.`
- `Use duckflow-manager-start and bootstrap this repo in DuckFlow.`
- `Use .agents/duckflow-manager.md and refresh DuckFlow from the current repo state.`

## Manager Workflow

1. Identify the requested outcome.
2. Identify the affected DuckFlow surfaces.
3. Load the smallest relevant subset of repo docs.
4. Discover project inputs by pattern, not by exact filename.
5. If one narrower DuckFlow skill clearly fits, switch to it.
6. If several surfaces change together, keep control here and sequence them:
   - hero/docs
   - sources/tables/nodes/edges
   - execution control
   - API tester/page plans
   - YAML output
7. Preserve consistency across surfaces.

## Discovery And Scaffolding Rules

If paths are non-canonical or key inputs are missing, use the setup skill's discovery rules. The manager should assume that real projects may:

- keep docs under `docs/planning/` or `specs/`
- split SQL across multiple files
- split API contracts across `openapi/` or `contracts/`
- start with missing project-facing docs that need minimal scaffolding

## Surface Checklist

Before finishing, verify whether the request should have updated any of:

- `hero`
- `environment`
- `sources`
- `tables`
- `nodes`
- `edges`
- `custom_views`
- `execution_control_nodes`
- `execution_control_edges`
- `api_targets`
- `api_tests`
- `api_suites`
- `api_page_plans`
- `view_layouts`
- `group_notes`
- YAML bundles/docs

## Common Requests This Skill Must Handle

- Build a project map from docs, specs, SQL, and source metadata.
- Translate docs/specs/tasks/contracts into DuckFlow nodes and edges.
- Derive docs/specs/contracts/API plans back out of current DuckFlow state.
- Set up local API targets and suites for a running app.
- Define page wireframes and component-linked API checks.
- Specify how an external extractor must produce schema/stats/preview manifests.
- Prepare DuckFlow YAML bundles for project onboarding or refresh.

## Dogfood Rehearsal

If the repo contains `mock-project/`, treat it as the canonical non-Cloudflare rehearsal harness.

Use it to verify that the manager can route across:

- docs and hero setup
- map creation from SQL and datasets
- browser-local API testing
- suites and page wireframe planning
- external-manifest extraction
- YAML-oriented project maintenance
