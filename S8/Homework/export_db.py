def find_last_student():  # Находит последнюю запись учеников
    with open('DataBase/Students.txt', 'r', encoding='utf-8') as file:
        last_student = 0
        for row in file:
            last_student += 1
    return str(last_student)


def find_last_parent():  # Находит последнюю запись родителей
    with open('DataBase/Parents.txt', 'r', encoding='utf-8') as file:
        last_parent = 0
        for row in file:
            last_parent += 1
    return str(last_parent)


def student_export(count, surname, name, birthday, grade):
    with open('DataBase/Students.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{count};{surname};{name};{birthday};{grade}\n')


def parents_export(par_count, surname, name, kinship, tel, std_id):
    with open('DataBase/Parents.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{par_count};{surname};{name};{kinship};{tel};{std_id}\n')
