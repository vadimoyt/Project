class Bus:

    def __init__(self, speed, max_amount, max_speed, list_of_passangers, empty):
        self.speed = float(speed)
        self.max_amount = int(max_amount)
        self.max_speed = float(max_speed)
        self.list_of_passangers = list(list_of_passangers)
        self.actual_amount = len(self.list_of_passangers)
        self.empty = empty
        self.places = {str(key): None for key in range(1, self.max_amount + 1)}
        for i, passenger in enumerate(self.list_of_passangers):
            self.places[str(i + 1)] = passenger

    def in_bus(self, *surname):
        for passanger in surname:
            if self.actual_amount >= self.max_amount:
                print(f'Мы не можем вместить всех, уменьшите список на {self.actual_amount - self.max_amount}')
                break
            for key, value in self.places.items():
                if value is None:
                    self.places[key] = passanger
                    self.list_of_passangers.append(passanger)
                    self.actual_amount += 1
                    break
        return f'Новый список пассажиров: {self.list_of_passangers},\nКоличество пассажиров: {self.actual_amount},\nМеста: {self.places}'

    def out_bus(self, *surname):
        for passanger in surname:
            if passanger in self.list_of_passangers:
                self.list_of_passangers.remove(passanger)
                for key, value in self.places.items():
                    if value == passanger:
                        self.places[key] = None
                        break
                self.actual_amount -= 1
            else:
                print(f'Такого пассажира {passanger} нет в автобусе.')
        return f'Новый список пассажиров: {self.list_of_passangers},\nКоличество пассажиров: {self.actual_amount},\nМеста: {self.places}'

    def free_seats(self):
        return 'Количество свободных мест:', len([seat for seat in self.places.values() if seat is None])

    def plus_or_minus_speed(self, plus_or_minus, how_much):
        if plus_or_minus == 'plus':
            self.speed += how_much
            if self.speed > self.max_speed:
                print('Нельзя ехать быстрее')
                self.speed = self.max_speed
        if plus_or_minus == 'minus':
            self.speed -= how_much
            if self.speed < 0:
                print('Медленнее некуда')
                self.speed = 0
        return f'Сейчас скорость такая: {self.speed}'

    def info(self):
        return (f"Текущая скорость: {self.speed},\nВместимость: {self.max_amount},\nМаксимальная скорость: {self.max_speed},\n"
                f"Список пассажиров: {self.list_of_passangers},\nКоличество пассажиров: {self.actual_amount}\n"
                f"Флаг места: {self.empty},\nСловарь мест: {self.places}")


bus = Bus(speed=80, max_amount=10, max_speed=90, list_of_passangers=('Carter', 'Palmer', 'Lem', 'Potter'), empty=True)
print(bus.info())
print(bus.free_seats())
print('***')
print(bus.in_bus('Marley', 'Jonson', 'Raidiuk', 'McCartney', 'Volsbrug'))
print('***')
print(bus.out_bus('Marley', 'Lem'))
print(bus.plus_or_minus_speed('minus', 81))
print(bus.free_seats())