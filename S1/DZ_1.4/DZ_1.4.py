# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).

while True:
    try:
        quarter = int(input("Введите номер четверти (от 1 до 4) в котророй находиться точка: "))

        if quarter == 1:
            x = '>'
            y = '>'
        elif quarter == 2:
            x = '<'
            y = '>'
        elif quarter == 3:
            x = '<'
            y = '<'
        elif quarter == 4:
            x = '>'
            y = '<'
        print(f"Точка находится в диапазоне X {x} 0 и Y {y} 0")
        break
    except (ValueError, NameError):
        print("Вы ввели неверные данные!")
