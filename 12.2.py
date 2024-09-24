class BeeElephant:

    def __init__(self, bee, elephant):
        self.bee = int(bee)
        self.elephant = int(elephant)

    def __str__(self):
        return self.bee, self.elephant

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.bee <= self.elephant:
            return 'tu-tu-doo-doo'
        else:
            return 'wzzzz'

    def eat(self, meal, value):
        if meal == 'nectar':
            self.elephant -= value
            self.bee += value
            if self.elephant < 0:
                self.elephant = 0
            if self.bee > 100:
                self.bee = 100
            if self.elephant > 100:
                self.elephant = 100
            if self.bee < 0:
                self.bee = 0
        elif meal == 'grass':
            self.elephant += value
            self.bee -= value
            if self.elephant < 0:
                self.elephant = 0
            if self.bee > 100:
                self.bee = 100
            if self.elephant > 100:
                self.elephant = 100
            if self.bee < 0:
                self.bee = 0
        elif meal != 'nectar' and meal != 'grass':
            print('Неверное значение')
        return self.bee, self.elephant
try:
    bee_elephant = BeeElephant(11,12)
    print(bee_elephant.__str__())
    print(bee_elephant.fly())
    print(bee_elephant.trumpet())
    print(bee_elephant.eat('nectar', 5))
except (ValueError, TypeError):
    print('Некорректные значения')