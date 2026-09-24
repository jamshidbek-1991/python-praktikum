# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:53:38 2026

@author: User
"""
"""
Mavzu: Lug'at ichida ro'yxat - Sevimli kinolar
"""

kinolar = {
    'murodjon': ['avatar', 'orqagaqaytish yo\'q', 'bo\'g\'bon'],
    'to\'rabek': ['esmeralda', 'xan 1', 'xan 3'],
    'jamoldin': ['dengiz xukumdori', 'otamdan qolgan dalalar', 'yulduzli tunlar']
}

for ism, royxat in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in royxat:
        print(f"- {kino}")
