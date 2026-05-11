# NYC Real Estate DuckFlow Starter

This folder is a moveable consumer-project starter for DuckFlow.

You can move it out of this repo and rename it, for example:

```bash
mv RealProject "/Users/kmkang/Documents/New Projects/NYCRealEstate"
```

After moving it, this folder becomes the DuckFlow-facing layer that lives with the real project codebase.

## What This Folder Already Includes

- `.agents/` and `.skills/` for the manager-driven workflow
- `duckflow.project.yaml` with a practical starter surface:
  - hero docs
  - a local browser API target on `http://127.0.0.1:3001`
  - saved API tests and a smoke suite
  - a dashboard page wireframe plan
  - an external-manifest source starter
- `docs/` project docs for hero, pages, and contracts
- `sql/schema.sql` for starter relational structure
- `openapi/local-api.yaml` for a local development API contract
- `tools/duckflow/` extractor examples and integration notes

## Before You Use It

Run the DuckFlow core app from the standalone app repo, not from this project folder.

Recommended backend runtime storage:

```bash
export DUCKFLOW_STORAGE_DIR="$HOME/.duckflow/storage"
```

Then start DuckFlow from the core repo:

```bash
cd "/Users/kmkang/Documents/New Projects/AppDevVisualization/my-react-flow-app"
npm run dev
```

## Minute-1 Setup

1. Move this folder to its final project location.
2. In DuckFlow UI, create a new project.
3. Import `duckflow.project.yaml` into that project.
4. Then use the manager.

You do not need to hand-maintain a fixed set of input paths before the first run.

The manager/setup skills are expected to:

- discover docs, SQL, OpenAPI/contracts, and sample data by pattern
- handle non-canonical layouts such as `docs/planning/` or `sql/schema/`
- tolerate split inputs across multiple files
- scaffold missing starter docs/specs when the project is still sparse

## Running The Manager

The normal single entrypoint is:

- `.agents/duckflow-manager.md`

There is also a start-project alias:

- `duckflow-manager-start` via `.agents.yml`

Use very short prompts.

### Simplest new-project prompt

```text
Use .agents/duckflow-manager.md and start a new project.
```

### Equivalent alias prompt

```text
Use duckflow-manager-start and bootstrap this repo in DuckFlow.
```

### Refresh prompt

```text
Use .agents/duckflow-manager.md and refresh DuckFlow from the current repo state.
```

You should not need to enumerate exact files unless you want to override discovery.

If the repo uses unusual locations, note them in:

- `docs/duckflow/operator-notes.md`

That file is the place to tell agents things like:

- which docs are authoritative
- where SQL really lives
- where OpenAPI/contracts really live
- what local port to use
- which files are generated vs hand-maintained

## End-To-End Verification Checklist

### 1. Hero and map

Verify in DuckFlow that:

- hero docs are visible and linked
- project goal and principles read correctly
- the project map contains:
  - API/runtime nodes
  - UI wireframe node(s)
  - execution-control contract nodes

### 2. SQL and schema planning

Verify that:

- `sql/schema.sql` is reflected in the map/planning context
- the manager creates or updates relevant data/runtime nodes

### 3. API tester

The starter YAML includes:

- target: `Local app`
- tests:
  - `GET /health`
  - `GET /api/listings/summary`
- suite:
  - `Dashboard smoke`

To verify:

1. Run the real project app locally on port `3001`, or update the target base URL.
2. Open `/api-tester` in DuckFlow.
3. Select the imported target and tests.
4. Run:
   - saved test once
   - saved test N times
   - suite once
5. Confirm response, stats, and history behave correctly.

### 4. Page wireframe plan

The starter YAML includes a dashboard page plan at:

- route: `/dashboard`

Verify that:

- the page plan imports correctly
- components render in the preview
- linked tests are visible on the relevant components
- clicking a component shows linked test details

### 5. YAML round-trip

After changes:

1. Export the project YAML from DuckFlow.
2. Compare it to `duckflow.project.yaml`.
3. Keep the project-local YAML current with the latest approved state.

## Local API Assumption

This starter assumes a local app on:

- `http://127.0.0.1:3001`

If the real app uses a different port or route shape, update:

- `duckflow.project.yaml`
- `openapi/local-api.yaml`
- `docs/api-contracts.md`

If docs or specs later move to different paths, update:

- `docs/duckflow/operator-notes.md`

The manager should then rediscover and realign the project without needing fixed canonical paths.

## External Ingestion Starter

For API/object-storage/external systems, prefer the external-manifest flow:

- project code owns real credentials
- DuckFlow only imports schema/stats/preview metadata

Starter references:

- `tools/duckflow/extract_manifest_example.py`
- `docs/duckflow/external-ingestion-contract-v1-plan.md`
- `docs/duckflow/coding-agent-ingestion-instructions.md`
