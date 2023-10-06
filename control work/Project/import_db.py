import time

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


def db_import_by_date():    # todo написать функцию для выбора даты заметки
    pass


def read_file():
    rows = []
    with open('DataBase/csvDB.csv', encoding='utf-8') as file:
        for row in file:
            rows.append(row)
        return rows


def get_date_info():
    file = read_file()
    date = []

    for row in file:
        row = row.split(";")[1]
        year = time.strftime("%Y", time.localtime(float(row)))
        month = time.strftime("%m", time.localtime(float(row)))
        day = time.strftime("%d", time.localtime(float(row)))
        if len(date) == 0:
            date.append([{year: [{month: [day]}]}])
        else:
            for years in date:
                for i in years:
                    if year in i.keys():
                        for j in i[year]:
                            if month in j.keys():
                                if day in j[month]:
                                    continue
                                else:
                                    j[month].append(day)
                            else:
                                i[year].append({month: []})
                    else:
                        date.append([{year: [{month: [day]}]}])

    return date
