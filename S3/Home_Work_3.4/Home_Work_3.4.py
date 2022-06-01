"""Напишите программу, которая будет преобразовывать десятичное число в двоичное."""


def dec_to_bin(dec_number):
    bin_list = []
    if dec_number == 0:
        bin_list.append(0)
    while dec_number >= 1:
        bin_list.append(dec_number - (dec_number // 2) * 2)
        dec_number = dec_number // 2
    bin_list.reverse()
    while len(bin_list) % 4 != 0:
        bin_list.insert(0, 0)
    return bin_list


def print_bin_list(bin_list):
    for i in range(0, len(bin_list)):
        if i % 4 == 0 and i != 0:
            print(' ', end='')
        print(f'{bin_list[i]}', end='')


while True:
    try:
        dec = int(input('Введите десятичное число: '))
        print_bin_list(dec_to_bin(dec))
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')
