# Семинарское занятие №1

**Задача 1**

За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
  
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.


Input:
n = 700
m = 750

Output:
2
____________
**Задача 3**

В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.

Input: 20 21 22 (ввод чисел НЕ в одну строку)

Output: 32
___________

**Задача №5**

Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
(при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»;
это зависит от того, в какую сторону едет электричка). В каждом вагоне написан
его номер.

Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
Он хочет определить, сколько всего вагонов в электричке.

Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

Input: 3 4 (ввод на разных строках)

Output: 6
___________________

**Задача 7**


Дано натуральное число. Требуется определить, является ли год с данным номером високосным.

Если год является високосным, то выведите YES, иначе выведите NO.
 
Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

Input: 2016

Output: YES

______________

# Семинарское занятие №2

**Задача 9**

По данному целому неотрицательному n вычислите
значение n!. 

N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1

Решить задачу используя цикл
while

Input: 5

Output: 120 
_________

**Задача 11**

Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи (не индекс!)
оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input:  5

Output: 6 
__________________

**Задача 13**

Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала
0 градусов Цельсия. 

Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

Input: 6 -> -20 30 -40 50 10 -10

Output: 2
____________

# Семинарское занятие №3

**Задача №17**

 Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6

*Примечание: пользователь может вводить значения
списка или список задан изначально*
_____

**Задача №19**

Дана последовательность из N целых чисел и число
k. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на k элементов вправо, k –
положительное число.

Input: [1, 2, 3, 4, 5]    k = 3

Output: [4, 5, 1, 2, 3]

*Примечание: Пользователь может вводить значения
списка или список задан изначально*
_________

**Задача №21** 

Напишите программу для печати всех различных значений в словаре.

Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

*Примечание: Список словарей задан изначально. Пользователь его не вводит*
_____________________

**Задача №23** 

Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)

Input: [0, -1, 5, 2, 3]

Output: 2 (-1 < 5, 2 < 3)

*Примечание: Пользователь может вводить значения списка или список задан изначально*
______________


# Семинарское занятие №4

**Задача №25**

Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз 
каждый символ уже встречался. Количество повторов добавляется к символам с помощью 
постфикса формата _n.

Input: a a a b c a a d c d d

Output: a_0 a_1 a_2 b_0 c_0 a_3 a_4 d_0 c_1 d_1 d_2

*Для решения данной задачи используйте функцию split( )*
__________________

**Задача №27**

Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько **различных** слов
содержится в этом тексте.

Input: 
She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure. So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells

Output: 17
______________________
**Задача №29**

Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность).
_________________________

# Семинарское занятие №5
