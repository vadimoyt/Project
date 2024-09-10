class Car():

    counter = 0

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        Car.counter +=1

    def start_the_engine(self):
        return 'Автомобиль заведен'

    def stop_the_engine(self):
        return 'Автомобиль заглушен'

    def color_of_the_car(self):
        print(f"Машине присвоен цвет {self.color}")

    def type_of_the_car(self):
        print(f"Марка - {self.type}")

    def year_of_the_car(self):
        print(f"Машина была выпущена в {self.year} году")

car_a = Car(color="черный", type="Пежо", year="2018")
print(car_a.start_the_engine())
print(car_a.stop_the_engine())
car_a.color_of_the_car()
car_a.type_of_the_car()
car_a.year_of_the_car()
print('Номер машины в списке', car_a.counter)
print('****')
car_b = Car(color="белый", type="Мерседес", year="2020")
print(car_b.start_the_engine())
print(car_b.stop_the_engine())
car_b.color_of_the_car()
car_b.type_of_the_car()
car_b.year_of_the_car()
print('Номер машины в списке', car_b.counter)

