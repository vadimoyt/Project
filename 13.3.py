class Pizza:

    def __init__(self, size='unknown', cheese='no', pepperoni='no', mushrooms='no', onions='no', bacon='no'):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        return (f'Pizza with: size - {self.size},\ncheese - {self.cheese},\npepperoni - {self.pepperoni},\n'
                f'mushrooms - {self.mushrooms},\nonions - {self.onions},\nbacon - {self.bacon}\n')

class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()

    def add_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def add_pepperoni(self, pepperoni):
        self.pizza.pepperoni = pepperoni
        return self

    def add_mushrooms(self, mushrooms):
        self.pizza.mushrooms = mushrooms
        return self

    def add_onions(self, onions):
        self.pizza.onions = onions
        return self

    def add_bacon(self, bacon):
        self.pizza.bacon = bacon
        return self

    def get_pizza(self):
        return self.pizza


class PizzaDirector:

    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        self.builder.add_size('medium').add_cheese('cheder')
        return self.builder.get_pizza()

builder1 = PizzaBuilder()
director1 = PizzaDirector(builder1)
pizza1 = director1.make_pizza()
print(pizza1)

builder2 = PizzaBuilder()
director2 = PizzaDirector(builder2)
pizza2 = director2.make_pizza()
builder2.add_bacon(True).add_onions(True).add_mushrooms('champignons')
print(pizza2)

