def find_last() -> str:
    '''Находит номер последней записи в телефонной книге'''
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        row_counter = 1
        for row in file:
            row_counter += 1
    return row_counter

def rebild_id():
    count = 1
    with open('phonebook.txt') as file:
        for row in file:
            id = row.split(';')[0]
            print(id)
            if id != count:
                row.split(';')[0] = count
            row



def add_user () -> None:
    '''Добавляет нового пользователя в '''
    user = []
    user.extend([find_last(),
                 input('Name: ').upper(),
                 input('Secondname: ').upper(),
                 input('Surname: ').upper(),
                 input('Phone number: ')])
    with open('phonebook.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{str(user)}\n')


def print_contact(contact: list) -> None:
    '''Печатает контакт'''
    # print('\n')
    for col in contact:
        print(col, ' ', end='')
    # print('\n')


def list_phonebook():
    phonebook = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for row in file:
            phonebook.append(row)
    print(phonebook)


def show_phonebook () -> None:
    '''Показывает всю телефонную книгу'''
    phonebook = []
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for row in file:
            phonebook.append(row)
            print(row, end='')
    print(phonebook)
            # user = row.split(';')
            # print(user)
            # print_contact(user)

def search_contact () -> None:
    search_str = input('Who you need?: ').upper()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        for row in file:
            list_row = row.split(';')
            if search_str in list_row:
                print_contact(list_row)


fileName = 'phonebook.txt'
# def readData (fileName):
#     with open (fileName) as f:
#         phoneBook = []
#         for line in f:
#             phoneBook.append(line.split(';'))
#     return phoneBook
#
list_phonebook()

# print(readData(fileName))

# add_user()
#
show_phonebook()
#
# search_contact()

# rebild_id()

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