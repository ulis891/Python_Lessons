"""
Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам
"""

slog_dic = 'йуеыаоэяиюeyuoai'
count_dic = {}
count_list = []

poem = input("Введите стих: ")

s1 = poem.split(' ')

for i in s1:
    count_dic[i] = 0
    for char in i:
        if char in slog_dic:
            count_dic[i] += 1

for j, p in count_dic.items():
    count_list.append(p)

if len(list(filter(lambda x: x - count_list[0] == 0, count_list))) != len(count_list):
    print("Пам парам")
else:
    print("Парам пам-пам")

"""
Задача 36:
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) ` 
**Вывод:**
"""


def print_operation_table(func, a: int, b: int):
    """Печатает таблицу """
    arr = [i for i in range(1, a + 1)]
    for k in arr:
        print_char(k)
    print('\n')
    for j in range(2, b + 1):
        print_char(j)
        for k in arr[1:]:
            print_char(func(k, j))

        print('\n')


def print_char(char_in_table: int):
    """Печатает число с правильным отступом"""
    if len(str(char_in_table)) == 1:
        print(char_in_table, ' ' * 3, end='')
    elif len(str(char_in_table)) == 2:
        print(char_in_table, ' ' * 2, end='')
    else:
        print(char_in_table, ' ', end='')


num_columns = int(input('Введите количество колонок: '))
num_rows = int(input('Введите количество строк: '))

print_operation_table((lambda c, r: c + r), num_columns, num_rows)
