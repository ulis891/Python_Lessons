phonebook = 'phonebook.txt'


def separator():
    print('-' * 40)


def find_last() -> str:
    """Находит номер последней записи в телефонной книге"""
    row_counter = sum(1 for line in open(phonebook, 'r')) + 1
    return str(row_counter)


def add_user() -> None:
    """Добавляет нового пользователя в """
    surname = input('Surname: ').upper()
    name = input('Name: ').upper()
    secondname = input('Secondname: ').upper()
    phone_number = input('Phone number: ')
    with open(phonebook, 'a+', encoding='utf-8') as file:
        file.write(f'{find_last()};{surname};{name};{secondname};{phone_number}\n')
    print('Contact recorded')


def rebild_id() -> None:
    """Упорядочивает ID контактов"""
    count = 1
    book = []
    with open(phonebook, 'r') as file:
        for row in file:
            id = int(row.split(';')[0])
            if id != count:
                book.append(row.replace(str(id), str(count)))
            else:
                book.append(row)
            count += 1
    with open(phonebook, 'w') as file:
        for user in book:
            file.write(user)


def print_contact(contact: list) -> None:
    """Печатает контакт"""
    for col in contact:
        print(col, ' ', end='')


def show_phonebook() -> None:
    """Показывает всю телефонную книгу"""
    print('  ', end='')
    separator()
    print('  ', end='')
    with open(phonebook, 'r', encoding='utf-8') as file:
        for row in file:
            user = row.split(';')
            print_contact(user)
    separator()
    print('\n')


def edit_user() -> None:
    """Изменяет существующий контакт"""
    show_phonebook()
    book = []
    id = int(input('Input user ID to edit: '))
    with open(phonebook, 'r') as file:
        for row in file:
            if id != int(row.split(';')[0]):
                book.append(row)
            else:
                ed_contact = []
                old_info = row.split(';')
                for info in old_info:
                    if old_info.index(info) == 0:
                        ed_contact.append(info)
                    elif old_info.index(info) == 4:
                        print(f'Old info {info}', end='')
                        new_info = input('New info: ')
                        ed_contact.append(new_info + '\n')
                    else:
                        print(f'Old info {info}')
                        new_info = input('New info: ').upper()
                        ed_contact.append(new_info)
                book.append(';'.join(ed_contact))
    with open(phonebook, 'w') as file:
        for user in book:
            file.write(user)
    print('Contact changed')


def del_contact() -> None:
    """Удаляет контакт"""
    show_phonebook()
    book = []
    id = int(input('print user ID to delete: '))
    with open(phonebook, 'r') as file:
        for row in file:
            if id != int(row.split(';')[0]):
                book.append(row)
            else:
                pass
    with open(phonebook, 'w') as file:
        for user in book:
            file.write(user)
    print('Contact deleted')
    rebild_id()


def search_contact() -> None:
    """Ищет контакт"""
    print('  ', end='')
    separator()
    search_str = input('Who are we looking for?: ').upper()
    print('  ', end='')
    with open(phonebook, 'r', encoding='utf-8') as file:
        for row in file:
            list_row = row.split(';')
            if search_str in list_row:
                print_contact(list_row)
    separator()
