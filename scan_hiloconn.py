import requests
import urllib3
import sys
import json

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

TARGETS = {
    "goploy": "https://goploy.hiloconn.com",
    "teenpatti": "https://teenpatti.hiloconn.com",
    "ws": "https://ws.hiloconn.com",  # Usually upgrades to WSS
    "api": "https://api.hiloconn.com"
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Content-Type': 'application/json'
}

def check_goploy():
    print(f"\n[+] Probing Goploy Deployment Tool ({TARGETS['goploy']})...")
    # Goploy common endpoints
    endpoints = [
        "/user/login", 
        "/deploy/getList", 
        "/project/getProjectList",
        "/api/common/init"
    ]
    
    for ep in endpoints:
        url = f"{TARGETS['goploy']}{ep}"
        try:
            r = requests.get(url, verify=False, timeout=5, headers=HEADERS)
            print(f"  - {ep}: {r.status_code} (Size: {len(r.content)})")
            if "json" in r.headers.get("Content-Type", ""):
                try:
                    data = r.json()
                    print(f"    ⚠️  JSON Response: {str(data)[:100]}...")
                except:
                    pass
        except Exception as e:
            print(f"  ❌ Error connecting to {ep}: {str(e)}")

def check_teenpatti():
    print(f"\n[+] Probing TeenPatti Gambling Server ({TARGETS['teenpatti']})...")
    # Check for game config or assets
    paths = [
        "/config.json",
        "/version.json",
        "/admin",
        "/api/login",
        "/assets/"
    ]
    
    for path in paths:
        url = f"{TARGETS['teenpatti']}{path}"
        try:
            r = requests.get(url, verify=False, timeout=5, headers=HEADERS)
            if r.status_code != 404:
                print(f"  🚨 FOUND: {url} [{r.status_code}]")
        except:
            pass

def check_api_root():
    print(f"\n[+] Checking API Root ({TARGETS['api']})...")
    try:
        r = requests.get(TARGETS['api'], verify=False, timeout=5, headers=HEADERS)
        print(f"  - Root Response: {r.status_code}")
        print(f"  - Headers: {r.headers.get('Server', 'Unknown')}")
        if r.status_code == 200:
            print(f"  - Content: {r.text[:200]}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

def main():
    print("⚔️  STARTING DEEP SCAN: HILOCONN INFRASTRUCTURE ⚔️")
    print("=" * 60)
    
    check_goploy()
    check_teenpatti()
    check_api_root()
    print("\n[!] Scan Complete. Check results for open doors.")

if __name__ == "__main__":
    main()
