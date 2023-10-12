import sys
from calendar import isleap
from datetime import datetime as dt
from random import randint

_ridel_log = dict()


def gen(max, min=1, chance=10):
    num = randint(min, max)
    for _ in range(chance):
        try:
            dig = int(input(f"Введите цифру от {min} до {max}: "))
            if dig == num:
                return True
            elif dig > num:
                print("Меньше")
            elif dig < num:
                print("Больше")
        except:
            print("Неверное значение")
    return False


def riddle_game(ridle: str, answers: list, guess_limmit: int):
    print(ridle)
    answers = {str(text).lower() for text in answers}
    guess_count = 1
    while guess_count <= guess_limmit:
        if input("Введите ответ: ") in answers:
            print(f"Угадали! С попытки №{guess_count}")
            _riddle_game_log(ridle, guess_count)
            return guess_count
        else:
            print(f"Невернрно! Отсталось {guess_limmit - guess_count} попыток.")
            guess_count += 1
    _riddle_game_log(ridle, -1)
    return -1


def _riddle_game_log(ridle: str, guess_count: int):
    if ridle not in _ridel_log.keys():
        _ridel_log[ridle] = []
    _ridel_log[ridle].append(guess_count)
    for row in _print_log():
        print(row)


def _print_log():
    return (f"{key} : {_ridel_log[key]}\n" for key in _ridel_log.keys())


def check_date(date: str):
    day, month, year = list(map(int, date.split(".")))
    try:
        dt(day=day, month=month, year=year)
        _check_leap(year)
        return True
    except:
        return False


def check_date_terminal():
    date = sys.argv[1]
    day, month, year = list(map(int, date.split(".")))
    try:
        dt(day=day, month=month, year=year)
        _check_leap(year)
        return True
    except:
        return False


def _check_leap(year):
    if isleap(year):
        print("Високосный")
    else:
        print("Не високосный")


if __name__ == '__main__':
    # riddle_game("Вопрос?", ["1", "2", "3", "4", "5"], 5)
    print(check_date("5.3.1992"))
