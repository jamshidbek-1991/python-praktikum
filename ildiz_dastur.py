# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:36:29 2026

@author: User
"""
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    if qiymat == 'exit':
        break
    
    qiymat = float(qiymat)
    
    if qiymat < 0:
        print("Manfiy son kiritdingiz, musbat son kiriting!\n")
        continue
    
    ildiz = qiymat ** 0.5
    print(f"{qiymat} ning ildizi {ildiz} ga teng\n")

print("Dastur to'xtadi. Rahmat!")