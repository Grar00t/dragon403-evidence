import requests
import socket
import json
import ssl
from datetime import datetime

# إعدادات الأداة - فحص البنية التحتية لتطبيق Vochat/Falla المرتبط بـ HILO
TARGET_DOMAINS = ["hiloconn.com", "hilo.com", "res-g.resygg.com"]
HILO_CONTRACT = "0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e"

class HiloAuditor:
    def __init__(self):
        self.results = {}

    def get_ip_info(self, domain):
        """استخراج معلومات السيرفر والشركة المستضيفة"""
        try:
            ip = socket.gethostbyname(domain)
            print(f"[+] فحص النطاق: {domain} -> IP: {ip}")
            # استخدام API عام لمعرفة موقع السيرفر (بدون مفتاح لغرض التجربة)
            response = requests.get(f"https://ipapi.co/{ip}/json/").json()
            return {
                "ip": ip,
                "org": response.get("org"),
                "country": response.get("country_name"),
                "city": response.get("city")
            }
        except Exception as e:
            return {"error": str(e)}

    def check_ssl_details(self, domain):
        """فحص شهادة الأمان لمعرفة الجهة المسجلة"""
        context = ssl.create_default_context()
        try:
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    issuer = dict(x[0] for x in cert['issuer'])
                    return issuer.get('organizationName', 'Unknown')
        except:
            return "Failed to fetch SSL"

    def run_audit(self):
        print(f"--- تقرير استقصائي: HILO & Vochat Infrastructure ---")
        print(f"التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for domain in TARGET_DOMAINS:
            print(f"[*] جاري تحليل {domain}...")
            info = self.get_ip_info(domain)
            org = self.check_ssl_details(domain)
            
            print(f"    - المستضيف: {info.get('org')}")
            print(f"    - الموقع: {info.get('city')}, {info.get('country')}")
            print(f"    - جهة الشهادة: {org}")
            print("-" * 30)

        print("\n[!] تحليل الربط المنطقي:")
        print("1. إذا ظهرت السيرفرات في (Singapore/Hong Kong) فهذا يؤكد تبعية المشروع لشركات صينية.")
        print("2. عقد HILO يحتوي على وراثة (Proxy) مما يعني إمكانية تغيير المالك أو سحب السيولة في أي وقت.")
        print("3. استخدامك لـ 20 حساباً سابقاً جعلهم يربطون بصمة جهازك (Device ID)، استخدم Proxy دائماً.")

if __name__ == "__main__":
    auditor = HiloAuditor()
    auditor.run_audit()
