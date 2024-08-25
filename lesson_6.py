# list - список
# Преобразование в верхний регистр
# Напишите программу, которая подсчитывает количество гласных в каждой строке.
glas = "ауоиэыяюеё"

while True:
    word = input("введите слово ").lower()
    a = 0
    b = 0
    for i in word:
        if i in glas:
            a += 1
        else:
            b += 1
    print(f"Количество гласных {a}\nКоличество согласных {b}")










"""удаление"""
# del words[:2]
# words.remove(False)
# deli = words.pop(5)
# print(deli)


"""добавление"""
# words.append("last")
# words.insert(3, "for")
# words.extend(numbers)
# words += numbers


"""изменение"""
# words[1] = 100
# words[0], words[6] = words[6], words[0]
# words[2:4] = ["Java", "C++"]
