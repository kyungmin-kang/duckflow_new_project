# Key ADRs

## ADR-001: DuckFlow is a planning and metadata layer

DuckFlow should not become the primary secret manager or production ingestion runtime.

## ADR-002: External systems use manifest-based metadata exchange

APIs, object storage, and other external systems should expose schema/stats/preview metadata to DuckFlow through project-owned extractor code.

## ADR-003: Local browser API testing is part of project readiness

Each project should maintain a minimal local smoke suite that can be run from DuckFlow against a local development server.
