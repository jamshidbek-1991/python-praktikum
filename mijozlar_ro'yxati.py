# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:09:24 2026

@author: User
"""

from foydalanuchi_royxati import foydalanuvchi_royxati

mijozlar = []

n = int(input("Nechta mijoz kiritasiz? "))
i = 0
while i < n:
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    yil = int(input("Tug'ilgan yil: "))
    joy = input("Tug'ilgan joy: ")
    yosh = 2026 - yil
    email = input("Email (ixtiyoriy): ")
    tel = input("Tel raqam (ixtiyoriy): ")
    
    mijoz = foydalanuvchi_royxati(ism, familiya, yil, joy, yosh, email, tel)
    mijozlar.append(mijoz)
    i += 1

for mijoz in mijozlar:
    print(mijoz)