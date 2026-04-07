# HILO Entity Verification Report

## Purpose

Determine whether "HILO" as referenced in this investigation (a video chat/social app ecosystem) and "HILO" as listed on CoinMarketCap (a prediction market token) are the same entity, different entities, or if the evidence is insufficient to determine.

---

## Entity A: HILO Chat App (This Investigation)

### Domains found in repository artifacts (NOT in falla_admin.js):

Source: `hilo_final_shakhl/hiloconn_subs.txt`, `FULL_FORENSIC_REPORT.txt`, `scan_hiloconn.py`

| Subdomain | Function |
|-----------|----------|
| hiloconn.com | Root domain |
| www.hiloconn.com | Website |
| api.hiloconn.com | API |
| ws.hiloconn.com | WebSocket (chat) |
| v.hiloconn.com | Video |
| image.hiloconn.com | CDN |
| grafana.hiloconn.com | Monitoring (Grafana) |
| promethues.hiloconn.com | Monitoring (Prometheus) |
| goploy.hiloconn.com | Deployment (Goploy) |
| teenpatti.hiloconn.com | Card game (Teen Patti) |
| test.teenpatti.hiloconn.com | Card game test env |

### Domains found in falla_admin.js / falla_beautified.js:

Source: `AUTOMATED_EXTRACTION_REPORT.json` (forensic_extract.py output)

- `falla.live`, `apifalla.com`, `fallaweb.com`
- `joymi.live`, `joymiweb.com`
- `apiboli.com`, `boli.live`
- `toofun.live`
- `fallalite.com`
- `taeal.live`
- `yigolive.com`

**"hilo" appears ZERO times in falla_admin.js or falla_beautified.js.**

### Ethereum contract referenced in investigation scripts:

- `hiloid.py` line 7: `HILO_CONTRACT = "0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e"`
- `hilointel.py` line 9: `HILO_CONTRACT = "0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e"`
- `hilointel.py` line 8: `TARGET_DOMAINS = ["hiloconn.com", "hilo.com", "res-g.resygg.com"]`

### Other references:
- `index.html` line 163: ASCII diagram shows "HILO TOKEN V2" with `(Proxy: 0x6c3f...)` alongside "FALLA LIVE ADMIN"
- `FINAL_EXPOSURE_REPORT.txt` line 5: "IP: 43.174.250.16 | Activity: Hilo/Falla WS & Payments"
- `root_files/hilo_report.html`: References `hiloconn.com` subdomains, mentions "hilo.apk"
- Package names referenced in investigation context: `com.juhaoliao.vochat`, `com.qiahao.nextvideo`

---

## Entity B: HILO Prediction Market Token (CoinMarketCap)

- Website: hilo.app
- Twitter: @Hilomarket (joined December 2022)
- Listed on: MEXC, Uniswap v3 (Ethereum), Uniswap v2
- CoinMarketCap rank: #4909
- Self-description: "No Risk Prediction App"
- Business type: Prediction market / betting platform

---

## Cross-Reference Analysis

### Domain overlap:

| Check | Entity A | Entity B | Match |
|-------|----------|----------|-------|
| Primary domain | hiloconn.com | hilo.app | NO |
| "hilo.app" in repo | Not found | hilo.app | NO |
| "hilomarket" in repo | Not found | @Hilomarket | NO |
| "hilo.com" in repo | Referenced in hilointel.py TARGET_DOMAINS | Unknown | UNVERIFIED |

### Keyword searches in falla_admin.js / falla_beautified.js:

| Search term | Matches |
|-------------|---------|
| hilo | 0 |
| hilo.app | 0 |
| hilomarket | 0 |
| predict / prediction | 0 |
| MEXC | 0 |
| uniswap | 0 |
| 0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e | 0 |

### Blockchain mismatch:

- Entity A investigation: TRON addresses (T-prefix, 34 chars) in `extracted_tron_addresses.json`
- Entity B (HILO token): Ethereum-based (listed on Uniswap, ETH DEX)
- Investigation scripts (`hiloid.py`): Reference Ethereum contract via Etherscan API
- The Ethereum contract `0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e` is referenced in the investigation but NOT found in falla_admin.js source code

### Infrastructure indicators:

- Entity A: Chinese-language comments in source (`hiloid.py`, `hilointel.py`), subdomains suggest Chinese tech stack (Goploy deployment tool), `teenpatti` subdomain (South Asian card game)
- Entity B: English-language prediction market app

---

## Conclusion

**INSUFFICIENT EVIDENCE to establish that Entity A and Entity B are the same entity.**

Reasons:
1. The word "hilo" is generic (Spanish for "thread"; also a common card game name "Hi-Lo")
2. Zero overlap between domains: `hiloconn.com` vs `hilo.app`
3. `hilo.app` appears nowhere in the repository
4. `hilomarket` appears nowhere in the repository
5. `predict`/`prediction`/`MEXC`/`uniswap` appear nowhere in the source code
6. The Ethereum contract `0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e` is hardcoded in investigation scripts (`hiloid.py`, `hilointel.py`) but not found in the actual evidence artifacts (`falla_admin.js`, `falla_beautified.js`). Its connection to either entity is not established by the source code evidence.
7. Entity A uses TRON blockchain addresses; Entity B is Ethereum-based

**What IS established:**
- `hiloconn.com` is an infrastructure domain enumerated during the investigation (subdomains, SSL certs, IP resolution)
- `hiloconn.com` is listed alongside Falla/Vochat domains in `FULL_FORENSIC_REPORT.txt` as part of the same network
- The connection between `hiloconn.com` and the Falla app ecosystem is documented in investigation artifacts but not proven by the `falla_admin.js` source code itself

**What is NOT established:**
- Whether `hiloconn.com` (chat app infrastructure) has any relationship to the HILO token on CoinMarketCap
- Whether the Ethereum contract `0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e` belongs to the `hiloconn.com` operators, the CoinMarketCap HILO token, or a third party
- Whether `hilo.com` (referenced in `hilointel.py`) is related to either entity

---

## Flagged References in Repository

The following files reference "HILO" in contexts that could create false attribution if Entity A and Entity B are different:

| File | Line | Content | Risk |
|------|------|---------|------|
| `index.html` | 163 | "HILO TOKEN V2" shown in network diagram alongside "FALLA LIVE ADMIN" | Implies HILO token is part of Falla fraud network without establishing the connection |
| `index.html` | 183 | "hilo_contract_audit.txt" window referencing `0x6c3f...` contract with `authorizeUpgrade()`, `pause()`, `blacklist()`, `mint()` | Presents contract functions as evidence of fraud without verifying contract ownership |
| `hiloid.py` | 7-68 | Hardcodes `HILO_CONTRACT` and generates conclusions about "HILO" and "Prince" identity | Script draws conclusions not supported by falla_admin.js evidence |
| `hilointel.py` | 8-9 | Targets `hilo.com` and the Ethereum contract as investigation targets | Assumes connection between domains and contract |
| `README.md` | 3,10 | "HILO/FALLA Fraud Network", "HILO/FALLA platform ecosystem" | Names HILO as part of the network; the name comes from `hiloconn.com` infrastructure, not from falla_admin.js |

---

## Recommendation

Before attributing blockchain token activity to the chat app operators:
1. Verify ownership of Ethereum contract `0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e` — is it the CoinMarketCap HILO, the hiloconn.com operators, or unrelated?
2. Check WHOIS / registration records for `hiloconn.com` vs `hilo.app` vs `hilo.com`
3. Do not present "HILO TOKEN V2" in diagrams linking it to Falla infrastructure until the connection is independently verified
