class Book:
    def __init__(self, title, author) :
        self.title = title
        self.author = author

    def info(self):
        return f"{self.title} Заголовок и {self.author}"
mybook = Book("Ляля", "Я")

print(mybook.info())


class Car:
    wheels = 4
car1 = Car()
car2 = Car()
print(car1.wheels)
print(car2.wheels)

class Cat:
    def __init__(self, name):
        self.name = name
    def meow(self):
        return(f"Кот {self.name} говорит Мяу!")
cat1 = Cat("Pocky")
print(cat1.meow())

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student1 = Student("Angelina", 30)
student2 = Student("Kira", 8)
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        return f"Телефон:{self.brand} {self.model}"
phone1 = Phone("Apple", "Iphone 16")
print(phone1.info())