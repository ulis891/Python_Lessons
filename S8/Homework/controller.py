import user_interface as ui
import export_db as ex
import import_db as im


def button_click():
    while True:
        action = ui.get_action()
        if action == 'w':
            surname = ui.get_value('surname')
            name = ui.get_value('name')
            birthday = ui.get_value('birthday')
            grade = ui.get_value('grade (year and letter)')
            count = ex.find_last_student()
            ex.student_export(count, surname, name, birthday, grade)

            for i in range(ui.count_parents()):
                par_count = ex.find_last_parent()
                surname = ui.get_value(f'{i+1} parent surname')
                name = ui.get_value(f'{i+1} parent name')
                kinship = ui.get_value(f'{i+1} parent kinship')
                tel = ui.get_value(f'{i+1} parent tel')
                std_id = int(ex.find_last_student()) - 1
                ex.parents_export(par_count, surname, name, kinship, tel, std_id)

        elif action == 'r':
            im.db_import()

        elif action == 'q':
            break

        else:
            ui.unknown()
