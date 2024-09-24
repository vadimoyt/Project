from abc import abstractmethod

class Animal:

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print('Af-af-af')

class Cat(Animal):

    def speak(self):
        print('Mew-mew-mew')

class AnimalFactory:

    def create_animal(self, animal_type):
        if animal_type == 'Dog':
            animal = Dog()
        elif animal_type == 'Cat':
            animal = Cat()
        else:
            raise ValueError('Unknown type of animal')
        animal.speak()
        return animal

animal1 = AnimalFactory()
animal1.create_animal('Dog')
animal2 = AnimalFactory()
animal2.create_animal('Cat')