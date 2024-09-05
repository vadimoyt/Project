import functools
with open('cezar.txt', 'r+') as nabor:
    stroka = nabor.read()
    str = stroka.split('\n')
alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
sp = []
res1 = ''
for i in str[0].upper():
    shag = 1
    if i in alphabet_eng:
        place_i = alphabet_eng.index(i)
        new_place_i = place_i + shag
        res1 += alphabet_eng[new_place_i]
    else:
        res1 += i
print(res1.capitalize() + ',' , end='')
res2 = ''
for i in str[1].upper():
    shag = 2
    if i in alphabet_eng:
        place_i = alphabet_eng.index(i)
        new_place_i = place_i + shag
        res2 += alphabet_eng[new_place_i]
    else:
        res2 += i
print(res2.capitalize() + ',' , end='')
res3 = ''
for i in str[2].upper():
    shag = 3
    if i in alphabet_eng:
        place_i = alphabet_eng.index(i)
        new_place_i = place_i + shag
        res3 += alphabet_eng[new_place_i]
    else:
        res3 += i
print(res3.capitalize() + ',' , end='')
res4 = ''
for i in str[3].upper():
    shag = 4
    if i in alphabet_eng:
        place_i = alphabet_eng.index(i)
        new_place_i = place_i + shag
        res4 += alphabet_eng[new_place_i]
    else:
        res4 += i
print(res4.capitalize() + ',' , end='')