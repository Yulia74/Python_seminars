'''
    Пользователь вводит текст(строка). Словом считается последовательность непробельных
символов идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки.
    Определите, сколько различных слов содержится в этом тексте.

Input:
She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure.
 So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells.

Output: 19

'''
line = (input('Введите символы строки через пробел: ').lower().split()
        )  # вводим строку,
# lower переводит символы в нижний регистр, split разделят список по пробелам (по умолчанию)
words = set()         # создаем пустое множенство
for i in line:
    words.add(i)    # заполняем множество уникальными словами
print(len(words))   # выводим количество элементов в множестве
