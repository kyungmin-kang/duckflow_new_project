# DuckFlow Agent and Skill System Guide

Date: 2026-05-08

This is the repo-level guide for coding agents that need to set up, update, test, or export DuckFlow project state without inventing new app features.

It explains:

- what DuckFlow offers today
- what data and planning surfaces DuckFlow stores
- what a good repo-local agent definition looks like
- what a good repo-local skill definition looks like
- how `.agents` and `.skills` should be used in this repo
- which manager/subskills should be used for which jobs
- how the per-project kit is packaged and bootstrapped

## What DuckFlow Offers Today

DuckFlow is a project-structure and validation layer over several coordinated surfaces:

- Hero and project docs
- Project map
- Tables and sources
- Execution control
- API tester
- Page wireframe plans
- YAML interchange

DuckFlow is not the primary owner of:

- production secrets
- full ingestion runtimes
- cloud infrastructure control planes

## Stored Project Surfaces

The persisted project model currently stores, at minimum:

- `environment`
- `hero`
- `database_catalogs`
- `sources`
- `tables`
- `nodes`
- `edges`
- `custom_views`
- `api_targets`
- `api_tests`
- `api_suites`
- `api_page_plans`
- `compute_nodes`
- `dependencies`
- `execution_control_nodes`
- `execution_control_edges`
- `view_layouts`
- `group_notes`
- `history`

These are evidenced in the repo’s type/model definitions:

- [lib/types.ts](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/lib/types.ts:80)
- [backend/app/models.py](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/backend/app/models.py:996)

## What Each Surface Is For

### Hero

Use Hero for:

- project goal
- project status
- operating docs
- agent rules
- key principles and ADR pointers

### Project map

Use the map for:

- tables and other data artifacts
- APIs, services, UI pages, and external systems
- tasks/work items
- runtime/data/architecture relationships

### Tables and sources

Use `sources` to describe where metadata comes from.

Use `tables` to describe structured data artifacts with schema, stats, and optional preview rows or artifacts.

### Execution control

Use execution control for:

- ownership
- contracts
- validation
- decisions
- deployment/runtime constraints

### API tester

Use the API tester for:

- reusable API targets
- one-request tests
- grouped suites
- component-linked page plans

### Page wireframe plans

Use page plans to model:

- route path
- components
- component placement
- load behavior
- linked tests

## Data and Secret Boundaries

### Cloudflare

Cloudflare auth is a separate exception. Keep it separate from the general ingestion model.

### Non-Cloudflare ingestion

For APIs, object storage, and other external systems:

- real project code owns credentials
- DuckFlow triggers or imports results
- DuckFlow stores schema, stats, and preview metadata

### Direct Postgres exception

Direct Postgres access remains supported, but only with caution:

- use read-only accounts
- avoid confidential or user-sensitive data unless explicitly intended

### Existing env/Bitwarden fields

The app still has project-level secret-provider fields in its current model. Treat those as current implementation detail and local-dev convenience, not the preferred trust boundary for serious project setup.

## External Ingestion Model

For non-Cloudflare external systems, the preferred model is:

1. define an `external_manifest` source in DuckFlow
2. let real project code fetch data and compute metadata
3. emit a DuckFlow ingestion manifest
4. import that manifest into DuckFlow

Required control plane:

- JSON manifest

Optional preview data plane:

- inline JSON preview rows
- `parquet` preview artifact preferred
- `duckdb` acceptable for multi-table bundles

See:

- [external-ingestion-contract-v1-plan.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/external-ingestion-contract-v1-plan.md:1)
- [coding-agent-ingestion-instructions.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/coding-agent-ingestion-instructions.md:1)

## YAML Role

YAML is the interchange layer for:

- humans
- coding agents
- setup/update workflows
- reviewable project snapshots

The canonical full-surface template is:

- [project-template.yaml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/project-template.yaml:1)

Example split bundles are under:

- [docs/examples/duckflow-yaml-bundles](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/examples/duckflow-yaml-bundles)

The repo-local rehearsal target is:

- [mock-project/](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/mock-project)

## What Good Agent Definitions Look Like

A good repo-local agent definition is broad and outcome-owning.

It should:

- own a class of outcomes, not a single micro-task
- decide which surfaces are affected
- decide which narrower skills to invoke
- state its non-goals clearly
- state what coherence checks it must perform before finishing

A good agent definition should not:

- duplicate all narrow procedures inline
- pretend to own secrets or infrastructure that belong elsewhere
- become a giant pile of low-level instructions with no routing logic

For DuckFlow, a good manager agent must understand:

- map vs execution control vs API tester vs YAML
- what belongs in DuckFlow and what belongs in real project code
- when to delegate and when to keep control

## What Good Skill Definitions Look Like

A good repo-local skill definition is narrow and reusable.

It should:

- say exactly when to use it
- say exactly when not to use it
- define a small read order
- define one workflow clearly
- list required outputs
- avoid becoming a second manager

A good skill definition should not:

- own several unrelated surfaces
- hide trigger conditions
- duplicate large reference docs in the skill body
- invent new app features

For DuckFlow, good skills split cleanly into:

- project setup / sync
- API tests and page wireframes
- external ingestion contracts

## Filesystem Convention

Use:

- `.agents/duckflow-manager.md` as the canonical directory-style manager prompt
- `.agents.yml` as the portable machine-readable agent registry
- `.agents.md` as the root compatibility shim for agent systems that only read one prompt file
- `.agents/` as the canonical directory-style expansion folder
- `.skills/` for narrow reusable workflows

This repo uses:

- [.agents/duckflow-manager.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents/duckflow-manager.md:1)
- [.agents/registry.yml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents/registry.yml:1)
- [.agents.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents.md:1)
- [.agents.yml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents.yml:1)
- [.skills/duckflow-manager](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-manager/SKILL.md:1)
- [.skills/duckflow-project-setup](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-project-setup/SKILL.md:1)
- [.skills/duckflow-ingestion-contract](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-ingestion-contract/SKILL.md:1)
- [.skills/duckflow-api-wireframe](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-api-wireframe/SKILL.md:1)

## Project-Kit Packaging

DuckFlow should be reused across projects as a small per-project kit, not by copying the full app repo into each consumer project.

The exact kit layout is documented in:

- [duckflow-project-kit-structure.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/duckflow-project-kit-structure.md:1)
- [duckflow-runtime-storage.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/duckflow-runtime-storage.md:1)

Bootstrap it with:

```bash
python3 tools/duckflow/bootstrap_project_kit.py --target /path/to/project --force
```

Validate the repo-local rehearsal harness with:

```bash
python3 tools/duckflow/run_mock_dogfood.py
```

For real project work, start the backend with:

```bash
export DUCKFLOW_STORAGE_DIR="$HOME/.duckflow/storage"
```

so live project state stays outside the core repo.

## Repo-Local Agent / Skill System

### Manager layer

The manager entrypoint lives in:

- [.agents.md](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents.md:1)

Machine-readable routing lives in:

- [.agents.yml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.agents.yml:1)

### Skill layer

The narrower skills live in:

- [.skills/duckflow-manager](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-manager/SKILL.md:1)
- [.skills/duckflow-project-setup](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-project-setup/SKILL.md:1)
- [.skills/duckflow-ingestion-contract](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-ingestion-contract/SKILL.md:1)
- [.skills/duckflow-api-wireframe](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/.skills/duckflow-api-wireframe/SKILL.md:1)

## How Work Should Route

### Use docs / SQL / specs to create or update the project map

Use:

- manager -> `duckflow-project-setup`

### Configure API tests, suites, page plans, and UI-linked checks

Use:

- manager -> `duckflow-api-wireframe`

### Define an external extractor contract for API/object-storage sources

Use:

- manager -> `duckflow-ingestion-contract`

### Keep everything aligned end-to-end

Use:

- manager, keeping control across:
  - hero/docs
  - sources/tables/nodes/edges
  - execution control
  - API tester/page plans
  - YAML output

## Operating Principle

The human should mainly observe, approve direction, and correct assumptions.

The coding agent should do the setup/update work by:

- reading current project docs and code
- mapping that into DuckFlow surfaces
- maintaining coherent YAML and linked planning state

The manager agent is the intended single entrypoint for that workflow.

When validating the system itself, use `mock-project/` as the first dogfood target before trying it on real project repos.
