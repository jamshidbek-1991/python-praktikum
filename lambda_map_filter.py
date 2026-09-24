# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:09:26 2026

@author: User
"""

sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ikki_barobar = list(map(lambda x: x * 2, sonlar))
print("2 barobar oshirilgan:", ikki_barobar)

sonlar2 = [3, 8, 12, 5, 20, 1, 15, 7, 25]

kattalar = list(filter(lambda x: x > 10, sonlar2))
print("10 dan katta sonlar:", kattalar)

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]

mevalar_b = list(filter(lambda meva: meva.startswith('b'), mevalar))
print("B harfi bilan boshlanadigan mevalar:", mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
print("5 yoki undan kam harfli mevalar:", mevalar2)

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]

natija = list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')), mevalar))
print("Natija:", natija)