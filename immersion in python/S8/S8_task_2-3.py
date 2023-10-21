"""
напишите функцию, которая в бесконечном цикле запрашивает имя, идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Ползователи групируются по уровню доступа.
Идентификатор пользователя выступает ключем для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import json
import csv


def take_level():
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


"""
Перевод из JSON в CSV
"""


def convert_to_csv():
    with open("level_data.txt", "r", encoding="UTF-8") as f:
        my_dict = json.load(f)
    with open("csv_data.csv", "w", encoding="UTF-8") as r:
        csv_write = csv.writer(r, dialect="excel", quoting=csv.QUOTE_ALL)
        for access in my_dict.keys():
            if my_dict[access]:
                for user in my_dict[access]:
                    for u_id, u_name in user.items():
                        result = f"{u_id};{u_name};{access}\n"
                        r.write(result)


if __name__ == "__main__":
    # take_level()
    convert_to_csv()
