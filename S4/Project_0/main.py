# """Задайте строку из набора чисел. Напишите программу, которая покажет
# большее и меньшее число. В качестве символа-разделителя используйте пробел"""
#
# num_str = '45 34 87 2 99 32'
# spl = num_str.split(' ')
#
# for i in range(0, len(spl)):
#     spl[i] = int(spl[i])
#
# print(max(spl), min(spl))


# """Найдите корни квадратнонго уравнения Ax**2 + Bx + c = 0 двумя спосабами:
#     1) с помощью математических фармул нахождения корней квадратного уравнения
#     2) с помощью даполнительных библиотек Python"""
#
# a = int(input('Введите А: '))
# b = int(input('Введите B: '))
# c = int(input('Введите C: '))
#
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b + d ** 0.5) / 2 * a
#     x2 = (-b - d ** 0.5) / 2 * a
#     print(f'x1 =  {x1}\nx2= {x2}')
# elif d == 0:
#     x = -(b/2*a)
#     print(x)
# else:
#     print('Корней нет')


"""Задайте 2 числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел"""

a = int(input('Введите А: '))
b = int(input('Введите B: '))


def NOD(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x == y:
        return x
    if x == 1 or y == 1:
        return 1
    if x % 2 == 0 and y % 2 == 0:
        return 2 * NOD(x / 2, y / 2)
    if x % 2 == 0 and y % 2 != 0:
        return NOD(x / 2, y)
    if x % 2 != 0 and y % 2 == 0:
        return NOD(x, y / 2)
    if x % 2 != 0 and y % 2 != 0 and y > x:
        return NOD((y - x) / 2, x)
    if x % 2 != 0 and y % 2 != 0 and x > y:
        return NOD((x - y) / 2, y)


def NOK(x, y):
    return (x * y) / NOD(x, y)


print(NOD(a, b))
print(NOK(a, b))
