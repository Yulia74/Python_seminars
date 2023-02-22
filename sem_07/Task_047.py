'''
У вас есть код, который вы не можете менять(так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):

transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
или любой другой список transormed_values = list(map(transformation, values))

Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation. Однако вы поняли, что для вашей текущей задачи вам не нужно
никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

Ввод:
values = [1, 23, 42, ‘asdfg’]
transformed_values = list(map(trasformation, values))
if values == transformed_values:
    print(‘ok’)
else:
    print(‘fail’)
Вывод:
ok
'''
transformation = lambda x: x # вводим в код строку, lambda (анонимную) функцию которая ничего не делает х=х
values = [1, 23, 42, 'asdfg']                          # чтобы не писать return
transformed_values = list(map(transformation, values)) #list функция, которая оборачивает в список работу map
                                                       # если не поставить list, то выдаст объект map <map object at 0x000000B67783B070>                                                    
                                                       # map применяет функцию transformation, на 
                                                       # каждый элемент списка values
if values == transformed_values:
    print('ok')
else:
    print('fail')

print(values)
print(transformed_values)
