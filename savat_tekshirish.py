# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:38:06 2026

@author: User
"""
"""
Mavzu: Ro'yxat va lug'atni birlashtirish - Savatni tekshirish
"""

savat = ['non', 'sut', 'tuhum', 'banan']   # foydalanuvchi buyurtma qilgan mahsulotlar

ebozor = {
    'non': '5000',
    'tuhum': '2000',
    'sut': '10000',
    'olma': '15000',
    "mol go'shti": '150000'
}

for mahsulot in savat:
    if mahsulot in ebozor:
        narx = ebozor[mahsulot]
        print(f"{mahsulot.title()}: {narx} so'm")
    else:
        print(f"Bizda '{mahsulot}' mahsuloti yo'q")