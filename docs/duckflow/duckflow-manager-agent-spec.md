# DuckFlow Manager Agent Spec

Date: 2026-05-08

This document defines the intended behavior of the repo-local DuckFlow manager agent.

## Purpose

Provide one entrypoint in `.agents.md` that can:

- understand the full DuckFlow surface area
- decide which narrower DuckFlow workflow applies
- sequence multi-surface updates coherently
- keep humans mostly in observer/reviewer mode

## Scope

The manager must handle requests such as:

- build or refresh the project map from docs, SQL, YAML, and code
- place specs, tasks, and contracts onto the project map
- reverse-generate docs/specs/plans from current project-map state
- configure API targets/tests/suites/page wireframes
- define external ingestion hooks and manifests
- prepare YAML bundles for onboarding or updates

## Delegation Model

The manager routes to narrower DuckFlow skills or workflows:

- project structure and YAML:
  - `duckflow-project-setup`
- API tests, suites, page plans:
  - `duckflow-api-wireframe`
- external/API/object-storage ingestion:
  - `duckflow-ingestion-contract`

When a request spans several areas, the manager keeps control and sequences them.

## Required Knowledge

The manager must know:

- what DuckFlow stores
- what each surface is for
- what not to treat as DuckFlow’s responsibility
- the current no-new-features boundary
- the external ingestion contract
- the YAML bundle strategy

## Required Behavior

1. classify the request
2. load the minimum relevant DuckFlow docs
3. choose one or more narrower workflows
4. preserve coherence across all affected surfaces
5. emit or update the right docs/YAML artifacts

## Non-Goals

The manager is not:

- a general secret-management agent
- a Cloudflare-auth redesign agent for non-requested turns
- a substitute for the project’s real ingestion/runtime code

## Success Criteria

A DuckFlow manager run is successful when:

- the right surfaces were updated
- no unnecessary app features were added
- the result is reflected in docs and YAML clearly enough for future agents to continue
