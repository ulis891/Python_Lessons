import user_interface as ui
import export_db as e
import import_db as i


def button_click():
    while True:
        action = ui.get_action()
        if action == 'w':
            surname = ui.get_value('surname')
            name = ui.get_value('name')
            tel = ui.get_value('tel')
            description = ui.get_value('description')
            e.cvs_export(surname, name, tel, description)
            e.txt_export(surname, name, tel, description)
            # e.json_export(surname, name, tel, description)

        elif action == 'r':
            i.db_import()

        elif action == 'q':
            break

        else:
            ui.unknown()
