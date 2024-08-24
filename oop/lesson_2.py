"""
наследование — наследование от родительского класса к дочерней
инкапсуляция — защищённые классы (методы)
полиморфизм — изменять методы от наследованного класса

магические методы (__init__, __str__, __len__)
""" ""

"""# class Person:
#     def __init__(self, name, age):       # конструктор
#         self.name = name
#         self.age = age
#
#     def __str__(self):     # представление объекта (для пользователей)
#         return f"Person({self.name}, {self.age})"
#
#     def __repr__(self):    # представление формального объекта (для разработчиков)
#         return f"Person('{self.name}', {self.age})"
#
#
# p = Person("Bektur", 10)
# print(str(p))
# print(repr(p))"""





"""# методы сравнения



# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __str__(self):
#         return f"Product(name {self.name}, price{self.price})"
#
#
# p1 = Product("Laptop", 12000)
# p2 = Product("Phone", 24000)
# p3 = Product("Laptop", 12000)
#
# print(p1 == p3)
# print(p1 < p3)
# print(p2 > p3)"""




"""class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
# 
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
# 
# 
# book1 = Book("Гарри потер", "Joan Roling")
# book2 = Book("Гарри потер", "Joan Roling")
# book3 = Book("New world", "Alexandro ginok")
# 
# print(book1 == book2)
# print(book1 == book3)"""



"""class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)


num1 = Number(100)
num2 = Number(20)
num3 = num1 + num2

print("Результат ", num3)
"""


class Cat:
    def __init__(self, name, age, hunger=50, energy=50):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.energy = energy

    def eat(self):
        self.hunger += 10
        self.energy -= 5
        print(f"{self.name} поел теперь он сытый!")

    def sleep(self):
        self.energy += 10
        self.hunger -= 5
        print(f"{self.name}, поспал и отдохнул")

    def play(self):
        self.energy -= 10
        self.hunger -= 5
        print(f"{self.name}, поиграл и повеселился")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Сытость: {self.hunger}")
        print(f"Энергия: {self.energy}")


my_cat = Cat("Барски", 3)

while True:
    print("\nЧто сделать с котом? ")
    print("1. Покормить")
    print("2. Поспать")
    print("3. Поиграть")
    print("4. Проверить статус")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        my_cat.eat()
    elif choice == "2":
        my_cat.sleep()
    elif choice == "3":
        my_cat.play()
    elif choice == "4":
        my_cat.status()
    elif choice == "5":
        break
    else:
        print("Некорректный ввод!!! ")



















