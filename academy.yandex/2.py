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

a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4 * a * c
if a == b == c == 0:
    print('Infinite solutions')
elif a != 0 and b == 0 and c == 0:
    print(f'{0:.2f}')
elif a == 0 and b != 0:
    print(f'{-c / b:.2f}')
elif a != 0 and c != 0 and b == 0:
    if -c / a > 0:
        res = [(-c / a) ** 0.5, -(-c / a) ** 0.5]
        print(f'{min(res):.2f} {max(res):.2f}')
    else:
        print('No solution')
elif a != 0 and b != 0 and c == 0:
    res = [0, -b / a]
    print(f'{min(res):.2f} {max(res):.2f}')
elif D > 0:
    res = [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]
    print(f'{min(res):.2f} {max(res):.2f}')
elif D == 0:
    print(f'{-b / (2 * a):.2f}')
else:
    print('No solution')
