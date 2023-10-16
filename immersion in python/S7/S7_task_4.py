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
from pathlib import Path
from random import randint


def gen_name(name_min, name_max):
    name = ""
    for i in range(randint(name_min, name_max)):
        name += chr(randint(ord("a"), ord("z")))
    return name


def file_maker(expansion, name_min=6, name_max=30, byte_min=256, byte_max=4096, count=5, path=""):
    for _ in range(count):
        if path != "":
            file_path = Path.cwd() / Path(path)
            if not file_path.exists():
                file_path.mkdir()
            file_path = file_path / Path(gen_name(name_min, name_max) + "." + expansion)
        else:
            file_path = Path.cwd() / Path(gen_name(name_min, name_max) + "." + expansion)
        with open(file_path, "w") as f:
            f.write(gen_name(byte_min, byte_max))


if __name__ == "__main__":
    file_maker("ttt", path="txt_dir")
