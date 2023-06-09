"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def mul(a_a: int, b_b: int) -> int:
    """Считаем степень числа"""
    print(a_a, b_b)
    if b_b < 2:
        return 'Reshenie'
    else:
        return mul(a_a * st, b_b - 1)


st = n = int(input('Введите число: '))
m = int(input('Введите степень: '))
rtt = mul(n, m)
print(rtt)
