#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════╗
║         KHAWRIZM FORENSICS — TRON WALLET TRACKER         ║
║              DRAGON403 Investigation Unit                 ║
╚═══════════════════════════════════════════════════════════╝
"""

import requests
import time
import json
from collections import Counter
from datetime import datetime

# ── CONFIG ──────────────────────────────────────────────────
API_KEY = "4e6a2f6a-7fca-4762-a671-245b05bb78a0"
DELAY   = 0.5

USDT_CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"

TARGETS = [
    "TAxmp5SnUjnTVSn1eom4UunnYGpaYcDgaw",
    "TBzTWnHsaOLI6pIuWMIaCbEFseAFWPAYrH",
    "TNjW2NbetsSWbrfQjnHSo6qSYpAYCQfpSA",
    "TOxRa4GDcPaYaRmHA62GBMVKeglN75PVxJ",
    "TVzTGwxy5RDkCuB9zWSPAym72rL5DzZh64",
    "TBMfkGsAskCJMUsx4tdN94TIVDHmpaYWNI",
    "TuDAOIbYAj7JoD4vutLdgYBxDfAEPZNAPF",
    "TNQ6oZub28L3YDKteXl5mgPDg7GbqDpg3D",
]

HEADERS = {
    "Accept": "application/json",
    "TRON-PRO-API-KEY": API_KEY,
}

# ── HELPERS ──────────────────────────────────────────────────

def get_trc20_txns(address, limit=200):
    url = f"https://api.trongrid.io/v1/accounts/{address}/transactions/trc20"
    params = {
        "limit": limit,
        "contract_address": USDT_CONTRACT,
        "only_confirmed": "true",
        "order_by": "block_timestamp,desc",
    }
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=15)
        if r.status_code == 429:
            print(f"    ⚠  Rate limit — انتظر 10 ثوانٍ...")
            time.sleep(10)
            r = requests.get(url, headers=HEADERS, params=params, timeout=15)
        if r.status_code != 200:
            print(f"    ✗  HTTP {r.status_code} — {r.text[:150]}")
            return []
        return r.json().get("data", [])
    except Exception as e:
        print(f"    ✗  {e}")
        return []

def get_trx_balance(address):
    url = f"https://api.trongrid.io/v1/accounts/{address}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code != 200:
            return "N/A", "N/A"
        data = r.json().get("data", [])
        if not data:
            return "0.00", "0.00"
        acc = data[0]
        trx = float(acc.get("balance", 0)) / 1_000_000
        usdt = 0.0
        for t in acc.get("trc20", []):
            if USDT_CONTRACT in t:
                usdt = float(t[USDT_CONTRACT]) / 1_000_000
        return f"{trx:,.2f}", f"{usdt:,.2f}"
    except:
        return "N/A", "N/A"

def fmt_time(ts):
    try:
        return datetime.utcfromtimestamp(int(ts) / 1000).strftime("%Y-%m-%d %H:%M")
    except:
        return "?"

# ── MAIN ────────────────────────────────────────────────────

def analyze():
    print("\n" + "="*70)
    print("   KHAWRIZM FORENSICS  |  DRAGON403 — FOLLOW THE MONEY")
    print(f"   {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}  |  {len(TARGETS)} Wallets")
    print("="*70)

    all_out   = Counter()
    all_in    = Counter()
    summaries = {}
    big_flows = []

    for addr in TARGETS:
        print(f"\n[>] {addr}")

        trx_bal, usdt_bal = get_trx_balance(addr)
        print(f"    TRX: {trx_bal}  |  USDT: {usdt_bal}")

        txns = get_trc20_txns(addr)
        print(f"    USDT Transactions: {len(txns)}")

        sent_usdt = 0.0
        recv_usdt = 0.0
        sent_to   = Counter()
        recv_from = Counter()

        for tx in txns:
            frm = tx.get("from", "")
            to  = tx.get("to", "")
            val = float(tx.get("value", 0)) / 1_000_000
            ts  = fmt_time(tx.get("block_timestamp", 0))

            if frm.lower() == addr.lower():
                sent_usdt += val
                sent_to[to] += 1
                all_out[to] += 1
                if val >= 50:
                    big_flows.append({"dir":"OUT","from":frm,"to":to,"amount":val,"time":ts})
            elif to.lower() == addr.lower():
                recv_usdt += val
                recv_from[frm] += 1
                all_in[frm] += 1
                if val >= 50:
                    big_flows.append({"dir":"IN","from":frm,"to":to,"amount":val,"time":ts})

        print(f"    SENT:  {sent_usdt:>12,.2f} USDT  ->  {len(sent_to)} destination(s)")
        print(f"    RECV:  {recv_usdt:>12,.2f} USDT  <-  {len(recv_from)} source(s)")

        if sent_to:
            print(f"    TOP DESTINATIONS:")
            for dest, cnt in sent_to.most_common(5):
                flag = "  [IN OUR LIST]" if dest in TARGETS else "  [NEW - CHECK IT]"
                print(f"       {dest}  ({cnt}x){flag}")

        summaries[addr] = {
            "usdt_balance": usdt_bal,
            "trx_balance": trx_bal,
            "txns": len(txns),
            "sent_usdt": round(sent_usdt, 2),
            "recv_usdt": round(recv_usdt, 2),
        }
        time.sleep(DELAY)

    # ═══ FINAL REPORT ═══════════════════════════════════════
    print("\n\n" + "="*70)
    print("   FINAL REPORT — THE VAULTS")
    print("="*70)

    print("\n[1] TOP DESTINATIONS (potential vaults):")
    for dest, cnt in all_out.most_common(10):
        flag = "  [KNOWN]" if dest in TARGETS else "  [NEW — AUDIT ON TRONSCAN]"
        print(f"    {dest}  ->  {cnt:>3} transfers{flag}")

    print("\n[2] TOP SOURCES (who funds these wallets?):")
    for src, cnt in all_in.most_common(5):
        flag = "  [KNOWN]" if src in TARGETS else "  [NEW]"
        print(f"    {src}  ->  {cnt:>3} transfers{flag}")

    print(f"\n[3] BIG FLOWS (>=50 USDT) — Total: {len(big_flows)}")
    for f in sorted(big_flows, key=lambda x: x["amount"], reverse=True)[:20]:
        arrow = "OUT" if f["dir"]=="OUT" else "IN "
        print(f"    {f['time']}  {arrow}  {f['amount']:>10,.2f} USDT")
        print(f"          FROM: {f['from']}")
        print(f"          TO:   {f['to']}")

    print("\n[4] WALLET SUMMARY:")
    print(f"    {'ADDRESS':<44} {'USDT':>10}  {'SENT':>12}  {'RECV':>12}  {'TXN':>5}")
    print("    " + "-"*88)
    for addr, s in summaries.items():
        print(f"    {addr}  {s['usdt_balance']:>10}  {s['sent_usdt']:>12,.1f}  {s['recv_usdt']:>12,.1f}  {s['txns']:>5}")

    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "targets": TARGETS,
        "top_destinations": dict(all_out.most_common(20)),
        "top_sources": dict(all_in.most_common(20)),
        "big_flows": sorted(big_flows, key=lambda x: x["amount"], reverse=True),
        "wallet_summary": summaries,
    }
    with open("/root/dragon403_results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print("\n[OK] Results saved to: /root/dragon403_results.json")
    print("="*70 + "\n")

if __name__ == "__main__":
    analyze()
