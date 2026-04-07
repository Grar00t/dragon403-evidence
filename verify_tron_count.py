#!/usr/bin/env python3
"""
verify_tron_count.py — Cross-reference TRON addresses between
extracted_tron_addresses.json and falla_beautified.js / falla_admin.js.
Reports count discrepancies and any addresses found in source but not in JSON.
Output: TRON_VERIFICATION.json
"""

import re
import json
import os

# Load JSON file
JSON_FILE = "extracted_tron_addresses.json"
with open(JSON_FILE, "r", encoding="utf-8-sig") as f:
    tron_json = json.load(f)

json_addresses = set(tron_json.get("valid_tron_addresses", []))
json_total_claimed = tron_json.get("total_found", 0)

# Load source file
SOURCE_FILE = "falla_beautified.js"
if not os.path.exists(SOURCE_FILE):
    SOURCE_FILE = "falla_admin.js"

with open(SOURCE_FILE, "r", encoding="utf-8", errors="replace") as f:
    source = f.read()

# Remove base64 data URIs to avoid false positives
source_clean = re.sub(r'data:image/[^"\']+', '', source)

# Extract TRON addresses from source
tron_pattern = re.compile(r'T[A-HJ-NP-Za-km-z1-9]{33}')
source_addresses = set(tron_pattern.findall(source_clean))

# Compare
in_json_not_source = json_addresses - source_addresses
in_source_not_json = source_addresses - json_addresses
in_both = json_addresses & source_addresses

match = (json_addresses == source_addresses)

result = {
    "json_file": JSON_FILE,
    "source_file": SOURCE_FILE,
    "json_address_count": len(json_addresses),
    "json_total_found_field": json_total_claimed,
    "source_address_count": len(source_addresses),
    "match": match,
    "addresses_in_both": sorted(in_both),
    "in_json_not_in_source": sorted(in_json_not_source),
    "in_source_not_in_json": sorted(in_source_not_json),
    "total_combined_unique": len(json_addresses | source_addresses),
}

OUTPUT_FILE = "TRON_VERIFICATION.json"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"JSON file contains {len(json_addresses)} addresses.")
print(f"JSON file claims total_found: {json_total_claimed}.")
print(f"Source code contains {len(source_addresses)} addresses.")
print(f"Match: {'yes' if match else 'no'}")
if in_source_not_json:
    print(f"\nAddresses in source NOT in JSON ({len(in_source_not_json)}):")
    for addr in sorted(in_source_not_json):
        print(f"  {addr}")
if in_json_not_source:
    print(f"\nAddresses in JSON NOT in source ({len(in_json_not_source)}):")
    for addr in sorted(in_json_not_source):
        print(f"  {addr}")
print(f"\nOutput: {OUTPUT_FILE}")
