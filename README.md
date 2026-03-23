<![CDATA[<div align="center">

# 🔴 PROJECT DRAGON 403

### Forensic Evidence Repository — HILO/FALLA Fraud Network

**Case Reference:** `6-3808000039722`

[![Case Status](https://img.shields.io/badge/Case-ACTIVE-red)]()
[![Victims](https://img.shields.io/badge/Victims-2%2C000+-critical)]()
[![Losses](https://img.shields.io/badge/Losses-600%2C000+%20SAR-red)]()
[![Filed With](https://img.shields.io/badge/Filed-FBI%20%7C%20FTC%20%7C%20CISA%20%7C%20Europol%20%7C%20Interpol-blue)]()
[![License](https://img.shields.io/badge/License-Public%20Evidence-green)]()

</div>

---

## Overview

This repository contains raw forensic evidence collected during the investigation of a **Chinese-operated pig-butchering fraud network** targeting Gulf Arab victims through fake social/dating applications (**HILO**, **FALLA**, **VoChat**) and a fraudulent cryptocurrency token (**HILO Token V2** on Ethereum).

The investigation was conducted by **Sulaiman Alshammari (Dragon403)** of **KHAWRIZM Forensic Labs**, Riyadh, Kingdom of Saudi Arabia.

---

## نظرة عامة

يحتوي هذا المستودع على أدلة جنائية رقمية خام تم جمعها خلال التحقيق في **شبكة احتيال صينية** تستهدف ضحايا الخليج العربي عبر تطبيقات اجتماعية مزيفة (**HILO**، **FALLA**، **VoChat**) وعملة رقمية احتيالية (**HILO Token V2** على شبكة Ethereum).

التحقيق أجراه **سليمان الشمري (Dragon403)** من **مختبرات خوارزم الجنائية**، الرياض، المملكة العربية السعودية.

---

## The Fraud Network

```
┌─────────────────────────────────────────────────────────────┐
│                    ACEVILLE PTE LTD                          │
│                  (Singapore Entity)                          │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │  HILO    │  │  FALLA   │  │  VoChat  │  │  HILO      │  │
│  │  App     │  │  App     │  │  App     │  │  Token V2  │  │
│  │ (Dating) │  │ (Social) │  │ (Voice)  │  │ (Ethereum) │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └─────┬──────┘  │
│       │             │             │               │         │
│       └─────────────┴─────────────┘               │         │
│                     │                             │         │
│            Pig-Butchering                  Token Fraud       │
│            (Social Engineering)           (Smart Contract)   │
│                     │                             │         │
│                     ▼                             ▼         │
│              2,000+ Victims                Ghost Admin       │
│              600,000+ SAR                 (0xB843F5...)     │
└─────────────────────────────────────────────────────────────┘
```

---

## Ethereum Contract Evidence

### HILO Token V2 — Smart Contract Architecture

| Component | Address | Risk |
|-----------|---------|------|
| **Proxy Contract** | [`0x6c3fE25a4de7FA243c653cfE1F165bf11D99704E`](https://etherscan.io/token/0x6c3fE25a4de7FA243c653cfE1F165bf11D99704E) | ERC1967 UUPSUpgradeable |
| **Implementation** | [`0x1475225bce629be110acf434acf6a2348bfe9d8f`](https://etherscan.io/address/0x1475225bce629be110acf434acf6a2348bfe9d8f#code) | Pausable + Blacklist + Upgrade |
| **Ghost Admin** | [`0xB843F547a8a46a9483cf46c757c7eF4220115A83`](https://etherscan.io/address/0xB843F547a8a46a9483cf46c757c7eF4220115A83) | 0 TX, 0 ETH — Shadow Controller |
| **V1 Deployer** | [`0xd2a73f77654ce70d8618bbe1710f15a6e0d29748`](https://etherscan.io/address/0xd2a73f77654ce70d8618bbe1710f15a6e0d29748) | Funded by Binance 14 |
| **V2 Deployer** | [`0x2d47b6f9251de1dd7e260d042322b1a6a455332e`](https://etherscan.io/address/0x2d47b6f9251de1dd7e260d042322b1a6a455332e) | Deployed current implementation |
| **V1 Contract** | [`0xbb9FD9Fa4863C03c574007fF3370787B9cE65ff6`](https://etherscan.io/address/0xbb9FD9Fa4863C03c574007fF3370787B9cE65ff6) | Old HILO Token (migrated) |

### Dangerous Functions (Confirmed in Source Code)

| Function | Access | Rug Pull Vector |
|----------|--------|-----------------|
| `_authorizeUpgrade(address)` | `onlyOwner` | Replace entire contract logic instantly |
| `pause()` | `onlyOwner` | Freeze ALL transfers (honeypot trigger) |
| `blacklist(address)` | `onlyOwner` | Block any wallet from transacting |
| `upgradeToAndCall(address, bytes)` | `onlyOwner` | Upgrade + execute arbitrary code in 1 tx |

### Team-Controlled Holdings

| Holder | Balance | % Supply | Connection |
|--------|---------|----------|------------|
| `0x8D52Ac52...` | 20,000,000 HILO | 13.33% | Funded by `hilolp.eth` (deployer team) |
| `0x5a87Ae3E...` | 4,261,891 HILO | 2.84% | Contract created by `hilorewards.eth` |
| **Total Team** | **24,261,891 HILO** | **16.17%** | Direct deployer control |

### Liquidity Status

| Field | Value |
|-------|-------|
| Pool | Uniswap V3: HILO/WETH |
| Liquidity | $119,000 |
| Locked Via | UNCX Network |
| **Lock Expiry** | **26 May 2026** |
| 24h Volume | ~$900 (dormant) |

> **⚠️ CRITICAL:** After 26 May 2026, the Ghost Admin can execute: upgrade → pause → mint → dump → drain liquidity. Dragon 403 Pattern Match: **94%**.

---

## Repository Contents

### `/hilo_dissection/`
Decompiled HILO application components, API endpoints, and internal configuration analysis.

### `/hilo_final_shakhl/`
Final network reconnaissance results against HILO infrastructure — headers, server fingerprints, exposed endpoints.

### `/target_shakhl/`
Falla.live infrastructure scans — HTTP headers, fuzzing results, target enumeration.

### `/root_files/`
Core evidence files recovered from investigation environment:
- `admin_logic.js` — Admin panel logic extraction
- `hidden_apis.txt` — Undocumented API endpoints discovered
- `leaked_keys.txt` — Exposed API keys and credentials found in app
- `network_map.txt` — Infrastructure network mapping
- `hilo_report.html` — Formatted investigation report
- `llama_forensics.py` — AI-assisted forensic analysis script

### Forensic Reports
| File | Description |
|------|-------------|
| `FULL_FORENSIC_REPORT.txt` | Complete technical forensic report (18.8 KB) |
| `FINAL_EXPOSURE_REPORT.txt` | Full exposure documentation (1.8 MB) |
| `FRAUD_FINANCIAL_REPORT.txt` | Financial fraud analysis (8.5 KB) |
| `FORENSIC_CRYPTO_REPORT.json` | Cryptocurrency forensic findings |
| `FINAL_SUBMISSION.md` | Case submission document |

### Investigation Scripts
| File | Description |
|------|-------------|
| `scan_falla.py` | Falla infrastructure scanner |
| `scan_hiloconn.py` | HILO connection analyzer |
| `hawrizm_wallet_tracker.py` | Cryptocurrency wallet tracking tool |
| `hiloid.py` | HILO identity analysis tool |
| `hilointel.py` | HILO intelligence gathering tool |
| `cert_check.py` | SSL certificate verification |
| `final_check.py` / `final_check_v2.py` | Final verification scripts |
| `decode_hex_test.py` | Hex payload decoder |
| `generate_report.py` | Automated report generator |

### Raw Evidence
| File | Description |
|------|-------------|
| `falla_admin.js` | Falla admin panel source (decompiled) |
| `falla_beautified.js` | Falla app source — beautified (918 KB) |
| `dragon403_results.json` | Investigation results index |
| `extracted_tron_addresses.json` | TRON blockchain addresses extracted |
| `sensitive_shakhl.json` | Target infrastructure fingerprints |
| `all_clean_targets.txt` | Validated target list |
| `big_loot.txt` | Discovered endpoints and data |
| `final_hilo_falla_clean.txt` | Cleaned HILO/FALLA evidence correlation |
| `contradiction_check.txt` | Cross-reference contradiction analysis |

---

## Investigation Timeline

| Date | Event |
|------|-------|
| **Dec 2022** | V1 Deployer funded by Binance 14 — HILO V1 contract deployed |
| **Sep 2024** | HILO V2 Implementation deployed (UUPSUpgradeable) |
| **Oct 2024** | V1 → V2 migration initiated |
| **Mar 2, 2026** | Kali forensic evidence collection begins |
| **Mar 8, 2026** | Network reconnaissance (httpx, ffuf) against HILO/FALLA infrastructure |
| **Mar 10, 2026** | Blockchain forensics — TRON address extraction, wallet tracking |
| **Mar 12, 2026** | Final evidence organization — hilo_dissection, target_shakhl |
| **Mar 14, 2026** | Forensic scripts finalized (hiloid, hilointel, cert_check) |
| **Mar 20, 2026** | Case filings submitted to international agencies |
| **Mar 23, 2026** | Ethereum contract audit completed — Ghost Admin identified |
| **Mar 23, 2026** | Recovery Evidence Letter generated for MEXC Compliance |
| **May 26, 2026** | ⚠️ **UNCX Liquidity Lock Expires** — Critical date |

---

## Case Filings

| Agency | Reference | Status |
|--------|-----------|--------|
| **FBI IC3** (USA) | Filed | ✅ Submitted |
| **FTC** (USA) | `#199332032` | ✅ Confirmed |
| **CISA** (USA) | `ae92fcd197b7b2109ea1b247f053afca` | ✅ Confirmed |
| **Europol** (EU) | Filed | ✅ Submitted |
| **Interpol** | Filed | ✅ Submitted |
| **Action Fraud UK** | `RF26030165360C` | ✅ Confirmed |
| **Google Safe Browsing** | 7 domains reported | ✅ Submitted |
| **Google Play** | VoChat takedown request | ✅ Submitted |
| **Apple App Store** | Fraud app report | ✅ Submitted |
| **Polygon Security** | HILO token report | ✅ Submitted |
| **MEXC Compliance** | Account Freeze Request | 📧 Pending |

---

## Addresses to Freeze

### Priority 1 — Immediate

| Address | Role |
|---------|------|
| `0xB843F547a8a46a9483cf46c757c7eF4220115A83` | Ghost Admin — controls upgrade, pause, blacklist |
| `0x8D52Ac5264917f811F2768339cc2Aa231F51a8C3` | Team wallet — 20M HILO funded by hilolp.eth |
| `0x5a87Ae3E337f9319434C51Ef2a73B6957352e917` | Team contract — 4.3M HILO by hilorewards.eth |

### Priority 2 — Investigation

| Address | Role |
|---------|------|
| `0xd2a73f77654ce70d8618bbe1710f15a6e0d29748` | V1 Deployer — funded by Binance 14 |
| `0x2d47b6f9251de1dd7e260d042322b1a6a455332e` | V2 Deployer — set Ghost Admin |
| `0x9642b23Ed1e01Df1092B92641051881A322F5d4e` | MEXC 16 — 1.95M HILO exit point |

---

## Investigator

**KHAWRIZM Forensic Labs** — Sulaiman Alshammari (سليمان الشمري)

| | |
|---|---|
| **Alias** | Dragon403 |
| **Entity** | Ghala Rafaa Al-Omari Trading Co. (CR 7050426415) |
| **Website** | [khawrizm.com](https://khawrizm.com) |
| **Email** | [admin@gratech.sa](mailto:admin@gratech.sa) |
| **X** | [@khawrzm](https://x.com/khawrzm) |
| **YouTube** | [@saudicyper](https://youtube.com/@saudicyper) |
| **GitHub** | [@Grar00t](https://github.com/Grar00t) |
| **Location** | Kingdom of Saudi Arabia 🇸🇦 |

---

## Related Repositories

- [`haven-sovereign`](https://github.com/Grar00t/haven-sovereign) — HAVEN IDE & Sovereign AI Platform
- [`haven-niyah-engine`](https://github.com/Grar00t/haven-niyah-engine) — NIYAH Arabic-First AI Engine

---

## Legal Notice

This repository is published as **public forensic evidence** for law enforcement, regulatory agencies, and cybersecurity researchers. All evidence was collected through:

- Publicly accessible APIs and endpoints
- Open-source intelligence (OSINT) techniques
- Blockchain analysis of public ledger data
- Decompilation of publicly distributed mobile applications

No unauthorized access to private systems was performed. This evidence is provided in good faith to support the investigation and prosecution of the HILO/FALLA fraud network.

---

<div align="center">

**المختبر الجنائي السيادي**

*"The algorithm found the thief. The map is drawn. The job is done."*

**الخوارزمية وجدت اللص. الخريطة رُسمت. المهمة انتهت.**

🐾

</div>
]]>