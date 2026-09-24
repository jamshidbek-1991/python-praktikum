# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:08:53 2026

@author: User
"""

"""
Mavzu: Muzey chiptasi - 2-usul (break operatori bilan)
"""

while True:
    yosh = input("Yoshingizni kiriting (chiqish uchun 'exit' yoki 'quit'): ")
    
    if yosh == 'exit' or yosh == 'quit':
        break
    
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

print("Dastur to'xtadi. Rahmat!")