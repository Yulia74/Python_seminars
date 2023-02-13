'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот:
все максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4

Output: 1 3 3 3 1
'''

import random

# n = int(input('Введите количество оценок в журнале '))

# jour=[]
# for i in range(n):
#     jour.append(random.randint(1,5))

# сокращенная запись заменяет строки 13-17
jour = [random.randint(1, 5) for i in range(int(input('Введите количество оценок в журнале ')))]

print(*jour)

max_mark = max(jour)
min_mark = min(jour)

for i in range(len(jour)):
    if jour[i] == max_mark:
        jour[i] = min_mark
print(*jour)



# создание списка в методе

def make_list(n):
        jour_new=[]
        for i in range(n):
             jour_new.append(random.randint(1,5))
        return jour_new

n=int(input('Введите количество оценок в журнале '))
jour_new=make_list(n)
print(jour_new)


# 3 вариант решения (мой)

jour = [random.randint(1, 5) for i in range(int(input('Введите количество оценок в журнале ')))]

print(*jour)

for i in range(len(jour)):
    if jour[i]>3:
        jour[i] = 1
print(*jour)

