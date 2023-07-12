# name = input('Как Вас зовут?')
# print(f'Здраствуйте, {name}!')
# hay = input('Как дела?')
# match hay:
#     case 'хорошо':
#         print('Я за вас рада!')
#     case 'плохо':
#         print('Всё наладится!')

#
# p = int(input())
# v = int(input())
# t = int(input())
#
# if v < p > t:
#     first = 'Петя'
#     if v > t:
#         second = 'Вася'
#         therd = 'Толя'
#     else:
#         second = 'Толя'
#         therd = 'Вася'
#
# elif p < v > t:
#     first = 'Вася'
#     if p > t:
#         second = 'Петя'
#         therd = 'Толя'
#     else:
#         second = 'Толя'
#         therd = 'Петя'
# else:
#     first = 'Толя'
#     if p > v:
#         second = 'Петя'
#         therd = 'Вася'
#     else:
#         second = 'Вася'
#         therd = 'Петя'
#
# print(f'{" " * 8}{first: ^8}\n'
#       f'{second: ^8}\n'
#       f'{" " * 16}{therd: ^8}\n'
#       f'{"II": ^8}'
#       f'{"I": ^8}'
#       f'{"III": ^8}')


# year = int(input())
#
# if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# n = input()
# i = int(n[0]) + int(n[1])
# j = int(n[1]) + int(n[2])
# if i > j:
#     print(i, j, sep='')
# else:
#     print(j, i, sep='')

# num = list(map(int, list(input())))
# i = max(num) + min(num)
# num.remove(max(num))
# num.remove(min(num))
# print(num)
# if i == num[0] * 2:
#     print('YES')
# else:
#     print('NO')


# a = input()
# b = input()
# c = input()
# for i in range(len(a)):
#     if a[i] == b[i] == c[i]:
#         print(a[i])

# n = sorted(list(map(int, input())))
#
# if min(n) == 0 and n[1] == 0:
#     first = second = str(n[2]) + '0'
#
# elif min(n) == 0 and n[1] != 0:
#     first = str(n[1]) + str(n[0])
#     second = str(n[2]) + str(n[1])
#
# else:
#     first = str(n[0]) + str(n[1])
#     second = str(n[2]) + str(n[1])
# print(first, second)

# a = list(map(int, input()))
# b = list(map(int, input()))
# max_num = max([(max(a)), max(b)])
# min_num = min([(min(a)), min(b)])
# mean_num = []
# if max_num in a and min_num in a:
#     mean_num = b
# elif max_num in b and min_num in b:
#     mean_num = a
# elif max_num in a and min_num in b:
#     a.remove(max(a))
#     b.remove(min(b))
#     mean_num = a + b
# else:
#     a.remove(min(a))
#     b.remove(max(b))
#     mean_num = a + b
# mean_num = list(str(sum(mean_num)))[-1]
# print(max_num, mean_num, min_num, sep='')

# mid_num = int(a.remove(max(a))) + b.remove(max(b))
# print(mid_num)


# g = 29
# merch = input()
# price = int(input())
# weight = int(input())
# cash = int(input())
# print(f'{"Чек":=^35}\n'
#       f'Товар:{merch: >29}\n'
#       f'Цена:{" " * (18 - (len(str(weight) + str(price))))} {weight}кг * {price}руб/кг\n'
#       f'Итого:{" " * (26 - (len(str(price * weight))))}{price * weight}руб\n'
#       f'Внесено: {" " * (23 - (len(str(cash))))}{cash}руб\n'
#       f'Сдача: {" " * (25 - (len(str(cash - price * weight))))}{cash - price * weight}руб\n'
#       f'{"=" * 35}')

# name = input()
# num = input()
# print(f'Группа №{num[0]}.\n'
#       f'{num[2]}. {name}\n'
#       f'Шкафчик: {num}.\n'
#       f'Кроватка: {num[1]}')

# x = int(input())
# y = int(input())
# ch3 = str(x % 10 + y % 10)[-1]
# x = x // 10
# y = y // 10
# ch2 = str(x % 10 + y % 10)[-1]
# x = x // 10
# y = y // 10
# ch1 = str(x % 10 + y % 10)[-1]
# print(ch1, ch2, ch3, sep='')

# h = int(input())
# m = int(input())
# t = int(input())
#
# ht =
# mt = t % 60
#
#
#
# hh = h + (ht // 24) + ((m + mt) // 60)
# mm = (m + mt) % 60
#
#
# print((m + mt) // 60)
# print(ht // 24)
# print(f'{hh:0>2}:{mm:0>2}')

# current_hour = int(input("Введите текущий час: "))
# current_minute = int(input("Введите текущую минуту: "))
# delivery_time = int(input("Введите время доставки в минутах: "))
#
# total_minutes = current_hour * 60 + current_minute + delivery_time
# final_hour = (total_minutes // 60) % 24
# final_minute = total_minutes % 60
#
#
# print(f'{final_hour:0>2}:{final_minute:0>2}')


# a = float(input())
# b = float(input())
# c = float(input())
# D = b**2 - 4 * a * c
# if a == b == c == 0:
#     print('Infinite solutions')
# elif a != 0 and b == 0 and c == 0:
#     print(f'{0:.2f}')
# elif a == 0 and b != 0:
#     print(f'{-c / b:.2f}')
# elif a != 0 and c != 0 and b == 0:
#     if -c / a > 0:
#         res = [(-c / a) ** 0.5, -(-c / a) ** 0.5]
#         print(f'{min(res):.2f} {max(res):.2f}')
#     else:
#         print('No solution')
# elif a != 0 and b != 0 and c == 0:
#     res = [0, -b / a]
#     print(f'{min(res):.2f} {max(res):.2f}')
# elif D > 0:
#     res = [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
#     print(f'{min(res):.2f} {max(res):.2f}')
# elif D == 0:
#     print(f'{-b / (2 * a):.2f}')
# else:
#     print('No solution')


# import math
#
# a = float(input())
# b = float(input())
# c = float(input())
# pi = math.pi
# deg = [math.acos((a**2 + c**2 - b**2) / (2 * a * c)) * (180 / pi),
#        math.acos((a**2 + b**2 - c**2) / (2 * a * b)) * (180 / pi),
#        math.acos((b**2 + c**2 - a**2) / (2 * b * c)) * (180 / pi)]
#
# for i in range(len(deg)):
#     if deg[i] == 90:
#         print('100%')
#         break
#     elif deg[i] > 90:
#         print('велика')
#         break
#     elif i == 2 and deg[i] != 90 and deg[i] < 90:
#         print('крайне мала')


# num_1 = int(input())
# num_2 = int(input())


# def nod(a: int, b: int) -> int:
#     if a % b == 0:
#         return b
#     else:
#         return nod(b, a % b)
#
#
# if num_2 > num_1:
#     gcd = nod(num_2, num_1)
# else:
#     gcd = nod(num_1, num_2)
#
# lcm = int((abs(num_1 * num_2)) / gcd)
# print(lcm)
#
# num = int(input())
# def fackt(j):
#     res = 1
#     for i in range(j):
#         res += i * res
#     return res
#
# print(fackt(num))


# x = 0
# y = 0
#
#
# while True:
#     move = input()
#     if move == 'СТОП':
#         break
#     step = int(input())
#     if move == 'СЕВЕР':
#         y += step
#     elif move == 'ЮГ':
#         y -= step
#     elif move == 'ВОСТОК':
#         x += step
#     elif move == 'ЗАПАД':
#         x += step
# print(x)
# print(y)

# print(sum(list(map(int, list(input())))))


# print(''.join(list(map(str, list(filter(lambda x: x % 2 != 0, list(map(int, list(input())))))))))


# def prime(num: int) -> list:
#     prime_list = []
#     for i in range(num // 2 + 1, 2, -1):
#         print(i)
#         if i < 3:
#             prime_list.append(i)
#         else:
#             for j in range(2, i // 2 + 1):
#                 if i % j == 0:
#                     break
#                 if j == i // 2:
#                     prime_list.append(j)
#     return prime_list
#
#
# print(prime(10))

# for j in range(10):
#     num = int(input())
#     if num == 1:
#         print('NO')
#     elif num == 2 or num == 3:
#         print('YES')
#     else:
#         for i in range(2, num // 2 + 2):
#             if num % i == 0:
#                 print('NO')
#                 break
#             if i == num // 2:
#                 print('YES')
#
# rrr = int(input())
#
#
# def is_prime(num):
#     prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
#     i = 5
#     d = 2
#
#     while prime and i * i <= num:
#         prime = num % i != 0
#         i += d
#         d = 6 - d
#     return prime
#
#
# def cheeknumb(num, del_list):
#     for i in del_list:
#         if num % i == 0:
#             num = num / i
#             result_list.append(i)
#             cheeknumb(num, del_list)
#             break
#
#
# prime_list = [i for i in range(rrr // 2 + 1) if is_prime(i)]
# prime_list.reverse()
#
# result_list = []
# cheeknumb(rrr, prime_list)
#
# result_list.reverse()
#
# for i in range(len(result_list)):
#     if i == len(result_list) - 1:
#         print(f'{result_list[i]}')
#     else:
#         print(f'{result_list[i]} *', end=' ')


# num_list = [1, 1001]
# print(num_list)
# num = sum(num_list) // 2
#
# while True:
#     print(num)
#     chek = input()
#     if chek == 'Угадал!':
#         break
#     elif chek == 'Больше':
#         num_list[0] = num
#         num = sum(num_list) // 2
#         print(num_list)
#     elif chek == 'Меньше':
#         num_list[1] = num
#         num = sum(num_list) // 2
#         print(num_list)

def check_hashes(N, blocks):
    prev_hash = 0  # Хэш предыдущего блока
    for i in range(N):
        block = blocks[i]
        m = block // 256 ** 2  # Полезная информация блока
        r = (block // 256) % 256  # Случайное число блока
        h = block % 256  # Хэш блока

        if h != (37 * (m + r + prev_hash)) % 256 or h >= 100:
            return i  # Номер первого блока с неправильным хэшем
        prev_hash = h
    return -1  # Все хэши правильные


# Считываем количество блоков
N = int(input())

# Считываем блоки
blocks = []
for _ in range(N):
    blocks.append(int(input()))

# Проверяем хэши
result = check_hashes(N, blocks)

# Выводим результат
print(result)

# n = int(input())
# p = 0
# bad = - 1
# for i in range(n+1):
#     b = int(input())
#     h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
#     t = ((m + r + p) * 37) % 256
#     if t != h or h >= 100:
#         bad = i
#         break
#     p = h
# print(bad)
