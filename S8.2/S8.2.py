def find_last() -> str:
    '''Находит номер последней записи в телефонной книге'''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        row_counter = 1
        for row in file:
            row_counter += 1
    return str(row_counter)

def rebild_id():
    count = 1
    with open('phonebook.txt') as file:
        for row in file:
            id = row.split(';')[0]
            print(id)
            if id != count:
                row.split(';')[0] = count
            row
    with open('phonebook.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{};{name};{surname};{phone_number}\n')

rebild_id()

def add_user () -> None:
    '''Добавляет нового пользователя в '''
    name = input('Name: ').upper()
    surname = input('Surname: ').upper()
    phone_number = input('Phone number: ')
    row_counter = 0
    with open('phonebook.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{find_last()};{name};{surname};{phone_number}\n')


def print_contact(contact: list) -> None:
    '''Печатает контакт'''
    # print('\n')
    for col in contact:
        print(col, ' ', end='')
    # print('\n')


def show_phonebook () -> None:
    '''Показывает всю телефонную книгу'''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for row in file:
            user = row.split(';')
            print_contact(user)

def search_contact () -> None:
    search_str = input('Who you need?: ').upper()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for row in file:
            list_row = row.split(';')
            if search_str in list_row:
                print_contact(list_row)


fileName = 'phonebook.txt'
def readData (fileName):
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(';'))
    return phoneBook

print(readData(fileName))

# add_user()
#
# show_phonebook()
#
# search_contact()

def main ():
    while True:
        comand = input('Input\n'
                       '    "w" for add contact,\n'
                       '    "r" for print phonebook,\n'
                       '    "s" for search contact: ')
        if comand == 'w':
            add_user()
            break
        elif comand == 'r':
            show_phonebook()
            break
        elif comand == 's':
            search_contact()
            break
        else:
            print('Unknown command. Try again')

# main()