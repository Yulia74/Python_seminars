"""
Дано натуральное число A > 1.
Определите, каким по счету числом (не индекс!) Фибоначчи оно является, то есть выведите
такое число n,что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
Input:  5
Output: 6
"""
print('Введите натуральное число A: ')
a = int(input())
f_prev, f_next = 0, 1
n = 2
while f_next <= a:
    if f_next == a:
        print(n)
        break
    else:
        f_prev, f_next = f_next, f_prev+f_next
        n += 1
else:
    print(-1)


""" другой вариант решения через временную переменную n0
n = int(input())
n0 = 0
n1 = 0
n2 = 1
i = 2
while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
if n0 > n:
    i = 0
if i != 0:
    print(i)
else:
    print(-1)
"""