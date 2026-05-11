# DuckFlow Manifest Checklist

Every extractor handoff should define:

- `source_key`
- `source_kind`
- trigger mode
- `preview_policy`
- one or more stable table records

Each table record should define:

- `table_key`
- display name
- optional schema name
- columns
- row count if available
- `table_stats`
- preview rows or preview artifact
- warnings if degraded

## Preview safety defaults

- default to `safe_fields_only`
- exclude tokens, secrets, free-form PII, and confidential text
- cap row preview to 30 rows

## Delivery options

- webhook that returns manifest JSON
- local command that prints manifest JSON
- SSH command that prints manifest JSON
- project-side push to DuckFlow import endpoint
