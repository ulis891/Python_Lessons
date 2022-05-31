"""Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
 и минимальным значением дробной части элементов."""

import random as r

while True:
    try:
        n = int(input('Введите колличество чисел: '))

        float_list = []
        for i in range(0, n):
            float_list.append(round(r.uniform(0, 10), 2))
        print(float_list)


        new_list = []
        for i in float_list:
            new_list.append(round(i - int(i), 2))

        min = new_list[0]
        max = new_list[0]
        for i in new_list:
            if i > max:
                max = i
            if i < min:
                min = i
        break
    except (ValueError, TypeError, IndexError):
        print('Вы ввели неверные данные')

print(f'Максимальное значение = {max}, минимальное значение {min}')
print(f'Разница = {round((max - min), 2)}')
