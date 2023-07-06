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
# print(f'1. {first}\n'
#       f'2. {second}\n'
#       f'3. {therd}')


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

a = list(map(int, input()))
b = list(map(int, input()))
max_num = max([(max(a)), max(b)])
min_num = min([(min(a)), min(b)])
if max_num in a:
    a.remove(max(a))
    b.remove(min(b))
else:
    a.remove(min(a))
    b.remove(max(b))
mean_num = list(str(sum(a + b)))[-1]
print(max_num, mean_num, min_num, sep='')

# mid_num = int(a.remove(max(a))) + b.remove(max(b))
# print(mid_num)