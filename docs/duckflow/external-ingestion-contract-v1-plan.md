# DuckFlow External Ingestion Contract V1

Date: 2026-05-08

## Goal

Move non-Cloudflare ingestion in DuckFlow to an external-extractor model:

- DuckFlow does not own operational secrets for API, object-storage, or external-system ingestion.
- Real project code owns credentials and data access.
- DuckFlow triggers the real project code when needed.
- DuckFlow stores and reasons over imported metadata:
  - schema
  - row count
  - column profiles / summary stats
  - preview rows
  - optional preview artifacts
  - freshness / import status

Cloudflare authentication remains a separate exception and is not part of this redesign.

## Why This Model Fits DuckFlow

DuckFlow already behaves primarily as a planning, mapping, metadata, and inspection layer.

Current persisted project state already includes:

- `sources`
- `tables`
- `nodes`
- `edges`
- `compute_nodes`
- `execution_control_nodes`
- `api_targets`
- `api_tests`
- `api_suites`
- `api_page_plans`
- `view_layouts`
- `group_notes`

Current table storage already supports:

- `columns`
- `row_count`
- `cached_profiles`
- `preview_rows`
- `snapshot_status`
- `freshness_status`
- `summary_enabled`
- `preview_enabled`
- `query_enabled`

That means DuckFlow is already well-shaped to consume extracted metadata without becoming the system that owns secrets.

## Security Boundary

### In scope

DuckFlow may:

- trigger extraction code
- receive a manifest
- import safe metadata and optional preview samples
- warn about sensitive preview policy choices

### Out of scope

DuckFlow should not become:

- the primary secret manager
- the primary ingestion runtime
- the place where project teams paste API keys, DB passwords, or object-storage credentials

### Postgres exception

Direct PostgreSQL access remains supported as an existing workflow.

Required warning:

- use read-only accounts
- do not point DuckFlow at confidential or user-sensitive production data unless explicitly intended

## Supported Source Families

V1 external ingestion source families:

- `api`
- `object_storage`
- `external_system`

Postgres remains separate and keeps its current direct-query workflow.

## Operating Model

### For API / object storage / external systems

1. Project developers build a small extractor in the real project codebase.
2. That extractor uses project-owned credentials and runtime configuration.
3. The extractor computes:
   - schema
   - row count
   - summary stats
   - preview rows, if enabled
   - optional preview artifact reference
4. The extractor emits a DuckFlow ingestion manifest.
5. DuckFlow imports the manifest and updates the project’s `sources` and `tables`.

### For DuckFlow triggers

DuckFlow may start the extractor through one of these modes:

- `manual`
- `webhook`
- `local_command`
- `ssh_command`

### Trigger result modes

V1 supports these practical trigger outcomes:

- direct manifest response
  - webhook returns JSON manifest
  - local command prints JSON manifest to stdout
  - SSH command prints JSON manifest to stdout
- push import
  - project code calls DuckFlow’s manifest-import endpoint directly

## New Project Concepts

### 1. External manifest source

Add a new source kind:

- `external_manifest`

This source describes:

- what family the upstream source belongs to
- what trigger mode to use
- what manifest source key DuckFlow expects
- what preview policy is allowed

This source does not contain secrets.

### 2. Trigger definition

Each `external_manifest` source has one trigger definition:

- `manual`
- `webhook`
- `local_command`
- `ssh_command`

### 3. Manifest import

DuckFlow receives a manifest and maps it into:

- source freshness state
- source change counters
- table definitions
- preview rows
- preview artifact metadata
- stats

## Exact Manifest Schema

Required top-level shape:

```json
{
  "schema_version": 1,
  "extracted_at": "2026-05-08T12:00:00Z",
  "status": "ok",
  "source": {
    "source_key": "orders_api",
    "source_kind": "api",
    "source_label": "Orders API",
    "preview_policy": "safe_fields_only"
  },
  "tables": [
    {
      "table_key": "orders",
      "name": "orders",
      "schema_name": null,
      "group_name": "Orders",
      "source_name": "Orders API",
      "columns": [
        {
          "name": "order_id",
          "data_type": "string",
          "nullable": false,
          "selection": "keep"
        },
        {
          "name": "status",
          "data_type": "string",
          "nullable": true,
          "selection": "keep"
        }
      ],
      "row_count": 12452,
      "column_profiles": [
        {
          "name": "order_id",
          "data_type": "string",
          "missing_pct": 0,
          "min": "A001",
          "max": "Z999",
          "mean": null,
          "std": null
        }
      ],
      "table_stats": {
        "latest_updated_at": "2026-05-08T11:55:00Z",
        "null_status_count": 14
      },
      "preview_rows": [
        {
          "order_id": "A123",
          "status": "paid"
        }
      ],
      "preview_artifact": {
        "format": "parquet",
        "path": "/srv/project/.duckflow/orders_preview.parquet",
        "uri": null,
        "table_name": null,
        "row_count": 30,
        "note": "Typed preview sample"
      },
      "data_fingerprint": "orders-2026-05-08T11:55:00Z",
      "summary_enabled": true,
      "preview_enabled": true,
      "query_enabled": false,
      "notes": "Preview excludes customer PII.",
      "warnings": []
    }
  ],
  "warnings": [],
  "errors": []
}
```

### Top-level fields

- `schema_version`
  - required
  - currently `1`
- `extracted_at`
  - required ISO timestamp
- `status`
  - `ok`
  - `warning`
  - `error`
- `source`
  - required descriptor of the upstream source family
- `tables`
  - required list
- `warnings`
  - optional list of non-fatal manifest-level warnings
- `errors`
  - optional list of fatal or semi-fatal manifest-level errors

### Source descriptor

- `source_key`
  - required stable identifier from the real project
  - must match the DuckFlow source’s configured manifest source key
- `source_kind`
  - `api`
  - `object_storage`
  - `external_system`
- `source_label`
  - optional human-readable label
- `preview_policy`
  - `none`
  - `safe_fields_only`
  - `full`

### Table entry

- `table_key`
  - required stable key for the table-like artifact
- `name`
  - required display name
- `schema_name`
  - optional logical schema/namespace
- `group_name`
  - optional preferred source group for DuckFlow
- `source_name`
  - optional human-readable upstream label
- `columns`
  - required list of column definitions
- `row_count`
  - optional
- `column_profiles`
  - optional list of summary profiles
- `table_stats`
  - optional dictionary of extra table-level stats
- `preview_rows`
  - optional inline preview rows
  - capped by DuckFlow to 30 rows on import
- `preview_artifact`
  - optional typed preview artifact metadata
- `data_fingerprint`
  - optional upstream fingerprint or revision token
- `summary_enabled`
  - optional hint
- `preview_enabled`
  - optional hint
- `query_enabled`
  - optional hint, but DuckFlow should default external manifests to `false`
- `notes`
  - optional table-level notes
- `warnings`
  - optional table-level warnings

### Preview artifact

Supported V1 metadata values:

- `format`
  - `parquet`
  - `duckdb`
  - `csv`
  - `json`
- `path`
  - backend-visible file path, if applicable
- `uri`
  - remote URI, if applicable
- `table_name`
  - optional table name for multi-table DuckDB bundles
- `row_count`
  - optional row count represented by the artifact
- `note`
  - optional explanation

### Why JSON manifest + optional artifact

DuckFlow should require the JSON manifest because it is:

- easy to validate
- easy to diff
- easy to import through HTTP
- easy to render in the UI

Artifacts are optional because they help with typed preview reuse, but should not be the only control-plane path.

Preferred artifact format:

- `parquet`

Acceptable later:

- `duckdb` for multi-table bundles

Fallback only:

- `csv`

## Mapping Manifest Data Into Project State

### Source mapping

Each external manifest source stores:

- `id`
- `kind = external_manifest`
- `upstream_kind`
- `name`
- `manifest_source_key`
- `group_name`
- `preview_policy`
- `trigger`
- freshness timestamps and counters

### Table mapping

Manifest tables map into normal DuckFlow `tables`.

Stable table identity:

- `stable_table_id(source_id, table_key)`

Imported fields:

- `columns`
- `row_count`
- `cached_profiles`
- `table_stats`
- `preview_rows`
- `preview_artifact`
- `data_fingerprint`
- `source_name`
- `group_name`
- `schema_name`
- `snapshot_status`
- `freshness_status`

Preserved from previous DuckFlow table metadata when the table already exists:

- user-renamed table name
- stage
- validation status
- notes
- update frequency
- assignee
- due date
- priority
- milestone
- sprint
- acceptance criteria
- review state
- group assignments
- related files
- extra fields
- PK / unique / index metadata

### Missing tables

If a table was previously imported for that source and is missing from a later manifest:

- keep the table record
- mark it as:
  - `snapshot_status = missing`
  - `freshness_status = stale`
- add an explanatory freshness note

This preserves planning work while still surfacing disappearance.

## Trigger Contract

### Mode: manual

DuckFlow stores the source and allows:

- manual import of a manifest
- manual trigger request logging

DuckFlow does not run code itself.

### Mode: webhook

DuckFlow:

- sends a POST request to the configured webhook URL
- includes a small context payload:
  - `project_id`
  - `project_name`
  - `source_id`
  - `manifest_source_key`
  - `triggered_at`
- expects a JSON manifest response

### Mode: local_command

DuckFlow:

- runs a configured backend-local command
- optionally within a working directory
- expects manifest JSON on stdout

### Mode: ssh_command

DuckFlow:

- uses the project’s SSH connection
- optionally changes into a configured working directory
- runs a configured command
- expects manifest JSON on stdout

## Coding-Agent / Project-Developer Contract

The real project team must build extractors that:

1. use project-owned credentials
2. fetch from the real upstream system
3. sanitize preview rows when needed
4. emit a DuckFlow manifest
5. either:
   - return it directly, or
   - push it into DuckFlow

DuckFlow agents must not:

- invent secret providers for this flow
- ask developers to paste credentials into DuckFlow
- route confidential data through the browser

## YAML / AI Interchange Implications

The YAML template must include all major project surfaces, including:

- hero
- environment
- sources
- tables
- nodes
- edges
- compute nodes
- dependencies
- custom views
- API tester targets/tests/suites/page plans
- execution control nodes/edges
- view layouts
- group notes
- history

It must also include an example `external_manifest` source and sample imported table metadata.

## What DuckFlow Needs To Build In V1

### Backend

1. new `external_manifest` source kind
2. trigger models
3. manifest validation models
4. manifest import endpoint
5. trigger endpoint
6. table storage fields for:
   - `table_stats`
   - `preview_artifact`
7. YAML import/export support

### Docs

1. implementation plan
2. coding-agent instructions
3. project setup/update agent spec
4. updated YAML template

### Frontend

Not the focus of this slice, but later the source editor should expose:

- upstream kind
- manifest source key
- trigger mode
- preview policy
- trigger readiness / instructions

## What V1 Explicitly Does Not Do

- Cloudflare auth redesign
- project-level secret management for ingestion
- object-storage credential storage in DuckFlow
- DuckFlow-side typed artifact preview readers
- full orchestration / scheduling engine
- per-target SSH overrides for ingestion commands

## Recommended Next Order

1. add models and endpoints
2. add YAML/template support
3. add coding-agent docs
4. add project-setup/update agent spec
5. later add frontend editor support for external manifest sources
