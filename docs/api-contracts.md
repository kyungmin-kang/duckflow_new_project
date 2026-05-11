# API Contracts

## GET /health

Purpose:

- liveness smoke check for the local backend

Expected:

- status `200`
- JSON response
- body contains a top-level `status` field

## GET /api/listings/summary

Purpose:

- provide the dashboard inventory summary

Expected:

- status `200`
- JSON response
- body contains:
  - `active_listings`
  - `pending_listings`
  - `closed_last_30_days`
  - `updated_at`

This endpoint is the initial wireframe-linked contract for the dashboard page plan.
