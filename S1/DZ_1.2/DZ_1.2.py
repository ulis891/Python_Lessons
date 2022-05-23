# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Введите 1 - для True или 0 - для false")
while True:
    x = input("Введите значение для X: ")
    if x == "0":
        x = False
        break
    if x == "1":
        x = True
        break
    else:
        print("Вы ввели неверное значение")

while True:
    y = input("Введите значение для Y: ")
    if y == "0":
        y = False
        break
    if y == "1":
        y = True
        break
    else:
        print("Вы ввел и неверное значение")

while True:
    z = input("Введите значение для Z: ")
    if z == "0":
        z = False
        break
    if z == "1":
        z = True
        break
    else:
        print("Вы ввели неверное значение")

if not (x and y and z) == (not x or not y or not z):
    print("True")
else:
    print("False")
