"""
Напишите функию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
среди которых обязательно должны быть гласные.
Полученные имена сохранять в файл
"""
from random import randint, random


file = "task_2.txt"


import random

VOWEL_SET = ["A", "E", "I", "O", "U", "Y"]


def name_filler(f_name: str, line_num: int):
    with open(f_name, "a", encoding="UTF-8") as f:
        for _ in range(line_num):
            name = []
            for _ in range(random.randint(4, 7)):
                name.append(chr(random.randint(ord("a"), ord("z"))))
            name[random.randint(0, len(name)-1)] = random.choice(VOWEL_SET)
            f.write(f"{''.join(name).capitalize()}\n")


if __name__ == "__main__":
    name_filler(file, 10)
