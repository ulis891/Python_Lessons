import time

import user_interface as ui
import import_db

# print(time.ctime())

# def get_last_id():
#     id_count = 1
#     with open('DataBase/csvDB.csv', 'r', encoding='utf-8') as file:
#         for _ in file:
#             id_count += 1
#     return id_count


# print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
# print(time.localtime())
# print(time.time())
# # print(time.localtime(time.time()))
#
# with open('DataBase/csvDB.csv', encoding='utf-8') as file:
#     for line in file:
#         print(isinstance(line, str))
#
# with open('DataBase/csvDB.csv', encoding='utf-8') as file:
#     for line in file:
#         text = line.split(";")
#         print(isinstance(text, list))


# print(type([3, 3]) == type(list()))
print(type([3, 3]))
print(type(list))


# def rebild_id() -> None:
#     """Упорядочивает ID контактов"""
#     count = 1
#     book = []
#     with open('DataBase/csvDB.csv','r', encoding='utf-8') as file:
#         for row in file:
#             id = int(row.split(';')[0])
#             if id != count:
#                 book.append(row.replace(str(id), str(count)))
#             else:
#                 book.append(row)
#             count += 1
#     with open('DataBase/csvDB.csv', 'w', encoding='utf-8') as file:
#         for note in book:
#             file.write(note)

# rebild_id()

# def edit_user() -> None:
#     """Изменяет существующий контакт"""
#     # show_phonebook()
#     book = []
#     id = int(input('Input note ID to edit: '))
#     with open('DataBase/csvDB.csv', 'r', encoding='utf-8') as file:
#         for row in file:
#             if id != int(row.split(';')[0]):
#                 book.append(row)
#             else:
#                 new_note = []
#                 old_info = row.split(';')
#                 for info in old_info:
#                     if old_info.index(info) == 0:
#                         new_note.append(info)
#                     elif old_info.index(info) == 1:
#                         new_note.append(str(time.time()))
#                     elif old_info.index(info) == 2:
#                         print(f'Old title {info}')
#                         new_info = input('New title: ').upper()
#                         new_note.append(new_info)
#                     else:
#                         print(f'Old note {info}')
#                         new_info = input('New note: ')
#                         new_note.append(new_info)
#                 book.append(';'.join(new_note))
#     with open('DataBase/csvDB.csv', 'w', encoding='utf-8') as file:
#         for user in book:
#             file.write(user)
#     print('Contact changed')
#
# edit_user()


# def del_contact() -> None:
#     """Удаляет контакт"""
#     book = []
#     id = int(input('print user ID to delete: '))
#     with open(phonebook, 'r') as file:
#         for row in file:
#             if id != int(row.split(';')[0]):
#                 book.append(row)
#             else:
#                 pass
#     with open(phonebook, 'w') as file:
#         for user in book:
#             file.write(user)
#     print('Contact deleted')
#     rebild_id()


def get_date_dic():
    file = import_db.read_file()
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
    #
    # print(date)
    return date


# get_date_dic()

def choise_date(data_list: list):
    note_data = []
    year_list = []
    month_list = []
    day_list = []
    print(data_list)
    ui.print_info("Choose the year of the note or leave the field empty to show all the notes")
    for year in data_list:
        year_list.append(*year)
        print(*year)
    choise_year = ui.get_value("Enter year: ")
    if len(choise_year) == 0:
        import_db.db_import()
    elif choise_year in year_list:
        note_data.append(choise_year)
        ui.print_info(f"Choose the month of the note or leave the field empty to show all the notes in {choise_year}")
        for year in data_list:
            for months in year.values():
                for month in months:
                    month_list.append(*month)
                    print(*month)
        choise_month = ui.get_value("Enter month: ")
        if len(choise_month) == 0:
            import_db.db_import_by_date(year=choise_year, month="", day="")
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
                                day_list.append(day)
                                print(day)
            choise_day = ui.get_value("Enter day: ")
            if len(choise_day) == 0:
                import_db.db_import_by_date(year=choise_year, month=choise_month, day="")
            elif choise_day in day_list:
                import_db.db_import_by_date(year=choise_year, month=choise_month, day=choise_day)
            else:
                ui.unknown()
    else:   # todo сделать так, что бы выводились только месяца выбранного года и дни выбранного месяца.
            # Добавить поведение на случай неверного воода
        ui.unknown()
    import_db.db_import_by_date(year="", month="", day="")


choise_date(get_date_dic())
