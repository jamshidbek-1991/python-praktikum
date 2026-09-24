# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:27:40 2026

@author: User
"""
"""
Mavzu: while + ro'yxatni to'ldirish - Buyurtma dasturi
"""

savat = []

while True:
    mahsulot = input("Savatga mahsulot qo'shing ('stop' desangiz tugaydi): ")
    if mahsulot == 'stop':
        break
    savat.append(mahsulot)

print(f"\nSizning savatingiz: {savat}")