import user_interface as ui

from datetime import datetime as dt


def logger(x, sing, y, result):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('time;{}; value1;{}; sing;{}; value2;{};result; {}\n'.format(time, x, sing, y, result))
