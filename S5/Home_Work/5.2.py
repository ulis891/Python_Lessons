"""Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
ход."""

"""Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? 
Ответ: 20 конфет"""

import random


def players_names():
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока (если хотите играть с ботом, то оставьте поле пустым): ')

    if player2 == '':
        player2 = 'Bot'
    return player1, player2


def player_move(name):
    while True:
        try:
            mv = int(input(f'{name}, берите конфеты: '))
            if 1 <= mv <= 28:
                return mv
                break
            else:
                print('Неверное количество конфет')
                print('Возьмите от 1 до 28 конфет')

        except (ValueError, TypeError):
            print('Введите число!!!')


def bot_move(cand):  # bot, который пытается оставить 29 кофет на столе
    if cand % 29 == 0:
        mv = random.randint(1, 28)
    else:
        mv = cand - (cand // 29) * 29
    return mv


def start_game(p1, p2):  # Определяет первого игрока
    start = random.randint(1, 10)
    if start % 2 == 0:
        player_move = p1
    else:
        player_move = p2
    print(f'Начинает {player_move}')
    return player_move


def candies_game(names):  # Тело игры
    p1, p2 = names
    candies = 2021
    player = start_game(p1, p2)
    while candies > 28:
        while True:
            if player != 'Bot':
                move = player_move(player)

                if player == p1:
                    player = p2
                else:
                    player = p1
                candies -= move
                print(f'Осталось конфет: {candies}')
                break
            else:
                move = bot_move(candies)
                candies -= move
                print(f'{player} берёт {move} конфет')
                player = p1
                print(f'Осталось конфет: {candies}')
                break

    else:
        print(f'{player}, победил!!!!')


candies_game(players_names())
