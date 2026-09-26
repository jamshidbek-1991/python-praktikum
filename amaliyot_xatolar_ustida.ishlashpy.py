# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:00:58 2026

@author: User
"""

# 1-topshiriq
son = float(input("Sonni kiriting: "))

if son % 2 == 0:
    print("Bu son juft.")
else:
    print("Bu son toq.")

yosh = float(input("Yoshingiz nechida? "))

if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000

print(f"Chipta {narh} so'm")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))

if x == y:
    print(f"{x}={y}")
elif x < y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

mahsulotlar = ['un', "yog'", "sovun", "tuxum", "piyoz",
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
else:
    print("Savatingiz bo'sh")

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

users = ['alisher1983', 'aziza', 'yasina', 'umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print("Xush kelibsiz!")





    