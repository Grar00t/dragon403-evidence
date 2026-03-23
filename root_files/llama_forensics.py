import requests
import os
import json

# إعدادات الاتصال بـ Llama عبر Hugging Face
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"}

def analyze_loot(filename):
    print(f"\n[*] Reading {filename}...")
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().strip()
            
        if not content:
            print("[-] File is empty. Nothing to analyze.")
            return

        # نرسل جزء من الملف عشان ما نضغط الـ API (أول 3000 حرف)
        chunk = content[:3000]
        
        payload = {
            "inputs": f"""
            You are a cybersecurity expert conducting a forensic investigation.
            Analyze the following extracted code/logs from a payment gateway.
            
            Task:
            1. Identify the Payment Provider (e.g., Stripe, HyperPay, Mada).
            2. Find variable names used for Credit Card numbers, CVV, or Tokens.
            3. Look for any hardcoded API Keys or Secrets.
            
            [CODE SNIPPET START]
            {chunk}
            [CODE SNIPPET END]
            
            Report:
            """,
            "parameters": {"max_new_tokens": 500, "temperature": 0.1}
        }

        print("🔥 Llama is analyzing the evidence... Please wait.")
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and 'generated_text' in result[0]:
                print("\n" + "="*40)
                print("💀 LLAMA VERDICT:")
                print("="*40)
                # تنظيف الرد لعرض التحليل فقط
                print(result[0]['generated_text'].split("Report:")[-1].strip())
            else:
                print(f"[-] Unexpected response: {result}")
        else:
            print(f"[-] API Error {response.status_code}: {response.text}")

    except FileNotFoundError:
        print(f"[-] File {filename} not found. Did you run the extraction script?")

# تشغيل التحليل على ملف الغنائم
if __name__ == "__main__":
    analyze_loot("payment_logic_loot.txt")
