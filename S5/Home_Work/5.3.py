"""Создайте программу для игры в "Крестики-нолики"."""

import random


def start_game(p1, p2):  # Определяем первого игрока
    start = random.randint(1, 10)
    if start % 2 == 0:
        player = p1
    else:
        player = p2
    print(f'Начинает {player}')
    return player


def check_win(board):
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 7, 8),
                       (0, 4, 8), (2, 4, 6))

    for win in win_combination:
        if board[win[0]] == board[win[1]] == board[win[2]]:
            return True

    return False


def table_daw(board):
    print('-' * 25)
    for i in range(3):
        print('|\t\t|\t\t|\t\t|')
        print(f'|\t{board[0 + i * 3]}\t|'
              f'\t{board[1 + i * 3]}\t|'
              f'\t{board[2 + i * 3]}\t|')
        print('|\t\t|\t\t|\t\t|')
        print('-' * 25)


def players_names():  # Определяем имена игроков
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока (если хотите играть с ботом, то оставьте поле пустым): ')

    if player2 == '':
        player2 = 'Bot'
    return player1, player2


def player_move(name, stage, board):  # Ход игрока - человека
    while True:
        try:
            cell = int(input(f'{name}, выберете ячейку для {stage}: '))
            if 1 <= cell <= 9:
                if cell in board:
                    board[cell - 1] = stage
                    return cell
                else:
                    print(f'Ячейка {cell} занята!\nВыберете другую')
            else:
                print('Неверный номер ячейки')
                print('Выберете от 1 до 9 ячейки')

        except (ValueError, TypeError):
            print('Введите число!!!')


def main(names):
    board = list(range(1, 10))
    s1, s2 = 'X', 'O'
    p1, p2 = names
    player = start_game(p1, p2)
    move_count = 0
    table_daw(board)
    while move_count < 9:
        if move_count % 2 == 0:
            stage = s1
        else:
            stage = s2
        if move_count > 4:
            if check_win(board):
                if player == p1:
                    player = p2
                else:
                    player = p1
                print(f'{player} выиграл!!!')
                break
        player_move(player, stage, board)
        table_daw(board)
        if player == p1:
            player = p2
        else:
            player = p1
        move_count += 1
    if move_count == 9:
        print('Ничья!!!')


main(players_names())
