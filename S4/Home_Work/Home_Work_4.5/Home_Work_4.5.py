"""Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
содержащий сумму многочленов. (нужно два полинома сложить. Файлы взять благодаря предыдущему заданию)"""

with open('polynomial_1.txt') as file1:
    for line in file1:
        s1 = str(line.split('=')[:-1]).strip("[]'")

with open('polynomial_2.txt') as file2:
    for line in file2:
        s2 = str(line.split('=')[:-1]).strip("[]'")

polynomial_sum = s1 + '+ ' + s2
with open('polynomial_sum.txt', 'w') as result:
    print(polynomial_sum + '= 0', file=result)


sep_polynominal = []    # Разделяем уравнение по многочленам
for i in polynomial_sum.split('+'):
    sep_polynominal.append(i.rstrip())

degree_list = []    # Список для многочленов в степени > 1
x_list = []         # Список многочленов в степени = 1
free_list = []      # Список многочленов без аргумента

for i in sep_polynominal:   # Распределяем многочлены по спискам
    if not 'x' in i:
        free_list.append(i)
    elif '^' in i:
        degree_list.append(i)
    else:
        x_list.append(i)

free_sum = 0        # Считаем сумму элементов без аргументов
for i in free_list:
    free_sum += int(i)

x_sum_list = []
x_sum = 0
for i in x_list:        # Считаем сумму элементов с аргументом
    x_sum_list.append(i.split('x'))
for j in range(len(x_list)):
    x_sum += int(x_sum_list[j][0])

degree_list_split = []
for i in degree_list:       # Разделяем числа и степень аргумента
    degree_list_split.append(i.split('x^'))

degree_list_split_sum = []

for j in range(len(degree_list_split)):     # Находим и сумируем елементы с одинаковой степенью аргумента
    for i in range(len(degree_list_split)):
        if degree_list_split[j][1] == degree_list_split[i][1] and j != i and j < i:
            degree_list_split_sum.append(
                str(int(degree_list_split[j][0]) + int(degree_list_split[i][0])) + 'x^' + str(degree_list_split[j][1]))

sep_x_split_list = []
for i in degree_list:       # Разделяем множества на коэфицеты и степени аргумента
    sep_x_split_list.append(i.split('x'))


alone_degree_element = []
for j in degree_list_split_sum:     # Составляем список множеств с неповторяющимися степенями
    for k in range(len(sep_x_split_list)):
        for i in sep_x_split_list:

            if j.rstrip()[-2::] not in sep_x_split_list[k] and len(alone_degree_element) < len(degree_list_split_sum):
                alone_degree_element.append(i)

degree = ''
for i in alone_degree_element:      # Собираем запись множеств с неповторяющимися степенями
    degree += i[0] + 'x' + i[1] + ' +'

x_srting = ''
for i in degree_list_split_sum:     # Собираем запись сумм множеств с повторяющимися степенями
    x_srting += i + ' + '

final_result = degree + x_srting + str(x_sum) + 'x' + ' + ' + str(free_sum) + ' = 0'    # Собираем строку для записи

with open('polynomial_sum.txt', 'a') as result:
    print(final_result, end='', file=result)