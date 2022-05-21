# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).


while True:
    try:
        x = int(input("Введите отличные от 0 координаты по оси Х: "))
        y = int(input("Введите отличные от 0 координаты по оси Y: "))

        if x > 0 and y > 0:
            quarter = 1
        elif x < 0 and y > 0:
            quarter = 2
        elif x < 0 and y < 0:
            quarter = 3
        elif x > 0 and y < 0:
            quarter = 4
        print(f"Точка находится в четверти № {quarter}")
        break
    except (ValueError, NameError):
        print("Вы ввели не число или ввели 0!")
