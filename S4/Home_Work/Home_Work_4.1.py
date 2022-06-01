"""Ввычислить число пи,
(использовать Ряд Нилаканта или любой другой вариант расчета числа Пи)
 c заданной точностью d"""
import math


def euler(de):
    sum = 0
    for i in range(1, de + 1):
        sum += 1 / (i ** 2)
    sum *= 6
    return math.sqrt(sum)


def neelaknt(de):
    sum = 0
    shift = True
    for i in range(2, de, 2):
        if shift:
            sum += 4 / (i * (i + 1) * (i + 2))
            shift = False
        else:
            sum -= 4 / (i * (i + 1) * (i + 2))
            shift = True
    sum += 3
    return sum


while True:
    try:
        d = int(input("Введите точность: "))
        if d > 1:
            print(f'Число π по формуле Нилаканта с точностью {d} равно: {neelaknt(d)}')
            print(f'Число π по формуле Эйлера с точностью {d} равно: {euler(d)}')
        else:
            raise ValueError
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')
