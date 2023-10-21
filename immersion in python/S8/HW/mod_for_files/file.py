import os
import json
import csv
import pickle


def _get_directory_size(directory: str):
    """
    реккурсивно проходит по всем файлам директории и возвращает общий размер всех файлов
    :param directory:
    :return: Размер файлов
    """
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Формируем путь к текущему файлу
            file_path = os.path.join(root, file)

            # Получаем размер файла и добавляем к общему размеру
            file_size = os.path.getsize(file_path)
            total_size += file_size

    return total_size


def traverse_directory(directory):
    """
    функция, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
    Результаты обхода сохраните в файлы json, csv и pickle.
    ○ Для дочерних объектов указывает родительскую директорию.
    ○ Для каждого объекта указивает файл это или директория.
    ○ Для файлов сохраняет его размер в байтах, а для директорий размер файлов в ней
     с учётом всех вложенных файлов и директорий.
    :param directory:
    :return:
    """
    # Создаем пустые списки для сохранения результатов обхода
    json_data = []
    csv_data = []
    pickle_data = []

    # Рекурсивно обходим директорию и все вложенные директории
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            # Формируем путь к текущей директории
            dir_path = os.path.join(root, dir)

            # Получаем общий размер всех файлов в директории
            dir_size = _get_directory_size(dir_path)

            # Пример обработки каждой директории
            dir_data = {'object_name': dir,
                        'object_path': dir_path,
                        'type': 'directory',
                        'size': dir_size}

            # Добавляем результаты обхода в соответствующий список
            json_data.append(dir_data)
            csv_data.append(dir_data)
            pickle_data.append(dir_data)

        for file in files:
            # Формируем путь к текущему файлу
            file_path = os.path.dirname(os.path.join(root, file))

            # Получаем тип объекта (файл или директория)
            file_type = 'file'

            # Получаем размер файла
            file_size = os.path.getsize(file_path)

            # Пример обработки каждого файла
            file_data = {'object_name': file,
                         'object_path': file_path,
                         'type': 'file',
                         'size': file_size}

            # Добавляем результаты обхода в соответствующий список
            json_data.append(file_data)
            csv_data.append(file_data)
            pickle_data.append(file_data)

    # Сохраняем результаты обхода в файлы json, csv и pickle
    with open('Files/result.json', 'w', encoding="UTF-8") as json_file:
        json.dump(json_data, json_file, indent=4)

    with open('Files/result.csv', 'w', newline='', encoding="UTF-8") as csv_file:
        writer = csv.DictWriter(csv_file,
                                fieldnames=['object_name', 'object_path', 'type', 'size'],
                                dialect="excel",
                                quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        writer.writerows(csv_data)

    with open('Files/result.pickle', 'wb') as pickle_file:
        pickle.dump(pickle_data, pickle_file)


def to_json(data_file, new_file):
    """
     создаёт из созданного ранее файла новый с данными в формате JSON.
    Имена пишите с большой буквы.
    Каждую пару сохраняйте с навой строки.
    :param data_file:
    :param new_file:
    :return:
    """
    new_json_data = {}
    with (open(data_file, "r", encoding="UTF-8") as f,
          open(new_file, "w", encoding="UTF-8") as new_f):
        for row in f:
            row_list = row.split(" ")
            new_json_data[row_list[0].capitalize()] = float(row_list[1])
        json.dump(new_json_data, new_f, indent=2)
    return new_json_data


def take_level():
    """
    функцию, которая в бесконечном цикле запрашивает имя, идентификатор и уровень доступа (от 1 до 7).
    После каждого ввода добавляйте новую информацию в JSON файл.
    Ползователи групируются по уровню доступа.
    Идентификатор пользователя выступает ключем для имени.
    Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
    При перезапуске функции уже записанные в файл данные должны сохраняться.
    :return:
    """
    with open("level_data.txt", "w", encoding="UTF-8") as f:
        groups = {str(i): list() for i in range(1, 8)}
        while True:
            user = dict()
            access = input("level: ")
            while True:
                id_ = input("id: ")
                exists = False
                for u in groups[access]:
                    if id_ in u.keys():
                        print("такой id есть в другой группе")
                        exists = True
                        break
                if not exists:
                    break
            user[id_] = input("Name: ")
            groups[access].append(user)
            if input("Exit?") == "y":
                break
        json.dump(groups, f, indent=4)


def convert_to_csv():
    """
    Переводит файл в csv формат
    :return:
    """
    with open("Files/level_data.txt", "r", encoding="UTF-8") as f:
        my_dict = json.load(f)
    with open("Files/csv_data.csv", "w", encoding="UTF-8") as r:
        csv_write = csv.writer(r, dialect="excel", quoting=csv.QUOTE_ALL)
        for access in my_dict.keys():
            if my_dict[access]:
                for user in my_dict[access]:
                    for u_id, u_name in user.items():
                        result = f"{u_id};{u_name};{access}\n"
                        r.write(result)
