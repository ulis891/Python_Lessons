"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
path_long = "/home/alrksandrkostromin/PycharmProjects/Python_Lessons/S8.2/phonebook.txt"


def pars_path(path: str) -> tuple:
    """
    Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    @param path: абсолютный путь до файла
    @return: кортеж из трёх элементов: путь, имя файла, расширение файла.
    """
    *path_short, name_extension = path.split("/")
    path_short = "/".join(path_short) + "/"
    name, extension = name_extension.split(".")
    return path_short, name, extension


print(pars_path(path_long))
