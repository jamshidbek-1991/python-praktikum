# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 08:01:21 2026

@author: User
"""

def foydalanuvchi_royxati(ism, familiya, tugilgan_yil, tugilgan_joy, yosh, email="", tel_raqam=""):
    return {
        "ism": ism,
        "familiya": familiya,
        "tugilgan_yil": tugilgan_yil,
        "tugilgan_joy": tugilgan_joy,
        "yosh": yosh,
        "email": email,
        "tel_raqam": tel_raqam
    }

user1 = foydalanuvchi_royxati("Ali", "Valiyev", 2000, "Toshkent", 25, tel_raqam="+998901234567")
print(user1)