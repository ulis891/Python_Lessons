import time

import user_interface as ui


def read_file() -> list:
    """
    Возвращает список строк из базы заметок
    :return:
    """
    rows = []
    with open('DataBase/csvDB.csv', encoding='utf-8') as file:
        for row in file:
            rows.append(row)
        return rows


def db_import_all(command="txt"):
    """
    Выводит все заметки в заданном виде.
    По умолчанию в формотированном виде
    :param command: "txt" или "csv"
    :return:
    """
    while True:
        if command == "txt" or command == "csv":
            ui.view_data("")
            ui.view_data("Notes:", end="\n\n")
            file = read_file()
            for line in file:
                if command == 'csv':
                    ui.view_data(line)
                elif command == 'txt':
                    text = line.split(";")
                    ui.view_data(text)
        else:
            ui.unknown()
        break


def db_import(year="", month="", day=""):
    """
    Выводит информацию
    @param year: год создания или редактирования заметки
    @param month: месяц создания или редактирования заметки
    @param day: день создания или редактирования заметки
    @return: None
    """
    while True:
        command = ui.get_value("input 'csv' or 'txt' fromat: ")
        if command == "txt" or command == "csv":
            ui.view_data("")
            ui.view_data("Notes:", end="\n\n")
            file = read_file()
            for line in file:
                row = line.split(";")[1]
                if len(year) != 0:
                    if year != time.strftime("%Y", time.localtime(float(row))):
                        continue
                if len(month) != 0:
                    if month != time.strftime("%m", time.localtime(float(row))):
                        continue
                if len(day) != 0:
                    if day != time.strftime("%d", time.localtime(float(row))):
                        continue
                if command == 'csv':
                    ui.view_data(line)
                elif command == 'txt':
                    ui.view_data(line.split(";"))
        else:
            ui.unknown()
        break


def get_date_info():
    """
    Проходится по файлу с заметками и возвращает даты заметок в формате
    [{year_1 : [{month_1 : [day_1, day_2,...]},
                {month_2 : [day_1, day_2,...]}],
    {year_2 : [{month_3 : [day_1, day_2,...]},
                {month_4 : [day_1, day_2,...]}]}]
    :return: Список словарей дат заметок
    """
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


def get_date_dic():
    file = read_file()
    date = []
    for row in file:
        row = row.split(";")[1]
        year = time.strftime("%Y", time.localtime(float(row)))
        month = time.strftime("%m", time.localtime(float(row)))
        day = time.strftime("%d", time.localtime(float(row)))
        if len(date) == 0:
            date.append({year: [{month: [day]}]})
        else:
            for years in date:
                if year in years.keys():
                    for j in years[year]:
                        if month in j.keys():
                            if day in j[month]:
                                continue
                            else:
                                j[month].append(day)
                        else:
                            years[year].append({month: []})
                else:
                    date.append({year: [{month: [day]}]})
    return date


def choise_date(data_list: list):
    """
    Запрашивает у пользователя дату необходимых заметок
    :param data_list: Список словарей дат заметок
    :return:
    """
    note_data = []
    year_list = []
    month_list = []
    day_list = []
    ui.print_info("Choose the year of the note or leave the field empty to show all the notes")
    for year in data_list:
        if str(*year) not in year_list:
            year_list.append(*year)
            print(*year)
    choise_year = ui.get_value("Enter year: ")
    if len(choise_year) == 0:
        db_import(year="", month="", day="")
    elif choise_year in year_list:
        note_data.append(choise_year)
        ui.print_info(f"Choose the month of the note or leave the field empty to show all the notes in {choise_year}")
        for year in data_list:
            for months in year.values():
                for month in months:
                    if str(*year) == choise_year:
                        if str(*month) not in month_list:
                            month_list.append(*month)
                            print(*month)
        choise_month = ui.get_value("Enter month: ")
        if len(choise_month) == 0:
            db_import(year=choise_year, month="", day="")
        elif choise_month not in month_list:
            ui.unknown()
        else:
            note_data.append(choise_month)
            ui.print_info(
                f"Choose the day of the note"
                f" or leave the field empty to show all the notes in {choise_month}.{choise_year}")
            for year in data_list:
                for months in year.values():
                    for month in months:
                        for days in month.values():
                            for day in days:
                                if str(*year) == choise_year and str(*month) == choise_month:
                                    if day not in day_list:
                                        day_list.append(day)
                                        print(day)
            choise_day = ui.get_value("Enter day: ")
            if len(choise_day) == 0:
                db_import(year=choise_year, month=choise_month, day="")
            elif choise_day in day_list:
                db_import(year=choise_year, month=choise_month, day=choise_day)
            else:
                ui.unknown()
    else:
        ui.unknown()
