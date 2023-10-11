from random import randint

def _is_conflict(board, knights):
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
    y_counter = y
    for i in range(x - 1, -1, -1):
        if y_counter < len(board):
            if board[i][y_counter] == 1:
                return True
            y_counter += 1
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


def check_knights(knights):
    board = _make_board(knights)
    for knight in knights:
        if _is_conflict(board, knight):
            return False
    return True


def check_gen_knights(counter=1):
    if counter > 0:
        knights = _gen_knights()
        board = _make_board(knights)
        for knight in knights:
            if _is_conflict(board, knight):
                check_gen_knights(counter)
            else:
                _print_board(board)
                check_gen_knights(counter - 1)
    else:
        print("End")


def _make_board(knights: list):
    board = [[0 for _ in range(8)] for _ in range(8)]
    for knight in knights:
        board[knight[0] - 1][knight[1] - 1] = 1
    # _print_board(board)
    return board


def _print_board(board: list):
    for row in board:
        print(row)
    print("-" * 100)


def _gen_knights(num=8) -> list:
    knights = []
    while num > 0:
        knight = (randint(1, 8), randint(1, 8))
        if knight not in knights:
            knights.append(knight)
            num -= 1
    print(knights)
    return knights


if __name__ == "__main__":
    # check_gen_knights()

    knights = [(1, 8), (2, 4), (3, 1), (4, 3), (5, 6), (6, 2), (7, 7), (8, 5)]
    # knights = [(2, 2), (5, 6), (7, 8), (1, 7), (7, 5), (1, 8), (8, 4), (3, 7)]
    # knights_gen = _gen_knights()

    if check_knights(knights):
        print("Ферзи не бьют друг друга")
    else:
        print("Есть пары бьющих друг друга ферзей")
