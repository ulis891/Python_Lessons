"""
Доработать пердидущую задачу.
Создать новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданых расширений может быть любым.
Количество файлов для каждого расширения различно.
Использовать вызов функции из прошлой задачи
"""
from pathlib import Path

from S7_task_4 import file_maker


def ext_maker(ext_dict: dict):
    for key, value in ext_dict.items():
        file_maker(key, count=value, path=key)


if __name__ == "__main__":
    ext_maker({"ttt": 5, "xxx": 2, "ggg": 3})
