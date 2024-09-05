#6 task 5 lesson

ls = sorted([4, 3, 65, 23, 77, 45, 32, 98])
print(ls)
element = int(input('Введите число из списка'))
while not element in ls:
    print('Этого числа нет в списке')
    element = int(input('Введите число из списка'))
else:
    print('Отлично')

def search(ls, element):
    low = 0
    high = len(ls) - 1
    result = False

    while low <= high and not result:
        middle = (low + high) // 2
        guess = ls[middle]
        if guess == element:
            result = True
            return  result
        if guess > element:
            high = middle - 1
        else:
            low = middle + 1
    return result

result = search(ls, element)
if result:
    print('Позиция искомого элемента:', ls.index(element))

#1 task 5 lesson

import math

m = 30
n = 0
x = (-1) ** n * (m ** (2 * n + 1)) / (2 * n +1)
print(math.sin(x))

l = 30
y = (-1) ** n * (l ** (2 * n + 1)) / math.factorial(2 * n)
print(math.cos(y))

#2 task 5 lesson

from multiprocessing.managers import all_methods

phone_price = int(input('Маша, введи цену телефона,'
                        'на который ты хочешь накопить?'))
daily_dep = int(input('Сколько денег в день ты можешь откладывать,'
                      'учитывая, что по воскресеньям ты будешь тратить деньги на кино?'))
whole_dep = 0
amount_days = 0
while phone_price > whole_dep:
    whole_dep += daily_dep
    amount_days += 1
    amount_weeks = amount_days / 7
print('Тебе понадобиться', amount_days + int(amount_weeks), 'дней, чтобы накопить на'
                                                            ' желаемый телефон.')
print('За столько дней ты накопишь', whole_dep, 'рублей.')


#3 task 5 lesson

n = int(input())
f1 = 1
f2 = 1
print(f1, f2, end=' ')
for i in range(2, n):
    f1, f2 = f2, f1 + f2
    n -= 1
    print(f2, end=' ')

#4 task 5 lesson

import math
a = [1, 2, 6, 56, 43, 99, 77]
print('Сумма всех чисел в списке равна', math.fsum(a))
print('Минимальное значение в списке равно', min(a))
print('Максимальное значение в списке равно', max(a))

#3 task 5 lesson

from collections import Counter
a = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
if len(a) != len(set(a)):
    print('Значения не уникальны')
    print('Количество повторений каждого элемента:', Counter(a))
else:
    print('Значения уникальны')
