"""
Создайте функцию которая ссздаёт файлы с указанным расширением.
Функция принимает следующие параметры:
- расширение
- минимальная длинна случайно сгенерированного имени, по умолчанию 6
- максимальная длинна случайно сгенерированного имени, по умолчанию 30
- минимальное число случайных байт, по умолчанию 256
- Максимальное число случайных байт, по умолчанию 4096
- колличество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона
"""
from random import randint


def gen_name(name_min, name_max):
    name = ""
    for i in range(randint(name_min, name_max)):
        name += chr(randint(ord("a"), ord("z")))
    return name


def file_maker(expansion, name_min=6, name_max=30, byte_min=256, byte_max=4096, count=5):
    for _ in range(count):
        with open(gen_name(name_min, name_max) + "." + expansion, "w") as f:
            f.write(gen_name(byte_min, byte_max))


if __name__ == "__main__":
    file_maker("ttt")
