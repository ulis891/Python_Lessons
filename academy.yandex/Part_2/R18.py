"""
Новогоднее настроение 2.0
Коллеги математика вновь хотят порадовать его и сделать математические ёлки, которые украсят кабинет учёного.
Помогите им, написав программу, которая по введённому числу строит математическую ёлку.

Формат ввода
Вводится одно натуральное число — количество чисел в математической ёлке.

Формат вывода
Требуемая новогодня ёлка.
"""
#
# num = int(input())
# lst = []
# count = 1
# for i in range(1, num + 1):
#     if count > num:
#         break
#     for j in range(i):
#         if j == 0 and count < num:
#             lst.append([count])
#             count += 1
#         elif count <= num:
#             lst[-1].append(count)
#             count += 1
#             if count > num/2:
#                 lst[-1].append(count)
#                 count += 1
#
# print(lst)


num = int(input())

counter = 1  # Переменная для отслеживания текущего числа
lst = [[]]
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if counter <= num:
            lst[-1].append(counter)
            counter += 1  # Увеличиваем счетчик текущего числа
    lst.append([])
counter = lst.count([])
for i in range(counter):
    lst.remove([])


def print_tree(array: list):
    sep = len(array[-1])
    if array[-1][-1] > 9:
        sep += 1
    elif array[-1][-1] > 99:
        sep += 1
    elif array[-1][-1] < 9:
        sep -= 1
    for i in array:
        print(f"{sep * ' '}", end="")
        for j in i:
            print(j, end=" ")
        print(f"{sep * ' '}")
        if array[-3] == i:
            sep -= 1
        sep -= 1


print_tree(lst)
