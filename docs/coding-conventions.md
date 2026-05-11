# Coding Conventions

- Keep project-specific DuckFlow assets in the project repo.
- Do not add secrets to DuckFlow YAML or docs.
- Prefer explicit contracts over implicit assumptions.
- Keep local API smoke endpoints stable:
  - `GET /health`
  - `GET /api/listings/summary`
- Update `duckflow.project.yaml` when runtime/API/page-plan meaning changes materially.
