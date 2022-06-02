"""Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
 многочлена и записать в файл многочлен степени пример записи в файл
 при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0
 при n=2 ==> 27x^2 + 95x + 79 = 0"""

import random as r

while True:
    try:
        n = int(input('Введите значение степени: '))

        coefficient_list = [r.randint(0, 100) for i in range(n + 1)]

        with open('polynomial.txt', 'w') as file:
            for i in coefficient_list:
                if n > 1:
                    print(f'{i}x^{n} + ', end='', file=file)
                elif n == 1:
                    print(f'{i}x + ', end='', file=file)
                else:
                    print(f'{i} = 0', file=file)
                n -= 1
        break
    except (TypeError, ValueError):
        print('Вы ввели неверные данные')
