"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
 и минимальным значением дробной части элементов."""

import random as r

while True:
    try:
        n = int(input('Введите колличество чисел: '))

        float_list = [ ]
        for i in range(0, n):
            float_list.append(round(r.uniform(0, 10), 2))
        print(float_list)

        new_list = []
        for i in float_list:
            new_list.append(round(i - int(i), 2))

        break
    except (ValueError, TypeError, IndexError):
        print('Вы ввели неверные данные')

print(f'Максимальное значение = {max(new_list)}\nМинимальное значение = {min(new_list)}')
print(f'Разница = {round((max(new_list) - min(new_list)), 2)}')
