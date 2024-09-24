number = int(input('Введите номер числа, до которого нужно выводить последовательность'))
def fibonachi(number):
    a, b = 0, 1
    actual = 0
    while actual < number:
        yield a
        a, b = b, a + b
        actual += 1

fibonachi = fibonachi(number)
for i in fibonachi:
    print(i)