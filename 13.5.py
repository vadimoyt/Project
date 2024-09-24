class Strategy:

    def execute(self):
        pass

class Adittion(Strategy):

    def execute(self, a, b):
        print(a + b)

class Subtraction(Strategy):

    def execute(self, a, b):
        print(a - b)

class Multiplication(Strategy):

    def execute(self, a, b):
        print(a * b)
class Division(Strategy):

    def execute(self, a, b):
        if b != 0:
            print(a / b)
        else:
            print('Not allowed')
class Calculator:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        self.strategy.execute(a, b)


a1 = Calculator(Division().execute(4,2))
a1.set_strategy(Multiplication().execute(4,2))
a1.set_strategy(Adittion().execute(4,2))
a1.set_strategy(Subtraction().execute(4,2))