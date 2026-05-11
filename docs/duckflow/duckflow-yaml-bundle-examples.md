# DuckFlow YAML Bundle Examples

Date: 2026-05-08

These files show how to split a project across smaller YAML bundles while keeping the same overall shape as the full template.

Files:

- [hero-environment.yaml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/examples/duckflow-yaml-bundles/hero-environment.yaml:1)
- [map-execution.yaml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/examples/duckflow-yaml-bundles/map-execution.yaml:1)
- [api-wireframes.yaml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/examples/duckflow-yaml-bundles/api-wireframes.yaml:1)
- [external-ingestion.yaml](/Users/kmkang/Documents/New%20Projects/AppDevVisualization/my-react-flow-app/docs/examples/duckflow-yaml-bundles/external-ingestion.yaml:1)

Use these as:

- onboarding examples for humans
- starter material for coding agents
- scoped updates when one agent owns one subset of the project

The intended routing is:

- manager agent in `.agents.md` / `.agents.yml`
- narrower procedures in `.skills/`

All bundles assume the same:

- `schema_version`
- `project.id`
- `project.name`

They differ only in the project sections they carry.
