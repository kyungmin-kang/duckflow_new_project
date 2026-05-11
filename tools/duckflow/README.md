# DuckFlow Extractor Hooks

Project-specific extraction logic belongs here.

Principles:

- the real project code owns secrets and upstream access
- DuckFlow should receive only manifests, schema, stats, and optional safe previews
- extraction hooks should emit the DuckFlow external-ingestion contract

Common contents:

- extractor scripts
- wrapper commands for CI or cron jobs
- manifest examples
- notes about trigger modes (`manual`, `webhook`, `local_command`, `ssh_command`)
