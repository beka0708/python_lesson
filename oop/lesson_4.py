# class Bank:
#     def __init__(self, name, balance):
#         self._name = name
#         self._balance = balance
#
#     def moneyX(self):
#         while True:
#             card = int(input("1) Узнать ваш баланс\n2)Пополнить баланс "))
#             if card == 1:
#                 print(f"Ваш баланс {self._balance}")
#                 break
#             elif card == 2:
#                 top_up = int(input("Сколько хотите добавить? "))
#                 print(f"Теперь ваш баланс составляет {self._balance + int(top_up)}")
#                 break
#             else:
#                 print("Введите правильный номер!!!")
#
#     def _kill(self):
#         print("Ваш счет обнуляется...")
#         self._balance = self._balance - self._balance
#         return self._balance
#
#     def __jackpot(self):
#         self._balance *= 10
#         print(f"Баланс после джекпота {self._balance}")
#
#     @property
#     def jackpot(self):
#         return self.__jackpot
#
#     def copy(self, other):
#         if isinstance(other, Bank):
#             self._balance += other._balance
#             print(f"Ваш баланс объединен. Новый баланс {self._balance}")
#         else:
#             print("Можно объединить только с объектом класса Bank")
#
#     def __str__(self):
#         return f"Name {self._name}, balance {self._balance}"
#
#
#
# account1 = Bank("Bektur", 2000)
# account2 = Bank("Baiel", 1000)
# # account2.moneyX()
# # print(account1._kill())
# # print(dir(Bank))
# # account1._Bank__jackpot()
# # account1.copy(account2)
# # print(account1.__str__())
# # print(account2.__str__())


# class Calculator:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Calculator(self.value + other.value)
#
#     def __sub__(self, other):
#         return Calculator(self.value - other.value)
#
#     def __mul__(self, other):
#         return Calculator(self.value * other.value)
#
#     def __truediv__(self, other):
#         if other.value == 0:
#             raise ValueError("На ноль делить нельзя!!!")
#         return Calculator(self.value / other.value)
#
#     def __str__(self):
#         return str(self.value)
#
#
# calc1 = Calculator(10)
# calc2 = Calculator(0)
#
# print(f"Сумма {calc1 + calc2}")
# print(f"Разность {calc1 - calc2}")
# print(f"Произведение {calc1 * calc2}")
# print(f"Частное {calc1 / calc2}")


# class Animal:
#     def speak(self):
#         return "Животное издает звук. "
#
#
# class Dog(Animal):
#     def speak(self):
#         return super().speak() + " Гав!!!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return super().speak() + " Мяу!!!"
#
#
# def animal_sounds(animal):
#     print(animal.speak())
#
#
# dog = Dog()
# cat = Cat()
#
#
# animal_sounds(dog)
# animal_sounds(cat)