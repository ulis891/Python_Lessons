"""Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д."""

numbers_list = [12, 4, 55, 2, 66, 86, 4, 80, 5, 2, 5, 3, 4]


def multiplication_pairs(list):
    multi_list = []
    for i in range(0, len(list) // 2):
        multi_list.append(list[i] * list[len(list) - (1 + i)])
    if len(list) > (len(multi_list) * 2):
        multi_list.append((list[len(list) // 2]) ** 2)
    return multi_list


print(multiplication_pairs(numbers_list))
