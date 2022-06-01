"""Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""


def multiplier(n):
    multiplier_list = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                multiplier_list.append(i)
                n = int(n / i)
                break
    return multiplier_list

while True:
    try:
        num = int(input('Введите число: '))
        print(multiplier(num))
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')