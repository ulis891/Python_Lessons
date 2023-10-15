from random import randint, random

file = "task_1.txt"


def task_1(file_name, count):
    for _ in range(count):
        int_num = randint(-1000, 1000)
        float_num = 2000 * random() - 1000
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"{int_num}|{float_num}\n")


task_1(file, 10)
