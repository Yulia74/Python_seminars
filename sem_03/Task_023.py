"""
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)

Input: [0, -1, 5, 2, 3]

Output: 2 (-1 < 5, 2 < 3)



1 вариант

list = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list)):
    if list[i] > list[i-1]:
        count += 1
print(count)


2 вариант
"""

list = [0, -1, 5, 2, 3]
count = 0
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        count += 1
print(count)
