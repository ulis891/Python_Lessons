def view_data(data):
    print(data)


def get_value(data):
    return input(f'{data} = ')


def get_format():
    layout = input('input "csv" or "txt" or "json": ')
    return layout


def get_action():
    action = input('input "w" to write new contact or "r" to read data base or "q" to exit: ')
    return action


def unknown():
    print('Unknown command')
