# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:53:27 2026

@author: User
"""

# 1. ismlar ro'yxati - kamida 3 ta yaqin do'st ismi
ismlar = ['Ali', 'Vali', 'Hasan']

# 2. Har bir do'stga qisqa xabar
print("Salom " + ismlar[0] + ", bugun choyxona bormi?")
print(f"{ismlar[1]}, choyxonaga boramizmi?")
print(f"{ismlar[2]}, kel choyxonaga boramiz")

# 3. sonlar ro'yxati - musbat, manfiy, butun, o'nlik sonlar
sonlar = [22, -58.2, 34.0, 67, 1983, 112.4]
print(sonlar)

# 4. Sonlar ustida arifmetik amallar
sonlar[0] = sonlar[0] + sonlar[-1]   # birinchi bilan oxirgisini qo'shamiz
sonlar[1] = -67.8                     # ikkinchisini almashtiramiz
sonlar[4] = sonlar[4] + 37            # beshinchisiga 37 qo'shamiz
print(sonlar)

# 5. t_shaxslar va z_shaxslar ro'yxatlari
t_shaxslar = ['Amir Temur', 'Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Donald Trump']

# 6. Har biridan .pop() bilan bittadan olib chiqarish
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n"
      f"zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n"
      f"suhbat qilishni istar edim\n")

# 7. friends bo'sh ro'yxat, .append() bilan 5-6 ta do'st qo'shamiz
friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)

# 8. Kela olmaydiganlarni .remove() bilan chiqarib tashlaymiz
friends.remove('John')
friends.remove('Alex')
print(friends)

# 9. Ro'yxatga oxiriga, boshiga, o'rtasiga yangi ism qo'shamiz
friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)

# 10. mehmonlar bo'sh ro'yxat, .pop() va .append() bilan
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)