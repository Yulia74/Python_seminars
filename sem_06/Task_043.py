'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.

Ввод: 
1 2 3 2 3

Вывод:
2
'''

from random import randint


arr = [randint(1, 10) for i in range(
    int(input('Введите количество элементов массива: ')))]

print(arr)

count = 0
for i in range(len(arr)-1):          # -1 чтобы последний элемент не сравнивался с последним
    for j in range(i+1, len(arr)):   # +1 чтобы первый элемент не сравнивался с последним
        if arr[i] == arr[j]:
            count+=1
print(count)
