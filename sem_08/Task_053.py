'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
   (например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
'''
def inputText():
    with open('tel_dir.txt', 'a', encoding='utf-8') as data: # конструкция позволяет открывать-закрвать файл авто
        surname = data.write(input('Введите фамилию '))
        data.write(' ')
        name = data.write(input('Введите имя '))
        data.write(' ')
        fathername = data.write(input('Введите отчество '))
        data.write(' ')
        phoneNumber = data.write(input('Введите номер телефона '))
        data.write('\n')


def printText():
    data = open('tel_dir.txt', 'r')
    for line in data:
        print(line)                       # <class 'str'>
    data.close()

def checkText(userInfo):
    path = 'tel_dir.txt'
    data = open('tel_dir.txt', 'r')

    for line in data.readlines():
        if userInfo in line:
            print(line)
    data.close()


inputText()
printText()
checkText(input('Введите данные '))


