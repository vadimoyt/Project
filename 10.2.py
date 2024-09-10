from curses.ascii import isdigit


class Math():

    def addition(self, x, y):
        return float(x + y)

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return float(x * y)

    def division(self, x, y):
        return x / y

try:
    result = Math()
    print('Результат деления - ', result.division(4, 2))
    print('Результат сложения - ', result.addition(4, 2))
    print('Результат вычитания - ', result.subtraction(4, 2))
    print('Результат умножения - ', result.multiplication(4, 2))

except TypeError:
    print('Невозможно выполнить действие')
except ValueError:
    print('Оба значения должны быть цифрами')