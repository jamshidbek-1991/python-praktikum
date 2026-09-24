# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 06:07:53 2026

@author: User
"""

# 1. cars ro'yxati - birinchi harifni katta qilish, GM uchun ikkala harifni katta
cars = ['toyota', 'mazda', 'huyundai', 'gm', 'kia']

for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
print()

# 2. Xuddi shu narsa, lekin != orqali
for car in cars:
    if car != 'gm':
       print(car.title())
    else:
       print(car.upper())
       
       # 3. Login ismini tekshirish
login = input("Login ismingizni kiriting: ")

if login == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")

# 4. Ikki son tengligini tekshirish
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    print("Sonlar teng")

# 5. Son manfiy yoki musbatligini aniqlash
son = float(input("Istalgan sonni kiriting: "))

if son < 0:
    print("Manfiy son")
else:
    print("Musbat son")

# 6. Musbat bo'lsa ildizini hisoblash
son = float(input("Sonni kiriting: "))

if son >= 0:
    print("Ildizi:", son ** 0.5)
else:
    print("Musbat son kiriting")