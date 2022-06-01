"""Задайте последовательность чисел. Напишите программу,
 которая выведет список неповторяющихся элементов исходной последовательности."""

import random as r


def no_copy(list_of_numbers):
    no_copy_list = []

    for i in list_of_numbers:
        if list_of_numbers.count(i) < 2:
            no_copy_list.append(i)
    return no_copy_list


while True:
    try:
        num = int(input('Введите колличество чисел: '))
        num_list = []

        for i in range(0, num):
            num_list.append(r.randint(0, 100))
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')

print(f'Созданный список: {num_list}')
print(f'Список неповторяющихся элементов: {no_copy(num_list)}')
