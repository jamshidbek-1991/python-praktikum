# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:31:59 2026

@author: User
"""

python_izohli_lugati = {
    'integer': "Butun son",
    'float': "O'nlik son",
    'string': "Matn",
    'list': "Ro'yxat",
    'tuple': "O'zgarmas ro'yxat",
    'dict': "Lug'at",
    'if': "Shart operatori",
    'else': "Aks holda",
    'for': "Takrorlash sikli",
    'print': "Ekranga chiqarish"}
kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))
kalit2 = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit2)

if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit2.title()} so'zi {tarjima} deb tarjima qilinadi")