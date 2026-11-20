from oop1 import car1


class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} eat"
class Dog(Animal):
 ...
dog = Dog("Rex")
print(dog.eat())


class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def info(self):
        return f"Бренд: {self.brand}"
class Car(Vehicle):
    def drive(self):
        return f"Машина едет"
car1 = Car("BMW")
print(car1.info())
print(car1.drive())
