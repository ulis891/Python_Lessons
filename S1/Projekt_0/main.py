# напишите программу для проверки 2 чисел. является ли одно квадратом другого
# print("введите первое число")
# a = int(input())
# print("введите второе число")
# b = int(input())
# if a == b * 2 or b == a ** 2:
#     print("одно число является квадратом другого числа")
# else:
#     print("числа не являютя квадратами друг друга")


# Напишите программу, которая принимает 5 чисел и находит максимальное из них

# i = 0
# list = []
# while i < 5:
#     a = int(input(f"Введите число {i+1}: "))
#     list.append(a)
#     i += 1
# n_max = list[0]
# for n in list:
#     if n >= n_max:
#         n_max = n
# print(f"максимальное число равняется {n_max}")


# Напишите программу, которая принимает на вход число N  и выводит все числа от -N до N

# n = int(input("Введите число: "))
#
# if n > 0:
#     N = -n
#     while N <= n:
#         print(f'{N}', end=' ')
#         N += 1
# else:
#     N = n * -1
#     while n <= N:
#         print(f'{n}', end=' ')
#         n += 1


# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15 но не 30

num = int(input("Введите число: "))
if ((num % 5 == 0 and num % 10 == 0) or num % 15 and not num % 30 == 0):
    print("Yes")
else:
    print("No")
