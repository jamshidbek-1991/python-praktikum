# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:00:52 2026

@author: User
"""
"""
Mavzu: Muzey chiptasi - 1-usul (oddiy shart tekshirish)
"""

yosh = input("Yoshingizni kiriting (chiqish uchun 'exit' yoki 'quit'): ")

while yosh != 'exit' and yosh != 'quit':
    yosh = int(yosh)
    
    if yosh < 7:
        narx = 2000
    elif yosh < 18:
        narx = 3000
    elif yosh < 65:
        narx = 10000
    else:
        narx = 0
    
    if narx == 0:
        print("Chipta narxi: Bepul")
    else:
        print(f"Chipta narxi: {narx} so'm")
    
    yosh = input("\nYana yosh kiriting (chiqish uchun 'exit' yoki 'quit'): ")

print("Dastur to'xtadi. Rahmat!")