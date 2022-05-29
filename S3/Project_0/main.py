# This is a sample Python script.

# """Реализуйте алгоритм задания рандомных чисел без
# использоварния встроенного генератора случайных чисел"""
#
# from datetime import datetime
# import time
#
#
# def my_shuffle(n):
#     res = []
#     for i in range(0, n + 1):
#         r = datetime.now().microsecond % 10
#         res.append(r)
#         time.sleep(0.00002)
#     return res
#
#
# print(my_shuffle(int(input('Введите колличество элементов: '))))


# """Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число"""
#
# list = ['5', '9', '8', '7', 'sd', 'op', 'ss']
#
# if input('Введите искомое:') in list:
#     print('True')
# else:
#     print('False')
#

# """напишите программу, которая определит позицию
# второго вхождения строки в список либо сообщит, что её нет"""
#
# list = ['5', '9', '8', '7', 'sd', 'op', 'ss', '9', '55', '7', 'sd', '9']
#
# n = input('Введите искомое: ')
# count = 0
# buffer = None
# for i in range(0, len(list)):
#     if n == list[i]:
#         count += 1
#
#         if count == 2:
#             buffer = i
#
#
# if count > 0:
#     if count == 1:
#         end = ''
#     else:
#         end = 'a'
#     print(f'{n} входит в список {count} раз{end}. Второй раз на позиции {buffer}')
# else:
#     print(f'строки {n} нет в списке')
#
# # """Для натурального N создать множество -3 ** N"""
#
# n = int(input('Введите число: '))


def mnojestvo(n):
    return [(-3) ** i for i in range(n)]


# print(mnojestvo(n))


"""Сформировать список из N чисел последовательности.
Список задать в файл "number_list.txt (в одну строку - одно число)"""

x = int(input('Введите число: '))
data = open('number_list.txt', 'w')
list = mnojestvo(x)
for i in list:
    data.write(str(i) + '\n')
data.close()
