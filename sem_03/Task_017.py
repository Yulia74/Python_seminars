"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6

Примечание: пользователь может вводить значения списка или список задан изначально


list = [1, 1, 2, 0, -1, 3, 4, 4] # задан список
new_set = set(list)
print(list)
print(f'В заданном списке {len(new_set)} различных чисел')

"""
# краткий вариант решения
list = [1, 1, 2, 0, -1, 3, 4, 4]
print(list)
print(f'В заданном списке {len(set(list))} различных чисел')


# 2 вариант решения (пользователь вводит значения самостоятельно)

list_1 = []            # создали пустой список
n = int(input('Введите количество элементов в списке '))          
for i in range(n):     # цикл выполнится n раз
    i = int(input('Введите элемент списка ')) # пользователь вводит элементы списка
    list_1.append(i)
print(list_1)
another_set=set(list_1)
print(f'В заданном списке {len(another_set)} различных чисел')

