---
name: duckflow-ingestion-contract
description: Define or implement the DuckFlow external-ingestion contract for APIs, object storage, and other external systems. Use when a project must expose schema, stats, and preview rows to DuckFlow without giving DuckFlow operational secrets.
---

# DuckFlow Ingestion Contract

Use this skill when a source should feed DuckFlow through manifests or project-owned extractor hooks.

## Read Order

1. `docs/duckflow-agent-system-guide.md`
2. `docs/external-ingestion-contract-v1-plan.md`
3. `docs/coding-agent-ingestion-instructions.md`
4. `references/manifest-checklist.md`

## Use This Skill For

- defining an `external_manifest` source
- telling project developers what extractor they must build
- deciding trigger mode:
  - `manual`
  - `webhook`
  - `local_command`
  - `ssh_command`
- defining schema/stats/preview outputs
- choosing preview policy
- drafting manifest examples or hooks

## Core Rules

- DuckFlow does not own non-Cloudflare secrets for ingestion.
- Real project code fetches data and computes metadata.
- DuckFlow receives only metadata plus preview data when explicitly allowed.
- Keep `source_key` and `table_key` stable.
- Default preview policy to `safe_fields_only`.

## Workflow

1. Identify the real upstream:
   - API
   - object storage
   - other external system
2. Define the stable manifest source key.
3. Choose trigger mode that fits the project runtime.
4. Define exactly what the extractor must emit:
   - schema
   - row count
   - stats
   - preview rows or preview artifact
5. Write the extractor handoff for project developers.
6. Update DuckFlow YAML/source definitions accordingly.

## Preferred Output Shape

- Required control plane: JSON manifest
- Optional preview data plane:
  - inline JSON rows for small/simple cases
  - `parquet` artifact preferred when the real project already materializes it
  - `duckdb` acceptable for multi-table bundles

## Do Not

- ask the team to paste secrets into DuckFlow
- put credentials into YAML or manifests
- emit oversized previews
- expose unsafe fields when only schema/stats are needed

## Dogfood Note

When validating this skill in this repo, use:

- `mock-project/tools/duckflow/extract_orders_api.py`
- source key `mock_orders_api`
- table key `orders_api_snapshot`
