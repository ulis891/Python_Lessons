def view_data(data):
    print(data)


def get_value(data):
    return input(f'{data} = ')


def find_student():
    layout = input('input students surname (q to exit): ')
    return layout


def count_parents():
    count = int(input('how many parents?: '))
    return count


def get_action():
    action = input('input "w" to write new or "r" to read data base or "q" to exit: ')
    return action


def unknown(type='command'):
    print(f'Unknown {type}')


def separator():
    print('-' * 25)
