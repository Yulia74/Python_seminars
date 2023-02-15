'''
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке,
в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
(каждое число вводится с новой строки)

Ввод: 
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1 

Вывод:
3 3 2 12



import random

n = int(input('Введите количество элементов первого массива: '))

first = []
for i in range(n):
    first.append(random.randint(1, 10))


m = int(input('Введите количество элементов второго массива: '))
second = []
for i in range(m):
    second.append(random.randint(1, 10))


print(first)
print(second)
                                # создаем счетчик, который посчитывает
count = 0                       # количество повторений числа во 2 массиве                    
for i in range(n):              # цикл проходится по первому списку
    for j in range(m):          # и по второму, чтобы сравнить числа
        if first[i] == second[j]: # сравниваем число из 1 на равенстро с числами 2 списка
            count += 1          # если есть равенство, то счетчик увеличиваем
    if count == 0:              # если счетчик остался равен 0, то выводим на 
        print(first[i], end=' ') # печать элемент 1 массива (в строку)
    count = 0                   # если повторы были, то обнулем счетчик и 
print('\n') # c новой строки    # переходим к следующему элементу массива
'''
# 2 вариант решения


# list_1 = [int(input('add element: ')) for i in range(int(input('enter n = ')))]
# list_2 = [int(input('add element: ')) for i in range(int(input('enter m = ')))]

# print([i for i in list_1 if i not in list_2])

# 3 вариант решения

from random import randint
num_list_1 = [randint(1, 10) for _ in range(int(input('Введите размер первого массива: ')))]
num_list_2 = [randint(1, 10) for _ in range(int(input('Введите размер второго массива: ')))]    
print(*num_list_1)
print(*num_list_2)

list1_unique_nums=set(num_list_1)-set(num_list_2)
for i in num_list_1:
    if i in list1_unique_nums:
        print(i, end=' ')

print('\n')