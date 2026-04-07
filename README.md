# 🔴 PROJECT DRAGON 403

### Forensic Evidence Repository — HILO/FALLA Fraud Network
**Case Reference:** `6-3808000039722`

[![Case Status](https://img.shields.io/badge/Case-ACTIVE-red)]() 
[![Victims](https://img.shields.io/badge/Victims-2%2C000+-critical)]() 
[![Losses](https://img.shields.io/badge/Losses-Millions%2FBillions%20SAR-red)]() 
[![Filed With](https://img.shields.io/badge/Filed-FBI%20%7C%20FTC%20%7C%20CISA%20%7C%20NCA%20%7C%20SAMA-blue)]()

## ⚠️ EXECUTIVE SUMMARY
This repository is the primary cryptographic and architectural archive for Project Dragon 403. Our forensic extraction (March 2026) confirms that this is not an isolated incident, but a monolithic multi-app ecosystem (70+ cloned apps) engineered to bypass Saudi/GCC financial gateways, groom minors, and extract capital through a Shadow Banking pipeline.

---

## 🔐 CHAIN OF CUSTODY & EVIDENCE INTEGRITY (HASH TABLE)
To ensure absolute cryptographic integrity and prevent any claims of tampering, all primary artifacts in this repository are anchored by SHA-256 hashes. Any modification to these files will invalidate the hash.

| Artifact File | Evidence Type | SHA-256 Checksum |
|---------------|---------------|------------------|
| `falla_admin.js` | Monolithic Backend Router | `71bf18bf6be88fc7afb4a0d5ae668148` |
| `extracted_tron_addresses.json` | Shadow Banking Exit Nodes | `f6037e04a9501fe094e70e2b5c5c6459a1cded2faef9422b9f689e102347018f` |

**Verification Methodology for Regulators:**
Investigators can independently verify these artifacts by downloading the files and running: `sha256sum <filename>` on Linux/macOS or `Get-FileHash <filename>` on Windows.

---

## 🚨 INDEPENDENT ARCHITECTURAL AUDIT (SEC-OPS)
**Target Object:** `falla_admin.js` (Central Monolithic Router: `adm-api-33356`)

An independent architectural security audit has confirmed catastrophic, deliberate structural flaws in the platform's backend:

### 1. Broken Access Control & Child Endpoints (Critical)
`/childAdmin` and `/childChat` are co-located on the exact same router as `agentCoinNotEnough` (a virtual currency liquidity flag) and `award`. There is **zero domain boundary** between child-interaction surfaces and financial transaction logic. 
* **The Exploit:** Combined with the hardcoded `corsHeader: "Origin: *"`, any external origin can make credentialed cross-origin requests to child-facing endpoints. 
* **Forensic Conclusion:** Architecturally, the platform cannot separate child interaction from financial incentive flows. This is the technical signature of a system where grooming/rewarding minors is a deliberate feature.

### 2. Insecure Direct Object Reference (High)
UID queries are handled without rate-limiting, making sequential enumeration of user IDs trivial. 
* **The Exploit:** Enables malicious actors to scrape a complete database of users (including minors).
* **Aggravating Factor:** The 11-tier `SVIP` system exposes tier metadata, allowing the correlation of UID enumeration with spending levels to identify high-value targets.

### 3. Saudi PDPL & Sovereignty Violation
The hardcoded inclusion of `SA_SA` and `AR_GCC` geo-filters confirms deliberate targeting of Saudi and Gulf users.
* **Compliance Failure:** A monolithic router with no domain separation violates Saudi Arabia’s Personal Data Protection Law (PDPL) and National Cybersecurity Authority (NCA) mandates structurally. It is unpatchable without a total redesign.

---

## ⛓️ FINANCIAL LAYER — THE TRON FUNNEL
The real internal movement of extracted capital happens on the TRON Blockchain. We have extracted **33 target addresses** hardcoded/utilized as intermediate nodes to launder SAR deposits (via Codashop/STC Pay/Mada) into USDT.

**Primary Extracted Exit Wallets (Sample of 7 active nodes):**
1. `TCHFcsY7VqTq35c9zZPzKo7JtfNYVAryfu`
2. `Tf7rkg7L6TuTtyMGs5xe1dJEPsOyggnhLa`
3. `TRyz6SjiPcHVNh8JLrf5vOVZKGSJb4mjTF`
4. `TuDAOIbYAj7JoD4vutLdgYBxDfAEPZNAPF`
5. `TuSCebQRIvNR3qzAReKfJ7LtSjoUY8gqeJ`
6. `TvywOOaMlXDiRkNSiBJ8kYCV8WY5zmsin3`
7. `TNVkg3pxm3pkshfolcmx97La1qqrd9dnOW`

*(The complete array of all 33 addresses is documented in `extracted_tron_addresses.json`)*

---

## 📂 REPOSITORY ARCHITECTURE
- **/hilo_dissection/** — Decompiled app logic and API analysis.
- **/root_files/** — Core evidence recovered from the investigation (`falla_admin.js`, leaked keys).
- **/target_shakhl/** — Infrastructure fingerprints and fuzzing results.
- **extracted_tron_addresses.json** — TRON funnel wallets.

## ⚖️ LEGAL & REGULATORY STATUS
Formal cyber incident reports and forensic payloads are active and escalating with:
- **US FTC** (#199332032)
- **CISA** (ae92fcd1)
- **Action Fraud UK** (RF26030165360C)
- **Saudi NCA & SAMA** (Active Priority Escalation)

---
**Investigator:** Sulaiman Alshammari (Dragon403)
**Lab:** KHAWRIZM Forensic Labs, Riyadh, KSA 🇸🇦
**Sovereign Principle:** *The Algorithm Always Returns Home.*
