import json
with open('employees.json') as file:
    json_data = json.load(file)
year = 0
lang = ''

def birth(year, json_data):
    year = int(input('Введите год рождения'))
    sr = []
    for dict in json_data:
        date = dict.get('birthday')
        dmy = date.split('.')
        years = dmy[-1].split()
        for i in years:
            if year >= int(i):
                sr.append(dict.get('height'))
    print('Рост сотрудников чей год рождения меньше заданного', sr)
    sredn = sum(sr) / len(sr)
    print('Средний рост этих сотрудников', sredn)

def langua(lang, json_data):
    lang = input("Maky your choise: 'C#', 'C++', 'C', 'Python', 'Pascal', 'Delphi'")
    for dict in json_data:
        if lang in dict.get('languages'):
            print('Этим языков влядеют:', dict)


def name():
    while True:
        name = input('Введите имя')
        if name == 'John Smith':
            print(json_data[0])
            break
        elif name == 'Alexey Alexeev':
            print(json_data[1])
            break
        elif name == 'Maria Ivanova':
            print(json_data[2])
            break
        elif name == 'Dima Koler':
            print(json_data[3])
            break


while True:
    action = (
        int(input('Выберите номер действия: 1) Узнать средний рост сотрудников, чей год рождения меньше заданного\n'
                  '2) Узнать кто владеет выбранным языком программирования\n'
                  '3) Узнать информацию о сотруднике по введенному имени\n'
                  '4) Выйти из программы')))
    if action == 1:
        birth(year, json_data)
    elif action == 2:
        langua(lang, json_data)
    elif action == 3:
        name()
    elif action == 4:
        break
