import time


def view_data(data, end="\n") -> None:  # todo str | list
    """
    Выводит в консоль заметки в заданном формате
    :param data: заметка в виде строки или списка
    :param end: окончание стрроки
    :return:
    """
    if isinstance(data, list):
        print("ID: ", end="")
        for i in range(len(data)):
            if i == 1:
                print("Date: ", end="")
                print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(float(data[i]))), end=end)
            elif i == 2:
                print("Title: {}".format(data[i]), end=end)
            else:
                print(data[i], end=end)
    else:
        print(data, end=end)


def get_value(data: str):
    """
    Запрашивает информацию у пользователя
    :param data: строка с требующейся информации
    :return: строка в введённой информацией
    """
    return input(data)


def print_info(data: str) -> None:
    """
    Выводит в консоль информацию
    :param data: информация для вывода в консоль
    :return:
    """
    print(data)


def unknown():
    """
    Выводит в консоль сообщение об ошибке
    :return:
    """
    print('Unknown command')
