import json
import csv

# Добавление нового сотрудника и пото запись его в scv файл
def add_to_json():
    json_dat = {
        "name": "Dima Koler",
        "birthday": '30.03.13',
        "height": 165,
        "weight": 50.1,
        "car": "true",
        "languages": ["C#", "C++", "C", "Python"]
    }
    data = json.load(open("employees.json"))
    data.append(json_data)
    with open('employees.json', 'r+') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
add_to_json()
with open('employees.json') as file:
    json_data = json.load(file)
with open('employees.csv', mode='w') as file:
    writer = csv.DictWriter(file, fieldnames=json_data[0].keys())
    writer.writeheader()
    writer.writerows(json_data)



