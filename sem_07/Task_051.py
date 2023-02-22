'''
Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют
одинаковое значение некоторой характеристики, и возвращают True, если это так. Если значение
характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это функция, которая принимает объект
и вычисляет его характеристику.

Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

Вывод:
same
'''

def same_by(charac, objects): # charac это lambda x: x % 2, objects это values
    list_characteristic = [charac(i) for i in objects] # list comprehension - генератор списка
    for i in range(len(list_characteristic) - 1):
        if list_characteristic[i] != list_characteristic[i+1]:
            return False
        return True
    
values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# list_characteristic = [charac(i) for i in objects] # list comprehension - генератор списка
# обратная запись, мы перед for ставим то, что будем заполнять через функцию и подаем параметр,
# так как это фукнция в нашем случает это 0 % 2, 2 % 2, 10 % 2)