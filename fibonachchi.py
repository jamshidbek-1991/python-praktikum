# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:41:37 2026

@author: User
"""

def fibonachchi(n):
    ketma_ketlik = []
    a, b = 1, 1
    for _ in range(n):
        ketma_ketlik.append(a)
        a, b = b, a + b
    return ketma_ketlik

n = int(input("Nechta had chiqarilsin: "))
natija = fibonachchi(n)
print("Fibonachchi ketma-ketligi:", natija)