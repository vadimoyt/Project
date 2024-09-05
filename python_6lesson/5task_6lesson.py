massage = input().upper()
choise = int(input('Введите "1" для шифрования сообщения или "2" для дешифрования '))
while choise != 1 and choise != 2:
    choise = int(input('Попробуйте еще раз'))

alphabet_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
shag = int(input('Введите шаг шифрования/дешифрования'))

if choise == 1:
    def shifr(massage):
        result = ''
        for i in massage:
            if i in alphabet_rus:
                place_i = alphabet_rus.index(i)
                new_place_i = place_i + shag
                result += alphabet_rus[new_place_i]
            if i in alphabet_eng:
                place_i = alphabet_eng.index(i)
                new_place_i = place_i + shag
                result += alphabet_eng[new_place_i]
            else:
                result += i
        return  result
    print(shifr(massage).capitalize())


if choise == 2:
    def shifr(massage):
        result = ''
        for i in massage:
            if i in alphabet_rus:
                place_i = alphabet_rus.index(i)
                new_place_i = place_i - shag
                result += alphabet_rus[new_place_i]
            if i in alphabet_eng:
                place_i = alphabet_eng.index(i)
                new_place_i = place_i - shag
                result += alphabet_eng[new_place_i]
            else:
                result += i
        return  result
    print(shifr(massage).capitalize())















