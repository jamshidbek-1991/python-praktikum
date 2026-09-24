# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 06:24:07 2026

@author: User
"""

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120, 1200, 2))
print(sonlar)

# 9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

# 10. Ro'yxatdagi eng katta   va eng kichik son o'rtasidagi ayirmani hisoblang
print(max(sonlar) - min(sonlar))

# 11. Ro'yxatdegi elementlar sonini hisoblang
print(len(sonlar))

# 12. Ro'yxatdagi boshidan, o'rtasidan va oxiridan 20 ta qiymatni chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[250:270])