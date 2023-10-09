import time

import user_interface as ui
import export_db as e
import import_db as i


def button_click():
    """
    Запускает приложение
    :return:
    """
    while True:
        action = ui.get_value("""Input command:
        "w"  to write new note
        "r"  to read data base
        "e"  to edit note
        "d"  to delete note
        "q"  to exit
        Your command: """)
        if action == 'w':
            id = get_last_id()
            date = str(time.time())
            title = ui.get_value('Title: ')
            if title == "":
                title = "None"
            note = ui.get_value('Note: ')
            if note == "":
                note = "None"
            e.cvs_export(id, date, title, note)
        elif action == 'r':
            i.choise_date(i.get_date_dic())
        elif action == 'e':
            edit_note()
        elif action == 'd':
            remove_note()
        elif action == 'q':
            break
        else:
            ui.unknown()


def get_last_id() -> str:
    """
    Возвращает идентификатор следущей заметки
    :return: идентификатор для новой заметки
    """
    id_count = 1
    file = i.read_file()
    for _ in file:
        id_count += 1
    return str(id_count)


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


def edit_note():
    """
    Выводит все заметки и запрашивает номер заметки для редактирования.
    Перезаписывает данные в файл
    :return:
    """
    i.db_import_all()
    edit_id = ui.get_value("Input note ID to edit: ")
    file = i.read_file()
    for old_note in file:
        old_note = old_note.split(";")
        if old_note[0] == edit_id:
            date = str(time.time())
            if ui.print_info(f"""Old title: {old_note[2]} Enter new title or leave the field empty: """) == "":
                title = old_note[2]
            else:
                title = ui.get_value('New title: ')
            if ui.print_info(f"""Old note: {old_note[3]} Enter new note or leave the field empty: """) == "":
                note = old_note[2]
            else:
                note = ui.get_value('Note: ')
            remove_note(str(edit_id))
            e.cvs_export(old_note[0], date, title, note)
            rebild_id()


def remove_note(note_id=""):
    """
    Выодит все заметки и запрашивает ID заметки которую надо удалить
    :return: None
    """
    notes = []
    if note_id == "":
        i.db_import_all()
        edit_id = ui.get_value("Input note ID to remove or leave the field empty: ")
    else:
        edit_id = note_id
    file = i.read_file()
    for note in file:
        note = note.split(";")
        if note[0] != edit_id:
            notes.append(";".join(note))
    with open('DataBase/csvDB.csv', 'w', encoding='utf-8') as file:
        for note in notes:
            file.write(note)
    rebild_id()
