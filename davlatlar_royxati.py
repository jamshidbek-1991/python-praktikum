# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 06:10:10 2026

@author: User
"""

# 1. O'zbekiston ma'lum davlatlarning ro'yxatini tuzing va konsolga chiqaring
davlatlar = ["O'zbekiston", "Qozog'iston", "Rassiya", "Malaziya", "Singapur", "AQSH"]
print(davlatlar)

# 2. Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# 3. sorted() funksiyasi yordamida ro'yxatni tartiblangan holda chiqaring
print(sorted(davlatlar))

# 4. sorted() yordamida ro'yxatni teskari tartibda chiqaring
print(sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan chiqaring (o'zgarmagan bo'lishi kerak)
print(davlatlar)

# 6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

# 7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin teskari tartibda chiqaring
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)