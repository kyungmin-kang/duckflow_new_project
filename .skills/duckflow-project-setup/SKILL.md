---
name: duckflow-project-setup
description: Build, refresh, and normalize DuckFlow project state across hero docs, map nodes and edges, execution control, sources and tables, and YAML bundles. Use when the task is to onboard a project, reconcile repo changes, or keep DuckFlow aligned with specs, SQL, docs, and runtime structure.
---

# DuckFlow Project Setup

Use this skill when the job is to create or refresh the project map and its related planning state.

## Read Order

1. `docs/duckflow-agent-system-guide.md`
2. `docs/duckflow-project-setup-agent-spec.md`
3. `references/checklist.md`
4. `references/discovery.md` when project inputs are missing, moved, or split
5. Read `docs/project-template.yaml` or the relevant bundle examples if YAML is part of the request.

## Use This Skill For

- initial project onboarding into DuckFlow
- updating hero docs and project framing
- creating nodes, edges, tables, sources, compute nodes, and dependencies
- aligning execution-control views with current code/specs
- turning docs and SQL into DuckFlow structure
- exporting or normalizing DuckFlow YAML bundles
- reverse-generating project docs from current DuckFlow state

## Workflow

1. Inspect the current repo docs, SQL, and any existing DuckFlow YAML.
2. Discover candidate docs/specs/SQL/OpenAPI/sample-data files by pattern.
3. If key project-facing inputs are missing, scaffold minimal starters.
4. Decide what belongs in:
   - `hero`
   - `sources`
   - `tables`
   - `nodes`
   - `edges`
   - `compute_nodes`
   - `dependencies`
   - `execution_control_*`
5. Reconcile runtime structure, data structure, and planning structure separately.
6. Preserve user planning metadata where possible.
7. Update or emit YAML bundles that match the maintained state.

## Modeling Rules

### Use tables for

- schema-bearing data artifacts
- imported manifest tables
- SQL relations

### Use nodes for

- APIs
- services
- pages and wireframes
- external systems
- work/task concepts

### Use execution-control items for

- contracts
- validation checks
- decisions
- deployment/runtime constraints

## Required Output Quality

- Node and edge labels must be intentional, not mechanical file dumps.
- Group/subgroup/tag assignments should be coherent across related items.
- Hero docs should reflect current reality, not stale aspiration.
- YAML must stay close to `docs/project-template.yaml`.

## Do Not

- invent app capabilities that do not exist
- put operational secrets into DuckFlow YAML
- collapse data, runtime, and execution-control concepts into one layer
- treat direct Postgres access as the default for all external systems

## Dogfood Note

When validating this skill in this repo, use `mock-project/` as the default rehearsal target for:

- docs -> hero and map modeling
- SQL -> table and runtime structure
- local datasets -> file-backed data planning
