# PROJECT DRAGON 403

### Forensic Evidence Repository — HILO/FALLA Fraud Network
**Case Reference:** `6-3808000039722`

[![Case Status](https://img.shields.io/badge/Case-ACTIVE-red)]()
[![Filed With](https://img.shields.io/badge/Filed-FBI%20%7C%20FTC%20%7C%20CISA%20%7C%20NCA%20%7C%20SAMA-blue)]()

## EXECUTIVE SUMMARY
This repository is the primary cryptographic and architectural archive for Project Dragon 403. Forensic extraction (March 2026) recovered backend source code, configuration artifacts, and blockchain address references from the HILO/FALLA platform ecosystem.

---

## CHAIN OF CUSTODY & EVIDENCE INTEGRITY (HASH TABLE)
All primary artifacts in this repository are anchored by SHA-256 hashes. Any modification to these files will invalidate the corresponding hash.

| Artifact File | Evidence Type | SHA-256 Checksum |
|---------------|---------------|------------------|
| `falla_admin.js` | Backend Router Source | `71bf18bf6be88fc7afb4a0d5ae668148d0f75f080ec9e6a6956776bc865ad88d` |
| `falla_beautified.js` | Beautified Router Source | `22d73b1648119fd7c4dea92b9c99c127406eafce286e07f38b83d5cc237efab7` |
| `extracted_tron_addresses.json` | Extracted TRON Addresses | `ea61b6fff8ef9a61b93047bbb83ce6417dc7ab4f1f23b9cd86bc9570a80486e5` |
| `FORENSIC_CRYPTO_REPORT.json` | Crypto Report | `a4fb9d2d5ea8ec1fcc899f49a8d5cd9f5023154f113c0b53235b26bdb77a315f` |
| `FULL_FORENSIC_REPORT.txt` | Full Forensic Report | `2e697479a4050dbe67f29d5bbad6ee9d163bb34f6c2170c82290acfd188a7071` |
| `FINAL_SUBMISSION.md` | Final Submission | `114a9a46152cefef794f4dcfc7f59510c65c1a02fd8877f018642989d6f5dbc3` |
| `FINAL_EXPOSURE_REPORT.txt` | Exposure Report | `a9ee8db17644572a988a38c990b6521f36705dedf0f638f086250e084b49053c` |
| `dragon403_results.json` | Investigation Results | `f4ddcad665fc55afda79a56c7511982f5ea52cdb2c934326c09c737e6be05cbf` |

**Verification:** Investigators can independently verify these artifacts by running: `sha256sum <filename>` on Linux/macOS or `Get-FileHash <filename>` on Windows.

---

## RAW EVIDENCE — Strings and Structures Found in Source Files

The following are literal strings, route definitions, and configuration values present in `falla_admin.js`:

- Route definitions `/childAdmin` and `/childChat` exist on the same Express router as `agentCoinNotEnough` and `award`.
- The string `corsHeader: "Origin: *"` is hardcoded in the source.
- UID query endpoints exist without rate-limiting middleware in the routing layer.
- An 11-tier `SVIP` system is defined with tier metadata exposed in API responses.
- Geo-filter strings `SA_SA` and `AR_GCC` are present in the codebase.

---

## ANALYSIS & INTERPRETATION

> An architectural analysis of the routing definitions was conducted. Findings are reproducible by any qualified security engineer using the artifacts in this repository.

See [ARCHITECTURAL_ANALYSIS.md](ARCHITECTURAL_ANALYSIS.md) for the full analysis. Key findings:

### 1. Access Control Observations (Critical)
The co-location of `/childAdmin`, `/childChat`, `agentCoinNotEnough`, and `award` on a single router means there is no domain boundary between child-interaction surfaces and financial transaction logic. Combined with `corsHeader: "Origin: *"`, any external origin could make cross-origin requests to these endpoints.

### 2. Insecure Direct Object Reference (High)
UID queries lack rate-limiting in the routing layer, making sequential enumeration of user IDs possible. The `SVIP` tier metadata could allow correlation of UIDs with spending levels.

### 3. Saudi PDPL & Sovereignty Concerns
The presence of `SA_SA` and `AR_GCC` geo-filters indicates targeting of Saudi and Gulf users. A monolithic router with no domain separation raises structural compliance concerns under Saudi Arabia's Personal Data Protection Law (PDPL) and NCA mandates.

---

## FINANCIAL LAYER — TRON ADDRESSES

7 TRON addresses are listed in `extracted_tron_addresses.json`:

1. `TCHFcsY7VqTq35c9zZPzKo7JtfNYVAryfu`
2. `Tf7rkg7L6TuTtyMGs5xe1dJEPsOyggnhLa`
3. `TRyz6SjiPcHVNh8JLrf5vOVZKGSJb4mjTF`
4. `TuDAOIbYAj7JoD4vutLdgYBxDfAEPZNAPF`
5. `TuSCebQRIvNR3qzAReKfJ7LtSjoUY8gqeJ`
6. `TvywOOaMlXDiRkNSiBJ8kYCV8WY5zmsin3`
7. `TNVkg3pxm3pkshfolcmx97La1qqrd9dnOW`

Address count verified by automated extraction (verify_tron_count.py): 0 TRON addresses found in `falla_admin.js` / `falla_beautified.js`. The 7 addresses listed above are present only in `extracted_tron_addresses.json`; their origin is not traceable to the source code in this repository. The original claim of 33 addresses has been corrected to 7.

---

## REPOSITORY ARCHITECTURE
- **/hilo_dissection/** — Decompiled app logic and API analysis.
- **/root_files/** — Core evidence recovered from the investigation (`falla_admin.js`, leaked keys).
- **/target_shakhl/** — Infrastructure fingerprints and fuzzing results.
- **extracted_tron_addresses.json** — Extracted TRON addresses.

## LEGAL & REGULATORY STATUS
Formal cyber incident reports and forensic payloads are active with:
- **US FTC** (#199332032)
- **CISA** (ae92fcd1)
- **Action Fraud UK** (RF26030165360C)
- **Saudi NCA & SAMA** (Active Priority Escalation)

---

## KNOWN LIMITATIONS

- **Hash corrections applied:** The original README listed an MD5 hash (32 characters) labeled as SHA-256 for `falla_admin.js`. All hashes in this version were recomputed using `sha256sum`.
- **Address count corrected:** `extracted_tron_addresses.json` originally claimed `total_found: 33` but listed only 7 addresses. Automated extraction found 0 TRON addresses in the source code. `total_found` corrected to 7.
- **Analysis not independently verified:** The architectural analysis in this repository was conducted by the investigator. It has not been reviewed or confirmed by an independent third party.
- **TRON address on-chain activity:** The 7 listed TRON addresses showed zero on-chain activity as of last check.

---
**Investigator:** Sulaiman Alshammari (Dragon403)
**Lab:** KHAWRIZM Forensic Labs, Riyadh, KSA
