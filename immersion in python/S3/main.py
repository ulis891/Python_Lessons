"""
Вручную создайте список с целыми числами, которые повторяются.
Получите новый списаок, который содержит уникальные элементы исзодного списка.
*Два решения: короткое и длинное (не использует другие колекции)
"""

# num_list = [12, 13, 12, 3, 4, 5, 5, 13, 3, 6, 7, 8, 6, 7, 9, 10]
# new_list = []
#
# for i in num_list:
#     if i not in new_list:
#         new_list.append(i)
#
# print(*num_list)
# print(*new_list)
# print(*set(num_list))

"""
Пользователь вводит данные. Сделать проверку данных и преобразуйте если возможно в один из вариантов:
 - Целое положительное число
 - Вещественное положительное или отрицательное цисло
 - Строку в нижнем регистре, если есть хотябы одна заглавная буква
 - Строку в верхнем регистре в остальных случаях
"""

# text = input()
#
# try:
#     if int(text) > 0:
#         result = int(text)
#         # print(f"Печатаю целое число: {int(text)}")
#     else:
#         raise ValueError
# except ValueError:
#     try:
#         result = float(text)
#         # print(f"Печатаю вещественное число: {float(text)}")
#     except ValueError:
#         for i in range(len(text)):
#             if text[i].isupper():
#                 result = text.lower()
#                 # print(f"Печатаю текст в нижнем регистре {text.lower()}")
#                 break
#             else:
#                 if i == len(text) - 1:
#                     result = text.upper()
#                     # print(f"Печатаю текст в верхнем регистре: {text.upper()}")
# print(result)

"""
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ - тип элемента,
значение - список элементов данного типа
"""

# my_tuple = (2, 3, "qwerty", 3.14, "france", [3, 5, "lll"], "xuy", 798, {1: "234", 2: "ppp"}, 98.78, ["123", "456"])
#
# my_dic = {}
# for i in my_tuple:
#     e_type = type(i).__name__
#     e_list = []
#     for j in my_tuple:
#         if type(j).__name__ == e_type:
#             e_list.append(j)
#     my_dic[e_type] = e_list
# print(my_dic)
#
#
# my_dic = {}
# for element in my_tuple:
#     e_type = type(element).__name__
#     if e_type not in my_dic:
#         my_dic[e_type] = []
#     my_dic[e_type].append(element)
#
# print(my_dic)


"""
Создайте вручную список с повторяющимися элементами
Удалите из него все элементы, которые встречаются дважды.
"""

# my_list = [1, 2, 3, 4, 5, 1, 2, 2, 2, 4]
#
# new_list = []
# for i in my_list:
#     if my_list.count(i) != 2:
#         new_list.append(i)
# print(new_list)


"""
Создайте вручную список с повторяющимися целыми числами.
Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы.
"""

# my_list = [1, 2, 7, 4, 5, 1, 2, 2, 2, 4]
#
# index_list = [i for i, j in enumerate(my_list, 1) if j % 2 != 0]
#
# # for i in my_list:
# #     if i % 2 != 0:
# #         index_list.append(my_list.index(i) + 1)
# #         my_list[my_list.index(i)] = 2
# print(*index_list)


"""
Пользователь вводит строку текста. Вывести каждое словао с новаой строки.
Слова нумеруюся начиная с единицы. Слова выводятся отсортированными согласно кодировке unicode.
Текст выравнивается по праваму краю так, чтобы у самого длинного слова был один пробел между ним и номером строки
"""
#
# text = ("Пользователь вводит строку текста Вывести каждое словао с новаой строки Слова нумеруюся начиная с единицы "
#         "Слова выводятся отсортированными согласно кодировке unicode Текст выравнивается по праваму краю")
#
# text = text.split(" ")
# text.sort()
#
# max_len = 0
# for t in text:
#     t = t.replace(" ", "")
#     if len(t) > max_len:
#         max_len = len(t)
#
# for i in range(1, len(text)):
#     sep = max_len
#     if i < 10:
#         sep += 1
#     print(f"{i} {text[i - 1]: >{sep}}")

"""
Пользователь вводит строку текста.
Посчитать сколько раз встречается каждая буква в строке.
Результат сохранить в словаре
 - ключ - символ
 - значение - частота
"""

# text = ("Пользователь вводит строку текста Вывести каждое словао с новой строки Слова нумеруюся начиная с единицы "
#         "Слова выводятся отсортированными согласно кодировке unicode Текст выравнивается по праваму краю")
#
# text = text.lower().replace(" ", "")
#
# print(text)
#
# fr_dic = {}
#
# for char in text:
#     if char not in fr_dic:
#         fr_dic[char] = 0
#     fr_dic[char] += 1
#
# print(fr_dic)

"""
Три друг взяли вещи в поход. Сформируйте словарь:
 - ключ - имя друга
 - значение - кортеж вещей
Какие вещи взяли все 3 друга?
Какие вещи уникальны?
Какие вещи есть у всех, кроме одного? И у кого её нету?
"""

toristers = {"Петя": {"Палатка", "Носки", "Трусы"},
             "Коля": {"Гитара", "Носки", "Трусы"},
             "Саша": {"Спички", "Носки", "Ноутбук"}}

multi_bag = list(toristers.values())[0]

for bag in list(toristers.values())[1:]:
    multi_bag = multi_bag.intersection(bag)

print(list(multi_bag))

value_count = {}
for values in toristers.values():
    for value in values:
        if value not in value_count:
            value_count[value] = 0
        value_count[value] += 1

print(value_count)
for key, value in value_count.items():
    if value == 1:
        print(key, end=" ")
print()


for key, value in value_count.items():
    if value == 2:
        for k, v in toristers.items():
            if key not in v:
                print(f"У {k} нету {key}")

