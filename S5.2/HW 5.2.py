"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""


<<<<<<< HEAD
def mul(a_a: int, b_b: int) -> int:
    """Считаем степень числа"""
    print(a_a, b_b)
    if b_b < 2:
        return 'Reshenie'
    else:
        return mul(a_a * st, b_b - 1)
=======
def mul(a: int, b: int) -> int:
    """Считаем степень числа"""
    if b < 2:
        return a
    else:
        return mul(a * st, b - 1)
>>>>>>> origin/HEAD


st = n = int(input('Введите число: '))
m = int(input('Введите степень: '))
<<<<<<< HEAD
rtt = mul(n, m)
print(rtt)
=======
print(mul(n, m))



"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""


def summ(i: int, j: int) -> int:
    """Считаем сумму чисел"""
    if j < 1:
        return i
    else:
        return summ(i + 1, j - 1)


n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
print(summ(n, m))
>>>>>>> origin/HEAD
