#!/usr/bin/env python3
"""Minimal DuckFlow external-ingestion manifest example.

Replace this with project-owned code that reads real upstream systems using the
project's own runtime and secret handling. DuckFlow should only receive the
resulting manifest and optional safe preview rows/artifacts.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone


def main() -> None:
    manifest = {
        "source_key": "replace_me_source_key",
        "source_kind": "api",
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "status": "ok",
        "warnings": [],
        "tables": [
            {
                "table_key": "replace_me_table_key",
                "name": "replace_me",
                "schema_name": None,
                "columns": [
                    {"name": "id", "data_type": "string", "nullable": False},
                    {"name": "status", "data_type": "string", "nullable": True},
                ],
                "row_count": 0,
                "stats": {},
                "preview_policy": "safe_fields_only",
                "preview_rows": [],
                "preview_artifact": None,
            }
        ],
    }
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
