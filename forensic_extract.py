#!/usr/bin/env python3
"""
forensic_extract.py — Automated forensic extraction from falla_admin.js / falla_beautified.js
Extracts routes, domains, TRON addresses, geo-filters, CORS configs,
child-related strings, crypto strings, API keys/secrets, and summary counts.
Output: AUTOMATED_EXTRACTION_REPORT.json
"""

import re
import json
import os
import sys

# Use beautified version if available (minified is a single line)
SOURCE_FILE = "falla_beautified.js"
if not os.path.exists(SOURCE_FILE):
    SOURCE_FILE = "falla_admin.js"

with open(SOURCE_FILE, "r", encoding="utf-8", errors="replace") as f:
    source = f.read()

report = {"source_file": SOURCE_FILE}

# --- A) Route definitions ---
# Match quoted strings starting with / in route-like contexts
route_pattern = re.compile(r'''["'](/[a-zA-Z0-9_/\-\.:\?\=\&\{\}]+)["']''')
routes_raw = route_pattern.findall(source)
# Filter out common non-route patterns (CSS selectors, definitions references, regex)
routes = sorted(set(
    r for r in routes_raw
    if not r.startswith("/#/definitions/")
    and not r.startswith("/g")
    and len(r) > 1
    and not r.startswith("/^")
))
report["routes"] = {"count": len(routes), "values": routes}

# --- B) Hardcoded domains, IPs, and URLs ---
url_pattern = re.compile(r'https?://[^\s"\'`,\)\]\}]+')
urls_raw = url_pattern.findall(source)
urls = sorted(set(urls_raw))

# Extract unique domains from URLs
domain_pattern = re.compile(r'https?://([^/\s:]+)')
domains = sorted(set(domain_pattern.findall(source)))

# IP addresses
ip_pattern = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b')
ips = sorted(set(ip_pattern.findall(source)))

report["urls"] = {"count": len(urls), "values": urls}
report["domains"] = {"count": len(domains), "values": domains}
report["ip_addresses"] = {"count": len(ips), "values": ips}

# --- C) TRON addresses ---
tron_pattern = re.compile(r'T[A-HJ-NP-Za-km-z1-9]{33}')
# Exclude matches inside base64 data URIs
# First, remove base64 data URI strings to avoid false positives
source_no_base64 = re.sub(r'data:image/[^"\']+', '', source)
tron_raw = tron_pattern.findall(source_no_base64)
tron_addresses = sorted(set(tron_raw))
report["tron_addresses"] = {"count": len(tron_addresses), "values": tron_addresses}

# --- D) Geographic/region filtering references ---
geo_pattern = re.compile(
    r'''["']([A-Z]{2}_[A-Z]{2,4})["']'''  # Patterns like SA_SA, AR_GCC, EN_IN
)
geo_raw = geo_pattern.findall(source)
geo_codes = sorted(set(geo_raw))

# Also extract standalone region objects
region_value_pattern = re.compile(r'''region:\s*["']([A-Z]{2,})["']''')
region_values = sorted(set(region_value_pattern.findall(source)))

report["geo_region_codes"] = {"count": len(geo_codes), "values": geo_codes}
report["region_values"] = {"count": len(region_values), "values": region_values}

# --- E) CORS-related configurations ---
cors_pattern = re.compile(r'''[^\n]{0,60}(?:Origin|Access-Control|cors|CORS)[^\n]{0,60}''', re.IGNORECASE)
cors_raw = cors_pattern.findall(source)
cors_configs = sorted(set(s.strip() for s in cors_raw))
report["cors_configurations"] = {"count": len(cors_configs), "values": cors_configs}

# --- F) Child-related functionality ---
child_keywords = re.compile(r'(?:child|minor|kid|youth|young|underage)', re.IGNORECASE)
child_matches = []
for m in child_keywords.finditer(source):
    start = max(0, m.start() - 20)
    end = min(len(source), m.end() + 20)
    context = source[start:end].replace('\n', ' ')
    child_matches.append({
        "match": m.group(),
        "context": context,
        "position": m.start()
    })
# Deduplicate by context
seen_contexts = set()
child_unique = []
for c in child_matches:
    if c["context"] not in seen_contexts:
        seen_contexts.add(c["context"])
        child_unique.append(c)
report["child_references"] = {"count": len(child_unique), "values": child_unique}

# --- G) Cryptocurrency-related strings ---
crypto_keywords = re.compile(
    r'(?:wallet|coin|token|usdt|tron|trx|withdraw|deposit|recharge)',
    re.IGNORECASE
)
crypto_matches = []
for m in crypto_keywords.finditer(source):
    start = max(0, m.start() - 30)
    end = min(len(source), m.end() + 30)
    context = source[start:end].replace('\n', ' ')
    crypto_matches.append(context.strip())
crypto_unique = sorted(set(crypto_matches))
report["crypto_references"] = {"count": len(crypto_unique), "values": crypto_unique}

# --- H) API keys, tokens, secrets ---
secret_patterns = [
    (r'firebase', re.compile(r'''[^\n]{0,40}firebase[^\n]{0,80}''', re.IGNORECASE)),
    (r'agora', re.compile(r'''[^\n]{0,40}agora[^\n]{0,80}''', re.IGNORECASE)),
    (r'rtc', re.compile(r'''[^\n]{0,20}(?:rtc|RTC)[^\n]{0,60}''')),
    (r'appid', re.compile(r'''[^\n]{0,20}(?:appId|AppID|SDKAppID|appid)[^\n]{0,60}''')),
    (r'apikey', re.compile(r'''[^\n]{0,20}(?:apikey|api_key|apiKey|API_KEY)[^\n]{0,60}''', re.IGNORECASE)),
    (r'secret', re.compile(r'''[^\n]{0,20}(?:secret|SECRET)[^\n]{0,60}''')),
    (r'password_config', re.compile(r'''[^\n]{0,20}(?:password|Password)[^\n]{0,60}''')),
]
secrets_found = {}
for label, pat in secret_patterns:
    matches = sorted(set(m.strip() for m in pat.findall(source)))
    if matches:
        secrets_found[label] = {"count": len(matches), "values": matches}
report["api_keys_tokens_secrets"] = secrets_found

# --- I) Summary counts ---
report["summary"] = {
    "total_unique_routes": len(routes),
    "total_unique_domains": len(domains),
    "total_unique_urls": len(urls),
    "total_unique_ip_addresses": len(ips),
    "total_unique_tron_addresses": len(tron_addresses),
    "total_unique_geo_codes": len(geo_codes),
    "total_child_references": len(child_unique),
    "total_crypto_references": len(crypto_unique),
}

OUTPUT_FILE = "AUTOMATED_EXTRACTION_REPORT.json"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print(f"Extraction complete. Output: {OUTPUT_FILE}")
print(f"Source file: {SOURCE_FILE}")
print(f"Routes: {len(routes)}")
print(f"URLs: {len(urls)}")
print(f"Domains: {len(domains)}")
print(f"IPs: {len(ips)}")
print(f"TRON addresses: {len(tron_addresses)}")
print(f"Geo/region codes: {len(geo_codes)}")
print(f"CORS configs: {len(cors_configs)}")
print(f"Child references: {len(child_unique)}")
print(f"Crypto references: {len(crypto_unique)}")
