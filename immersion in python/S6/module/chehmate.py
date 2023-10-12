from random import randint


def _is_conflict(board: list, knights: list) -> bool:
    """
    Проверяет ферзя и шахматную доску на возможность удара по другому ферзю
    :param board: шахматная доска с раставленными на ней ферзями
    :param knights: координаты ферзя
    :return: True - если ферзь может побить другоо ферзя и False - если не может
    """
    # Проверьте, бьет ли ферзь на доске данного ферзя
    x, y = knights

    #   Прповеряем наличие ферзя в линии
    if board[x - 1].count(1) > 1:
        return True

    #   Прповеряем наличие ферзя в колонне
    for i in range(len(board)):
        if i != x - 1 and board[i][y - 1] == 1:
            return True

    #   Проверка по диоганали вправо вниз
    y_counter = y
    for i in range(x, len(board)):
        if y_counter < len(board):
            if board[i][y_counter] == 1:
                return True
            y_counter += 1
        else:
            break

    # Проверка по диоганали влево вниз
    y_counter = y - 2
    for i in range(x, len(board)):
        if y_counter >= 0:
            if board[i][y_counter] == 1:
                return True
            y_counter -= 1
        else:
            break

    # Проверка по диоганали вправо вверх
    y_counter = y - 1
    x_counter = x - 1
    for i in range(x_counter):
        if y_counter < len(board) and i > 0:
            if board[i][y_counter] == 1:
                return True
            y_counter += 1
            x_counter -= 1
        else:
            break

    # Проверка по диоганали влево вверх
    y_counter = y - 2
    for i in range(x - 2, -1, -1):
        if y_counter >= 0:
            if board[i][y_counter] == 1:
                return True
            y_counter -= 1
        else:
            break
    return False


def check_knights(knights: list) -> bool:
    """
    Проверяет всех ферзей на фозможность конфликта
    :param knights: список с координатами ферзей
    :return: True - если все ферзи прошли проверку на конфликт, False - если хотябы один ферзь не прошол проверку
    """
    board = _make_board(knights)
    for knight in knights:
        if _is_conflict(board, knight):
            return False
    return True


def _find_true_board(cont_knights: int) -> bool:
    """
    Генерирует расположение ферзей на шахматной доске. И отправляет их на проверку.
    Если сгенерирована верная доска, то она отправляется на печать.
    Колличество ферзей задаётся входным парраметром
    :param cont_knights: колличество ферзей на доске
    :return: True - если на сгенерированной доске ферзи не бют друг друга, False - если бьют
    """
    knights = _gen_knights(cont_knights)
    if check_knights(knights):
        _print_board(knights)
        return True
    return False


def gen_true_board(cont_knights=8, count_board=4) -> None:
    """
    Функция принимает на вход количество ферзей на доске и количество досок которое необходимо сгенерировать.
    Отпраляет генерировать правильную доску пока не получит правильную
    :param cont_knights: количество ферзей
    :param count_board: количество досок
    :return:
    """
    while count_board > 0:
        if _find_true_board(cont_knights):
            count_board -= 1


def _make_board(knights: list) -> list:
    """
    Принимает список с координатами ферзей и возвращает шахматную доску с раставленными ферзями
    :param knights: список с координатами ферзей
    :return: список списков с "1" на месте ферзей
    """
    board = [[0 for _ in range(8)] for _ in range(8)]
    for knight in knights:
        board[knight[0] - 1][knight[1] - 1] = 1
    return board


def _print_board(knights: list) -> None:
    """
    Создаёт и выводит в консоль шахматную доску
    :param knights: список с координатами ферзей
    :return:
    """
    board = _make_board(knights)
    for row in board:
        print(row)
    print("-" * 100)


def _gen_knights(cont_knights=8) -> list:
    """
    Генерирует случайное расположение ферзей
    Количество ферзей зависит от входного параметра
    :param cont_knights: количество ферзей на доске
    :return: список с координатами ферзей
    """
    knights = []
    while cont_knights > 0:
        knight = (randint(1, 8), randint(1, 8))
        if knight not in knights:
            knights.append(knight)
            cont_knights -= 1
    return knights


if __name__ == "__main__":
    gen_true_board(8, 4)

    # # knights = [(1, 8), (2, 4), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)]
    # # knights = [(1, 4), (2, 2), (3, 8), (4, 5), (5, 7), (6, 1), (7, 3), (8, 6)]
    # knights_gen = _gen_knights(2)
    #
    # if check_knights(knights_gen):
    # if check_knights(knights):
    #     print("Ферзи не бьют друг друга")
    # else:
    #     print("Есть пары бьющих друг друга ферзей")
