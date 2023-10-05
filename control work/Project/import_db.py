import user_interface as ui


def db_import():
    """
    Выводит информацию
    :return:
    """
    while True:
        command = ui.get_format()
        if command == "txt" or command == "csv":
            ui.view_data("")
            ui.view_data("Notes:", end="\n\n")
            with open('DataBase/csvDB.csv', encoding='utf-8') as file:
                for line in file:
                    if command == 'csv':
                        ui.view_data(line)
                    elif command == 'txt':
                        text = line.split(";")
                        ui.view_data(text)
        else:
            ui.unknown()
        break


def read_file():
    rows = []
    with open('DataBase/csvDB.csv', encoding='utf-8') as file:
        for row in file:
            rows.append(row)
        return rows
