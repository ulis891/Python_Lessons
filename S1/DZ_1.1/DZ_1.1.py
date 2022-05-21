# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.


while True:
    try:
        day_number = int(input("Введите цифру, обозначающую день недели: "))
        if day_number in range(1, 6):
            print("Работать!!!!")
        elif day_number in range(6, 8):
            print("ДА! Выходной!")
        else:
            print("Нет такого дня недели")
        break
    except ValueError:
        print("Вы ввели не число!")
