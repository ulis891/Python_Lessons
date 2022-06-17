import user_interface as ui


def db_import():
    while True:
        request = ui.find_student()
        if request == 'q':
            break
        else:
            id_list = []
            data = []
            with open('DataBase/Students.txt', encoding='utf-8') as f:
                for row in f:
                    if request in row:
                        id_list.append(row.split(';')[0])
                        data.append(row)
                if len(data) == 0:
                    ui.unknown('name')
                    break
                else:
                    for i in range(0, len(id_list)):
                        ui.separator()
                        ui.view_data(data[i][2:].replace(';', ' '))
                        with open('DataBase/Parents.txt', 'r', encoding='utf-8') as f:
                            for row in f:
                                if row.split(';')[-1] == f'{id_list[i]}\n':
                                    ui.view_data(str(row.split(';')[1:5]))
                        ui.separator()
            break
