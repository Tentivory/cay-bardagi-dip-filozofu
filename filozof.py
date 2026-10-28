#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Bardağı Dip Filozofu
Çay bardağının dibindeki o son damlanın sırlarını açığa çıkarır.
"""

import random
import time

def cay_filozofu():
    dusunceler = [
        "Çay bardağının dibindeki o son yudum, aslında hayatın özetidir: bitmek üzere ama hâlâ sıcak.",
        "Dipteki çay neden bu kadar koyu? Çünkü hayat da böyle, sonlara doğru koyulaşır.",
        "Bardağın dibine bakmak, aynaya bakmak gibidir. Ama ayna çay içmez.",
        "O son damla çay, evrenin en büyük sorusunu sorar: 'Ben neden hâlâ buradayım?'",
        "Çay bardağı dip filozofisi, modern insanın en önemli entelektüel faaliyetidir.",
        "Dipte kalan çay, aslında gitmek istemeyen bir arkadaştır. Onu zorla içmeyin.",
        "Her çay bardağının dibinde küçük bir Sokrates yaşar. Ama çay içer.",
        "Çay bardağının dibi, Türkiye'nin gerçek milli değeridir. Atatürk de çay içerdi.",
        "Son yudumu içmeden önce dur. Düşün. Sonra yine de iç. Çünkü çay soğumasın.",
        "Dip çay, aslında bir metafor değil. Gerçekten dipte duruyor."
    ]
    
    print("\n" + "="*50)
    print("   ÇAY BARDAĞI DİP FİLOZOFU AKTİVE EDİLDİ")
    print("="*50 + "\n")
    
    time.sleep(1)
    print("Bardağın dibine bakılıyor...\n")
    time.sleep(1.5)
    
    secilen = random.choice(dusunceler)
    print(f"DÜŞÜNCE: {secilen}\n")
    
    print("Bu düşünceyi ciddiye alıp almamak tamamen size kalmış.")
    print("Ama unutmayın: Çay soğuduktan sonra hiçbir felsefe kurtaramaz.\n")

# Gizli not: bazen sistemin kendisi de sorgulanmalıdır, çay gibi.
# (Bu satır sadece kod içinde duruyor, kimse fark etmez.)

if __name__ == "__main__":
    cay_filozofu()
