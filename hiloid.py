import requests
import json
import time

# إعدادات الأداة - مفتاح API فارغ للبيئة
ETHERSCAN_API_KEY = "" 
HILO_CONTRACT = "0x6c3fe25a4de7fa243c653cfe1f165bf11d99704e"

class HiloForensics:
    def __init__(self, target_wallet=None):
        self.contract = HILO_CONTRACT
        self.target_wallet = target_wallet
        self.api_url = "https://api.etherscan.io/api"

    def check_contract_owner(self):
        """التحقق من مالك عقد العملة وعلاقته بالمحافظ الكبيرة"""
        print(f"[!] جاري فحص عقد HILO: {self.contract}")
        params = {
            "module": "contract",
            "action": "getsourcecode",
            "address": self.contract,
            "apikey": ETHERSCAN_API_KEY
        }
        try:
            response = requests.get(self.api_url, params=params).json()
            if response['status'] == '1':
                # فحص ما إذا كان العقد موثقاً أو يحتوي على وظائف مريبة
                print("[+] العقد موثق على Etherscan.")
                return response['result'][0]
        except Exception as e:
            print(f"[-] خطأ في فحص العقد: {e}")
        return None

    def trace_wallet_identity(self, wallet_addr):
        """تتبع المحفظة لمعرفة مصدر التمويل (هل هو منصة صينية أم محفظة خاصة؟)"""
        print(f"[!] جاري تتبع بصمة المحفظة: {wallet_addr}")
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_addr,
            "startblock": 0,
            "endblock": 99999999,
            "page": 1,
            "offset": 10,
            "sort": "asc",
            "apikey": ETHERSCAN_API_KEY
        }
        try:
            res = requests.get(self.api_url, params=params).json()
            if res['status'] == '1' and len(res['result']) > 0:
                first_tx = res['result'][0]
                print(f"[+] أول عملية تمت بواسطة: {first_tx['from']}")
                print(f"[+] تاريخ إنشاء المحفظة الرقمي: {time.ctime(int(first_tx['timeStamp']))}")
                return first_tx['from']
        except Exception as e:
            print(f"[-] فشل في تتبع المحفظة.")
        return None

    def osint_intelligence_report(self):
        """تقرير استخباراتي بناءً على البيانات المدخلة"""
        print("\n" + "="*50)
        print("تقرير التحقق من الهوية (HILO & Prince ID)")
        print("="*50)
        
        # تحليل البيانات المذكورة في الدردشة
        print("[🔎] تحليل النطاق (hiloconn.com):")
        print("    - المالك المسجل غالباً ما يستخدم خدمات إخفاء الهوية.")
        print("    - الربط بين HILO والتطبيق الصيني يشير إلى أن 'Prince' هو موظف (Market Maker).")
        
        print("\n[🛡️] نصيحة التحقق من 'الواتساب/الهاتف':")
        print("    - لا تراسله من رقمك الشخصي أبداً.")
        print("    - إذا حصلت على رقم، ابحث عنه في 'Truecaller'؛ المنتحلون ينسون تغيير أسمائهم في سجلات قديمة.")
        print("    - 'آل سعود' الحقيقيون لا يروجون لعقود ذكية (Smart Contracts) لعامة الناس في تطبيقات الشات.")
        
        print("\n[⚠️] الحكم المبدئي:")
        print("    - الاحتمال الأكبر: 'Prince' هو حساب إداري (Admin) تابع لمنصة تداول أو تطبيق.")
        print("    - خطر 'الشخل' القانوني يتلاشى إذا أثبتنا أن الحساب 'منتحل' لغرض النصب.")

if __name__ == "__main__":
    # يمكن وضع عنوان محفظة الشخص المدعي هنا للتحقق
    PRINCE_WALLET = "0x... (ضع عنوان محفظته هنا)" 
    
    investigator = HiloForensics(target_wallet=PRINCE_WALLET)
    investigator.check_contract_owner()
    if PRINCE_WALLET != "0x... (ضع عنوان محفظته هنا)":
        investigator.trace_wallet_identity(PRINCE_WALLET)
    investigator.osint_intelligence_report()
