#!/bin/bash
# Package ID اللي لقطناه من قوقل بلاي
PKG="com.qiahao.nextvideo"

echo -e "\033[1;32m[+] Targeting App: Hilo ($PKG)\033[0m"

# تنزيل التطبيق (يحتاج يكون عندك adb وجوال موصل أو محاكي، أو بنسحبه من مستودع)
# ملاحظة: إذا معك الملف APK بجهازك سحبه لـ /home/kali/
if [ ! -f "hilo.apk" ]; then
    echo -e "\033[1;33m[*] Searching for APK source...\033[0m"
    # محاولة سحب الروابط المباشرة للتحميل
    curl -s "https://apkpure.com/hilo-group-chat-video-connect/$PKG" | grep -oE 'https://[^"]+.apk' | head -n 1 > apk_link.txt
fi

# تفكيك الكود المصدري
echo -e "\033[1;31m[!] Decompiling Hilo... Time to see their guts!\033[0m"
apktool d -f *.apk -o hilo_source 2>/dev/null

# البحث عن السوالف والمدفوعات (Keywords Search)
echo -e "\033[1;34m[*] Extracting Payment & Chat Endpoints...\033[0m"
grep -riE "pay|wallet|recharge|token|admin|chat|http" hilo_source/res/values/strings.xml > payment_strings.txt
grep -riE "api\.|v1/|v2/|\.php|\.json" hilo_source/smali/ > hidden_api_logic.txt

echo -e "\033[1;32m[+] Dissection Complete! Check payment_strings.txt for the loot.\033[0m"
