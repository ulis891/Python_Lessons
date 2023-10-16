import os
from pathlib import Path
from random import random, randint, choice


def create_random_num_pair(file_name: str, count: int):
    """
    Создаёт файл с парами чисел. Первое число - целое, второе - вещественное. Разделитель - |
    :param file_name: имя файла
    :param count: количество записей
    :return:
    """
    for _ in range(count):
        int_num = randint(-1000, 1000)
        float_num = 2000 * random() - 1000
        with open(file_name, "a", encoding="utf-8") as f:
            f.write(f"{int_num}|{float_num}\n")


def name_filler(f_name: str, line_num: int):
    """
    генерирует псевдоимена.
    Имя начинаться с заглавной буквы, состоять из 4-7 букв,
    среди которых обязательно должны быть гласные.
    Полученные имена сохраняет в файл
    :param f_name: имя файла
    :param line_num: количество записей
    :return:
    """
    VOWEL_SET = ["A", "E", "I", "O", "U", "Y"]
    with open(f_name, "a", encoding="UTF-8") as f:
        for _ in range(line_num):
            name = []
            for _ in range(randint(4, 7)):
                name.append(chr(randint(ord("a"), ord("z"))))
            name[randint(0, len(name) - 1)] = choice(VOWEL_SET)
            f.write(f"{''.join(name).capitalize()}\n")


def _make_lists(file_1: str, file_2: str):
    """
    Создаёт списки из строк из двух файлов
    :param file_1: первый файл
    :param file_2: втрорй файл
    :return: кортеж из двух списков
    """
    name_list = []
    num_list = []
    with open(file_1, "r", encoding="UTF-8") as f_name:
        for row in f_name:
            name_list.append(row)

    with open(file_2, "r", encoding="UTF-8") as f_name:
        for row in f_name:
            num_list.append(int(row.split('|')[0]) * float(row.split('|')[1]))
    return name_list, num_list


def _print_file(file, list_1, list_2):
    """
    Создаёт и записывает в файл информацю из двух списков
    :param file: имя файла
    :param list_1: первый список с информацией
    :param list_2: второй список с информацией
    :return:
    """
    with open(file, "a", encoding="UTF-8") as f_res:
        f_res.write(f"{list_1} {list_2}\n")


def _to_fixed(num: float, digits=0) -> float:
    """
    Оставляет заданное количество знаков после запятой у вещественного числа
    :param num: вещественное число
    :param digits: количество знаков после запятой
    :return: вещественное число
    """
    return float(f"{num:.{digits}f}")


def join_file(name_file: str, num_file: str, new_file: str):
    """
    Открывает на чтение файлы с числами и именами.
    перемножает пары чисел.
    В новый файл сохраняет имя и произведение:
        если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю.

        если результат умножения положительный, сохраните имя прописными буквами и произведение округлите до целого.

    В результирующем файле столько же строк, сколько в более длинном файле.
    При достижении конца более короткого файло в его начало.
    :param name_file: имя файла с именами
    :param num_file:   имя файла с числами
    :param new_file: имя нового фойла
    :return:
    """
    joins = _make_lists(name_file, num_file)
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
            num = abs(_to_fixed(num, 2))
        else:
            name = name.upper()[:-1]
            num = int(num)
        _print_file(new_file, name, num)


def _gen_name(name_min: int, name_max: int):
    """
    Генерирует случайные наборы букв
    :param name_min: минимальное количество букв
    :param name_max: максималльное количество букв
    :return: сгенерированное имя
    """
    name = ""
    for i in range(randint(name_min, name_max)):
        name += chr(randint(ord("a"), ord("z")))
    return name


def file_maker(extension: str, name_min=6, name_max=30, byte_min=256, byte_max=4096, count=5, path=""):
    """
    Создает фойлы с заданными параметрами и случайныи именами
    :param extension: расширение файла
    :param name_min:  минимальное количество букв в названии файла
    :param name_max:  максимальное количество букв в названии файла
    :param byte_min:    минимальное количество знаков в файле
    :param byte_max:    максимальное количество знаков в файле
    :param count:   количество файлов
    :param path:    путь к папке где будут создаваться файлы
    :return:
    """
    for _ in range(count):
        if path != "":
            file_path = Path.cwd() / Path(path)
            if not file_path.exists():
                file_path.mkdir()
            file_path = file_path / Path(_gen_name(name_min, name_max) + "." + extension)
        else:
            file_path = Path.cwd() / Path(_gen_name(name_min, name_max) + "." + extension)
        with open(file_path, "w") as f:
            f.write(_gen_name(byte_min, byte_max))


def ext_maker(ext_dict: dict):
    """
    Создаёт фойлы в заданном колличистве и разрешении и распределяет их по папкам согластно разрешению
    :param ext_dict: словарь где ключ - разрешение, значение - количество файлов {"txt": 5}
    :return:
    """
    for key, value in ext_dict.items():
        file_maker(key, count=value, path=key)


def create_subdir(ext: str, wd=Path.cwd()):
    """
    Функция для сортировкм файлов по директориям: видео, изабражения, текст и т.д.
    Каждая группа вклчает файлы с несколкими расширениями.
    В исходной папке должны остаться толко те файлы, которые не подошли для сортировки
    :param ext: разширение необходимых файлов
    :param wd: путь для создания директории
    :return:
    """
    cur_path = Path(wd) / Path(ext + "_dir")
    try:
        cur_path.mkdir()
    except FileExistsError:

        pass
    for file in wd.iterdir():
        if file.suffix == "." + ext:
            file.replace(cur_path / file.name)


def batch_rename_files(dir_name, desired_name, num_digits, source_extension, target_extension, name_range=None):
    """
    Переименовывает все файлы в заданной директории.
    При переименовании в конце имени добавляется порядковый номер.
    К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение.
    :param dir_name:    директория где ниобходимо переименовать файлы
    :param desired_name:    желаемое конечное имя файлов
    :param num_digits:  количество цифр в порядковом номере
    :param source_extension:    расширение исходного файла
    :param target_extension:    расширение конечного файла
    :param name_range:  диапазон сохраняемого оригинального имени.
    Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла
    :return:
    """
    files = os.listdir(f"{dir_name}")

    filtered_files = []
    for file in files:
        if file.endswith(source_extension):
            filtered_files.append(file)

    for i, file in enumerate(filtered_files):
        if name_range is None or len(file) < name_range[1]:
            name = file
        else:
            name = file[name_range[0]:name_range[1]]

        new_name = name + desired_name + str(i).zfill(num_digits) + target_extension

        os.rename(Path(dir_name + "/" + file), Path(dir_name + "/" + new_name))
