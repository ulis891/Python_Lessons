import user_interface as ui

# import json
# from pprint import pprint


def db_import():
    while True:
        command = ui.get_format()
        if command == 'csv':
            with open('DataBase/csvDB.csv', encoding='utf-8') as file:
                for line in file:
                    ui.view_data(line)
                break
        # elif command == 'json':
        #     with open('jsonDB.json', encoding='utf-8') as file:
        #         text = json.load(file)
        #         ui.view_data(text)
        #         break
        elif command == 'txt':
            with open('DataBase/txtDB.txt', encoding='utf-8') as file:
                for line in file:
                    ui.view_data(line)
                break
        else:
            ui.unknown()
