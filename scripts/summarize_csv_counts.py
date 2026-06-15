#!/usr/bin/env python3
"""Print basic row/column counts for CSV files in the replication package."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
for path in sorted((ROOT / "data").rglob("*.csv")):
    with path.open(newline='', encoding='utf-8-sig') as fp:
        rows = list(csv.reader(fp))
    header = rows[0] if rows else []
    print(f"{path.relative_to(ROOT)}: {max(0, len(rows)-1)} data rows, {len(header)} columns")
