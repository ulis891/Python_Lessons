"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def mul(a: int, b: int) -> int:
    print(a, b)
    if b < 2:
        return 'Reshenie'
    else:
        mul(a * st, b - 1)


n = int(input('Введите число: '))
m = int(input('Введите степень: '))
st = n
print(mul(n, m))
