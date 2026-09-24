# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 06:43:05 2026

@author: User
"""

# 1. taomlar degan ro'yxar yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh', 'somsa', 'norin', 'shashlik', 'qozonkabob']
print(taomlar)

# 2. nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
print(nonushta)

# 3. Yangi ro'yxatda faqat nonushtaga yeyiladigon taomlarni qoldirring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')

# 4. Ikkila ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# 5. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga (tuple) aylantiring
nonushta = tuple(nonushta)
print(nonushta)
print(type(nonushta))

# 6. Endi uni o'zgartirishga harakat qilamiz
nonushta[0] = "qaymoq va non"