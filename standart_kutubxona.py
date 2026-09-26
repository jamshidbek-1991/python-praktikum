# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 07:29:06 2026

@author: User
"""

from datetime import date, timedelta

bugun = date.today()

print("2 hafta oralig'idagi 10 ta sana:")
for i in range(10):
    sana = bugun + timedelta(weeks=2 * i)
    print(sana.strftime("%d.%m.%Y"))
    
    # 2-vazifa: Ramazon va Qurbon hayitgacha qolgan kunlar
ramazon_hayit = date(2027, 3, 9)
qurbon_hayit = date(2027, 5, 17)

ramazon_qolgan = (ramazon_hayit - bugun).days
qurbon_qolgan = (qurbon_hayit - bugun).days

print(f"\nRamazon hayitigacha {ramazon_qolgan} kun qoldi")
print(f"Qurbon hayitigacha {qurbon_qolgan} kun qoldi")

# 3-vazifa: Yosh hisoblovchi funksiya
def yosh_hisobla(tugilgan_sana):
    bugun = date.today()
    
    yil = bugun.year - tugilgan_sana.year
    oy = bugun.month - tugilgan_sana.month
    kun = bugun.day - tugilgan_sana.day
    
    if kun < 0:
        oy -= 1
        oldingi_oy = date(bugun.year, bugun.month, 1) - timedelta(days=1)
        kun += oldingi_oy.day
    
    if oy < 0:
        yil -= 1
        oy += 12
    
    return yil, oy, kun

tugilgan = date(1991, 12, 30)   # o'zingizning tug'ilgan sanangizni yozing
y, o, k = yosh_hisobla(tugilgan)
print(f"\nSizga {y} yil, {o} oy, {k} kun bo'ldi")

# 4-vazifa: Telefon raqamini tekshirish
import re

raqam = input("\nTelefon raqamingizni kiriting (masalan +998901234567): ")

andoza = r'^\+998\d{9}$'

if re.match(andoza, raqam):
    print("Raqam to'g'ri formatda kiritildi ✅")
else:
    print("Raqam noto'g'ri formatda! Namuna: +998901234567 ❌")
    
    # 5-vazifa: Matndan URL (havola) larni ajratib olish
def linklarni_topish(matn):
    andoza = r'https?://\S+'
    return re.findall(andoza, matn)

matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

linklar = linklarni_topish(matn)
print("\nTopilgan linklar:")
for link in linklar:
    print(link)