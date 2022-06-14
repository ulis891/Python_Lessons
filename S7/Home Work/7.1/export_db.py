# import json


def cvs_export(surname, name, tel, description):
    with open('DataBase/csvDB.csv', 'a+', encoding='utf-8') as file:
        file.write('surname;{};name;{};tel;{};description;{}\n'.format(surname, name, tel, description))


def txt_export(surname, name, tel, description):
    with open('DataBase/txtDB.txt', 'a+', encoding='utf-8') as file:
        file.write(f'surname: {surname}\nname: {name}\ntel: {tel}\ndescription: {description}\n\n')

# def json_export(surname, name, tel, description):
#     new_json = {tel: {"surname": surname,
#                       "name": name,
#                       "description": description}}
#
#     with open('jsonDB.json', 'r', encoding='utf-8') as file:
#         data = json.load(file)
#         data.append(new_json)
#
#     with open('jsonDB.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, indent=2)
