'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

Input: 5

Output: yes
'''


def check_num(n):
    flag = True
    for i in range(2, n):
        if n % i != 0:
            continue
    else:
        flag = False
    return flag

n = int(input('Введите число: '))
print(check_num(n))

