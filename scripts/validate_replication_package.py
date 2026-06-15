#!/usr/bin/env python3
"""Validate required files in the Fairness Requirements SLR replication package."""
from pathlib import Path
import csv, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT / "metadata" / "FILE_MANIFEST.csv"
if not manifest.exists():
    print("ERROR: metadata/FILE_MANIFEST.csv missing")
    sys.exit(1)

missing = []
hash_mismatch = []
with manifest.open(newline='', encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    for row in reader:
        if row['status'] != 'OK':
            missing.append(row['package_path'])
            continue
        path = ROOT / row['package_path']
        if not path.exists():
            missing.append(row['package_path'])
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != row['sha256']:
            hash_mismatch.append(row['package_path'])

if missing:
    print("Missing files:")
    for item in missing:
        print(" -", item)
if hash_mismatch:
    print("Checksum mismatches:")
    for item in hash_mismatch:
        print(" -", item)

if missing or hash_mismatch:
    sys.exit(1)

print("Replication package validation passed.")
