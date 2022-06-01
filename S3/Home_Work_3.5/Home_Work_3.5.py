"""Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""


def nega_fibonachi(n):
    fibo_list = [0, 1]
    nega_fibo_list = [0, 1]

    for i in range(2, n + 1):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
        nega_fibo_list.append(nega_fibo_list[i - 2] - nega_fibo_list[i - 1])
    nega_fibo_list.reverse()
    result = nega_fibo_list[:-1] + fibo_list
    print(result)


while True:
    try:
        num = int(input('Введите число: '))
        if num == 0:
            print([0])
        else:
            nega_fibonachi(num)
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')
