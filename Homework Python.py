#Задача 1
number  = 42
number_str = str(number)
text = "The answer is: "

result = text + number_str

#Результаты
print(number,type(number))
print(number_str,type(number_str))
print(text,type(text))
print(result,type(result))

#Задача 2
name = "Ангелина"
age = 30

text = f"Меня зовут {name}, мне {age} лет"
print(text)

#Задача 3
my_list = [1, 2, 3]
print(my_list)
my_list_copy = my_list.copy()
my_list_copy[0] = 10
print(my_list_copy)

#Задача 4
digit = int(input("Введите ваше число:"))
if digit > 0:
    print("Положительное")
elif digit == 0:
    print("Ноль")
elif digit < 0:
    print("Отрицательное")


#Задача 5
person = {

   	"name": {

       	"first_name": "Иван",
       	"last_name": "Иванов"

 },
    "address": {
    "city": "Москва",
   	"country": "Россия"
 	}

 }
person["address"]["city"] = "Санкт-Петербург"
person["address"]["postal_code"] = "333777"
print(person)
del person["address"]["city"]
print(person)

#Задача 6
#count = 0
#while count <= 10:
#  if count % 4 == 0:
#    count += 1
#      continue
#    print(count)

# Задача 7
with open("fruits.txt", "r" , encoding="utf-8") as fruits:
    for line in fruits.readlines():
        if line.startswith("a"):
            print(line)

# Задача 8
def greet_user(user_role, user_name=None):
    if user_name:
        print(f"Привет, {user_name}! Ваша роль: {user_role}." )
    else:
        print(f"Привет, Гость! Ваша роль: {user_role}.")
greet_user("admin")
greet_user("admin", user_name="Alex")

# Задача 9
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Angelina", 30)
print(student.name)
print(student.age)

# Задача 10
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        return f"self.species по имени {self.name} умеет есть"
    def sleep(self):
        return f"self.species по имени {self.name} умеет спать"

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, "Dog")

Labrador = Dog("Lucky", "Labrador")
print(Labrador.eat())
print(Labrador.sleep())