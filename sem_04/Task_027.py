'''
    Пользователь вводит текст(строка). Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки.
    Определите, сколько различных слов содержится в этом тексте.

Input:
She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. 
So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells.

Output: 17

1 вариант решения через множество

line = (input('Введите символы строки через пробел: ').lower().split())  # вводим строку,
# lower переводит символы в нижний регистр, split разделят список по пробелам (по умолчанию)
words = set()         # создаем пустое множенство
for i in line:
    words.add(i)    # заполняем множество уникальными словами
print(len(words))   # выводим количество элементов в множестве


2 вариант решения, записанное в одну строку

print(len(set(input('Введите текст ').upper().replace('.', ' ').split())))


3 вариант - решение через словарь
'''

list = input('Введите текст: ').split()
dict = {}
for i in list:
    dict[i.lower()]=0
print(len(dict.keys()))