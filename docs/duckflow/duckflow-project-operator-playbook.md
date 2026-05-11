# DuckFlow Project Operator Playbook

Date: 2026-05-08

This document explains how a project should use DuckFlow end-to-end after the external-ingestion redesign.

## What DuckFlow Is

DuckFlow is:

- a planning and mapping tool
- a metadata and schema explorer
- an execution-control and validation planner
- an API testing and wireframe-planning tool
- a YAML interchange layer for humans and coding agents

DuckFlow is not:

- the primary secret manager for your project
- the primary ingestion runtime for external systems
- the canonical home of production credentials

## Core Surfaces In DuckFlow

### Hero

Use Hero for:

- project goal
- project status
- core operating docs

Recommended docs:

- project goal
- product principles
- coding conventions
- agent rules
- key ADRs

### Project map

Use the map for:

- data artifacts
- runtime/API/service components
- wireframes/pages
- external systems
- work tracking and validation context

### Tables and sources

Use `sources` to represent where data metadata comes from.

Use `tables` to represent concrete schema-bearing data artifacts.

### Execution control

Use execution control for:

- ownership
- contracts
- validation checks
- decisions
- deployment/runtime constraints

### API tester

Use the API tester for:

- saved targets
- saved tests
- suites
- page wireframe plans
- component-linked API checks

## Source Strategy

### Use direct Postgres only when appropriate

Direct Postgres support remains available.

Required caution:

- use read-only accounts
- avoid confidential/user-sensitive production data unless explicitly intended

### Use external manifests for API/object storage/external systems

For:

- APIs
- S3/object storage
- vendor exports
- non-Postgres external systems

Preferred approach:

- real project code performs ingestion/extraction
- DuckFlow triggers it or imports its manifest

## External Ingestion Workflow

1. Create an `external_manifest` source in DuckFlow.
2. Give it:
   - upstream kind
   - stable manifest source key
   - preview policy
   - trigger mode
3. Build the real extractor in the project codebase.
4. Trigger it from DuckFlow or push a manifest into DuckFlow.
5. Let DuckFlow update tables, stats, previews, and freshness metadata.

## Preview Safety Rules

Preview rows are potentially sensitive.

Use:

- `preview_policy = none` when preview data is unsafe
- `preview_policy = safe_fields_only` for default external ingestion
- `preview_policy = full` only when explicitly acceptable

## YAML Strategy

Use YAML as the AI/human interchange layer.

The full project YAML should be able to carry:

- hero
- environment
- sources
- tables
- nodes
- edges
- compute nodes
- dependencies
- custom views
- API tester state
- execution control state
- view layouts
- group notes
- history

## What Real Project Code Owns

The real project owns:

- credentials
- authentication
- network access to private systems
- extraction / ingestion logic
- masking/sanitization rules for preview rows

## What DuckFlow Owns

DuckFlow owns:

- metadata import
- schema/state mapping
- project planning state
- graph/wireframe/API test linkage
- YAML representation

## Recommended Agent Workflow

For each project update:

1. update hero docs
2. update nodes/edges/tables/sources
3. update execution control
4. update API tests/suites/page plans
5. update external-manifest source definitions
6. export/update YAML

## Minimum Project Deliverables

For a project using DuckFlow seriously, maintain:

1. hero docs
2. accurate sources/tables
3. accurate runtime nodes/edges
4. execution-control graph
5. API tester catalog
6. external-ingestion manifests or direct Postgres usage
