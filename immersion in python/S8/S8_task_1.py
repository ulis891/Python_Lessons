"""
Напишите функцию которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с навой строки.
"""
from pprint import pprint
import json


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


pprint(to_json("task_3.txt", "new.txt"))
