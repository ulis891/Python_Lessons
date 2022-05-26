"""Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N."""

result_list = []

while True:
    try:
        number = int(input("Введите число: "))
        for i in range(1, number + 1):
            if i == 1:
                result_list.append(i)
            else:
                result_list.append(result_list[i - 2] * i)
        break
    except ValueError:
        print("Вы ввели неверные данные")

print(result_list)
