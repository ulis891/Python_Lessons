import time

import user_interface as ui
import export_db as e
import import_db as i


def button_click():
    while True:
        action = ui.get_action()
        if action == 'w':
            id = get_last_id()
            date = time.time()
            title = ui.get_value('title')
            note = ui.get_value('note')
            e.cvs_export(id, date, title, note)
            # note = ui.get_value('note')
            # description = ui.get_value('description')
            # e.txt_export(title, note, tel, description)
            # e.json_export(surname, name, tel, description)

        elif action == 'r':
            i.db_import()

        elif action == 'q':
            break

        else:
            ui.unknown()


def get_last_id() -> int:
    """
    Возвращает идентификатор следущей заметки
    :return:
    """
    id_count = 1
    with open('DataBase/csvDB.csv', 'r', encoding='utf-8') as file:
        for _ in file:
            id_count += 1
    return id_count


def rebild_id() -> None:
    """Упорядочивает ID контактов"""
    count = 1
    book = []
    with open('DataBase/csvDB.csv','r', encoding='utf-8') as file:
        for row in file:
            id = int(row.split(';')[0])
            if id != count:
                book.append(row.replace(str(id), str(count)))
            else:
                book.append(row)
            count += 1
    with open('DataBase/csvDB.csv', 'w', encoding='utf-8') as file:
        for note in book:
            file.write(note)
