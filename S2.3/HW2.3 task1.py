"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
"""
import fractions


def gcd_fun(a: int, b: int) -> int:
    """
    Находим НОД
    """
    while b:
        a, b = b, a % b
    return int(a)


def lcm_fun(a: int, b: int) -> int:
    """
    Находим НОК
    """
    return int((a * b) // gcd_fun(a, b))


def mul_fra(a: list, b: list) -> str:
    """
    Умножаем дроби
    """
    gcd = gcd_fun(a[0] * b[0], a[1] * b[1])
    chis = int(a[0] * b[0] / gcd)
    znam = int(a[1] * b[1] / gcd)
    return str(chis) + "/" + str(znam)


def sum_fra(a: list, b: list) -> str:
    """
    Сумируем дроби
    """
    lcm = lcm_fun(a[1], b[1])
    mul1 = int(lcm / a[1])
    mul2 = int(lcm / b[1])
    chis = a[0] * mul1 + b[0] * mul2
    return str(int(chis / gcd_fun(chis, lcm))) + "/" + str(int(lcm / gcd_fun(chis, lcm)))


x = input("Первая дробь - ")
y = input("Вторая дробь - ")

fraction1 = list(map(int, x.split("/")))
fraction2 = list(map(int, y.split("/")))

print("\nДроби полученые самостоятельно")
print(sum_fra(fraction1, fraction2))
print(mul_fra(fraction1, fraction2))

r = fractions.Fraction(x)
z = fractions.Fraction(y)

print("\nДроби полученые через fractions")
print(r + z)
print(r * z)
