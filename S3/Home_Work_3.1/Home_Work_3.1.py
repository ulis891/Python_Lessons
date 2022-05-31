"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции."""

numbers_list = [12, 4, 55, 2, 66, 86, 4, 80, 5, 2, 5, 3, 7]


def sum_odd_index(list):
    sum_odd = 0
    for i in range(0, len(list), 2):
        sum_odd += list[i]
    return sum_odd


print(sum_odd_index(numbers_list))
