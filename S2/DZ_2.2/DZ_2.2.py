'''Задайте список из n чисел последовательности (1+ 1\n)^n и выведите на экран их сумму.'''

while True:
    try:
        number = int(input('Введите число: '))
        result_list = []
        result = 0
        for i in range(1, number + 1):
            result_list.append((1 + 1 / i) ** i)
        for i in result_list:
            result += i
        print(round(result, 3))
        break
    except (ValueError, TypeError, ZeroDivisionError):
        print('Вы ввели неверные данные')
