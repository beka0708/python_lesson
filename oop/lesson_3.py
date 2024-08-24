class Cat:
    def __init__(self, name, age, hunger=50, energy=50, mood="happy"):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.mood = mood

    def update_mood(self):
        if self.hunger < 30:
            self.mood = "hungry"
        elif self.energy < 20:
            self.mood = "tired"
        else:
            self.mood = "happy"

    def eat(self):
        self.hunger += 10
        self.energy -= 5
        self.update_mood()
        print(f"{self.name}, поел теперь он сытый, \nНастроение: {self.mood}")

    def sleep(self):
        self.hunger -= 5
        self.energy += 10
        self.update_mood()
        print(f"{self.name}, поспал и теперь полон энергии, \nНастроение: {self.mood}")

    def play(self):
        self.hunger -= 10
        self.energy -= 10
        self.update_mood()
        print(f"{self.name}, поиграл и повеселился и устал, \nНастроение: {self.mood}")

    def status(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Сытость: {self.hunger}")
        print(f"Энергия: {self.energy}")
        print(f"Настроение: {self.mood}")


my_cat = Cat("Том", 3)
my_cat2 = Cat("Джерри", 3)


while True:
    print("Что сделать с котом? ")
    print("1. Покормить ")
    print("2. Поспать ")
    print("3. Поиграть ")
    print("4. Проверить статус ")
    print("5. Выйти ")

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
        print("Заходи еще поиграть мы тебя ждем!!!")
        break
    else:
        print("Некорректный ввод, кошка обиделась на тебя ...")





