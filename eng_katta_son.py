# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:02:25 2026

@author: User
"""
def eng_katta(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

natija = eng_katta(son1, son2, son3)
print("Eng katta son:", natija)