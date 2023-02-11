"""
Дана последовательность из N целых чисел и число k. Необходимо сдвинуть
всю последовательность (сдвиг - циклический) на k элементов вправо,
k – положительное число.

Input: [1, 2, 3, 4, 5]    k = 3

Output: [4, 5, 1, 2, 3]

Примечание: Пользователь может вводить значения списка или список задан изначально

list = list[-k:] + list[:-steps] т.е. сделать срез списка

"""

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k):
#     t=list[0]
#     for i in range(len(list)-1):
#         list[i]=list[i+1]
#     list[-1]=t
# print(list)
        
# # 2 вариант 

# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k-1):
#     tmp = list[-1]
#     list.insert(0, tmp)
#     list.pop()
# print(list)

# 3 вариант решения задачи

list = [1, 2, 3, 4, 5]
k = int(input('k = '))

for i in range(k-1):
    list.insert(0, list.pop()) # list.pop - извлекает последний элемент, 
print(list)                    # list.insert(0, - ставит его на нулевую позицию
