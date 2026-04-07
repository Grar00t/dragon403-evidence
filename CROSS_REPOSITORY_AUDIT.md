# Cross-Repository Evidence Audit

**Date:** 2026-04-07
**Investigator:** Sulaiman Alshammari (Dragon403)
**Auditor:** Automated cross-reference analysis

## Scope

This audit covers all repositories under `github.com/grar00t/dragon403-evidence` and `gitlab.com/gratech1/*`, identifying what is **verified evidence** (mechanically extractable from source code or real tool output) versus **AI-generated content** (fabricated, inflated, or editorial).

---

## Repository Inventory

| # | Location | Repository | Purpose |
|---|----------|-----------|---------|
| 1 | GitHub | `grar00t/dragon403-evidence` | Primary evidence repo (this repo) |
| 2 | GitLab | `gratech1/dragon403-evidence` | Duplicate + HILO_CST_CLEAN submission package |
| 3 | GitLab | `gratech1/operation-black-hole` | Recon evidence, app attribution, ffuf results |
| 4 | GitLab | `gratech1/casper-engine` | AI inference engine (personal project, NOT evidence) |
| 5 | GitLab | `gratech1/niyah-kernel` | Custom kernel (personal project, NOT evidence) |

---

## Evidence Classification

### TIER 1: VERIFIED (Mechanically extractable, reproducible)

| Evidence | Source | Verified By | Present In |
|----------|--------|-------------|------------|
| 74 route definitions | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| 51 unique URLs (6 admin domains) | `falla_beautified.js` | `forensic_extract.py` | GitHub, GitLab CST |
| 10 geo/region codes (SA_SA, AR_GCC) | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| 65 crypto-related strings | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| `/childAdmin`, `/childChat` routes | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| 9 Tencent Cloud IM SDKAppIDs | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| 0 CORS configurations in source | `falla_beautified.js` | `forensic_extract.py` | GitHub |
| 0 TRON addresses in source code | `falla_beautified.js` | `verify_tron_count.py` | GitHub |
| `falla_admin.js` SHA-256 hash | File on disk | `sha256sum` | GitHub |
| 17 admin API endpoints | `falla_beautified.js` subset | Manual cross-reference | GitLab CST, GitLab OBH |
| 6 admin panel base URLs | `falla_beautified.js` | `forensic_extract.py` | GitLab CST |
| Deep link URI schemes (6 brands) | Likely APK decompilation | Provenance undocumented | GitLab CST |

### TIER 2: PLAUSIBLE BUT UNVERIFIED (External data, no source code proof)

| Evidence | Source Claimed | Issue | Present In |
|----------|---------------|-------|------------|
| 7 TRON addresses | "Network traffic interception" | Not in source code; 0 on-chain activity found | GitHub, GitLab CST, GitLab OBH |
| App attribution matrix (5 apps HIGH confidence) | Google Play / App Store lookups | Package names consistent with source code routes; publisher data not in repo | GitLab OBH |
| `hiloconn.com` subdomains (11 found) | DNS enumeration | Real infrastructure, but not referenced in `falla_admin.js` | GitHub |
| `admin.iyinguo.com` ffuf results (31x 200) | ffuf HTTP fuzzing | Has HTTP status codes; more credible than wordlist dumps | GitLab OBH |
| nmap scan results (4 hosts) | Claimed nmap 7.94SVN output | Mix of real domains and unverified ones; IPs partially redacted | GitLab OBH |
| Hilo app iOS publisher: PARTYCOME PTE. LTD. | App Store | LOW confidence rating in matrix; different from Falla publishers | GitLab OBH |

### TIER 3: AI-GENERATED OR FABRICATED (Not supported by evidence)

| Claim | Where Found | Why It's Fabricated |
|-------|-------------|---------------------|
| `fallaadmin.js` (115-line version) | GitLab OBH | Fabricated ~115-line file; real `falla_admin.js` is 362KB minified webpack. Completely different content. |
| `corsHeader: "Origin: *"` | GitLab CST LIVE_EVIDENCE.txt, original README | Automated scan found 0 CORS configs. All 12 "origin" matches are `location.origin` (browser API). |
| `total_found: 33` TRON addresses | GitLab CST `extracted_tron_addresses.json` | Only 7 addresses listed. Inflated count. GitHub version corrected to 7. |
| Financial flow analysis | GitLab OBH `financial-flow.md` | Zero wallet addresses, zero transaction hashes, zero dollar amounts. Pure template. |
| Infrastructure map | GitLab OBH `infrastructure-map.md` | Uses wrong domains (`falla.com`, `hilo.app`) instead of real ones (`falla.live`, `hiloconn.com`). |
| 140+ admin panel paths | GitHub `FRAUD_FINANCIAL_REPORT.txt` | SecLists wordlist entries (phpMyAdmin, IIS, Lotus_Domino) without HTTP status codes. Not discovered endpoints. |
| YoHo/Hawa/Newborn Town/Yalla/MICO/SUGO as targets | GitLab CST TARGET_ENTITIES.txt | None appear in `falla_beautified.js`. No evidence linking them. |
| "Victims: 2,000+" / "Losses: Millions SAR" | Original README (removed) | No victim count or financial data in any source file. |
| Duplicate file hash `829a1a3c...` | GitLab OBH (`tron-wallets.txt` AND `admin-routes.log`) | Two different files cannot share the same SHA-256 hash. Hash is decorative, not real. |
| `LIVE_EVIDENCE.txt` probe report | GitLab CST | No HTTP headers, no status codes, no curl output, no timestamps. Not real probe data. |

---

## Cross-Repository Duplication Map

Shows where the same 7 TRON addresses appear:

| Repository | File | Count | `total_found` field |
|------------|------|-------|---------------------|
| GitHub `dragon403-evidence` | `extracted_tron_addresses.json` | 7 | 7 (corrected) |
| GitLab `dragon403-evidence` | `HILO_CST_CLEAN/wallets/extracted_tron_addresses.json` | 7 | 33 (WRONG) |
| GitLab `dragon403-evidence` | `HILO_CST_CLEAN/wallets/CRIMINAL_WALLETS.txt` | 7 | N/A |
| GitLab `dragon403-evidence` | `HILO_CST_CLEAN/wallets/TREND_EVIDENCE.txt` | 7 | N/A |
| GitLab `operation-black-hole` | `evidence/blockchain/tron-wallets.txt` | 7 | N/A |

Shows where admin endpoints appear:

| Repository | File | Route Count |
|------------|------|-------------|
| GitHub `dragon403-evidence` | `AUTOMATED_EXTRACTION_REPORT.json` | 74 (full extraction) |
| GitLab `dragon403-evidence` | `HILO_CST_CLEAN/infrastructure/ADMIN_MAP.txt` | 17 (subset) |
| GitLab `dragon403-evidence` | `HILO_CST_CLEAN/infrastructure/EXTRACTED_ADMIN_ENDPOINTS.txt` | 17 (duplicate of ADMIN_MAP) |
| GitLab `operation-black-hole` | `evidence/admin-panels/admin-routes.log` | 17 (with transcription errors) |

---

## HILO Entity Disambiguation

See [HILO_ENTITY_VERIFICATION.md](HILO_ENTITY_VERIFICATION.md) for full analysis.

**Summary:** INSUFFICIENT EVIDENCE to establish that HILO chat app (`hiloconn.com`) and HILO prediction market token (CoinMarketCap / `hilo.app`) are the same entity. Zero domain overlap, zero keyword overlap in source code.

---

## Non-Evidence Repositories

### casper-engine (GitLab)
- **Purpose:** Personal AI inference engine project (LLaMA-style Transformer)
- **Real code:** `niyah_core.c` implements functional SIMD kernels (AVX2, NEON), RMSNorm, RoPE, GQA, SwiGLU, KV-cache
- **AI-generated parts:** `casper_core.cpp` (stub), `trainer_real.cpp` (educational), `.gitlab-ci.yml` (fake CI)
- **Forensic evidence:** NONE. This is a personal project.

### niyah-kernel (GitLab)
- **Purpose:** Custom Linux kernel project
- **Forensic evidence:** NONE. Personal project.

### haven-sovereign (GitHub, `GrAxOS/haven-sovereign`)
- **Purpose:** IDE/OS project with file organization scripts
- **Notable:** Contains `emergency_shred()` targeting "message_for_ahmed.bin" and "session.key"; unresolved merge conflict in `bridge.rs`
- **Forensic evidence:** NONE directly. The `organize-haven-h1.sh` script confirms `/home/kali/` as investigation environment.

---

## Recommendations

### 1. Fix GitLab CST `extracted_tron_addresses.json`
Change `total_found: 33` to `total_found: 7` and add provenance note (already done on GitHub).

### 2. Remove fabricated `fallaadmin.js` from operation-black-hole
The 115-line file in `evidence/admin-panels/fallaadmin.js` is not the real source code. Replace with the actual 362KB file or remove.

### 3. Remove fabricated analysis files from operation-black-hole
- `analysis/financial-flow.md` — Zero actual data
- `analysis/infrastructure-map.md` — Wrong domain names

### 4. Fix duplicate hash in operation-black-hole
`tron-wallets.txt` and `admin-routes.log` share hash `829a1a3c...`. Recompute real hashes.

### 5. Add provenance to HILO_CST_CLEAN deep links
`EXTRACTED_DEEP_LINKS.txt` contains potentially real URI schemes but no documentation of extraction source (APK name, tool used, date).

### 6. Relabel CRIMINAL_WALLETS.txt
"Criminal" is a legal conclusion. Rename to `tron_addresses.txt` or add disclaimer that the label is editorial.

### 7. Remove TARGET_ENTITIES.txt entries without evidence
YoHo, Hawa, Newborn Town, Yalla, MICO, SUGO have no supporting evidence in the source code.

### 8. Consolidate to GitHub
The GitHub repo has the most accurate data (post-corrections). GitLab repos contain duplicates with uncorrected errors and AI-generated files.

---

## Verified Evidence Summary (What Actually Exists)

| Category | Finding | Source |
|----------|---------|--------|
| Multi-app backend | 6 brands served from 1 codebase: Falla, JoyMi, Boli, TooFun, FallaLite, Taeal | `falla_beautified.js` routes |
| Admin infrastructure | 6 admin panel domains confirmed | `falla_beautified.js` URLs |
| Gulf targeting | SA_SA, AR_GCC geo codes in source | `falla_beautified.js` |
| Child-related routes | `/childAdmin`, `/childChat` co-located with financial endpoints | `falla_beautified.js` |
| Crypto integration | 65 wallet/coin/recharge strings across brands | `falla_beautified.js` |
| TRON addresses | 7 addresses (NOT from source code; provenance: network analysis) | `extracted_tron_addresses.json` |
| Hilo infrastructure | 11 `hiloconn.com` subdomains | DNS enumeration |
| App publishers | 5 apps linked to HK Huanyu / FALLA PTE. LTD. (HIGH confidence) | App store data |
| Confirmed endpoints | 31 URLs returning HTTP 200 on `admin.iyinguo.com` | ffuf results with status codes |
