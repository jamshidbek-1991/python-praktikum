# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:31:00 2026

@author: User
"""

def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(multiply(4, 5, 6))

def talaba_info(ism, familiya, **kwargs):
    malumot = {
        "ism": ism,
        "familiya": familiya
    }
    malumot.update(kwargs)
    return malumot

talaba1 = talaba_info("Sardor", "Aliyev", yosh=20, guruh="AI-21", email="sardor@gmail.com")
print(talaba1)

talaba2 = talaba_info("Nodira", "Karimova")
print(talaba2)