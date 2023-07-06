import controller as c



def main() -> None:
    '''Запускает телефонный справочник'''
    while True:
        comand = input('Input'
                       '   "w" to add a contact\n'
                       '        "r" to view the phone book\n'
                       '        "s" to search for a contact \n'
                       '        "e" to edit the contact\n'
                       '        "d" for to delete the contact\n'
                       '    :')
        if comand == 'w':
            c.add_user()

        elif comand == 'r':
            c.show_phonebook()

        elif comand == 's':
            c.search_contact()

        elif comand == 'e':
            c.edit_user()

        elif comand == 'd':
            c.del_contact()

        else:
            print('Unknown command. Try again')

main()