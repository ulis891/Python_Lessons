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
    date = {}
    month_list = []
    day_list = []

    for row in file:
        row = row.split(";")[1]
        year = time.strftime("%Y", time.localtime(float(row)))
        month = time.strftime("%m", time.localtime(float(row)))
        day = time.strftime("%d", time.localtime(float(row)))
        if len(date[year]) == 0:
            month_list.append({month: day})
            date[year] = month_list



        print(year, month, day)
        month_list.append({month: [day]})
        date[year] = month_list
        print(date)

get_date_dic()

    #
    # # data = get_value("""Input command: """)
    # return data

