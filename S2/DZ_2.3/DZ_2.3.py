"""Реализуйте алгоритм перемешивания списка"""
import random

data_list = ['мама', 'мыла', 'раму']


# random.shuffle(list)
# print(list)


def list_shuffle(list_to_shuffle):
    new_list = list_to_shuffle
    for i in range(len(new_list) - 1, 0, -1):
        j = random.randint(0, i)
        new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list


print(f'Начальный список: {data_list} \nИзмененный список: {list_shuffle(data_list)}')
