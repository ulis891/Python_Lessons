"""
Напишите функцию, которая открывает на чтение созданные файлы с числами и именами.
перемножите пары чисел.
В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю.
если результат умножения положительный, сохраните имя прописными буквами и произведение округлите до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
при достижении конца более короткого файло в его начало.
"""

file_1 = "task_1.txt"
file_2 = "task_2.txt"
file = "task_3.txt"


def make_lists(name_file, num_file):
    name_list = []
    num_list = []
    with open(name_file, "r", encoding="UTF-8") as f_name:
        for row in f_name:
            name_list.append(row)

    with open(num_file, "r", encoding="UTF-8") as f_name:
        for row in f_name:
            num_list.append(int(row.split('|')[0]) * float(row.split('|')[1]))
    return name_list, num_list


def print_file(name, num):
    with open(file, "a", encoding="UTF-8") as f_res:
        f_res.write(f"{name} {num}\n")


def to_fixed(num, digits=0):
    return float(f"{num:.{digits}f}")


def join_file(joins):
    count = max(len(joins[0]), len(joins[1]))
    name_iter_list = iter(joins[0])
    num_iter_list = iter(joins[1])

    for _ in range(count):
        try:
            num = next(num_iter_list)
        except StopIteration:
            num_iter_list = iter(joins[1])
            num = next(num_iter_list)
        try:
            name = next(name_iter_list)
        except StopIteration:
            name_iter_list = iter(joins[0])
            name = next(name_iter_list)
        if num < 0:
            name = name.lower()[:-1]
            num = abs(to_fixed(num, 2))
        else:
            name = name.upper()[:-1]
            num = int(num)
        print_file(name, num)


join_file(make_lists(file_2, file_1))
