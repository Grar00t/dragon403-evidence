import requests
import urllib3
import sys

# Disable SSL warnings for cleaner output
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TARGET = "https://adm.yinguo.falla.live"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}

def scan_target():
    print(f"\n⚔️  STARTING RECON: {TARGET}")
    print("=" * 50)

    try:
        # 1. Basic Fingerprinting (Server Headers)
        print("[*] Checking Server Headers...")
        response = requests.get(TARGET, verify=False, timeout=10, headers=HEADERS)
        print(f"  ✅ Status Code: {response.status_code}")
        
        interesting_headers = ['Server', 'X-Powered-By', 'Via', 'X-AspNet-Version', 'Set-Cookie']
        found_tech = False
        for k, v in response.headers.items():
            if k in interesting_headers:
                print(f"  🔍 {k}: {v}")
                found_tech = True
        if not found_tech:
            print("  ⚠️  No tech headers found (Hidden).")

        # 2. Check for Sensitive Files (Common Misconfigurations)
        print("\n[*] Checking for Exposed Files...")
        paths = [
            ".env", ".git/HEAD", "config.js", "web.config", 
            "admin/", "login/", "dashboard/", 
            "api/docs", "swagger.json", "v2/api-docs",
            "keygen", "keys", "secrets", "secret", "oauth", # New Loot
            "passwords", "showkey", "_vti_bin/_vti_aut/author.dll", # New Loot
            "actuator/health", # Spring Boot vulnerability
            "dbadmin", "phpmyadmin", "useradmin", "pay", "paypal", "admincp" # Financial & Admin Loot
        ]
        
        for path in paths:
            url = f"{TARGET}/{path}"
            try:
                r = requests.get(url, verify=False, timeout=5, headers=HEADERS)
                if r.status_code == 200:
                    print(f"  🚨 EXPOSED: {url} (200 OK) - Check this immediately!")
                    # Deep inspection for financial traces
                    content = r.text.lower()
                    fin_keywords = ['alipay', 'wechat', 'usdt', 'recharge', 'coin', 'gold', 'payment', 'bank']
                    found = [k for k in fin_keywords if k in content]
                    if found:
                        print(f"    💰 FINANCIAL TRACE DETECTED: {found}")
                elif r.status_code == 403:
                    print(f"  🔒 Forbidden: {url} (403) - Exists but protected.")
            except:
                pass

        # 3. Check robots.txt for hidden paths
        print("\n[*] Checking robots.txt...")
        r_robots = requests.get(f"{TARGET}/robots.txt", verify=False, timeout=5, headers=HEADERS)
        if r_robots.status_code == 200:
            print("  📄 Found robots.txt! Checking for disallowed paths...")
            for line in r_robots.text.split('\n'):
                if 'Disallow:' in line:
                    print(f"    👉 {line.strip()}")
        else:
            print("  ❌ No robots.txt found.")

    except Exception as e:
        print(f"❌ Error: {e}")

    print("\n" + "=" * 50)
    print("⚠️  Recommendation: Use 'nuclei' tool for deep CVE scanning.")

if __name__ == "__main__":
    scan_target()
