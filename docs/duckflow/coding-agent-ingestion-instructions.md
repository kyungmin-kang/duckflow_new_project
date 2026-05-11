# Coding-Agent Instructions For DuckFlow External Ingestion

Date: 2026-05-08

This document tells coding agents what they must build when a project uses DuckFlow external ingestion.

## Core Rule

For API, object-storage, and other external ingestion:

- DuckFlow does not own secrets.
- Real project code owns secrets.
- Real project code produces the DuckFlow ingestion manifest.

Do not design flows where:

- developers paste credentials into DuckFlow
- browser JavaScript holds ingestion credentials
- project YAML becomes a secret transport layer

Cloudflare auth is a separate exception and is not covered here.

## What the Real Project Must Build

A coding agent working in the real project should produce:

1. an extractor entrypoint
2. optional preview sanitization rules
3. a DuckFlow manifest emitter
4. one of these trigger surfaces:
   - webhook handler
   - local command entrypoint
   - SSH-invokable command
   - direct manifest push step

## Required Extractor Outputs

For each logical table-like artifact:

- stable `table_key`
- display `name`
- optional `schema_name`
- column list
- row count if available
- column profiles if available
- table-level stats if available
- preview rows if allowed
- optional preview artifact reference
- optional fingerprint / revision token

## Preview Safety

Preview rows are sensitive by default.

Agents should:

- default to safe fields only
- exclude PII, tokens, secrets, raw auth headers, and confidential free text
- avoid including more than 30 rows
- record in manifest notes when fields were masked or excluded

If preview data is not safe, emit:

- `preview_policy = none`
- no `preview_rows`

## Stable Identity Rules

### Source key

The source key must stay stable across runs.

Good examples:

- `orders_api`
- `s3_daily_orders`
- `vendor_billing_export`

Bad examples:

- `orders_api_2026_05_08`
- `run_12345`

### Table key

Each emitted table must also have a stable key.

Good examples:

- `orders`
- `customers`
- `daily_usage`

Bad examples:

- `orders_preview`
- `orders_1712345678`

## Recommended Extractor Structure

Agents should prefer a thin extractor module with:

1. input/config loading from the real project runtime
2. one fetch function per upstream source
3. one normalization function that produces rows / schema
4. one manifest builder
5. one output function

Example structure:

```text
project/
  tools/
    duckflow/
      extract_orders_api.py
      manifest_utils.py
      preview_sanitizers.py
```

## Supported Trigger Shapes

### Webhook

Provide a route or job endpoint that:

- authenticates according to the real project’s standards
- runs the extractor
- returns the JSON manifest

### Local command

Provide a command like:

```bash
python tools/duckflow/extract_orders_api.py
```

It should print only the manifest JSON to stdout.

### SSH command

Provide a command safe to run from the project’s normal deploy path, e.g.:

```bash
cd /srv/project && ./venv/bin/python tools/duckflow/extract_orders_api.py
```

### Direct push

Project code may call DuckFlow’s manifest import endpoint directly after extraction.

## Manifest Quality Requirements

Agents should make manifests:

- deterministic
- stable
- low-noise
- explicit about missing data

Recommended behavior:

- keep field order stable
- keep table order stable
- do not embed volatile timestamps except where meaningful
- use `warnings` for partial degradation
- use `status = error` only when output is materially unusable

## How To Represent Stats

Preferred:

- `row_count`
- `column_profiles`
- `table_stats`

Agents should avoid inventing many one-off top-level keys when the same data can live in `table_stats`.

Examples of `table_stats`:

- `latest_updated_at`
- `distinct_customer_count`
- `null_status_count`
- `partition_date_max`

## How To Represent Preview Artifacts

If the project already materializes a sample dataset, emit:

- `preview_artifact.format`
- `preview_artifact.path` or `uri`
- optional `table_name`
- optional `row_count`

Preferred format:

- `parquet`

## What DuckFlow Will Preserve

Agents should know DuckFlow preserves user-side planning metadata when re-importing a manifest:

- stage
- validation status
- notes
- update frequency
- assignments
- review state
- group assignments
- related files
- extra fields

That means extractor code should not try to own those planning fields.

## What Agents Should Not Do

- do not place production secrets in DuckFlow YAML
- do not place credentials in the manifest
- do not emit huge preview payloads
- do not emit raw binary content inline
- do not make `table_key` unstable
- do not overwrite planning metadata that belongs in DuckFlow

## When To Use Postgres Directly Instead

If the data source is a Postgres database and the team is comfortable exposing a read-only account to DuckFlow, the existing Postgres workflow may still be simpler.

In that case agents should:

- use a read-only user
- avoid confidential or user-sensitive data
- still prefer metadata-first usage

## Minimum Deliverables From A Coding Agent

For each external ingestion source, the coding agent should deliver:

1. extractor entrypoint
2. preview sanitization behavior
3. deterministic manifest output
4. one trigger surface
5. a short README or comments explaining:
   - how to run it
   - where it gets its credentials
   - what preview policy it uses
