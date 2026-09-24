# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:53:43 2026

@author: User
"""

import matematika

print(matematika.yigindi(5, 3))
print(matematika.ayirma(10, 4))
print(matematika.kopaytma(6, 7))
print(matematika.PI)

# Modulga qisqa nom berish
import matematika as mat
print(mat.yigindi(100, 50))

# Faqat kerakli funksiyani olish
from matematika import ayirma
print(ayirma(20, 5))

# Funksiyaga qisqa nom berish
from matematika import kopaytma as ko_p
print(ko_p(3, 4))

import random

# 1 dan 100 gacha tasodifiy son
son = random.randint(1, 100)
print("Tasodifiy son:", son)

# Ro'yxatdan tasodifiy bitta element tanlash
mevalar = ["olma", "anor", "uzum", "shaftoli", "nok"]
tanlangan = random.choice(mevalar)
print("Tanlangan meva:", tanlangan)

# Ro'yxatni aralashtirish
random.shuffle(mevalar)
print("Aralashtirilgan ro'yxat:", mevalar)