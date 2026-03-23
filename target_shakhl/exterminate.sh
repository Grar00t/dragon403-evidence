#!/bin/bash
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}[+] Starting Sovereignty Scan on Fraud Network...${NC}"

for target in $(cat targets.txt); do
    echo -e "${RED}[!] Shakhling Target: $target ${NC}"
    
    # فحص المنافذ والخدمات المخفية
    nmap -sV -Pn --script=http-title,http-methods,http-enum -p 80,443,8080,8443 $target -oN scan_$target.txt
    
    # البحث عن مسارات الأدمن والـ API المسربة
    ffuf -w /usr/share/wordlists/dirb/common.txt -u https://$target/FUZZ -mc 200,301,403 -t 50 -o fuzz_$target.json
    
    # استخراج الـ Headers لكشف تقنيات التمويه (Cloaking)
    curl -I -s https://$target > headers_$target.txt
done

echo -e "${GREEN}[+] Scan Complete. Check ~/target_shakhl for the loot.${NC}"
