# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:13:29 2026

@author: User
"""

import math

def aylana_malumotlari(radius):
    diametr = 2 * radius
    perimetr = 2 * math.pi * radius
    yuza = math.pi * radius ** 2
    return {
        "radius": radius,
        "diametr": diametr,
        "perimetr": round(perimetr, 2),
        "yuza": round(yuza, 2)
    }
radius = float(input("Aylananing radiusini kiriting: "))
natija = aylana_malumotlari(radius)
print(natija)