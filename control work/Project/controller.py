import time

import user_interface as ui
import export_db as e
import import_db as i


def button_click():
    while True:
        action = ui.get_value("""Input command:
        "w"  to write new note
        "r"  to read data base
        "q"  to exit
        Your command: """)
        if action == 'w':
            id = get_last_id()
            date = time.time()
            title = ui.get_value('title')
            note = ui.get_value('note')
            e.cvs_export(id, date, title, note)
        elif action == 'r':
            i.db_import()
        elif action == 'd':
            i.db_import_by_date()
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
    file = i.read_file()
    for _ in file:
        id_count += 1
    return id_count


def rebild_id() -> None:
    """Упорядочивает ID контактов"""
    count = 1
    book = []
    file = i.read_file()
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
