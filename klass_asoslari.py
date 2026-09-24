# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 06:54:16 2026

@author: User
"""

class Talaba:
    maktab_nomi = "MOHIRDEV"
    def __init__(self, ism, familiya, yosh, guruh):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.guruh = guruh

    def malumot(self):
        print(f"Ism: {self.ism}, Familiya: {self.familiya}, Maktab: {self.maktab_nomi}")
        
talaba1 = Talaba("Sardor", "Aliyev", 20, "AI-21")
talaba2 = Talaba("Nodira", "Karimova", 19, "AI-22")

talaba1.malumot()
talaba2.malumot()

talaba3 = Talaba("rustam", "razzaqov", 35, "AI-21")
talaba4 = Talaba("komiljon", "alixonov", 28, "AI-23")

talaba3.malumot()
talaba4.malumot()
print(Talaba.maktab_nomi)